#!/usr/bin/env bash
#
# Orchestrator — รันหลังจาก brief .md ของวันนั้นถูกเขียนเสร็จแล้ว
# ใช้งาน: bash scripts/run_daily.sh [YY-MM-DD]
#
# ลำดับ:
#   1. tts.py              — generate MP3 + per-episode JSON
#   2. update_index.py     — rebuild audio/index.json (source of truth ของ feed)
#   3. git commit + push   — ส่งไฟล์ขึ้น GitHub (feed อ่านผ่าน raw.githubusercontent.com)
#   4. push_telegram.py    — ส่งข้อความ + audio เข้า Telegram
#
# ถ้าขั้นไหนล้ม script จะหยุดและ exit non-zero
#
# Env flags:
#   SKIP_TELEGRAM=1   ข้าม Telegram push
#   SKIP_GIT=1        ข้าม git commit/push (เช่น ตอน dev ในเครื่อง)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESEARCH_ROOT="$(dirname "$SCRIPT_DIR")"
DATE_SLUG="${1:-$(TZ=Asia/Bangkok date +%y-%m-%d)}"

cd "$RESEARCH_ROOT"

echo "=== run_daily.sh for $DATE_SLUG ==="

# 1. TTS
echo "[1/4] TTS..."
python3 "$SCRIPT_DIR/tts.py" --date "$DATE_SLUG"

# 2. Rebuild index
echo "[2/4] Rebuild audio/index.json..."
python3 "$SCRIPT_DIR/update_index.py"

# 3. Commit + push (so feed สามารถ fetch ผ่าน raw.githubusercontent.com ได้)
if [ -n "${SKIP_GIT:-}" ]; then
  echo "[3/4] SKIP_GIT set — ข้าม git push"
else
  echo "[3/4] git commit + push..."
  git add -A "news/${DATE_SLUG}"*.md "audio/${DATE_SLUG}".* "audio/index.json"
  if git diff --cached --quiet; then
    echo "      (ไม่มีอะไรใหม่ — ข้าม commit)"
  else
    git commit -m "daily: ${DATE_SLUG}" \
      -m "$(ls "news/${DATE_SLUG}"-*.md 2>/dev/null | grep -v -- '-index\.md$' | wc -l | awk '{print $1" brief(s) + audio"}')"
    # ถ้ายังไม่ตั้ง remote หรือ push ไม่สำเร็จ ก็แค่เตือน ไม่หยุด pipeline
    if git remote | grep -q .; then
      git push || echo "      [warn] git push ล้มเหลว — commit ยังอยู่ local"
    else
      echo "      [warn] ยังไม่ได้ตั้ง git remote — commit อยู่ local เท่านั้น"
    fi
  fi
fi

# 4. Telegram push
if [ -n "${SKIP_TELEGRAM:-}" ]; then
  echo "[4/4] SKIP_TELEGRAM set — ข้าม Telegram"
else
  echo "[4/4] Push Telegram..."
  python3 "$SCRIPT_DIR/push_telegram.py" --date "$DATE_SLUG"
fi

echo "=== done ==="
