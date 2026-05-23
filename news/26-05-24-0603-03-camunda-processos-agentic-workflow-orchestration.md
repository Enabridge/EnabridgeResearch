---
date: 2026-05-20
slug: camunda-processos-agentic-workflow-orchestration
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A futuristic control room with four glowing AI agent avatars — each represented
  as a distinct geometric shape (hexagon for Discovery, triangle for Design,
  circle for Build, diamond for Optimize) — standing around a holographic
  blueprint of a business process flowchart that morphs and rewires itself in
  real-time. Bold text "ProcessOS" rendered prominently in the upper left, with
  "4 AGENTS" in the lower right for thumbnail legibility. The background shows
  a dark enterprise server room with subtle Camunda orange accent lighting.
  Floating badges read "CLOSED BETA" and "AWS BEDROCK". Style: cinematic tech
  illustration, dark mode, neon accents on dark background, high contrast,
  1:1 aspect ratio. No human faces — agents are abstract geometric avatars.
image: images/26-05-24-0603-03-camunda-processos-agentic-workflow-orchestration.png
---

# Camunda เปิดตัว ProcessOS — ระบบปฏิบัติการ agentic ที่ใช้ 4 AI agents ปรับ business process ตั้งแต่ค้นหาจนถึง optimize

## TL;DR
- Camunda เปิดตัว ProcessOS ที่ CamundaCon Amsterdam (20 พ.ค.) — intelligence layer ที่ใช้ 4 AI agents ครอบคลุม lifecycle ของ business process: ค้นหา → ออกแบบใหม่ → build+deploy → optimize ต่อเนื่อง
- เข้า closed beta ทันที — รันบน AWS natively, integrate กับ Amazon Bedrock และ AgentCore
- เป็น direct signal ว่า workflow orchestration platform กำลังกลายเป็น "agentic OS" — ไม่ใช่แค่ workflow engine อีกต่อไป

## เกิดอะไรขึ้น

เมื่อวันที่ 20 พฤษภาคม ที่งาน CamundaCon ในอัมสเตอร์ดัม ต่อหน้าผู้นำ enterprise กว่า 1,200 คนจาก 25 ประเทศ Camunda ประกาศเปิดตัว ProcessOS — ที่บริษัทเรียกว่า "agentic operating system for business processes" แทนที่จะเป็นแค่ workflow engine ที่รัน process ที่มนุษย์ออกแบบ ProcessOS ใช้ 4 AI agents ทำงานครอบคลุมทั้ง lifecycle

Agent ตัวแรก **Discovery** วิเคราะห์ว่าองค์กร run process จริง ๆ อย่างไรในปัจจุบัน ไม่ใช่ตามที่เขียนไว้ใน documentation Agent ตัวที่สอง **Design** ออกแบบ process ใหม่ตาม outcome ที่ต้องการ Agent ตัวที่สาม **Build** generate solution เต็มรูปแบบ ทั้ง agentic process, integrations, data mapping, agent prompts, decision logic และ UI forms Agent สุดท้าย **Optimize** ติดตาม process ใน production แล้วปรับปรุงต่อเนื่อง

จุดที่น่าสนใจคือ ProcessOS สร้าง knowledge base ขององค์กรที่ compound ขึ้นเรื่อย ๆ — ทุกครั้งที่ process ใหม่ถูก deploy ระบบจะเรียนรู้ว่า pattern ไหน work ไม่ work สำหรับองค์กรนั้น ๆ ทำให้ agent ฉลาดขึ้นตามเวลา ไม่ใช่ generic AI ที่เริ่มจากศูนย์ทุกครั้ง Camunda เคลมว่า cycle time ของ process อย่าง auditing และ onboarding ลดลง 50-70% ส่วน manual tasks อย่าง data entry ลดลงถึง 80% — ตัวเลขจากบริษัทเอง ยังไม่มี third-party verification

ฝั่ง infrastructure ProcessOS รันบน AWS natively โดย integrate กับ Amazon Bedrock สำหรับ foundation models และ Amazon Bedrock AgentCore สำหรับ agent memory, identity และ gateway services เปิด closed beta ทันที 20 พ.ค. สำหรับ enterprise ที่ลงทะเบียน

## ทำไมสำคัญ

