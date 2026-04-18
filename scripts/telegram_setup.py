#!/usr/bin/env python3
"""
One-time setup: detect your Telegram chat_id by polling getUpdates.

Usage:
    1. Open Telegram, find your bot (the one you got the token for), send /start
    2. Run: python scripts/telegram_setup.py
    3. Copy the chat_id it prints into .env as TELEGRAM_CHAT_ID
"""
import os
import sys
from pathlib import Path

try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    sys.exit("ต้อง: pip install requests python-dotenv --break-system-packages")

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

token = os.environ.get("TELEGRAM_BOT_TOKEN")
if not token:
    sys.exit("ไม่เจอ TELEGRAM_BOT_TOKEN ใน .env")

print("[setup] ดึง updates จาก Telegram...")
r = requests.get(f"https://api.telegram.org/bot{token}/getUpdates", timeout=10)
r.raise_for_status()
data = r.json()

if not data.get("ok"):
    sys.exit(f"Telegram error: {data}")

results = data.get("result", [])
if not results:
    print("ไม่เจอ update — ตรวจว่าได้ /start bot ใน Telegram แล้วหรือยัง?")
    print("Steps:")
    print("  1. Open Telegram → ค้นหา bot ที่เพิ่งสร้าง (ใช้ username ที่ @BotFather ให้)")
    print("  2. กด Start หรือพิมพ์ /start")
    print("  3. รัน script นี้อีกครั้ง")
    sys.exit(1)

chats = {}
for upd in results:
    msg = upd.get("message") or upd.get("channel_post") or {}
    chat = msg.get("chat")
    if chat:
        chats[chat["id"]] = chat

print(f"[setup] เจอ {len(chats)} chat:")
for cid, chat in chats.items():
    name = chat.get("first_name") or chat.get("title") or chat.get("username") or "?"
    ctype = chat.get("type")
    print(f"  chat_id={cid}  type={ctype}  name={name}")

if len(chats) == 1:
    cid = next(iter(chats))
    print(f"\n→ copy ไปใส่ .env:  TELEGRAM_CHAT_ID={cid}")

# Offer to update .env automatically
print("\nต้องการให้ update .env ให้เลยไหม? (y/n)")
try:
    ans = input().strip().lower()
except EOFError:
    ans = "n"
if ans == "y" and len(chats) == 1:
    cid = next(iter(chats))
    env_path = ROOT / ".env"
    text = env_path.read_text(encoding="utf-8")
    if "TELEGRAM_CHAT_ID=" in text:
        import re
        text = re.sub(r"TELEGRAM_CHAT_ID=.*", f"TELEGRAM_CHAT_ID={cid}", text)
    else:
        text += f"\nTELEGRAM_CHAT_ID={cid}\n"
    env_path.write_text(text, encoding="utf-8")
    print(f"[setup] .env updated: TELEGRAM_CHAT_ID={cid}")
