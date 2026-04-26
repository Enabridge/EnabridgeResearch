---
date: 2026-04-27
slug: 26-04-27-0617-02-adobe-cx-enterprise-agentic-rebrand
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a customer journey funnel transformed into a translucent crystalline orchestration plane with multiple flowing data ribbons converging into a single conductor figure made of light, abstract minimalist shapes, muted coral magenta and deep navy palette, soft volumetric lighting, no text, no logos, no faces
image:
---

# Adobe ทุบ Experience Cloud ทิ้ง — รีแบรนด์เป็น "CX Enterprise" agentic-first พร้อม MCP endpoints, 1,770+ ลูกค้า entitled, partner ครบทั้ง 7 hyperscaler/frontier lab: customer experience layer กลายเป็นสนามรบ orchestration ใหม่

## TL;DR
- Adobe ประกาศที่ Adobe Summit (20 เม.ย.) **ทุบแบรนด์ Experience Cloud อายุ 13 ปี ทิ้ง** เปลี่ยนเป็น **CX Enterprise** — agentic-first, MCP endpoints native, "Coworker" agent layer + governance plane
- **1,770+ ลูกค้า entitled** ใช้ agent ผ่าน credit-based pricing tier ทันที (จาก 20,000+ Adobe enterprise base) — หมายถึง ~9% migrate มาใช้ agentic mode ใน 1-2 weeks
- **Partner ecosystem ครบ 7 ตัวใหญ่**: AWS, Anthropic, Google Cloud, IBM, Microsoft, NVIDIA, OpenAI — Adobe เลือก orchestrator stance, ไม่ผูก hyperscaler ใด

## เกิดอะไรขึ้น

วันที่ 20 เม.ย. ที่ Adobe Summit ลาสเวกัส (วันเดียวกับ Adobe ประกาศ Firefly Studio รุ่นใหม่) Anjul Bhambhri หัวหน้า Adobe Experience Cloud ขึ้น keynote ประกาศสิ่งที่ analyst ในห้องเรียกว่า **"การฆ่าแบรนด์ตัวเองเพื่อเกิดใหม่"** — Adobe Experience Cloud ที่ดำเนินการมาตั้งแต่ปี 2013 (จาก Marketing Cloud + Analytics Cloud + Advertising Cloud merge) **จะถูกแทนที่ทั้งหมดด้วยชื่อใหม่ "CX Enterprise"** ซึ่งเป็น agentic AI system end-to-end ครอบคลุมตั้งแต่ acquire prospect → engage → convert → loyalty.

ใจกลางของ CX Enterprise คือ **"Coworker"** — persistent agent layer ที่ Bhambhri อธิบายว่า "ไม่ใช่ chatbot, ไม่ใช่ workflow automation — เป็น colleague ที่จดจำ context ของ campaign, รู้ว่า audience segment ไหนตอบสนองกับ creative asset ไหน, ดำเนินการ optimization ได้เอง". CX Enterprise Coworker สามารถ assemble agents + tools ข้าม Adobe products (Real-Time CDP, Customer Journey Analytics, Experience Manager, Marketo) + 3rd-party platforms (Salesforce CRM, ServiceNow ITSM, Snowflake data warehouse) ผ่าน **Model Context Protocol endpoints native** + **A2A protocol** ที่ Adobe ประกาศ adopt วันเดียวกัน.

ตัวเลขที่ Bhambhri เผยใน keynote แล้ว analyst ตามจับ — **1,770+ ลูกค้า entitled ใช้ agent feature ทันที** ผ่าน credit-based pricing tier ใหม่ (ไม่เปิดเผยราคา, แต่ Constellation Research ประเมินว่า starting tier ~$5K/month ต่อ workspace + $0.05-0.20 ต่อ agent execution). **Adobe มี enterprise base 20,000+ brands** — หมายความว่า ~9% migrate เข้า agentic mode ภายใน 1-2 สัปดาห์แรก ซึ่งเป็นตัวเลขที่ปกติ enterprise rebrand ใช้เวลา 6-12 เดือน. Adobe ประกาศ partner ecosystem ใหม่ครบ — **AWS, Anthropic, Google Cloud, IBM, Microsoft, NVIDIA, OpenAI** ทั้ง 7 hyperscaler/frontier lab — โดย Coworker จะ route requests ไปยัง model ที่เหมาะกับ task: Claude สำหรับ campaign reasoning, GPT-5.5 สำหรับ creative copy, Gemini สำหรับ data analytics, Llama 4 บน NVIDIA สำหรับ image segmentation.

