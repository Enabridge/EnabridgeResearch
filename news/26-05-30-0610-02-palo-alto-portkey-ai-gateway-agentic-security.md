---
date: 2026-05-30
slug: palo-alto-portkey-ai-gateway-agentic-security
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial illustration of a colossal Palo Alto Networks orange shield
  swallowing a glowing Portkey gateway portal, with hundreds of tiny AI agent
  silhouettes streaming through the portal labeled "AI Gateway · 3,000+ LLMs".
  A bold white banner overhead reads "trillions of tokens/month". Below, smaller
  shields labeled "Prisma AIRS · MCP · A2A" form a fortress wall. Style:
  cinematic editorial illustration, dramatic backlighting, deep navy and bright
  Palo Alto orange palette, high contrast all text legible at 200px thumbnail.
  1:1 aspect ratio. No real human faces.
image: images/26-05-30-0610-02-palo-alto-portkey-ai-gateway-agentic-security.png
---

# Palo Alto Networks ปิดดีลซื้อ Portkey — AI gateway ที่จัดการ "trillions of tokens/month" กลายเป็น security stack หลักของ agentic enterprise

## TL;DR
- 29 พ.ค. Palo Alto Networks (PANW) ประกาศ "completed acquisition" ของ Portkey — AI gateway company จาก SF ที่ process trillions of tokens/month
- Portkey รองรับ 3,000+ LLMs + MCP tools, ทำ semantic routing, cost control, observability — กลายเป็น control plane ของ AI agent traffic
- ดีลนี้ anchor agentic security stack ของ PANW — Prisma AIRS + AI gateway + agent governance ทั้งหมดใน platform เดียว, ราคาดีลไม่เปิดเผย

## เกิดอะไรขึ้น

วันที่ 29 พ.ค. 2026 Palo Alto Networks ประกาศปิดดีลซื้อ Portkey อย่างเป็นทางการ — startup จาก San Francisco ที่ตั้งตัวเองเป็น "AI gateway" สำหรับ enterprise คล้าย Kong หรือ Apigee แต่สร้างมาเฉพาะสำหรับ AI traffic ราคาดีลไม่ได้เปิดเผยใน press release แต่ Palo Alto Networks ระบุว่าจะ integrate Portkey เป็นส่วนหนึ่งของ Prisma AIRS — AI security platform ของบริษัท

ตัวเลขที่ทำให้ดีลนี้น่าสนใจ — Portkey process **trillions of tokens per month** บน production traffic ของลูกค้า enterprise และรองรับ 3,000+ LLMs พร้อม MCP tools ผ่าน unified interface เดียว Portkey ทำ semantic routing (ส่ง request ไปยัง model ที่เหมาะกับงานนั้น), caching, granular quotas, observability และ cost control — feature pack ที่ enterprise ที่ deploy AI agent หลายร้อยตัวต้องการแต่ build เองไม่คุ้ม

CEO ของ Portkey เคยบอกว่า — "ทุกคนพูดเรื่อง AI agent แต่ไม่มีใครพูดเรื่อง bill ที่กำลังจะมา" Portkey ทำ centralized artifact management ที่ version, control access ทั้ง models, agents และ MCP servers — เปลี่ยน "fragmented AI experiments" ของ enterprise เป็น "disciplined global production engine" ที่ CFO มอง bill รวมได้ในที่เดียว

ดีลนี้คือส่วนหนึ่งของ pattern ที่ใหญ่กว่า — Palo Alto Networks เพิ่งซื้อ Protect AI เมื่อเดือนก่อน (สำหรับ AI security posture management) และดีล Portkey ทำให้ PANW มี stack ครบ ตั้งแต่ runtime protection, gateway, governance, observability ทั้งหมด CEO Nikesh Arora บอก analyst ว่า "agentic AI is the next attack surface" และ PANW จะลงทุนหนักในเส้นนี้เพื่อ position ตัวเองเป็น "agentic SOC" ของ enterprise

ในบริบทเดียวกัน — Snowflake ก็เพิ่ง acquire Natoma (MCP gateway) เมื่อวานนี้, Cloudflare ก็ ship MCP Server Portals ไปแล้ว, ตอนนี้ PANW มี Portkey — แสดงว่า **AI gateway category กำลังถูก consolidate เร็วมาก** ในวงรอบ 60 วันที่ผ่านมา

## ทำไมสำคัญ

ประเด็นหลักคือ — **agentic AI gateway กำลังกลายเป็น category เดียวกับ API gateway ใน era 2010s** ตอนนั้น Kong, Apigee (Google ซื้อ $625M ปี 2016), MuleSoft (Salesforce $6.5B ปี 2018) เป็น must-have สำหรับ enterprise ที่จะรัน microservices ผลตอนนั้นคือ M&A wave ที่ทำให้ category นี้ consolidate ภายใน 3 ปี ตอนนี้เรากำลังเห็น replay เดียวกัน — Portkey ถูกซื้อโดย PANW, Natoma ถูกซื้อโดย Snowflake, OpenRouter ยังอยู่อิสระแต่ราคาก็ขึ้นเรื่อย ๆ

