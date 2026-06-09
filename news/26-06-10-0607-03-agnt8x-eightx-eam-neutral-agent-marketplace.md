---
date: 2026-06-10
slug: agnt8x-eightx-eam-neutral-agent-marketplace
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a glowing five-pillar Greek temple labeled FIND,
  FORGE, STUDIO, MANAGE, CONDUCTOR, sheltering a row of small robotic agent
  figures from multiple LLM provider logos (Claude orb, GPT spiral, Gemini
  prism) hovering above. A large blueprint scroll unfurls in front bearing
  the title "EAM v0.1 · Apache 2.0" with the agnt8x wordmark stamped boldly.
  Style: cinematic editorial illustration, isometric perspective, neutral
  marble-and-steel palette with electric cyan accents, dramatic lighting
  from the temple interior, high-contrast typography legible at 200px
  thumbnail. No real human faces — only robotic silhouettes.
image: images/26-06-10-0607-03-agnt8x-eightx-eam-neutral-agent-marketplace.png
---

# agnt8x เปิด neutral marketplace ของ AI agent ข้ามทุก LLM — open-source EAM v0.1 ภายใต้ Apache 2.0 ตั้งเป้าเป็น HTML ของ agent layer

## TL;DR
- 3 มิ.ย. EightX Labs (UK) เปิด agnt8x — platform กลางที่ enterprise ใช้ recruit, onboard, manage, orchestrate AI agent ข้าม Claude / GPT / Gemini ภายใต้ digital identity + audit trail + contract เดียว
- เปิด **EightX Agent Manifest (EAM) v0.1** ภายใต้ **Apache 2.0** — declarative spec ที่ describe agent (skills, connectors, sub-agents, policies) แบบ portable ข้าม runtime
- 5 module: **FIND / FORGE / STUDIO / MANAGE / CONDUCTOR** — บวก builder marketplace ที่ developer publish agent แล้วได้ recurring monthly revenue ตราบเท่าที่ agent ยัง run

## เกิดอะไรขึ้น

วันที่ 3 มิ.ย. 2026 EightX Labs (จดทะเบียนใน UK) ประกาศเปิด **agnt8x** — platform ที่ตั้งเป้าเป็น "neutral workforce management layer สำหรับ AI agent" ทั้งงาน enterprise และ developer marketplace agnt8x ทำในสิ่งที่ ServiceNow + Salesforce + Workday พยายามทำ แต่ทำใน **ฝั่ง model-neutral** — เปิดให้ enterprise hire/manage agent จาก Claude, GPT, Gemini, Llama, DeepSeek, Mistral ภายใต้ digital identity เดียว, audit trail เดียว, contract เดียว ไม่ต้อง integrate ทีละ vendor แยกกัน

ของจริงที่ทำให้ launch นี้สำคัญคือ **EightX Agent Manifest (EAM) v0.1** ที่ publish พร้อมกันภายใต้ **Apache 2.0 license** — EAM เป็น declarative spec ที่อธิบาย agent ในรูป "skills, connectors, sub-agents, policies" ในไฟล์ YAML/JSON เดียว แบบ runtime-agnostic agent ที่เขียนตาม EAM สามารถ compile ลง Claude Agents SDK, OpenAI AgentKit, Google Agent Engine, LangGraph, หรือ runtime ใด ๆ ก็ได้โดยไม่ต้อง rewrite — pattern ที่เหมือน HTML สำหรับ web (ที่ render บน Chrome, Safari, Firefox ได้เหมือนกัน)

Platform แบ่งเป็น **5 module** ที่เป็น lifecycle ของ AI workforce: **FIND** (search agent ในตลาด match skill ที่ต้องการ), **FORGE** (build agent ใหม่จาก EAM), **STUDIO** (test + version control + benchmark), **MANAGE** (deploy + monitor + cost control + compliance), **CONDUCTOR** (multi-agent orchestration ที่ route task ระหว่าง agent หลายตัว) ลูกค้า enterprise เลือกใช้ทั้ง 5 module หรือเลือกเฉพาะส่วนที่ต้องการก็ได้ — ที่สำคัญคือ "Passport" ที่เป็น digital identity ของแต่ละ agent ที่ตามทุก action ที่ agent ทำ (audit trail สำหรับ compliance + governance)

EightX Labs ไม่ได้เปิดเผยตัวเลข funding หรือ ARR แต่บอกว่ามี enterprise pilot กับ 12 บริษัท Fortune 500 (ไม่ระบุชื่อ) ในช่วง 6 เดือนที่ผ่านมา และ launch partner ใน builder marketplace มี 200+ agent ที่ publish ตั้งแต่วันเปิด ครอบคลุม use case ตั้งแต่ data analyst, sales SDR, legal contract review, ถึง DevOps incident response Pricing model สำหรับ developer คือ **recurring monthly revenue tied to agent runtime** — developer ได้เงินตราบเท่าที่ agent ยัง run ใน customer environment ของ enterprise ใด ๆ ก็ตาม

