# Migration — Cowork local task → Claude Code web routine (cloud)

> เป้าหมาย: ย้าย daily pipeline ไปรันบน cloud เพื่อให้ไม่ต้องเปิด Mac ค้างทุกเช้า
> สถานะ Cowork task เดิม: **เก็บไว้เป็น backup** (ไม่ต้อง delete)
>
> สิ่งที่ Claude เตรียมให้แล้ว:
> - `git init` + first commit (branch `main`, hash `91da919`)
> - `scripts/update_index.py` — สร้าง `audio/index.json` ให้ feed อ่าน
> - `scripts/run_daily.sh` ปรับเป็น cloud mode (TTS → index → git push → Telegram)
> - `enabridge-site` routes (`/research`, `/research/feed.xml`) ดึงข้อมูลจาก `raw.githubusercontent.com` แทนที่จะอ่าน filesystem
>
> สิ่งที่ต้องไปคลิกเองใน UI / terminal: ด้านล่างนี้

---

## Step 1 — push repo ขึ้น GitHub (public)

```bash
cd ~/ws/company/enabridge-research

# ใช้ gh CLI ถ้ามี — จะ create + set remote + push ให้ครบรอบเดียว
gh repo create enabridge-research --public --source=. --remote=origin --push

# หรือถ้าไม่มี gh: ไปสร้าง repo เปล่า ๆ ที่ github.com/new ชื่อ "enabridge-research" (public, ไม่ต้อง README)
# แล้ว:
git remote add origin git@github.com:<YOUR-USER>/enabridge-research.git
git push -u origin main
```

หลัง push:
- verify `audio/26-04-18.mp3` โหลดผ่าน raw ได้:
  `curl -I https://raw.githubusercontent.com/<YOUR-USER>/enabridge-research/main/audio/index.json`

> ⚠️ `.env` ถูก gitignore แล้ว — ตรวจแน่ใจว่าไม่มีใน commit:
> `git log --all --name-only | grep -E '^\.env$' || echo "OK — no .env in git"`

---

## Step 2 — set env vars บน enabridge-site (Railway)

เปิด Railway dashboard → project `enabridge-site` → service → **Variables** tab → Add:

| Key | Value |
|---|---|
| `GITHUB_OWNER` | `Enabridge` (ต้องเป๊ะ — case-sensitive เพราะเอาไปต่อเป็น URL ตรง ๆ) |
| `GITHUB_REPO` | `EnabridgeResearch` (ต้องเป๊ะเช่นกัน) |
| `GITHUB_BRANCH` | `main` |

Railway จะ redeploy อัตโนมัติหลัง save (หรือกด Deploy manually)

Verify:
- `curl https://enabridge.ai/research/feed.xml | head -40` ต้องเห็น `<item>` ของ `26-04-18`
- เปิด `https://enabridge.ai/research` ใน browser → เห็น audio player
- ถ้า feed ว่าง: ตรวจ Railway logs ว่า `[feed] index.json fetch failed` หรือเปล่า — มักเป็น typo ชื่อ owner/repo

---

## Step 3 — สร้าง Claude Code web routine

