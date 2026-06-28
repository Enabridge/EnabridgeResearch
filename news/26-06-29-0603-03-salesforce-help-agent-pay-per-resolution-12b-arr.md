---
date: 2026-06-29
slug: salesforce-help-agent-pay-per-resolution-12b-arr
topic: use-case
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial illustration of a stylized Salesforce cloud logo on the left, dispatching
  glowing autonomous "Help Agent" robotic figures across a service desk landscape;
  each agent figure carries a tiny price tag labeled "$0 → ✓ resolved → $". A
  prominent floating dial reads "PAY-PER-RESOLUTION" with a checkmark stamp. Large
  legible numerals "$1.2B ARR" and "18,500 customers" hover prominently above the
  scene; a smaller ribbon reads "+205% YoY". Style: cinematic editorial illustration,
  isometric perspective, Salesforce sky-blue lighting with warm gold accents on
  resolved-status checkmarks, dramatic depth, high-contrast typography legible at
  200px thumbnail. No real human faces — only robotic agent silhouettes.
image: images/26-06-29-0603-03-salesforce-help-agent-pay-per-resolution-12b-arr.png
---

# Salesforce ปล่อย Help Agent + Pay-per-Resolution — agent business model ใหม่ที่ "ไม่แก้ได้ ไม่เก็บเงิน", พ่วงตัวเลข Agentforce $1.2B ARR / 18,500 ลูกค้า / +205% YoY

## TL;DR
- 25 มิ.ย. Salesforce launch **Agentforce Help Agent** บน Agentforce 360 — เก็บเงินเฉพาะตอนที่ agent **แก้ปัญหา end-to-end สำเร็จเองเท่านั้น**, ลูกค้า escalate ไป human หรือให้ negative feedback = ไม่ชาร์จ
- Agentforce รวมข้าม product line ขึ้นแตะ **$1.2B ARR** ใน 18,500 ลูกค้า — โต **205% YoY** ตัวเลข AI+data ARR รวม $3.4B
- PenFed Credit Union เป็น early customer ที่ confirm public — vertical แรกที่ active rollout คือ financial services / service org เน้น omnichannel (voice + web + portal + messaging)

## เกิดอะไรขึ้น

วันที่ 25 มิ.ย. 2026 Salesforce ประกาศ **Agentforce Help Agent** — autonomous service agent ที่ pre-packaged เข้า Agentforce 360 Platform โดยมี twist สำคัญที่เปลี่ยน agent economics ของทั้งอุตสาหกรรม: **pay-per-resolution** เก็บเงินเฉพาะเมื่อ agent ปิด case ได้แบบ end-to-end ลูกค้าไม่ได้ escalate ไป human, ไม่ได้กด thumbs-down, ระบบเห็นว่าปัญหาถูกแก้จริง — เก็บเงินตอนนั้น ถ้าไม่ — Salesforce ไม่ชาร์จ ไม่มีค่า seat ไม่มีค่า base subscription ของ agent

นี่คือ pricing model ที่ vendor agentic AI เกือบทุกเจ้าพูดมา 12 เดือนแต่ไม่กล้าทำจริง เพราะ vendor risk ทั้งหมดไปอยู่กับ accuracy ของ model — ถ้า agent ห่วย vendor เก็บเงินไม่ได้เลย Salesforce กล้าทำเพราะเชื่อ accuracy ของ Agentforce หลังจาก iteration อยู่หลายรุ่น + มี deflection rate ที่สูงพอใน early production คาดเดาได้ว่า cohort นี้คือลูกค้า PenFed Credit Union, Wiley และ Indeed ที่ Marc Benioff ยกใน earnings call หลายรอบที่ผ่านมา

