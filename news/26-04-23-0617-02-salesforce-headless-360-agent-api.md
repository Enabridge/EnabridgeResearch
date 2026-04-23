---
date: 2026-04-23
slug: salesforce-headless-360-agent-api
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: Editorial illustration of a translucent glass CRM dashboard peeling away like a discarded skin, revealing a dense network of glowing API tendrils and agent connectors beneath, minimal flat geometric shapes, muted slate-blue and coral palette, soft gradient background, dramatic side lighting, no text no logos no faces
image: images/26-04-23-0617-02-salesforce-headless-360-agent-api.png
---

# Salesforce เปิด Headless 360 — ยอมทิ้ง UI ให้ agent ใช้ platform แทนมนุษย์ 60+ MCP tools + 30 coding skills ship ทันที

## TL;DR
- Salesforce เปิดตัว **Headless 360** ที่ TDX 2026 — strategy ที่ expose **ทุก capability** บน platform (CRM, Data Cloud, analytics) เป็น API, MCP tool, หรือ CLI command — "agent operate ทั้งระบบโดยไม่เปิด browser"
- Ship ทันที: **60+ MCP tools ใหม่** + **30 preconfigured coding skills** ให้ Claude Code / Codex / Windsurf / VS Code build app ทับ Salesforce ได้ตรง. Agentforce Vibes 2.0 + AgentExchange เปิดพร้อมกัน
- Case study: **Engine** (B2B travel management) build customer service agent "Ava" ใน **12 วัน** → handle **50% ของ case autonomously**
- CEO Benioff: "เราตัดสินใจ rebuild Salesforce for agents เมื่อสองปีครึ่งก่อน" — นี่ไม่ใช่ retrofit, เป็น architectural bet ระยะยาวที่ปะทะ Google Gemini Enterprise ตรง

## เกิดอะไรขึ้น

ที่ TDX 2026 ใน San Francisco กลางเดือน เม.ย. Marc Benioff เปิดตัวสิ่งที่ Salesforce ตั้งชื่อจงใจให้เข้าใจง่ายว่า **"Headless 360"** — คำว่า 360 คือ Customer 360 edition stack เดิมของ Salesforce; คำว่า **Headless** คือ "ไม่ต้องมี UI แล้ว". ท่าทีของ Benioff ชัดเจนบนเวที: "We made a decision two and a half years ago to rebuild Salesforce for agents." — เป็นภาษาที่ CEO ของ SaaS platform ขนาด 300 พันล้าน market cap ไม่ได้พูดออกมาง่าย ๆ

ตัวผลิตภัณฑ์ที่ ship ทันทีมีสามชั้น. **ชั้นแรก:** Salesforce expose **ทุก capability** ที่เคยซ่อนหลัง UI ออกเป็น **API first-class** — รวมถึง Data Cloud queries, analytical pipelines, workflow orchestration, permission grants, audit logs. **ชั้นที่สอง:** ปล่อย **60+ MCP tools ใหม่** ทั้งชุด ให้ Claude Code / Codex / Windsurf / Cursor / VS Code ที่เป็น agentic IDE เข้าถึง platform ได้ตรง — agent สามารถ query object, สร้าง flow, deploy Lightning component โดยไม่ต้องเปิด Setup UI. **ชั้นที่สาม:** **30 preconfigured coding skills** ที่ wrap pattern common (build approval flow, setup permission set, migrate legacy Apex) เป็น callable skill — agent ไม่ต้อง reinvent wheel

Case study ที่ Salesforce ยกขึ้นเวทีโดดเด่นที่สุดคือ **Engine** — B2B travel management startup. ทีม Engine ใช้ Agentforce สร้าง customer service agent ชื่อ "Ava" ใน **12 วัน** — ไม่ใช่ 12 สัปดาห์, ไม่ใช่ 12 เดือน. Ava ตอนนี้ **handle 50% ของ customer case autonomously** (ไม่มี human loop) — ส่วนที่เหลือ escalate เข้า human agent พร้อม context. Engine เป็น reference ที่ powerful เพราะไม่ใช่ Fortune 500 — ทีมเล็ก, ไม่มี AI research team, ship บน off-the-shelf Agentforce + Headless 360 APIs

**Agentforce Vibes 2.0** เป็นอีกชิ้นที่ประกาศพร้อมกัน — เป็น "vibe coding" interface ที่ให้ admin/consultant คุย natural language กับ agent แล้วสร้าง flow, permission, report ออกมาได้เลย. ท่านี้ตรงคู่แข่งกับ Google Workspace Studio ที่ประกาศวันเดียวกับนี้ (22 เม.ย.) — pattern เดียวกัน: no-code agent builder สำหรับ non-developer

