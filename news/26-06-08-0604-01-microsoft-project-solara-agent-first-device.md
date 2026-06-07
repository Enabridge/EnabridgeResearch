---
date: 2026-06-07
slug: microsoft-project-solara-agent-first-device
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a sleek silver employee ID badge and a desktop hub device
  sitting side-by-side on a minimalist Microsoft-style desk. Large floating typography
  reads "PROJECT SOLARA" with the Microsoft four-square logo above and the subtitle
  "AGENT-FIRST OS" below in bold. A glowing orb of light radiates out from each device,
  with translucent agent silhouettes streaming between them and faint app icons
  dissolving into pixels at the edges. Background brand strips show Target, CVS,
  Best Buy, Levi's logos as pilot partners. Render style: cinematic editorial,
  isometric perspective, cool blue-cyan Microsoft palette with warm amber agent
  glow, high-contrast typography legible at 200px thumbnail, 1:1 aspect. No real
  human faces.
image: images/26-06-08-0604-01-microsoft-project-solara-agent-first-device.png
---

# Microsoft Project Solara — Build 2026 ปล่อย OS ใหม่ที่ "agent แทน app" พร้อม pilot กับ Target, CVS, Best Buy, Levi's

## TL;DR
- Microsoft เปิดตัว Project Solara ที่ Build 2026 — chip-to-cloud platform สำหรับ agent-first devices, fork จาก Android (MDEP) ไม่ใช่ Windows
- Reference device 2 ตัว: smart display ติดข้างจอ PC (login ด้วย face recognition + cloud Windows) และ wearable badge ที่อัด/transcribe การคุย, มี fingerprint ปลุก agent, มีกล้องในตัว
- Pilot partners ตั้งใจรุนแรง: Target, CVS Health, Best Buy, Levi's, AccuWeather เริ่มทดสอบเดือนหน้า — ไม่ใช่ pre-order page เปล่า ๆ แต่ deploy hardware จริง

## เกิดอะไรขึ้น

ที่ Build 2026 สัปดาห์ที่แล้ว Microsoft เปิด Project Solara ซึ่งเป็น chip-to-cloud platform ที่สร้างขึ้นใหม่ทั้ง stack สำหรับอุปกรณ์ที่ "รัน agent ไม่ใช่ app" สิ่งที่น่าสังเกตคือ Solara **ไม่ใช่ Windows** — มันเป็น fork ของ Android ที่เรียกว่า Microsoft Device Ecosystem Platform (MDEP) สร้างมาเฉพาะสำหรับ enterprise device ที่ agent คือ primary interface ไม่ใช่ launcher แบบเดิม

Reference device ที่ Microsoft โชว์มี 2 ตัวที่ตีกันคนละทิศ: ตัวแรกเป็น **desktop hub** ที่วางข้าง PC — ตอบคำสั่งเสียง, login ด้วย face recognition, สรุปงานเร่งด่วนของวัน, และเมื่อเสียบจอเข้าไปจะกลายเป็น Windows machine ที่รันบน cloud ทันที ตัวที่สองเป็น **wearable badge** ที่ออกแบบมาแทน employee ID เดิม — มีปุ่ม fingerprint ปลุก agent, อัด+transcribe การคุย, มีกล้องในตัว Microsoft ให้คำว่า "the next computer" และตั้งใจให้ Solara เป็นแพลตฟอร์มที่อุปกรณ์ AI-first รุ่นใหม่ของวงการรันได้

ที่ทำให้เรื่องนี้ไม่ใช่แค่ keynote slideshow คือ **pilot list ที่จริง** — Target, CVS Health, Best Buy, Levi's, AccuWeather ทั้งหมดจะเริ่มทดสอบ Solara device ในไม่กี่เดือนข้างหน้า สี่ในห้ารายเป็น Fortune 500 retailer / pharmacy / consumer electronics ที่มีพนักงาน hourly หลักหมื่นถึงแสน ซึ่งเป็นกลุ่มที่ "badge ที่คุยกับ agent ได้" น่าจะมีผลทันที — เช่น ใช้ในร้านเพื่อเช็คสต็อก, ดูตารางกะ, อนุมัติคูปองให้ลูกค้า โดยไม่ต้องเปิด POS terminal

## ทำไมสำคัญ

นี่คือ commitment ที่ใหญ่ที่สุดจาก hyperscaler ว่า **app store paradigm กำลังจะถูกแทนที่** ในบาง vertical Apple ยังไม่ขยับ, Google มี Gemini Spark แต่ยังเป็น software-only, ส่วน Microsoft ลงทุนถึงระดับ silicon-to-OS ใหม่และ recruit hardware partner ในวันแรก ที่ smart คือ Microsoft เลือกไม่ใช้ Windows — เพราะ Windows มี legacy ทั้ง driver, app, security model ที่ทำให้ agent-first ไม่คล่อง MDEP/Android เป็น clean slate ที่ตัด assumption เรื่อง user คลิก app ทิ้งไป

