---
date: 2026-05-25
slug: anthropic-mcp-tunnels-self-hosted-sandboxes
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A glowing tunnel made of encrypted data streams connects a floating Claude
  logo on the left to a secure enterprise server rack on the right, wrapped in
  a translucent shield labeled "PRIVATE NETWORK" in bold white text. Below the
  tunnel, the letters "MCP" are rendered large and luminous in Anthropic orange.
  Inside the tunnel, small tool icons (database, API endpoint, ticketing system)
  travel like packets. The enterprise side sits behind a stylized firewall wall
  with a green padlock. Above, a banner reads "ZERO INBOUND PORTS" in high-contrast
  text. Style: cybersecurity editorial illustration, isometric perspective, dark
  background with neon accent lines, high contrast for thumbnail legibility.
  No human faces.
image: images/26-05-25-0603-01-anthropic-mcp-tunnels-self-hosted-sandboxes.png
---

# Anthropic ปล่อย MCP Tunnels + Self-Hosted Sandboxes — Claude agent เข้าถึง enterprise API ได้โดยไม่ต้องเปิด port

## TL;DR
- Claude Managed Agents รองรับ **self-hosted sandboxes** (public beta) — agent ทำงานบน infra ของลูกค้าเอง หรือผ่าน Cloudflare/Daytona/Modal/Vercel
- **MCP tunnels** (research preview) ให้ agent เข้าถึง MCP server ใน private network โดยไม่ต้องเปิด port เข้า — outbound connection เส้นเดียว, encrypted end-to-end
- ประกาศที่งาน Code with Claude London (19 พ.ค. 2026) — เป็นการแก้ปัญหา #1 ของ enterprise adoption: "จะให้ AI agent เข้าถึงระบบภายในยังไงโดยไม่เสี่ยง"

## เกิดอะไรขึ้น

Anthropic ประกาศสองฟีเจอร์ใหม่สำหรับ Claude Managed Agents ที่งาน Code with Claude London เมื่อวันที่ 19 พ.ค. — self-hosted sandboxes และ MCP tunnels ทั้งสองฟีเจอร์เกิดจากปัญหาเดียวกัน: enterprise ที่อยากใช้ Claude agent ทำงานจริง (ไม่ใช่แค่ chatbot) ต้องให้ agent เข้าถึง internal database, private API, ticketing system แต่ไม่มีทางยอมเปิด production system ให้ cloud service ภายนอกเข้าถึงโดยตรง

Self-hosted sandboxes แก้ปัญหาฝั่ง compute — แทนที่จะให้ agent ทำงานบน Anthropic infra ตอนนี้ sandbox ที่ agent execute tools ทำงานอยู่บน infrastructure ของลูกค้าเอง หรือผ่าน managed provider อย่าง Cloudflare, Daytona, Modal, Vercel โดย orchestration layer (context management, error recovery, agent loop) ยังอยู่บน Anthropic เป็นการแบ่ง concern ที่ชัดเจน — Anthropic ดูแล "สมอง" ลูกค้าดูแล "มือ" ที่สัมผัส data จริง

MCP tunnels แก้ปัญหาฝั่ง connectivity — lightweight gateway ที่ deploy ภายใน private network สร้าง outbound connection เส้นเดียวไปยัง Anthropic ไม่มี inbound firewall rule ไม่มี public endpoint traffic encrypted end-to-end ผลคือ internal database, knowledge base, Jira, Confluence หรือ API ภายในใด ๆ ที่มี MCP server กลายเป็น tool ที่ Claude agent เรียกใช้ได้ทันที — โดยที่ security team ไม่ต้องเปิดอะไรให้อินเทอร์เน็ตเห็นเลย

VentureBeat รายงานว่า MCP tunnels ออกแบบมาเพื่อแก้ปัญหา credential leaking ที่เป็น concern หลักของ enterprise — agent ไม่ต้อง "ถือ" credential ของ API เพราะ gateway ภายใน network จัดการ auth ให้ Anthropic เองก็ไม่เห็น credential ที่ใช้ ซึ่งเป็น architecture ที่ security-conscious organization ยอมรับได้ง่ายกว่า

## ทำไมสำคัญ

นี่คือ missing piece ที่ทำให้ "agentic AI for enterprise" กลายจาก demo เป็น production ได้จริง ปัญหาที่ผ่านมาไม่ใช่ว่า Claude ไม่เก่งพอ แต่คือ enterprise ไม่มีทางปลอดภัยที่จะให้ cloud AI เข้าถึงระบบภายใน MCP tunnels เปลี่ยน equation — จาก "เปิด port ให้ AI เข้ามา" เป็น "ระบบภายใน connect ออกไปหา AI" ซึ่งตรงกับ zero-trust architecture ที่ enterprise ใช้อยู่แล้ว

