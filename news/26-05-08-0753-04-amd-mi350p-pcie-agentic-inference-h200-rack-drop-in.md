---
date: 2026-05-08
slug: amd-mi350p-pcie-agentic-inference-h200-rack-drop-in
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: A bold editorial illustration in deep navy and warm cream — at center, an oversized stylized PCIe accelerator card rendered as a glossy navy slab with bright coral 'AMD INSTINCT MI350P' text and '144GB HBM3E' in cream below, dropping into a slot of an existing standard server rack drawn in cream outlines. Above the card floats a coral burst marked '+40% vs H200 NVL' and a teal banner reading 'NO REBUILD'. To the side, eight smaller card icons stack like dominoes labelled '8x' showing scale-out. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + teal palette, no human figures, all text and logos crisp for 200px thumbnail readability.
image: 
---

# AMD ปล่อย MI350P PCIe — agentic inference 144GB ใส่เซิร์ฟเวอร์เดิม ไม่ต้อง rebuild rack, FP16 เหนือ H200 NVL 40%

## TL;DR
- 7 พ.ค. 2026 AMD เปิดตัว Instinct MI350P PCIe — dual-slot air-cooled card, 128 CU + **144GB HBM3E** + 600W envelope; design ให้ drop-in กับ standard server ที่มีอยู่แล้วของ enterprise — ไม่ต้อง rebuild rack, ไม่ต้องเปลี่ยน power, ไม่ต้องเปลี่ยน cooling
- Tom's Hardware ทดสอบ — **FP16/FP8 theoretical compute เร็วกว่า Nvidia H200 NVL ราว 40%**; รันได้ LLM 200–250B parameter ต่อ GPU; max 8 cards ต่อ node สำหรับ scale-out — ครอบคลุม SLM/MLM/LLM inference + RAG pipeline
- Position ของ AMD: เปิดศึก enterprise AI inference ที่ "Tier 2" — ลูกค้าที่ "อยากรัน LLM on-prem แต่ไม่พร้อมลงทุน HGX/NVL72 rack"; ครั้งแรกที่ AMD ออก PCIe Instinct ตั้งแต่ MI210 ปี 2022 — signal ว่าตลาด agentic inference โตจน "ขั้น mid-market" ขายได้แล้ว

## เกิดอะไรขึ้น

วันที่ 7 พ.ค. 2026 AMD ประกาศ Instinct MI350P PCIe — accelerator card สำหรับ enterprise AI ในรูป dual-slot air-cooled PCIe ออกแบบเฉพาะให้ "drop in" กับ standard server ที่ enterprise มีอยู่แล้ว ไม่ต้องเปลี่ยน power supply, cooling system, หรือ rack architecture (10.5 นิ้ว, 600W envelope, fanless cooling อาศัย airflow ของ chassis) Spec ของ chip: 128 compute units, **144GB HBM3E memory** ต่อ card — มากกว่า H200 NVL ของ Nvidia (141GB HBM3E) เล็กน้อย — และ Tom's Hardware รายงานว่า FP16 + FP8 theoretical compute เร็วกว่า H200 NVL ประมาณ 40% สำหรับ workload inference

Use case ที่ AMD push หนักที่สุดคือ **agentic AI inference + RAG pipeline** — workload ที่ enterprise CIO ต้องรัน 24/7 และต้องการ throughput สูง โดย latency พอใช้ MI350P รัน LLM ขนาด 200–250B parameter ต่อ GPU ได้ — ครอบคลุม Llama 3 70B, Mixtral 8x22B, DBRX 132B ทั้งหมดในตัวเดียว max scale คือ 8 card ต่อ node — ซึ่งหมายความว่า standard 2U/4U server ที่ติด PCIe slot 8 ช่อง สามารถรัน 1.5–2 trillion parameter ของ aggregated capacity ได้ หรือ shard model ขนาด 400B parameter ลงในเครื่องเดียว

จุดที่ AMD ตอกย้ำใน press deck: นี่คือ **PCIe Instinct ตัวแรกของ AMD ตั้งแต่ MI210 ปี 2022** — รุ่นต่อมา (MI250, MI300, MI325) ทั้งหมดออกแบบเป็น OAM module สำหรับ liquid-cooled HGX-style rack 8-GPU setup ราคา $200k+ ต่อ node, ลูกค้า hyperscaler / large research lab เท่านั้น MI350P PCIe = AMD ตัดสินใจกลับมาขาย "Tier 2" enterprise — บริษัทที่อยากรัน LLM on-prem แต่งบไม่ถึง HGX/NVL72 rack The Register สรุปตรง ๆ ว่า AMD "takes aim at enterprise AI with PCIe-based Instinct GPUs" — ตลาดที่ Nvidia ครอง H200 NVL อยู่คนเดียวมาตลอด

