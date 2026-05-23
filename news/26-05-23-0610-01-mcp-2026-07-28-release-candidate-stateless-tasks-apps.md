---
date: 2026-05-22
slug: mcp-2026-07-28-release-candidate-stateless-tasks-apps
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Hero illustration showing the Model Context Protocol logo as a USB-C-shaped
  connector being upgraded from a tangled session-based cable to a clean
  stateless line, with bold text "MCP 2026-07-28" and "STATELESS" rendered
  large in the bottom third for thumbnail legibility. Composition: split-screen
  before/after, dark navy background on the left (old session-locked routing
  with sticky-server icons) shifting to bright cyan on the right (load-balancer
  fanning out HTTP requests to identical server nodes, no session state). Add
  small badges floating around the new side reading "Tasks", "MCP Apps",
  "OAuth 2.1". Style: editorial tech illustration, isometric, flat vector,
  high contrast, Stripe/Anthropic blog aesthetic. No human faces.
image: images/26-05-23-0610-01-mcp-2026-07-28-release-candidate-stateless-tasks-apps.png
---

# MCP เปลี่ยนเครื่องยนต์ — release candidate 2026-07-28 ตัดทิ้ง session state ทั้ง protocol

## TL;DR
- Anthropic ล็อก MCP 2026-07-28 release candidate (21 พ.ค.) — เป็นการรีวิชั่นใหญ่ที่สุดของ protocol ตั้งแต่เปิดตัว
- หัวใจคือ **stateless core** — ตัด `Mcp-Session-Id` ทิ้ง ทำให้ remote MCP server วิ่งหลัง plain HTTP load balancer ได้โดยไม่ต้อง sticky routing
- **Tasks** (long-running work) และ **MCP Apps** (server-rendered UI) ย้ายไปอยู่ใน Extensions framework แยกออกจาก core; OAuth 2.1 + OIDC alignment เข้ามาแทน custom auth

## เกิดอะไรขึ้น

