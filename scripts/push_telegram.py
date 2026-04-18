#!/usr/bin/env python3
"""
Push a daily brief to Telegram as message + audio.

Usage:
    python scripts/push_telegram.py --date 26-04-18
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    sys.exit("ต้อง: pip install requests python-dotenv --break-system-packages")

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


def parse_index(md_text: str) -> dict:
    """Extract theme + item lines from the index .md."""
    lines = md_text.splitlines()
    theme = ""
    items = []
    for i, line in enumerate(lines):
        if line.startswith("**Theme"):
            theme = line.split(":", 1)[1].strip(" *")
        # items look like: **[001] Title** — body
        m = re.match(r"\*\*\[\d+\]\s*([^*]+?)\*\*\s*—\s*(.+)", line)
        if m:
            items.append({"title": m.group(1).strip(), "summary": m.group(2).strip()})
    return {"theme": theme, "items": items}


def build_message(date_slug: str) -> str:
    index_path = ROOT / "news" / f"{date_slug}-index.md"
    if not index_path.exists():
        sys.exit(f"ไม่เจอ index: {index_path}")
    idx = parse_index(index_path.read_text(encoding="utf-8"))
    yy, mm, dd = date_slug.split("-")
    lines = [
        f"<b>Daily AI Brief — 20{yy}-{mm}-{dd}</b>",
        "",
    ]
    if idx["theme"]:
        lines.append(f"<i>{idx['theme']}</i>")
        lines.append("")
    for i, item in enumerate(idx["items"], 1):
        lines.append(f"<b>{i}.</b> {item['title']}")
        lines.append(f"   {item['summary']}")
        lines.append("")
    lines.append(f"🎧 podcast: https://enabridge.ai/research")
    return "\n".join(lines)


def send_message(token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = requests.post(url, json={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }, timeout=15)
    r.raise_for_status()
    return r.json()


def send_audio(token: str, chat_id: str, audio_path: Path, caption: str):
    url = f"https://api.telegram.org/bot{token}/sendAudio"
    with audio_path.open("rb") as f:
        r = requests.post(url, data={
            "chat_id": chat_id,
            "caption": caption,
            "parse_mode": "HTML",
            "title": audio_path.stem,
            "performer": "Enabridge Daily AI Brief",
        }, files={"audio": (audio_path.name, f, "audio/mpeg")}, timeout=120)
    r.raise_for_status()
    return r.json()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YY-MM-DD")
    ap.add_argument("--skip-audio", action="store_true", help="ส่งแค่ข้อความ ไม่ส่ง MP3")
    args = ap.parse_args()

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token:
        sys.exit("ไม่เจอ TELEGRAM_BOT_TOKEN ใน .env")
    if not chat_id:
        sys.exit("ไม่เจอ TELEGRAM_CHAT_ID ใน .env — รัน scripts/telegram_setup.py ก่อน")

    msg = build_message(args.date)
    print("[telegram] ส่ง message...")
    send_message(token, chat_id, msg)

    audio_path = ROOT / "audio" / f"{args.date}.mp3"
    if args.skip_audio or not audio_path.exists():
        print(f"[telegram] skip audio ({'flag' if args.skip_audio else 'ไม่มีไฟล์'})")
    else:
        print(f"[telegram] ส่ง audio {audio_path.name}...")
        send_audio(token, chat_id, audio_path, caption=f"🎧 {args.date} · ฟังในแอพ Telegram ได้เลย")
    print("[telegram] เสร็จ")


if __name__ == "__main__":
    main()
