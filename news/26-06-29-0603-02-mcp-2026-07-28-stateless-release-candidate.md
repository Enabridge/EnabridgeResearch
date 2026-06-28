---
date: 2026-06-29
slug: mcp-2026-07-28-stateless-release-candidate
topic: openbridge-trend
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial illustration of an MCP protocol diagram morphing from a chain of sticky
  "session" boxes (left, fading away) into a clean parallel array of identical MCP
  server cubes (right) — requests as glowing arrows hit any cube equally, with a
  round-robin load-balancer ring floating above. Large floating numerals "2026-07-28"
  and "STATELESS" hover prominently; a smaller ribbon reads "Mcp-Session-Id ✗
  REMOVED". Style: cinematic editorial blueprint illustration, isometric perspective,
  deep navy background with electric-cyan request beams, technical schematic
  aesthetic, high-contrast typography legible at 200px thumbnail. No real human faces.
image: images/26-06-29-0603-02-mcp-2026-07-28-stateless-release-candidate.png
---

# MCP ฉีก Session ทิ้ง — RC 2026-07-28 ทำให้ protocol stateless, ทุก request วิ่งเข้า server instance ไหนก็ได้, breaking change ทุก SDK ต้อง re-validate ใน 10 สัปดาห์

## TL;DR
- 21 พ.ค. MCP Steering Committee lock release candidate `2026-07-28` — final spec ratify 28 ก.ค. มี breaking change ระดับเปลี่ยน mental model ของ MCP ทั้งหมด
- ตัวเปลี่ยนใหญ่: **เลิกใช้ `initialize` handshake + `Mcp-Session-Id` header** — protocol กลายเป็น stateless ทั้งดุ้น horizontal scaling วิ่ง round-robin ได้โดยไม่ต้อง sticky routing หรือ shared session store
- Extensions framework แยก capability ออกจาก spec core, **MCP Apps** เปิดให้ server render HTML iframe เข้า client ได้, **Tasks** redesign เป็น stateless `tasks/get|update|cancel`, authorization align กับ OAuth/OIDC เข้มขึ้น (mandatory `iss` validation)

## เกิดอะไรขึ้น

วันที่ 21 พ.ค. 2026 Anthropic + Steering Committee ของ Model Context Protocol lock release candidate ของ spec `2026-07-28` — เปิด 10 สัปดาห์ให้ SDK maintainer + Tier-1 client implementer (Claude Code, Cursor, Windsurf, Continue, Cline) validate ก่อน ratify final 28 ก.ค. ของจริงที่เปลี่ยน mental model ของ MCP ทั้งดุ้นคือ headline change: **protocol ไม่มี session ที่ระดับ wire อีกต่อไป** `Mcp-Session-Id` header หาย, `initialize` handshake หาย — ทุก request เป็น atomic unit ที่ลงไป server instance ไหนก็ได้

ความหมายในแง่ deployment ตรงเป๊ะ: ถ้าก่อนหน้านี้คุณ deploy MCP server ขนาด enterprise ต้องวาง sticky routing (Envoy/Nginx) + shared session store (Redis cluster) ตามมาตรฐาน stateful WebSocket — version `2026-07-28` ตัดทิ้งทั้งสอง อย่าง spec ระบุตรง ๆ ว่า "any MCP request can land on any server instance" — vanilla round-robin load balancer + autoscaling group แบบ stateless HTTP service ทำงานได้ทันที Microsoft App Service team ออกบทความ explicitly บอกว่า scale-out cost ลดลง "อย่างมีนัยสำคัญ" จาก architecture change นี้อย่างเดียว

นอกจาก stateless core ตัวที่ใหม่จริง ๆ คือ **Extensions framework** — capability ใหม่ ๆ ไม่ต้องรอ spec release รอบใหญ่อีกแล้ว มี governance track ของตัวเอง + reverse-DNS identifier + delegated maintainer ที่เปิดตัวมาพร้อม RC คือสอง extension หลัก: **MCP Apps** ให้ server ส่ง server-rendered HTML iframe ไปให้ client (sandboxed, template prefetching, security review hooks) — สำคัญสำหรับ workflow ที่ต้องการ rich UI inside chat (form, table, dashboard) **Tasks** ที่ก่อนหน้านี้เป็น experimental ใน spec เก่า ถูก redesign เป็น stateless `tasks/get` `tasks/update` `tasks/cancel` แทน `tasks/list` ที่เป็น stateful pattern เดิม

