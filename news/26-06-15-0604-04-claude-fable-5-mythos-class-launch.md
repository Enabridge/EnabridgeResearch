---
date: 2026-06-15
slug: claude-fable-5-mythos-class-launch
topic: agentic-ai
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial illustration of a tall stone obelisk inscribed with the word
  "FABLE 5" glowing in Anthropic amber, standing in a research courtyard.
  In front of the obelisk, large floating numerals "80.3% SWE-Bench Pro"
  and "95% SWE-Bench Verified" hover prominently. A smaller secondary
  obelisk behind, half in shadow, is labeled "MYTHOS 5 — restricted access".
  Smaller tags pinned around: "$10 / $50 per M tokens" and "Opus 4.8: 69.2%".
  Render style: cinematic editorial illustration, classical architecture
  perspective, warm Anthropic amber lighting on Fable obelisk vs cool blue
  shadow on Mythos, dramatic depth, high-contrast typography legible at 200px
  thumbnail. No real human faces.
image: images/26-06-15-0604-04-claude-fable-5-mythos-class-launch.png
---

# Claude Fable 5 (Mythos-class) เปิด GA — 80.3% บน SWE-Bench Pro, แซง Opus 4.8 แบบขาดลอย, แต่ Anthropic ตั้ง safeguard ที่ปฏิเสธ cybersecurity/bio/chem 5% ของ session

## TL;DR
- 9 มิ.ย. Anthropic ปล่อย **Claude Fable 5** GA — Mythos-class model แรกที่ public access ผ่าน Claude API, Bedrock, Vertex AI, Microsoft Foundry; ราคา $10 input / $50 output per M tokens (ขึ้นจาก Opus 4.8 ที่ $5/$25 = 2x)
- Benchmark: **80.3% SWE-Bench Pro** (Opus 4.8 = 69.2%, leads ที่สอง 11 percentage points), **95% SWE-bench Verified**, **88% Terminal-Bench 2.1**, **78% ExploitBench**
- Safeguard ปฏิเสธ cybersecurity/bio/chem queries ~5% ของ session — route ไป Opus 4.8 ฟรี; **Mythos 5** (ตัวเดียวกัน safeguard ลด) เปิดเฉพาะ vetted partner ผ่าน Project Glasswing
- รวม pricing 9–22 มิ.ย. ฟรีบน Pro/Max/Team/seat-Enterprise plans; 23 มิ.ย. ต้องใช้ usage credits

## เกิดอะไรขึ้น

วันที่ 9 มิ.ย. 2026 Anthropic ปล่อย **Claude Fable 5** GA — Mythos-class model แรกที่ public ใช้ได้ ผ่าน Claude API, Anthropic apps, Amazon Bedrock, Vertex AI, Microsoft Foundry Pricing $10 input / $50 output per million tokens — เท่ากับ 2x ของ Opus 4.8 ($5/$25) ที่ปล่อย 28 พ.ค. ห่างกัน 12 วัน นี่เป็น Mythos-class model ตัวแรกที่ Anthropic ยอมเปิด public — Mythos series ก่อนหน้านี้ทำ inference experiment ภายในเท่านั้น (รวม Glasswing collaborator ในงาน security)

Benchmark ที่ Anthropic เปิดเผยทำให้ Fable 5 เป็น frontier model ที่ลำดับชั้นชัดเจน: **SWE-Bench Pro 80.3%** (Opus 4.8 = 69.2%, GPT-5 ที่ launch ก่อนหน้าอยู่ที่ ~69%) — leadership ที่ 11 percentage points คือ gap ที่ใหญ่ที่สุดที่ frontier model เคยมีในรอบ 12 เดือน **SWE-bench Verified 95%**, **Terminal-Bench 2.1 88%**, **FrontierCode Diamond 29.3%** (ปกติ Opus 4.8 ทำได้ <10%) **GDPval-AA 1932**, **Humanity's Last Exam without tools 59%, with tools 64.5%**, **HealthBench Professional 66%**, และ **ExploitBench 78%** — ตัวสุดท้ายนี่เป็น exact reason ที่ต้องมี Mythos/Fable split

