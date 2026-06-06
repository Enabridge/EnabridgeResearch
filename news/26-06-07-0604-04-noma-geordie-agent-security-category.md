---
date: 2026-06-07
slug: noma-geordie-agent-security-category
topic: openbridge-trend
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial illustration of a security checkpoint gate at the entrance of a
  vast digital city, with hundreds of robotic agent silhouettes lined up in a
  glowing queue being scanned one by one. Each agent has a small floating ID
  badge above it labeled "Approved" "Review" or "Blocked" in three colors.
  The checkpoint gate is constructed from translucent shield panels with
  inspection beams scanning agents from both sides. Bold floating text reads
  "Agent Security · New Category" with smaller tags "Noma" and "Geordie $30M"
  pinned at the gate posts. Cinematic editorial style, moody twilight lighting
  with cyan security beams and amber warning lights, dramatic depth,
  high-contrast typography legible at 200px thumbnail. No real human faces —
  only robotic agent silhouettes.
image: images/26-06-07-0604-04-noma-geordie-agent-security-category.png
---

# AI Agent Security เกิดเป็น category ใหม่ — Noma เปิดตัว Agent Access Control + Geordie ระดม $30M Series A ในสัปดาห์เดียวกัน

## TL;DR
- 2 มิ.ย. **Noma เปิด Agent Access Control** — ระบบ discover/govern/enforce policy สำหรับ AI agent + MCP server ทั่ว enterprise ตั้งแต่วันแรก ใช้ identity ต่อ agent + tool-level approval (Approved/Review/Blocked)
- 28 พ.ค. — 1 มิ.ย. **Geordie AI ปิด Series A $30M** นำโดย Balderton (รวม Crosspoint, General Catalyst, Ten Eleven) — valuation ~$180M, **ARR โต 1,300% ในแค่ 5 เดือนแรกของปี 2026**, ชนะ RSAC Innovation Sandbox 2026
- Pattern: "AI agent security" กลายเป็น category ใหม่ที่ Big Cyber (Palo Alto, CrowdStrike, Wiz) ยังไม่มี product เฉพาะ — VC + buyer signal ตรงกัน

## เกิดอะไรขึ้น

ภายใน 6 วันเดียว — **28 พ.ค. ถึง 2 มิ.ย. 2026** — มี 2 ข่าวจากชั้น "AI agent security" ที่รวมกันบอกชัดว่ามี category ใหม่เกิดขึ้นในตลาด cybersecurity enterprise

ก้อนแรก **Geordie AI** — startup ที่ London + New York — ปิด **Series A $30M นำโดย Balderton Capital** ร่วมกับ Crosspoint Capital + follow-on จาก General Catalyst + Ten Eleven Ventures total funding แตะ $36.5M valuation ~$180M post-money และ Balderton บอกว่าเป็น **Series A cybersecurity ใหญ่ที่สุดของ Europe ตั้งแต่ก่อตั้งวงการ** ตัวเลขที่ทำให้ VC เทเงิน: **ARR โต 1,300% ใน 5 เดือนแรกของปี 2026** + ชนะ **RSAC Innovation Sandbox 2026** (รางวัล "best new cybersecurity startup" ที่ industry คาดหวังว่าใครชนะจะเป็น unicorn ใน 24 เดือน) ปัจจุบัน Geordie deploy ใน ~30 customer environment headcount 37 คน — กำลังจะถึง 50 ใน 3 เดือน

ก้อนสอง **Noma** เปิดตัว **Agent Access Control** วันที่ 2 มิ.ย. — ระบบที่ build inventory ของทุก AI agent + ทุก MCP server ทั่ว enterprise โดยอัตโนมัติ feature หลัก 4 ก้อน:
1. **Enterprise Agentic Registry** — registry ที่ update real-time ทุกครั้งที่มี agent/MCP server connect, แสดงว่า server expose อะไร, agent ตัวไหน connect, สถานะกับ security policy ปัจจุบัน
2. **Agent Identity** — ให้ identity เฉพาะกับทุก agent เวลา connect กับ MCP server/tool (ไม่ใช่ใช้ user credential แบบเดิม)
3. **Governance Model** — security team config ทุก agent/MCP connection ใน 3 สถานะ: **Approved / Requires Review / Blocked** — Approved วิ่งผ่าน, Review เข้าคิวรอ review พร้อม risk context, Blocked โดน enforce อัตโนมัติไม่ต้องตัดสินใจทุกครั้ง
4. **Tool-Level Control** — approve/block ระดับ tool ไม่ใช่ระดับ server (granularity ตาม tool, agent type, user, team, environment)

