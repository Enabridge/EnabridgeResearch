---
date: 2026-05-08
slug: servicenow-action-fabric-mcp-anthropic-claude-cowork
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A bold editorial illustration in deep navy and warm cream — at center, a glowing teal bridge labelled 'ACTION FABRIC' arches between two cliffs. On the left cliff sits a row of glossy navy AI agent orbs labelled tiny but crisp 'CLAUDE / COPILOT / CUSTOM'. On the right cliff is a stylized vault door cut from cream and coral marked 'SERVICENOW SYSTEM OF ACTION'. Above the bridge floats a bright coral banner reading 'MCP' in big sans-serif and a cream tag '300+ AGENT SKILLS'. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + teal palette, no human figures, all text and logos crisp for 200px thumbnail readability.
image: 
---

# ServiceNow Action Fabric เปิด MCP Server ให้ "ทุก agent" ทำงานในระบบ — Anthropic เป็น launch partner ผ่าน Claude Cowork

## TL;DR
- ServiceNow ประกาศ Action Fabric ที่ Knowledge 2026 (5 พ.ค. 2026) — MCP Server เปิด **GA แถมในทุก Now Assist + AI Native SKU** ให้ agent ภายนอก (Claude, Microsoft Copilot, Gemini, custom agent ที่ลูกค้า build เอง) เรียก flows / playbooks / approvals / catalogs ของ ServiceNow ได้แบบ headless ทุก call ผ่าน AI Control Tower → identity-verified, permission-scoped, fully auditable
- **Anthropic เป็น launch partner** ของ Action Fabric ผ่าน "Claude Cowork" — agent ของ Claude เข้า ServiceNow ผ่าน MCP เป็น first-class citizen; ServiceNow position ตัวเองเป็น "place where every other vendor's agent comes to do real work" — ไม่ใช่ผูกขาดด้วย agent ของตัวเอง
- Pattern ที่ชัดมาก: MCP กลายเป็น **OAuth ของ AI era** — Microsoft, Google, AWS, OpenAI, Anthropic, ServiceNow ทุกรายรองรับแล้ว — บริษัทไหนยังไม่มี MCP server บน product ตัวเอง คือ "default ไม่อยู่ใน flow ของลูกค้า" และจะหายไปใน 12–18 เดือน

## เกิดอะไรขึ้น

วันที่ 5 พ.ค. 2026 ที่ Knowledge 2026 (Las Vegas) ServiceNow ประกาศ Action Fabric — MCP Server แบบ generally available ที่เปิดให้ AI agent **ทุกตัว** ไม่ว่าจะ build บน ServiceNow, Anthropic Claude, Microsoft Copilot, Google Gemini, หรือ custom agent ของลูกค้าเอง สามารถเรียกใช้ "system of action" ของ ServiceNow ได้ตรง ๆ แบบ headless: flows, playbooks, approvals, catalogs, workflow ทั้งหมดที่อยู่บน Now Platform + Configuration Management Database + Workflow Data Fabric ทุก call หลายชั้น ผ่าน AI Control Tower (AICT) เป็นกลาง — identity-verified ผ่าน enterprise SSO, permission-scoped ตาม role ของ user/agent นั้น, fully auditable ลง log ทุก step โดน reviewer มองเห็น real-time

ที่น่าจับตามากที่สุดคือ **Anthropic เป็น launch partner** อย่างเป็นทางการ — ผ่าน "Claude Cowork" agent ของ Claude เข้าไปใน ServiceNow ผ่าน MCP server ได้ใน day 1 เหมือนเป็น first-class citizen ServiceNow CEO Bill McDermott พูดในคีย์โน้ตว่า ServiceNow ไม่ได้ตั้งใจสู้กับ Claude หรือ Copilot หรือ Gemini แต่ตั้งใจเป็น "place where every other vendor's agent comes to do real work" — pivot ที่สำคัญมากเพราะ ServiceNow มี own agent (Now Assist) แต่ยอมเปิดให้ agent คู่แข่งใช้ system of action ของตัวเองพร้อมกัน

Action Fabric แถมมาพร้อมกับ **300+ pre-built AI agent skills** ที่ลูกค้า reuse ได้ — แต่ละ skill คือ encapsulation ของ workflow มาตรฐาน เช่น "ปิด incident IT", "approve PR", "kick off onboarding flow" — agent ภายนอกเรียก skill เดียวก็ได้ result กับมา แทนที่จะต้อง stitch หลาย API call เอง pricing ที่ก่อ shock ในวงคือ MCP Server **included** ในทุก Now Assist + AI Native SKU ที่ลูกค้าซื้ออยู่แล้ว — ไม่ต้องจ่ายเพิ่ม ServiceNow ตัดสินใจให้ MCP เป็น default ไม่ใช่ premium feature เพื่อ lock การเป็น integration hub