ตัวเลขที่ Salesforce แปะมาด้วยตอน launch ก็ frame ของ Help Agent ได้ชัด: **Agentforce รวมทั้ง product line ขึ้นแตะ $1.2B ARR ใน 18,500 ลูกค้า โต 205% YoY** AI + data ARR รวม $3.4B Q1 FY27 revenue โดยรวม $11.1B โต 13% YoY (FY26 ปิดที่ $41.5B โต 10%) — ตัวเลขเหล่านี้บอกว่า agentic AI ไม่ใช่ experimental cost center อีกต่อไป แต่เป็น growth engine ที่ขับ topline ของ Salesforce ทั้งบริษัท

Help Agent ใช้งานผ่าน guided setup ที่ Salesforce พยายาม brand ว่า "ไม่ต้องเขียน code" — มี prepackaged workflow action, deploy ข้าม voice + web + portal + messaging จาก config interface เดียว target ตรง ๆ คือลูกค้าที่ก่อนหน้านี้ตอบว่า "ผมต้องการ AI agent แต่ทีม implement ผมไม่พอ" — Salesforce พยายามตัด activation barrier ทิ้งทั้งหมด

## ทำไมสำคัญ

Pay-per-resolution คือ **business model innovation ที่สำคัญกว่า model capability ใด ๆ** ที่ Salesforce ship มาในรอบปีนี้ — เพราะมันเปลี่ยนทั้ง risk allocation ระหว่าง vendor กับ enterprise: enterprise มี cost certainty (จ่ายตามผลลัพธ์ที่จับต้องได้, ไม่จ่ายกับ false positive), vendor ต้อง keep skin in the game (accuracy พังเมื่อไหร่ revenue หายเมื่อนั้น) เป็นการบีบให้ Salesforce ต้อง invest ใน eval + safety เพิ่ม เพราะมันสะท้อนตรง ๆ ใน P&L ของตัวเอง

Pattern นี้จะกดดัน competitor หนักมาก ServiceNow, Microsoft (Copilot), Google (Gemini Enterprise), Zendesk Answer Bot ที่ขายเป็น seat license แบบเดิม — ลูกค้าจะถาม "ทำไมต้องจ่ายก่อนรู้ผล" CFO หลายเจ้าจะ insist ว่าต้องมี pay-per-outcome option ก่อนจะต่อ contract Forrester / Gartner รายงานปลายปี 2025 บอกว่า 67% ของ enterprise procurement team ระบุ "outcome-based pricing" เป็น top-3 selection criteria สำหรับ AI agent ปี 2026 — Salesforce เป็น first mover ที่กล้าทำในระดับ flagship product

ตัวเลข 205% YoY กับ 18,500 ลูกค้า บอกอีกอย่างที่สำคัญ: **agentic AI ไม่ใช่ enterprise-only แล้ว** 18,500 ลูกค้าเทียบกับ ~150,000 ลูกค้า Salesforce ทั้งหมด คือ ~12% penetration ใน 18 เดือน — pace ที่ Salesforce รับมาในยุค cloud transformation ไม่เคยมีรุ่นไหนเร็วขนาดนี้ ความหมายคือ SMB / mid-market ใน Salesforce ecosystem ก็เริ่มซื้อ Agentforce แล้ว ไม่ใช่แค่ Fortune 500

## มุม OpenBridge

Pay-per-resolution model บอก signal ให้ OpenBridge สองข้อ ข้อแรก **ลูกค้า enterprise ของ OpenBridge ที่ใช้ Agentforce อยู่แล้ว — และที่จะใช้เพิ่ม — จะต้องการ integration layer ที่ feed context cross-system ให้ accurate ขึ้น เพราะ accuracy = revenue ของ vendor** ถ้า OpenBridge connector ของ Salesforce-to-X (SAP, NetSuite, ERP, billing) ช่วยให้ Help Agent ปิด case ได้ end-to-end สำเร็จ เพราะมี data จาก system อื่น — value prop ของเรา link ตรงกับ ROI ที่ลูกค้าจ่าย Salesforce