จุดที่ต้อง note เป็นสัญญาณ: Salesforce **ไม่เลือก protocol เดียว**. Headless 360 expose capability ผ่าน **3 path พร้อมกัน** — REST API, CLI commands, MCP tools. ภาษาทางการของ Benioff คือ "insulating ourselves against protocol shifts" — แปลว่า Salesforce ไม่เดิมพันว่า MCP จะชนะ A2A จะชนะ; ออกมาตัวเดียวพร้อม ทุกคนใช้ได้. Strategic defensive move — ไม่ trend-chasing

## ทำไมสำคัญ

**Pattern เดียวกับ Google Gemini Enterprise แต่จากมุม vendor CRM** — และมันสำคัญกว่าที่ดูเผิน ๆ. Google ถือ compute + control plane; Salesforce ถือ **system of record** ของลูกค้า enterprise (customer data, pipeline, workflow). ถ้า Salesforce ยอม expose ทุกอย่างเป็น API/MCP/CLI **โดยที่ UI เป็นทางเลือก ไม่บังคับ** — แปลว่า layer "human interact with CRM" กลายเป็น **optional** อย่างถูกต้องตามสถาปัตยกรรม

Engine case study = **12 วัน 50% autonomous** คือตัวเลขที่ขายได้ในห้อง CFO ทุกที่. Benchmark เดิมของ CS automation (Intercom AI, Zendesk Agent AI) ช่วงปีที่ผ่านมาเคลม 20-30% deflection rate ใน 3-6 เดือน — Engine ทำได้ 50% ใน 2 สัปดาห์. ถ้าตัวเลขนี้ reproducible (แม้จะเป็น cherry-pick ของ Salesforce) — **software SaaS spending ปี 2027 จะเห็น budget shift 20-30% จาก "CS seats" ไป "agent seats"** ทั่ววงการ

เชิงยุทธศาสตร์ น่าจับตาคือ Salesforce **ปะทะ Google ชนกันตรงหัว**. Gemini Enterprise เชิญ Salesforce agents ขึ้น Model Garden (partner-built), แต่ Headless 360 สร้าง path ให้ลูกค้า skip Gemini Enterprise ไปเลย — "เขียน agent ด้วย Claude Code, เรียก MCP tool ของ Salesforce ตรง, ไม่ต้องผ่าน Gemini control plane". ทั้งสองรายไม่ได้เป็นเจ้าของ stack — แต่พยายามให้ **stack ตัวเองเป็น default ใน organization** ของลูกค้า. เกมนี้เหมือน iOS vs Android ช่วงปี 2010 — ทั้งคู่อยู่รอด แต่ลูกค้าเลือกข้าง

## มุม OpenBridge

**Direct threat + tactical opportunity:** Headless 360 = **Salesforce ลงมาเล่นใน lane เดียวกับ OpenBridge** — "our platform is an agent-accessible API layer". ข้อดี: Salesforce อยู่ในเซกเมนต์ enterprise ($300+ พันล้าน market cap) ที่ Thai SMB ไม่ใช่ target; ข้อเสีย: ถ้า Thai mid-market start ซื้อ Salesforce + Agentforce กันมาก (ผ่าน Salesforce Thailand partner network) — OpenBridge จะถูกแทนที่ในโจทย์ CRM/sales ops โดยตรง

**Product action 30 วัน:** (1) **Ship "OpenBridge MCP tools for Thai SaaS"** ตาม pattern Headless 360 60+ tools — wrap FlowAccount, PEAK, Loyverse, Wongnai POS เป็น callable MCP tool ให้ Claude Code / Codex ใช้สร้าง automation ทับ — **positioning: "Headless 360 for the Thai SMB stack"**; (2) **Reproduce "Engine case study" ท้องถิ่น** — ลงไปช่วย Thai SME (ร้านอาหาร/retail/logistics) build agent ด้วย OpenBridge ใน 2 สัปดาห์, วัด CS deflection rate, publish numbers — ใช้เป็น social proof ว่าของ Salesforce เฉพาะ enterprise, ของเราเฉพาะ SMB; (3) **เปิด "vibe coding" สำหรับ admin** — clone Agentforce Vibes 2.0 experience แต่ใช้ภาษาไทย, ยังไม่มี vendor ไทยไหนทำ, ได้ first-mover

**Strategic signal:** Benioff พูดว่า "rebuild for agents" ใช้เวลา **2.5 ปี**. OpenBridge ถ้าจะเอาจริง — ไม่มีเวลา 2.5 ปี. แต่ OpenBridge เล็กกว่ามาก ไม่มี legacy Lightning codebase ต้อง refactor. window คือ **6 เดือน** เพื่อประกาศ "OpenBridge-native agent architecture" แบบเดียวกับ Headless 360 ก่อน Thai enterprise buyer เริ่มถามว่า "ของคุณเป็น headless หรือยัง"