Anthropic อธิบาย split ของ Mythos/Fable เป็นครั้งแรกใน production deployment — **Mythos 5** กับ **Fable 5** คือ underlying model เดียวกัน ต่างที่ safeguard layer Fable 5 มี conservative safeguards ที่ flag query เกี่ยวกับ cybersecurity, chemistry, biology, model distillation แล้ว route ไปยัง Opus 4.8 (ไม่ใช่ refuse) — และไม่คิด Fable price กับ query ที่ถูก route Anthropic ประมาณว่า safeguards จะ trigger ใน **น้อยกว่า 5% ของ session** เฉลี่ย — ไม่เป็น blocker สำหรับ enterprise use case ทั่วไป Mythos 5 (ตัวเดียวกัน safeguard ลด) เปิดเฉพาะ vetted partner ผ่าน **Project Glasswing** ซึ่งเป็น infrastructure provider + cybersecurity researcher ที่ผ่าน vetting หลายขั้น

Anthropic เปิด promotional access 9–22 มิ.ย. ที่ Fable 5 ฟรีบน Pro, Max, Team, และ seat-based Enterprise plans หลัง 23 มิ.ย. กลับมาคิดผ่าน usage credits ($10/$50 per M tokens) — pattern ที่เริ่มหลัง 13 พ.ค. ที่ Anthropic ประกาศ subscription subsidy reform Simon Willison เขียน initial impression ว่า "Fable 5 is the first model where I felt the SWE-bench Pro number is real" — comment ที่บอกว่า benchmark ไม่ใช่แค่ saturation game

## ทำไมสำคัญ

Fable 5 เป็น **pace check** สำหรับ Anthropic — ปล่อย Opus 4.7 (เม.ย.), Opus 4.8 (28 พ.ค.), Fable 5 (9 มิ.ย.) — 3 release ใหญ่ใน 6 สัปดาห์ pattern นี้กดดัน OpenAI (ที่ GPT-5 ยังไม่มา GA) + Google (Gemini 3 stuck ที่ research preview) อย่างต่อเนื่อง gap 11 percentage point บน SWE-Bench Pro เปลี่ยน developer mindset จาก "ลองหลายตัว" เป็น "default Claude" ทันที — Anthropic ที่นำใน Ramp AI Index (34.4% vs OpenAI 32.3% ณ พ.ค. 2026) จะขยาย lead ต่อ

Mythos/Fable split คือ **business model innovation** ไม่ใช่แค่ safety theater Anthropic เปิด Fable 5 ราคา 2x ของ Opus 4.8 ($10/$50 vs $5/$25) แต่ลูกค้าจ่ายเฉพาะ query ที่ผ่าน safeguard (95% ของ session) ส่วน 5% ที่ถูก flag จะใช้ Opus 4.8 ฟรี — net ลูกค้าจ่ายมากขึ้นต่อ token แต่ได้ frontier capability ที่ matter จริง pattern นี้คือ "tiered safeguard pricing" ที่ scale ได้ — ในอนาคต Anthropic อาจมี Fable Pro, Fable Premier, Mythos partner-only เป็น hierarchy

ด้านที่ underrated คือ **ExploitBench 78%** — benchmark ที่วัด ability ในการ identify + exploit security vulnerability ใน production code base 78% เป็นตัวเลขที่ทำให้ Mythos ห้ามขายเป็น public — Glasswing partnership ที่เปิด Mythos 5 ให้กับ cybersecurity researchers หมายความว่า Anthropic กำลังเป็น vendor ของ offensive security tool ในระดับ frontier ที่อยู่ใน controlled distribution market นี้ก่อนหน้า dominated โดย Mandiant/CrowdStrike (defensive), Cobalt Strike (offensive grey market) — Anthropic กำลังจะเข้าเป็น top tier ของ offensive AI tool ที่ขายเฉพาะ vetted buyer

## มุม OpenBridge

Fable 5 + Mythos pattern เป็น **lesson ของ tiered access control** ที่ OpenBridge ควรเอามาประยุกต์ — agent integration layer ที่ขาย enterprise ก็มี dimension ของ "data access tier" + "tool access tier" ที่ควร tier ตามเหตุผลเดียวกัน customer Fortune 500 ที่ใช้ Claude บน production ต้องการ "selective tool exposure" ที่ค่าพื้นฐานปลอดภัยใน 95% ของ session แต่ unlock advanced tool ได้สำหรับ vetted user + task ที่ผ่าน review pattern ที่ Anthropic ใช้ (route ไป safer model + price discrimination) นำมาประยุกต์ใน integration ได้: route tool call ที่ sensitive ไปยัง Sandboxed connector + price reflectivity

