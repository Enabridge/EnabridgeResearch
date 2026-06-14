---
date: 2026-06-15
slug: ntt-data-google-cloud-500-agents-gemini
topic: agentic-ai
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial illustration of a Google Cloud logo and NTT DATA logo joined by
  a glowing factory conveyor belt, producing rows of 500 small Gemini agent
  capsules that fan out toward labeled industry pavilions: "Banking",
  "Insurance", "Manufacturing", "Retail". Large floating numerals "500 AI
  agents" and "5,000 certified experts" hover above the factory line.
  Render style: cinematic editorial illustration, isometric perspective,
  Google blue and red factory lighting against deep navy industrial floor,
  high-contrast typography legible at 200px thumbnail. No real human faces
  — silhouettes only at industry pavilions.
image: images/26-06-15-0604-03-ntt-data-google-cloud-500-agents-gemini.png
---

# NTT DATA + Google Cloud — 500 Gemini agents เป็น "reusable building blocks" สำหรับ banking/insurance/manufacturing/retail พร้อม 5,000 certified experts

## TL;DR
- 8 มิ.ย. NTT DATA + Google Cloud expand collaboration — joint roadmap **500 AI agents** ครอบคลุม banking, insurance, manufacturing, retail; agents เป็น "reusable building blocks" ที่ลูกค้า deploy ซ้ำได้
- NTT DATA ตั้ง **Gemini Enterprise practice** ใหม่ — เป้า **5,000 certified experts** ที่ deploy/maintain Gemini Enterprise ในระบบลูกค้า
- ครอบคลุม software development, cloud migration, marketing, procurement, finance — pattern เดียวกับ TCS-Anthropic (11 มิ.ย.) แต่ใช้ Gemini แทน Claude — distribution war heat up

## เกิดอะไรขึ้น

วันที่ 8 มิ.ย. 2026 NTT DATA Group และ Google Cloud ประกาศ expand collaboration ครั้งใหญ่ — focus ที่ "moving enterprises from AI experimentation to scaled deployment" บน Gemini Enterprise สามเสาหลักของดีล: (1) **Gemini Enterprise practice** ใหม่ของ NTT DATA ที่เป้าหมายให้มี **5,000 certified experts** สำหรับ deploy, integrate, และ maintain Gemini Enterprise ในระบบลูกค้า (2) **joint roadmap 500 AI agents** ที่ co-innovate กับ Google Cloud เป็น "reusable building blocks" ที่ลูกค้า deploy ซ้ำได้ในหลาย vertical (3) end-to-end service: strategy → implementation → adoption → managed services → value realization ที่ NTT DATA รับผิดชอบทั้ง lifecycle ของ deployment

500 agents ตัวนี้ครอบคลุม **horizontal use cases** (software development, cloud migration, marketing, procurement, finance) และ **vertical-specific** ใน 4 industry หลัก: banking, insurance, manufacturing, retail Approach ที่น่าสนใจคือไม่ได้สร้าง agent ใหม่ทุกครั้งสำหรับแต่ละลูกค้า แต่สร้าง catalog ของ agent ที่ tested แล้ว ลูกค้าใหม่ "deploy ซ้ำ" ได้ — model นี้คือ vertical SaaS แบบที่ Salesforce Agentforce ใช้ แต่ทำในเชิง SI partnership

NTT DATA เป็น $30B+ revenue SI สัญชาติญี่ปุ่นที่มีฐานลูกค้าในเอเชีย + ยุโรป + อเมริกาเหนือ ในระดับ Fortune Global 500 — ครอบคลุมหลายอุตสาหกรรมที่ Google Cloud อยากเข้าให้ลึกขึ้น (BFSI ในญี่ปุ่น, manufacturing ในเยอรมัน, retail ใน UK) Google Cloud ตอนนี้มี gap กับ Microsoft Azure ใน enterprise relationship — Gemini Enterprise ที่เปิดตัวต้นปี 2026 มี feature ดี แต่ go-to-market ติดเพราะลูกค้า enterprise ไม่มี SI ที่ specialize ใน Google Cloud พอ การ scale 5,000 certified experts ของ NTT DATA = closing the gap แบบเร็วที่สุด

