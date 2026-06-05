---
date: 2026-06-06
slug: microsoft-mai-thinking-code-launch
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial illustration of a giant Microsoft logo lifting off from a tangled web of OpenAI cables it has just cut, ascending toward a sunrise of code symbols rendered in flat geometric style. Foreground shows a glowing "5B" and "51% SWE Bench" text floating on a chip die. Composition: low-angle hero shot, strong diagonal split between dark "dependency" lower-left and bright "first-party" upper-right. Muted teal, electric blue, and warm amber palette, sharp editorial lines, no real human faces, large legible text rendering for thumbnail at 200px.
image: images/26-06-06-0604-01-microsoft-mai-thinking-code-launch.png
---

# Microsoft ตัดสายสะดือ OpenAI — เปิด MAI-Thinking-1 + MAI-Code-1-Flash บน Build 2026, เคลม match Opus 4.6

## TL;DR
- 2 มิ.ย. ที่ Build 2026 — Microsoft เปิด **MAI-Thinking-1** (reasoning) และ **MAI-Code-1-Flash** (coding) — โมเดล first-party ตัวแรกที่ train **from scratch ไม่มี distillation จาก OpenAI**
- ตัวเลข: **MAI-Thinking-1 ทำ 97.0% AIME 2025, 94.5% AIME 2026, match Opus 4.6 บน SWE-Bench Pro** (1T total params, 35B active, sparse MoE). **MAI-Code-1-Flash ทำ 51% SWE Bench Pro ที่ 5B params** — Mustafa Suleyman อ้างชนะ Claude Haiku 4.5 ทั้ง perf และ price
- รวมเป็น 7 in-house model ในตระกูล MAI ที่ launch รอบเดียว — ขึ้นเป็น default ใน GitHub Copilot model picker และ Foundry. Independence จาก OpenAI ที่บ่นมา 2 ปี = ของจริงแล้ว
- มุม OpenBridge: เกม model commoditization เร่งอีกขั้น — workflow tool ที่ commit กับ vendor เดียวจะถูก undercut เมื่อ "good-enough cheaper" ตัวใหม่ขึ้น marketplace เกือบทุกเดือน

## เกิดอะไรขึ้น

วันที่ 2 มิ.ย. บนเวที Build 2026 ที่ San Francisco, Mustafa Suleyman เดินขึ้นมาเปิดประโยคแรกที่เป็นข่าวที่สุดของงาน — "These are Microsoft's first frontier models, end-to-end" — แล้ว unveil **7 in-house models** พร้อมกัน นำโดย **MAI-Thinking-1** (reasoning) และ **MAI-Code-1-Flash** (coding) ทั้งสองตัวอยู่บน Microsoft Foundry และ GitHub Copilot ทันที

ตัวเลขที่ Suleyman เน้นบนเวที: MAI-Thinking-1 ใช้ **sparse Mixture of Experts** ขนาด **~1 ล้านล้าน params total / 35B active** พร้อม **256K context** ที่ Microsoft เคลมว่า "รับเอกสาร 600 หน้าได้สบาย" — และเป็น in-house reasoning ตัวแรกที่ทำ **97.0% บน AIME 2025, 94.5% บน AIME 2026 และ match Opus 4.6 ของ Anthropic บน SWE-Bench Pro**. ส่วน MAI-Code-1-Flash เป็น coding model **5B params** ที่ทำ **51% บน SWE Bench Pro** — Suleyman เคลมว่า "ขนาดเท่า Haiku แต่ราคาถูกกว่า, perf ดีกว่า"

จุดที่เป็น line in the sand คือคำว่า "from scratch, no distillation from third-party models" — ที่ทีม MAI พูดซ้ำหลายครั้ง. ตลอด 2 ปีที่ผ่านมา Microsoft โดน street ขุดว่า in-house model ทุกตัว distill จาก GPT-4 (ข้อกล่าวหาที่ตอบยาก เพราะ Microsoft ถือ exclusive license อยู่แล้ว) — รอบนี้ Suleyman ตัดข้อสงสัยทิ้งโดยใส่ในประโยคเปิด keynote, ใน paper, และในทุกการ briefing สื่อ. Independence จาก OpenAI ที่ Satya Nadella บ่นเป็นการภายในมาตั้งแต่ปลายปี 2024 = ของจริงแล้ว

Distribution: ทั้งคู่ขึ้นเป็น default ใน **GitHub Copilot model picker** บน VS Code (สำหรับ individual user) และ **Microsoft Foundry** สำหรับ enterprise. ที่น่าสนใจกว่าคือ Microsoft ปล่อยลง **OpenRouter, Fireworks, Baseten ด้วย** — ภาษา strategy คือ "เรา hedge ทุกทาง" แทนที่จะล็อกอยู่ใน Azure ecosystem เดียวเหมือนเดิม นี่คือ shift ระดับ Azure org chart

ที่ CNBC เก็บได้ในวง briefing — analyst ที่ Microsoft track อยู่ตั้งคำถามว่าทำไม Microsoft ปล่อย model ไป third-party inference provider ทั้งที่กำลังพยายามดัน Foundry. คำตอบจาก Microsoft AI exec: "developer adoption เป็นเงื่อนไขแรก — Foundry monetize ได้ทีหลังถ้าโมเดลชนะ" — ภาษาคน DeepMind/Anthropic มากกว่าภาษาคน Azure

## ทำไมสำคัญ

