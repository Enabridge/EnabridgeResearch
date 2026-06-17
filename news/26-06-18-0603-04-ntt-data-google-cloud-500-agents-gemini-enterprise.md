---
date: 2026-06-17
slug: ntt-data-google-cloud-500-agents-gemini-enterprise
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a vast agent factory floor where 500 small robotic
  agents stand in tidy grid formation, each tagged with industry icons (bank,
  insurance shield, manufacturing gear, retail bag). A Google Cloud Gemini
  diamond logo and an NTT DATA wordmark glow above the floor. Giant overlaid
  text reads "500 AGENTS" and "5,000 EXPERTS". Composition is wide-angle low
  perspective looking across the factory floor toward a glowing horizon, deep
  blue industrial palette with bright Gemini gradient blue-purple-pink
  lighting from above. Style is cinematic editorial illustration, high-contrast,
  brand marks and numerals legible at 200px thumbnail, no real human faces — only
  robotic silhouettes. 1:1 aspect ratio.
image: images/26-06-18-0603-04-ntt-data-google-cloud-500-agents-gemini-enterprise.png
---

# NTT DATA + Google Cloud joint roadmap 500 agents + 5,000 certified experts — Gemini Enterprise ขยับจาก pilot สู่ production

## TL;DR
- 8 มิ.ย. NTT DATA (Japanese SI ใหญ่, $30B+ revenue) ประกาศ expanded collaboration กับ Google Cloud — joint roadmap 500 AI agents สำหรับ horizontal + industry-specific use case + 5,000 certified Gemini Enterprise experts
- Target industry: banking, insurance, manufacturing, retail — รวมถึง cloud migration, SDLC, marketing, procurement, finance ops
- เป็น "agent factory" model — agent reusable แชร์ across ลูกค้า, ลด time-to-deployment จาก pilot สู่ production scale

## เกิดอะไรขึ้น

วันที่ 8 มิถุนายน 2026 NTT DATA — ฝ่าย IT services ของ NTT Group ($30B+ revenue, employee 190,000+ คน) — ประกาศ expanded collaboration กับ Google Cloud เพื่อเร่ง deployment ของ agentic AI ใน enterprise client การ collaboration มี 2 component หลัก: (1) **joint roadmap ที่จะ co-innovate up to 500 AI agents** ครอบคลุมทั้ง horizontal use case (procurement, finance ops, marketing) และ industry-specific (banking, insurance, manufacturing, retail) — agent เหล่านี้ design ให้เป็น "reusable building block" ที่ deploy ข้ามลูกค้าได้, (2) **5,000 certified experts** — NTT DATA จะตั้ง Gemini Enterprise practice ที่ certified ใน Gemini stack เพื่อ deliver implementation

นี่เป็น **scale ที่ใหญ่กว่า typical SI partnership** หลายเท่า ก่อนหน้านี้ Accenture + ServiceNow ประกาศ Forward Deployed Engineering program (6 พ.ค.) ที่มี 300 pre-built skill + คน FDE จำนวนไม่เปิดเผย — NTT DATA + Google คือ 500 agent + 5,000 expert ที่มีจำนวน specific และ public ตัวเลข 5,000 expert คือ ~2.6% ของ employee base ของ NTT DATA ซึ่งเป็นการ commit organizational capacity ระดับ "strategic bet" ไม่ใช่ side project

Focus area เปิดเผยตรง — banking + insurance สำหรับ regulated workflow, manufacturing สำหรับ predictive maintenance + supply chain optimization, retail สำหรับ personalization + inventory ส่วน horizontal use case เช่น procurement automation, finance close, marketing campaign — เป็น area ที่ ROI วัดได้ในไตรมาสเดียว (Klarna AI agent save $60M จาก 853 FTE-equivalent ในปี 2025 เป็น benchmark ที่ลูกค้ารายอื่นใช้เปรียบเทียบ)