Pace 12 วันระหว่าง Opus 4.8 → Fable 5 = **cadence ที่ OpenBridge ต้อง factor เข้า roadmap** — ลูกค้า enterprise ที่ integrate Claude วันนี้จะ ask ว่า "swap Fable 5 → Fable 6 → Mythos 6 ได้ไหม" Plus ความซับซ้อนที่ Fable model มี multiple safeguard tier ที่ behavior ต่างกันต่อ query — integration layer ต้องเก็บ context ของ "ตอบจาก Fable หรือ Opus" + handle routing ที่ Anthropic ทำ transparently (เพราะ developer ไม่รู้ว่า query ใดถูก route) OpenBridge ที่ออกแบบให้ neutral + observable จะ handle ได้ดีกว่า hard-coded SDK integration window สำคัญคือต้องสร้าง observability layer สำหรับ Anthropic safeguard routing ก่อนที่ลูกค้าจะถาม

## Sources
- [Claude Fable 5 and Claude Mythos 5 — Anthropic News](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Anthropic's Claude Fable 5 is a version of Mythos the public can access today — TechCrunch](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)
- [Anthropic Launches Claude Fable 5, Its First Public Mythos-Class Model — MacRumors](https://www.macrumors.com/2026/06/09/anthropic-fable-5/)
- [Claude Fable 5 & Claude Mythos 5 Benchmarks Explained — Vellum AI](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)
- [SWE-bench Pro Leaderboard (2026): Every Model Score, Claude Fable 5 Leads at 80.3% — Morph LLM](https://www.morphllm.com/swe-bench-pro)
- [Initial impressions of Claude Fable 5 — Simon Willison](https://simonwillison.net/2026/Jun/9/claude-fable-5/)

---

## Audio script
สวัสดีครับ Yoh ข่าวสุดท้ายคือ Claude Fable 5 9 มิถุนายน Anthropic ปล่อย Fable 5 GA เป็น Mythos-class model ตัวแรกที่ public access ผ่าน Claude API Bedrock Vertex AI Microsoft Foundry ราคา 10 input 50 output per million tokens ขึ้นจาก Opus 4.8 ที่ 5 และ 25 เท่ากับ 2 เท่า ปล่อยห่างจาก Opus 4.8 แค่ 12 วัน Benchmark สำคัญคือ SWE-Bench Pro 80.3% Opus 4.8 ทำได้ 69.2% gap ที่ 11 percentage points คือ gap ที่ใหญ่ที่สุดที่ frontier model เคยมีในรอบปี SWE-bench Verified 95% Terminal-Bench 88% Anthropic เปิด split ระหว่าง Fable กับ Mythos เป็นครั้งแรก underlying model เดียวกัน ต่างที่ safeguard Fable 5 มี conservative safeguards ที่ flag query เกี่ยวกับ cybersecurity chemistry biology model distillation แล้ว route ไปยัง Opus 4.8 ฟรี ประมาณ 5% ของ session Mythos 5 เปิดเฉพาะ vetted partner ผ่าน Project Glasswing สำหรับ infrastructure provider และ cybersecurity researcher ตัวเลขที่ underrated คือ ExploitBench 78% ที่วัด ability ใน identify และ exploit security vulnerability เป็นเหตุผลที่ Mythos ห้ามขายเป็น public Anthropic กำลังเป็น vendor ของ offensive security tool ระดับ frontier ใน controlled distribution Pace 12 วันระหว่าง Opus 4.8 ไป Fable 5 คือ cadence ที่ enterprise ต้อง factor เข้า roadmap สำหรับ OpenBridge สอง takeaway หนึ่ง Mythos Fable split เป็น tiered access control ที่ควรเอามาประยุกต์ใน agent integration layer route tool call ที่ sensitive ไปยัง sandboxed connector pattern เดียวกัน สอง integration layer ต้อง observable เพราะ Anthropic จะ route query transparently developer ไม่รู้ว่า query ใดถูก route OpenBridge ที่ออกแบบให้ observable จะ handle ได้ดีกว่า hard-coded SDK integration window สำคัญคือต้องสร้าง observability ก่อนที่ลูกค้าจะถามครับ
