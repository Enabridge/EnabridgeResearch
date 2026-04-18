#!/usr/bin/env bash
#
# Orchestrator — หลังจาก scheduled task เขียน brief .md เสร็จ
# รัน: bash scripts/run_daily.sh [YY-MM-DD]
#
# ลำดับ:
#   1. tts.py     — generate MP3 + metadata
#   2. คัดลอก MP3 + JSON ไป enabridge-site/public/research/audio/ (สำหรับ feed)
#   3. push_telegram.py — ส่งข้อความ + audio
#
# ถ้าขั้นไหนล้ม script จะหยุดและ exit non-zero

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESEARCH_ROOT="$(dirname "$SCRIPT_DIR")"
SITE_ROOT="$(cd "$RESEARCH_ROOT/.." && pwd)/enabridge-site"

DATE_SLUG="${1:-$(date +%y-%m-%d)}"

echo "=== run_daily.sh for $DATE_SLUG ==="

# 1. TTS
echo "[1/3] TTS..."
python3 "$SCRIPT_DIR/tts.py" --date "$DATE_SLUG"

# 2. Publish to site
echo "[2/3] Copy audio → enabridge-site/public/research/audio/..."
SITE_AUDIO="$SITE_ROOT/public/research/audio"
mkdir -p "$SITE_AUDIO"
cp -f "$RESEARCH_ROOT/audio/$DATE_SLUG.mp3"  "$SITE_AUDIO/"
cp -f "$RESEARCH_ROOT/audio/$DATE_SLUG.json" "$SITE_AUDIO/"
echo "      → $SITE_AUDIO/$DATE_SLUG.mp3"

# 3. Telegram push
if [ -n "${SKIP_TELEGRAM:-}" ]; then
  echo "[3/3] SKIP_TELEGRAM set — ข้าม Telegram"
else
  echo "[3/3] Push Telegram..."
  python3 "$SCRIPT_DIR/push_telegram.py" --date "$DATE_SLUG"
fi

echo "=== done ==="
