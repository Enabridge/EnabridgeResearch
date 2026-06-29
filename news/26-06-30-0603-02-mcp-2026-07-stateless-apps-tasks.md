---
date: 2026-06-30
slug: mcp-2026-07-stateless-apps-tasks
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a giant stone obelisk engraved with "MCP 2026-07-28"
  in the center of a server hall, with a single severed iron chain labeled
  "SESSION" lying broken on the floor in front of it. Around the obelisk float
  three glowing holographic panels labeled "STATELESS", "APPS", and "TASKS".
  Large floating numerals "19,831 servers" and "0 session state" hover
  prominently above the scene. Render style: cinematic editorial illustration,
  isometric perspective, cool teal-cyan data center lighting with one warm
  orange beam from the broken chain, dramatic depth, high-contrast typography
  legible at 200px thumbnail. No human figures — only architectural elements
  and holographic data.
image: images/26-06-30-0603-02-mcp-2026-07-stateless-apps-tasks.png
---

# MCP 2026-07-28 RC: protocol ตัดทิ้ง session state, เพิ่ม MCP Apps ให้ server ส่ง UI iframe กลับ — เปลี่ยน scaling model ทั้งหมด

## TL;DR
- Model Context Protocol ออก release candidate spec 2026-07-28 (final ship 28 ก.ค.) — เป็น revision ใหญ่ที่สุดตั้งแต่ launch protocol
- **Stateless** เป็น headline change — server ไม่ต้อง maintain session อีกต่อไป ทำให้ scale ผ่าน HTTP infrastructure ปกติ (load balancer, gateway) ได้โดยไม่ต้อง sticky session
- เพิ่ม 3 extension ใหญ่: **MCP Apps** (server ส่ง interactive HTML iframe ได้), **Tasks** (long-running work), authorization aligned OAuth/OIDC — registry ตอนนี้ index 19,831+ server, company-operated 4,133 (โต 873% จาก mid-2025)

## เกิดอะไรขึ้น

ปลายมิ.ย. ทีม Model Context Protocol ปล่อย release candidate ของ spec ใหม่ **2026-07-28** ซึ่งจะ ship final 28 ก.ค. — คนใน community เรียกว่า "MCP 2.0" เพราะเป็น revision ใหญ่ที่สุดตั้งแต่ Anthropic เปิดตัว protocol นี้ในปลายปี 2024 มี 6 Specification Enhancement Proposals (SEPs) ที่ทำงานร่วมกัน

**Headline change** คือทำให้ protocol **stateless** ที่ layer ของ protocol เอง ก่อนหน้านี้ MCP server ต้อง maintain session กับ client ผ่าน connection ที่เปิดยาว ซึ่งเป็น nightmare เวลาจะ scale — sticky session, connection draining ตอน deploy, state replication ระหว่าง replica ตอนนี้ทุก request เป็น standalone ทำให้ vendor ใช้ HTTP infrastructure เดิมได้ทั้งหมด — load balancer, gateway, rate limiter, CDN ทุกอย่างที่ enterprise มีอยู่แล้ว Streamable HTTP transport บังคับใส่ header ใหม่ `Mcp-Method` และ `Mcp-Name` เพื่อให้ infrastructure route ได้โดยไม่ต้อง inspect body ของ request

**MCP Apps** เป็น extension ที่น่าสนใจที่สุดจาก product perspective — มันให้ server "ship interactive HTML interfaces" ที่ host (Claude, ChatGPT) จะ render ใน sandboxed iframe Tool ต้อง declare UI template ล่วงหน้าเพื่อให้ host prefetch + cache + security-review ได้ก่อน — ทุก UI action ยังต้องผ่าน JSON-RPC audit + consent path เดียวกับ direct tool call แปลว่า MCP server ไม่ใช่แค่ "ส่ง JSON กลับ" อีกต่อไป — มันส่ง **full interactive widget** ที่ host จะแสดงในแชทได้ คิดถึง Stripe checkout widget ที่ pop ขึ้นมาในแชท Claude โดย Claude ไม่ต้องเขียน UI เอง