Pattern ที่เห็นคือ "MCP กำลังกลายเป็น TCP/IP ของ AI agents" — เดิม MCP เป็นแค่ protocol สำหรับ local tool calling ตอนนี้มี tunneling, auth, sandbox isolation เป็น stack เต็มสำหรับ enterprise deployment เมื่อ MCP spec 2026-07-28 stabilize (ดู brief รอบก่อน) + MCP tunnels ให้ secure connectivity + self-hosted sandboxes ให้ data residency — enterprise ที่ลังเลจะไม่มีข้ออ้างอีกต่อไป

อีกมุมที่น่าสนใจคือ competitive positioning — Anthropic เลือกที่จะไม่ own ทุกอย่าง: sandbox ให้ partner (Cloudflare, Vercel) run, connectivity ให้ลูกค้า control สิ่งนี้ต่างจาก approach ของ OpenAI/Codex ที่ sandbox อยู่บน OpenAI infra ทั้งหมด ถ้า enterprise ต้องเลือกระหว่าง "data อยู่กับ AI vendor" กับ "data อยู่กับเรา AI vendor เข้าถึงผ่าน tunnel" คำตอบชัดเจน

## มุม OpenBridge

สำหรับ OpenBridge นี่คือ signal ที่ชัดเจนที่สุดว่า **MCP-native architecture คือ correct bet** MCP tunnels หมายความว่า enterprise จะ deploy MCP server สำหรับทุก internal system อยู่แล้ว — OpenBridge ที่ position ตัวเองเป็น "MCP integration backbone" จะได้ประโยชน์โดยตรง เพราะทุก MCP server ที่ enterprise deploy สำหรับ Claude ก็ใช้กับ OpenBridge ได้ทันทีและในทางกลับกัน

action item ที่ชัดคือ: OpenBridge ควรทดสอบ MCP tunnels research preview ทันที และเตรียม integration guide สำหรับลูกค้าที่จะ deploy OpenBridge MCP server ผ่าน tunnel ถ้า OpenBridge เป็น "MCP server ตัวแรกที่ enterprise ลองผ่าน MCP tunnel" จะได้ first-mover advantage ในตลาด enterprise agent integration

## Sources
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels — Anthropic](https://claude.com/blog/claude-managed-agents-updates)
- [Anthropic adds self-hosted sandboxes and MCP tunnels to Claude Managed Agents — The Decoder](https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/)
- [Anthropic Introduces MCP Tunnels for Private Agent Access to Internal Systems — InfoQ](https://www.infoq.com/news/2026/05/claude-mcp-tunnels/)
- [Securing AI agent credentials with MCP tunnels — VentureBeat](https://venturebeat.com/orchestration/claude-agents-can-finally-connect-to-enterprise-apis-without-leaking-credentials)

---

## Audio script
สวัสดีครับ Yoh ข่าวแรกวันนี้เป็นเรื่อง Anthropic ที่ปล่อยสองฟีเจอร์ใหม่สำหรับ Claude Managed Agents ที่งาน Code with Claude London เมื่อสัปดาห์ก่อน ตัวแรกคือ self-hosted sandboxes ที่ให้ agent ทำงานบน infrastructure ของลูกค้าเองแทนที่จะทำงานบน Anthropic cloud ตัวที่สองคือ MCP tunnels ซึ่งน่าสนใจมากครับ มันให้ Claude agent เข้าถึง MCP server ที่อยู่ใน private network ของ enterprise ได้โดยไม่ต้องเปิด port เข้าเลย ใช้ outbound connection เส้นเดียว encrypted end-to-end หมายความว่า internal database private API หรือ ticketing system กลายเป็น tool ที่ agent เรียกใช้ได้ทันที โดย security team ไม่ต้องเปิดอะไรให้อินเทอร์เน็ตเห็น นี่คือ missing piece ที่ทำให้ agentic AI for enterprise กลายจาก demo เป็น production ได้จริง สำหรับ OpenBridge นี่เป็น signal ชัดเจนว่า MCP-native architecture คือ correct bet เพราะ enterprise จะ deploy MCP server สำหรับทุก internal system อยู่แล้ว OpenBridge ที่เป็น MCP integration backbone จะได้ประโยชน์โดยตรงครับ