ฝั่ง security: 6 SEPs align authorization กับ OAuth 2.0 + OpenID Connect แน่นขึ้น มี mandatory `iss` parameter validation + refresh token handling ที่ clarified ส่วน Roots / Sampling / Logging ถูก deprecate แบบ annotation-only มี grace window 12 เดือนก่อน remove จริง — ครั้งแรกที่ MCP มี formal deprecation policy แทนการ break แบบเงียบ ๆ

## ทำไมสำคัญ

นี่คือ **moment ที่ MCP ฉีกตัวเองออกจาก "research protocol" ไปสู่ "enterprise infrastructure"** — version แรก ๆ ถูก design ให้เหมือน Language Server Protocol (LSP) ที่ session-bound เพราะ assume client/server 1:1 ใน developer tooling แต่พอ Cloudflare/Microsoft/Databricks ลอง deploy ในระดับ production ที่ MCP server รัน 100+ instance หลัง load balancer — session model พังตรง ๆ ทุก call ต้อง route ไป instance เดิม ทุก instance ต้อง share state ผ่าน Redis ที่ scale ไม่ทัน ทั้งหมดถูก kill ใน RC นี้

Pattern ที่เห็นใน 6 เดือนที่ผ่านมาคือ **MCP กำลังเดินทางเดียวกับ HTTP** — HTTP/1.0 → 1.1 → 2 → 3 ก็ลด state ลดความ stateful ลง ทุกรอบ เพราะนั่นคือทางเดียวที่จะ scale ตามที่ web growth ต้องการ MCP จาก spec แรก (มีนาคม 2024) จนถึง 2026-07-28 ใช้เวลาเกือบ 2 ปีถึงจะมาถึง "HTTP/2 moment" ของตัวเอง — เท่ากับยอมรับว่า design เดิม assume scale ผิด ทุกคนที่ build production MCP server ใน 18 เดือนที่ผ่านมาต้อง refactor

ด้าน timeline 10 สัปดาห์ validation window ที่กำหนดให้ Tier-1 SDK (TypeScript, Python, Go, Rust) ต้องส่ง support ก่อน final ratify — pace นี้สั้นมากสำหรับ breaking change ระดับนี้ ปกติ HTTP/OAuth ใช้เวลา 6-12 เดือน Anthropic เลือกบีบให้สั้นเพราะรู้ว่ายิ่งช้า ecosystem ยิ่ง fragmentation มากขึ้น (มี vendor หลายเจ้าที่เริ่ม fork MCP ออกไปเป็น proprietary แล้ว — เห็นใน Mistral / xAI ปลายเดือนที่แล้ว) — เป็น message ชัดว่า "ถ้าใครไม่ตามก็โดน leave behind"

## มุม OpenBridge

อันนี้ตรงใจ OpenBridge แบบ direct hit — เรากำลัง build integration platform ที่ expose enterprise tool/data ผ่าน MCP protocol ทุกอย่างที่เรา ship ก่อนหน้านี้ใช้ session model เดิมที่จะ deprecate ใน 4 สัปดาห์ (ยังมี 12-month grace แต่ลูกค้า enterprise ที่ใช้ Tier-1 client จะ insist version ใหม่เร็วกว่านั้นแน่นอน) — **action item ระดับ P0: ใส่ stateless spec compliance เข้า roadmap ภายใน Q3** ถ้าเรามี SDK wrapper / connector library ของตัวเอง ต้อง refactor ลด assumption เรื่อง session, ลบ shared store dependency, retest โหลด round-robin

