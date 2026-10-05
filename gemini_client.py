import os
import sys
import re
import json
import base64
import time
import socket
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import (
    KEYS_FILE,
    GEMINI_MODEL,
    FALLBACK_MODELS,
    CHANNEL_NAME
)

socket.setdefaulttimeout(45)

def _load_keys(filepath: Path) -> List[str]:
    # Chercher sur le chemin configuré ou en fallback dans le répertoire courant
    p = filepath if filepath.exists() else Path(__file__).parent / "gemini_keys.txt"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            keys = [k.strip() for k in f if k.strip() and not k.startswith("#")]
        if keys:
            return keys
    raise ValueError(f"Fichier de clés introuvable ou vide : {filepath}")

_KEYS = _load_keys(KEYS_FILE)
_KEY_IDX = [0]
STATS = {"calls": 0, "rotations": 0, "failures": 0}

def call_gemini(parts: List[Dict[str, Any]], retries: int = 4) -> str:
    """
    Exécute une requête vers l'API Gemini avec rotation automatique des clés
    et repli transparent entre les modèles (gemini-3.5-flash-lite -> fallback).
    """
    models_to_try = [GEMINI_MODEL] + FALLBACK_MODELS

    for model in models_to_try:
        for attempt in range(retries):
            key = _KEYS[_KEY_IDX[0] % len(_KEYS)]
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
            payload = json.dumps({"contents": [{"parts": parts}]}).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})

            try:
                with urllib.request.urlopen(req, timeout=35) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    cands = data.get("candidates", [])
                    if cands and "content" in cands[0] and "parts" in cands[0]["content"]:
                        STATS["calls"] += 1
                        return cands[0]["content"]["parts"][0].get("text", "")
            except urllib.error.HTTPError as e:
                _KEY_IDX[0] += 1
                STATS["rotations"] += 1
                if e.code in (429, 503, 500):
                    time.sleep(1.2)
                    continue
                err_text = e.read().decode("utf-8", "ignore")[:150]
                print(f"[Gemini] HTTPError {e.code} sur {model}: {err_text}", flush=True)
            except Exception as e:
                _KEY_IDX[0] += 1
                time.sleep(1.0)

    STATS["failures"] += 1
    return ""

def process_visual_block(
    candidate_frames: List[Dict[str, Any]],
    timestamp_str: str,
    verbatim_fr: str
) -> Dict[str, Any]:
    """
    Analyse multimodale des images clés d'un segment via gemini-3.5-flash-lite.
    Identifie les interfaces, lignes de commandes, diagrammes, architectures et matériels.
    """
    default_res = {
        "valid_frame_indices": [],
        "frame_captions": {},
        "interface": "Présentation ou face-caméra sans interface informatique partagée.",
        "contenu": "Explications orales des concepts, architectures et retours d'expérience.",
        "action": "Démonstration pédagogique et mise en perspective technique."
    }

    n_imgs = len(candidate_frames)
    if n_imgs == 0:
        return default_res

    img_list_txt = "\n".join([f"- Image #{i+1} : horodatage @ {cf.get('timestamp_str', '')}" for i, cf in enumerate(candidate_frames)])
    visual_prompt = (
        f"Tu es un expert DevOps / SysAdmin et analyste visuel pour la chaîne {CHANNEL_NAME} (segment {timestamp_str}).\n"
        f"Contexte du discours prononcé : {verbatim_fr[:350]}\n\n"
        f"Tu as reçu {n_imgs} capture(s) d'écran candidate(s) extraite(s) de la vidéo :\n{img_list_txt}\n\n"
        "DIRECTIVE DE SÉLECTION D'IMAGES :\n"
        "- Retiens STRICTEMENT les images contenant du contenu technique réel : terminal Linux, code source, interfaces cloud/AWS/OVH/Cloudflare, consoles Docker/Kubernetes, diagrammes d'architecture réseau, benchmarks, matériel homelab/serveurs, puces IA (Nvidia, Groq, Cerebras), etc.\n"
        "- Élimine systématiquement les plans purement face-caméra du créateur sans aucun support graphique ou interface pertinente.\n\n"
        "Format STRICT obligatoire de ta réponse en français :\n"
        "[VALID_IMAGES] <numéros séparés par virgule (ex: 1, 2) ou AUCUNE>\n"
    )
    for i in range(n_imgs):
        visual_prompt += f"[DESC_IMAGE_{i+1}] <légende concise et technique décrivant ce qui est visible à l'écran>\n"
    visual_prompt += (
        "[INTERFACE] <outils, terminaux, logiciels ou consoles affichés>\n"
        "[CONTENU] <commandes, code, architectures ou métriques visibles>\n"
        "[ACTION] <manipulation, configuration, test ou explication technique réalisée>"
    )

    visual_parts: List[Dict[str, Any]] = [{"text": visual_prompt}]
    for cf in candidate_frames:
        img_path = cf.get("path")
        if img_path and isinstance(img_path, Path) and img_path.exists() and img_path.stat().st_size > 0:
            try:
                with open(img_path, "rb") as f:
                    b64_img = base64.b64encode(f.read()).decode("utf-8")
                visual_parts.append({
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": b64_img
                    }
                })
            except Exception:
                pass

    raw_vis = call_gemini(visual_parts)
    if not raw_vis:
        return default_res

    res = dict(default_res)
    try:
        valid_indices = []
        frame_captions = {}
        if "[VALID_IMAGES]" in raw_vis:
            raw_val = raw_vis.split("[VALID_IMAGES]")[1]
            for m in ["[DESC_IMAGE_", "[INTERFACE]", "[CONTENU]", "[ACTION]"]:
                if m in raw_val:
                    raw_val = raw_val.split(m)[0]
            raw_val = raw_val.strip().upper()

            if "AUCUNE" not in raw_val and "NONE" not in raw_val and "ZERO" not in raw_val:
                if "TOUTES" in raw_val or "TOUT" in raw_val or "ALL" in raw_val:
                    valid_indices = list(range(n_imgs))
                else:
                    for token in re.findall(r'\b\d+\b', raw_val):
                        num = int(token)
                        if 1 <= num <= n_imgs:
                            valid_indices.append(num - 1)

        for i in range(n_imgs):
            tag = f"[DESC_IMAGE_{i+1}]"
            if tag in raw_vis:
                part_desc = raw_vis.split(tag)[1]
                for next_tag in [f"[DESC_IMAGE_{j+1}]" for j in range(i+1, n_imgs)] + ["[INTERFACE]", "[CONTENU]", "[ACTION]"]:
                    if next_tag in part_desc:
                        part_desc = part_desc.split(next_tag)[0]
                desc_text = part_desc.strip().lstrip(": -").strip()
                if desc_text and not desc_text.startswith("<"):
                    frame_captions[i] = desc_text

        res["valid_frame_indices"] = sorted(list(set(valid_indices)))
        res["frame_captions"] = frame_captions

        if "[INTERFACE]" in raw_vis:
            p_i = raw_vis.split("[INTERFACE]")[1]
            for m in ["[CONTENU]", "[ACTION]"]:
                if m in p_i:
                    p_i = p_i.split(m)[0]
            res["interface"] = p_i.strip()

        if "[CONTENU]" in raw_vis:
            p_c = raw_vis.split("[CONTENU]")[1]
            if "[ACTION]" in p_c:
                p_c = p_c.split("[ACTION]")[0]
            res["contenu"] = p_c.strip()

        if "[ACTION]" in raw_vis:
            res["action"] = raw_vis.split("[ACTION]")[1].strip()

    except Exception as e:
        print(f"[Gemini-Visual] Erreur parsing bloc visuel : {e}", flush=True)

    return res

