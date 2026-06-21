---
date: 2026-06-21
slug: aws-summit-nyc-agentcore-quick-context
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of three glowing AWS-orange agent cube modules stacked
  vertically forming a tall control tower at the center — labeled "AgentCore"
  "Quick" "Context" from bottom to top. Around the tower, beams of light radiate
  outward to small generic enterprise app silhouettes (CRM, finance, dev tools)
  through a glowing gateway gate marked "MCP". Massive bold numerals "$200B"
  floating in the upper third with a smaller tag "39 regions" pinned beside it.
  Render style: cinematic editorial illustration, isometric perspective, warm
  AWS orange lighting radiating from tower to cool dark navy at the edges,
  high-contrast typography legible at 200px thumbnail. No real human faces.
image: images/26-06-22-0602-03-aws-summit-nyc-agentcore-quick-context.png
---

# AWS Summit NYC 2026 — Amazon เปิด Bedrock AgentCore + Quick + Context ส่งสัญญาณว่า "agent stack ของ enterprise" คือ stack ปิดของ hyperscaler ไม่ใช่ LLM lab

## TL;DR
- 17–18 มิ.ย. AWS Summit NYC: Swami Sivasubramanian ขึ้น keynote ในตำแหน่งใหม่ "VP of Agentic AI" — เปิด AgentCore expansion, **Amazon Quick** (agent + Apple Siri-like assistant), **AWS Context** (auto knowledge graph), Graviton5 GA สำหรับ agentic workload
- Bedrock AgentCore เพิ่ม Gateway ที่ทำหน้าที่เป็น **managed MCP server** — แปล REST API เป็น MCP-compatible tools อัตโนมัติ, integrate Bedrock Guardrails ตรวจ prompt injection + sensitive data exposure ทุก agent action
- AWS commit **$200B AI infrastructure across 39 global regions** — บวก Continuum (security vulnerability agent) และ Kiro Mobile (agentic coding บน iOS)

## เกิดอะไรขึ้น

17–18 มิถุนายน AWS จัด Summit ที่นิวยอร์ก — ครั้งแรกที่ Swami Sivasubramanian ขึ้น keynote ในตำแหน่งใหม่ "VP of Agentic AI" (เลื่อนจาก VP of Data & AI ในช่วง reorg เดือนก.พ.) signal นี้สำคัญเพราะ AWS reorg เป็นการเพิ่ม "agentic" เป็น org-level entity ก่อนใครใน hyperscaler ทั้งสามค่าย Microsoft + Google ยังไม่มีตำแหน่งเทียบเท่าใน org chart ระดับนี้

ของจริงในรอบนี้คือ **Bedrock AgentCore ขยาย** ตัว Gateway ที่อยู่ระหว่าง agent กับ external tool ทุกตัวกลายเป็น **managed MCP server** — เมื่อ agent ต้องเรียก REST API, Lambda function, หรือ service อื่น request จะวิ่งผ่าน Gateway ที่ "auto-translate REST APIs into MCP-compatible tools" + บังคับใช้ Cedar policy language สำหรับ authorization (Cedar เป็น open-source ของ AWS ที่ donate ให้ CNCF ไปแล้ว) ในมุม dev นี่คือ "เปลี่ยน REST API existing 1,000+ ตัวให้ agent เรียกได้แบบ standard เดียว ไม่ต้องเขียน adapter" Bedrock Guardrails ก็ถูก integrate เข้า AgentCore — ทุก action จะถูกตรวจ prompt injection + harmful content + sensitive data exposure อัตโนมัติ พร้อมจะรับ signal จาก Check Point, Zscaler, Rubrik, Netskope, SentinelOne เข้ามาเสริม (เปิดในไตรมาสหน้า)

Product ใหม่ที่ดังสุดในงานคือ **Amazon Quick** — agent ที่ "connects to everything you use, takes action on your behalf, and gets smarter with every interaction" Andy Jassy บอกว่า user ใช้ Quick ได้ตั้งแต่ "ขอคำตอบสั้นๆ" ไปจนถึง "ปล่อย Quick ทำงาน autonomous เป็นวันๆ" — ตัวอย่างที่ AWS โชว์คือ Quick agent ที่ดูแล Salesforce + Workday + JIRA + Slack ในชื่อ executive ผู้ใช้ ที่น่าจับตาคือ Quick ใช้ AgentCore Gateway เป็น runtime แปลว่า third-party developer ที่ build connector ผ่าน MCP จะถูกเรียกอัตโนมัติจาก Quick ของ enterprise customer

