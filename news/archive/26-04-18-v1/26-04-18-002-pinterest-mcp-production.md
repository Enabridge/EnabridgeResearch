---
date: 2026-04-18
slug: pinterest-mcp-production
topic: use-case
reading_time_min: 2
sources: 1
---

# Pinterest เอา MCP ขึ้น production — agent ช่วย engineer ประหยัดหลายพันชั่วโมง/เดือน

## TL;DR
- Pinterest deploy MCP ecosystem เต็มรูปแบบให้ internal engineering agents ใช้งาน production
- โครง: domain-specific MCP servers + central registry + human-in-the-loop approval
- เคลมประหยัด **หลายพันชั่วโมงต่อเดือน** จาก engineering task ที่ agent ช่วยอัตโนมัติ

## เกิดอะไรขึ้น
Pinterest engineering เปิด production MCP ecosystem ให้ AI agents รัน complex engineering task ข้าม internal tools ของบริษัท

สถาปัตยกรรมที่น่าสนใจ:
- **Domain-specific MCP servers** — แยก server ตาม domain (ไม่ใช่ one-size-fits-all)
- **Central registry** — agent ค้นเจอ server ที่ต้องใช้
- **Human-in-the-loop approval** — agent ไม่ commit action เสี่ยง ๆ เองโดยไม่ผ่านคน

ผลที่อ้าง: security ดีขึ้น, governance ตรวจสอบได้, developer productivity เพิ่ม, ประหยัด "thousands of hours per month"

## ทำไมสำคัญ
เป็น case study **production-scale** ที่หายากใน MCP world — ส่วนใหญ่ยังเป็น demo หรือ pilot

Pattern "registry + domain-specific + HITL" ให้คำตอบเรื่อง governance ที่ enterprise ถามบ่อย — "จะปล่อย agent ไปทำอะไรในระบบ prod ยังไงให้ไม่พัง"

หมายเหตุ: ตัวเลข "thousands of hours" เป็น Pinterest อ้างเอง ไม่มี breakdown ละเอียด — treat as directional มากกว่า gospel

## มุม OpenBridge
- Blueprint นี้ copy ได้แทบทั้งก้อน — ถ้า OpenBridge ขาย agent orchestration "registry + domain MCP + approval gate" คือ 3 layer ต้องมี
- HITL approval เป็น sell point เผื่อตอบลูกค้า enterprise ไทย ที่ยังไม่มั่นใจ agent เต็มตัว — ขายเป็น "agent-assisted" ไม่ใช่ "agent-autonomous"

## Sources
- [Pinterest Deploys Production-Scale Model Context Protocol Ecosystem for AI Agent Workflows — InfoQ](https://www.infoq.com/news/2026/04/pinterest-mcp-ecosystem/)

---

## Audio script
เรื่องที่สอง Pinterest เปิดให้ MCP ขึ้น production จริง ๆ ไม่ใช่ experiment แล้ว โครงสร้างเขาน่าสนใจ แยกเป็น domain-specific server หลาย ๆ ตัว มี central registry ให้ agent ค้นเจอ แล้วใส่ human-in-the-loop approval ก่อน action เสี่ยง ๆ เคลมประหยัดเวลา engineer หลายพันชั่วโมงต่อเดือน ผมว่าเรื่องนี้สำคัญเพราะตัวอย่าง production-scale แบบนี้หายาก ส่วนใหญ่ยังเป็น demo อยู่ และ pattern registry บวก domain server บวก approval gate มันตอบคำถาม enterprise ว่าจะปล่อย agent เข้าระบบ prod ยังไงให้ไม่พัง สำหรับ OpenBridge ผมว่านี่คือ blueprint ที่ copy ได้ตรง ๆ เลย และ HITL approval เป็น angle ขายลูกค้าไทยที่ยังไม่กล้า agent เต็มตัวได้ดีมาก
