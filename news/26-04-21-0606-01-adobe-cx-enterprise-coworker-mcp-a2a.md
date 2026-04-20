---
date: 2026-04-21
slug: adobe-cx-enterprise-coworker-mcp-a2a
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: Editorial illustration of a central orchestrator figure weaving luminous threads outward to a ring of smaller worker silhouettes that become nodes on a network, minimal flat geometric shapes, muted navy and amber palette, soft gradient background, dramatic rim lighting, no text no logos no faces
image:
---

# Adobe เปิด "CX Enterprise Coworker" ที่ Summit — Experience Cloud โดนรีแบรนด์ทั้ง stack, วาง MCP + A2A เป็นมาตรฐานกลาง, พาร์ทเนอร์กับ AWS/Anthropic/Google/Microsoft/OpenAI/NVIDIA พร้อมกัน

## TL;DR
- วันนี้ (20 เม.ย. เปิด Summit) Adobe ทิ้งชื่อ "Experience Cloud" ที่ใช้มา 15 ปี รีแบรนด์เป็น **CX Enterprise** — ชูธง agentic AI เป็นศูนย์กลางของ marketing stack
- Launchhead คือ **CX Enterprise Coworker** — super-agent ที่ orchestrate agent อื่น decompose goal เป็น multi-step plan มี guardrail + scope ของ expertise; built บน **MCP + A2A** เป็น open standard
- Adobe Marketing Agent ถูก embed เข้าไปใน **Amazon Quick, Anthropic Claude Enterprise, ChatGPT Enterprise, Gemini Enterprise, IBM watsonx Orchestrate, Microsoft 365 Copilot** — surface เดียวอยู่ทุกที่
- Partnership พร้อม **NVIDIA OpenShell secure runtime + Nemotron models** สำหรับ regulated industry — "governed agents" เป็น pitch หลักตอนนี้ ไม่ใช่ capability

## เกิดอะไรขึ้น

วันจันทร์เช้าที่ Vegas, Shantanu Narayen เปิด Adobe Summit 2026 ด้วยการ **ฆ่าชื่อ "Experience Cloud"** — brand ที่ Adobe ใช้มาตั้งแต่ซื้อ Omniture ปี 2009 — แล้วแทนด้วย **"CX Enterprise"**. คนที่ไม่ได้ดูใกล้ ๆ อาจคิดว่าเป็นแค่ rebrand marketing ธรรมดา แต่ถ้าอ่าน press release ของ Adobe ทั้งห้าหน้าต่อเนื่องจะเห็นว่ามัน **คือการ re-platform marketing tech stack ทั้งเล่ม** รอบแกน agentic AI

ตัวเด่นคือ **CX Enterprise Coworker** — Adobe ไม่ได้ pitch ว่าเป็น "AI assistant" หรือ "chatbot" แต่เรียกมันว่า **super-agent ที่ orchestrate agent อื่น**. Anjul Bhambhri (SVP Adobe) อธิบายตอนเปิดตัวว่า Coworker สามารถ "decompose goal เป็น multi-step plan, มี permission + guardrail + scope ของ expertise ที่จำเป็น" — ซึ่งตรงกับ mental model ที่ LangChain, CrewAI, Microsoft Agent Framework วาดไว้เป๊ะ ๆ แต่ pitch นี้มาจาก enterprise vendor ที่ขาย license ให้ 83% ของ Fortune 100 แล้ว

ส่วนที่ยิ่งกว่าคือ architecture choice. Adobe ประกาศว่า CX Enterprise Coworker **built on MCP + A2A** (Agent2Agent protocol) — แปลว่า Adobe ไม่ได้สร้าง proprietary agent protocol ของตัวเอง แต่ adopt MCP ของ Anthropic เป็นมาตรฐาน. และเพื่อยืนยันว่าเป็นของจริง Adobe ประกาศ **pushed Adobe Marketing Agent เข้า surface ของทุก hyperscaler พร้อมกัน**: Amazon Quick, Anthropic Claude Enterprise, ChatGPT Enterprise, Gemini Enterprise, IBM watsonx Orchestrate, Microsoft 365 Copilot. เป็น partner announcement ที่มีจำนวน logo มากที่สุดใน keynote AI ปี 2026 จนถึงวันนี้

อีกหนึ่ง signal ที่ถูกมองข้ามคือ **NVIDIA deal**: Adobe integrate NVIDIA **OpenShell secure runtime + Nemotron open models** เข้ากับ security/governance layer ของ CX Enterprise Coworker. Narayen อ้างว่าส่วนนี้เป็น "complete solution สำหรับ regulated industries" — financial services, healthcare, pharma. การที่ Adobe ต้องพ่วง NVIDIA OpenShell เข้ามาสะท้อนว่า **หลัง Flowise CVE + Context.ai breach อาทิตย์ที่แล้ว ไม่มี enterprise vendor ไหนกล้าพูด "agent" โดยไม่มีคำว่า sandbox + governed ต่อท้าย** อีกแล้ว