**Tasks** extension ให้ MCP server handle long-running work ที่ใช้เวลาเป็นนาทีหรือชั่วโมง โดยไม่ต้อง block conversation — ส่ง task ID กลับ แล้ว client poll หรือ webhook ได้ และ list/read results ตอนนี้แนบ `ttlMs` กับ `cacheScope` (modeled ตาม HTTP Cache-Control) — client รู้แน่ว่า tools/list response cache ได้นานเท่าไหร่ และ share ระหว่าง user ได้หรือไม่ Authorization aligned กับ OAuth + OIDC มากขึ้น — enterprise ที่ใช้ Okta/Auth0 อยู่แล้ว plug ได้เลย

ขนาด ecosystem ตอนนี้: Glama registry index 19,831+ server (รวม community + closed source), SkillsIndex track 4,133 company-operated server — โต **873%** จาก mid-2025 และ Tier 1 SDK (Python, TypeScript, Rust) คาดจะ ship support ภายใน 10-week validation window ก่อน 28 ก.ค.

## ทำไมสำคัญ

**Stateless = MCP พร้อม enterprise-scale แล้วจริง ๆ** ก่อนหน้านี้ MCP scale ได้แค่ระดับ developer workstation หรือ small team หลายบริษัทใหญ่ที่จะ deploy MCP ใน production ต้องสร้าง connection pool/session manager เอง ซึ่งเป็น engineering effort ที่ไม่ trivial ตอนนี้ MCP server เป็น stateless HTTP service ปกติที่ deploy ผ่าน Cloud Run, Lambda, Vercel, Fly.io ได้โดยตรง — เหมือนการ scale REST API ทั่วไป นี่คือ moment ที่ MCP เปลี่ยนจาก "interesting protocol" เป็น "infrastructure ที่ enterprise สั่ง deploy ได้"

**MCP Apps คือ killer feature ที่จะเปลี่ยน UX ของ AI assistant** — เดิม Claude/ChatGPT ตอบเป็น text + tool call แต่ตอนนี้ MCP server ส่ง **widget** กลับมาได้ ลองนึก: ผู้ใช้พิมพ์ "book me a flight to Tokyo" → Anthropic แชทแสดง flight search widget ที่ render โดย MCP server ของ Skyscanner เลย ผู้ใช้คลิกใน iframe แล้ว action กลับมาเป็น tool call ปกติ pattern นี้จะเปิด third-party developer experience ที่ใกล้เคียง **Slack App ยุค 2014** หรือ **iMessage Apps** — และคนที่ build widget เก่ง ๆ จะกิน distribution ของ Claude/ChatGPT user base

**Tasks extension** คือคำตอบสำหรับ workflow ที่ใช้เวลานาน — เช่น "วิเคราะห์ 10,000 invoices" หรือ "render video 4K" ที่ก่อนหน้านี้ต้อง workaround ด้วย background job queue ตัวเอง ตอนนี้ MCP มี first-class primitive แล้ว — ทำให้ agent ขออะไรที่ใช้เวลานานได้โดยไม่ต้อง block session

ที่น่าจับตา: NSA ออก MCP security guidance ไป 2 พ.ค. (Defense Department CSI) — ตอนนี้ spec ใหม่ harden authorization ให้ตรง standard enterprise มากขึ้น signal ว่า MCP กำลังกลายเป็น **government-blessed protocol** ในยุคที่ regulator จับ AI agent หนัก

## มุม OpenBridge

**OpenBridge ต้อง upgrade ทุก MCP server ที่ run อยู่ก่อน 28 ก.ค.** — ลูกค้าที่ใช้ Claude/Cursor/ChatGPT จะ migrate ไป spec ใหม่ภายในไตรมาส 3 และ legacy server ที่ยัง stateful จะถูกแสดง warning ใน client ภายในไม่กี่เดือน นี่คือ engineering work ที่ต้องเริ่มสัปดาห์นี้ ไม่ใช่ Q3

