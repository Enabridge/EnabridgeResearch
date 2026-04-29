---
date: 2026-04-30
slug: sereact-110m-cortex-world-model-robotics
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: Editorial illustration of a translucent robotic arm reaching toward a swirling sphere of light that contains miniature 3D physics simulations, set against an industrial warehouse backdrop with conveyor belts, minimal flat geometric shapes, muted slate gray and electric cyan palette, dramatic side-lighting, no text no logos no faces
image: images/26-04-30-0602-04-sereact-110m-cortex-world-model-robotics.png
---

# Sereact ระดม $110M Series B — Cortex 2.0 ใส่ "world model" ลง VLA แล้วกระโดดเข้าสหรัฐ: physical AI ผ่านจุด human-takeover 1 ใน 53,000 pick

## TL;DR
- 27 เม.ย. — Sereact (Stuttgart, Germany) ระดมทุน Series B $110M (€93M) นำโดย Headline; ผู้ลงทุนรวม Bullhound, Daphni, Felix Capital; รวม disclosed funding $140M+ (Series B = 4x ของ Series A)
- เปิดตัว **Cortex 2.0** — บริการ "robotic brain" ที่เพิ่ม **world model** เข้าไปใน vision-language-action (VLA) baseline; รัน possible action ผ่าน learned physics simulation ก่อนเลือก action ที่น่าจะ work ที่สุด + adapt real-time เมื่อ scene เปลี่ยน
- Production reality: **200+ Cortex systems deployed ใน Europe**; **1B+ production picks** สำเร็จ; human takeover rate = **1 ใน 53,000 picks** (≈ 0.0019%); ลูกค้ารวม BMW, PepsiCo; Boston US office จะเปิด summer 2026

## เกิดอะไรขึ้น

วันที่ 26 เมษายน 2026 Sereact, robotics software startup จาก Stuttgart ประเทศเยอรมนี ประกาศ Series B ขนาด $110M (เทียบเท่าประมาณ €93M) นำโดย Headline พร้อมผู้ลงทุนรวม Bullhound Capital, Daphni, Felix Capital — round นี้ใหญ่กว่า Series A ของบริษัทกว่า 4 เท่า และทำให้ disclosed funding ทั้งหมดของ Sereact ขึ้นไปที่ $140M+ ในรอบ 3 ปี

สิ่งที่ Sereact ขายไม่ใช่ฮาร์ดแวร์หุ่นยนต์ — เป็น **software platform** ที่ทำให้หุ่นยนต์ที่มีอยู่แล้วของลูกค้า (jaw gripper, robotic arm, mobile picker จาก vendor หลากหลาย) "ฉลาดพอ" ที่จะหยิบของในคลังสินค้าหรือสายการผลิตที่ของไม่ได้ stack เรียงเป็นระเบียบ ลูกค้าหลักของ Sereact คือ **BMW** ที่ใช้ในสายการประกอบรถ + **PepsiCo** ที่ใช้ในศูนย์กระจายสินค้า — และ press release ระบุว่า "200+ Cortex systems deployed across Europe" ปัจจุบัน

ตัวเลขที่น่าทึ่งที่สุดในประกาศ: ตั้งแต่เริ่ม deploy ระบบ Sereact ทำ production picks สะสมไปแล้วมากกว่า **1,000,000,000 (หนึ่งพันล้าน) picks** ในสภาพแวดล้อมจริง — ที่ของไม่เรียง, lighting เปลี่ยน, มี occlusion, มี item ที่ไม่อยู่ใน training distribution — และ human takeover rate (จำนวนครั้งที่ระบบขอให้คน intervene เพราะมั่นใจไม่พอ) อยู่ที่ **1 ใน 53,000 picks** หรือประมาณ 0.0019% ตัวเลขนี้คือ benchmark ที่จะถูกอ้างถึงในวงการ logistics + manufacturing automation เป็นปีอย่างน้อย ๆ เพราะเทียบกับคู่แข่ง horizontal ที่ตัวเลขเดียวกันอยู่ที่ 1 ใน 500–2,000 picks

จุดเปลี่ยนคือ release **Cortex 2.0** ที่ประกาศพร้อมระดมทุน — Cortex 2.0 อัพเกรดจาก vision-language-action (VLA) model baseline (ที่เห็น scene + รับ command + generate action) โดยเพิ่ม **world model** เข้าไป ก่อนที่หุ่นยนต์จะเคลื่อนไหว Cortex 2.0 รัน possible action หลายแบบผ่าน learned simulation ของ physics + object behavior แล้วเลือก action ที่ "predicted to work best" + ใน scene ใหม่ที่ลักษณะของ object ไม่เคยเจอมาก่อน Cortex 2.0 update world model ของตัวเอง real-time จาก feedback ของ sensor