ProcessOS เป็น signal ชัดเจนว่า workflow orchestration platform กำลังเปลี่ยนจาก "เครื่องมือ run process" เป็น "ระบบปฏิบัติการที่คิดเอง" — category shift จาก BPM (Business Process Management) เป็น ABPM (Agentic Business Process Management) ถ้ามองตลาด Camunda ไม่ใช่รายเดียวที่ move ไปทางนี้ — Salesforce มี Agentforce Operations, ServiceNow มี AI agents สำหรับ workflow — แต่ Camunda เป็นรายแรกที่ frame ตัวเองเป็น "OS" ที่ agent ทำงานทั้ง lifecycle ไม่ใช่แค่ช่วยเรื่องใดเรื่องหนึ่ง

สิ่งที่ต้องจับตาคือ knowledge base ที่ compound — ถ้าใช้งานจริงได้ตามที่เคลม จะสร้าง switching cost สูงมาก เพราะ agent ที่เข้าใจ process ขององค์กรลึกขึ้นเรื่อย ๆ จะยากที่จะย้ายไป platform อื่น เป็น moat แบบ data network effect ที่ Salesforce เคยสร้างด้วย CRM data แต่ระวัง vendor claim — ProcessOS ยังอยู่ใน closed beta ยังไม่มี case study จากลูกค้าจริง

## มุม OpenBridge

เรื่องนี้ relevant ตรง ๆ กับ OpenBridge — Camunda กำลังบอกตลาดว่า "ยุคของ workflow platform ที่แค่ execute process ตาม rule จบแล้ว" ถ้า buyer enterprise เริ่ม expect ว่า platform ต้องมี agent ที่ discover, design, build, optimize process ให้ OpenBridge ต้องตอบคำถามว่า positioning จะอยู่ตรงไหนใน landscape ใหม่

ทางเลือกคือ — (1) build agentic layer ของตัวเองเหมือน Camunda แต่ focus ที่ integration workflow ไม่ใช่ BPM workflow; (2) เป็น tool layer ที่ ProcessOS เรียกใช้ผ่าน MCP ตอน Build agent ต้องสร้าง integration; หรือ (3) partner กับ Camunda ตรง ๆ เป็น preferred integration provider ใน ProcessOS marketplace ทางเลือกที่ 2 อาจเร็วที่สุดและสอดคล้องกับ MCP strategy ที่คุยกันรอบก่อน

## Sources
- [Camunda announces ProcessOS, an agentic operating system for AI-first enterprise transformation — BusinessWire](https://www.businesswire.com/news/home/20260520352437/en/Camunda-announces-ProcessOS-an-agentic-operating-system-for-AI-first-enterprise-transformation)
- [ProcessOS: The Agentic Operating System for Business Processes — Camunda](https://camunda.com/platform/process-os/)
- [Why business process reinvention is needed for agentic AI workflows — Computer Weekly](https://www.computerweekly.com/news/366643396/Why-business-process-reinvention-is-needed-for-agentic-AI-workflows)

---

## Audio script
เรื่องสุดท้ายสำคัญมากสำหรับ OpenBridge ครับ Camunda เพิ่งเปิดตัว ProcessOS ที่งาน CamundaCon ในอัมสเตอร์ดัม เป็นสิ่งที่เขาเรียกว่า agentic operating system for business processes ไม่ใช่แค่ workflow engine ธรรมดาอีกต่อไป ProcessOS ใช้ AI agent 4 ตัวทำงานครอบคลุมทั้ง lifecycle ของ business process ตัวแรก Discovery วิเคราะห์ว่าองค์กรรัน process จริงยังไง ตัวที่สอง Design ออกแบบใหม่ ตัวที่สาม Build สร้างและ deploy ตัวสุดท้าย Optimize ปรับปรุงต่อเนื่อง ที่น่าสนใจคือระบบสร้าง knowledge base ขององค์กรที่ฉลาดขึ้นเรื่อย ๆ ยิ่งใช้ยิ่งเก่ง ตอนนี้อยู่ใน closed beta รันบน AWS กับ Amazon Bedrock สำหรับ OpenBridge สิ่งที่ต้องคิดคือ Camunda กำลังบอกตลาดว่ายุคของ workflow platform ที่แค่ execute ตาม rule จบแล้ว ต้อง position ตัวเองว่าจะ build agentic layer เอง เป็น tool ให้ ProcessOS เรียกใช้ผ่าน MCP หรือ partner กับ Camunda ตรง ๆ ครับ