Pattern ที่น่าสนใจ: ดีลนี้ประกาศ 3 วันก่อน TCS-Anthropic — Google ก้าวก่อน Anthropic ในเรื่อง SI partnership แต่ TCS-Anthropic มี advantage ใน scale per single customer (50,000 associates internal vs. 5,000 experts external) ที่จะ scale ต่อไปเป็น 500,000 end users ใน TCS client base

## ทำไมสำคัญ

3 ดีลใน 5 วัน — Google + NTT DATA (8 มิ.ย.), OpenAI + Oracle (10 มิ.ย.), Anthropic + TCS (11 มิ.ย.) — เป็น **moment ที่ enterprise AI distribution ปรับโครงสร้างพร้อมกัน** ทุก frontier lab เห็นตรงกันว่า self-serve API + ChatGPT subscription ไม่พอสำหรับ Fortune 500 / regulated industry ต้องอาศัย channel ที่อยู่ในระบบลูกค้าอยู่แล้ว — system integrator (NTT DATA, TCS) หรือ cloud (Oracle) Google เลือกทาง SI เพราะ Gemini Enterprise ยังต้อง customization สูงในแต่ละ vertical OpenAI เลือกทาง cloud เพราะ Codex + frontier models เน้น horizontal use cases Anthropic เลือก SI เพราะ ตอบ regulated industry ที่ต้อง compliance heavy

500 agents เป็น "catalog approach" ที่จะ shape mental model ของ enterprise buyer ในปีหน้า — ลูกค้าจะถามว่า "vendor X มี catalog ของ agent กี่ตัวที่ pre-built สำหรับ vertical ของฉัน" แทนที่จะถาม "model ของ vendor X ทำอะไรได้บ้าง" Salesforce Agentforce ตอนนี้มี 100+ pre-built agent skills, ServiceNow มี 300+, NTT DATA targeting 500 บน Gemini ตัวเลขแบบนี้กลายเป็น procurement metric ที่ทุก vendor ต้องตอบให้ได้

จุดที่ Google + NTT DATA ต่างจาก Salesforce Agentforce คือ — **agent ไม่ได้ผูกกับ CRM platform เดียว** NTT DATA จะ build agent ให้ deploy ได้บน Gemini Enterprise ทั้ง standalone หรือ embed ใน SAP, ServiceNow, ระบบ banking core, ระบบ insurance core ของลูกค้า — broader composability ที่ Salesforce ไม่มี และนี่คือ defensible position ที่ Google Cloud + NTT DATA ตั้งเป้า: **"agent fabric ที่อยู่ทุกที่ในระบบลูกค้า ไม่ใช่ในแอป CRM อย่างเดียว"**

## มุม OpenBridge

500 agents ของ NTT DATA + Google Cloud ที่เป็น "reusable building blocks" คือ **threat โดยตรง** ของ position "connector marketplace" — NTT DATA จะมี catalog ของ agent ที่ตัวเอง pre-integrate กับ enterprise system ของลูกค้าไว้แล้ว ลูกค้าใหม่ที่ใช้ NTT DATA จะได้ทั้ง agent + integration + consulting เป็น bundle เดียว — OpenBridge ที่ขายแค่ connector layer จะ commoditize ทันที ทางออกของ OpenBridge: position เป็น "infrastructure ที่ NTT DATA/TCS/Accenture ใช้ใต้ board" ไม่ใช่ alternative ของ SI

ที่ต้องอ่านชัด — NTT DATA ทำ "joint roadmap" กับ Google Cloud ไม่ใช่ "เป็น customer ของ Google Cloud" position ของ NTT DATA ในเลเยอร์ value chain สูงกว่าที่คิด: เป็น **co-product owner** ของ 500 agents = NTT DATA ได้ revenue share จาก agent ที่ใช้ใน customer base ของตัวเอง + sell ต่อให้ลูกค้ารายอื่นที่ไม่ใช่ NTT DATA delivery — เป็น product business ไม่ใช่ consulting business เดิม OpenBridge ควรคิดในมุมเดียวกัน — ถ้า build "connector + agent template" ที่ SI หลายเจ้าใช้ได้ ก็เปลี่ยน business model จาก "selling integration" เป็น "platform ที่มี recurring revenue per deployment" คล้ายที่ HubSpot ทำกับ marketing automation 10 ปีก่อน window สั้น 6–12 เดือนก่อน NTT DATA / TCS build catalog ของตัวเองที่ครอบจักรวาล