Noma คู่ Agent Access Control กับ **AI Detection and Response (AI-DR)** ของตัวเองที่ monitor prompt, tool call, data access, action taken ของ agent session **real-time** + detect prompt injection, data exfiltration, scope violation

## ทำไมสำคัญ

สองข่าวนี้รวมกัน confirm ว่า **"AI agent security" เป็น category ใหม่จริง** ไม่ใช่ subcategory ของ DLP/CASB/EDR ที่ Big Cyber (Palo Alto, CrowdStrike, Wiz) เคยครอบ — เพราะ threat model ของ agent ต่างจาก traditional endpoint:
- **Identity** — agent ไม่ใช่ user, ไม่ใช่ service account ต้องมี first-class identity (Geordie + Noma ทำตัวนี้พร้อมกัน)
- **Action chain** — agent ทำ tool call หลาย ๆ step ใน session เดียว ต้อง audit เป็น chain ไม่ใช่ event เดี่ยว
- **MCP server discovery** — Shadow MCP (server ที่ developer install เองโดย security team ไม่รู้) เป็น threat vector ใหม่ ที่ Cloudflare เพิ่ง publish reference architecture แก้ตอน 28 พ.ค.

VC อ่านสัญญาณนี้ตรงกัน — **ARR 1,300% growth ใน 5 เดือนของ Geordie + Series F $200M ของ Coralogix ในสัปดาห์เดียวกัน = capital rotation ขนาดใหญ่เข้าชั้น AI infrastructure** Gartner ก่อนหน้านี้คาดว่า **40% ของ agentic AI project จะถูกยกเลิกภายในปี 2027 เพราะ governance failure** — ตัวเลขนี้คือ TAM ของ category นี้โดยตรง (เพราะ project ที่ไม่ยกเลิกจะ require governance product)

อีกมุมที่น่าสนใจ: ทั้ง Noma + Geordie + Cloudflare MCP + ServiceNow MCP Registry (publish 6 พ.ค. ที่ Knowledge 2026) — **4 product ที่แก้ปัญหาเดียวกัน** = "enterprise ไม่รู้ว่ามี MCP server กี่ตัวในระบบ, agent ทำอะไรได้บ้าง, ใครให้สิทธิ์เมื่อไหร่" tells ว่า **MCP adoption ไปเร็วกว่า governance tooling 6–12 เดือน** — gap ตรงนี้ = product opportunity ที่ทุก vendor พยายาม fill ตอนนี้

## มุม OpenBridge

OpenBridge ในฐานะ **integration layer = อยู่ตรง center ของ threat model นี้พอดี** — เพราะ MCP server + connector ของ OpenBridge เป็นจุดที่ enterprise data flow เข้า agent ทุก governance product ที่กล่าวมาต้อง integrate กับ integration layer ในที่สุด — OpenBridge ควร **เปิด API หรือ webhook สำหรับ governance product** (Noma, Geordie, ServiceNow MCP Registry) ให้ ingest metadata ของ OpenBridge MCP server ได้ตรง ๆ จะกลายเป็น "default integration" ที่ security team ทุกคนยอมรับ

นอกจากนั้น OpenBridge **ห้าม design ระบบบนสมมติฐาน "user credential = agent credential"** — pattern ที่ Noma + Geordie ทำคือ first-class agent identity ที่แยกจาก user OpenBridge ต้อง support identity ระดับ "agent คนนี้ (instance) ของ tenant นี้ ทำ action นี้ ตอนเวลานี้" ตั้งแต่ schema ของ audit log ถ้าออกแบบ identity ผิดวันนี้ จะ migrate ยากมากในปีหน้า

สุดท้าย Geordie ARR 1,300% growth เป็น **benchmark ที่ใช้ measure ตัวเอง** — ถ้า OpenBridge หา product-market fit ใน enterprise integration + agent governance ได้, growth rate ระดับนี้เป็นไปได้ pattern Geordie คือ niche แต่ deep — focus วันละ 1 segment (เช่น "MCP server inventory ที่ enterprise security team ใช้") แทนที่จะกว้างทันที — model ที่ OpenBridge ควรพิจารณา

