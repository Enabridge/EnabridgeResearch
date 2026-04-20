---
date: 2026-04-19
slug: factory-150m-droids-coding-agent
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: Editorial illustration of a translucent assembly line of glowing humanoid silhouettes building cascading layers of code blocks, minimal flat shapes, muted emerald and copper palette, dramatic top-down lighting, no text no logos no faces
image: images/26-04-19-2312-02-factory-150m-droids-coding-agent.png
---
# Factory ปิด Series C $150M ที่ valuation $1.5B — "Droids" agent coder doubled MoM 6 เดือนติด

## TL;DR
- **Factory.ai** ปิด Series C $150M ที่ post-money valuation **$1.5B** — นำโดย Khosla Ventures, ตามด้วย Sequoia, Insight Partners, Blackstone (16 เม.ย.)
- Product: **"Droids"** — autonomous AI agent ที่ทำ full SDLC (test, code review, doc, deploy, refactor) ไม่ใช่แค่ code completion
- **Differentiator คือ model-agnostic** — switch ระหว่าง Claude / DeepSeek / GPT ได้แบบ runtime, ลด vendor lock-in
- Customer enterprise: **NVIDIA, Adobe, EY, Palo Alto Networks, Adyen** — ใช้งานโดย "developer หลายแสนคน" (บริษัทอ้าง)
- Revenue: **doubled MoM 6 เดือนติด** — แปลว่าเริ่มต้นปี 2026 เล็ก แต่ตอนนี้ ARR run-rate ระดับ unicorn-justifiable

## เกิดอะไรขึ้น

วันที่ 16 เม.ย. Factory ประกาศปิด Series C $150 ล้าน นำโดย Khosla Ventures พร้อม Sequoia Capital, Insight Partners, Blackstone — post-money valuation พุ่งจาก $300M (Series B ปลายปี 2025) ขึ้น **$1.5B ภายในไม่ถึง 6 เดือน** ทำให้ Matan Grinberg founder อายุ 26 ปี เข้า unicorn club อย่างเป็นทางการ

Product ของ Factory ชื่อ **"Droids"** — เป็น autonomous coding agent ที่ positioning ต่างจาก Cursor, Windsurf, GitHub Copilot ที่ assist developer แบบ pair programming. Droids ออกแบบให้ **ทำงานเอง** end-to-end: รับ ticket จาก Jira → เขียน code + test → run CI → review own PR → deploy. Workflow ใกล้กับ Devin ของ Cognition แต่ scope เน้น **enterprise refactoring + maintenance** มากกว่า greenfield

จุดที่ทำให้ Khosla เปิด check $150M เร็วขนาดนี้คือ **growth metric**. Sources ที่ TechFundingNews และ ByteIota ยืนยันตรงกัน: Factory **double revenue MoM ทุกเดือนติดต่อกัน 6 เดือน** ตั้งแต่ ต.ค. 2025 — ถ้าเริ่มต้น Q4 2025 ที่ ARR ~$2M, ตอนนี้ run-rate ราว $130M+; เป็น growth rate ที่ Cursor และ Windsurf เคยทำได้ในปี 2024 และ justify valuation premium ของ AI infrastructure

**Customer logo** สำคัญพอ ๆ กับ growth: NVIDIA, Adobe, EY (เชื่อม brief วันที่ 18 เรื่อง EY agentic AI rollout — Factory เป็นหนึ่งใน supplier สำหรับ engineering side), Palo Alto Networks, Adyen. ทั้งหมดเป็น **enterprise tier 1** ที่ procurement ยาก — แปลว่า Factory ผ่าน vendor security review + IP review ของลูกค้าเหล่านี้แล้ว, moat ที่ไม่อยู่ใน screenshot product

**Differentiator ที่ Khosla ชูคือ "model-agnostic"** — Droids switch ระหว่าง Claude Opus, DeepSeek V3, GPT ได้ runtime ตาม task; ใช้ Claude สำหรับ planning, DeepSeek สำหรับ refactor (ถูก + เร็ว), GPT สำหรับ code review. Pattern เดียวกับ NVIDIA AI-Q ที่ brief afternoon — **hybrid model architecture = winning pattern ของ agentic 2026**

## ทำไมสำคัญ

ตลาด AI coding agent กำลัง **bifurcate ชัดเจน** ในรอบ 90 วันที่ผ่านมา:
- **Tier 1 — Pair programmer** (Cursor, Windsurf 2 จาก brief เมื่อวาน, GitHub Copilot): UX แบบ IDE-native, focus on developer-in-loop, valuation $5-20B
- **Tier 2 — Autonomous worker** (Factory, Devin ของ Cognition, OpenAI Codex Mac จาก brief เช้า): focus on full SDLC, valuation $1-5B

Factory ถือเป็น **bellwether ของ tier 2** เพราะมี enterprise customer + revenue traction ที่ verifiable. ถ้า Factory hit $200M ARR ภายในกลางปี 2026 — จะ trigger wave ของ "autonomous engineer" funding ในเดือน Q2-Q3 (Devin, Magic.dev, AutoCodeRover ทุกเจ้าจะ bump valuation)

ที่น่าสังเกตอีกจุดคือ **model-agnostic positioning**. ใน Q1 2026 หลายคนคิดว่า Anthropic จะ dominate coding (เพราะ Claude Opus 4.7 lead benchmark) — Factory โต้ thesis นี้: ลูกค้า enterprise ไม่อยากผูกขาดกับ Anthropic อย่างเดียว เพราะ (1) cost — DeepSeek V3 ถูกกว่า 8-10×, (2) risk — supply chain MCP vulnerability วันนี้ (brief 01) คือ reminder ว่าทำไม "single vendor agent stack = liability"

