---
date: 2026-04-27
slug: 26-04-27-0617-01-a2a-protocol-150-orgs-linux-foundation
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: Editorial illustration of overlapping translucent hexagonal nodes connected by glowing data threads forming a cross-platform network mesh, abstract geometric circuit patterns radiating between nodes, muted indigo teal and warm amber palette, dramatic side lighting on a dark canvas, minimal flat shapes, no text, no logos, no faces
image: images/26-04-27-0617-01-a2a-protocol-150-orgs-linux-foundation.png
---

# A2A Protocol แตะ 150 องค์กร — Google ส่งมอบให้ Linux Foundation, AWS/Microsoft/SAP/Salesforce/ServiceNow ทำ production: agent interop กลายเป็น "TCP/IP layer" ของยุค agentic ในไม่ถึง 12 เดือน

## TL;DR
- **Agent2Agent (A2A) protocol** ที่ Google ปล่อยปลายเม.ย. 2025 ตอนนี้ **มี 150+ องค์กร support, version 1.2 ใช้ production** (จาก ~50 ตอน launch ปีก่อน) — Linux Foundation Agentic AI Foundation governance
- AWS / Microsoft / Cisco / IBM / Salesforce / SAP / ServiceNow **ทุกตัว ship A2A native** แล้ว — "Salesforce Agentforce → Vertex agent → ServiceNow ITAM" คุยกันได้โดยไม่ต้องคุย API
- คู่กับ MCP (97M monthly SDK downloads, 10K+ public servers) = **two-protocol stack** ที่กำลังกลายเป็น default layer ของ enterprise agent — OpenBridge ต้องเลือก lane ภายใน 30 วัน

## เกิดอะไรขึ้น

วันที่ 22 เม.ย. ที่ Google Cloud Next 2026 ลาสเวกัส Mat Velloso ผู้นำ AI ของ Google Cloud ขึ้น keynote ประกาศตัวเลขที่หลายคนรอฟัง — **A2A protocol ครบ 12 เดือน, มี 150 องค์กร support, ผ่าน production deployment จริง ไม่ใช่ pilot อีกต่อไป**. วันเดียวกัน Linux Foundation ออก press release ผ่าน PRNewswire ยืนยันว่า "Agent2Agent Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year" — รายชื่อที่ปรากฏมี AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP, ServiceNow ครบ 8 hyperscaler/SaaS giant ที่ปกติไม่เคยเดินทางเดียวกัน.

ตัวเลขที่น่าตกใจคือ **scale ของการเดินทางจาก concept → production**. เมษายน 2025 A2A เปิดด้วย ~50 partner เป็น announcement-only — ส่วนใหญ่ logo slide ไม่มีคน implement จริง. ธันวาคม 2025 Google **donate protocol** ให้ Linux Foundation จัดตั้งเป็น Agentic AI Foundation (AAIF) ร่วมกับ Anthropic, Block, OpenAI — Google สละ unilateral control แลกกับ enterprise trust. ตอนนี้ **เมษา 2026 — version 1.2 มี cryptographic signed agent cards (DNS-based domain verification เหมือน HTTPS), production routing จริง**, native support ใน Google Agent Development Kit (Python/Go/Java/TypeScript stable v1.0), LangGraph, CrewAI, LlamaIndex Agents, Semantic Kernel, AutoGen.

ตัวอย่างที่ Velloso ขึ้น demo บนเวที — **Salesforce Agentforce agent** ที่อยู่ใน Salesforce cloud ส่งงาน inbound sales lead enrichment ไปยัง **Google Gemini Enterprise agent** ที่ทำ deep research ใน corporate data, แล้ว Gemini agent ส่งงานต่อไปยัง **ServiceNow agent** เพื่อตรวจ IT asset history ของ lead account, สุดท้าย ServiceNow ส่งกลับมาให้ Salesforce agent คุยกับ sales rep — **ทั้งหมดผ่าน A2A discovery + capability negotiation, ไม่มีการเขียน custom integration**, ใช้เวลา setup 4 นาทีจาก Workspace Studio (no-code agent builder ตัวใหม่ที่ Google เปิดวันเดียวกัน). Velloso ทิ้ง quote: "Five years from now, when an enterprise hires an AI agent, that agent shouldn't care which platform it lives on. A2A is the TCP/IP layer of the agentic era."

