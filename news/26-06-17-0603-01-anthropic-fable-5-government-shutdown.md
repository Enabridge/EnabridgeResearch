---
date: 2026-06-17
slug: anthropic-fable-5-government-shutdown
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Hero illustration: a giant translucent Claude orb (Anthropic logo subtle on it)
  cracked down the middle by a glowing red government seal stamp labeled
  "SUSPENDED — JUNE 12". Behind it, a wall-sized calendar shows three pages —
  "JUN 9 LAUNCH", "JUN 10", "JUN 12 PULLED" — torn off in sequence to convey
  a 72-hour life cycle. In the foreground, a silhouette enterprise architect
  holds a laptop showing "Fable 5 unavailable" error and a second screen
  switching to "Claude Opus 4.8". Style: dramatic editorial illustration, deep
  navy + red palette, high contrast, big readable text "72 HOURS" overlaid at
  bottom-left. Square 1:1. No real faces.
image: images/26-06-17-0603-01-anthropic-fable-5-government-shutdown.png
---

# Fable 5 ออนไลน์ได้ 72 ชั่วโมง ก่อนรัฐบาลสหรัฐสั่งดับ — บทเรียน vendor risk ของยุค agentic

## TL;DR
- Anthropic ปล่อย Claude Fable 5 + Mythos 5 วันที่ 9 มิ.ย. แล้ววันที่ 12 มิ.ย. 17:21 ET รัฐบาลสหรัฐส่ง export-control directive สั่งระงับการเข้าถึงจาก foreign nationals — Anthropic ตัดสินใจดับทั้งสองรุ่นให้ทุกคนเพื่อ comply
- เหตุผล: รัฐเชื่อว่ามี jailbreak ผ่านการขอให้โมเดล "อ่าน codebase แล้ว fix vulnerabilities" → เปลี่ยน Fable 5 เป็นเครื่องหา zero-day อัตโนมัติ
- โมเดลอื่นของ Anthropic (Opus 4.8 ฯลฯ) ยังออนไลน์ปกติ — แต่สัญญาณคือ frontier model หนึ่งตัวอาจถูกถอดออกจากตลาดในวันเดียวด้วยเหตุผลความมั่นคงแห่งชาติ

## เกิดอะไรขึ้น

วันที่ 9 มิถุนายน 2026 Anthropic ปล่อย Claude Fable 5 — โมเดลระดับ Mythos ตัวแรกที่เปิดให้ public ใช้ — ราคา $10/$50 per million tokens, ฟรีบน Pro/Max/Team/Enterprise ถึง 22 มิ.ย. CEO Dario Amodei เคลมว่าเป็นโมเดลที่เก่งที่สุดที่ Anthropic เคยปล่อย state-of-the-art แทบทุก benchmark โดยเฉพาะ software engineering, autonomous task execution และ vision

72 ชั่วโมงต่อมา วันที่ 12 มิ.ย. 17:21 ET คำสั่ง export-control จากรัฐบาลสหรัฐมาถึง — อ้างอำนาจ national security ระงับการเข้าถึง Fable 5 และ Mythos 5 จาก "foreign nationals" ทั้งในและนอกประเทศ รวมถึงพนักงาน foreign national ของ Anthropic เอง เนื่องจาก Anthropic กรอง foreign national ออกจาก US users แบบ real-time ไม่ได้ จึงต้องดับทั้งสองโมเดลให้ผู้ใช้ทุกคนเพื่อ comply

เหตุผลที่รัฐยกขึ้นมา: พบ jailbreak method ที่ทำง่ายมาก — แค่บอก Fable 5 ให้ "อ่าน codebase นี้แล้ว fix software flaws ที่เจอ" โมเดลก็จะระบุช่องโหว่ออกมาให้หมด เปลี่ยนสภาพจากผู้ช่วย dev เป็นเครื่องสแกน zero-day อัตโนมัติ Anthropic ออกแถลงการณ์ตอบกลับว่า "เราไม่เห็นด้วยว่าการพบ jailbreak แคบ ๆ ตัวเดียวควรเป็นเหตุให้ถอดโมเดลที่ปล่อยไปแล้วให้คนใช้หลายร้อยล้านคน ถ้ามาตรฐานนี้ถูกใช้กับทั้งวงการ จะหยุดการ deploy frontier model ทุกเจ้า"

ระหว่างที่ Fable 5 ถูกระงับ — บริษัทไหนที่เพิ่งย้าย workflow ขึ้น Fable 5 ใน 72 ชั่วโมงแรก ต้องสลับกลับไป Opus 4.8 หรือเปลี่ยน vendor กลางคัน enterprise customers ที่ผูกสัญญา seat-based กับ Fable 5 ได้ตื่นมาเจอ error "model unavailable" โดยไม่มีการแจ้งล่วงหน้า

## ทำไมสำคัญ

เรื่องนี้เป็นจุดเปลี่ยนที่ใหญ่กว่า news cycle ทั่วไป สามมิติพร้อมกัน: (1) frontier AI ตอนนี้เข้าข่าย dual-use technology ระดับเดียวกับ semiconductor — รัฐสามารถสั่งระงับการ deploy ได้ภายในไม่กี่ชั่วโมง (2) "เปิดสาธารณะ" กลายเป็นสถานะที่กลับได้ไม่ใช่ one-way door ที่เราเคยคิด — Anthropic เปิด Fable 5 แล้วต้องดับเองภายในสามวัน (3) jailbreak ที่ทำได้ในประโยคเดียว ("อ่าน codebase fix flaws") ทำให้เห็นว่า safety แบบ post-hoc filtering ไม่พอเมื่อโมเดลฉลาดพอจะหา vulnerability เอง

