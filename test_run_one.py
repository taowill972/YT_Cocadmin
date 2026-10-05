import json
from pipeline import process_single_video
from git_manager import update_readme_index, commit_and_push_repo

vid_id = "NChuyBBcH64"
title = "Pourquoi Nvidia à peur de ces nouvelles puces AI"

print(f"=== Lancement du test unitaire sur la vidéo {vid_id} ===")
res = process_single_video(vid_id, catalog_title=title)

with open("/root/YT_Cocadmin/state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

if vid_id not in state["processed_ids"]:
    state["processed_ids"].append(vid_id)
    state["processed_videos"].append(res)
    state["completed_count"] = len(state["processed_ids"])

with open("/root/YT_Cocadmin/state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

update_readme_index(state["processed_videos"], total_catalog_count=142)
commit_and_push_repo(f"feat: transcription multimodale {vid_id} - {title[:50]}")
print("=== Test unitaire complet terminé avec succès ! ===")
