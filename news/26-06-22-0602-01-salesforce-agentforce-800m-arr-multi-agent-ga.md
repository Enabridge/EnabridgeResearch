---
date: 2026-06-21
slug: salesforce-agentforce-800m-arr-multi-agent-ga
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a single glowing Salesforce-cloud-shaped orchestrator
  agent at center, dispatching beams of light to four smaller specialist subagent
  silhouettes arranged around it like a constellation. Massive bold numerals
  "$800M ARR" and "169% YoY" floating in the upper third, with a smaller tag
  "Agentforce Summer '26" pinned near the central cloud. Render style: cinematic
  editorial illustration, isometric perspective, warm Salesforce blue lighting
  radiating from center to deep navy at the edges, high-contrast typography
  legible at 200px thumbnail. No real human faces — robotic silhouettes only.
image: images/26-06-22-0602-01-salesforce-agentforce-800m-arr-multi-agent-ga.png
---

# Salesforce Agentforce ทะลุ $800M ARR ใน 18 เดือน — Multi-Agent Orchestration GA พร้อม MCP support บอกว่า "agent platform war" จบรอบแรกแล้ว

## TL;DR
- Salesforce รายงาน Agentforce ARR $800M เพิ่ม **169% YoY** ทำดีลใหม่ 29,000 รายในปีที่ผ่านมา (Q4 เพียวๆ +50% QoQ), ลูกค้า 18,500 รายใน 124 ประเทศ — Benioff เรียก "fastest growing product ever" ของ Salesforce
- Summer '26 release (15 มิ.ย.) ปล่อย Multi-Agent Orchestration ขึ้น GA — Atlas Reasoning Engine 3.0 ใช้ "agent description" เป็น routing input แทน hardcoded workflow, รองรับ A2A protocol + MCP สำหรับ external tools
- ระบบ logged 2.4 พันล้าน agentic work units รวม Agentforce + Slack ตั้งแต่ launch — เป็น first-party benchmark ที่ enterprise customer ใช้เป็นเหตุผลเพิ่ม seat

## เกิดอะไรขึ้น

15 มิถุนายน Salesforce ปล่อย Summer '26 release พร้อมรายงานตัวเลขที่ทำให้ทุก enterprise software CEO หยุดอ่าน — Agentforce ARR แตะ **$800M** ขึ้น 169% เทียบ year-ago และเป็น product ที่โตเร็วที่สุดในประวัติศาสตร์บริษัทตามคำพูด Marc Benioff รวม AI revenue ทั้งหมด (Agentforce + Data Cloud + Einstein) เกิน $2.9B ใน annualized run rate วันเดียวกัน ดีลใหม่ Q4 +50% QoQ แตะ 29,000 ดีลใหม่ในรอบปี และฐานลูกค้า 18,500 รายใน 124 ประเทศ — ตัวเลขที่ปีก่อนคงจินตนาการไม่ออก

ของจริงที่ทำให้ Summer '26 เป็น release ที่สำคัญที่สุดในยุค Agentforce คือ **Multi-Agent Orchestration ขึ้น GA** ขับเคลื่อนด้วย Atlas Reasoning Engine 3.0 — pattern ใหม่คือ orchestrator agent รับ request, scan registry หา subagent ที่ register ไว้, อ่าน description + available actions, แล้ว route งานแบบ runtime ไม่ใช่ hardcode workflow เหมือนก่อน นั่นทำให้ "agent description" กลายเป็น **load-bearing infrastructure** ไม่ใช่ documentation สำหรับมนุษย์อ่านอีกต่อไป Atlas อ่านจริง routing real-time ตาม description ที่ admin เขียน

Salesforce เปิด multi-protocol stack เต็มสูบในรอบนี้: รองรับ **Google A2A (Agent-to-Agent) protocol** สำหรับสื่อสารกับ agent นอกระบบ, รองรับ **Anthropic MCP** สำหรับเชื่อม external tool และเปิด Tableau MCP server พร้อมใช้ทันที — แปลว่า agent ที่สร้างใน Agentforce สามารถ "ออกไปทำงานกับเครื่องมือนอก Salesforce ecosystem ได้ทันทีโดยไม่ต้อง custom integration" ในเชิง architecture นี่คือ acknowledgement ของ Salesforce ว่า "ปิด stack เองทำเองทั้งหมด ไม่เวิร์คใน agentic era" ต่างจาก strategy เดิมที่อยากให้ลูกค้าอยู่ใน Salesforce cloud เป็นหลัก

