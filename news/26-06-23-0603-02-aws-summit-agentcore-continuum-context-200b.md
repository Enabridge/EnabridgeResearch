---
date: 2026-06-22
slug: aws-summit-agentcore-continuum-context-200b
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of three glowing AWS service shields hovering in a row
  above a Manhattan skyline silhouette — left shield labeled "AGENTCORE",
  middle "CONTINUUM", right "CONTEXT". Below the skyline, a large floating
  banner reads "$200B AI INFRA — 39 REGIONS". Tiny robot agent silhouettes
  walk on connecting paths between the shields, while a Graviton5 chip icon
  glows at the base. Render style: cinematic editorial illustration,
  isometric perspective, deep teal sky with AWS orange highlights and white
  data-flow lines, dramatic depth, high-contrast typography legible at 200px
  thumbnail. No real human faces — only robotic silhouettes.
image: images/26-06-23-0603-02-aws-summit-agentcore-continuum-context-200b.png
---

# AWS Summit NY 2026 — $200B AI infra + AgentCore Web Search + Continuum security agent + Context knowledge graph: AWS ฝัง agent ลึกที่สุดในระบบ enterprise

## TL;DR
- 17 มิ.ย. ที่ AWS Summit New York Swami Sivasubramanian (VP Agentic AI) ประกาศ AgentCore Web Search GA, AWS Continuum security agent (gated preview), AWS Context knowledge graph (coming soon), Kiro on iOS, Amazon Quick autonomous agents — พร้อม commitment $200B AI infrastructure ทั่ว 39 global regions
- Continuum เป็น security agent แบบใหม่ที่เริ่มใน "learn mode" แล้วได้ permission ทีละหมวด — pattern "graduated autonomy" ที่ AWS เลือกแทน full-auto agent
- Graviton5 GA สำหรับ CPU-intensive agentic workload + QuEra fault-tolerant quantum compute บน Braket ภายในปี 2028

## เกิดอะไรขึ้น

วันที่ 17 มิ.ย. 2026 ที่ AWS Summit New York Swami Sivasubramanian — ที่เพิ่งถูก promote ขึ้นเป็น VP of Agentic AI เมื่อต้นปี — ขึ้น keynote ประกาศ feature 5-6 ตัวที่รวมกันแล้วเป็น "agent platform" ที่สมบูรณ์ที่สุดของ hyperscaler ตอนนี้ ตัวที่สำคัญที่สุดคือ **AgentCore Web Search** ที่เปิด GA ทันที — agent บน Bedrock เรียก web search ที่ AWS managed ได้โดยตรง พร้อม citation, zero data egress ออกจาก secured environment ของลูกค้า แปลว่าบริษัทใน regulated industry (banking, healthcare, government) ใช้ search-grounded agent ได้โดยไม่ผิด data residency policy

**AWS Continuum** เป็น security agent ตัวแรกที่ AWS ปล่อยใน gated preview — ใช้ STRIDE threat modeling framework, รับ vulnerability finding ข้าม environment ลูกค้า, prioritize ตาม business impact, ประเมิน exploitability, แล้วผลัก fix ผ่าน workflow เดิม สิ่งที่น่าสนใจคือ design pattern: Continuum เริ่มใน "supervised learn mode" — agent ดูพฤติกรรม ลูกค้ายังต้อง approve ทุก action — แล้วลูกค้าค่อย ๆ grant permission หมวดต่อหมวด ("auto-fix CVE high-severity", "auto-rotate compromised secrets") AWS ตั้งใจชัดว่าไม่ pitch full-auto agent แต่ pitch "graduated autonomy"

**AWS Context** ยังเป็น coming soon — knowledge graph แบบ automatic ที่ map ความสัมพันธ์ของ data ทั่ว AWS (S3, RDS, DynamoDB, Lake Formation) แล้ว expose เป็น "agentic search" ที่ agent ที่อยู่ใน org เดียวกันใช้ navigate governed data ได้ runtime นี่คือคำตอบของ AWS ต่อ Databricks Genie + Snowflake Cortex — แต่ position ที่ infrastructure layer ไม่ใช่ data warehouse layer

**Kiro on iOS** เปิด gated preview — Kiro คือ coding agent ของ AWS (คล้าย Devin/Cursor agent) ตอนนี้มี native iOS app ให้ developer kick session, monitor progress, approve diff จากมือถือโดยไม่ต้องเปิด laptop **Amazon Quick** เป็น autonomous background agent ตัวใหม่ที่รวม email + messaging + calendar + tasks เข้า activity feed อันเดียว — pitch ตรงกับ Microsoft 365 Copilot

AWS ยังประกาศ **commitment $200B AI infrastructure ครอบคลุม 39 global regions, Graviton5 GA สำหรับ CPU-intensive agentic workload, และ partnership กับ QuEra Computing** ที่จะนำ fault-tolerant quantum compute เข้า Amazon Braket ภายในปี 2028

## ทำไมสำคัญ

ปี 2026 hyperscaler ทุกรายมี agent platform แต่ AWS เลือก strategy ต่างคนอื่นชัดเจน — Microsoft pitch "Agent 365 governance layer" ที่นั่ง above existing tools, Google pitch "Gemini agentic across Workspace + Vertex" ที่ใช้ vertical integration, AWS pitch "agentic primitives ที่ developer ประกอบเอง" — AgentCore + Context + Continuum คือ Lego blocks ไม่ใช่ packaged product Strategy นี้ตรงกับ DNA ของ AWS — ลูกค้าเลือก stack, AWS provide infra — แต่อาจช้ากว่า packaged play ของ Microsoft ในตลาด non-developer

