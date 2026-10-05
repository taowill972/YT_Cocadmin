from pathlib import Path

# Chemins d'accès système
BASE_DIR = Path("/root/YT_Cocadmin")
REPO_DIR = BASE_DIR
TRANSCRIPTS_DIR = BASE_DIR / "YT_Cocadmin_Transcript"
CATALOG_FILE = BASE_DIR / "catalog.json"
STATE_FILE = BASE_DIR / "state.json"
WORK_DIR = Path("/tmp/yt_cocadmin_work")
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
LOG_FILE = Path("/var/log/yt_cocadmin.log")

# Identification de la chaîne YouTube
CHANNEL_ID = "UCVRJ6D343dX-x730MRP8tNw"
CHANNEL_NAME = "cocadmin"
CHANNEL_HANDLE = "@cocadmin"
CHANNEL_URL = "https://www.youtube.com/@cocadmin"
RSS_FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
CHANNEL_DOMAIN = "DevOps, SysAdmin, Linux, Cloud, Docker, Kubernetes, Homelab, Bases de Données, Architecture Réseau, IA & Hardware"

# Modèles IA (Strictement conformes aux consignes utilisateur)
WHISPER_MODEL = "large-v3-turbo"
GEMINI_MODEL = "gemini-3.5-flash-lite"
FALLBACK_MODELS = ["gemini-2.5-flash-lite", "gemini-2.5-flash"]
MODEL_SIGNATURE = f"whisper-v3-large-turbo+{GEMINI_MODEL}"

# Clés API & Réseau
KEYS_FILE = BASE_DIR / "gemini_keys.txt"
PROXY = "socks5://127.0.0.1:4001"
PLAYER_CLIENT = "android"

# Paramètres du traitement
BATCH_SIZE = 5               # Lot de 5 vidéos toutes les 12h
MAX_BLOCK_DURATION = 32.0    # Secondes max par bloc temporel
MIN_BLOCK_DURATION = 18.0    # Secondes min par bloc temporel
FRAME_DIFF_THRESHOLD = 15.0  # Seuil de différence MSE / Pillow pour screenshot clé
FRAME_MAX_WIDTH = 1280       # Résolution max des screenshots (720p)

# Création proactive des répertoires si exécuté localement ou sur VPS
BASE_DIR.mkdir(parents=True, exist_ok=True)
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
WORK_DIR.mkdir(parents=True, exist_ok=True)