2.4 พันล้าน agentic work units ที่ logged รวมทั้ง Agentforce และ Slack เป็น metric ใหม่ที่ Salesforce ใช้แทน "conversation count" หรือ "ticket resolved" — มันรวมทุก action ที่ agent ทำในชื่อ user แต่ละ unit คือ task discrete ตั้งแต่ retrieve record, draft email, ไปจนถึง execute workflow ตัวเลข 2.4B เป็น first-party data ที่ enterprise procurement ใช้เป็น justification เพิ่ม license seat ในรอบ renewal ครั้งต่อไป

## ทำไมสำคัญ

$800M ARR ใน 18 เดือนคือ **the fastest enterprise software growth run in recent history** — Cognition Devin ที่ $492M, Microsoft Copilot Studio ที่ 120K+ องค์กร, Notion AI ที่ไม่เปิดเผยตัวเลข ไม่มีใครเจ้าโตเร็วกว่านี้ในรอบล่าสุด pattern คือ enterprise CRM ที่เป็น "system of record" สำคัญกว่า standalone agent platform เพราะ agent ทำงานได้ดีก็ต่อเมื่อมี context จากธุรกิจจริง — Salesforce ครอบครอง context นั้นอยู่แล้ว ทำให้การ retrofit agent layer ลงไปเป็น expansion play ที่กดดัน standalone agent vendor ทุกตัว

Multi-Agent Orchestration ขึ้น GA พร้อม MCP + A2A ส่ง signal ชัดว่า **"agent orchestration layer" กำลัง commoditize เร็วกว่าที่คาด** เมื่อปีที่แล้วทุกคนพูดว่า orchestration คือ moat ของ startup รายใหม่ ตอนนี้ Anthropic build เข้า Claude Code (1,000 subagents), AWS build เป็น AgentCore Gateway, และ Salesforce build เป็น Atlas 3.0 — ทั้งสามรายใหญ่ ship feature เหมือนกันในไตรมาสเดียว Cognition, Cursor, Lindy, และ orchestration startup รายอื่นๆ ต้องตอบโจทย์ใหม่: differentiation คืออะไรเมื่อ orchestration ไม่ใช่ value prop อีกต่อไป

Atlas Reasoning Engine 3.0 ที่อ่าน agent description เพื่อ route runtime คือ **inverse Conway** ของ workflow design — แทนที่ business analyst จะ map decision tree, admin เขียนคำบรรยายว่า "agent นี้ทำอะไร" แล้ว LLM จัดสายงานเอง implication คือทักษะใหม่ของ Salesforce admin ปี 2026 ไม่ใช่ Flow Designer แต่เป็น **"prompt engineering for agent registry"** — agent description ที่ดีจะกำหนดคุณภาพระบบ ตัวอย่างที่ Salesforce ยกใน docs คืออธิบาย "Sales Discount Agent" ในประโยคเดียวสั้นๆ จะ route ผิดบ่อย แต่อธิบายมี boundary clear ("approve discounts < 15% with manager auto-notify") routing แม่นยำขึ้นมาก

## มุม OpenBridge

Salesforce รองรับ MCP + A2A เป็น GA แปลว่า **MCP กลายเป็น default protocol ของ enterprise agent** อย่างเป็นทางการ — ก่อนหน้านี้ Anthropic, OpenAI, Google, AWS รองรับ ตอนนี้ Salesforce ที่มี 18,500 enterprise customer ก็รองรับด้วย OpenBridge ต้อง position ตัวเองเป็น **MCP server registry + governance layer** สำหรับ enterprise ที่มี agent ทั้งจาก Agentforce + Microsoft Copilot + Claude + internal ใช้พร้อมกัน — ความเจ็บปวดจริงของลูกค้าคือ "ฉันมี MCP server 30 ตัวจาก 8 vendor, ใครเปลี่ยน version ใครต้องอัพเดต permission ใครเห็น log ตอนผิด" OpenBridge คือคำตอบ

