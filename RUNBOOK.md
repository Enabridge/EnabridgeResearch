# Runbook — Phase 2 first-time setup

> ทำตาม 4 ขั้น ~10 นาที จะ end-to-end pipeline ทำงาน: brief → audio → podcast feed → Telegram

## 0. Prerequisite

Credentials อยู่ใน `.env` (เรียบร้อยแล้ว). ติดตั้ง Python deps:

```bash
cd ~/ws/company/enabridge-research
pip3 install openai python-dotenv requests 'httpx[socks]' --break-system-packages
```

## 1. เชื่อม Telegram bot

```bash
# 1a. เปิด Telegram, search bot ของคุณ (username ที่ @BotFather ให้), กด Start หรือพิมพ์ /start
# 1b. รัน:
python3 scripts/telegram_setup.py
```

Script จะแสดง chat_id ที่เจอ, ถามว่า update .env ให้เลยไหม → ตอบ `y`

## 2. ทดสอบ TTS + Telegram ด้วย brief ของเมื่อวาน

```bash
bash scripts/run_daily.sh 26-04-18
```

ถ้าทุกอย่างผ่าน:
- `audio/26-04-18.mp3` จะเกิด (~3 MB)
- Copy ไปที่ `enabridge-site/public/research/audio/`
- Telegram message + voice file จะเด้งเข้ามือถือคุณ

ถ้าพังที่ TTS → ดู `audio/26-04-18.txt` ก่อน (script ยังอยู่), ตรวจ OpenAI key
ถ้าพังที่ Telegram → ตรวจ TELEGRAM_CHAT_ID ใน .env

## 3. Deploy enabridge-site ให้ feed ใช้งานได้

```bash
cd ~/ws/company/enabridge-site
npm run build   # ตรวจว่า route ใหม่ build ผ่าน
# ถ้า build ผ่าน: deploy ตามปกติ (Vercel auto จาก git push, หรือ vercel --prod)
```

เสร็จแล้ว test:
- https://enabridge.ai/research — landing page พร้อม audio player
- https://enabridge.ai/research/feed.xml — RSS XML

## 4. Subscribe podcast

- **Apple Podcasts**: Library → Follow Show by URL → paste `https://enabridge.ai/research/feed.xml`
- **Spotify**: ต้อง submit feed ผ่าน [Spotify for Podcasters](https://podcasters.spotify.com/) (ครั้งเดียว, รอ review ~1-2 วัน)
- **Overcast / Pocket Casts / ฯลฯ**: กด "Add by URL" แล้ววาง feed URL

## 5. Pre-approve tools ใน scheduled task

เปิด Cowork → Sidebar "Scheduled" → task `enabridge-daily-research` → กด "Run now"

ครั้งแรกจะ prompt ขอ permission (Bash, WebSearch, ฯลฯ) — approve ให้หมด เพื่อ run ต่อ ๆ ไปไม่ติดขัด

## Troubleshooting

| ปัญหา | ที่ดู |
|---|---|
| MP3 เป็น 0 ไบต์ | OpenAI key ผิด หรือ credit หมด — ดู error ใน terminal |
| Telegram ไม่ส่ง | `python3 scripts/telegram_setup.py` อีกครั้ง, ตรวจว่า chat ยังเปิดอยู่ |
| Feed ว่าง | MP3 ยังไม่ถูก copy ไป `enabridge-site/public/research/audio/` — ตรวจ path ใน `run_daily.sh` |
| Feed โหลดไม่ได้ | Deploy enabridge-site ยัง? ตรวจ vercel log |
| Scheduled task ไม่รัน | Cowork ต้องเปิดตอน 07:00 — ถ้าไม่สะดวก ย้ายไป GitHub Actions (ดู PHASE2-PLAN.md) |

## หลัง setup เสร็จ — rotate credentials

⚠️ Key ทั้ง 2 ตัว (OpenAI + Telegram) ถูก paste ใน chat — หลัง pipeline ทำงาน please:
1. OpenAI: https://platform.openai.com/api-keys → revoke key เดิม + create ใหม่ → update `.env`
2. Telegram: คุย `@BotFather` → `/mybots` → เลือก bot → "API Token" → "Revoke current token"  → update `.env`