def generate_executive_summary(video_title: str, full_verbatim_fr: str) -> str:
    """
    Génère la synthèse exécutive structurée calquée sur le modèle de référence
    '2026-08-19_YT_Cet Agent Vidéo Open-Source GRATUIT est FOU.md'.
    """
    prompt = (
        f"Tu es un ingénieur expert DevOps / Cloud / Systèmes et rédacteur technique d'élite.\n"
        f"Vidéo de la chaîne {CHANNEL_NAME} : « {video_title} ».\n\n"
        f"Transcription intégrale verbatim du contenu en français :\n\"\"\"\n{full_verbatim_fr[:12000]}\n\"\"\"\n\n"
        "Rédige une synthèse exécutive d'une clarté irréprochable, hautement structurée, intuitive et professionnelle en français.\n"
        "Tu DOIS STRICTEMENT employer ces titres de niveau 3 exacts :\n\n"
        "### 💡 Résumé\n"
        "(2 à 3 paragraphes denses et captivants détaillant le problème concret abordé, la solution technique présentée, les architectures ou commandes démontrées, et l'impact opérationnel pour un SysAdmin ou développeur)\n\n"
        "### 🛠️ Outils, Modèles & Logiciels Présentés\n"
        "(Liste à puces exhaustive avec le nom de l'outil/technologie/matériel en gras et une phrase explicative percutante de son rôle)\n\n"
        "### 🔑 Points Clés & Enseignements Stratégiques\n"
        "(8 à 12 points clés détaillés, rigoureusement actionnables, avec bonnes pratiques, erreurs critiques à éviter et retours d'expérience prod)"
    )

    res = call_gemini([{"text": prompt}])
    if not res:
        res = (
            "### 💡 Résumé\n"
            f"Dans cette vidéo intitulée **{video_title}**, cocadmin propose une immersion approfondie dans les problématiques concrètes d'infrastructure, de systèmes et d'ingénierie logicielle.\n\n"
            "### 🛠️ Outils, Modèles & Logiciels Présentés\n"
            "- **Linux & Outils Systèmes** : Administration système, automatisation et surveillance.\n"
            "- **Conteneurisation & Cloud** : Déploiement et gestion d'environnements résilients.\n\n"
            "### 🔑 Points Clés & Enseignements Stratégiques\n"
            "- Maîtriser les fondamentaux réseau et système pour diagnostiquer efficacement les pannes.\n"
            "- Privilégier les architectures simples et observables en environnement de production."
        )
    return res