CEO และ co-founder Ralf Gulde บอก Bloomberg ว่า "VLA models alone hit a ceiling because they react to what they see — they can't predict consequences. Adding a world model lets the robot think before it moves" — และ pattern เดียวกันคือสิ่งที่ Physical Intelligence (Pi), Skild AI, และ DeepMind RT-2/RT-X ทุกค่ายกำลังเดินตาม

Sereact ใช้ทุนรอบนี้ทำสามอย่าง: (1) เปิด US office แรกที่ Boston ใน summer 2026 hire ทีม commercial, application engineering, sales locally; (2) scale Cortex 2.0 deployment ไปสู่ logistics customer ใน North America; (3) expand R&D ใน Stuttgart โดย hire ทีมจากภาคอุตสาหกรรมยานยนต์เยอรมัน + AI lab ใหญ่

## ทำไมสำคัญ

ปี 2025–2026 เป็นยุคที่ "physical AI" ผ่านจุด threshold ของการ commercial scale Pi ระดมทุน $400M ที่ valuation $5.6B ใน ก.พ., Skild ระดมทุน $300M ใน ม.ค., Bezos ตั้ง Prometheus ที่ $38B valuation ใน เม.ย. — ทั้งหมดเป็น bet ว่า VLA + world model จะเปลี่ยน economics ของ warehousing, manufacturing, last-mile fulfillment ในอีก 24-36 เดือน Sereact คือคนที่ **มี production data จริง** ที่ใหญ่ที่สุดในยุโรปและกำลังจะ scale ข้ามมหาสมุทร

ตัวเลข 1 ใน 53,000 pick = human takeover rate คือ **bar ใหม่ที่ทุก operator คลังสินค้าจะใช้ใน RFP** ใน 12 เดือนหน้า เพราะ unit economics ของ warehouse automation ขึ้นอยู่กับ takeover rate โดยตรง — ถ้า takeover rate = 1 ใน 1,000 ต้องมี human supervisor 1 คนต่อ 5-8 robot, ถ้า 1 ใน 50,000 supervisor 1 คนคุม 50+ robot ได้ ROI ของ deployment เปลี่ยนไป 5-10x เพราะ labor ที่ประหยัดมากขึ้นมาก — Sereact ทำตัวเลขนี้ได้ใน production จริงไม่ใช่ lab demo

ที่น่าสนใจกว่าตัวเลขคือ **architecture choice** — Sereact bet บน "VLA + world model + real-time updating" ไม่ใช่ "ใหญ่ขึ้น train ยาวขึ้น" ที่ frontier lab ทั่วไปทำ และตัวเลขที่ออกมา validate ทาง model นี้ — Pi, Skild, Sereact ทุกค่ายกำลัง converge ไปทาง world model เหมือน ๆ กัน ซึ่งเทียบได้กับช่วงที่ NLP ทุกค่าย converge ไปทาง transformer ในปี 2018-2019 architecture sweep รอบใหม่ของ physical AI กำลังสรุปให้เห็นว่า world model + VLA + sim-to-real loop คือ winning formula

ความเสี่ยงระยะกลาง: ถ้า Tesla Optimus หรือ Figure AI จาก US ทำ humanoid generalist สำเร็จด้วย transformer scale อย่าง brute-force (training compute 10-100x), specialized vertical robot อย่าง Sereact อาจเสีย market บน edge case ที่ humanoid ทำได้ — แต่ในระยะ 24-36 เดือน Sereact ที่ focused warehouse + production line น่าจะปลอดภัย เพราะ ROI per pick ของ specialized arm ดีกว่า humanoid 5-10x ในงาน narrow

## มุม OpenBridge

ไม่ direct เกี่ยว เพราะ OpenBridge อยู่ software workflow layer ไม่ใช่ physical robotics — แต่มี **adjacent insight 3 ข้อ** ที่ควรจดไว้:

(1) **Benchmark "human takeover rate" จะถูกย้ายเข้า software agent world ในอีก 6-12 เดือน** — Monte Carlo รายงานล่าสุดที่เราเขียนเมื่อ 28 เม.ย. ระบุว่า 64% ของ enterprise ส่ง agent ก่อนพร้อม + 86-89% ของ pilot ไม่ scale; ตัวเลขที่ enterprise customer จะเริ่มถามใน RFP คือ "agent ของคุณต้องให้คน intervene กี่ครั้งต่อ 1,000 task" ที่ Sereact ตั้ง bar ในโลก physical (1 ใน 53,000) จะเป็น analog ของ bar ใน software agent (เป้าควรจะอยู่ที่ 1 ใน 100-1,000 task ในระยะแรก) — OpenBridge ควรมี **takeover rate metric** เป็น first-class observability feature ตั้งแต่ตอนนี้ และเริ่ม benchmark กับลูกค้า

