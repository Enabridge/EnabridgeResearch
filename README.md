# enabridge-research

Daily AI research brief สำหรับทีม Enabridge / OpenBridge
โฟกัส: **Agentic AI, AI business use cases (ของจริง มีผลงานจับต้องได้), OpenBridge-relevant trends**

## โครงสร้าง

```
enabridge-research/
├── news/            # daily brief: YY-MM-DD-xxx.md
├── audio/           # daily audio: YY-MM-DD.mp3 (Phase 2)
├── prompts/         # research prompts ที่ scheduled task จะใช้
├── templates/       # brief template
├── scripts/         # helper scripts (TTS, deliver, publish feed)
└── config.json      # topics, delivery settings
```

## Workflow

1. **07:00 ทุกเช้า** — Cowork scheduled task รัน `prompts/daily-research.md`
2. Claude research ข่าวใหม่ → เขียน `news/YY-MM-DD-001.md` (และ -002, -003 ถ้ามีหลายเรื่อง)
3. (Phase 2) Script อ่าน .md → TTS เป็น MP3 → publish ไป private podcast feed
4. (Phase 2) Email digest + Line/Telegram push

## Phase 1 (ตอนนี้)

- [x] Folder structure
- [x] Research prompt
- [x] Brief template
- [x] Brief วันแรก (2026-04-18)
- [x] Cowork scheduled task

## Phase 2 (รออยู่)

- [ ] TTS pipeline (ElevenLabs หรือ OpenAI TTS)
- [ ] Private podcast RSS feed (host บน enabridge-site /research/feed.xml)
- [ ] Email digest (ผ่าน Gmail MCP)
- [ ] Line OA หรือ Telegram bot push
- [ ] ตัดสินใจ: auto-commit กลับ git repo ไหม

## หมายเหตุเรื่อง schedule

Cowork scheduled task รัน **บนเครื่องคุณ** — ต้องเปิด Cowork ค้างไว้ช่วง 7:00 ถ้าวันไหนปิดคอมพ์ task จะ skip วันนั้น
ถ้าอยากให้รันบนคลาวด์จริง ๆ ทุกวัน → ย้ายไป GitHub Actions (ดู Phase 2)
