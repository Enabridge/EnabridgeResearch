---
date: 2026-05-08
slug: nvidia-servicenow-project-arc-openshell-nemotron-nowai-bench
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A bold editorial illustration in deep navy and warm cream — at center, a stylized flat-vector laptop sits open with an oversized cream desktop window labeled 'PROJECT ARC' showing a glowing teal agent orb running long-running tasks. The laptop sits inside a transparent sandbox cube outlined in coral with the label 'NVIDIA OPENSHELL' in bright sans-serif. Below the desk, a benchmark scoreboard reads 'NOWAI-BENCH' in big cream letters with '#1' rendered very large in coral and 'NEMOTRON 3 SUPER' in tiny cream below. A small NVIDIA green eye logo and ServiceNow purple logo float at the corners. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + teal palette, no human figures, all text and logos crisp for 200px thumbnail readability.
image: 
---

# NVIDIA + ServiceNow ปล่อย Project Arc — autonomous desktop agent ที่ run บน OpenShell, Nemotron 3 Super คว้า #1 บน NOWAI-Bench

## TL;DR
- 5 พ.ค. 2026 ที่ Knowledge 2026 ServiceNow + NVIDIA เปิด Project Arc — long-running self-evolving autonomous desktop agent สำหรับ developer/IT/admin; เข้าถึง local file system + terminal + apps บนเครื่องของ user ได้, รัน multi-step task ที่ traditional automation ทำไม่ได้, แต่ทุก action ผ่าน ServiceNow Action Fabric ได้ governance + audit
- Project Arc รันบน **NVIDIA OpenShell** — open-source secure runtime สำหรับ deploy autonomous agent ใน sandbox ที่ policy-governed, ป้องกัน agent ทำของผิดที่ไม่ควรบนเครื่อง endpoint
- เปิดตัว **NOWAI-Bench** — open benchmarking suite พร้อม EnterpriseOps-Gym (one of industry's most challenging enterprise agent benchmarks) integrated กับ NVIDIA NeMo Gym; **Nemotron 3 Super คว้า #1 บน EnterpriseOps-Gym** ตอนนี้ — signal ว่า open-source model ของ NVIDIA แข่งกับ frontier proprietary ในงาน enterprise agent ได้แล้ว

## เกิดอะไรขึ้น

วันที่ 5 พ.ค. 2026 ที่ Knowledge 2026 NVIDIA กับ ServiceNow extend partnership ที่มีมาตั้งแต่ Apriel Nemotron — ออกของใหม่สามชิ้นพร้อมกัน Project Arc คือชิ้นที่ใหญ่ที่สุด: **autonomous desktop agent** ที่ออกแบบให้รันยาว ๆ ทำงานข้ามวัน เป้าลูกค้าคือ developer, IT engineer, system admin ของ enterprise ที่งานต้อง stitch tools 5–10 ตัวเข้าด้วยกัน — IDE, terminal, monitoring tool, ticketing, ChatOps, doc system Project Arc เข้าถึง local file system, terminal, และ application ที่ install บนเครื่องของ user ได้โดยตรง — ทำงานที่ traditional UI automation (RPA) ทำไม่ได้ เช่น "ไปดู repo นี้, identify failing test, ลอง patch, push branch ใหม่, ขอ review" — แต่ตัว connector layer ที่ Arc ใช้ map เข้า ServiceNow Action Fabric ทุก step → identity ของ user verified, scope ของ permission ตาม role, ทุก action audit ลง log ของ AICT

ใต้ฝา Project Arc รันบน **NVIDIA OpenShell** — open-source secure runtime ที่ NVIDIA ออกใหม่สำหรับ deploy autonomous agent ใน sandbox ที่ policy-governed Concept คือ agent ใด ๆ จะ execute code, file write, terminal command, network call ใน container ที่ทุก permission กำหนดได้ละเอียดระดับ syscall — ถ้า agent ทำ action ที่ outside policy เช่น ลบ file ที่ไม่ใช่ scope, หรือ open port outbound ที่ไม่ได้ approve — sandbox block ทันทีและ ping AI Control Tower OpenShell open-source ทำให้ทุก enterprise sec team สามารถ audit code ของ runtime ได้เอง — ตอบโจทย์ CISO ที่กลัว "agent หลุด permission" ที่ Fortune ใช้ครอบคลุมในข่าว 6 พ.ค. ว่า "9 seconds delete everything" ตรง ๆ

ชิ้นที่สาม คือ **NOWAI-Bench** — open benchmarking suite สำหรับ enterprise AI agent ที่ ServiceNow + NVIDIA build ร่วมกัน รวม **EnterpriseOps-Gym** ที่ NVIDIA เคลม เป็น "one of industry's most challenging enterprise agent benchmarks" — task ที่ต้อง agent solve รวม IT operations, customer service triage, HR workflow, finance approval — integrated เข้ากับ NVIDIA NeMo Gym library ที่ developer ใช้ train/evaluate agent อยู่แล้ว ตัวเลขที่ทุกคนพูดถึง: **Nemotron 3 Super (open-source) ranks #1 บน EnterpriseOps-Gym ตอนนี้** — ขึ้นมานำ Anthropic Claude Opus 4.7, GPT-5.5, Gemini 2.5 Pro ในงาน enterprise agent specifically (ไม่ใช่ math/code benchmark ที่ทุกคนสนใจ)

## ทำไมสำคัญ

Pattern หลักที่เห็น: **agentic AI กำลังย้ายลงมาที่ desktop endpoint** — ปี 2024–25 เราเห็น agent ส่วนใหญ่อยู่บน cloud (ChatGPT, Claude.ai, Sierra), บน webapp (Glean, Harvey), หรือใน chatbox ของ SaaS (Salesforce Einstein, ServiceNow Now Assist) ปี 2026 ตลาดเริ่มเห็นว่างานจริงของ knowledge worker — โดยเฉพาะ developer/IT — ต้อง agent เข้าถึง local environment ของ user (file system, terminal, app installed) ไม่ใช่แค่ cloud — Project Arc + Microsoft Agent 365 + OpenAI ChatGPT desktop agent ทุกอันตอบโจทย์เดียวกัน point of friction ที่ใหม่จึงไม่ใช่ "เรียก API ได้ไหม" แต่ "agent ที่ run ในเครื่อง user ได้ governance + sandbox ที่ CISO ยอมรับไหม" — OpenShell คือคำตอบของ NVIDIA สำหรับคำถามนั้น

นัยที่สอง: **Nemotron 3 Super #1 บน EnterpriseOps-Gym** เป็น signal ที่สำคัญมาก — open-source model ของ NVIDIA (พัฒนาบน Llama base ของ Meta + Apriel Nemotron + อื่น ๆ) สามารถแข่งกับ frontier proprietary model ในงาน enterprise agent specifically ได้แล้ว ปี 2025 ข้อโต้แย้งสนับสนุน Anthropic/OpenAI คือ "frontier model ดีกว่า open-source อย่างชัดเจน" — ปี 2026 อย่างน้อยใน enterprise vertical-specific benchmark, ข้อโต้แย้งนั้นเริ่มอ่อน Cost ของ Nemotron บน TCO ต่ำกว่า Claude/GPT ใน 5–10x สำหรับ workload ที่รัน 24/7 — enterprise CFO ที่จ่ายค่า token ของ frontier model จะถามคำถาม "ทำไม Nemotron ทำได้แค่นี้ก็พอ" ในทุก budget review

นัยที่สาม: **NOWAI-Bench เป็น benchmark ที่จะเปลี่ยน procurement** — ปี 2025 enterprise CTO ดู MMLU, GPQA, SWE-Bench เป็น primary metric — เป็น benchmark ที่ตรงกับงาน developer/research ไม่ใช่ enterprise ops พอ NOWAI-Bench / EnterpriseOps-Gym ออกมา (open + governed by ServiceNow + NVIDIA) — ทุก vendor ที่ขาย enterprise agent ต้อง publish score ของตัวเองบน benchmark นี้ ลูกค้า Fortune 500 ที่ทำ POC จะเริ่ม "score-driven procurement" — ใครไม่ test ตัวเองบน NOWAI ก็คือ "ไม่ enterprise-ready" สำหรับ buyer

## มุม OpenBridge

OpenBridge ต้องอ่าน 3 ทางจากข่าวนี้ทันที (1) **ทดสอบ OpenBridge connector บน NOWAI-Bench / EnterpriseOps-Gym** — submit ของจริง, publish score ที่ลูกค้า Fortune 500 ใน Thai (SCB/KBank/AIS/PTT) ดูได้, claim ว่า "agent ที่ใช้ OpenBridge connector ผ่าน NOWAI ได้ score X% เพิ่มขึ้น" — กลายเป็น marketing material ที่ technical (2) **Build OpenBridge connector ที่ Project Arc / OpenShell sandbox มัน trust ได้** — Project Arc agent ของ developer/IT จะ invoke OpenBridge ผ่าน MCP เพื่อทำ action ภายนอก (call HubSpot, push GitHub PR, post Slack); OpenBridge ต้องทำ connector spec ที่ระบุ permission scope ละเอียด (เช่น "อ่าน HubSpot contact ของ tenant X เท่านั้น") เพื่อให้ OpenShell policy engine block correctly (3) **Tap Nemotron 3 Super เป็น default model ใน OpenBridge "AI Workflow" feature** — ลูกค้าที่ไม่อยากผูก OpenAI/Anthropic, อยากรัน on-prem หรือ on-VPC เพื่อ data residency, OpenBridge ขายว่า "เลือก Nemotron 3 Super, NOWAI #1, รันใน VPC ของลูกค้าได้, cost 5–10x ถูกกว่า Claude" — open-source advantage ที่ enterprise CFO เซ็นได้ทันที

Adjacent insight: ที่ NVIDIA ปล่อย OpenShell open-source = signal ว่า NVIDIA เริ่มไม่ได้แค่ขายชิป แต่ขาย runtime + benchmark + model ทั้ง stack — competition กับ Microsoft Agent 365 stack จะเข้มขึ้น OpenBridge ไม่ควรเลือกข้าง แต่ออก connector ที่ work บนทั้ง OpenShell และ Agent 365 sandbox — ตำแหน่งที่ทุก endpoint runtime ของ enterprise มอง OpenBridge เป็น default integration

## Sources
- [NVIDIA and ServiceNow Partner on New Autonomous AI Agents for Enterprises | NVIDIA Blog](https://blogs.nvidia.com/blog/servicenow-autonomous-ai-agents-enterprises/)
- [ServiceNow extends agentic AI governance from desktops to data centers with NVIDIA | ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-extends-agentic-AI-governance-from-desktops-to-data-centers-with-NVIDIA/default.aspx)
- [NVIDIA at ServiceNow Knowledge | May 5–7, 2026 | NVIDIA](https://www.nvidia.com/en-us/events/servicenow-knowledge/)
- [NVIDIA Nemotron: Advanced Multimodal AI Models for Agentic Reasoning | NVIDIA](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)

---

## Audio script
เรื่องที่สามครับโย ที่งาน Knowledge 2026 เดียวกัน NVIDIA กับ ServiceNow ออกของใหม่สามชิ้น Project Arc คือ autonomous desktop agent ที่รันยาว ๆ ทำงานข้ามวัน เข้าถึง local file system terminal app บนเครื่อง user ได้ตรง สำหรับ developer IT admin เรา agent ทำงานที่ RPA ทำไม่ได้ เช่นไปดู repo identify failing test patch push PR ขอ review แต่ทุก step ผ่าน Action Fabric ได้ identity scope audit

ใต้ฝา Project Arc รันบน NVIDIA OpenShell open source secure runtime ที่ deploy agent ใน sandbox policy governed ระดับ syscall ถ้า agent ทำผิด policy block ทันทีและ ping AICT เปิด open source ให้ CISO audit code เองได้ ตอบโจทย์ที่ Fortune เคยเตือนว่า agent หลุดลบของได้ใน 9 วินาที

ชิ้นที่สามคือ NOWAI Bench open benchmark ที่ ServiceNow และ NVIDIA build ร่วมกัน รวม EnterpriseOps Gym task ที่ครอบคลุม IT ops customer service HR finance ของจริงคือ Nemotron 3 Super open source ของ NVIDIA ขึ้น number 1 บน EnterpriseOps Gym ตอนนี้ นำ Claude Opus 4.7 GPT 5.5 Gemini 2.5 Pro ในงาน enterprise agent specifically signal ว่า open source แข่ง frontier ใน vertical benchmark ได้แล้ว cost ต่ำ 5 ถึง 10 เท่า

มุม OpenBridge สามเรื่อง หนึ่ง submit OpenBridge connector ทดสอบบน NOWAI Bench publish score ให้ลูกค้า Thai Fortune 500 ดู กลายเป็น marketing technical สอง build connector ที่ Project Arc OpenShell sandbox trust ได้ permission scope ละเอียด สาม tap Nemotron 3 Super เป็น default model ใน OpenBridge AI Workflow ขายว่า run ใน VPC ลูกค้าได้ data residency ผ่าน cost 5 ถึง 10 เท่าถูกกว่า Claude open source advantage ที่ CFO เซ็นได้ทันทีครับ