(2) **World model + sim-loop pattern จะถูก port เข้า software agent** — software agent ที่ดีกว่าจะเริ่มเป็น agent ที่ "simulate consequences ก่อน act" — เช่น agent procurement ที่ simulate price negotiation ก่อนส่ง offer, agent customer support ที่ simulate response branch ก่อน reply, agent ops ที่ simulate downstream impact ก่อนสั่ง action; OpenBridge สามารถออกแบบ workflow primitives ที่ encourage pattern นี้ — "dry-run mode" + "expected outcome simulation" เป็น first-class step

(3) **Physical AI deployment + software agent deployment จะรวมกันเร็ว** — ถ้าลูกค้า logistics ของไทย (Kerry, Flash, J&T) เริ่ม deploy Sereact-class robot ใน warehouse, OpenBridge ที่อยู่ orchestration layer ของ workflow IT ของลูกค้าจะมีโอกาสเชื่อม physical agent + software agent เข้า workflow เดียวกัน — เช่น agent ที่รับ order จาก Shopee → trigger Sereact pick robot → software agent ติดตาม shipment → autonomous customer notification — ตลาดนี้ยังไม่มีใครจับ ASEAN และเป็น optionality ที่ควร watch

## Sources
- [Sereact raises $110M to scale AI 'robotic brain' and expand into the US — SiliconANGLE](https://siliconangle.com/2026/04/27/sereact-raises-110m-scale-ai-robotic-brain-expand-us/)
- [AI Startup Sereact Raises $110 Million for Robots That Predict Consequences — Bloomberg](https://www.bloomberg.com/news/articles/2026-04-27/ai-startup-sereact-raises-110-million-for-robots-that-predict-consequences)
- [Sereact raises $110 million Series B to scale Cortex 2 and enter US robotics market — Robotics & Automation News](https://roboticsandautomationnews.com/2026/04/27/sereact-raises-110-million-investment-to-advance-its-world-model-for-robotics-and-ai/101043/)

---

## Audio script
Yoh วันนี้มีเรื่อง physical AI จากเยอรมัน Sereact ระดม Series B 110 ล้านดอลลาร์ นำโดย Headline ทำให้ funding รวม 140 ล้าน Series B ใหญ่กว่า Series A กว่า 4 เท่า Sereact ขายไม่ใช่หุ่นยนต์ฮาร์ดแวร์ — เป็น software platform ทำให้หุ่นยนต์ของลูกค้าฉลาดพอที่จะหยิบของในคลังสินค้าที่ของไม่เรียงเป็นระเบียบ ลูกค้าหลักรวม BMW PepsiCo deploy ไปแล้วกว่า 200 ระบบทั่วยุโรป ตัวเลขที่ทึ่งที่สุดคือทำ production picks สะสมเกิน 1 พันล้าน pick และ human takeover rate อยู่ที่ 1 ใน 53000 pick — เทียบคู่แข่งทั่วไปอยู่ที่ 1 ใน 500-2000 pick ทำให้ ROI ของ warehouse automation เปลี่ยน 5-10 เท่า จุดเปลี่ยนคือ Cortex 2.0 ที่ปล่อยพร้อมระดมทุน — เพิ่ม world model เข้าไปใน vision-language-action baseline หุ่นยนต์รัน possible action ผ่าน learned physics simulation ก่อนเคลื่อน CEO Ralf Gulde บอกว่า VLA model อย่างเดียว hit ceiling เพราะ react แต่ predict ไม่ได้ — เพิ่ม world model ทำให้ robot คิดก่อน act pattern เดียวกันที่ Pi Skild DeepMind ทุกค่ายกำลังเดินตาม Sereact จะเปิด US office ที่ Boston summer 2026 มุม OpenBridge ไม่ direct เกี่ยวเพราะอยู่ software layer แต่ adjacent insight สามข้อสำคัญมาก หนึ่ง human takeover rate จะถูกย้ายเข้า software agent world ใน 6-12 เดือน enterprise จะเริ่มถามใน RFP ว่า agent ของคุณให้คน intervene กี่ครั้งต่อ 1000 task OpenBridge ควรมี takeover rate metric เป็น first-class observability feature ตอนนี้ สอง world model + sim-loop pattern จะถูก port เข้า software agent — agent ที่ดีกว่าจะ simulate consequence ก่อน act เช่น agent procurement simulate negotiation ก่อนส่ง offer สาม physical AI กับ software agent deployment จะรวมกันเร็ว ลูกค้า logistics ไทย Kerry Flash J&T ที่ deploy Sereact-class robot จะมี optionality ที่ OpenBridge เชื่อม physical agent + software agent เข้า workflow เดียวกัน — ตลาดนี้ยังไม่มีใครจับ ASEAN