แต่ใน opportunity ที่ใหญ่กว่าคือ **MCP Apps extension** — เปิดให้ server render UI inside client โดยตรง สำหรับ OpenBridge นี่คือทางที่ทำให้ "embedded experience ของแต่ละ integration" เป็น differentiator ได้ ไม่ใช่แค่ "ดึงข้อมูล" เฉย ๆ ลูกค้าเปิด Salesforce connector ใน Claude Code แล้วเห็น native Salesforce dashboard inline ได้เลย โดยที่เรา host UI fragment เอง — ของแบบนี้ third-party orchestration layer (Zapier/Make) ทำไม่ได้เพราะ MCP-specific Position OpenBridge เป็น "MCP-native integration suite ที่ลูกค้าเห็น UI ตรง ๆ" จะ stand out จาก legacy iPaaS ที่ต้องส่ง user ออกไปหน้าเว็บอื่น

## Sources
- [The 2026-07-28 MCP Specification Release Candidate — Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [MCP 2026-07-28: The Stateless Release Candidate, Explained — MCP.Directory](https://mcp.directory/blog/mcp-2026-07-28-release-candidate)
- [MCP Goes Stateless: What the 2026-07-28 Spec Release Candidate Means for Your Servers — jsmanifest](https://jsmanifest.com/mcp-stateless-spec-2026-07-28)
- [MCP Just Went Stateless — What the 2026 Spec Changes About Scaling on App Service — Microsoft Tech Community](https://techcommunity.microsoft.com/blog/appsonazureblog/mcp-just-went-stateless-%E2%80%94-what-the-2026-spec-changes-about-scaling-on-app-servic/4530222)
- [What changed in the 2026-07 MCP specification — Stacktree](https://stacktr.ee/blog/mcp-2026-spec-changes)
- [MCP Is Growing Up — Agentic AI Foundation](https://aaif.io/blog/mcp-is-growing-up/)

---

## Audio script
สวัสดีครับ Yoh เรื่องที่สอง MCP เพิ่ง lock release candidate spec 2026 07 28 ที่จะ ratify ปลายเดือนกรกฎาคมนี้ มี breaking change ระดับเปลี่ยน mental model ของ protocol ทั้งหมด headline change คือ MCP กลายเป็น stateless ทั้งดุ้น เลิกใช้ initialize handshake และเลิกใช้ Mcp Session Id header ทุก request เป็น atomic unit ที่ลงไป server instance ไหนก็ได้ ความหมายในแง่ deployment ตรงเป๊ะคือ ก่อนหน้านี้ enterprise ที่ deploy MCP server ต้องวาง sticky routing แล้วก็ shared session store ผ่าน Redis ตอนนี้ตัดทิ้งทั้งคู่ vanilla round robin load balancer ทำงานได้ทันที Microsoft App Service team ออกบทความบอกว่า scale out cost ลดลงอย่างมีนัยสำคัญ extension ใหม่ที่เปิดมาคือ MCP Apps ที่ให้ server ส่ง HTML iframe เข้า client โดยตรง กับ Tasks ที่ redesign เป็น stateless authorization align กับ OAuth กับ OIDC เข้มขึ้น มี mandatory iss validation ระยะเวลา 10 สัปดาห์ที่ให้ Tier 1 SDK validate ก่อน final ratify ถือว่าสั้นมากสำหรับ breaking change ระดับนี้ Anthropic บีบให้สั้นเพราะรู้ว่ายิ่งช้า ecosystem ยิ่ง fragmentation มากขึ้น สำหรับ OpenBridge อันนี้กระทบเราตรง ๆ ทุก integration ที่เรา ship ใช้ session model เดิมที่จะ deprecate ต้องใส่ stateless spec compliance เข้า roadmap ใน Q3 แต่ที่ใหญ่กว่าคือ MCP Apps extension เปิดให้ server render UI inside client ตรง ๆ เป็นโอกาสที่ OpenBridge ใช้ position ตัวเองเป็น MCP native integration suite ที่ลูกค้าเห็น UI ตรง ๆ stand out จาก legacy iPaaS ที่ต้องส่ง user ไปหน้าเว็บอื่น ได้ครับ
