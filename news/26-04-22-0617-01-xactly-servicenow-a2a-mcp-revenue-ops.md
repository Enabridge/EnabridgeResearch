---
date: 2026-04-22
slug: xactly-servicenow-a2a-mcp-revenue-ops
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: Editorial illustration of two robotic figures shaking hands across a glowing bridge of data tokens that flows between two separate glass platforms, minimal flat geometric shapes, muted teal and burnt orange palette, soft gradient background, dramatic rim lighting, no text no logos no faces
image: images/26-04-22-0617-01-xactly-servicenow-a2a-mcp-revenue-ops.png
---

# Xactly + ServiceNow ยิง Agent-to-Agent MCP production agent ตัวแรกใน revenue ops — "Dispute Management Agent" เล่น commission dispute ผ่าน A2A orchestration

## TL;DR
- **21 เม.ย.** Xactly (sales performance management leader, Vista Equity-owned) ประกาศร่วมกับ ServiceNow เปิด **Dispute Management AI Agent** ตัวแรกที่ production — built บน **MCP + agent-to-agent (A2A) orchestration** เชื่อม Xactly revenue platform กับ ServiceNow Now Assist
- เป้าหมายคือ **automate commission dispute end-to-end** — seller ถามผ่าน chat, Now Assist คุยกับ Xactly agent, แก้ข้อสงสัยโดยไม่ต้องสร้าง ticket formal
- Framework นี้ **ไม่ใช่ one-off** — Xactly + ServiceNow ประกาศว่าจะทยอยปล่อย "fleet of agents" ตามมา = framework agnostic สำหรับ revenue ops ทั้ง funnel
- Signal: **A2A cross-vendor ไม่ใช่ demo อีกแล้ว** — enterprise SaaS vendor สอง brand ตกลง contract + production SLA บน MCP handshake

## เกิดอะไรขึ้น

วันอังคารที่ 21 เม.ย. — ตรงกับที่ ServiceNow เตรียมประกาศ Q1 2026 earnings วันพุธ — Xactly และ ServiceNow เปิดตัว **Dispute Management AI Agent** เป็น agent-to-agent production integration ตัวแรกระหว่างสอง platform. เสียงในข่าวอาจจะกลืน แต่โครงสร้างของ announcement นี้ **ต่างจาก MCP integration ทั่วไปที่เราเห็นมาทั้งเดือน** — เพราะมันไม่ใช่ "ให้ ChatGPT/Claude call เข้า API ของเรา" แต่เป็น **"agent ของเราคุยกับ agent ของคุณโดยตรง"**

Chris Li, CPO ของ Xactly, อธิบายสั้น ๆ ว่า: "This solution marks a shift beyond just AI to intelligent, autonomous revenue orchestration." คำที่น่าจับตาคือ **orchestration** — ไม่ใช่ assistant, ไม่ใช่ copilot. Anandan Jayaraman, VP Product, Sales CRM ของ ServiceNow เสริมเป็นภาษาที่ชัดกว่า: "Xactly and ServiceNow's Dispute Management Agent demonstrates how **agent-to-agent orchestration** can eliminate manual processes and accelerate resolution cycles for revenue teams." — เน้นคำว่า agent-to-agent ตรงตัว ไม่อ้อม

Use case เริ่มจาก pain point ที่ revenue ops ทุกบริษัทรู้จักดี: seller ที่ commission คำนวณไม่ตรงกับที่คิดจะ ping manager → manager เปิด ticket ใน ServiceNow → finance ต้องเปิด Xactly ไปเช็ค policy → กลับไปอธิบายใน ticket → ปิดเคส. รอบหนึ่งกินเวลาเป็นวัน. agent ใหม่ทำงานแทนทั้ง loop: seller ถาม Now Assist ว่า "เดือนที่แล้วคอมมิชชันลดลงทำไม" → Now Assist **ยิง MCP call เข้า Xactly agent โดยตรง** → Xactly ดึง policy + transaction + attainment → คำตอบเด้งกลับพร้อม context ภายในสนทนาเดียว. ถ้าเป็นข้อโต้แย้งจริง ๆ ถึงจะ escalate เป็น ticket — แต่ส่วนมาก 70-80% ของ "dispute" จริง ๆ เป็นคำถามที่ตอบได้

จุดที่น่าจะโดนมองข้ามคือ **commercial model**. ทั้ง Xactly และ ServiceNow ประกาศว่า Dispute Management Agent เป็นแค่ตัวแรกของ **"fleet of agents"** — ไม่ใช่ one-off integration. สอง vendor ตกลง architecture กลางว่าใช้ MCP + A2A เป็น substrate แล้วทยอยปล่อย agent pair เพิ่มตามฟังก์ชัน: forecasting, quote approval, territory planning, revenue recognition. นี่คือ commitment ยาว ไม่ใช่ PR stunt