วันเดียวกัน Microsoft Agent 365 ประกาศ general availability + Novaworks shipping Core HR operating system บน MCP — สามค่ายใหญ่ออก MCP-native product พร้อมกันใน 24 ชั่วโมงเดียว ตามคำของ Asanify "ผูกกันเป็นวันที่ MCP กลายเป็น standard ของ enterprise AI"

## ทำไมสำคัญ

Pattern หลัก: MCP กำลังกลายเป็น **OAuth ของ AI era** ปี 2025 ทุกคนเถียงว่า MCP จะกลายเป็น standard จริงหรือเปล่า, จะถูก fragmenting หรือไม่; ปี 2026 ทุกค่ายใหญ่ — Microsoft (Agent 365), Google (Cloud Next 2026 ประกาศ managed MCP servers), AWS (Bedrock Managed Agents), OpenAI (Workspace Agents/Frontier), Anthropic (Claude Cowork), ServiceNow (Action Fabric) — **shipped MCP product ภายใน Q2 เดียวกัน** บริษัทไหนยังไม่มี MCP server บน product ตัวเองในวันนี้ คือ "default ไม่อยู่ใน flow ของลูกค้า" — และจะตกขบวนใน 12–18 เดือน เหมือน SaaS ที่ไม่มี OAuth ในปี 2014

นัยที่สอง: **ServiceNow choose openness over proprietary lock-in** — ถ้าให้ Now Assist เป็น only agent ที่ใช้ Action Fabric ได้ ServiceNow ก็ขายเฉพาะ AI Native SKU ราคา premium แต่จะกินส่วนแบ่งแค่ลูกค้าที่ซื้อ stack ของ ServiceNow ทั้งกอง การยอมเปิดให้ Claude/Copilot/Gemini/custom agent ใช้ — แลกเปลี่ยนกับการเป็น default "system of action" ที่ทุก agent มา dock เพื่อจะทำงานได้ — เก็บ rent ที่ governance plane (AI Control Tower license) แทนที่ที่ runtime — pricing model คล้าย Stripe ที่เก็บค่า transaction ไม่ใช่ค่า dev seat

นัยที่สาม: **Anthropic launch partner choice** เป็น signal ว่า Anthropic จะไม่ build "agent platform" ของตัวเอง — Anthropic เลือกขาย Claude เป็น runtime ที่อยู่ใน infra ของ partner (Microsoft 365, ServiceNow Action Fabric, Google Cloud Vertex/Gemini Enterprise, Bedrock), ไม่สู้ Microsoft Agent 365 / OpenAI Frontier head-on — strategic choice ที่ play เข้ากับ $200B Google TPU deal (Anthropic ลงทุนใน compute, ปล่อยให้ partner build distribution) ที่ปลายทาง: agentic AI จะเป็น layered cake — model layer (Anthropic, OpenAI, Google), runtime layer (Frontier, Agent 365, Action Fabric), control plane (Control Tower, Frontier audit, Microsoft Defender Shadow AI), service layer (Accenture/EY/Deloitte FDE)

## มุม OpenBridge

OpenBridge ต้อง execute 3 ทางจากข่าวนี้ทันที (1) **Ship MCP server ที่ "auto-register" ใน ServiceNow Action Fabric registry** — ตอนนี้ Action Fabric มี 300+ pre-built skill บน Now Platform; ถ้า OpenBridge มี MCP server ที่ Action Fabric discover ได้ ทุก ServiceNow customer ใน enterprise IT จะมี "OpenBridge connector skill" พร้อมเรียกใช้ใน Now Assist + Claude Cowork ทันที — ไม่ต้อง build ใหม่; กลายเป็น default integration ระดับเดียวกับ SAP/Salesforce/Oracle (2) **Build "OpenBridge Cowork" บน MCP** — แพ็คเกจที่ลูกค้าซื้อ ChatGPT Enterprise + Claude Cowork + Microsoft Agent 365 ใช้ OpenBridge เป็น single point ที่ทุก agent เรียก HubSpot/Stripe/Shopify/LINE OA — ขาย "agent-portable connector" ที่ทำงานได้ทุก runtime; messaging "เขียน workflow ครั้งเดียว รันได้ทุก agent platform" (3) **Position OpenBridge AI Control Tower equivalent** — emit OpenTelemetry agent semantic convention ที่ ServiceNow AICT, Microsoft Defender, OpenAI Frontier audit consume ได้หมด — กลายเป็น "Switzerland of agent telemetry" ที่ enterprise เลือก plug-in ที่ governance plane ใดก็ได้

