#!/usr/bin/env bash
#
# Helper สำหรับ routine — สร้าง branch + push ของวัน
# ใช้งาน: bash scripts/write_briefs.sh [YY-MM-DD]
#
# ก่อนเรียกสคริปต์นี้ routine ต้องเขียน news/YY-MM-DD-*.md เรียบร้อยแล้ว
# สคริปต์จะ checkout feature branch + commit + push
# GHA workflow `daily-branch-build.yml` จะรับช่วงต่อ (gen images → TTS → index → PR → Telegram)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
DATE_SLUG="${1:-$(date +%y-%m-%d)}"
BRANCH="daily/${DATE_SLUG}"

cd "$REPO_ROOT"

echo "=== write_briefs.sh for $DATE_SLUG (branch: $BRANCH) ==="

# ตรวจว่ามี brief ของวันนี้แล้วยัง
COUNT=$(ls "news/${DATE_SLUG}"-*.md 2>/dev/null | grep -v -- '-index\.md$' | wc -l | tr -d ' ')
if [ "$COUNT" = "0" ]; then
  echo "[ERR] ไม่เจอ brief สำหรับ ${DATE_SLUG} — เขียน news/${DATE_SLUG}-NNN-*.md ก่อน"
  exit 1
fi
echo "[ok] พบ ${COUNT} brief(s)"

# Checkout branch (สร้างใหม่หรือ reset ถ้ามีอยู่แล้ว)
if git show-ref --verify --quiet "refs/heads/${BRANCH}"; then
  echo "[git] branch ${BRANCH} มีอยู่แล้ว — checkout + reset ไป main"
  git checkout "$BRANCH"
  git reset --hard origin/main 2>/dev/null || git reset --hard main
else
  echo "[git] สร้าง branch ${BRANCH} จาก main"
  git fetch origin main 2>/dev/null || true
  git checkout -b "$BRANCH" origin/main 2>/dev/null || git checkout -b "$BRANCH" main
fi

# Stage + commit แค่ news/ ของวันนี้
git add "news/${DATE_SLUG}"*.md
if git diff --cached --quiet; then
  echo "[git] ไม่มีอะไรใหม่ — ข้าม commit"
else
  git commit -m "daily: ${DATE_SLUG} briefs (${COUNT} stories)"
fi

# Push (force-with-lease — กัน race condition)
echo "[git] push ${BRANCH}..."
git push --force-with-lease -u origin "$BRANCH"

echo "=== done ==="
echo "GHA workflow จะรัน: gen images → TTS → update index → open PR → ส่ง Telegram"
echo "ดูสถานะ: https://github.com/Enabridge/EnabridgeResearch/actions"
