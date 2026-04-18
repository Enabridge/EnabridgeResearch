---
date: 2026-04-18
slug: atlassian-ai-training-data
topic: openbridge-trend
reading_time_min: 2
sources: 2
---

# Atlassian จะดูดข้อมูลลูกค้าไป train AI ตั้งแต่ ส.ค. — opt-out ได้แค่ Enterprise tier

## TL;DR
- Atlassian ประกาศ (16-17 เม.ย.) — เริ่ม **17 ส.ค. 2026** จะเอา metadata + in-app data จาก Jira/Confluence/cloud product ทั้งหมดไป train AI ของบริษัท
- Free/Standard: opt-in โดย default, opt-out ได้; **Premium/Enterprise: off โดย default**; metadata เฉพาะ Enterprise เท่านั้นที่ opt-out ได้
- กระทบ ลูกค้า 300,000 องค์กรทั่วโลก, settings rollout เริ่มแล้ว 16 เม.ย.

## เกิดอะไรขึ้น
17-18 เม.ย. 2026 The Register และอื่น ๆ รายงานนโยบายใหม่ Atlassian — เริ่ม 17 ส.ค. 2026 บริษัทจะ collect data 2 ประเภทจากลูกค้า cloud 300,000 องค์กร:

**1. In-app data** — content ที่ user สร้างใน platform: title + content ของ Confluence page, title/description/comment ของ Jira issue, custom emoji name, custom status name, workflow name

**2. Metadata** — usage pattern, structural data

Settings rollout เริ่มแล้ว 16 เม.ย. ให้องค์กรเตรียมก่อนนโยบายมีผล

**Tier matrix ที่สำคัญ:**
- Free + Standard: in-app data on-by-default, opt-out ได้
- Premium + Enterprise: in-app data off-by-default
- **Metadata: on-by-default ทุก tier — opt-out ได้เฉพาะ Enterprise**

ข้อยกเว้นเต็ม: customer-managed key (BYOK), Atlassian Government Cloud, Atlassian Isolated Cloud, HIPAA compliance, government, financial services

## ทำไมสำคัญ
ขั้นที่ใหญ่ที่สุดของ "SaaS ใช้ data ลูกค้าไป train AI" ในปีนี้ — Atlassian นั่งบน data ที่มีค่าที่สุดของ enterprise: ticket, doc, workflow, decision history หลายปีย้อนหลัง

The Register สรุปคม: "เว้นแต่จ่าย Enterprise license แพงสุด หรือกฎหมายห้าม Atlassian จะเอา data คุณไป train AI — opt out เต็ม ๆ ไม่ได้"

Pattern ที่จะตามมา: SaaS อื่นจะเริ่มประกาศแบบเดียวกัน (Slack, Notion, Linear, Monday) — เพราะ AI feature ของ vendor ต้องการ data, การไป license dataset นอกแพง, data ของลูกค้าเลย "ของฟรี" ที่หลีกเลี่ยงยาก

ผลกระทบจริง: legal team ของ enterprise ต้องเริ่ม audit DPA ของทุก SaaS อีกรอบ — Q3 2026 น่าจะมี wave ของการ renegotiate contract

## มุม OpenBridge
- **Trust positioning** — ถ้า OpenBridge ไม่ใช้ data ลูกค้าไป train AI ของตัวเอง พูดออกมาให้ชัด เป็น differentiator ทันที
- ถ้า OpenBridge ทำ integration กับ Atlassian — flag ให้ลูกค้ารู้ว่า data ที่ผ่านท่อจะถูก consume ที่ Atlassian ปลายทาง
- เป็นโอกาสคุยกับ enterprise prospect ที่ระแวง vendor lock-in กับ AI — "เราไม่ติดกับดักนี้"

## Sources
- [Atlassian to train AI on user data unless law or cash say no — The Register](https://www.theregister.com/2026/04/18/atlassians_new_data_collection_policy/)
- [Atlassian will train AI on your data starting August 2026 — Agent Wars](https://agent-wars.com/news/2026-04-17-atlassian-customer-data-ai-training)

---

## Audio script
เรื่องสุดท้ายของวันนี้ Atlassian ประกาศนโยบายใหม่ — เริ่ม 17 สิงหา 2026 บริษัทจะเอา metadata กับ in-app data จาก Jira Confluence และ cloud product อื่นทั้งหมด ไป train AI ของตัวเอง กระทบลูกค้า 300,000 องค์กรทั่วโลก Free กับ Standard ถูก opt-in ตั้งแต่แรก opt-out ได้ Premium กับ Enterprise off เป็น default แต่ส่วน metadata ทุก tier เปิดอยู่ จะ opt-out ได้แค่ Enterprise เท่านั้น The Register สรุปสั้น ๆ ว่าถ้าไม่จ่าย Enterprise license หรือไม่มีกฎหมายห้าม คุณ opt out เต็ม ๆ ไม่ได้ สำหรับ OpenBridge ผมว่ามี angle สำคัญ — ถ้าเราไม่ใช้ data ลูกค้าไป train AI ของตัวเอง พูดออกมาให้ชัด เป็น differentiator ทันที โดยเฉพาะกับ enterprise prospect ที่เริ่มระแวง vendor lock-in กับ AI และอีกอย่าง คาดได้ว่าอีกหลาย SaaS จะตามรอย Atlassian ในไม่กี่เดือน