นอกจาก Coworker, Adobe เปิด **Agent Skills marketplace** (developer สามารถ ship agent skill บน CX Enterprise ผ่าน revenue share ~70/30, model เดียวกับ App Store), **Audit & Governance plane** (track agent decision lineage, retain compliance log สำหรับ GDPR/CCPA/EU AI Act), และ **Brand Safety guardrails** (agent ห้าม publish ad ที่ขัดกับ brand guidelines ที่ encode ไว้ใน policy DSL ของ Adobe). Quote ที่ Bhambhri ทิ้งไว้: "Marketing tech stack ที่ใช้ workflow automation ปี 2020 ตอนนี้เป็น tech debt — CX Enterprise คือ vertical agentic OS ของ customer lifecycle".

## ทำไมสำคัญ

นี่คือ **moment ที่ vertical SaaS giant accept เกม agentic แล้ว rebuild stack ของตัวเอง — ไม่ใช่ทาบ AI feature ลงบน UI เก่า**. Adobe ใช้เวลา 18 เดือนสร้าง CX Enterprise ตั้งแต่ Q4 2024 (รายงาน internal ที่ Constellation อ้างอิง) — เลือก path ที่ **risky ที่สุด**: ทุบแบรนด์เก่า + repackage pricing + force migration. เปรียบเทียบกับ Salesforce ที่ใช้ "Agentforce add-on" บน Sales/Service Cloud เดิม — Adobe เลือก burn the boats. ถ้าสำเร็จ — Adobe จะ define playbook ที่ Workday, Oracle Cloud, SAP, ServiceNow ตาม. ถ้าล้มเหลว — Adobe เสี่ยงเสีย 13 ปีของ brand equity ใน Marketing Cloud namespace.

ที่ smart คือ **partner ecosystem ที่กว้างผิดปกติ — ครบ 7 frontier lab**. Adobe ตัดสินใจเป็น **orchestrator stance, ไม่ผูก hyperscaler** — ต่างจาก Salesforce (lock-in กับ Anthropic + AWS), ServiceNow (lock-in กับ Microsoft + OpenAI), Workday (lock-in กับ Google). Adobe ตำแหน่งตัวเองเป็น **"Switzerland ของ CX layer"** — ลูกค้าเลือก model + cloud ได้, Adobe เก็บ control plane + ลูกค้า. นี่คือ pattern เดียวกับ Anthropic ที่กำลังทำในระดับ frontier model layer (รับเงินจาก AWS + Google ทั้งคู่). **Switzerland positioning จะกลายเป็น default playbook ของ vertical SaaS ปี 2026-2027** — ลูกค้า enterprise ไม่ยอมเดิมพัน hyperscaler ใด เพราะ TPU shortage / Trainium delays / GPU allocation politics.

ที่น่าจับตาสำหรับ analyst คือ **9% adoption ใน 1-2 weeks เป็นตัวเลขจริงหรือ press number**. ถ้าจริง — แสดงว่า enterprise CMO/CDO **ยอมจ่าย credit-based pricing ใหม่ทันที** เพื่อ access agentic feature, สวนทางกับ Stanford AI Index 2026 ที่บอก 89% ของ enterprise AI agent project ไม่ถึง production. คำอธิบายที่น่าจะใช่: Adobe มี **embedded ลึกใน workflow ของ marketing team แล้ว** (data + content + journey + identity) ทำให้ "deployment" จริงๆ คือ flip switch ไม่ใช่ build from scratch. นี่คือ moat ที่ AI-native challenger (Hightouch, Census, RudderStack, etc.) ไม่มี — pre-existing data graph + content library + identity resolver.

## มุม OpenBridge

**Indirect relevance — แต่สำคัญสำหรับ positioning**. CX Enterprise ไม่แข่งกับ OpenBridge โดยตรง (Adobe เล่น tier enterprise ระดับ Fortune 500 เป็น primary, ราคา starting tier ~$5K/month เกิน Thai SME budget) แต่ **playbook ของ Adobe คือ template ที่ OpenBridge ต้องเรียน** — โดยเฉพาะ 3 จุด:

(1) **Agent Skills marketplace + 70/30 revenue share** — OpenBridge สามารถ replicate model นี้สำหรับ Thai SaaS ecosystem. เปิด "OpenBridge Skills Catalog" ให้ developer Thai ship agent skill (เช่น "Auto-reconcile FlowAccount with K-Bank statement", "Trigger LINE OA broadcast เมื่อ Shopee inventory < 5 ชิ้น") โดย OpenBridge เก็บ 30% revenue share. ตลาด developer Thai ที่ active ~15-20K คน — ถ้าได้ 5% (~1,000 dev) ขาย skill เฉลี่ย 500 บาท/เดือน × revenue share 30% = ~150K บาท/เดือน + flywheel effect.