ข้อสอง — และอาจสำคัญกว่า — **OpenBridge เองควร consider pay-per-outcome pricing ในบาง use case** ลูกค้าที่ deploy integration เพื่อ feed agent อยู่แล้ว จะยอมจ่ายถ้าเรา price ตาม "จำนวน successful agent action" ที่วิ่งผ่านเรา ไม่ใช่ flat per-connector / per-record เหมือนเดิม Salesforce กำลังเปิด market education ให้เราอยู่ใน category นี้ฟรี ๆ เราต้อง piggyback ทันที — มิเช่นนั้นจะกลายเป็น "iPaaS เก่าที่ยังคิดราคาแบบ 2015" ในขณะที่ vendor ใหญ่กว่ารู้จัก outcome-based แล้ว

## Sources
- [Salesforce Debuts Help Agent With Pay-Per-Resolution AI — CMSWire](https://www.cmswire.com/contact-center/salesforce-debuts-help-agent-with-payperresolution-ai/)
- [Salesforce credits agentic AI with driving revenue in Q1 2027 — Digital Commerce 360](https://www.digitalcommerce360.com/article/salesforce-revenue/)
- [Agentforce Statistics and Trends (2025-2026) — Cyntexa](https://cyntexa.com/blog/agentforce-statistics-and-trends/)
- [Salesforce Agentforce Guide 2026: Products, AI Agents & Use Cases — Vantagepoint](https://vantagepoint.io/blog/sf/the-complete-guide-to-salesforces-agentforce-ecosystem-understanding-the-full-product-portfolio-in-2026)
- [AI's next act: how Salesforce is turning efficiency gains into revenue — Fortune](https://fortune.com/2026/04/18/salesforce-agentforce-ai-efficiency-revenue-growth/)

---

## Audio script
สวัสดีครับ Yoh เรื่องที่สาม Salesforce เพิ่ง launch Agentforce Help Agent เมื่อวันที่ 25 มิถุนายน พร้อม pricing model ใหม่ที่จะเปลี่ยน agent economics ของทั้งอุตสาหกรรม pay per resolution เก็บเงินเฉพาะเมื่อ agent แก้ปัญหา end to end สำเร็จจริง ลูกค้า escalate ไป human หรือกด thumbs down ไม่ชาร์จ ไม่มีค่า seat ไม่มี base subscription นี่คือ pricing model ที่ vendor agentic AI หลายเจ้าพูดมา 12 เดือนแต่ไม่กล้าทำ เพราะ vendor risk ทั้งหมดไปอยู่กับ accuracy ของ model Salesforce กล้าทำเพราะเชื่อ accuracy ของ Agentforce หลังจาก iteration หลายรุ่น ตัวเลขที่ stamp มาด้วยตอน launch คือ Agentforce รวมแตะ 1.2 พันล้านดอลลาร์ ARR ใน 18,500 ลูกค้า โต 205% YoY AI plus data ARR รวม 3.4 พันล้านดอลลาร์ pattern นี้จะกดดัน ServiceNow Microsoft Copilot Google Gemini Enterprise Zendesk ที่ขายเป็น seat license หนัก CFO หลายเจ้าจะ insist ต้องมี pay per outcome option ก่อนต่อ contract สำหรับ OpenBridge สอง signal ข้อแรก ลูกค้าที่ใช้ Help Agent อยู่ต้องการ integration layer ที่ feed cross system context ให้ accurate ขึ้น เพราะ accuracy เท่ากับ revenue ของ Salesforce value prop ของเรา link ตรงกับ ROI ที่ลูกค้าจ่าย ข้อสอง OpenBridge เองควร consider pay per outcome pricing ใน use case ที่ feed agent อยู่แล้ว Salesforce กำลังเปิด market education ให้เราอยู่ใน category นี้ฟรี เราต้อง piggyback ไม่ให้กลายเป็น iPaaS เก่าที่ยังคิดราคาแบบยุคปี 2015 ครับ
