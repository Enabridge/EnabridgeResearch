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

## Task

1. ทำ research ตาม `prompts/daily-research.md` — 3–5 เรื่องคุณภาพ
2. เขียน briefs + index ใน `news/` ใช้ `templates/brief.md` (ใส่ `image_prompt:` ทุกไฟล์)
3. รัน:
   ```bash
   bash scripts/write_briefs.sh $(date +%y-%m-%d)
   ```
4. รอ GHA: gen images → TTS → update index → open PR → ส่ง Telegram preview

## ห้าม
- อย่า merge PR เอง — Yoh จะฟัง MP3 ใน Telegram แล้ว approve เอง
- อย่ารัน `run_daily.sh` (legacy — สำหรับ local backup เท่านั้น)
- อย่าทำ TTS/Telegram เอง — GHA ทำให้

## Done เมื่อ
- `git push origin daily/YY-MM-DD` สำเร็จ
- GHA workflow ที่ https://github.com/Enabridge/EnabridgeResearch/actions เริ่มรัน
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
# จำลอง routine: สร้าง branch + ใส่ brief demo + push
git checkout main && git pull
git checkout -b daily/26-04-19
# (ถ้าอยาก test ไม่เสียง API token, เอา brief ของ 26-04-18 มาเปลี่ยน date เป็น 26-04-19)
bash scripts/write_briefs.sh 26-04-19
```

หลัง push ดู:
- GHA running: https://github.com/Enabridge/EnabridgeResearch/actions
- รอ ~3-5 นาที → Telegram preview + PR link
- คลิก PR link → review → merge
- รอ 5 นาที (ISR) → เปิด https://enabridge.ai/research ดูว่ามีวันใหม่โผล่

## Architecture diagram

```
┌──────────────────────────────────────────────────────────────┐
│  Claude Code Routine (6:00 AM daily, Asia/Bangkok)           │
│  → research + write news/*.md (w/ image_prompt)             │
│  → scripts/write_briefs.sh → push daily/YY-MM-DD branch     │
└────────────────────┬─────────────────────────────────────────┘
                     │ push
                     ▼
┌──────────────────────────────────────────────────────────────┐
│  GitHub Actions: daily-branch-build.yml                      │
│  1. gen_images.py  (DALL-E 3)                               │
│  2. tts.py         (gpt-4o-mini-tts → coral 1.3x)           │
│  3. update_index.py                                          │
│  4. commit back to daily/YY-MM-DD                           │
│  5. open PR to main                                          │
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
│  - list: grid of 60 days                                     │
│  - /research/[date]: rich detail + audio player              │
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