Strategic context — Google Cloud ในรอบ 12 เดือนที่ผ่านมา push Gemini Enterprise หนักมาก, target Anthropic Claude + OpenAI ที่ครองเอ็นเตอร์ไพรซ์ตอนนี้ การได้ NTT DATA เป็น delivery partner หลักใน Asia-Pacific คือ play ใหญ่ — NTT DATA มี relationship กับ Japanese banking + manufacturing ที่ Google Cloud เข้าไม่ถึงโดยตรง การมี 5,000 expert ที่ certify ใน Gemini Enterprise = sales channel + delivery channel ในประเทศที่ adoption Google Cloud ช้ากว่า US/EU (ที่ AWS/Azure ครอง)

## ทำไมสำคัญ

ดีลนี้คือ **template ใหม่สำหรับ "agent factory at SI scale"** — model เก่าของ SI consulting (Accenture, Deloitte, PwC, NTT, TCS, Infosys) คือ deploy custom implementation per client — แพง, ช้า, ไม่ reuse ตัวเลข 500 agent + 5,000 expert บอก model ใหม่: build agent library + skill pool ที่ reuse + deploy ข้ามลูกค้าได้ — ลด unit cost per deployment ลงหลายเท่า สอดคล้องกับที่ Gartner คาดว่า 40% ของ enterprise app จะมี task-specific AI agent ฝังภายในสิ้น 2026 (จาก <5% ในต้น 2025) — ถ้า Gartner ถูก ดีล NTT × Google คือ delivery infrastructure ที่ทำให้ scale นี้ตามได้

นัยที่สอง — **regulated industry กลายเป็น tipping point ของ enterprise AI adoption** Banking + insurance ใน Japan ที่ NTT DATA serve คือ industry ที่ระมัดระวังที่สุดในการ deploy AI ตอนนี้ ถ้า NTT DATA + Google deliver agent ที่ผ่าน regulator ของ japanese banking ได้ (Financial Services Agency) จะเป็น proof point ที่ลูกค้า banking ทั่วโลกใช้อ้างอิง Anthropic + Claude ที่ partner กับ TCS (11 มิ.ย.) และ DXC (12 มิ.ย.) ก็เล็งกลุ่มเดียวกัน — กำลังจะมี race ใน 2H 2026 ว่าใครจะ deploy agent ใน regulated industry ได้ scale ที่สุด

ที่สาม — **5,000 certified expert คือ moat ที่ replicate ยากกว่า model** Google Cloud คงคิดได้ว่า model ของ Gemini จะถูก commoditize ใน 18 เดือน (เพราะ Anthropic + OpenAI + xAI ปล่อย model competitive ทุก 6 สัปดาห์) แต่ 5,000 certified expert ที่รู้ enterprise workflow + Japanese culture + Gemini stack ลึก เป็น advantage ที่ Anthropic + OpenAI สร้างเร็วไม่ทัน นี่คือเหตุผลที่ hyperscaler ทุกเจ้ากำลัง force partner ระดับนี้ — เพราะ "delivery layer" คือ moat ใหม่ที่ผูกกับ infra

## มุม OpenBridge

ดีลนี้ **validate model ของ "vertical agent library"** สำหรับ OpenBridge — ถ้า NTT DATA + Google ลงทุนสร้าง 500 agent ที่ reusable, OpenBridge มี opportunity เป็น **integration platform underneath ที่ agent เหล่านั้นวิ่งผ่าน** เพื่อเชื่อมเข้า enterprise system (SAP, Workday, ServiceNow, Salesforce, core banking system) คำถามคือ Google Cloud จะ standardize ที่ MCP, A2A, OpenSharing protocol หรือสร้าง proprietary connector ของตัวเอง — OpenBridge ถ้า expose ตัวเองผ่าน open protocol ทุกตัว จะสามารถ plug เข้า delivery channel ของ NTT DATA + Accenture + TCS โดยที่ไม่ต้อง deal โดยตรงกับ SI

ที่ต้อง pay attention — 500 agent reusable คือ **commoditization ของ implementation work** — ลูกค้า enterprise จะคาด price drop 50-70% ต่อ agent deployment ภายใน 12 เดือน OpenBridge ที่ขายเป็น integration platform per-seat หรือ per-connector ต้องปรับ pricing model ให้แข่ง — usage-based + outcome-based น่าจะ sustainable กว่า seat-based เมื่อ unit cost ของ implementation ลดลง