## ทำไมสำคัญ

Pattern หลัก: **agentic inference = workload ที่ enterprise ยอม invest hardware on-prem** ปี 2024–25 enterprise CIO ส่วนใหญ่เลือก rent compute จาก hyperscaler (Azure OpenAI, AWS Bedrock, Vertex AI) เพราะ workload ของ AI ยังไม่ stable ปี 2026 หลัง Microsoft Work Trend Index ยืนยัน 78% ของ knowledge worker ใช้ agent ทุกสัปดาห์ — workload กลาย stable, cost-per-call ของ frontier API เริ่มเป็น ค่าใช้จ่าย CFO มอง pattern ที่จะเห็น H2 2026: enterprise ขนาด mid-large จะลงทุน on-prem inference cluster เล็ก ๆ (8–32 card) สำหรับ workload ที่ predictable + sensitive (data residency, compliance) — เป็น tier ตรงกลางระหว่าง laptop edge inference กับ hyperscaler cloud MI350P PCIe = ตอบโจทย์นี้ตรงตัว

นัยที่สอง: **ราคา BoM ของ on-prem inference จะเริ่ม commoditize** เมื่อมี alternative ของ Nvidia ที่ drop-in ได้ใน server เดิม + ราคาคาดการณ์ลด 30–40% จากการ skip OAM premium + ไม่ต้อง redesign rack — TCO ของ on-prem inference จะลดลงเร็วใน 18 เดือน เปรียบเทียบกับ trajectory ของ enterprise SSD เมื่อเข้า PCIe form factor ปี 2018 (จาก enterprise-only เป็น mid-market ใน 24 เดือน) Nvidia H200 NVL ไม่มี alternative มาก่อน, การออก MI350P เป็น first credible Tier-2 alternative — Nvidia จะถูกบีบให้ออก H200 PCIe variant ใน 6–12 เดือน เพื่อกัน market share

นัยที่สาม: **enterprise CIO เริ่มมีอำนาจต่อรองคืน** ที่ Anthropic/OpenAI/Google ผูก compute deal ระดับ $200B (Anthropic-Google) / $300B (OpenAI consortium) ดูใหญ่ที่สุดในประวัติศาสตร์ — แต่ enterprise CIO ที่อยากรัน agent ที่ไม่ใช่ frontier model ในเครื่องของตัวเอง จะมี option จริงใน Q3 ปี 2026 — Llama 4, Nemotron 3 Super, DBRX-Next, Mistral Large 3 บน MI350P 8x ที่อยู่ใน server room ของ enterprise เอง — leverage in negotiation กับ hyperscaler / frontier API vendor เพิ่มขึ้นทันที

## มุม OpenBridge

OpenBridge อ่าน 3 ทางจากข่าวนี้ทันที (1) **Build "OpenBridge On-Prem Edition" ที่ตอบ MI350P workload** — ลูกค้า Thai Fortune 500 (โดยเฉพาะ regulated — ธนาคาร, telco, public sector) ที่ต้องรัน agent on-prem ด้วย data residency จะซื้อ MI350P 8x rack ใน Q3–Q4 2026 OpenBridge ที่มี deployment mode "on-prem in customer's VPC" + connector ที่ talks กับ MI350P-hosted Nemotron/Llama จะกลายเป็น default; pricing แพงกว่า cloud edition 30–50% justified โดย sovereignty (2) **Develop "agentic inference cost calculator"** — เครื่องมือที่ลูกค้า input workload (calls per day, average tokens, model size) แล้ว OpenBridge แสดง TCO comparison ระหว่าง Bedrock/Azure OpenAI (rent) vs MI350P 8x on-prem (own); ตัวเลขที่ลูกค้าเอาไป board meeting ได้ — sales tool ที่ทำลายข้อโต้แย้ง "cloud cheaper than on-prem" ใน 2 นาที (3) **Partnership กับ Thai server integrator (Stream, AIS Cloud, NTT, true)** ที่จะขาย MI350P-based AI server — bundle OpenBridge เป็น default software layer; ขาย "AI server + OpenBridge agent platform + connector pack" เป็น turnkey solution ราคาเดียว — vertical SI play ที่ shortcut sales cycle 6 เดือน

