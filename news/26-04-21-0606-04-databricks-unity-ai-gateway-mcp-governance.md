---
date: 2026-04-21
slug: databricks-unity-ai-gateway-mcp-governance
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: Editorial illustration of a translucent portcullis gate woven from circuit lines guarding a warehouse of glowing data crates, small agent silhouettes waiting in line with tokenized badges, minimal flat shapes, muted indigo and copper palette, soft spotlight lighting, no text no logos no faces
image:
---

# Databricks รวม AI Gateway เข้า Unity Catalog — MCP governance, OBO access, end-to-end observability; Agent Bricks platform เปิดพร้อมกัน, positioning ตรงต่อ Snowflake Cortex + Salesforce Agentforce

## TL;DR
- Databricks ประกาศ **Unity AI Gateway** — ยก AI Gateway เข้าไปอยู่ภายใต้ **Unity Catalog** (governance layer ของ Databricks); apply policy + audit เดียวกันกับ agent ที่เรียก LLM + MCP + API
- Capability ใหม่: **MCP governance** ระบุว่า agent ไหน access MCP server ไหนได้ + **on-behalf-of (OBO)** access; unified model API across 70+ models มี fallback + rate limit built-in; full cost attribution ลงถึง workflow/team
- เปิดพร้อม **Agent Bricks** — governed enterprise agent platform — positioning ชัดต่อ Snowflake Cortex + Salesforce Agentforce + Adobe CX Enterprise
- IDC MarketScape 2025-2026 เพิ่ง name Databricks เป็น **Leader** ใน Unified AI Governance — timing ไม่บังเอิญ

## เกิดอะไรขึ้น

Databricks ใช้สัปดาห์นี้ — cycle ที่ Adobe/Microsoft/Anthropic/Cloudflare ทุกคน push agent stack พร้อมกัน — ประกาศ **Unity AI Gateway** ผ่าน official blog. ไม่ใช่ product ใหม่ที่แยกออกมา แต่เป็นการ **merge AI Gateway (ที่ launch เป็น standalone feature กลางปีที่แล้ว) เข้า Unity Catalog** — ซึ่งเป็น data + permission governance layer ที่ Databricks วางไว้ตั้งแต่ปี 2022

Move นี้สำคัญเพราะ Unity Catalog เป็น **crown jewel ของ Databricks** — **ที่ Snowflake ไม่มี equivalent ชัดเจน** ในตอนนี้. ทุก table, notebook, ML model, dashboard ใน Databricks ถูก govern ผ่าน Unity Catalog. ตอนนี้ **LLM call + MCP call + external API call** ของ agent ก็อยู่ภายใต้ policy engine เดียวกัน — แปลว่า CISO + data governance team ของ enterprise ไม่ต้อง maintain tool ใหม่; ทุกอย่าง reuse framework เดิม

Feature ที่ sharp ที่สุดคือ **MCP governance**: control ว่า agent ไหน invoke MCP server ไหนได้ — fine-grained ระดับ tool-by-tool — และ **on-behalf-of (OBO) access**, แปลว่า agent action จะถูก authorize ด้วย identity ของ user ที่ trigger (ไม่ใช่ identity ของ agent service account). Pattern นี้ solve **"confused deputy problem"** ใน agent security ที่เป็นหัวใจของ MCP vulnerability ที่ Anthropic ปฏิเสธแก้เมื่อสัปดาห์ที่แล้ว

Observability side: Unity AI Gateway emit **trace ของทุก LLM + MCP call** พร้อม metadata — latency, token count, cost, model, outcome — attribute ได้ถึง **team/project/workflow level**. คนที่ build agent จำนวนมากใน enterprise เจอ pain นี้ชัดเจน — **coding agent sprawl** (Cursor + Claude Code + GitHub Copilot + internal agent) ทำให้ finance team ไม่รู้ว่า $ X หมดไปกับ project ไหน. Databricks แก้ cost attribution ที่ gateway layer แทนให้ทีม BI ต้อง reconcile manual

ประกาศ Unity AI Gateway มาพร้อมกับ **Agent Bricks** — governed enterprise agent platform ที่ Databricks เรียกว่า "integrated platform that unifies data, models, governance, evaluation, deployment". Agent Bricks ใช้ Unity AI Gateway เป็น runtime substrate — positioning implicit คือ "ถ้าคุณ build enterprise agent นอก Agent Bricks, คุณกำลัง rebuild governance เอง"

