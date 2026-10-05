import os
import sys
import json
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, List

from config import (
    BASE_DIR,
    REPO_DIR,
    CATALOG_FILE,
    STATE_FILE,
    BATCH_SIZE
)
from pipeline import process_single_video
from git_manager import update_readme_index, commit_and_push_repo

def disable_cron_batch_job() -> bool:
    """
    Retire automatiquement la routine de crontab toutes les 12h
    lorsque toutes les vidéos de la chaîne ont été traitées.
    L'écoute passive reste quant à elle active en tâche de fond.
    """
    try:
        res = subprocess.run(["crontab", "-l"], capture_output=True, text=True, check=True)
        lines = res.stdout.splitlines()
        new_lines = [l for l in lines if "yt_cocadmin" not in l and "YT_Cocadmin/run_cron.sh" not in l]
        if len(new_lines) != len(lines):
            new_cron = "\n".join(new_lines) + "\n"
            p = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE, text=True)
            p.communicate(new_cron)
            print("[BatchRunner] 🛑 Crontab 12h retiré avec succès : routine arrêtée suite à la complétion intégrale.", flush=True)
            return True
        return False
    except Exception as e:
        print(f"[BatchRunner] Erreur lors de la désactivation du cron : {e}", flush=True)
        return False

def load_state() -> Dict[str, Any]:
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "processed_ids": [],
        "processed_videos": [],
        "last_run_timestamp": None,
        "completed_count": 0,
        "total_catalog_count": 142,
        "status": "idle"
    }

def save_state(state: Dict[str, Any]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def main():
    print(f"\n===================================================================", flush=True)
    print(f"🔄 [BatchRunner] Lancement de la routine 12h (Lot de {BATCH_SIZE} vidéos)", flush=True)
    print(f"⏱️ Horodatage : {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}", flush=True)
    print(f"===================================================================", flush=True)

    if not CATALOG_FILE.exists():
        print(f"[BatchRunner] ❌ Catalogue introuvable : {CATALOG_FILE}", flush=True)
        sys.exit(1)

    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        catalog_entries = json.load(f)

    total_catalog = len(catalog_entries)
    print(f"[BatchRunner] Catalogue global : {total_catalog} vidéos.", flush=True)

    state = load_state()
    state["total_catalog_count"] = total_catalog
    processed_ids_set = set(state.get("processed_ids", []))

    # Filtrer les vidéos non encore traitées (classées de la plus récente à la plus ancienne)
    pending_videos = [v for v in catalog_entries if v.get("id") and v.get("id") not in processed_ids_set]
    print(f"[BatchRunner] Vidéos restantes à transcrire : {len(pending_videos)} / {total_catalog}", flush=True)

    if len(pending_videos) == 0:
        print("\n🎉 [BatchRunner] TOUTES LES VIDÉOS DE LA CHAÎNE ONT ÉTÉ TRAITÉES !", flush=True)
        print("🛑 Arrêt définitif de l'automatisation 12h. Seule l'écoute continue des nouvelles publications est conservée.", flush=True)
        state["status"] = "ALL_VIDEOS_PROCESSED_AUTOMATION_COMPLETED"
        state["completed_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        save_state(state)
        disable_cron_batch_job()
        sys.exit(0)

    # Sélectionner le lot de 5 vidéos
    current_batch = pending_videos[:BATCH_SIZE]
    print(f"[BatchRunner] Démarrage du lot de {len(current_batch)} vidéo(s) :", flush=True)
    for i, v in enumerate(current_batch):
        print(f"  [{i+1}/{len(current_batch)}] {v.get('id')} — {v.get('title')} ({v.get('upload_date')})", flush=True)

    batch_success_count = 0
    for v in current_batch:
        vid_id = v.get("id")
        try:
            res = process_single_video(vid_id, catalog_title=v.get("title"))
            state["processed_ids"].append(vid_id)
            state["processed_videos"].append(res)
            state["completed_count"] = len(state["processed_ids"])
            save_state(state)

            update_readme_index(state["processed_videos"], total_catalog_count=total_catalog)
            commit_and_push_repo(f"feat: transcription multimodale {vid_id} - {res.get('title')[:50]}")
            batch_success_count += 1
        except Exception as e:
            print(f"[BatchRunner] ❌ Erreur sur la vidéo {vid_id} : {e}", flush=True)

    state["last_run_timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    save_state(state)

    print(f"\n===================================================================", flush=True)
    print(f"✅ [BatchRunner] Lot terminé : {batch_success_count}/{len(current_batch)} traitée(s) avec succès.", flush=True)
    print(f"📊 Total cumulé : {len(state['processed_ids'])} / {total_catalog} vidéos.", flush=True)
    print(f"===================================================================", flush=True)

    # Si ce lot a terminé la dernière vidéo de la chaîne
    if len(state["processed_ids"]) >= total_catalog:
        print("\n🎉 [BatchRunner] Dernière vidéo atteinte ! Désactivation de la routine crontab 12h.", flush=True)
        state["status"] = "ALL_VIDEOS_PROCESSED_AUTOMATION_COMPLETED"
        save_state(state)
        disable_cron_batch_job()

if __name__ == "__main__":
    main()