Adjacent insight: ที่ AMD ออก MI350P + เป้า Tier 2 enterprise = signal ว่า "agentic inference market เริ่มเข้าขั้นที่ขายได้ที่ mid-market" — ปี 2025 ตลาดนี้ขายได้เฉพาะ hyperscaler + frontier lab; ปี 2026 enterprise ขนาดกลาง 500–5,000 พนักงานเริ่ม afford on-prem inference rack OpenBridge ควรปรับ ICP ให้กว้าง — จาก "regional bank only" เป็น "regulated enterprise + manufacturer + retailer ขนาดกลาง" — pipeline ใหญ่ขึ้น 5–10 เท่า

## Sources
- [AMD Launches Instinct MI350P PCIe GPUs | TechPowerUp](https://www.techpowerup.com/348856/amd-launches-instinct-mi350p-pcie-gpus)
- [AMD announces MI350P PCIe AI accelerator card with 144GB of HBM3E — roughly 40% faster in FP16 and FP8 theoretical compute compared to Nvidia's H200 NVL competitor | Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/amd-announces-mi350p-pcie-ai-accelerator-card-with-144gb-of-hbm3e-roughly-40-percent-faster-in-fp16-and-fp8-theoretical-compute-compared-to-nvidias-h200-nvl-competitor)
- [AMD takes aim at enterprise AI with PCIe-based Instinct GPUs | The Register](https://www.theregister.com/ai-and-ml/2026/05/07/amd-takes-aim-at-enterprise-ai-with-pcie-based-instinct-gpus/5231481)
- [AMD Instinct MI350P: Enterprise PCIe AI Inference Returns to Standard Servers | StorageReview](https://www.storagereview.com/news/amd-instinct-mi350p-enterprise-pcie-ai-inference-returns-to-standard-servers)
- [AMD Targets Enterprise AI Inference Deployment | Jon Peddie Research](https://www.jonpeddie.com/news/amd-targets-enterprise-ai-inference-deployment/)

---

## Audio script
เรื่องสุดท้ายครับโย วันที่ 7 พฤษภาคม AMD ปล่อย Instinct MI350P PCIe accelerator ใหม่ เป็น dual slot air cooled card 128 compute unit 144GB HBM3E memory 600 watt envelope ออกแบบให้ drop in กับ standard server ที่ enterprise มีอยู่แล้ว ไม่ต้องเปลี่ยน power cooling rack อะไรเลย Tom's Hardware รายงานว่า FP16 FP8 compute เร็วกว่า Nvidia H200 NVL 40 เปอร์เซ็นต์ รัน LLM ขนาด 200 ถึง 250 พันล้านพารามิเตอร์ต่อ GPU max 8 card ต่อ node สำหรับ scale out

จุดสำคัญคือ นี่คือ PCIe Instinct ตัวแรกของ AMD ตั้งแต่ MI210 ปี 2022 รุ่นกลางทั้งหมดเป็น OAM module liquid cooled HGX style 200,000 ดอลลาร์ขึ้นต่อ node ขายให้ hyperscaler เท่านั้น MI350P คือ AMD กลับมาขาย Tier 2 enterprise ที่อยากรัน LLM on prem แต่งบไม่ถึง HGX rack The Register บอกตรงว่า AMD takes aim at enterprise AI

Pattern หลักคือ ปี 2026 หลัง Microsoft Work Trend Index ยืนยัน 78 เปอร์เซ็นต์ของ knowledge worker ใช้ agent ทุกสัปดาห์ workload กลาย stable cost per call ของ frontier API เริ่มเป็นค่าใช้จ่ายที่ CFO มอง enterprise mid large จะลงทุน on prem inference cluster เล็กในครึ่งหลังปีนี้ MI350P PCIe ตอบโจทย์ตรงตัว และ Nvidia จะถูกบีบให้ออก H200 PCIe variant ใน 6 ถึง 12 เดือนเพื่อกัน market share

มุม OpenBridge สามเรื่อง หนึ่ง build OpenBridge On Prem Edition สำหรับ MI350P workload ลูกค้า Thai Fortune 500 ธนาคาร telco public sector ที่ต้อง data residency จะซื้อ MI350P rack ใน Q3 Q4 OpenBridge ที่ deploy ใน VPC ลูกค้าได้กลายเป็น default pricing แพงกว่า cloud edition 30 ถึง 50 เปอร์เซ็นต์ justified ด้วย sovereignty สอง develop agentic inference cost calculator ลูกค้า input workload เห็น TCO เปรียบ Bedrock vs MI350P on prem นำเข้า board meeting สาม partner กับ Thai server integrator Stream AIS NTT ขาย AI server บวก OpenBridge เป็น turnkey shortcut sales cycle 6 เดือนครับ