Signal บาง ๆ แต่สำคัญ: IDC MarketScape Worldwide Unified AI Governance Platforms 2025-2026 เพิ่ง **name Databricks เป็น Leader** พร้อม launch นี้. ไม่บังเอิญ — analyst briefing cycle ของ IDC ใช้เวลา 6+ เดือน, Databricks plan launch นี้พอดีกับ cycle analyst เพื่อ max validation. คือ **coordinated launch + analyst stamp** ที่ Snowflake, Salesforce ยังไม่มี positioning เดียวกันใน category นี้

## ทำไมสำคัญ

สองสัปดาห์นี้เห็น **pattern เร่งตัว**: Microsoft Agent Framework 1.0 (3 เม.ย.) → Anthropic Claude Managed Agents (8 เม.ย.) → Cloudflare Agents Week (13-17 เม.ย.) → Adobe CX Enterprise Coworker (20 เม.ย.) → Databricks Unity AI Gateway (อาทิตย์นี้). ทุกเจ้า pitch **"governed agent platform"** พร้อมกันหมด. Category นี้กลายเป็น **"table stakes สำหรับ enterprise software 2026"** — ถ้าไม่มี MCP governance + agent observability + cost attribution, vendor ไม่ shortlist ใน enterprise RFP

ประเด็นที่ Databricks เดินแต้มได้ดีคือ **data gravity**. Snowflake + Databricks ถือ warehouse ของ **Fortune 500 ส่วนใหญ่** — ทุก agentic workflow ที่ mature จริงต้อง query enterprise data = ต้องผ่าน warehouse. Snowflake Cortex มี agent layer ของตัวเอง แต่ **governance story ยังไม่ sharp เท่า Unity Catalog**. Databricks ใช้ moment นี้ทำ "governance leader" positioning ก่อน Snowflake ตามทัน. คาดว่า Snowflake response ภายใน 30-45 วัน (Snowflake Summit มิ.ย.)

อีกจุดที่ต้อง note: **OBO access = เริ่มต้น end ของ "agent service account era"**. ปีที่แล้ว agent ส่วนใหญ่ใช้ service account ที่มี permission รวม = security nightmare. OBO pattern (agent action inherit permission จาก user) เป็น default ของ Microsoft 365 Copilot มาปีกว่าแล้ว แต่ Databricks เป็น **first data platform ที่ ship OBO สำหรับ MCP tool call** — และ spec นี้จะถูก copy โดย Snowflake/BigQuery ภายใน 90 วัน

## มุม OpenBridge

**ไม่ direct เกี่ยว แต่...** OpenBridge ไม่แข่งกับ Databricks/Snowflake — data platform layer ไม่ใช่ territory SMB. **Adjacent insight**: ภาษาที่ enterprise buyer ใช้ใน Q2 2026 กำลัง shift จาก "AI capability" เป็น "**AI governance + observability + cost attribution**". ถ้า OpenBridge sales deck ยังพูด "agent integration" ล้วน ๆ โดยไม่มี slide ว่า **"ทุก tool call มี audit log, cost attribution, scope minimization"** จะฟังเหมือน 2024 vendor

**Product absorb (30 วัน):** 
1. **Cost attribution dashboard** — แสดง token/call cost per workflow, per team; ใช้ copy pattern ของ Unity AI Gateway ในระดับ SME (ไม่ต้อง enterprise feature-parity, แค่ให้ลูกค้า Thai SME เห็น "คุณใช้ OpenAI ไปเดือนละกี่บาท แยกตาม channel/team")
2. **Policy slide ใน sales deck** — 1 slide เดียวก็พอ: "OpenBridge ทุก connector มี audit log + scope minimization + OBO-compatible" — พูดคำเดียวกับ enterprise vendor เพื่อ reduce perceived gap
3. **MCP-first positioning** — ถ้า OpenBridge push MCP server sooner, claim ได้ว่า "governed by your existing MCP gateway" — piggyback บน Unity AI Gateway, Cloudflare AI Gateway, Auth0 MCP Gateway แทนจะ build governance ของเอง (ไม่มี budget ทำ)