## Sources
- [Salesforce launches Headless 360 to turn its entire platform into infrastructure for AI agents (VentureBeat)](https://venturebeat.com/technology/salesforce-launches-headless-360-to-turn-its-entire-platform-into-infrastructure-for-ai-agents)
- [Salesforce debuts Headless 360 agentic platform (The Register)](https://www.theregister.com/2026/04/15/salesforce_headless_360/)
- [Salesforce Headless 360 and Agentforce Vibes 2.0 Revealed at TDX 2026 (Salesforce Ben)](https://www.salesforceben.com/salesforce-headless-360-and-agentforce-vibes-2-0-revealed-at-tdx-2026/)
- [Salesforce Opens Entire Platform to AI Agents With Headless 360 API Strategy (Creati.ai)](https://creati.ai/ai-news/2026-04-19/salesforce-headless-360-api-ai-agents-platform/)
- [Salesforce Shifts To API-first Future With Headless 360 (Dataconomy)](https://dataconomy.com/2026/04/17/salesforce-shifts-to-api-first-future-with-headless-360/)

---

## Audio script
ที่ TDX 2026 Marc Benioff เปิดตัว Headless 360. strategy ที่ expose ทุก capability ของ Salesforce platform เป็น API MCP tool หรือ CLI command ให้ agent operate ทั้งระบบโดยไม่เปิด browser. Benioff พูดบนเวทีว่า เราตัดสินใจ rebuild Salesforce for agents เมื่อสองปีครึ่งก่อน. นี่ไม่ใช่ retrofit. เป็น architectural bet.

สิ่งที่ ship ทันทีมีสามชั้น. หนึ่ง ทุก capability Data Cloud query analytical pipeline workflow orchestration permission audit log ออกเป็น API first class. สอง หกสิบ MCP tools ใหม่ ให้ Claude Code Codex Windsurf Cursor VS Code เข้าถึง platform ตรง สร้าง flow deploy Lightning component โดยไม่เปิด Setup UI. สาม สามสิบ preconfigured coding skills wrap pattern common build approval flow setup permission set migrate legacy Apex.

case study ที่โดดเด่นที่สุด. Engine บริษัท B2B travel management. build customer service agent ชื่อ Ava ใน สิบสองวัน. Ava handle ห้าสิบเปอร์เซ็นต์ของ customer case autonomously. Engine ไม่ใช่ Fortune 500. ทีมเล็ก ไม่มี AI research team. ship บน Agentforce plus Headless 360. นี่คือตัวเลขที่ขายได้ในห้อง CFO ทุกที่.

benchmark เดิม Intercom AI Zendesk Agent AI เคลม ยี่สิบถึงสามสิบเปอร์เซ็นต์ deflection ใน สามถึงหกเดือน. Engine ทำได้ ห้าสิบเปอร์เซ็นต์ใน สองสัปดาห์. ถ้าตัวเลขนี้ reproducible SaaS spending ปี 2027 budget จะ shift ยี่สิบถึงสามสิบเปอร์เซ็นต์ จาก CS seats ไป agent seats ทั่ววงการ.

Agentforce Vibes 2.0 คือ vibe coding interface ที่ admin คุย natural language กับ agent. pattern เดียวกับ Google Workspace Studio. Salesforce ไม่เลือก protocol เดียว. expose ทั้ง REST API CLI และ MCP พร้อมกัน. Benioff บอก insulating against protocol shifts.

pattern ใหญ่. Google ถือ compute plus control plane. Salesforce ถือ system of record. ทั้งคู่ชนกันตรงหัว ในการทำให้ stack ตัวเองเป็น default ใน organization ลูกค้า. iOS vs Android ยุค 2010 ทั้งคู่อยู่รอด ลูกค้าเลือกข้าง.

สำหรับ OpenBridge. Headless 360 คือ Salesforce ลงมาใน lane เดียวกับเรา. Thai SMB ยังไม่ใช่ target ของเขา. action สามสิบวัน. หนึ่ง ship OpenBridge MCP tools for Thai SaaS wrap FlowAccount PEAK Loyverse Wongnai position ว่า Headless 360 for Thai SMB stack. สอง reproduce Engine case study ท้องถิ่น ลงไปช่วย Thai SME build agent ใน สองสัปดาห์ วัด deflection publish. สาม เปิด vibe coding ภาษาไทย ยังไม่มี vendor ไทยไหนทำ first mover.

Benioff ใช้เวลาสองปีครึ่ง rebuild. OpenBridge ไม่มีเวลาเท่านั้น แต่เราเล็กกว่าไม่มี legacy. window หกเดือน ประกาศ OpenBridge native agent architecture ก่อน Thai enterprise buyer ถามว่า ของคุณ headless หรือยัง