Context ที่ต้องไม่ลืม: ServiceNow Q4 2025 รายงาน Now Assist มี **net new ACV โต 2x YoY + 244 ดีล $1M+** — ตัวเลขที่ signal ว่า AI agent เป็น main growth driver จริง, ไม่ใช่ rounding error. Dispute Management Agent จึงไม่ใช่การทดลอง — มันคือ reference architecture ที่ ServiceNow จะใช้ขายลง sales ops vertical ต่อไป. Xactly ได้ distribution ผ่าน ServiceNow installed base (~8,100 enterprise customers), ServiceNow ได้ vertical depth ที่ตัวเองไม่มี

## ทำไมสำคัญ

Pattern ที่เห็นในสัปดาห์เดียว — Adobe CX Enterprise วันจันทร์ใช้ MCP + A2A, Knak Enterprise Marketing วันเดียวกันเปิด MCP server, Xactly + ServiceNow วันอังคารเปิด A2A production agent — สะท้อนว่า **"agent-to-agent" ข้ามจาก protocol paper ไปเป็น SLA-backed commercial integration ในสัปดาห์เดียว**. Adobe บอกว่า "เราจะใช้ A2A" (future tense); Xactly + ServiceNow **กำลังใช้แล้ว** (present tense ที่มี CPO + VP Product ของทั้งสองบริษัทยืนการันตี)

ที่น่าจับตากว่าคือ **ตำแหน่งของ Xactly ในห่วงโซ่**. Xactly ไม่ใช่ hyperscaler ไม่ใช่ CRM leader — มันเป็น **category-specific SaaS** (sales performance management, ขนาดตลาด ~$2-3B). ถ้า Xactly/ServiceNow ทำ A2A ได้ **ทุกคู่ SaaS vendor ทำได้**. เมื่อก่อน integration ระหว่าง SaaS ต้องพึ่ง Mulesoft/Workato/Zapier เป็น middleware; ตอนนี้ **MCP + A2A = middleware ไม่ต้องมี** — agent ของ vendor A พูดกับ agent ของ vendor B โดยตรง. นี่คือ existential threat ต่อ category ของ iPaaS ทั้งยวง — ไม่ใช่ 3-5 ปีข้างหน้า แต่ **ภายใน 12-18 เดือน**

Bet ของผม: ภายในสิ้น Q2 เราจะได้เห็น Workday + ServiceNow, Adobe + Salesforce, Atlassian + HubSpot เปิด A2A pair แบบเดียวกัน — ทุก cross-vendor "strategic partnership" ที่เคยทำผ่าน data connector จะ **port ขึ้น A2A ในรอบ announcement ถัดไป** เพราะ buying committee ของลูกค้าเริ่มถามแล้วว่า "ของคุณคุยกับ vendor อื่นของผมผ่าน MCP ได้ไหม" ถ้าตอบไม่ได้ = ตกรอบ

## มุม OpenBridge

**Direct threat + existential lens:** Dispute Management Agent **คือ exactly สิ่งที่ OpenBridge ควรเป็น** — แต่ build โดย SaaS vendor สองรายเจ้าเอง ไม่ต้องผ่าน integration platform คนกลาง. ถ้าเทรนด์นี้ลามไป Thai SaaS stack (FlowAccount ↔ PEAK, LINE OA ↔ SCB Connect, K-Plus ↔ PromptPay) — vendor จับคู่กันเอง **OpenBridge เสียบใต้ไม่ได้**. ทางรอดไม่ใช่การแข่งกับ A2A โดยตรง แต่เป็นการ **positioning เป็น "broker layer" ระหว่าง A2A pair ที่ไม่ได้มี official partnership** — พอที่ตลาด Thai SMB มี pair combo นับร้อยที่ไม่มีทาง invest partner ต่างฝ่ายต่างกันเอง

**Product action 30 วัน:** (1) **ออก "A2A broker" feature**: ให้ OpenBridge เป็น MCP server ที่ proxy call ไปยัง 3-5 Thai SaaS (FlowAccount, PEAK, Wongnai POS, Loyverse, LINE OA) ที่ยังไม่มี native MCP — ขายใน pitch deck ว่า "until vendor builds MCP, OpenBridge is their MCP"; (2) **publish playbook "how to replace your Workato job with A2A"** — ใช้ Xactly + ServiceNow เป็น reference case, แสดงว่า OpenBridge = agent-mediated replacement; (3) เริ่มคุย **revenue ops vertical ใน Thai enterprise** (SCB, KBank, PTT, AIS) — เอา commission dispute pattern มาเสนอ LOC เดียวกัน, ใช้ Xactly case เป็น existence proof