ที่ stretch goal — Japanese banking + manufacturing คือ market ที่ OpenBridge ยังไม่มี presence ที่ NTT DATA ถ้า expand 5,000 expert จริง คือ channel partner potential ที่ใหญ่มาก แต่ต้องเข้าใจ relationship dynamic ของ Japanese SI (long sales cycle, deep technical proof needed, decision by committee) — partnership development ที่ต้องเตรียม 6-12 เดือน ไม่ใช่ deal ที่ปิดเร็ว — แต่ถ้าได้ relationship จะเป็น defensive moat ที่ทำให้ competitor วงตะวันตกเข้าตลาด Japan ตามยาก

## Sources
- [NTT DATA Expands Collaboration with Google Cloud to Accelerate Enterprise AI from Pilots to Production — NTT DATA](https://www.nttdata.com/global/en/news/press-release/2026/june/060900)
- [Google Cloud Adds NTT DATA to Gemini Enterprise Delivery Push — ERP Today](https://erp.today/google-cloud-ntt-data-gemini-enterprise-ai/)
- [NTT Data, Google Cloud target enterprise AI rollout with 500 AI agents — Bizcommunity](https://www.bizcommunity.com/article/ntt-data-google-cloud-target-enterprise-ai-rollout-with-500-ai-agents-286527a)
- [NTT DATA and Google Cloud Prepare a Global AI Agent Factory — Cloud News](https://cloudnews.tech/ntt-data-and-google-cloud-prepare-a-global-ai-agent-factory/)
- [NTT DATA and Google Cloud expand collaboration on agentic AI — Techzine](https://www.techzine.eu/news/applications/141910/ntt-data-and-google-cloud-expand-their-collaboration-on-agentic-ai/)

---

## Audio script

ข่าวสุดท้ายของรอบ NTT DATA บริษัท IT services ของ NTT Group ขนาด สามหมื่นล้าน ดอลลาร์ ประกาศ expanded collaboration กับ Google Cloud วันที่ แปด มิถุนายน roadmap ใหญ่มาก สร้าง 500 AI agent ที่ reuse ได้ ครอบคลุม banking insurance manufacturing retail และ horizontal use case เช่น procurement finance close marketing บวกกับ 5,000 certified expert ใน Gemini Enterprise

นี่คือ scale ที่ใหญ่กว่า typical SI partnership หลายเท่า เทียบกับ Accenture บวก ServiceNow ที่ประกาศ Forward Deployed Engineering ต้นเดือน พฤษภาคม มี 300 pre-built skill NTT DATA บวก Google คือ 500 agent + 5,000 expert ที่ตัวเลข specific 5,000 expert คือ สองจุดหก เปอร์เซ็นต์ ของ employee base ของ NTT DATA เป็น strategic bet ไม่ใช่ side project

template ใหม่ที่เห็น — agent factory at SI scale — model เก่าของ consulting deploy custom per client แพง ช้า ไม่ reuse model ใหม่ build library reuse ข้ามลูกค้า unit cost ลดหลายเท่า สอดคล้องกับ Gartner ที่คาดว่าสี่สิบ เปอร์เซ็นต์ ของ enterprise app จะมี agent ฝังภายในสิ้นปี ตัวเลขที่ดูเยอะแต่อาจทำได้ถ้า delivery infrastructure ตามทัน

สำหรับ OpenBridge ดีลนี้ validate model ของ vertical agent library OpenBridge เป็น integration layer ใต้ agent เชื่อมเข้า SAP Workday ServiceNow Salesforce core banking ถ้า expose ผ่าน MCP A2A OpenSharing protocol สามารถ plug เข้า delivery channel ของ NTT Accenture TCS โดยไม่ต้อง deal SI โดยตรง ที่ต้องคิดคือ pricing per seat ต้องปรับ เป็น usage-based เพราะ implementation cost จะตกลง ห้าสิบ ถึง เจ็ดสิบ เปอร์เซ็นต์ ใน 12 เดือนหน้า และ NTT DATA channel partner คือ door ใหญ่เข้า Japanese banking manufacturing ถ้าทำ partnership development ได้