**MCP Apps เป็นโอกาสที่ใหญ่ที่สุดของ OpenBridge ในรอบปี** — OpenBridge มี integration library ที่ครอบ tool/service หลายร้อยตัวอยู่แล้ว ถ้า package แต่ละ integration เป็น MCP App ที่ ship interactive UI ไปด้วย → ลูกค้าเปิด Claude/ChatGPT พิมพ์ "ตรวจ order ใน Shopify" → OpenBridge MCP App ส่ง widget ของ order table มาแสดงในแชทเลย ไม่ต้อง redirect ออกไป Shopify admin pattern นี้จะ **lock-in distribution ลึกกว่าการเป็น API integration ปกติ** — เพราะ user เห็น UI ของ OpenBridge ตรง ๆ ใน Claude

Tasks extension match กับ workflow ของ OpenBridge ที่มัก involve long-running job (data sync, bulk operations, large file processing) — เคยต้อง workaround ผ่าน webhook ของลูกค้าเอง ตอนนี้ใช้ native MCP Task ได้

## Sources
- [The 2026-07-28 MCP Specification Release Candidate — Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [MCP 2026-07-28: The Stateless Release Candidate, Explained — MCP.Directory](https://mcp.directory/blog/mcp-2026-07-28-release-candidate)
- [MCP Just Went Stateless — What the 2026 Spec Changes About Scaling on App Service — Microsoft Tech Community](https://techcommunity.microsoft.com/blog/AppsonAzureBlog/mcp-just-went-stateless-%E2%80%94-what-the-2026-spec-changes-about-scaling-on-app-servic/4530222)
- [MCP's biggest growing pains for production use will soon be solved — The New Stack](https://thenewstack.io/model-context-protocol-roadmap-2026/)
- [MCP Killed the Session. Here's Why That's a Big Deal — Sathish Raju, Medium](https://medium.com/@sathishkraju/mcp-killed-the-session-heres-why-that-s-a-big-deal-4e484b331c27)

---

## Audio script
เรื่องที่สองครับ Yoh Model Context Protocol ออก release candidate ของ spec ใหม่ 2026-07-28 ปลายเดือนนี้ และจะ ship final 28 กรกฎา คนใน community เรียกว่า MCP 2.0 เพราะเป็น revision ใหญ่ที่สุดตั้งแต่ Anthropic เปิดตัว protocol นี้

Headline change คือทำให้ protocol stateless ทั้งหมดครับ ก่อนหน้านี้ MCP server ต้อง maintain session กับ client ผ่าน connection ที่เปิดยาว เป็น nightmare เวลาจะ scale ตอนนี้ทุก request เป็น standalone deploy บน Cloud Run Lambda Vercel ได้โดยตรง เป็น moment ที่ MCP เปลี่ยนจาก interesting protocol เป็น infrastructure ที่ enterprise สั่ง deploy ได้

เพิ่ม 3 extension ใหญ่ MCP Apps ที่ให้ server ส่ง interactive HTML iframe กลับมาแสดงในแชทได้ เหมือน Stripe checkout widget pop ขึ้นมาใน Claude เลย Tasks extension สำหรับ long-running work ที่ใช้เวลาเป็นนาทีหรือชั่วโมง แล้ว authorization aligned OAuth OIDC มากขึ้น

มุม OpenBridge อันนี้สำคัญมาก เราต้อง upgrade MCP server ทุกตัวก่อน 28 กรกฎา และ MCP Apps คือโอกาสที่ใหญ่ที่สุดของ OpenBridge ในรอบปี ถ้า package integration เป็น MCP App ที่ ship UI ไปด้วย ลูกค้าจะเห็น UI ของ OpenBridge ตรงๆ ใน Claude lock-in distribution ลึกกว่าการเป็น API integration ปกติครับ