## Sources
- [Noma Launches Agentic Access Control to Govern AI Agents and MCP Servers Across the Enterprise — PR Newswire](https://www.prnewswire.com/news-releases/noma-launches-agentic-access-control-to-govern-ai-agents-and-mcp-servers-across-the-enterprise-302788534.html)
- [Noma brings visibility and access governance to AI agents and MCP servers — Help Net Security](https://www.helpnetsecurity.com/2026/06/02/noma-brings-visibility-and-access-governance-to-ai-agents-and-mcp-servers/)
- [Controlling Agent and MCP Access with Noma — Noma Security Blog](https://noma.security/blog/controlling-agent-and-mcp-access-with-noma/)
- [Geordie Raises $30M to Help Enterprises Securely Adopt Agentic AI at Scale — Balderton Capital](https://www.balderton.com/news/geordie-raises-30m-to-help-enterprises-securely-adopt-agentic-ai-at-scale/)
- [Exclusive: Geordie AI raises $30 million Series A to be 'air traffic control' for your company's AI agents — Fortune](https://fortune.com/2026/05/28/geordie-security-governance-ai-agents/)
- [Geordie raises $30M Series A led by Balderton — Tech Funding News](https://techfundingnews.com/geordie-raises-30m-series-a-led-by-balderton-to-become-the-security-layer-enterprises-need-as-ai-agents-take-over-their-infrastructure/)

---

## Audio script
สวัสดีครับ Yoh เช้านี้มี 2 ข่าวที่รวมกันบอกว่ามี category ใหม่เกิดขึ้นในตลาด cybersecurity ภายใน 6 วันเดียว 28 พ.ค. ถึง 2 มิ.ย. ก้อนแรก Geordie AI startup London ปิด Series A 30 ล้านดอลลาร์ นำโดย Balderton ร่วมกับ Crosspoint General Catalyst Ten Eleven Ventures valuation 180 ล้านดอลลาร์ ตัวเลขที่ทำให้ VC เทเงินคือ ARR โต 1,300% ใน 5 เดือนแรกของปี 2026 และชนะ RSAC Innovation Sandbox 2026 ก้อนสอง Noma เปิดตัว Agent Access Control วันที่ 2 มิ.ย. ระบบที่ build inventory ของทุก AI agent ทุก MCP server ทั่ว enterprise โดยอัตโนมัติ feature หลักคือ Enterprise Agentic Registry update real-time, Agent Identity ให้ identity เฉพาะกับทุก agent ไม่ใช้ user credential, Governance Model 3 สถานะ Approved Requires Review Blocked, และ Tool-Level Control approve block ระดับ tool ไม่ใช่ระดับ server สองข่าวนี้รวมกัน confirm ว่า AI agent security เป็น category ใหม่จริง ไม่ใช่ subcategory ของ DLP CASB EDR ที่ Big Cyber อย่าง Palo Alto CrowdStrike Wiz เคยครอบ เพราะ threat model ของ agent ต่างจาก endpoint Gartner เคยคาดว่า 40% ของ agentic AI project จะถูกยกเลิกภายในปี 2027 เพราะ governance failure ตัวเลขนี้คือ TAM ของ category โดยตรง สำหรับ OpenBridge มีสามเรื่อง หนึ่ง OpenBridge อยู่ตรง center ของ threat model นี้พอดี เพราะ MCP server กับ connector ของเราเป็นจุดที่ enterprise data flow เข้า agent ควรเปิด API หรือ webhook ให้ governance product ingest metadata ตรง ๆ จะเป็น default integration ที่ security team ยอมรับ สอง ห้าม design ระบบบนสมมติฐาน user credential เท่ากับ agent credential ต้อง support first-class agent identity ตั้งแต่ schema ของ audit log ออกแบบผิดวันนี้ migrate ยากมากในปีหน้า สาม Geordie ARR 1,300% growth เป็น benchmark ที่น่าใช้ measure ตัวเอง pattern คือ niche แต่ deep focus วันละ segment เดียวแทนกว้างทันที model ที่ควรพิจารณาครับ