**Strategic signal:** Thai SMB โอกาสยัง open กว่า US enterprise เพราะ Thai SaaS vendor ส่วนใหญ่ยังไม่มี MCP roadmap — OpenBridge มี **6-12 เดือน window** ก่อนที่ SCB/KBank/LINE เริ่ม bundle MCP เข้า product. ใช้ window นี้ลงรากเป็น default integration layer ก่อน ไม่งั้นเมื่อ Thai vendor เริ่ม native — OpenBridge จะเหลือแค่ long tail

## Sources
- [Xactly and ServiceNow Launch Agent-to-Agent AI Integration for Revenue Operations (DestinationCRM)](https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/Xactly-and-ServiceNow-Launch-Agent-to-Agent-AI-Integration-174463.aspx)
- [Xactly and ServiceNow Launch Agent-to-Agent AI Integration (Yahoo Finance)](https://ca.finance.yahoo.com/news/xactly-servicenow-launch-agent-agent-123000563.html)
- [ServiceNow to Announce First Quarter 2026 Financial Results on April 22 (Investor Relations)](https://investor.servicenow.com/news/news-details/2026/ServiceNow-to-Announce-First-Quarter-2026-Financial-Results-on-April-22/default.aspx)
- [ServiceNow Unveils ServiceNow AI Platform (The Agile Brand Guide)](https://agilebrandguide.com/servicenow-unveils-servicenow-ai-platform/)
- [Introducing Xactly's AI Lab: Enterprise-Ready AI for the Future of SPM](https://www.xactlycorp.com/blog/artificial-intelligence/introducing-xactlys-ai-lab-enterprise-ready-ai-future-spm)

---

## Audio script
วันอังคารที่ยี่สิบเอ็ดเมษา Xactly กับ ServiceNow เปิดตัว Dispute Management AI Agent ตัวแรกของ agent to agent production integration ระหว่าง SaaS vendor สอง brand. ไม่ใช่ MCP plug in ที่ให้ ChatGPT เรียกเข้า API. แต่เป็น agent ของ Xactly คุยกับ agent ของ ServiceNow ผ่าน MCP handshake ตรง.

use case คือ commission dispute. seller ถาม Now Assist ว่าเดือนที่แล้วคอมมิชชันลดลงทำไม. Now Assist ยิง MCP call เข้า Xactly agent. Xactly ดึง policy transaction attainment. คำตอบเด้งกลับในสนทนาเดียว. รอบที่เคยกินเวลาเป็นวันลด เหลือไม่กี่นาที. Chris Li CPO Xactly เรียกสิ่งนี้ว่า autonomous revenue orchestration.

ที่น่าจับตาที่สุดคือภาษาของ Anandan Jayaraman VP Product ServiceNow. เรียกตรงๆว่า agent to agent orchestration. ไม่อ้อม. และทั้งสอง vendor ประกาศว่าจะทยอยปล่อย fleet of agents ตาม Dispute Management Agent. ไม่ใช่ one off. เป็น commitment ยาวใน revenue ops funnel forecasting quote approval territory planning revenue recognition.

signal สำคัญคือ. Xactly ไม่ใช่ hyperscaler ไม่ใช่ CRM leader. เป็น category SaaS ขนาดสองถึงสามพันล้าน. ถ้า Xactly ServiceNow ทำ A2A ได้ทุกคู่ SaaS vendor ทำได้. middleware integration ที่เคยพึ่ง Mulesoft Workato Zapier. ตอนนี้ MCP plus A2A equal middleware ไม่ต้องมี. agent ของ vendor A คุย agent ของ vendor B ตรง. นี่คือ existential threat category iPaaS ในสิบสองถึงสิบแปดเดือน.

Adobe บอกจันทร์ที่แล้วว่าจะใช้ A2A future tense. Xactly ServiceNow กำลังใช้แล้ว present tense. Workday Salesforce Atlassian HubSpot น่าจะตามในไตรมาสนี้.

สำหรับ OpenBridge. Dispute Management Agent คือ exactly สิ่งที่ OpenBridge ควรเป็น. แต่ build โดย SaaS vendor เอง ไม่ผ่าน integration platform. ถ้า FlowAccount PEAK LINE OA SCB Connect K Plus PromptPay จับคู่กันเองผ่าน A2A. OpenBridge เสียบใต้ไม่ได้. ทางรอด position เป็น broker layer ระหว่าง A2A pair ที่ไม่มี official partnership.

action สามสิบวัน. หนึ่ง ออก A2A broker feature. OpenBridge เป็น MCP server proxy call ไป Thai SaaS ที่ยังไม่มี native MCP. ขายว่า until vendor builds MCP OpenBridge is their MCP. สอง publish playbook how to replace Workato with A2A ใช้ Xactly ServiceNow เป็น reference. สาม เริ่มคุย revenue ops vertical Thai enterprise SCB KBank PTT AIS เอา commission dispute pattern มาเสนอ window สิบสองเดือนก่อน Thai vendor native MCP