สำหรับ enterprise นี่คือ wake-up call เรื่อง vendor concentration risk บริษัทที่ออกแบบ workflow ทั้งระบบให้อิง model ตัวเดียว ของ provider เดียว มีความเสี่ยงที่ workflow ดับชั่วข้ามคืนด้วยเหตุผลที่ตัวเองควบคุมไม่ได้ — ไม่ใช่ outage เทคนิค แต่เป็น geopolitical event ที่ไม่มี SLA ครอบคลุม

จับตา pattern: ครั้งนี้คือสหรัฐ → Anthropic → "ความสามารถ cyber" ครั้งหน้าอาจเป็น EU AI Act → OpenAI → "ความสามารถ bio" หรือ China → DeepSeek → "ความสามารถ disinfo" ใครก็ตามที่ deploy agentic workflow บน frontier model ต้องเริ่มออกแบบ fallback ระหว่าง provider เป็น first-class architecture ไม่ใช่ afterthought

## มุม OpenBridge

โดยตรงเลย: OpenBridge ในฐานะ integration platform มี angle ที่ใหญ่กว่าที่คาดไว้ ลูกค้าที่เพิ่งเริ่มสร้าง agentic workflow จะต้องการ abstraction layer ที่ swap LLM provider ได้โดยไม่ต้อง rewrite — และเหตุการณ์ 72 ชั่วโมงนี้คือ marketing case study ที่ดีที่สุดที่จะทำให้คนเข้าใจว่าทำไมต้องมี layer นั้น เราควรชู "vendor-neutral routing" เป็น core value prop ไม่ใช่ feature เสริม

อีกประเด็น: ถ้า Fable 5 / Mythos 5 ดับนาน — โอกาสที่ enterprise จะเริ่ม pilot model จีน (DeepSeek V4, Qwen) หรือ open-weight (Llama 4.x) สูงขึ้นเพื่อกระจาย risk OpenBridge ที่ wire MCP / connector กับ provider หลายเจ้าได้แต่ต้น จะเป็น winner เพราะการ swap จะเป็น norm ไม่ใช่ exception เริ่ม internal test ตอนนี้ — sales pitch เดือนหน้าจะใช้ได้ทันที

## Sources
- [Statement on the US government directive to suspend access to Fable 5 and Mythos 5 — Anthropic](https://www.anthropic.com/news/fable-mythos-access)
- [Anthropic Disables Claude Fable 5 and Mythos 5 After US Government Order — MarkTechPost](https://www.marktechpost.com/2026/06/13/anthropic-disables-claude-fable-5-and-mythos-5-after-us-government-order/)
- [Anthropic releases Claude Fable, days after warning AI is becoming too dangerous — TechCrunch](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/)
- [When a Government Pulls an AI Model: What the Fable 5 and Mythos 5 Suspension Means for Security Teams — Snyk](https://snyk.io/blog/fable-mythos-suspension-security-takeaways/)

---

## Audio script
สวัสดีครับโย วันนี้มีเรื่องใหญ่ที่ต้องคุยกันก่อนเรื่องอื่น Anthropic ปล่อย Claude Fable 5 วันที่ 9 มิถุนายน เป็นโมเดลระดับ Mythos ตัวแรกที่เปิดให้สาธารณะใช้ Dario โฆษณาว่าเก่งที่สุดเท่าที่เคยปล่อย state-of-the-art แทบทุก benchmark โดยเฉพาะ coding กับ autonomous task แต่ผ่านไปแค่ 72 ชั่วโมง วันที่ 12 มิถุนายน 5 โมงเย็น รัฐบาลสหรัฐส่ง export-control directive มาสั่งให้ระงับการเข้าถึงจาก foreign nationals ทั่วโลก Anthropic กรอง real-time ไม่ได้ ก็เลยตัดสินใจดับให้คนใช้ทุกคน เหตุผลคือมีคนเจอ jailbreak ที่ทำง่ายเกินไป แค่บอกให้โมเดลอ่าน codebase แล้ว fix flaws มันก็จะระบุ vulnerability ให้หมด เปลี่ยนเป็นเครื่องหา zero-day อัตโนมัติ Anthropic ออกมาเถียงว่าไม่ควรถอดทั้งโมเดลเพราะ jailbreak ตัวเดียว แต่ก็ต้อง comply โมเดลตัวอื่นอย่าง Opus 4.8 ยังออนไลน์ปกตินะครับ จุดที่อยากให้โยคิดต่อมีสามอย่าง หนึ่ง frontier AI ตอนนี้ถูก treat เหมือน semiconductor รัฐสั่งดับได้ภายในไม่กี่ชั่วโมง สอง การเปิดสาธารณะกลับได้ ไม่ใช่ one-way door อีกต่อไป สาม สำหรับ enterprise นี่คือ wake-up call เรื่อง vendor concentration risk บริษัทที่ผูก workflow กับ model เดียว provider เดียว เสี่ยงดับข้ามคืนโดยไม่มี SLA ครอบคลุม สำหรับ OpenBridge ผมว่านี่คือ marketing case study ที่ดีที่สุด ที่จะอธิบายว่าทำไมต้องมี abstraction layer ที่สลับ LLM provider ได้ทันที vendor-neutral routing ควรเป็น core value prop ไม่ใช่ feature เสริมแล้วครับ