วันที่ 21 พฤษภาคม 2026 ทีม Model Context Protocol ประกาศ lock release candidate ของ spec รุ่นใหม่ `2026-07-28` หลังจาก draft วนหลายเดือน — และนี่คือการรีวิชั่นที่ใหญ่ที่สุดของ MCP ตั้งแต่ Anthropic เปิดตัวเมื่อปลายปี 2024 ทีมตั้งกรอบเวลา 10 สัปดาห์ให้ SDK maintainer ทั้ง Tier 1 (TypeScript, Python, Java, C#, Go, Kotlin, Swift) ทดสอบกับ workload จริงก่อน publish ตัวจริงวันที่ 28 ก.ค. 2026

หัวใจของรอบนี้คือ "stateless at the protocol layer" — header `Mcp-Session-Id` หายไป pure protocol-level session ก็หายไปด้วย ผลคือ remote MCP server วิ่งหลัง round-robin load balancer ทั่วไปได้ทันที ไม่ต้องทำ sticky routing หรือ shared session store อีกต่อไป client cache `tools/list` response ได้ตาม `ttlMs` ที่ server บอก request ตัวใหม่จะตกที่ instance ไหนของ server ก็ทำงานได้ครบ — ของที่เคยเป็นปัญหาใหญ่สำหรับทีม ops ตอน scale-out

**Tasks** ซึ่งเคยเป็น experimental core feature ใน spec `2025-11-25` ถูกย้ายลงไปอยู่ใน Extensions framework แทน — server ตอบ `tools/call` ด้วย task handle, client ขับ lifecycle ด้วย `tasks/get`, `tasks/update`, `tasks/cancel` Anthropic บอกตรง ๆ ว่าหลังเอาไปใช้ production แล้วเจอ pattern ที่ต้อง redesign จึงไม่ commit เข้า spec core ส่วน **MCP Apps** (server-rendered UI inside agent surfaces) ก็มาเป็น extension เช่นกัน รวมถึง 6 SEPs (Specification Enhancement Proposals) ที่ปรับ authorization ให้ตรงกับ OAuth 2.0 + OpenID Connect deployment pattern จริงในองค์กร

## ทำไมสำคัญ

เรื่อง stateless อาจฟังดูเป็น engineering detail แต่จริง ๆ คือสัญญาณว่า MCP กำลังโตจาก "AI protocol ที่ developer เล่นใน localhost" เป็น "infrastructure protocol ที่ enterprise ops team รับได้" Cloudflare กับ Anthropic เปิด MCP tunnels + self-hosted sandboxes ไปเมื่อกลางเดือน (20 พ.ค.) — ตอนนั้นทุกคนพูดเรื่อง deployment model วันนี้ spec layer ตามมาแก้ปัญหา infra ที่เป็นหินจริงในการรัน MCP ที่ scale

จุดที่ต้องจับตาคือ Extensions framework — โดยการย้าย Tasks กับ MCP Apps ออกจาก core spec ทีมโปรโตคอลกำลังบอกว่า "core ต้อง minimal และเสถียร feature ที่ยัง evolve ให้ไปอยู่ extension" ซึ่งเป็น pattern เดียวกับที่ HTTP/WebSocket spec ใช้มา — เป็น signal ว่า MCP กำลัง mature เข้าสู่ phase ที่ vendor lock-in risk ต่ำลง ใครจะ build บนนี้ก็ predictable มากขึ้น สำหรับ Anthropic ที่ต้องการให้ MCP เป็น "USB-C for AI" นี่คือ move ที่ถูก — แต่ต้องดูว่า OpenAI ที่ยังไม่ได้ commit MCP เต็มตัว (ปัจจุบันยัง opt-in ผ่าน Agents SDK) จะตามมาตอนไหน

## มุม OpenBridge

ถ้า OpenBridge มี MCP server หรือ MCP client อะไรอยู่ใน roadmap — 10 สัปดาห์ก่อน 28 ก.ค. นี่คือ window ที่ต้องตัดสินใจว่าจะรองรับ stateless model หรือ stick กับ session-based ตอนเปิดตัวจริง การ build บน stateless core หมายความว่า OpenBridge MCP integration จะ scale ได้ง่ายแบบ stateless service ปกติ — ลด ops cost ของลูกค้า enterprise และทำให้ pitch deck เรื่อง "deploy MCP server เข้า production ภายในวันเดียว" จริงขึ้น

อีกประเด็นคือ OAuth 2.1 alignment — สำหรับ integration platform แบบ OpenBridge ที่ลูกค้าเป็น B2B การที่ MCP authorization เข้ากับ OIDC ที่ลูกค้ามีอยู่แล้ว (Okta, Auth0, Microsoft Entra) จะตัด friction การขายไปได้เยอะ ไม่ต้อง onboard auth pattern ใหม่ให้ IT team

## Sources
- [The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [MCP's biggest growing pains for production use will soon be solved — The New Stack](https://thenewstack.io/model-context-protocol-roadmap-2026/)
- [The 2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)

---

## Audio script
สวัสดีครับ Yoh วันนี้ข่าวเด่นคือ Model Context Protocol หรือ MCP ที่ Anthropic ดูแลอยู่ ล็อก release candidate ตัวใหม่ของ spec ชื่อ 2026-07-28 ไปเมื่อวานนี้ 21 พฤษภาคม และนี่เป็นการเปลี่ยนแปลงครั้งใหญ่ที่สุดของโปรโตคอลตั้งแต่เปิดตัว หัวใจคือเขาตัด session state ทิ้งทั้งโปรโตคอล หมายความว่า MCP server ที่อยู่บน remote วิ่งหลัง load balancer ปกติได้ทันที ไม่ต้อง sticky routing ไม่ต้อง shared session store เป็นการแก้ปัญหาที่ ops team เจอตอน scale ขึ้นจริง ส่วน feature ใหญ่อย่าง Tasks สำหรับ long-running work และ MCP Apps ที่ render UI จากฝั่ง server ก็ถูกย้ายไปอยู่ใน Extensions framework แยกจาก core spec ตามด้วย authorization ที่ปรับให้ตรงกับ OAuth 2.1 และ OpenID Connect ที่องค์กรใช้กันจริง ทีมโปรโตคอลให้เวลา 10 สัปดาห์ก่อน publish ตัวจริง 28 กรกฎาคม สำหรับ SDK maintainer ทุกภาษาทดสอบกับ workload production ของจริง สัญญาณที่เห็นคือ MCP กำลังเปลี่ยนจาก protocol ของ developer เล่นใน localhost เป็น infrastructure protocol ระดับ enterprise ops ที่ scale ได้และตรงกับ auth stack ที่ลูกค้ามีอยู่แล้ว ใครที่ build บน MCP อยู่ ตอนนี้คือเวลาที่ต้องตัดสินใจ design choice ก่อนที่ตัวจริงจะ ship ครับ