Pattern ที่เห็นซ้ำในรอบนี้คือ **enterprise hardware เริ่มกลับมาน่าสนใจ** หลังจาก 15 ปีที่ทุกอย่างย้ายไป BYOD/web หลัง ChatGPT ทำให้คนยอมรับ AI assistant แบบ standalone ตอนนี้ทุกค่ายเชื่อว่า dedicated agent device จะกลับมา — Humane Pin, Rabbit R1 อาจล้ม แต่ Microsoft + Target + Best Buy ไม่ใช่ scale เดียวกัน ถ้า pilot Q3 ได้ผล Solara อาจกลายเป็น "Android for the enterprise agentic era" ภายในปีหน้า

## มุม OpenBridge

OpenBridge ต้องคิดว่า **integration platform ของเราจะ surface ที่ไหนเมื่อ end-user ไม่ได้นั่งหน้า browser แล้ว** ถ้า Solara badge ของพนักงาน CVS ขอ agent ดู order status จาก SAP + Shopify + Salesforce, คนสร้าง integration นั้นอยู่ไหน? คำตอบส่วนใหญ่คือ MCP server ที่ฝัง agent connectors — และนี่คือพื้นที่ที่ OpenBridge ออกแบบมาตั้งแต่แรก ความท้าทายคือ Microsoft จะดัน Agent 365 + Copilot Connectors เป็น default integration layer บน Solara ซึ่งหมายความว่า OpenBridge ต้องวาง position ว่าเป็น **"third-party MCP catalog"** ที่ไป plug เข้า Solara ได้ ไม่ใช่ replace Microsoft stack

อีกมุมที่น่าเก็บคือ **agent observability ในระดับ device** — เมื่อ agent ทำงานบน badge ที่อัดเสียงได้และมี camera, compliance/audit logging กลายเป็น first-class concern ลูกค้า enterprise จะถามว่า "agent ทำอะไรกับข้อมูลฉันบ้าง" คำตอบนี้ OpenBridge มีโอกาสเป็น layer ที่ตอบแทน Microsoft ได้ ถ้าวาง integration log + permission scoping ที่ละเอียดกว่า

## Sources
- [Inside Microsoft's Project Solara — GeekWire](https://www.geekwire.com/2026/inside-microsofts-project-solara-a-new-platform-for-devices-that-run-ai-agents-instead-of-apps/)
- [Microsoft Project Solara: AI agents replace apps on Android — BetaNews](https://betanews.com/article/microsoft-project-solara-ai-agents-replace-apps/)
- [Microsoft Project Solara Brings AI Agents to Enterprise Devices — TechRepublic](https://www.techrepublic.com/article/news-microsoft-project-solara-ai-agents/)
- [Microsoft outlines its vision for "the next computer" — Windows Central](https://www.windowscentral.com/microsoft/project-solara-agentic-os-build-2026-announcement)
- [Build 2026: Microsoft Project Solara Envisions a Future of Agent-First Devices — Thurrott](https://www.thurrott.com/smart-tech/336967/build-2026-microsoft-project-solara-envisions-a-future-of-agent-first-devices)

---

## Audio script
สวัสดีครับ Yoh วันนี้มีข่าวที่อยากเล่าก่อนเลยคือ Microsoft เปิดตัว Project Solara ที่งาน Build 2026 ซึ่งไม่ใช่ feature ใหม่ของ Windows แต่เป็น operating system ใหม่ทั้ง stack ที่ออกแบบมาให้ agent เป็นตัวหลัก ไม่ใช่ app แบบเดิม ที่น่าสนใจคือ Microsoft เลือก fork Android มาทำ ไม่ใช้ Windows เพราะ Windows มี legacy เยอะเกินไปสำหรับ agent-first paradigm

Microsoft โชว์ device อ้างอิงสองตัว ตัวแรกเป็น desktop hub วางข้างจอ PC ที่ login ด้วย face recognition แล้วเปลี่ยนเป็น Windows บน cloud ได้ทันที อีกตัวเป็น wearable badge ที่แทน employee ID เดิม มีปุ่ม fingerprint ปลุก agent อัดเสียงและ transcribe การคุยได้ มีกล้องในตัว ที่ทำให้ข่าวนี้ไม่ใช่แค่ vaporware คือ pilot partner จริง Target, CVS Health, Best Buy, Levi's, AccuWeather เริ่มทดสอบเดือนหน้า ไม่ใช่ pre-order page เปล่า ๆ

มุม OpenBridge คือต้องเริ่มคิดแล้วว่า integration ของเราจะ surface ที่ไหนเมื่อ end-user ไม่ได้นั่งหน้า browser ถ้าพนักงาน CVS ขอ agent ดึงข้อมูลข้าม SAP กับ Shopify จาก badge บน Solara เราต้องวาง position ให้เป็น third-party MCP catalog ที่ plug เข้า Microsoft stack ได้ ไม่ใช่ไปแข่งตรง ๆ ครับ