Trajectory ที่เห็น: **agent platform ที่ชนะปี 2026-2027 = orchestrate ของ frontier + open weight + cost-effective** — pattern เดียวกับ NVIDIA AI-Q, Anthropic-managed Tools, Vertex AI Agent Builder. Factory พิสูจน์ว่า startup ขนาดเล็กยังทำได้ดีกว่า hyperscaler ถ้า focus + execute เร็ว

## มุม OpenBridge

**Lesson #1 — Hybrid model routing คือ table stakes แล้ว**. ทุก agent product ที่ขาย enterprise ปี 2026 ต้องมี ability ที่จะ swap model runtime; ถ้า OpenBridge รุ่นปัจจุบัน hardcode Claude อย่างเดียว = action item Q2: implement model router (Claude + GPT + Llama 4 หรือ Typhoon ของ SCB10X สำหรับ workload ที่ต้องการ Thai context)

**Lesson #2 — Vertical autonomy > horizontal assistance สำหรับ B2B**. Factory ขาย "ทำงานแทน developer" ไม่ใช่ "ช่วย developer" — และ enterprise CFO จ่ายเพราะ ROI ตรง (1 droid ทดแทน $200K/year engineer); OpenBridge ที่ขาย workflow agent ควร frame เป็น **outcome-based pricing** (per-ticket completed, per-form processed) ไม่ใช่ seat-based. มี leverage บน margin มากกว่าเยอะ

**Lesson #3 — Enterprise logo > revenue ตอน fundraise**. Khosla เปิด check ส่วนหนึ่งเพราะ NVIDIA + Adobe + EY ยืนยัน procurement; OpenBridge ที่จะ raise series A-B ในไทย ต้อง chase brand-name SET100 logo ก่อน (CP, SCB, Krungthai, Bangchak) — แม้ ARR จะเล็ก แต่ logo จะ unlock check ที่ใหญ่กว่า

**Direct adjacency:** Factory + EY rollout (brief 03 ของรอบนี้) บอกว่า Big 4 consulting กำลังจะใช้ agentic stack ระดับ infrastructure — OpenBridge มี window 6-9 เดือนที่จะ position ตัวเองเป็น "agent integration partner สำหรับ Deloitte / PwC / EY / KPMG ไทย" ก่อนที่ Factory จะมา expand SEA เอง

## Sources
- [TechCrunch — Factory hits $1.5B valuation to build AI coding for enterprises](https://techcrunch.com/2026/04/16/factory-hits-1-5b-valuation-to-build-ai-coding-for-enterprises/)
- [Factory.ai — Factory raises $150M Series C](https://factory.ai/news/series-c)
- [The AI Insider — Factory Raises $150M at $1.5B Valuation to Scale AI Coding Agents for Enterprises](https://theaiinsider.tech/2026/04/17/factory-raises-150m-at-1-5b-valuation-to-scale-ai-coding-agents-for-enterprises/)
- [TechFundingNews — AI coding startup Factory raises $150M from Khosla Ventures, Sequoia Capital](https://techfundingnews.com/factory-ai-150m-series-c-unicorn-ai-agents-developers/)
- [ByteIota — Factory Raises $150M: Model-Agnostic AI Coding Agents](https://byteiota.com/factory-raises-150m-model-agnostic-ai-coding-agents/)

---

## Audio script
Factory เพิ่งปิด Series C 150 ล้าน valuation 1.5 พันล้าน. นำโดย Khosla Ventures พร้อม Sequoia, Insight, Blackstone. founder Matan Grinberg อายุ 26 เข้า unicorn club ภายในไม่ถึง 3 ปีตั้งแต่ตั้งบริษัท.

Product ชื่อ Droids. ต่างจาก Cursor หรือ Copilot ที่ pair programming. Droids ออกแบบให้ทำงานเอง end-to-end. รับ ticket จาก Jira เขียน code, test, deploy เอง. เน้น enterprise refactoring กับ maintenance.

ตัวเลขที่ทำให้ Khosla กล้าเปิด check 150 ล้านเร็วขนาดนี้คือ revenue doubled month-over-month 6 เดือนติด. ถ้าเริ่มที่ 2 ล้าน ARR ตอน Q4 ที่แล้ว. ตอนนี้ run-rate ราว 130 ล้าน. เป็น growth rate เดียวกับที่ Cursor ทำได้ปี 2024.

Customer คือ NVIDIA, Adobe, EY, Palo Alto Networks, Adyen. ทั้งหมด enterprise tier 1 ที่ procurement ยาก. ผ่าน security review แล้ว นี่คือ moat ที่ไม่ได้อยู่ใน screenshot.

Differentiator ที่ชูเด่นคือ model-agnostic. Droids switch ระหว่าง Claude, DeepSeek, GPT runtime ตาม task. Claude สำหรับ planning. DeepSeek สำหรับ refactor เพราะถูกและเร็ว. GPT สำหรับ review. pattern เดียวกับ NVIDIA AI-Q ของรอบบ่าย. hybrid model architecture คือ winning pattern ของ agentic ปี 2026.

สำหรับ OpenBridge. lesson หนึ่ง model router คือ table stakes ปีนี้. ใครยัง hardcode Claude อย่างเดียวต้อง action item Q2. lesson สอง vertical autonomy ชนะ horizontal assistance สำหรับ B2B. ขายเป็น outcome-based pricing per ticket per form. ไม่ใช่ seat-based. lesson สาม brand-name logo สำคัญกว่า ARR ตอน raise. ไล่จับ SET100 ก่อน. CP, SCB, Krungthai, Bangchak. unlock check ใหญ่ที่ตามมา.
