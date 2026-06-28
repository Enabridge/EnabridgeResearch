---
date: 2026-06-29
slug: anthropic-mythos-5-us-commerce-clears-trusted-partners
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial illustration of a giant blueprint-style US government seal stamping a glowing
  Anthropic logo orb, releasing it through a steel vault door that opens onto a corridor
  of corporate skyscrapers labeled "Apple, Google, Microsoft, Nvidia, Cisco". A second
  smaller orb labeled "Fable 5" remains locked inside the vault. Large legible numerals
  "~200 partners" and "Mythos 5" float prominently above the scene; a small ribbon
  beneath reads "Project Glasswing". Style: cinematic editorial illustration, isometric
  perspective, cool steel-blue lighting with warm Anthropic amber glow on the released
  orb, dramatic depth, high-contrast typography legible at 200px thumbnail. No real
  human faces.
image: images/26-06-29-0603-01-anthropic-mythos-5-us-commerce-clears-trusted-partners.png
---

# Anthropic Mythos 5 — Commerce ปลดล็อก ~200 trusted partners หลัง export-control freeze 2 สัปดาห์, Fable 5 ยังโดนล็อกอยู่

## TL;DR
- 26 มิ.ย. Commerce Secretary Howard Lutnick เซ็นจดหมายถึง co-founder Tom Brown อนุญาตให้ Anthropic เปิด Claude Mythos 5 ให้ "trusted partners" ประมาณ 200 รายที่อยู่ใน Project Glasswing — รวม Apple, Google, Microsoft, Nvidia, Cisco
- ของเดิมโดน freeze ทั้งดุ้นวันที่ 12 มิ.ย. เพราะ Amazon ส่ง concern เรื่อง jailbreak ไปถึง Treasury แล้ว Lutnick invoke export-control authority สั่ง shut off
- **Fable 5** (รุ่น general-purpose) ยังไม่ปลดล็อก — message ชัดว่า US Gov เลือก "approve เป็นรายชื่อ" สำหรับ defensive cyber/critical infra เท่านั้น ไม่ใช่ broad consumer access

## เกิดอะไรขึ้น

วันที่ 12 มิ.ย. 2026 Commerce Department อ้างอำนาจ export-control สั่ง Anthropic ปิด access ทั้ง Mythos 5 และ Fable 5 ทุก foreign national ทั่วโลก — เป็นครั้งแรกที่ frontier model lab โดน freeze โดยรัฐบาลในระดับนี้ เหตุผลตื้น ๆ คือ "national security risk" แต่ของจริงตามที่ Bloomberg/CNBC รายงานคือ **Amazon ส่ง internal concern เรื่อง jailbreak ไปถึง Treasury Secretary Scott Bessent** ว่าโมเดล Anthropic ที่เป็น partner หลักของตัวเอง สามารถถูก adversary ใน China/Russia ใช้ทำ offensive cyber ได้ Treasury ส่งต่อให้ Lutnick แล้ว Lutnick ก็ไม่ลังเล

สองสัปดาห์ต่อมา (26 มิ.ย.) Lutnick เซ็นจดหมายถึง Tom Brown ระบุว่า "Anthropic ได้ทำงานร่วมกับ US Gov เพื่อแก้ความเสี่ยงของ Covered Models สำเร็จในระดับที่น่าพอใจ" — และอนุญาตให้ Mythos 5 กลับมาให้ใช้ได้กับ trusted partners ราว 200 ราย ส่วนใหญ่อยู่ใน Project Glasswing ซึ่ง Anthropic launch ไปเมื่อหลายเดือนก่อนเพื่อเปิด Mythos ให้ภาค cyber defense + critical infrastructure (Apple, Google, Cisco, Nvidia, Microsoft confirm public แล้วว่าอยู่ในรายชื่อ) Fortune รายงานตัวเลข "ประมาณ 200" CNBC บอก "ประมาณ 100" — ตัวเลขจริง Annex A ที่แนบจดหมายยังไม่ public