## ทำไมสำคัญ

EAM ภายใต้ Apache 2.0 เป็น **bet ที่ใหญ่กว่าตัว platform** — ถ้า EAM กลายเป็น standard ของอุตสาหกรรม (เหมือน HTML, OpenAPI, MCP) EightX Labs จะกลายเป็น governance body ที่ทุก agent platform ต้องอ้างอิง ตอนนี้ industry ขาด standard spec แบบนี้อย่างชัดเจน — Claude มี Agent Skills, OpenAI มี AgentKit (กำลังจะ deprecate Nov 2026), Google มี Agent Engine, LangGraph มี YAML configuration ของตัวเอง ทุก spec lock เข้า vendor เดียว EAM ที่ neutral + open จะดึงดูด developer ที่ไม่อยากเลือกข้าง

Pattern ที่ตามมาจาก EAM v0.1 คือ — **portability ของ agent กลายเป็นเงื่อนไข enterprise procurement** ลูกค้า enterprise ที่ deploy agent หลายร้อยตัว (ดู Sierra ที่ $150M ARR จาก voice agent, ดู Dust ที่ deploy 300K agent ในองค์กรเดียว) ไม่ยอม lock เข้า runtime เดียวอีกต่อไป CIO จะถามวันแรกว่า "agent นี้ portable ตาม spec อะไร?" และ EAM จะเป็นคำตอบที่ทุก vendor ต้องมีหรือ negotiate ระยะยาว pattern เดียวกับที่ OpenAPI/Swagger บีบ vendor REST API ในยุค 2015-2018

ที่ลึกกว่าคือ **agnt8x ตั้งคำถามต่อ business model ของ Claude Code, Cursor, Windsurf, Cognition Devin** ที่ขาย "agent ที่ทำงานได้ผ่าน specific runtime ของเรา" agnt8x บอกว่า — "ทำไมต้อง lock? hire agent ใน marketplace ของเราดีกว่า portable + ราคาแข่งกัน" ถ้า traction ตามนี้ Cognition Devin ($1B ARR, $26B valuation) จะถูกบีบให้เปิด integration กับ agnt8x หรือเสี่ยงโดน commoditize เพราะลูกค้า enterprise สามารถ rent agent ที่ทำสิ่งเดียวกันใน marketplace แทนได้

Pattern marketplace แบบนี้ — recurring revenue ที่ developer ได้ตราบเท่าที่ agent ยัง run — เป็นโมเดลที่ Apple App Store เคยทำกับ mobile app ในปี 2008-2012 และ epic value creation รอบนั้นเปลี่ยน industry ทั้งโลก agent marketplace อาจเป็น turning point เดียวกัน — แต่ที่ใหญ่กว่าเพราะ agent เป็น productive worker ที่ generate revenue ให้ enterprise ตรง ๆ ไม่ใช่แค่ entertainment app

## มุม OpenBridge

agnt8x เป็น **wake-up call ที่ตรงคู่กับ business model OpenBridge ที่สุดในรอบหลายเดือน** — สิ่งที่ agnt8x สร้างคือ "neutral integration layer + marketplace + governance" ที่ overlap กับ vision ของ OpenBridge อย่างมาก ความต่างคือ — agnt8x focus ที่ agent layer (deploy/orchestrate agent), OpenBridge focus ที่ data + tool integration layer (เชื่อม enterprise system เข้า agent) ตำแหน่งสองอันนี้ adjacent ไม่ใช่ overlap 100% แต่จะเริ่ม overlap ใน 12-18 เดือนแน่นอน — เพราะ agent ที่ deploy ผ่าน agnt8x จะต้องเรียกใช้ data/tool ที่ OpenBridge เป็น layer เดียวกัน

ทางเลือก strategic ของ OpenBridge มี 3 ทาง: (1) **partner กับ agnt8x** — เป็น first-class connector marketplace สำหรับ data + tool ใน EAM spec (ทำให้ทุก agent ใน agnt8x เรียก OpenBridge connector ได้); (2) **fork EAM spec** — เอา EAM มาเป็น base แล้ว extend ให้ support data plane operations แบบที่เราต้องการ (ส่ง back ให้ community); (3) **compete head-on** — สร้าง EAM equivalent ของเราเอง + marketplace แยก แต่ต้อง pace เร็วมากเพราะ network effect ของ EAM ที่ open + Apache 2.0 จะแซงเรา ทางที่ 1 เป็น lowest-risk highest-leverage แนะนำเริ่มทันที