Pattern **"graduated autonomy"** ของ Continuum เป็น product decision ที่น่าจับตา — ตรงข้ามกับ Cognition Devin หรือ Cursor Agent ที่ pitch "autonomous coding agent วันแรก" AWS เลือก position ที่ enterprise security team ฟังแล้ว buy ได้ — start in learn mode, earn trust ทีละ permission — pattern นี้จะเป็น default ของ enterprise agent deployment ในช่วง 12 เดือนข้างหน้า เพราะ regulator (EU AI Act, NIST AI RMF) บังคับให้ explainability + human-in-loop กลายเป็น requirement

**$200B infra commitment** ก็เป็น signal ว่า compute scarcity ยังไม่ผ่อนคลาย — Anthropic + OpenAI ต่างก็พึ่ง AWS เป็นส่วนหนึ่ง, ตอนนี้ AWS bet ว่า inference demand จะ outpace supply ไปอีก 24+ เดือน Graviton5 GA สำหรับ agentic workload คือการ commoditize CPU-side ของ agent runtime ที่ orchestrate tool call (ไม่ต้อง GPU ทุก step) — ถ้าทำได้จริง marginal cost ต่อ agent run จะลดลง 30-50% เปรียบเทียบกับ GPU-only stack

## มุม OpenBridge

AWS Context กับ OpenBridge อยู่ใน collision course — ทั้งสองตอบโจทย์เดียวกัน "agent ต้องการรู้ว่าข้อมูล/tool ไหนอยู่ที่ไหน" ต่างกันที่ scope: Context map ข้อมูลภายใน AWS account (S3 → RDS → Lake Formation), OpenBridge map ข้อมูล + tool ข้าม cloud + SaaS Strategy ของ OpenBridge ต้องตอบให้ชัด: เราเป็น "multi-cloud + SaaS-first integration fabric" ที่ AWS Context ทำไม่ได้ ลูกค้าที่ใช้ AWS + Salesforce + Azure AD จะเลือก OpenBridge เพราะ Context cover แค่ AWS

อีกประเด็นคือ **graduated autonomy pattern** ของ Continuum — OpenBridge ถ้า build agent-enabled integration ต้องใส่ feature นี้ตั้งแต่ design: workflow แต่ละ step ต้อง map ได้ว่า "auto-execute", "ask before exec", "log only" — และ admin ต้อง upgrade permission per category ได้ ไม่ใช่ all-or-nothing toggle นี่จะเป็น differentiator vs Zapier MCP ที่ยังเป็น all-or-nothing trigger

## Sources
- [Top announcements of the AWS Summit in New York, 2026 — AWS Blog](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)
- [AWS Summit New York 2026: New ways to make AI agents more effective at work — Amazon](https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents)
- [Amazon unveils new AI agents, trying to thread the needle between autonomy and human control — GeekWire](https://www.geekwire.com/2026/amazon-unveils-new-ai-agents-trying-to-thread-the-needle-between-autonomy-and-human-control/)
- [AWS Summit 2026: The Agent Announcements That Actually Matter — Mission Cloud](https://www.missioncloud.com/blog/aws-summit-2026-the-agent-announcements-that-actually-matter)
- [AWS NY Summit 2026: AgentCore, Continuum and Context — Digital Applied](https://www.digitalapplied.com/blog/aws-summit-ny-2026-agentcore-continuum-context-agents)

---

## Audio script
สวัสดีครับ Yoh วันที่ 17 มิถุนา AWS Summit New York Swami Sivasubramanian VP Agentic AI ขึ้น keynote ประกาศ feature สำคัญหลายตัวที่รวมกันเป็น agent platform ที่สมบูรณ์ที่สุดของ hyperscaler ตอนนี้ AgentCore Web Search เปิด GA ทันที agent บน Bedrock เรียก web search ที่ AWS managed ได้ พร้อม citation zero data egress เหมาะกับ banking healthcare government ที่มี data residency policy AWS Continuum เป็น security agent ตัวแรก ใช้ STRIDE framework แต่ที่น่าสนใจคือ design pattern Continuum เริ่มใน supervised learn mode ลูกค้า approve ทุก action ก่อน แล้วค่อย grant permission ทีละหมวด AWS pitch graduated autonomy ตรงข้ามกับ Devin หรือ Cursor ที่ pitch full-auto วันแรก AWS Context เป็น knowledge graph อัตโนมัติที่ map data ทั่ว AWS แล้วให้ agent navigate ได้ Kiro on iOS เปิด preview สำหรับ developer คุม agent จากมือถือ Amazon Quick autonomous agent รวม email messaging calendar tasks เข้า feed เดียว AWS ยัง commit 200 พันล้านดอลลาร์สำหรับ AI infrastructure 39 region Graviton5 GA สำหรับ agentic workload ทำไมสำคัญ AWS เลือก strategy ต่างคนอื่น Microsoft pitch governance layer Google pitch vertical integration AWS pitch primitives ให้ developer ประกอบเอง pattern graduated autonomy จะเป็น default ของ enterprise agent deployment 12 เดือนข้างหน้า เพราะ regulator บังคับ explainability และ human in loop สำหรับ OpenBridge AWS Context อยู่ใน collision course กับเรา ทั้งสองตอบโจทย์เดียวกัน agent ต้องการรู้ว่าข้อมูลและ tool อยู่ที่ไหน ต่างกันที่ scope OpenBridge ต้องชูจุดขาย multi cloud และ SaaS first ที่ AWS Context cover ไม่ได้ และต้องใส่ graduated autonomy เข้า design ตั้งแต่ต้นครับ