ของที่น่าสังเกตคือ **Fable 5 — รุ่น general-purpose ที่มี additional safeguards ที่ Anthropic บอกว่าเข้มกว่า — ยังไม่ได้รับอนุญาต** Tom Brown บอก expect ว่า conversation กับ government จะดำเนินต่อไป สำหรับ technical mitigation ที่ Anthropic ทำเพื่อให้ผ่าน — ไม่มีรายละเอียด public ออกมา ทั้ง Lutnick และ Anthropic ระบุแค่ว่า "appropriate safeguards in place" และ "diversion-risk assessment ผ่าน"

Lutnick กับ Tom Brown ประชุมกันหลายรอบในช่วง 14 วันที่ freeze — เห็นได้ชัดว่ารัฐบาลใช้ freeze เป็น leverage บีบให้ Anthropic ลงทุน technical guardrail เพิ่ม ก่อนปล่อยกลับ ผลคือ "approved list" ที่ตัวบริษัทเองคุมไม่ได้ — ใครอยากใช้ Mythos 5 ต้องผ่านการคัดของ Commerce Department

## ทำไมสำคัญ

นี่คือ **moment ที่ frontier model access กลายเป็น export-controlled commodity เต็มตัว** เหมือน semiconductor ขั้นสูง — ไม่ใช่แค่ chip รุ่น Blackwell ที่ขายไป China ไม่ได้แล้ว แต่รวมถึง weight + inference endpoint ของโมเดลด้วย Pattern นี้คาดเดาได้มานานแล้วตั้งแต่ Biden ออก AI executive order ปี 2024 แต่นี่คือครั้งแรกที่ Commerce ใช้อำนาจจริง freeze แบบรายบริษัท + รายโมเดล แล้วบังคับให้ negotiate กลับมาเป็น "approved list" — สิ่งที่ Anthropic จะต้อง deal กับมันทุกครั้งที่ปล่อย flagship รุ่นใหม่ต่อจากนี้

ส่วนที่ Amazon เป็นต้นเรื่องน่าคิดมาก — Amazon ลงทุน Anthropic ไป $8B กว่า เป็น cloud partner หลัก แต่กลับเป็นคนส่ง concern ขึ้นไป Treasury ตีความได้สองทาง: (1) Amazon เห็น real risk จาก inside ที่ Anthropic เองยังไม่เห็น (2) Amazon ใช้ government เป็น leverage บีบ Anthropic ให้ commercial term ที่ดีขึ้น ไม่ว่าทางไหน signal ชัดว่า cloud hyperscaler ที่เป็น investor มี power ในการ shape access policy ของ frontier model partner ตัวเอง — เปลี่ยน power dynamic ของ ecosystem ทั้งหมด

Pattern Project Glasswing ที่เป็น "ชื่อ ๆ ใหญ่ ๆ ใน cyber defense" จะกลายเป็น template ของยุคต่อจากนี้ — ทุก frontier lab จะต้องมี "approved enterprise list" ของตัวเอง ไม่ใช่แค่ pricing tier แต่เป็น **regulatory tier** ลูกค้านอกรายชื่อจะใช้ได้แค่รุ่น 2nd-tier (เช่น Sonnet/Haiku) ที่ไม่ติด national-security threshold

## มุม OpenBridge

นี่ไม่ใช่ข่าวที่ OpenBridge "ใช้ได้ตรง ๆ" แต่เป็น **structural signal ที่ต้อง factor เข้า product narrative** สำหรับลูกค้า enterprise ของเรา โดยเฉพาะลูกค้าในเอเชีย ตะวันออกกลาง หรือ multinational ที่มี subsidiary ใน China/Russia — ลูกค้าเหล่านี้จะเริ่มถาม "ใช้ Mythos 5 ผ่าน OpenBridge ได้ไหม" คำตอบของเราต้องเป็น "neutral routing layer" ที่ swap model ไป Fable 4 / Sonnet / Gemini / DeepSeek ได้แบบ transparent ไม่ลูกค้าค้างเมื่อ vendor หลักโดน geo-restriction

