# Phase 3 — Review-before-publish + rich content + site redesign

> การเปลี่ยนแปลง (หลัง Phase 2):
> - **Routine เขียนแค่ briefs** (ไม่ทำ TTS/Telegram เอง) → push ไป branch `daily/YY-MM-DD`
> - **GHA รับช่วงต่อ**: gen images (DALL-E 3) → TTS → update index → commit กลับ → เปิด PR → ส่ง Telegram preview
> - **Yoh review** ใน Telegram + GitHub → merge PR → content ขึ้น main → site update ภายใน 5 นาที
> - **Site redesign**: `/research` เป็น grid ของ 60 วันล่าสุด, `/research/[date]` เป็น detail page พร้อมรูป + markdown + audio player

## Setup checklist

### 1. เพิ่ม GitHub Actions secrets

ไปที่ `https://github.com/Enabridge/EnabridgeResearch/settings/secrets/actions` → **New repository secret** ทั้ง 3 ตัว:

```
OPENAI_API_KEY       = sk-proj-Q9Vcd2K...    (key เดียวกับ routine — ใช้สำหรับ DALL-E + TTS)
TELEGRAM_BOT_TOKEN   = 8740988487:AAH7RSy... (จาก .env)
TELEGRAM_CHAT_ID     = 7500968194             (จาก .env)
```

> `GITHUB_TOKEN` — ใช้ default ของ GHA, ไม่ต้องเพิ่มเอง

### 2. เปิดสิทธิ์ PR ให้ workflow

`https://github.com/Enabridge/EnabridgeResearch/settings/actions` → **Workflow permissions** →
- เลือก **"Read and write permissions"**
- ติ๊ก **"Allow GitHub Actions to create and approve pull requests"**
- Save

### 3. Auto-delete merged branches (optional แต่สะอาด)

`https://github.com/Enabridge/EnabridgeResearch/settings` → General → **Pull Requests** section →
ติ๊ก **"Automatically delete head branches"**

### 4. Update Claude Code routine prompt

เดิม prompt สั่งให้รัน `run_daily.sh` ทำทุกขั้น — ใหม่ให้แค่เขียน briefs + push branch:

````markdown
# Enabridge Daily AI Brief — research routine

Today: {{date}}
Working dir: ~/ws/company/enabridge-research

**Slug format:** `YY-MM-DD-HHMM` (timestamp per run — วันเดียวรันหลายรอบได้ ไม่ทับกัน)

## Task

1. Compute timestamp + checkout branch:
   ```bash
   cd ~/ws/company/enabridge-research
   SLUG=$(date +%y-%m-%d-%H%M)
   git checkout main && git pull
   git checkout -b "daily/${SLUG}"
   ```

2. ทำ research ตาม `prompts/daily-research.md` — **3–5 เรื่องคุณภาพ**
   Source bias: OpenAI/Anthropic/Google AI blogs, HN front page, a16z, Stratechery, The Information, Pragmatic Engineer, TechCrunch
   เน้นตัวเลขจริง/deployment จริง — **ห้าม padding ข่าวเก่า**

3. เขียน briefs ใน `news/${SLUG}-NNN-slug.md` + index `news/${SLUG}-index.md` ใช้ `templates/brief.md`
   **ทุก brief ต้องมี:**
   - `image_prompt:` (English, editorial illustration, ห้าม text/logos/faces)
   - เนื้อหา 3–5 ย่อหน้า story-driven (เหมือน Stratechery article)
   - `## Audio script` สำหรับ TTS

4. Commit + push:
   ```bash
   bash scripts/write_briefs.sh "${SLUG}"
   ```

5. จบงาน — รอ GHA ~3–5 นาที: gen images → TTS → update index → open PR → ส่ง Telegram preview

## ห้าม
- ❌ อย่า merge PR เอง — Yoh จะฟัง MP3 ใน Telegram แล้ว approve เอง
- ❌ อย่ารัน `run_daily.sh` (legacy — สำหรับ local backup เท่านั้น)
- ❌ อย่าทำ TTS / Telegram / update_index เอง — GHA ทำให้
- ❌ อย่า push ตรงเข้า main