**Strategic watch:** **Snowflake Summit มิ.ย.** จะเป็นจุดที่ชัดว่า Snowflake จะ match Databricks governance story หรือปล่อย. ถ้า Snowflake ปล่อย = Databricks ยึด enterprise agent governance อย่างน้อย 12 เดือน = OpenBridge ควร messaging ว่า "OpenBridge works with Databricks Unity AI Gateway" เป็น proof point. ถ้า Snowflake response ดี = market ยัง fragment = OpenBridge มี time ปรับ messaging ช้ากว่า

## Sources
- [Databricks Blog — Expanding Agent Governance with Unity AI Gateway](https://www.databricks.com/blog/ai-gateway-governance-layer-agentic-ai)
- [Databricks Blog — Agent Bricks: The Governed Enterprise Agent Platform](https://www.databricks.com/blog/agent-bricks-governed-enterprise-agent-platform)
- [Databricks Blog — Governing Coding Agent Sprawl with Unity AI Gateway](https://www.databricks.com/blog/governing-coding-agent-sprawl-unity-ai-gateway)
- [Databricks Blog — Databricks Named a Leader in IDC MarketScape Unified AI Governance Platforms 2025-2026](https://www.databricks.com/blog/databricks-named-leader-idc-marketscape-worldwide-unified-ai-governance-platforms-2025-2026)
- [CIO Dive — Salesforce, Databricks unveil agentic AI governance tools](https://www.ciodive.com/news/salesforce-databricks-agentic-ai-governance/817746/)

---

## Audio script
Databricks ใช้อาทิตย์นี้ ที่ Adobe Microsoft Anthropic Cloudflare ทุกคน push agent stack พร้อมกัน. ประกาศ Unity AI Gateway. ไม่ใช่ product ใหม่. เป็นการ merge AI Gateway เข้า Unity Catalog. data + permission governance layer ที่ Databricks วางไว้ตั้งแต่ สองพันยี่สิบสอง.

move สำคัญเพราะ Unity Catalog คือ crown jewel ของ Databricks ที่ Snowflake ไม่มี equivalent ชัดเจน. ทุก table notebook ML model dashboard ถูก govern ผ่าน Unity Catalog. ตอนนี้ LLM call MCP call external API call ของ agent ก็อยู่ภายใต้ policy engine เดียวกัน. CISO ไม่ต้อง maintain tool ใหม่. ทุกอย่าง reuse framework เดิม.

feature ที่ sharp ที่สุดคือ MCP governance บวก on behalf of access. agent action จะถูก authorize ด้วย identity ของ user ที่ trigger ไม่ใช่ identity ของ agent service account. pattern นี้ solve confused deputy problem ใน agent security. เป็นหัวใจของ MCP vulnerability ที่ Anthropic ปฏิเสธแก้เมื่อสัปดาห์ที่แล้ว. Databricks แก้ที่ gateway layer แทน.

observability. Unity AI Gateway emit trace ของทุก LLM และ MCP call. cost attribution ลงถึง team project workflow level. coding agent sprawl Cursor Claude Code Copilot ทำ finance team ไม่รู้ว่าเงินหมดไปกับ project ไหน. Databricks แก้ cost attribution ที่ gateway.

pattern เร่งตัว. Microsoft สาม เม ย. Anthropic แปด. Cloudflare สิบสาม ถึงสิบเจ็ด. Adobe ยี่สิบ. Databricks อาทิตย์นี้. ทุกเจ้า pitch governed agent platform พร้อมกัน. category นี้กลายเป็น table stakes สำหรับ enterprise software สองพันยี่สิบหก.

สำหรับ OpenBridge. ไม่ direct แข่ง. แต่ adjacent insight สำคัญ. ภาษาที่ enterprise buyer ใช้ใน Q2 กำลัง shift จาก AI capability เป็น AI governance observability cost attribution. ถ้า OpenBridge sales deck ยังพูด agent integration ล้วน ๆ โดยไม่พูด audit log cost attribution scope minimization จะฟังเหมือน vendor สองพันยี่สิบสี่.

product absorb สามสิบวัน. cost attribution dashboard. policy slide. MCP first positioning piggyback บน Unity AI Gateway Cloudflare AI Gateway Auth0. OpenBridge ไม่ต้อง build governance เอง. แค่ต้อง emit signal ว่า govern-able.

watch Snowflake Summit มิถุนายน. ถ้า Snowflake match Databricks ได้ market ยัง fragment OpenBridge ปรับ messaging ช้า. ถ้าไม่ match Databricks ยึด enterprise agent governance สิบสองเดือน OpenBridge messaging ว่า works with Databricks Unity AI Gateway.