นี่คือ **moment of independence ครั้งที่สอง** ของ Microsoft จาก OpenAI — ครั้งแรกคือตอน Suleyman ถูก hire มาตั้งทีม MAI เมื่อต้นปี 2024; ครั้งนี้คือตอนทีม ship model ที่อ้างว่า match Opus 4.6 — น่าจะเป็น emotional reset ใน relationship ระดับที่ Sam Altman ต้องตอบใน TechCrunch สัปดาห์หน้า

แต่จุดที่น่าสนใจที่สุดสำหรับ **agentic / business use case** ไม่ใช่ benchmark — มันคือ **price per token + distribution width**. ถ้า MAI-Code-1-Flash ที่ 5B params จริง ๆ ทำ 51% SWE Bench Pro แล้ว undercut Haiku 4.5 ใน VS Code default — coding agent vendor ทุกเจ้าที่ build บน Anthropic (Cursor, Cline, Aider, Codeium) ต้อง re-bench ทันที. **Margin ของ coding agent layer จะหดอีก 20-30% ภายใน Q3** ถ้า Microsoft pricing aggressive จริง

Pattern ที่เห็นชัดในปี 2026: **frontier capability commoditizes ภายใน 6 เดือน**. Opus 4.7 ของ Anthropic launch เดือน เม.ย. ที่ราคา premium ที่ enterprise ยอมจ่าย; วันนี้ Microsoft อ้างว่า MAI-Thinking-1 match ได้แล้ว และ Google ก็เพิ่ง ship Gemini 3.5 Pro เดือนนี้. **คนที่ position แบบ "เราเลือก best model" สำหรับ workflow user แทนที่จะ "lock เข้า provider เดียว" จะอยู่รอดกว่า** — Sierra, Cursor, Glean ทำแบบนี้แล้ว, Salesforce/ServiceNow ก็ทำ multi-model

จุดเตือน: Microsoft เปิดในวง **private preview สำหรับ Foundry และ default ใน Copilot — ยังไม่ปล่อย API ทั่วไป**. การที่ Suleyman อ้างชนะ Opus 4.6 บน "search task ที่ independent rater preferred Sonnet 4.6 น้อยกว่า MAI-Thinking-1" คือการเลือก eval ที่ favor เอง — รอ external bench ใน 2-3 สัปดาห์ก่อน update mental model

## มุม OpenBridge

ถ้า OpenBridge positioning เป็น **AI-native workflow / integration platform** — story นี้ทำ 2 อย่างที่ต้องคุยในทีม สัปดาห์นี้: (1) ถ้า product layer ของเราใช้ Claude/GPT เป็น default ใน production — เพิ่ม Microsoft MAI เข้า model routing **ก่อน** customer ถาม. (2) Positioning ของ Microsoft ที่ "we hedge across inference providers" คือ playbook ที่ workflow vendor ทุกเจ้าควรลอก — ไม่ใช่ทุก customer ต้องการ best model; หลายเจ้าต้องการ **cheapest model ที่ work**

มุมรอง: ถ้า Microsoft จริง ๆ ดัน MAI-Code-1-Flash ใน Copilot default — **customer ที่ใช้ Copilot อยู่แล้วจะ assume coding capability เป็น commodity ภายในไตรมาส** — ถ้า OpenBridge มี code-gen / automation feature เป็น differentiator ต้องรีบ reposition จาก "code AI" เป็น "code AI ที่เชื่อม system X-Y-Z ของคุณได้" — vertical integration ของ workflow data จะเป็น moat แทน raw model quality

## Sources
- [Microsoft unveils new AI models to lessen reliance on OpenAI](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [Introducing MAI-Code-1-Flash | Microsoft AI](https://microsoft.ai/news/introducingmai-code-1-flash/)
- [Microsoft Build 2026: MAI-Thinking-1 Is First In-House Reasoning Model](http://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm)
- [Microsoft Build 2026 Highlights: 7 Self-Developed AI](https://www.tradingkey.com/analysis/stocks/us-stocks/261943322-microsoft-build-2026-highlights-7-proprietary-ai-models-tradingkey)

---

## Audio script
ข่าวใหญ่ที่สุดของวันมาจาก Build 2026. Microsoft เปิดตัว MAI-Thinking-1 กับ MAI-Code-1-Flash — โมเดล frontier first-party ตัวแรกที่ Mustafa Suleyman ยืนยันว่า train from scratch ไม่ได้ distill มาจาก OpenAI. ตัวเลขที่ทีม MAI โชว์น่าตกใจ — MAI-Thinking-1 ใช้ sparse Mixture of Experts หนึ่งล้านล้าน parameter active 35 billion ทำ AIME 2026 ได้ 94.5% และ match Opus 4.6 บน SWE-Bench Pro. ส่วน Code-1-Flash 5 billion parameter เท่านั้น แต่ทำ SWE Bench Pro 51% — Suleyman อ้างว่าชนะ Haiku 4.5 ทั้ง perf และราคา. ที่น่าสนใจกว่า benchmark คือ distribution — Microsoft ปล่อยลง OpenRouter, Fireworks, Baseten นอกจาก Foundry ตัวเอง. นี่คือ moment of independence ครั้งที่สองจาก OpenAI หลังจากดึง Suleyman เข้ามาเมื่อปีก่อน. มุม OpenBridge — ถ้า product เรา default Claude หรือ GPT อยู่ ต้องเพิ่ม MAI เข้า model routing ก่อน customer ถาม. Pattern ปี 2026 ชัดเจน — frontier capability commoditize ใน 6 เดือน, vendor ที่ lock provider เดียวจะถูก undercut. ของจริงคือ workflow data ที่ wrap รอบโมเดล ไม่ใช่ตัวโมเดลเอง.