## Done เมื่อ
- `git push origin daily/${SLUG}` สำเร็จ (SLUG = YY-MM-DD-HHMM)
- GHA workflow ที่ https://github.com/Enabridge/EnabridgeResearch/actions เริ่มรัน

## ถ้าเจอปัญหา
- ไม่มี source แข็งพอ → เขียน 2 เรื่อง ห้าม padding
- Git push fail → ตรวจ GitHub App permission ของ routine
- GHA error → แจ้ง Yoh พร้อม link workflow run
````

### 5. Enabridge-site — update env + deploy

Railway vars ไม่ต้องเพิ่มอะไร — `GITHUB_OWNER` / `GITHUB_REPO` / `GITHUB_BRANCH` ตั้งไว้แล้วตั้งแต่ Phase 2

แต่ต้อง install deps ใหม่ (markdown renderer) — รันใน local:

```bash
cd ~/ws/company/enabridge-site
npm install react-markdown remark-gfm gray-matter
npm run build  # ตรวจว่า build ผ่าน
git add package.json package-lock.json src/app/research/
git commit -m "research page redesign — grid + per-day detail + markdown render"
git push
```

Railway จะ redeploy อัตโนมัติ

### 6. ทดสอบ end-to-end

บน Mac (หรือ Claude Code routine กด "Run now"):

```bash
cd ~/ws/company/enabridge-research
# จำลอง routine: timestamp slug + สร้าง branch + ใส่ brief demo + push
SLUG=$(date +%y-%m-%d-%H%M)   # เช่น 26-04-19-1430
git checkout main && git pull
git checkout -b "daily/${SLUG}"
# copy brief เก่ามาแก้ slug (สมมติ test ไม่ใช้ API token)
#   cp news/26-04-18-0700-001-*.md news/${SLUG}-001-test.md  ← แก้ filename + frontmatter
bash scripts/write_briefs.sh "${SLUG}"
```

หลัง push ดู:
- GHA running: https://github.com/Enabridge/EnabridgeResearch/actions
- รอ ~3-5 นาที → Telegram preview + PR link
- คลิก PR link → review → merge
- รอ 5 นาที (ISR) → เปิด https://enabridge.ai/research ดูว่ามี episode ใหม่โผล่

## Architecture diagram

```
┌──────────────────────────────────────────────────────────────┐
│  Claude Code Routine (6:00 AM + adhoc, Asia/Bangkok)         │
│  → SLUG=$(date +%y-%m-%d-%H%M)  e.g. 26-04-19-0700           │
│  → research + write news/${SLUG}-*.md (w/ image_prompt)      │
│  → scripts/write_briefs.sh → push daily/${SLUG} branch       │
└────────────────────┬─────────────────────────────────────────┘
                     │ push  (1 run = 1 branch = 1 episode)
                     ▼
┌──────────────────────────────────────────────────────────────┐
│  GitHub Actions: daily-branch-build.yml                      │
│  1. gen_images.py  --slug ${SLUG}  (DALL-E 3)                │
│  2. tts.py         --slug ${SLUG}  (gpt-4o-mini-tts coral)   │
│  3. update_index.py                                          │
│  4. commit back to daily/${SLUG}                             │
│  5. open PR to main  (title: Daily AI Brief — YY-MM-DD HH:MM)│
│  6. Telegram: message + MP3 + PR link                        │
└────────────────────┬─────────────────────────────────────────┘
                     │ Yoh: listen + approve
                     ▼
┌──────────────────────────────────────────────────────────────┐
│  Merge PR → main                                             │
└────────────────────┬─────────────────────────────────────────┘
                     │ ISR (5 min)
                     ▼
┌──────────────────────────────────────────────────────────────┐
│  enabridge.ai/research (Next.js on Railway)                  │
│  - list: grid of 60 latest episodes (with time)              │
│  - /research/[slug]: rich detail + audio player              │
│  - /research/feed.xml: podcast RSS                           │
└──────────────────────────────────────────────────────────────┘
```

## Cost estimate

Per day (4 briefs assumed):
- DALL-E 3 standard: 4 × $0.04 = **$0.16**
- TTS gpt-4o-mini-tts: ~6k chars × $0.015/1k = **~$0.09**
- Claude Code routine: included in Pro plan (no extra)
- GHA: free for public repo

Monthly: **~$7.50** all-in
