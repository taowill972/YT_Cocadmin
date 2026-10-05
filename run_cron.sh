#!/bin/bash
set -e

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
export HOME="/root"

cd /root/YT_Cocadmin

echo "=== [$(date -u +"%Y-%m-%dT%H:%M:%SZ")] Lancement Batch 12h YT_Cocadmin ===" >> /var/log/yt_cocadmin.log
/usr/bin/python3 /root/YT_Cocadmin/batch_runner.py >> /var/log/yt_cocadmin.log 2>&1
echo "=== [$(date -u +"%Y-%m-%dT%H:%M:%SZ")] Fin Batch 12h YT_Cocadmin ===" >> /var/log/yt_cocadmin.log
