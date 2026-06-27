---
date: 2026-06-02
slug: microsoft-acs-agent-governance-open-standard
topic: agentic-ai
reading_time_min: 3
sources: 2
image_prompt: |
  Editorial illustration of a glowing translucent policy shield wrapped around
  a cluster of agent figures from multiple frameworks (each labeled: LANGCHAIN,
  OPENAI, ANTHROPIC, CREWAI, AUTOGEN, MCP), positioned in a circular formation.
  At each agent's "boundary" — before input, before tool call, after tool
  result, before user response — small floating gate icons glow with options
  ALLOW / BLOCK / REDACT / HUMAN APPROVAL. Large floating text "ACS" pins
  prominently above the cluster. Render style: cinematic editorial
  illustration, isometric perspective, cool blue policy shield contrasting
  warm amber agent glow, dramatic depth, high contrast typography legible at
  200px thumbnail. No real human faces — only robotic silhouettes.
image: images/26-06-28-0602-03-microsoft-acs-agent-governance-open-standard.png
---

# Microsoft Agent Control Specification (ACS) — open standard ตัวแรกที่ govern agent behavior ข้าม LangChain / OpenAI / Anthropic / CrewAI / AutoGen / MCP

## TL;DR
- 2 มิ.ย. Microsoft เปิด open-source spec **Agent Control Specification (ACS)** — portable policy file ที่ define ได้ว่า agent ทำอะไรได้บ้าง ต้อง require human approval เมื่อไหร่ ต้อง log อะไร
- บังคับใช้ที่ 4 จุดสำคัญ: before input, before tool call, after tool result, before user response — action ทำได้ allow / block / redact / require human approval
- SDK plugins ออกพร้อมกัน 8 frameworks: LangChain, OpenAI Agents SDK, Anthropic Agents SDK, AutoGen, CrewAI, Semantic Kernel, Microsoft.Extensions.AI, MCP tools

## เกิดอะไรขึ้น

วันที่ 2 มิ.ย. 2026 Microsoft ประกาศ Agent Control Specification (ACS) เป็น open-source standard สำหรับให้ developer, compliance team, security team define policy ที่ AI agent ต้อง follow Microsoft ระบุว่าปัจจุบัน developer "อาจ specify instruction ใน system prompt เพิ่ม custom check ใน application code หรือใช้ classifier ดัก problematic input/output" — ACS ออกแบบมา consolidate fragmentation นั้นให้เป็น unified governance layer ที่ทำงาน consistent ข้าม framework

Spec บังคับใช้ที่ 4 control point ของ agent workflow: **(1) before input reception** (กรอง input ก่อน agent รับ), **(2) before tool call** (อนุญาต/ปฏิเสธ tool invocation), **(3) after tool result** (ตรวจ/redact ผลลัพธ์ก่อนกลับเข้า model), **(4) before user response** (กรอง output สุดท้าย) ทุกจุด policy เลือก action ได้ 4 แบบ: allow / block / redact information / require human approval — policy file portable ข้าม environment

ที่สำคัญที่สุดคือ **adoption breadth ของ SDK plugins ใน launch day** — มี 8 frameworks: LangChain (open-source orchestration ที่นิยมที่สุด), OpenAI Agents SDK (ที่ Anthropic แข่งโดยตรง), Anthropic Agents SDK, AutoGen (Microsoft Research), CrewAI (multi-agent framework), Semantic Kernel (Microsoft .NET), Microsoft.Extensions.AI, และ MCP tools (รวมทั้ง ecosystem ของ MCP server) Microsoft ดึงทั้ง Anthropic และ OpenAI เข้า launch — pattern ที่หาได้ยากในตลาด AI ที่แข่งกันดุเดือด แสดงว่า governance เป็น problem ใหญ่พอที่ทำให้ rival vendor ตกลงร่วมมือ

## ทำไมสำคัญ

ACS เป็น signal ว่า **agent governance กำลังจะเป็น commodity layer** — ไม่ใช่ feature ที่ vendor แข่งกันสร้างเอง Microsoft ตัดสินใจ open-source เพราะ governance fragmentation เป็น blocker ที่ทำให้ enterprise ลังเลที่จะ deploy agent ที่ scale (กลัวว่า policy ที่เขียนสำหรับ framework หนึ่ง จะไม่ portable ไปอีก framework) ACS แก้ที่ root cause: policy เขียนครั้งเดียวใช้ได้ทุก framework ที่ enterprise ใช้อยู่ — pattern เดียวกับ Kubernetes ที่ commoditize "container orchestration" เมื่อ 10 ปีก่อน