(2) **Switzerland positioning (ไม่ผูก hyperscaler/LLM)** — OpenBridge ต้อง ship **BYO-LLM tier** ที่ลูกค้าเลือก Claude/GPT/Gemini/Llama เองได้ ภายใน 30 วัน. นี่ไม่ใช่ technical hard ปัญหา — ใช้ LiteLLM/OpenRouter wrapper + agent framework abstraction. แต่ marketing/positioning ต้องชัด: "OpenBridge — Switzerland ของ Thai SaaS automation layer".

(3) **Audit/Governance plane เป็น differentiator ไม่ใช่ feature optional** — Adobe ทำให้ governance เป็น first-class plane ใน CX Enterprise. OpenBridge ต้องตามทันที — โดยเฉพาะใน Thai context ที่ PDPA + BOT (Bank of Thailand) compliance + IRD audit เป็น hard requirement. ออก "OpenBridge Audit Trail" feature ที่ retain agent decision lineage, exportable เป็น CSV ส่ง KPMG/Deloitte/PwC Thailand audit ได้ภายใน 60 วัน. นี่จะเป็น sales weapon ที่ปิดดีล Thai mid-market enterprise (200-2000 employees) ที่กังวล PDPA fines.

Action 14 วัน: (a) draft 3-pager spec ของ OpenBridge Skills marketplace + revenue share economics, (b) ออก "BYO-LLM" tier announcement, (c) brief design partner 5 รายแรกของ Audit/Governance plane (FlowAccount, PEAK, K-Bank Biz, LINE OA, KTC).

## Sources
- [Adobe Summit: Adobe Redefines Customer Experience Orchestration Vision in the Agentic AI Era with Introduction of CX Enterprise (Adobe News)](https://news.adobe.com/news/2026/04/adobe-redefines-custome-experience)
- [Adobe rebrands Experience Cloud as 'CX Enterprise,' goes all-in on AI agents (MarTech)](https://martech.org/adobe-rebrands-experience-cloud-as-cx-enterprise-goes-all-in-on-ai-agents/)
- [Adobe Summit 2026: Agentic orchestration for CX, creative workflows (Constellation Research)](https://www.constellationr.com/insights/news/adobe-summit-2026-agentic-orchestration-cx-creative-workflows)
- [Adobe Summit 2026, Day 1: The Rise of the 'Agentic Enterprise' (CMS Critic)](https://cmscritic.com/adobe-summit-2026-day-1-the-rise-of-the-agentic-enterprise)

---

## Audio script
เรื่อง Adobe น่าสนใจมากนะ Yoh เพราะมันคือ vertical SaaS giant ตัวแรกที่ยอม burn the boats ทุบแบรนด์เก่าทิ้งเพื่อรีบิวด์ stack agentic. วันที่ 20 เมษายน Adobe Summit ลาสเวกัส Anjul Bhambhri หัวหน้า Experience Cloud ประกาศ kill brand Experience Cloud ที่อายุ 13 ปี เปลี่ยนเป็น CX Enterprise — agentic-first ใช้ MCP endpoints native, มี Coworker agent layer ที่จำ context campaign ได้, หมุน optimization เอง. ตัวเลขที่หนักคือ 1,770 ลูกค้า entitled ใช้ agent feature ทันทีจาก base 20,000 brand เท่ากับ 9% migrate เข้า agentic mode ใน 1-2 สัปดาห์ ปกติ rebrand ใช้เวลา 6-12 เดือน. ที่ smart คือ partner ecosystem ครบ 7 ราย AWS, Anthropic, Google, IBM, Microsoft, NVIDIA, OpenAI Adobe เลือก orchestrator stance ไม่ผูก hyperscaler ใด — เป็น Switzerland ของ CX layer. ลูกค้าเลือก model เลือก cloud ได้ Adobe เก็บ control plane กับลูกค้า. มุม OpenBridge — indirect แต่ playbook สำคัญ. 3 จุดต้องเรียน: หนึ่ง เปิด OpenBridge Skills marketplace 70/30 revenue share ให้ Thai dev ship agent skill, สอง ship BYO-LLM tier ให้ลูกค้าเลือก Claude GPT Gemini Llama เอง 30 วัน positioning Switzerland ของ Thai SaaS automation, สาม ทำ Audit Trail plane เป็น first-class feature ไม่ใช่ optional เพราะ PDPA กับ BOT audit ต้องการ. design partner 5 ราย FlowAccount PEAK K-Bank Biz LINE OA KTC. 14 วันออก spec กับ announcement.
