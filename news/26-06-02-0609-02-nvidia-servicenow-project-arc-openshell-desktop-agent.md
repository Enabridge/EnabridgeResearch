---
date: 2026-06-02
slug: nvidia-servicenow-project-arc-openshell-desktop-agent
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a glowing knowledge worker's desktop computer
  enclosed inside a translucent green safety vault, with the NVIDIA logo on
  top and ServiceNow logo on the side. Inside the vault, a robotic arm
  silhouette types on a keyboard while a clipboard labeled "AUDIT LOG"
  hovers beside it, capturing every action with checkmarks. Outside the
  vault, a glowing badge reads "Project Arc" in bold white letters, with a
  subline "OpenShell · Sandboxed Runtime". Background: a corporate enterprise
  office at night with blue Bill McDermott silhouette and green Jensen Huang
  silhouette standing on a stage. Style: clean editorial, cinematic lighting,
  NVIDIA green and ServiceNow blue palette, high contrast, 1:1 aspect, text
  readable at 200px thumbnail. No real human faces.
image: images/26-06-02-0609-02-nvidia-servicenow-project-arc-openshell-desktop-agent.png
---

# NVIDIA + ServiceNow เปิด Project Arc — desktop agent ที่ enterprise governance built-in, vs OpenClaw และ Microsoft Agent 365

## TL;DR
- ServiceNow Knowledge 2026: Jensen Huang ขึ้น keynote ร่วม Bill McDermott ประกาศ Project Arc — long-running self-evolving desktop agent
- รันบน NVIDIA OpenShell — open-source sandboxed runtime ที่แต่ละ agent มี isolated environment แยก infrastructure layer ออกจาก policy layer
- ServiceNow AI Control Tower คุม policy + audit log ทุก action — vs OpenAI OpenClaw ที่ enterprise มอง "ungoverned" และ Microsoft Agent 365 ที่เน้น discover/control plane

## เกิดอะไรขึ้น

ที่ ServiceNow Knowledge 2026 ในต้นพฤษภาคม Jensen Huang ขึ้น keynote ร่วมกับ Bill McDermott CEO ของ ServiceNow และเปิดตัว Project Arc — autonomous desktop agent ที่ออกแบบมาสำหรับ knowledge worker, developer และ IT admin ตัว agent เข้าถึงได้ผ่าน desktop app, enterprise collaboration tool หรือ email และทำงาน multi-step ข้าม enterprise tool ได้โดยไม่ต้องมี pre-built workflow รองรับ

ส่วนที่เป็นจุดเปลี่ยนคือ runtime layer — Project Arc ทำงานบน NVIDIA OpenShell ซึ่งเป็น open-source secure-by-design runtime ที่ NVIDIA ปล่อยออกมาในรอบเดียวกัน OpenShell สร้าง individual isolated sandbox ให้แต่ละ agent โดยแยก application-layer operation ออกจาก infrastructure-layer policy enforcement ชัดเจน enterprise สามารถกำหนดได้ละเอียดว่า agent เห็นอะไรได้บ้าง ใช้ tool อะไรได้ และทุก action ถูก contain ใน sandbox ที่ audit ได้

ServiceNow AI Control Tower เป็น governance layer ด้านบน — ทำหน้าที่ set policy, monitor behavior และ log ทุก file ที่อ่าน command ที่รัน API ที่เรียก ทุก action ผ่าน ServiceNow Action Fabric หมายความว่า admin ของบริษัทเห็น real-time ทุกสิ่งที่ Project Arc ทำในเครื่องของ employee — และสามารถ pause หรือ terminate agent ได้ทันที architecture นี้ตอบโจทย์ CISO ที่กังวลกับ OpenAI OpenClaw (desktop agent ตัวก่อนหน้าที่หลายบริษัทแบนเพราะไม่มี enterprise audit layer)

ที่น่าสนใจคือ Microsoft เพิ่งเปิด Agent 365 GA เมื่อ 1 พ.ค. เป็น cross-cloud control plane ที่ discover และ govern AI agent ข้าม Microsoft, AWS Bedrock, Google Cloud — รวมถึง detection ของ shadow agent อย่าง OpenClaw, Claude Code ที่ employee install เอง Microsoft positioning เป็น meta-layer ที่ดูแลทุก agent ส่วน NVIDIA + ServiceNow เลือกเส้นทาง vertical integration — ขายทั้ง runtime + governance + agent product เป็น stack เดียวที่ทำงานร่วมกันแน่น

## ทำไมสำคัญ

Pattern ที่ชัดในรอบนี้คือ **enterprise agent ตลาดแยกเป็น 3 ค่ายชัดเจน** — (1) OpenAI OpenClaw + ChatGPT Enterprise ที่เป็น product-first, governance รอเสริมทีหลัง (2) Microsoft Agent 365 ที่เป็น cross-cloud control plane, neutral กับ vendor (3) NVIDIA + ServiceNow Project Arc + OpenShell ที่ขาย full stack governance-native ตั้งแต่วันแรก ค่าย 3 นี้กำลังแย่ง CIO budget เดียวกัน — และ enterprise procurement ที่เลือกระหว่าง 3 ตัวนี้จะ define เอนคอน next 5 ปี