อีกมุมที่สำคัญกว่าคือ **trust + auditability layer ที่ enterprise ต้องการเพิ่มขึ้นหลังจากเหตุการณ์นี้** — ลูกค้า financial / healthcare / gov จะ insist ว่าต้อง audit ได้ว่าโมเดลที่ใช้คือรุ่นไหน, ใช้ผ่าน endpoint อะไร, มี approved status อย่างไร OpenBridge มีโอกาส position "model governance + routing" เป็น feature ที่ enterprise ต้องการมากขึ้นไม่ใช่ nice-to-have อีกต่อไป — ตลาดเพิ่งรับรู้ว่า "model อาจถูก freeze โดย regulator ข้ามคืน" และ procurement team ต้องการ insurance policy

## Sources
- [Trump admin allows Anthropic to release Mythos AI model to some companies, government agencies — CNBC](https://www.cnbc.com/2026/06/26/us-government-anthropic-claude-mythos5-ai.html)
- [Anthropic's Mythos 5 AI Model Cleared by US for Wider Use — Bloomberg](https://www.bloomberg.com/news/articles/2026-06-26/us-allows-trusted-partners-to-use-anthropic-s-mythos-5-ai-model)
- [Anthropic's Mythos 5 AI model cleared by U.S. for wider use — Fortune](https://fortune.com/2026/06/27/anthropic-mythos-5-ai-model-us-commerce-department-clearance-fable/)
- [Federal government permits release of Anthropic's Mythos model to select companies — The Hill](https://thehill.com/policy/technology/5943549-anthropic-mythos-5-access/)
- [U.S. government gives Anthropic green light for limited re-release of Mythos 5 — NBC News](https://www.nbcnews.com/tech/tech-news/us-government-gives-anthropic-green-light-limited-re-release-mythos-5-rcna352018)
- [U.S. partially reverses Anthropic AI ban for Mythos but keeps Fable 5 off the market — Neowin](https://www.neowin.net/news/us-partially-reverses-anthropic-ai-ban-for-mythos-but-keeps-fable-5-off-the-market/)

---

## Audio script
สวัสดีครับ Yoh เช้านี้มีข่าวใหญ่ระดับ structural ที่ต้องรู้ Anthropic เพิ่งได้รับอนุญาตจาก Commerce Secretary Howard Lutnick ให้กลับมาเปิด Claude Mythos 5 ให้ trusted partners ประมาณ 200 รายในรายชื่อ Project Glasswing ซึ่งรวม Apple Google Microsoft Nvidia และ Cisco หลังจากที่โดน export control freeze ทั้งดุ้นเมื่อวันที่ 12 มิถุนายน เรื่องเดิมคือ Amazon เป็นคนส่ง concern เรื่อง jailbreak ไปถึง Treasury ก่อน Lutnick จะ invoke export control authority สั่ง shut off ทั้ง Mythos 5 และ Fable 5 ที่ต้องสังเกตคือ Fable 5 รุ่น general purpose ยังไม่ได้ปลดล็อก รัฐบาลเลือก approve เป็นรายชื่อสำหรับ defensive cyber กับ critical infrastructure เท่านั้น ไม่ใช่ broad access โดยทั่วไป นี่คือ moment ที่ frontier model access กลายเป็น export controlled commodity เต็มตัวเหมือน semiconductor ขั้นสูง ทุก frontier lab จากนี้จะต้องมี approved enterprise list ของตัวเอง สำหรับ OpenBridge ข่าวนี้ไม่กระทบเราตรง ๆ แต่เป็น structural signal สำคัญ ลูกค้า enterprise ในเอเชียและตะวันออกกลางจะเริ่มถามว่า swap model อัตโนมัติได้ไหมเมื่อ vendor หลักโดน geo restriction และจะต้องการ model governance plus routing เป็น feature ที่ audit ได้ ตลาดเพิ่งเห็นว่า model อาจถูก freeze โดย regulator ข้ามคืน procurement team จึงต้องการ insurance policy ที่ neutral routing layer ตอบโจทย์ ได้พอดีครับ