Adjacent insight: ที่ ServiceNow ยอม include MCP server ฟรีในทุก SKU = signal ว่า MCP server กลายเป็น commodity feature ภายใน 6 เดือน, value capture ย้ายไปที่ catalog ของ skill / connector / governance — OpenBridge ต้อง position ตัวเองที่ skill catalog (depth) + telemetry (governance), ไม่ใช่ที่ MCP server (จะถูก undercut ฟรีในไม่ช้า)

## Sources
- [ServiceNow opens its full system of action to every AI Agent in the enterprise | ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx)
- [AI News Deep Dive, May 6: The Open MCP Agent Platform Race Hits Your HR Stack | Asanify](https://asanify.com/blog/news/open-mcp-agent-platform-may-6-2026/)
- [ServiceNow Wants to Be the Control Layer for Every AI Agent in the Enterprise | Reworked](https://www.reworked.co/digital-workplace/servicenow-launches-action-fabric-major-overhaul-of-ai-control-tower/)
- [ServiceNow Knowledge 2026: AI Control Tower, Action Fabric, Autonomous Workforce and more | Constellation Research](https://www.constellationr.com/insights/news/servicenow-knowledge-2026-ai-control-tower-action-fabric-autonomous-workforce-and)

---

## Audio script
ต่อกันเรื่องที่สองครับโย ServiceNow ที่เปิด Knowledge 2026 ในลาสเวกัสเมื่อ 5 พฤษภาคม นอกจาก kill switch ที่เราเล่ากันเมื่อวาน ของจริงในงานคือ Action Fabric ตัว MCP server ที่เปิดให้ AI agent ทุกตัว ทั้ง Claude Microsoft Copilot Google Gemini หรือ agent ของลูกค้าเอง เรียกใช้ flows playbooks approvals catalogs ของ ServiceNow ได้ตรงแบบ headless ทุก call ผ่าน AI Control Tower verified scoped auditable

ที่สำคัญที่สุดคือ Anthropic เป็น launch partner ผ่าน Claude Cowork agent ของ Claude เข้า ServiceNow ผ่าน MCP เป็น first class CEO Bill McDermott พูดเองว่า ServiceNow ไม่ได้สู้กับ Claude หรือ Copilot แต่ตั้งใจเป็น place where every other vendor's agent comes to do real work pivot สำคัญเพราะ ServiceNow มี Now Assist เองแต่ยอมเปิดให้คู่แข่งใช้ และที่ shock วงการคือ MCP server แถมฟรีในทุก Now Assist และ AI Native SKU

Pattern หลักคือ MCP กลายเป็น OAuth ของ AI era ปี 2026 Microsoft Google AWS OpenAI Anthropic ServiceNow ทุกรายชิป product MCP native ใน Q2 เดียวกัน บริษัทไหนยังไม่มี MCP server วันนี้ จะ default ไม่อยู่ใน flow ของลูกค้า เหมือน SaaS ที่ไม่มี OAuth ในปี 2014 และ ServiceNow ตัดสินใจเก็บ rent ที่ governance plane ไม่ใช่ runtime model คล้าย Stripe ที่เก็บค่า transaction

มุม OpenBridge สามเรื่อง หนึ่งคือ ship MCP server ที่ auto register ใน Action Fabric registry ทุก ServiceNow customer จะมี OpenBridge connector skill พร้อมเรียกทันทีใน Now Assist และ Claude Cowork สองคือ build OpenBridge Cowork ที่ทุก agent เรียก HubSpot Stripe Shopify LINE OA ได้ผ่าน connector เดียว เขียน workflow ครั้งเดียวรันได้ทุก agent platform สามคือ position ตัวเองเป็น Switzerland ของ telemetry emit OpenTelemetry agent convention ให้ AICT Defender Frontier consume ได้หมด ที่สำคัญ MCP server ตัวมันเองจะกลายเป็น commodity ใน 6 เดือน OpenBridge ต้อง capture value ที่ skill catalog และ telemetry ไม่ใช่ที่ MCP server เปล่า ๆ ครับ