Agent description = routing input เป็น insight สำคัญสำหรับ B2B automation tool — OpenBridge connector แต่ละตัวควรมี **machine-readable description** ที่ดี ไม่ใช่แค่ human readable เพราะ orchestrator agent ของลูกค้าจะอ่านเอง decide ว่าจะเรียก connector ไหน ถ้า description กำกวม connector จะถูกเรียกผิด หรือไม่ถูกเรียกเลย ทีม product OpenBridge ควรทดสอบ description ของแต่ละ connector ผ่าน Atlas 3.0 + Claude orchestrator + Bedrock AgentCore ว่า route ถูกหรือไม่

2.4B work units ใน Agentforce + Slack คือ traffic pattern ที่ทุก integration platform ต้องเตรียมรับ — ลูกค้า enterprise ที่ใช้ Agentforce รุ่น Summer '26 จะ generate API call ผ่าน connector มากกว่าเดิมหลายเท่า เพราะ subagent แต่ละตัวเรียก tool หลายรอบใน 1 session OpenBridge ต้อง stress-test rate limit + caching layer ให้รองรับ traffic แบบ "agent-driven burst" ไม่ใช่ "human-driven steady"

## Sources
- [Salesforce Summer '26 Release Announcement](https://www.salesforce.com/news/stories/summer-2026-product-release-announcement/)
- [Agentforce Reaches $800M ARR as Multi-Agent Era Begins — Enterprise DNA](https://enterprisedna.co/resources/news/salesforce-summer-26-agentforce-800m-arr-multi-agent-2026/)
- [Salesforce Summer '26 Atlas 3.0, A2A, MCP — ChatForest](https://chatforest.com/builders-log/salesforce-summer-26-agentforce-multi-agent-orchestration-atlas-a2a-mcp-builder-guide/)
- [Salesforce Agentforce Multi-Agent Orchestration Hits GA — TechTimes](https://www.techtimes.com/articles/318456/20260616/salesforce-agentforce-multi-agent-orchestration-hits-ga-agent-descriptions-now-drive-reliability.htm)
- [Salesforce Announces Summer '26 (June 2026): Tableau Gets MCP — ACTGSYS](https://actgsys.com/en/blog/salesforce-agentforce-summer-26-multi-agent-sme-2026-06)

---

## Audio script
สวัสดีครับโยห์ วันนี้ข่าวใหญ่จาก Salesforce ครับ Agentforce ของเขาโตทะลุ 800 ล้านเหรียญ ARR ขึ้น 169% เทียบปีก่อน Benioff บอกว่าเป็น product ที่โตเร็วที่สุดในประวัติศาสตร์บริษัท เพิ่มดีลใหม่ 29,000 รายในปีที่ผ่านมา ลูกค้า 18,500 รายใน 124 ประเทศ ตัวเลขที่ปีก่อนคงไม่มีใครเชื่อ และในวันเดียวกัน Summer 26 release ก็ปล่อย Multi-Agent Orchestration ขึ้น GA Atlas Reasoning Engine version 3 ตัวใหม่ใช้ agent description เป็น input ในการ route งาน real-time แทน hardcode workflow แปลว่าทักษะใหม่ของ Salesforce admin ปี 2026 คือเขียน description ที่ดี ไม่ใช่ออกแบบ flow ที่สำคัญที่สุดสำหรับเราคือ Salesforce รองรับทั้ง MCP ของ Anthropic และ A2A protocol ของ Google เปิด Tableau MCP server พร้อมใช้ทันที นี่คือ acknowledgement ใหญ่ว่ายุค "ปิด stack เองทำเอง" จบแล้ว สำหรับ OpenBridge มีสองมุม หนึ่ง MCP กลายเป็น default protocol ของ enterprise agent อย่างเป็นทางการ เราต้อง position ตัวเองเป็น MCP server registry และ governance layer สอง connector ของเราทุกตัวต้องมี machine-readable description ที่ดี เพราะ orchestrator agent จะอ่านเอง decide ว่าจะเรียกอะไร description กำกวม connector ถูกเรียกผิด หรือไม่ถูกเรียกเลยครับ