## Sources
- [NTT DATA Expands Collaboration with Google Cloud to Accelerate Enterprise AI from Pilots to Production — NTT DATA Press Release](https://www.nttdata.com/global/en/news/press-release/2026/june/060900)
- [NTT DATA Expands Collaboration with Google Cloud to Accelerate Enterprise AI from Pilots to Production — NTT DATA Newsroom](https://services.global.ntt/en-us/newsroom/ntt-data-expands-collaboration-with-google-cloud)
- [NTT DATA and Google Cloud expand collaboration on agentic AI — Techzine Global](https://www.techzine.eu/news/applications/141910/ntt-data-and-google-cloud-expand-their-collaboration-on-agentic-ai/)
- [NTT DATA expands Google Cloud work on Gemini Enterprise — Cloud Computing News](https://www.cloudcomputing-news.net/news/ntt-data-google-cloud-gemini-enterprise-ai-deployments/)
- [Google Cloud Adds NTT DATA to Gemini Enterprise Delivery Push — ERP Today](https://erp.today/google-cloud-ntt-data-gemini-enterprise-ai/)
- [NTT DATA and Google Cloud Gemini enterprise push targets scale — DQ Channels](https://www.dqchannels.com/news/ntt-data-and-google-cloud-gemini-enterprise-push-targets-scale-12024197)

---

## Audio script
สวัสดีครับ Yoh ข่าวที่สามคือ NTT DATA กับ Google Cloud 8 มิถุนายน ขยาย collaboration ครั้งใหญ่ Joint roadmap สร้าง 500 AI agents เป็น reusable building blocks ครอบคลุม banking insurance manufacturing retail พร้อมตั้ง Gemini Enterprise practice ใหม่ที่เป้าหมาย 5,000 certified experts สำหรับ deploy integrate maintain Gemini ในระบบลูกค้า 500 agents ครอบคลุม horizontal use cases เช่น software development cloud migration marketing procurement finance และ vertical-specific 4 อุตสาหกรรมหลัก approach ที่น่าสนใจคือไม่ได้สร้าง agent ใหม่ทุกครั้งสำหรับแต่ละลูกค้า แต่สร้าง catalog ของ agent ที่ tested แล้ว ลูกค้าใหม่ deploy ซ้ำได้ Pattern เดียวกับ vertical SaaS แบบ Salesforce Agentforce แต่ทำในเชิง SI partnership ดีลนี้ประกาศ 3 วันก่อน TCS-Anthropic 3 ดีลใน 5 วัน Google NTT DATA Anthropic TCS OpenAI Oracle เป็น moment ที่ enterprise AI distribution ปรับโครงสร้างพร้อมกัน 500 agents เป็น catalog approach ที่จะ shape mental model ของ enterprise buyer ในปีหน้า ลูกค้าจะถามว่า vendor X มี catalog ของ agent กี่ตัวที่ pre-built สำหรับ vertical ของฉัน Salesforce Agentforce มี 100+ ServiceNow มี 300+ NTT DATA targeting 500 บน Gemini ตัวเลขแบบนี้กลายเป็น procurement metric สำหรับ OpenBridge 500 agents ของ NTT DATA ที่เป็น reusable building blocks คือ threat โดยตรง ของ position connector marketplace ทางออก position เป็น infrastructure ที่ NTT DATA TCS Accenture ใช้ใต้ board ไม่ใช่ alternative ของ SI window สั้น 6 ถึง 12 เดือนก่อน NTT DATA TCS build catalog ของตัวเองครอบจักรวาลครับ