**AWS Context** เป็น service ใหม่อีกตัวที่สำคัญ — "automatically maps the relationships across your existing data into a knowledge graph and provides agentic search" แทน Bedrock Knowledge Bases เดิมที่ต้อง chunk + embed manual Context จะ scan data lake / RDS / S3 / DynamoDB ของลูกค้าและสร้าง knowledge graph + ontology อัตโนมัติ ให้ agent ใน org ใช้ query ผ่าน "agentic search" คือถาม natural language แล้วได้ structured answer พร้อม trace ว่ามาจาก source ไหน

นอกจากนี้: **Continuum** (security agent ที่ prioritize vulnerability ตาม business impact + prove ว่า exploitable หรือไม่ + drive fix อัตโนมัติ) เปิด gated preview, **Kiro Mobile** (agentic coding บน iOS) ปล่อย iOS app, **Graviton5** GA สำหรับ CPU-intensive agentic workload (claim 30% perf/watt ดีขึ้นเทียบ Graviton4), และ AWS commit **$200B AI infrastructure across 39 regions** ในรอบ 5 ปี

## ทำไมสำคัญ

AWS เพิ่งทำให้ **MCP เป็น "default integration protocol ของ enterprise cloud"** อย่างเป็นทางการ — เมื่อ Bedrock AgentCore Gateway แปล REST → MCP อัตโนมัติ และ Amazon Quick เรียกผ่าน Gateway แปลว่า enterprise ที่ใช้ AWS จะ default ไป MCP โดยที่ developer แทบไม่ต้องคิด ผสมกับที่ Salesforce รองรับ MCP เป็น GA วันที่ 15, Anthropic ที่ออกแบบ protocol นี้แต่ต้น, และ Microsoft ที่เพิ่งประกาศ MCP support ใน Copilot Studio April release — 4 ใน 5 enterprise platform ใหญ่ที่สุดในโลกใช้ MCP แล้ว Google ยังเหลือ A2A protocol ที่ตัวเองออกแบบ แต่ตัว Gemini ก็เริ่มรองรับ MCP ในเดือนพ.ค.

Amazon Quick เป็น product ที่ก้าวข้าม "chatbot" ไปสู่ **"long-running autonomous agent ที่ persist context ข้าม session ข้ามวัน"** — feature ที่ Anthropic เพิ่งเปิด Claude Cowork ในเดือนเม.ย. ตอนนี้ AWS ทำเป็น native ของ cloud ลูกค้าเพิ่ม implication ที่ใหญ่คือ user ของ enterprise ที่ใช้ AWS จะมี agent persistent ที่ทำงานต่อเนื่อง — ไม่ใช่แค่ ask-answer pattern แบบ ChatGPT แต่ pattern ที่ใกล้กับ "AI employee" มากขึ้น ส่งผลให้ workload ของ AWS ที่ measure ใน CPU-seconds จะเพิ่มขึ้นเร็วกว่า simple LLM call

ตำแหน่ง "VP of Agentic AI" ของ Swami เป็น org signal ที่ underestimated — AWS เพิ่งบอกว่า agentic ไม่ใช่ "feature ของ Bedrock" แต่เป็น **business unit ของ Amazon** ผลกระทบในระดับ planning คือทุก service ของ AWS ตั้งแต่ S3, Lambda, EC2 จะถูกออกแบบใหม่ให้รองรับ agent invocation pattern — pricing model ใหม่จะตามมาในรอบไตรมาส (มี hint แล้วใน FAQ ของ AgentCore ว่า "millisecond-level billing for active runtime, idle excluded")

## มุม OpenBridge

AWS เพิ่งทำให้ **OpenBridge มี moat ใหม่ที่ไม่เคยมี** — เมื่อ AgentCore Gateway แปล REST API → MCP ได้อัตโนมัติ คำถามคือ "ทำไมลูกค้าต้องใช้ OpenBridge" คำตอบไม่ใช่ "translation" แต่เป็น **multi-cloud + multi-tenant + cross-vendor governance** เพราะ AWS Gateway ทำให้ AWS-native API เป็น MCP ได้ แต่ไม่ทำให้ Salesforce + Microsoft + Stripe + Notion เป็น MCP ได้ทั้งหมด — OpenBridge คือ broker ที่ทำงานข้าม vendor ใน MCP layer เดียวกัน

