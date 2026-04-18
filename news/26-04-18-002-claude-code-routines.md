---
date: 2026-04-18
slug: claude-code-routines
topic: agentic-ai
reading_time_min: 2
sources: 3
---

# Claude Code Routines — Anthropic ดัน agent ขึ้น cloud, รันเองโดยไม่ต้องเปิดเครื่อง

## TL;DR
- Anthropic เปิด **Routines** ใน Claude Code (research preview, 14 เม.ย.) — packaged prompt + repo + connector รันบน cloud Anthropic เอง
- Pro 5 routines/วัน, Max 15, Team/Enterprise 25 — เกินจ่ายเพิ่มได้
- Desktop app redesign พ่วงมาด้วย: parallel sessions, integrated terminal, in-app file editor

## เกิดอะไรขึ้น
14 เม.ย. 2026 Anthropic ปล่อย dual release — Claude Code desktop app เวอร์ชั่น redesign + Routines ใน research preview

**Routines** คือ saved Claude Code configuration: 1 prompt + 1+ repo + ชุด connector ห่อรวมไว้ครั้งเดียว แล้วรันอัตโนมัติ key point: รันบน cloud infrastructure ของ Anthropic เอง — laptop ปิดอยู่ก็รัน

Quota: Pro 5/วัน, Max 15, Team/Enterprise 25 ใช้เกินได้แต่ billed extra

**Desktop redesign** เน้นลด context-switch — integrated terminal, faster diff viewer, in-app file editor, expanded preview area Anthropic เน้นเรื่อง multiple sessions รองรับวิธีที่ developer ใช้ AI จริง ๆ ทุกวัน — หลาย task พร้อมกัน

## ทำไมสำคัญ
นี่คือ Anthropic ก้าวจาก "AI ผู้ช่วย dev คนเดียว" เป็น "agent infrastructure ที่ทีมจ้างงาน" — Routines ทำให้ scheduled/triggered automation เป็น first-class แทน hack ผ่าน cron

VentureBeat ถามคำถามที่ตรง: enterprise พร้อมให้ agent รันโดยไม่มี developer cosign ทุกครั้งหรือยัง? Routines เลยมาพร้อม SSO, audit log, controllable permissions — ตอบ governance ก่อน scale

Pattern ที่เห็น: foundation lab ขยับขึ้นไป layer "agent operations" — แข่งกับ workflow startup จำนวนมากที่กำลังสร้าง orchestration layer เหนือ Claude

## มุม OpenBridge
- ถ้า OpenBridge ใช้ Claude Code อยู่แล้ว — ลอง Routines ทำงาน batch ที่ทีม dev ทำซ้ำ (release notes, dependency upgrade, security patch sweep)
- เป็น threat ต่อ wrapper startup ที่สร้างเฉพาะ "scheduling layer" บน Claude — ของ Anthropic เอง free แล้ว ใครคิดสร้าง orchestrator ต้องมีอย่างอื่น
- ถ้า OpenBridge ทำ integration platform — Routines เป็น workflow primitive ใหม่ที่ลูกค้าเริ่มคุ้น ออกแบบให้ trigger ของเราต่อกับมันได้

## Sources
- [Anthropic's Claude Code gets automated 'routines' and a desktop makeover — SiliconANGLE](https://siliconangle.com/2026/04/14/anthropics-claude-code-gets-automated-routines-desktop-makeover/)
- [We tested Anthropic's redesigned Claude Code desktop app and 'Routines' — VentureBeat](https://venturebeat.com/orchestration/we-tested-anthropics-redesigned-claude-code-desktop-app-and-routines-heres-what-enterprises-should-know)
- [Anthropic Rebuilds Claude Code Desktop App Around Parallel Sessions — MacRumors](https://www.macrumors.com/2026/04/15/anthropic-rebuilds-claude-code-desktop-app/)

---

## Audio script
เรื่องที่สอง Anthropic เพิ่งเปิด Routines ใน Claude Code เมื่อวันที่ 14 เมษา ตัวนี้สำคัญ มันคือการห่อ prompt บวก repo บวก connector ของเรารวมเป็น automation ตัวเดียว แล้วรันบน cloud ของ Anthropic เอง laptop ปิดอยู่ก็รัน Pro รันได้ 5 ครั้งต่อวัน Max 15 ส่วน Team กับ Enterprise 25 เกินจ่ายเพิ่มได้ พร้อมกันนี้ desktop app ก็โดน redesign ใหม่หมด รองรับหลาย session พร้อมกัน มี terminal กับ file editor ในตัว สำหรับ OpenBridge ผมว่าน่าจับตา ถ้าเราใช้ Claude Code อยู่แล้ว ลอง Routines ทำงาน batch ที่ dev ทำซ้ำ ๆ เช่น release note, security patch sweep แต่ที่สำคัญกว่าคือ Anthropic ขยับขึ้น layer agent operations เอง — startup ที่สร้างแค่ scheduling layer บน Claude เริ่มอยู่ยาก เพราะของ official ก็มีให้ใช้ฟรีแล้ว