ตัวเลข "trillions of tokens/month" ของ Portkey สำคัญเพราะมันบอกว่า — agentic workload ใน production เริ่ม consume volume ที่ใกล้เคียงกับ web traffic ของ medium SaaS แล้ว ที่ benchmark ปี 2024 ระดับนี้ระดับ "billions" ไม่ใช่ "trillions" หมายความว่า AI inference cost ของ enterprise โดยรวมโตเร็วกว่า web hosting cost ใน 10 ปีแรกของ cloud era — ทำให้ "AI cost governance" จะกลายเป็นปัญหา CFO ที่ใหญ่กว่า "cloud cost governance" ของยุคปัจจุบัน

Pattern ที่อันตรายคือ — Palo Alto Networks มี enterprise distribution ที่ massive แล้ว (Fortune 1000 ใช้ Prisma หรือ Cortex อยู่แล้ว) การที่ AI gateway capability กลายเป็น "feature ฟรีของ security platform" จะทำให้ standalone AI gateway startup ไม่มี oxygen — โอกาสที่ Portkey-like ตัวอื่นจะ raise round ใหญ่ในอีก 6 เดือนข้างหน้าน่าจะลดลงเร็ว

## มุม OpenBridge

OpenBridge ต้อง take away จากดีลนี้ 3 เรื่อง — **หนึ่ง** AI gateway category กำลังจะ consolidate เข้า security vendor + data vendor (Snowflake, PANW, ในอนาคต Databricks หรือ CrowdStrike) ถ้า OpenBridge มองตัวเองเป็น gateway/governance layer จะแข่งยาก ทางที่ดีกว่าคือ position เป็น "workflow orchestration layer ที่ใช้ gateway ของ vendor ใดก็ได้" — เป็น customer ของ Portkey/Natoma ไม่ใช่ competitor

**สอง** — ตัวเลข trillions of tokens บอกว่าตลาด AI cost optimization (caching, semantic routing, model fallback) จะเป็น $10B+ TAM ใน 3 ปี OpenBridge ที่มี workflow telemetry สามารถ surface "ที่ไหนใช้ token เยอะ, ที่ไหนถูก over-engineered" — เป็น value add ที่ workflow vendor มีแต่ gateway vendor ไม่มี (เพราะ gateway เห็นแค่ raw traffic ไม่เห็น business context)

**สาม** — PANW positioning agentic AI เป็น "next attack surface" คือ signal สำหรับ APAC market ที่มี security-paranoid regulator (Singapore MAS, Bank of Thailand, Hong Kong HKMA) — OpenBridge ที่ message ว่า "agentic workflow with security-first design" จะ resonate กับลูกค้า financial services ใน APAC ที่กำลัง start adopt agentic AI แต่ยังกลัว risk

## Sources
- [Palo Alto Networks Completes Acquisition of Portkey to Secure AI Agents — Palo Alto Networks](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents)
- [Palo Alto Networks: Portkey Acquisition Anchors its Agentic Security Stack — NAND Research](https://nand-research.com/palo-alto-networks-portkey-acquisition-anchors-its-agentic-security-stack/)
- [Palo Alto Networks Portkey Deal Highlights AI Security And Valuation Story — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/palo-alto-networks-portkey-deal-200727779.html)
- [Securing and Governing AI Agents At Scale Through A Unified AI Gateway — Palo Alto Networks blog](https://www.paloaltonetworks.com/blog/2026/04/securing-and-governing-ai-agents-at-scale-through-a-unified-ai-gateway/)

---

## Audio script
ข่าวที่สองคือ Palo Alto Networks ปิดดีลซื้อ Portkey อย่างเป็นทางการเมื่อวันที่ 29 พฤษภาคม Portkey เป็น AI gateway startup จาก San Francisco ที่ process trillions of tokens ต่อเดือน รองรับ 3,000 LLMs บวก MCP tools ผ่าน unified interface ทำ semantic routing caching cost control และ observability ราคาดีลไม่เปิดเผย Palo Alto Networks จะ integrate Portkey เข้า Prisma AIRS เป็น security platform หลัก CEO Nikesh Arora บอก analyst ว่า agentic AI คือ next attack surface ของ enterprise pattern ที่เห็นชัดคือ AI gateway category กำลังจะถูก consolidate เข้า security และ data vendor ภายใน 60 วันมี Snowflake ซื้อ Natoma Cloudflare ship MCP Server Portals และ Palo Alto Networks ซื้อ Portkey กำลังจะเป็น replay ของ API gateway category ใน era 2010s ที่ Apigee MuleSoft ถูก consolidate ภายใน 3 ปี ตัวเลข trillions of tokens ต่อเดือนสำคัญเพราะมันโตเร็วกว่า web traffic ของ medium SaaS แล้ว AI cost governance จะกลายเป็นปัญหา CFO ใหญ่กว่า cloud cost governance ของยุคปัจจุบัน สำหรับ OpenBridge ต้องไม่แข่งที่ generic gateway แต่ position เป็น workflow orchestration layer ที่ใช้ gateway ของ vendor ใดก็ได้ และ message ว่า security-first agentic workflow จะ resonate กับลูกค้า APAC financial services ที่กำลัง start adopt agentic AI ครับ