ที่ต้องเรียนรู้จาก agnt8x คือ **license + spec แยกจาก platform** — EightX ให้ EAM ฟรีภายใต้ Apache 2.0 (ใครก็ implement ได้) แต่ platform agnt8x เป็น commercial product pattern นี้คือสิ่งที่ Anthropic ทำกับ MCP (spec open, Claude Code commercial), HashiCorp ทำกับ Terraform (เคยเป็น), MongoDB ทำกับ database OpenBridge ถ้ามี spec ของตัวเอง (เช่น "OpenBridge Connector Spec" หรือ "Enterprise Data Plane Manifest") ต้องวางแบบเดียวกัน — open + Apache 2.0 + governed by OpenBridge — เพื่อสร้าง community + lock-in ที่ technical, ไม่ใช่ commercial

## Sources
- [agnt8x — Hire AI agents from any provider. Govern them all.](https://agnt8x.ai/)
- [agnt8x Launches the World's First AI Agent Recruitment and Workforce Management Platform — GlobeNewswire](https://www.globenewswire.com/news-release/2026/06/03/3306081/0/en/agnt8x-launches-the-world-s-first-ai-agent-recruitment-and-workforce-management-platform.html)
- [EightX Labs Opens agnt8x, a Neutral Marketplace to Hire, Manage, and Orchestrate AI Agents Across Every Major LLM — BigGo Finance](https://finance.biggo.com/news/29ZyjZ4BaoGGrU-IQBD8)
- [Your next hire isn't human: agnt8x Launches the World's First AI Agent Recruitment and Workforce Management Platform — Thailand Business News](https://www.thailand-business-news.com/pr-news/your-next-hire-isnt-human-agnt8x-launches-the-worlds-first-ai-agent-recruitment-and-workforce-management-platform)
- [agnt8x Launches the World's First AI Agent Recruitment and Workforce Management Platform — Manila Times](https://www.manilatimes.net/2026/06/03/tmt-newswire/pr-newswire/agnt8x-launches-the-worlds-first-ai-agent-recruitment-and-workforce-management-platform/2357803)

---

## Audio script
สวัสดีครับ Yoh อยากให้ฟังเรื่องนี้ระวังเป็นพิเศษ เพราะ adjacent ที่สุดกับ OpenBridge 3 มิถุนายน EightX Labs ใน UK เปิด agnt8x platform ที่ตั้งเป้าเป็น neutral workforce management layer สำหรับ AI agent ทำในสิ่งที่ ServiceNow Salesforce Workday พยายามทำ แต่ทำใน ฝั่ง model-neutral เปิดให้ enterprise hire และ manage agent จาก Claude GPT Gemini Llama DeepSeek Mistral ภายใต้ digital identity เดียว audit trail เดียว contract เดียว ของจริงที่สำคัญคือ EightX Agent Manifest หรือ EAM v0.1 ที่ publish ภายใต้ Apache 2.0 ตามเดิม EAM เป็น declarative spec ที่อธิบาย agent ในรูป skills connectors sub-agents policies ในไฟล์ YAML เดียวแบบ runtime-agnostic agent ที่เขียนตาม EAM compile ลง Claude Agents SDK OpenAI AgentKit Google Agent Engine LangGraph ได้โดยไม่ต้อง rewrite เป็น HTML สำหรับ agent layer Platform แบ่ง 5 module FIND FORGE STUDIO MANAGE CONDUCTOR บวก builder marketplace ที่ developer publish agent แล้วได้ recurring monthly revenue ตราบเท่าที่ agent ยัง run ใน customer environment เป็น Apple App Store ของ agent age สำหรับ OpenBridge เรื่องนี้สำคัญสุด เพราะ overlap กับ vision ของเราโดยตรง agnt8x focus ที่ agent layer เรา focus ที่ data integration layer adjacent ไม่ overlap 100% แต่จะเริ่มทับใน 12 ถึง 18 เดือน 3 strategic option ที่ Yoh ต้องเลือก หนึ่ง partner กับ agnt8x เป็น first-class connector marketplace ใน EAM spec สอง fork EAM เอามาเป็น base แล้ว extend สำหรับ data plane operations สาม compete head-on สร้าง spec marketplace ของเราเอง ผมแนะนำตัว 1 เริ่มทันที lowest-risk highest-leverage บทเรียนที่ต้องเอามาใช้คือ license + spec แยกจาก platform เหมือนที่ Anthropic ทำกับ MCP ถ้า OpenBridge มี spec ของตัวเอง ต้อง open + Apache 2.0 + governed by OpenBridge สร้าง community lock-in technical ไม่ใช่ commercial ครับ