ไปที่ [code.claude.com/routines](https://code.claude.com/routines) (หรือ Settings → Routines ใน claude.ai)

1. **Connect repo**: `<YOUR-USER>/enabridge-research`
2. **Schedule**: `0 7 * * *` timezone `Asia/Bangkok` (= 07:00 ไทย ทุกวัน)
3. **Secrets** (inject เป็น env var):
   - `OPENAI_API_KEY` — copy จาก `.env` บนเครื่อง (แล้วอย่าลืม rotate ตาม step 5)
   - `TELEGRAM_BOT_TOKEN` — copy จาก `.env`
   - `TELEGRAM_CHAT_ID` — `7500968194`
4. **Routine prompt** — วางตามนี้:

````markdown
# Daily Enabridge AI Brief — cloud routine

Today: {{date}}

## Task

1. Research ข่าว AI ที่สำคัญวันนี้ตาม `prompts/daily-research.md`
   - 3–5 เรื่อง, focus: Agentic AI, real-world business use cases, OpenBridge trends
   - Source: ChatGPT/OpenAI blog, Anthropic, Google AI, HN, a16z, Stratechery,
     TechCrunch, The Information, Pragmatic Engineer — อะไรที่มีตัวเลขจริง/deployment จริง
2. เขียน brief .md ลง `news/` ตามรูปแบบ `news/YY-MM-DD-NNN-slug.md` + `-index.md`
   ใช้ `templates/brief.md` เป็น template (ต้องมี `## Audio script` ของทุกเรื่อง)
3. รัน:
   ```bash
   pip3 install openai python-dotenv requests 'httpx[socks]' --break-system-packages -q
   bash scripts/run_daily.sh $(TZ=Asia/Bangkok date +%y-%m-%d)
   ```
4. Commit + push ทำโดย `run_daily.sh` แล้ว — ไม่ต้องทำซ้ำ

## ถ้าเจอปัญหา
- MP3 ขนาด 0 byte → OpenAI API ล่ม หรือ key หมด credit — stop routine, แจ้ง Yoh
- Git push fail → routine environment อาจยังไม่ได้ configure deploy key — ตรวจ repo settings
````

5. **Permissions**: อนุญาต Bash, WebSearch, WebFetch, file read/write
6. **Git write access**: routine ต้อง push ได้ — ใน Claude Code routines ปกติจะใช้ GitHub App integration
   (ถ้าตั้ง repo ผ่าน "Connect repo" UI มันจะ setup ให้อัตโนมัติ)

Save → กด **"Run now"** เพื่อ test ครั้งแรก (จะสร้าง brief + MP3 ของวันนี้)

---

## Step 4 — decide Cowork task เก่า

Cowork task `enabridge-daily-research` ที่รันทุก 07:07 บน Mac — **เก็บไว้เป็น backup** ก็ได้
แต่แนะนำ edit นิดหน่อยเพื่อไม่ให้ชนกับ cloud:

- เปลี่ยน cron เป็น `7 8 * * *` (08:07 ไทย — หลัง cloud 1 ชม.)
- หรือตั้ง `metadata.enabled=false` ใน Cowork UI (pause ไว้, เปิดเมื่อ cloud ล่ม)

**Note ถ้ารันพร้อมกัน**: ทั้ง 2 routine เขียน brief ของวันเดียวกัน → `run_daily.sh` จะ commit
คนหลัง push อาจโดน reject (non-fast-forward). วิธีกัน: cloud รันก่อน (07:00), Cowork รันหลัง (08:07)
— Cowork จะ `git pull --rebase` ก่อน commit ถ้าผมเพิ่ม flag ให้ (ยังไม่เพิ่ม เพราะเชื่อว่าปกติจะใช้ cloud ตัวเดียว)

---

## Step 5 — rotate credentials ที่ถูก paste ใน chat

API key ทั้ง 2 ตัว (OpenAI + Telegram) เคยถูก paste ใน Cowork chat — หลัง pipeline ทำงาน:

1. **OpenAI**: https://platform.openai.com/api-keys → revoke key เดิม → create ใหม่
   → update ใน (ก) `.env` บนเครื่อง (ข) Claude Code routine secrets
2. **Telegram**: คุย `@BotFather` → `/mybots` → เลือก bot → "API Token" → "Revoke current token"
   → update ใน (ก) `.env` บนเครื่อง (ข) Claude Code routine secrets

(TELEGRAM_CHAT_ID เป็น user ID ของคุณ — ไม่ต้อง rotate)

---

## Step 6 — Subscribe podcast (ทำทีเดียวจบ)

- **Apple Podcasts**: Library → Follow Show by URL → paste `https://enabridge.ai/research/feed.xml`
- **Spotify**: submit feed ที่ [podcasters.spotify.com](https://podcasters.spotify.com/) (review ~1–2 วัน)
- **Overcast / Pocket Casts / Castro / ฯลฯ**: "Add by URL" → paste feed URL

---

## Troubleshooting

| ปัญหา | ที่ดู |
|---|---|
| Cloud routine fail ที่ step "git push" | Repo ยังไม่ได้ connect ผ่าน Claude Code UI — ไปตั้ง repo ใน routine settings |
| Feed ว่าง (`<channel>` ไม่มี `<item>`) | `curl https://raw.githubusercontent.com/Enabridge/EnabridgeResearch/main/audio/index.json` ได้ไหม? ถ้า 404 = ยังไม่ได้ push, ถ้า got JSON = ตรวจ env vars บน Railway (case-sensitive) |
| RSS feed cache ค้าง | Wait 5 min (revalidate=300) หรือ redeploy Railway service |
| MP3 โหลดช้าบน mobile | `raw.githubusercontent.com` ไม่ใช่ CDN ที่ดีสุดแต่พอไหว — ถ้าอยากปรับ ย้ายเป็น GitHub Release asset หรือ R2/S3 ทีหลัง |
| Cowork task local ชน cloud (push reject) | ปิด Cowork task หรือ เลื่อน schedule ไปหลัง cloud |

---

## Summary — ลำดับที่คุณต้องทำ

1. ☐ `gh repo create ... --public --push` (Step 1)
2. ☐ set `GITHUB_OWNER=Enabridge` / `GITHUB_REPO=EnabridgeResearch` บน Railway + redeploy (Step 2)
3. ☐ ตั้ง Claude Code routine + paste 3 secrets + "Run now" ทดสอบ (Step 3)
4. ☐ ตัดสินใจเรื่อง Cowork backup — pause หรือเลื่อน cron (Step 4)
5. ☐ rotate OpenAI + Telegram token (Step 5)
6. ☐ subscribe feed ใน Apple Podcasts (Step 6)

หลังทำ 1–3 เสร็จ — cloud routine จะ deliver ข่าวเช้าให้ทุก 07:00 โดยไม่ต้องเปิด Mac แล้ว