จุดที่ NVIDIA + ServiceNow แข็งคือ vertical stack — agent run บน NVIDIA GPU, sandbox โดย OpenShell, governance โดย ServiceNow Control Tower เป็น integration ที่ tight มากเทียบกับ OpenClaw ที่ run บน user desktop OS ที่ controlled น้อย หรือ Microsoft Agent 365 ที่เป็น layer บางบนของ heterogeneous agent ecosystem — ทำให้ Project Arc ขายให้ regulated industry (bank, healthcare, gov) ได้ง่ายกว่า เพราะมี audit trail end-to-end ที่ defensible ต่อ regulator

อีกประเด็น — OpenShell เป็น open-source หมายความว่า NVIDIA ตั้งใจให้เป็น **default runtime spec** ของ agent ecosystem ทั้งหมด ถ้าทำสำเร็จ OpenShell จะเป็น Docker ของ AI agent era — ทุก agent ต้อง package ใน OpenShell sandbox เพื่อให้ enterprise ยอมรัน นี่คือ play ที่ NVIDIA เคยทำสำเร็จกับ CUDA — ลอง standardize layer ที่ทุกคนต้องใช้ ถึงแม้ตัว runtime จะฟรี แต่ GPU ที่รันมันคือสิ่งที่ NVIDIA ขาย

## มุม OpenBridge

สำหรับ OpenBridge — ตลาด enterprise agent governance กำลัง crystallize เป็น 3 ค่ายชัด integration backbone neutral ที่ทำงานได้กับทั้ง OpenClaw, Agent 365 และ Project Arc พร้อมกันคือ positioning ที่มีค่ามากใน 6–12 เดือนข้างหน้า เพราะ enterprise ส่วนใหญ่ไม่ได้เลือกแค่ค่ายเดียว — มี dev team ใช้ Claude Code, customer-facing team ใช้ Sierra agents, IT ops ใช้ Project Arc — ต้องการ orchestration layer ที่อยู่เหนือทั้งหมด

อีกมุม — OpenShell ที่เป็น open standard อาจเป็น opportunity สำหรับ OpenBridge — ถ้าเราสร้าง connector library ที่ deploy เข้า OpenShell sandbox ได้ตรง ๆ จะกลายเป็น default integration option สำหรับลูกค้า Project Arc และในระยะยาว ถ้า OpenShell ขึ้นเป็น industry standard จริง ทุก agent ที่ run บน OpenShell ก็จะใช้ connector ของ OpenBridge ได้ทันที — เป็น distribution advantage ที่ scale ขึ้นพร้อมกับ ecosystem โดยที่เราไม่ต้องลงทุนเอง

## Sources
- [NVIDIA and ServiceNow Partner on New Autonomous AI Agents for Enterprises — NVIDIA Blog](https://blogs.nvidia.com/blog/servicenow-autonomous-ai-agents-enterprises/)
- [ServiceNow extends agentic AI governance from desktops to data centers with NVIDIA — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-extends-agentic-AI-governance-from-desktops-to-data-centers-with-NVIDIA/default.aspx)
- [Jensen Huang and Bill McDermott bet on OpenShell to secure enterprise AI agents — The New Stack](https://thenewstack.io/nvidia-openshell-agent-runtime/)
- [Project Arc: ServiceNow and Nvidia's Enterprise Desktop Agent — The Letter Two](https://thelettertwo.com/2026/05/13/project-arc-servicenow-nvidia-enterprise-desktop-agent)
- [Microsoft Agent 365 GA: Control Plane for Governing AI Agents Across Windows and Multicloud — Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)

---

## Audio script
สวัสดีครับ Yoh ที่ ServiceNow Knowledge 2026 Jensen Huang ขึ้น keynote ร่วมกับ Bill McDermott เปิดตัว Project Arc desktop agent ที่ทำงาน multi step ข้าม enterprise tool โดยไม่ต้องมี pre built workflow และที่สำคัญคือมี governance built in ตั้งแต่วันแรก ตัว agent รันบน NVIDIA OpenShell ซึ่งเป็น open source sandboxed runtime ที่แต่ละ agent มี isolated environment ของตัวเอง แยก application layer ออกจาก policy layer ชัดเจน ส่วน ServiceNow AI Control Tower ทำหน้าที่ log ทุก action ที่ agent ทำ ทั้ง file ที่อ่าน command ที่รัน API ที่เรียก architecture แบบนี้ตอบโจทย์ CISO ที่กังวลกับ OpenAI OpenClaw ที่ไม่มี enterprise audit ตรงจุดที่ขายให้ regulated industry ทั้ง bank healthcare และ government ได้ง่ายกว่า ตอนนี้ตลาด enterprise agent แยกเป็นสามค่ายชัด คือ OpenAI OpenClaw, Microsoft Agent 365 ที่เป็น cross cloud control plane, และ NVIDIA ServiceNow ที่เป็น full stack แบบ vertical สำหรับ OpenBridge ตลาดนี้กำลัง crystallize หมายความว่า integration backbone neutral ที่ทำงานได้กับทั้งสามค่ายพร้อมกันคือ positioning ที่มีค่ามาก เพราะ enterprise ส่วนใหญ่ไม่ได้เลือกค่ายเดียว ในระยะยาวถ้า OpenShell ขึ้นเป็น industry standard จริง ทุก agent ที่รันบนนั้นก็จะใช้ connector ของ OpenBridge ได้ทันที เป็น distribution advantage ที่ scale พร้อม ecosystem ครับ