นอกจากนี้ Google เปิด **Workspace Studio** (no-code), **200+ models ใน Model Garden** (รวม Anthropic Claude — โผล่ใน competitor's catalog ครั้งแรก), **partner agents จาก Box/Workday/Salesforce/ServiceNow**, **managed MCP servers** + Apigee เป็น API-to-MCP bridge, และ **Project Mariner** (web-browsing autonomous agent) — รวมเป็น **full-stack agentic offensive** ที่ Google ใช้สู้กับ OpenAI Workspace Agents (Apr 22, 1 วันห่างกัน) และ Anthropic Claude Managed Agents (Apr 8). Cloud backlog ของ Google Cloud ตอนนี้แตะ **$240B** — สัญญาณว่าทุนเริ่มไหลเข้า Google Cloud หลังจาก AWS dominate มา 15 ปี.

## ทำไมสำคัญ

A2A เป็น **infrastructure decision ของยุค agentic** ที่ enterprise ส่วนใหญ่ยังประเมินไม่ทัน — และนี่คือเหตุผลว่าทำไม 150 องค์กรในเวลา 12 เดือนคือตัวเลขที่หนัก. เปรียบเทียบ — MCP ใช้เวลา **17 เดือนถึงจะแตะ 97M SDK downloads** หลังจาก Anthropic ปล่อย Nov 2024; HTTPS ใช้เวลา 3-4 ปีถึงจะกลายเป็น default; OAuth 2.0 ใช้เวลา 5 ปี. A2A ทำได้ใน 12 เดือน เพราะ Google เลือกเดินเกม **donate-first** (Linux Foundation governance ตั้งแต่เดือนที่ 8) แลกกับ enterprise adoption — pattern เดียวกับ Kubernetes ที่ Google donate ให้ CNCF ปี 2015 แล้ว 18 เดือนหลังจากนั้นกลายเป็น standard.

ที่สำคัญกว่าคือ **A2A + MCP form complementary stack** ที่กำลัง lock pattern. MCP (Anthropic-led, 97M downloads) แก้ปัญหา **agent-to-tool/data**; A2A (Google-led, 150 orgs production) แก้ปัญหา **agent-to-agent across platforms**. ผู้เล่นใหญ่ทุกคน—AWS, Microsoft, Google, Anthropic, OpenAI—ยอมรับสองโปรโตคอลนี้แล้ว ไม่มีสงคราม protocol ครั้งที่สอง (ต่างจากยุค SOAP vs REST). หมายความว่า **enterprise CIO ที่จะออกแบบ AI agent strategy ปี 2026-2027 ไม่ต้องเดิมพันโปรโตคอล** — เลือก stack ที่ ship A2A + MCP native, จบ. ผู้เล่น SaaS ที่ ship integration ผ่าน webhook/API custom จะถูก disrupt ภายใน 18-24 เดือน เหมือนที่ REST API เคย disrupt ผู้เล่น SOAP/RPC ปี 2010-2013.

ที่ยังเป็นคำถามคือ **economic capture** — Google ที่ donate protocol ออกไปจะกินส่วนแบ่งอย่างไร? คำตอบที่เริ่มเห็น: Google capture ผ่าน **distribution + observability** — Gemini Enterprise Agent Platform เป็น control plane ที่เห็น traffic A2A ทั้งหมดของ enterprise, billing $/agent-runtime-hour + telemetry. Anthropic ทำคล้ายกัน — Claude Managed Agents เก็บ 8 cents/agent-runtime-hour + $150-800/month minimums. **Real money อยู่ที่ control plane + telemetry layer ไม่ใช่ที่ protocol** — และนี่คือ slot ที่ OpenBridge ต้องตัดสินใจว่าจะแย่งเข้ามาเล่นหรือไม่.

## มุม OpenBridge

**Direct relevance สูงมาก** — A2A + MCP คือ **infrastructure layer ที่ OpenBridge ต้องอยู่ข้างบน ไม่ใช่ข้างใต้**. ถ้า OpenBridge ตำแหน่งตัวเองเป็น **"Thai SaaS A2A/MCP gateway"** = ตลาดเปิด, OpenBridge เป็นคนแปล Thai SaaS (FlowAccount, PEAK, K-Bank, LINE OA, Shopee Seller, Lazada Seller) เข้า A2A capability cards + MCP servers ที่ enterprise CIO Thai สามารถ plug-and-play เข้า Google Gemini Enterprise / Microsoft Copilot Studio / Salesforce Agentforce ได้ — pricing 50-200K บาท/เดือนต่อ vendor + transaction fee. ถ้า OpenBridge ไม่จับ slot นี้ — **Apigee + AWS API Gateway จะกินก่อน Q3 2026** (ทั้งคู่ขณะนี้ ship managed MCP + A2A bridge แล้ว แต่ยังไม่ผูก localized Thai SaaS).

Action 14 วัน: (1) implement A2A v1.2 spec บน OpenBridge core ทันที — มี Python SDK / Go SDK / TypeScript SDK พร้อมใช้, ไม่ต้อง R&D หนัก; (2) เปิด **OpenBridge A2A Catalog** ภายใน 30 วัน — list 5-7 Thai SaaS ที่ pre-built เป็น A2A agent card + MCP server, lock exclusivity 6 เดือน; (3) ออก reference architecture blog "OpenBridge บน A2A + MCP — Thai SaaS ที่ enterprise agent ของไทยใช้ได้ใน 5 นาที" เป็น credibility play สำหรับ CIO survey. **Window ปิดเมื่อ Apigee ออก Thai SaaS adapter pack** — น่าจะ 6-9 เดือน ดูจาก roadmap GCP Thailand ที่ Google เปิด data residency ที่ Bangkok ปลายปี 2025.

## Sources
- [A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year (Linux Foundation)](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
- [Google Cloud Next 2026: AI agents, A2A protocol, Workspace Studio, and the full-stack bet against OpenAI and Anthropic (TheNextWeb)](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era)
- [The new Gemini Enterprise: one platform for agent development (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development)
- [A2A Protocol Explained: How Google's Agent-to-Agent Standard Grew to 150+ Organizations in One Year (Stellagent)](https://stellagent.ai/insights/a2a-protocol-google-agent-to-agent)

---

## Audio script
ข่าว A2A protocol น่าสนใจมากนะ Yoh. Google เปิด protocol นี้ปีที่แล้วเมษายน 2025 ตอนนั้นมีแค่ 50 partner ส่วนใหญ่เป็น logo slide. ผ่านไป 12 เดือนพอดี วันที่ 22 เมษายน Cloud Next 2026 ที่ลาสเวกัส Google ประกาศว่า ตอนนี้ A2A มี 150 องค์กร support, version 1.2 ใช้ production จริงแล้ว ไม่ใช่ pilot. AWS, Microsoft, Salesforce, SAP, ServiceNow, IBM, Cisco — hyperscaler กับ SaaS giant 8 รายที่ปกติไม่เคยเดินทางเดียวกัน ตอนนี้ ship A2A native ทุกตัว. Google demo บนเวที — Salesforce Agentforce agent คุยกับ Gemini Enterprise agent คุยกับ ServiceNow agent เกี่ยวกับ sales lead enrichment ทั้งหมดผ่าน A2A discovery ไม่มี custom integration ใช้เวลา setup 4 นาทีบน Workspace Studio. ที่สำคัญคือ Google donate protocol ให้ Linux Foundation Agentic AI Foundation ตั้งแต่ธันวา 2025 — เลิก unilateral control เพื่อแลก enterprise trust pattern เดียวกับ Kubernetes. คู่กับ MCP ของ Anthropic ที่มี 97 ล้าน SDK downloads ตอนนี้ — กลายเป็น two-protocol stack ที่ enterprise ทุกคนยอมรับแล้ว. มุม OpenBridge คือ direct relevant เลย. A2A กับ MCP เป็น infrastructure layer ที่ OpenBridge ต้องอยู่ข้างบน ตำแหน่งตัวเองเป็น Thai SaaS A2A gateway — แปล FlowAccount, PEAK, K-Bank, LINE OA ให้ enterprise agent ของ Gemini, Copilot, Agentforce เรียกได้. ถ้าไม่จับช้า Apigee จะกินก่อน Q3. 30 วันต้อง implement A2A spec บน OpenBridge core, เปิด A2A Catalog 5-7 Thai SaaS, ออก reference blog. window ปิดเมื่อ Apigee ออก Thai adapter pack ประมาณ 6-9 เดือนข้างหน้า.