ทำไม Anthropic + OpenAI ยอมร่วม? เพราะ **ทั้งคู่กลัว fragmentation มากกว่ากลัวกัน** — ถ้า enterprise ติด lock-in กับ governance layer ของ Microsoft, Anthropic/OpenAI จะถูก distort พฤติกรรมของ enterprise customer มากกว่าที่ open standard จะ distort ทั้งคู่จึงเลือก ship plugin วันแรกแทนที่จะ wait-and-see นี่เป็น pattern ที่บอกว่า "governance layer ที่ open + neutral" จะชนะ — ตรงกันข้ามกับ orchestration layer ที่ Anthropic/OpenAI กำลัง build เข้า model เอง (commoditize ด้วยการดูดเข้า) ใน governance, Microsoft commoditize ด้วยการ open spec

ตัวเลขที่ context นี้สำคัญ — รายงานเดียวกันระบุว่า Claude Code มี developer adoption 97% แต่ governance coverage แค่ 33% ช่องว่าง 64 จุดนี้คือ TAM ของ ACS และ tool ที่จะ implement spec นี้ — agent ถูก deploy เร็วกว่า security/compliance team จะตามทัน ACS ถูก timing พอดี

## มุม OpenBridge

ACS เป็น tailwind สำหรับ OpenBridge — เพราะ governance layer ที่ neutral, multi-vendor, MCP-compatible คือ position ที่ตรงกับ ACS spec **OpenBridge ควร ship ACS support เป็น day-1 feature** ใน MCP gateway ของตัวเอง — มี policy editor, policy versioning, audit log ที่ output เป็น ACS format ลูกค้า enterprise ที่เขียน policy ครั้งเดียว ใช้ได้ทุก agent framework ที่ deploy บน OpenBridge นี่เป็น differentiation ที่ classical iPaaS (Zapier/Workato/Boomi) ไม่มี

ที่ลึกกว่านั้น — ACS เปิดทาง business model "policy-as-a-service" ที่ OpenBridge ขายได้: pre-built compliance pack สำหรับ vertical สำคัญ (financial services SOX/GLBA, healthcare HIPAA, EU GDPR/AI Act, government FedRAMP) policy เขียนถูกต้องครั้งเดียว recurring revenue ต่อ deployment ลูกค้าไม่ต้องจ้าง consultant compliance ราคา $500K+ ต่อ project ใช้ OpenBridge policy pack ที่ $50K/year แทน margins ดี และ moat อยู่ที่ vertical expertise — เรื่องที่ Cloudflare/OpenRouter ที่เป็น horizontal infrastructure ทำตามได้ยาก

## Sources
- [Microsoft offers devs a better way to control AI agent behavior — TechCrunch](https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/)
- [Agent Control Specification (ACS) — open standard for governing AI agent actions](https://github.com/microsoft/agent-control-specification)

---

## Audio script
สวัสดีครับ Yoh เมื่อต้นเดือน Microsoft ปล่อย open-source spec ที่น่าสนใจชื่อ Agent Control Specification หรือ ACS เป็น portable policy file ที่ define ได้ว่า AI agent ทำอะไรได้บ้าง ต้อง require human approval เมื่อไหร่ ต้อง log อะไร บังคับใช้ที่ 4 จุดของ agent workflow คือ ก่อน input ก่อน tool call หลัง tool result และก่อน user response ทุกจุด policy เลือก action ได้ 4 แบบ allow block redact หรือ require human approval ที่สำคัญที่สุดคือ Microsoft เปิดตัวพร้อม SDK plugin 8 framework รวมทั้ง LangChain, OpenAI Agents SDK, Anthropic Agents SDK, AutoGen, CrewAI, Semantic Kernel และ MCP tools ดึงทั้ง Anthropic และ OpenAI เข้า launch ในวันเดียว pattern ที่หาได้ยากในตลาดที่แข่งกันดุเดือด สาเหตุที่ rival vendor ยอมร่วมมือคือ governance fragmentation เป็น blocker ที่ทำให้ enterprise ลังเลที่จะ deploy agent ที่ scale ทั้งคู่กลัว fragmentation มากกว่ากลัวกัน ตัวเลขที่ context นี้สำคัญ Claude Code มี developer adoption 97% แต่ governance coverage แค่ 33% ช่องว่าง 64 จุดนี้คือ TAM ของ ACS สำหรับ OpenBridge นี่เป็น tailwind ที่ใหญ่ ควร ship ACS support เป็น day-1 feature ของ MCP gateway มี policy editor, versioning, audit log ที่ output เป็น ACS format และเปิดทาง business model policy-as-a-service ขาย pre-built compliance pack สำหรับ vertical สำคัญ financial, healthcare, government margins ดี moat อยู่ที่ vertical expertise ที่ Cloudflare กับ OpenRouter ตามได้ยากครับ