นอกจากนี้ Adobe ยังปล่อย **Brand Visibility Solution** — เครื่องมือวัดว่าแบรนด์คุณปรากฏยังไงใน ChatGPT/Perplexity/Gemini — ซึ่งเป็น territory เดียวกับที่ Bluefish ปิด Series B $43M เมื่ออาทิตย์ที่แล้ว. Adobe กำลัง bake คำตอบของ category agentic marketing visibility เข้าไปใน suite ของตัวเองก่อน startup category creator จะมี distribution ทัน

## ทำไมสำคัญ

Pattern ที่เห็นในสัปดาห์เดียว — Adobe วันนี้, Databricks Unity AI Gateway เมื่อวาน, Microsoft Agent Framework 1.0 ต้นเดือน, Anthropic Claude Managed Agents ก่อนหน้า — เป็น signal ที่ชัดมากว่า **MCP + A2A กลายเป็น default substrate ของ enterprise agent stack ปี 2026**. นี่ไม่ใช่ emerging standard อีกแล้ว มันถูก Adobe (Adobe!) adopt ใน flagship product — Adobe เป็น vendor ที่ประวัติศาสตร์ชอบ proprietary format เกือบทุกอย่าง (PSD, AI, PDF, PostScript); การที่ Adobe ไม่สร้าง "Adobe Agent Protocol" แล้วไปใช้ MCP ของ Anthropic สะท้อนว่า **network effect ของ MCP ถึง tipping point แล้ว**

จุดที่ Adobe เดาถูกคือ **single-vendor agent หมดยุคใน enterprise**. ลูกค้า Adobe ไม่ได้ใช้แค่ Adobe — พวกเขาใช้ Salesforce + ServiceNow + Workday + SAP + Atlassian + Snowflake + Databricks พร้อมกันหมด. Adobe จึงไม่ pitch ว่า "ใช้ Coworker ของเราแล้วยกเลิก Copilot/Claude/ChatGPT" แต่ pitch ตรงข้าม — "Marketing Agent ของเราเสียบได้กับทุก surface ที่ลูกค้าคุณใช้อยู่". นี่คือ positioning ของ **tool-layer vendor** ไม่ใช่ **portal vendor** — แตกต่างกับ OpenAI ที่ push ให้ ChatGPT เป็น portal เดียวชัดเจน

ที่น่าจับตาถัดไปคือ **Salesforce**. Agentforce ของ Marc Benioff ถูก position เป็น "Agentforce runs the world" — portal-like ambition คล้าย ChatGPT. Adobe เลือกข้าง opposite: distributed + interoperable. **ภายใน 30 วันน่าจะได้ดู Dreamforce preview หรือ blog จาก Benioff responses** ว่า Salesforce จะ double down Agentforce portal หรือจะ concede ใช้ MCP/A2A ตาม Adobe. Bet ผม: Salesforce จะ hybrid — เสริม MCP compatibility แต่ยังคง Data Cloud + Agentforce portal เป็นศูนย์กลาง เพราะเขามี CRM incumbency

## มุม OpenBridge

**Existential lens:** CX Enterprise Coworker ไม่ใช่ threat ตรงกับ OpenBridge เพราะ Adobe ลุยตลาด enterprise brand-level (Fortune 500) — ที่ budget + compliance bar ไม่ overlap กับ Thai SME. **แต่ signal สำคัญคือ MCP + A2A ไม่ optional อีกแล้ว** — ถ้า OpenBridge ไม่ emit MCP tool schema ภายใน Q2 จะถูกถามทันทีตอน sales call ว่า "พ่วงกับ Claude Enterprise/Copilot ของเราได้ไหม?" — และคำตอบ "มี plugin custom" จะแพ้ "yes, เรา MCP-compliant"

**Positioning move:** เก็บคำว่า "Coworker" ไว้ — Adobe แปะ label นี้กับ super-agent orchestrator. OpenBridge ควรชัดเจนว่า OpenBridge = **workflow/integration layer** (tool) ไม่ใช่ coworker (orchestrator). pitch ที่ sharp คือ "OpenBridge = ตัวเสียบ Thai SaaS (SCB Connect, K-Plus, FlowAccount, LINE OA, PromptPay) เข้า Coworker ของ Claude/ChatGPT/Gemini ที่องค์กรคุณมีอยู่แล้ว" — defensible เพราะ local context ที่ Adobe + US vendor ไม่ทำ