AWS Context ที่สร้าง knowledge graph อัตโนมัติเป็น **เทคนิคที่ OpenBridge ต้อง study อย่างจริงจัง** — pattern ของการ scan source data + infer relationship + expose ผ่าน agentic search คือสิ่งที่ลูกค้า B2B ทุกรายต้องการ ถ้า OpenBridge สามารถทำ "connector + auto knowledge graph" ในตัวเดียว (เช่นเชื่อม Salesforce + HubSpot + Pipedrive แล้ว auto-infer ว่า "Account = Account = Company" ระหว่างระบบ) นี่คือ value prop ที่ AWS Context ทำได้แค่ใน AWS ecosystem แต่ OpenBridge ทำได้ข้าม cloud

สุดท้าย Amazon Quick ที่ทำตัวเป็น "AI employee" จะกดดันให้ **OpenBridge ต้อง design connector ให้รองรับ "long-running session"** — ไม่ใช่ stateless API call ที่ระบบเดิมรองรับ session อาจยาวเป็นชั่วโมงหรือเป็นวัน, มี context state ที่ต้อง persist, มี checkpoint ที่ resume ได้ ลูกค้า enterprise ที่ใช้ Quick จะคาดหวัง integration platform ทุกตัวรองรับ pattern นี้ — ใครรองรับก่อนได้ deal

## Sources
- [AWS Summit New York 2026: New AI agent innovations — About Amazon](https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents)
- [Top announcements of the AWS Summit in New York, 2026 — AWS Blog](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)
- [AWS Summit NYC: Major New Agentic AI and Bedrock Announcements — Archyde](https://www.archyde.com/aws-summit-nyc-major-new-agentic-ai-and-amazon-bedrock-announcements/)
- [Amazon unveils new AI agents — GeekWire](https://www.geekwire.com/2026/amazon-unveils-new-ai-agents-trying-to-thread-the-needle-between-autonomy-and-human-control/)
- [AWS Summit 2026: The Agent Announcements That Actually Matter — Mission Cloud](https://www.missioncloud.com/blog/aws-summit-2026-the-agent-announcements-that-actually-matter)

---

## Audio script
สวัสดีครับโยห์ AWS Summit New York เมื่อวานนี้ Amazon เปิดของใหญ่หลายตัวในวงการ agentic AI Swami Sivasubramanian ขึ้น keynote ในตำแหน่งใหม่ VP of Agentic AI ครั้งแรกในประวัติศาสตร์ AWS reorg เพิ่ม agentic เป็น business unit ของ Amazon ก่อนใครใน hyperscaler ทั้งสามค่าย ของหลักคือ Bedrock AgentCore Gateway ที่ทำหน้าที่เป็น managed MCP server แปล REST API เก่าทุกตัวเป็น MCP compatible tool อัตโนมัติ บังคับใช้ Cedar policy language สำหรับ authorization Bedrock Guardrails ตรวจ prompt injection ทุก action รวมกับ signal จาก Check Point Zscaler และอื่นๆ ในไตรมาสหน้า มี Amazon Quick ที่เป็น agent autonomous ระยะยาว ลูกค้าใช้ตั้งแต่ตอบสั้นๆ ไปจนถึงทำงานเป็นวัน AWS Context ที่ scan data lake แล้วสร้าง knowledge graph อัตโนมัติให้ agent ใช้ search Continuum agent ตรวจ security vulnerability prioritize ตาม business impact Kiro Mobile บน iOS Graviton5 GA สำหรับ agentic workload และ commit 200 พันล้านเหรียญลงทุน infrastructure ใน 39 region ทั่วโลก สำหรับ OpenBridge ข้อสรุปคือ MCP กลายเป็น default protocol ของ enterprise cloud อย่างเป็นทางการ Salesforce Anthropic Microsoft AWS รองรับครบแล้ว moat ของเราต้องเปลี่ยนจาก protocol translation ไปสู่ multi-cloud governance ข้าม vendor และต้อง design connector ให้รองรับ long-running session ไม่ใช่ stateless API call แบบเดิมครับ