**Product action 30 วัน:** (1) publish MCP server spec public — submit เข้า Anthropic MCP registry + Microsoft Agent Framework registry; (2) demo video 60 วินาที "ChatGPT Enterprise + OpenBridge MCP: ดู order PromptPay ล่าสุด ส่ง invoice PEAK ผ่าน LINE OA" — ใช้เป็น top-of-funnel ใน Q2; (3) เริ่มคุย Adobe Thailand/APAC partner team — **เป็น first Thai-native MCP connector ใน Adobe CX Enterprise partner ecosystem ก่อน Q3** — เป็น distribution play ที่ cost-effective กว่า direct SMB outbound

## Sources
- [Adobe News — Adobe Redefines Customer Experience Orchestration Vision in the Agentic AI Era](https://news.adobe.com/news/2026/04/adobe-redefines-custome-experience)
- [Adobe News — Adobe Unveils CX Enterprise Coworker to Build Agentic-Enabled Workflows](https://news.adobe.com/news/2026/04/adobe-unveils-cx-enterprise-coworker)
- [SiliconANGLE — Adobe deploys AI agents across its customer experience tools](https://siliconangle.com/2026/04/20/adobe-deploys-ai-agents-across-customer-experience-tools/)
- [MarTech — Adobe rebrands Experience Cloud as 'CX Enterprise,' goes all-in on AI agents](https://martech.org/adobe-rebrands-experience-cloud-as-cx-enterprise-goes-all-in-on-ai-agents/)
- [Diginomica — Adobe Summit 2026: Adobe gives CX an agentic makeover with the launch of CX Enterprise](https://diginomica.com/adobe-summit-2026-adobe-gives-cx-agentic-makeover-launch-cx-enterprise)

---

## Audio script
วันนี้ที่ Adobe Summit ลาสเวกัส Shantanu Narayen เปิดงานด้วยการฆ่าชื่อ Experience Cloud ที่ใช้มาสิบห้าปี. รีแบรนด์เป็น CX Enterprise. แกนหลักของ suite ใหม่คือ agentic AI ไม่ใช่ marketing automation แบบเดิมแล้ว.

launchhead ที่เด่นที่สุดคือ CX Enterprise Coworker. Adobe ไม่เรียกว่า AI assistant. เรียกว่า super agent ที่ orchestrate agent อื่นได้. decompose goal เป็น multi step plan. มี guardrail + scope ของ expertise. mental model เดียวกับ LangChain CrewAI แต่ pitch โดย enterprise vendor ที่มี Fortune 100 อยู่แล้วแปดสิบสามเปอร์เซ็นต์.

ส่วนที่ใหญ่กว่าคือ architecture. Adobe ไม่สร้าง proprietary agent protocol ของตัวเอง. adopt MCP + A2A เป็นมาตรฐานเปิด. และ push Adobe Marketing Agent เข้า surface ของทุก hyperscaler พร้อมกัน. Amazon Quick. Anthropic Claude Enterprise. ChatGPT Enterprise. Gemini Enterprise. IBM watsonx Orchestrate. Microsoft 365 Copilot. partner logo เยอะที่สุดในปีนี้แล้ว.

ที่น่าจับตาคือ deal กับ NVIDIA. Adobe integrate OpenShell secure runtime + Nemotron models เข้า governance layer. หลัง Flowise CVE + Context ai breach อาทิตย์ที่แล้ว ไม่มี vendor ไหนกล้าพูดคำว่า agent โดยไม่พ่วง sandbox + governed ต่อท้าย. Adobe เข้าใจจุดนี้เร็ว.

signal ที่สำคัญที่สุดคือ. Adobe ที่ชอบ proprietary format ทุกอย่าง. PSD. AI. PDF. PostScript. วันนี้ adopt MCP ของ Anthropic. แปลว่า network effect ของ MCP ถึง tipping point แล้ว. ใครไม่มี MCP ใน Q2 จะถูกถามใน sales call ว่าพ่วง Claude Enterprise กับ Copilot ได้ไหม. แล้วแพ้ทันที.

สำหรับ OpenBridge. ไม่ใช่ threat ตรง เพราะ Adobe เล่น Fortune 500 ไม่ overlap Thai SME. แต่ message ที่ต้องชัดในสามสิบวันคือ OpenBridge equal tool layer ไม่ใช่ coworker. pitch ที่คม คือ OpenBridge เป็นตัวเสียบ Thai SaaS SCB Connect K Plus FlowAccount LINE OA PromptPay เข้า Coworker ของ Claude หรือ ChatGPT ที่องค์กรคุณมีอยู่แล้ว. defensible เพราะ local context.

action ที่ทำใน tri day thirty. publish MCP server spec submit เข้า Anthropic registry. demo video หกสิบวินาที ChatGPT Enterprise plus OpenBridge MCP. แล้วคุย Adobe Thailand partner team. เป็น first Thai native MCP connector ใน Adobe CX Enterprise partner ecosystem ก่อน Q3. distribution play ที่ cost effective กว่า direct outbound.
