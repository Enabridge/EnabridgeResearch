---
date: 2026-04-26
slug: google-40b-anthropic-tpu-compute
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: Editorial illustration of two giant interlocking gears made of glowing circuit boards, one tinted deep blue and the other amber, with thin streams of light pouring from one gear into the other across a dark backdrop, minimal flat geometric shapes, dramatic rim lighting, no text no logos no faces
image: images/26-04-26-0622-01-google-40b-anthropic-tpu-compute.png
---

# Google ทุ่ม $40B เข้า Anthropic — $10B เงินสดทันที + $30B ผูก performance, 5GW TPU 5 ปี: สัปดาห์เดียว Anthropic ล็อก $65B / 10GW จาก 2 hyperscaler

## TL;DR
- **24 เม.ย.** Bloomberg/CNBC/TechCrunch ยืนยัน Google ลงทุน Anthropic เพิ่ม **up to $40B** — แบ่งเป็น **$10B เงินสดทันที** ที่ valuation **$350B** + **$30B แบบ performance-locked** ถ้าทำเป้าได้
- **5GW TPU compute** เพิ่มอีก 5 ปี (เดิมประกาศ 3.5GW ใน Broadcom filing) — Anthropic confirm "**1GW Trainium2/3 capacity by end of 2026**" ใน Amazon track พร้อมกัน
- รวมกับ Amazon $25B (20 เม.ย., $5B now + $20B milestone) สัปดาห์เดียว Anthropic ได้ **$65B equity capital + 10GW reserved compute**; ARR $9B (ปลายปี 2025) → **$30B (มี.ค. 2026)** = **3.3x in 4 months**
- Signal: hyperscaler dual-bet pattern กลายเป็น norm — **AWS + Google cofinance Claude** เพื่อทำให้ OpenAI ไม่ผูกขาด Microsoft; Anthropic ขายตำแหน่ง "Switzerland frontier model" ให้ทั้งสองค่ายแล้วเก็บ compute commitment ทับซ้อน

## เกิดอะไรขึ้น

วันศุกร์ที่ 24 เม.ย. ตอนเช้าตามเวลานิวยอร์ก Bloomberg ปล่อยข่าวที่ตลาดรอมาตั้งแต่กลางสัปดาห์ — **Alphabet กำลังจะลงทุน Anthropic เพิ่มอีก up to $40B** หลังเพิ่งให้ Anthropic เข้าถึง 1M TPU เมื่อปลายปีที่แล้ว. ดีล structure แปลกเป็นพิเศษ: **$10B จ่ายทันทีเป็นเงินสด** ที่ post-money valuation **$350B** เพื่อรองรับการขยาย compute footprint ของ Anthropic, อีก **$30B จะตามมาแบบ tranched** ก็ต่อเมื่อ Claude maker ทำเป้า "performance milestones" บางอย่างได้ — ซึ่งทั้งสองฝ่ายไม่เปิดเผยตัวเลข แต่ TechCrunch ระบุเป็น mix ของ revenue ramp + model capability disclosure

ที่สำคัญพอ ๆ กัน คือ Google Cloud ยอม commit **5 gigawatts ของ TPU capacity เพิ่มอีก 5 ปี** — ขยายต่อจากดีลเดิมที่ Anthropic เคยประกาศ "multiple gigawatts of TPU" จะเริ่ม online ปี 2027 (Broadcom filing ระบุเฉพาะตัวเลข 3.5GW). ดีลใหม่ขยับตัวเลขที่ commit ไปเป็น **5GW dedicated TPU + room to scale**. รวมกันแล้ว Anthropic จะมี hyperscaler-class compute ที่ Google ดูแลให้ตั้งแต่ปลายปี 2027 — **เพียงพอ train โมเดลขนาด GPT-7-class โดยไม่พึ่ง NVIDIA H100/B200 เลยก็ได้**

จังหวะตลกของอุตสาหกรรมคือดีลนี้มาห่างจาก **ดีล Amazon เพียง 4 วัน**. วันจันทร์ที่ 20 เม.ย. AWS ประกาศ "up to $25B" เข้า Anthropic — $5B ทันทีที่ valuation **$380B** (สูงกว่า Google โดดเดียวด้วยเหตุผลที่ AWS เปิดดีลก่อน Google compete) + $20B ผูกกับ "commercial milestones". ของแถมที่ Anthropic ตกลงจ่ายให้ AWS: **commit สั่งซื้อ AWS service เกิน $100B ใน 10 ปี** + เริ่มใช้ **Trainium2 + Trainium3 รวม 1GW ภายในสิ้นปี 2026**, มี Graviton **tens of millions of cores** เป็น CPU layer. รวมกับ Google = **10GW reserved capacity / $65B equity** ในสัปดาห์เดียว

CFO Anthropic เปิดประโยคที่ตลกที่สุดไว้ใน Monday press release: "ความต้องการของ developer และ enterprise พร้อม **'sharp rise' in consumer usage** ทำให้เกิด **'inevitable strain' on infrastructure** ที่กระทบ reliability และ performance" — แปลตรงเลยคือ "Claude เซิร์ฟไม่ทันแล้ว เราต้องการเงินและ chip ก่อนจะเสีย market share". The Information รายงานสัปดาห์ที่แล้วว่า ARR ของ Anthropic ขึ้นจาก ~$9B ปลายปี 2025 เป็น **$30B+ ในเดือน มี.ค. 2026** — **เกือบ 3.3x ใน 4 เดือน** หลัก ๆ มาจาก Claude Code + Opus 4.6/4.7 ที่ดูดดีลใหญ่จาก Microsoft Copilot. ตัวเลขนี้คือเหตุผลที่ valuation $350-380B จึง "ไม่บ้า" ในสายตา Amazon/Google: P/S ~12x ยัง cheaper กว่า OpenAI ที่ $852B / $25B ARR

ฝั่ง Google มี dual-purpose obvious. หนึ่ง — รักษา **Anthropic เป็นลูกค้า TPU ระยะยาว** ที่ใช้กำลังการผลิต TPU v7 ที่กำลังจะ ramp. สอง — **ดักไม่ให้ OpenAI ครอบครองตลาด frontier model alone** เพราะถ้า OpenAI ผูก Microsoft ฝ่ายเดียว Google จะไม่มี frontier model partner ที่ scale ได้นอกจาก Gemini. สาม — DOJ antitrust case ของ Google ยังเปิดอยู่; **การ co-fund competitor** เป็น defensive narrative ที่ "Google ไม่ได้ผูกขาด AI" สำคัญในการต่อรอง

## ทำไมสำคัญ

**เกมเปลี่ยนจาก compute-as-cost ไปเป็น compute-as-equity-instrument**. ก่อน 2025 ดีล cloud-AI ปกติคือลูกค้าจ่าย usage fee, ผู้ขาย cloud ลด price บ้างตามขนาด. **2026 deal pattern ใหม่** = AWS/Google ทำ **"compute lend-lease"** กับ frontier model lab — ให้ทั้ง equity และ compute commitment ทับซ้อน, เก็บ revenue กลับผ่าน obligation purchase ($100B over 10 years สำหรับ AWS). ทุกฝ่ายได้ optic ที่ต้องการ: Anthropic ได้ compute ราคา below-market + buffer งบ R&D; cloud provider ได้ revenue ระยะยาว lock-in + ป้องกัน customer migration

**Pattern dual-bet ของ Anthropic คือ master class ของ negotiation**. ปกติแล้ว frontier model lab จะเลือก "primary cloud partner" คนเดียว (OpenAI–Microsoft, xAI–Oracle/Microsoft) เพื่อ optimization และ commitment. Anthropic เลือกตรงข้าม: **ขาย "Switzerland frontier model" position** ให้ AWS และ Google พร้อมกัน — แต่ละค่ายกลัวอีกฝ่ายผูกขาด เลยยอมจ่ายแพงกว่าเพื่อรักษา exposure. ผลคือ Anthropic **เก็บ compute commitment ซ้อนทับ** (10GW เกินที่ใช้จริงในระยะ 3 ปี) พร้อม optionality สูง — ถ้า Trainium ramp ช้า ก็ใช้ TPU แทน, vice versa

แต่จุดเปราะคือ **Anthropic ต้องทำ "performance milestone" ให้ได้สำหรับ $30B + $20B ที่ผูกอยู่**. ดีล tranched แบบนี้บีบให้ Anthropic ต้อง ship Claude Opus 4.8/5.0 + Claude Agent Runtime ภายใน 6-12 เดือน ให้ tangible enough จนกล่อง escrow เปิดได้. นี่คือ pressure ที่ explain ทำไม Anthropic เพิ่งปล่อย Opus 4.7 (16 เม.ย.) แล้วยังต้องเร่ง — **survival math เดียวกับที่ OpenAI เผชิญตอน GPT-5.5**, แค่จังหวะถัดไป

**Bet ของเรา**: ภายในสิ้นปี 2026 จะมี **deal เพิ่มอีก 1-2 รายระหว่าง hyperscaler-frontier model lab** ที่มี compute commitment ทับซ้อน — น่าจะเป็น **Microsoft–xAI** (Microsoft ต้อง diversify หลัง OpenAI exclusivity expire ม.ค. 2027) หรือ **Oracle–Mistral** (Oracle ต้องการ EU positioning + Mistral ต้องการ scale). ตลาดจะแยกเป็น 4-5 frontier lab × 3 hyperscaler grid ที่ทุกคู่จะมี dual-funding ภายใน 18 เดือน. **valuation $300-400B** จะเป็น new "sub-trillion frontier" tier (OpenAI $852B = trillion tier เดียว Anthropic ตอนนี้)

## มุม OpenBridge

**ไม่ direct เกี่ยว แต่ implication ใหญ่กับ pricing strategy**. ถ้า Anthropic ARR ทะลุ $30B และ Claude Opus 4.7/4.8 capacity เพิ่มขึ้น 2-3x ในไตรมาสนี้ (จาก 1GW Trainium online สิ้นปี + TPU expansion), **ราคา Claude API จะ pressure ลงในช่วงครึ่งหลัง 2026**. OpenBridge ควรเตรียม model routing layer ใน workflow engine ภายใน 30 วัน ให้ลูกค้า **switch ระหว่าง Claude / GPT-5.5 / Gemini Flash / Llama-class** ได้แบบ runtime — ถ้า Anthropic ลดราคา 20-30% เพื่อแย่ง market share จาก OpenAI ใน Q3, ลูกค้า OpenBridge ที่ใช้ Claude backend ควรได้ benefit ทันทีโดยไม่ต้อง re-integrate

**Strategic positioning คำถามใหญ่กว่า**: ดีล Google–Anthropic + AWS–Anthropic ทำให้ Claude เป็น **"hyperscaler-blessed second model"** ในทุก major cloud (Google Cloud Vertex, AWS Bedrock, Microsoft Foundry — Anthropic Claude อยู่ทั้ง 3). OpenBridge ที่ทำ B2B agent platform ใน Thailand จะเจอ **enterprise procurement ที่ default ไปที่ "ใช้ Claude เพราะ Google Cloud bundle ให้"** มากขึ้น. คำตอบคือ **อย่าเสียเวลา compete ที่ raw model layer** — focus ที่ Thai SaaS connector + LINE OA integration + revenue attribution ที่ hyperscaler ไม่แข่ง. ถ้าลูกค้าอยากใช้ Claude/GPT/Gemini = OpenBridge ใช้ทั้ง 3 ผ่าน routing — ขายแค่ orchestration + integration layer

**Action item 14 วัน**: (1) ออก **"BYO-LLM" pricing tier** ที่ลูกค้าเอา Claude/GPT/Gemini API key มาเอง, OpenBridge เก็บค่า orchestration อย่างเดียว — undercuts hyperscaler bundle 30-40% สำหรับลูกค้าที่มี cloud commit อยู่แล้ว (Krungsri, KBank, SCB ที่มี enterprise agreement กับ Google Cloud). (2) **Track Claude Opus 4.7 Bedrock latency vs Claude.ai direct** — ถ้า Bedrock ช้ากว่า 30%+ บอก enterprise ลูกค้าให้ใช้ direct API ผ่าน OpenBridge แทน. (3) เริ่ม **track Anthropic Q2 earnings (มิ.ย.)** เพื่อดู disclosure ของ "performance milestone" ที่ผูกกับ Google $30B — ถ้า Anthropic miss = compute slowdown ใน Q3 = OpenAI/Google โอกาสกินส่วนแบ่ง = window สำหรับ OpenBridge เปลี่ยน default backend

## Sources
- [Google Plans to Invest Up to $40 Billion in Anthropic (Bloomberg)](https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic)
- [Google to invest up to $40 billion in Anthropic as search giant spreads its AI bets (CNBC)](https://www.cnbc.com/2026/04/24/google-to-invest-up-to-40-billion-in-anthropic-as-search-giant-spreads-its-ai-bets.html)
- [Google to invest up to $40B in Anthropic in cash and compute (TechCrunch)](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [Google's $40B Anthropic move is Big Tech's latest huge AI bet (Axios)](https://www.axios.com/2026/04/24/google-amazon-anthropic-investment)
- [Amazon to invest up to another $25 billion in Anthropic as part of AI infrastructure deal (CNBC)](https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html)
- [Amazon expands Anthropic partnership with $25 billion investment (CloudComputing News)](https://www.cloudcomputing-news.net/news/amazon-anthropic-25-billion-investment/)

---

## Audio script
วันศุกร์ที่ยี่สิบสี่เมษา ตอนเช้านิวยอร์ก Bloomberg ปล่อยข่าวที่ตลาดรอตั้งแต่กลางสัปดาห์. Alphabet จะลงทุน Anthropic เพิ่มอีก up to สี่สิบ billion. แบ่งเป็นสิบ billion เงินสดทันที ที่ valuation สามร้อยห้าสิบ billion. อีกสามสิบ billion ตามมาแบบ performance locked ถ้า Anthropic ทำเป้าได้.

ที่สำคัญพอ ๆ กัน Google Cloud ยอม commit ห้า gigawatt ของ TPU capacity เพิ่มอีกห้าปี. ขยายจากดีลเดิมที่ Broadcom filing ระบุไว้สามจุดห้า gigawatt. รวมกัน Anthropic จะมี hyperscaler class compute เพียงพอ train โมเดลขนาด GPT เจ็ด คลาส โดยไม่พึ่ง NVIDIA เลยก็ได้.

จังหวะตลกคือดีลนี้ห่างจาก Amazon เพียงสี่วัน. วันจันทร์ที่ยี่สิบเมษา AWS ประกาศ up to ยี่สิบห้า billion เข้า Anthropic. ห้า billion ทันทีที่ valuation สามร้อยแปดสิบ billion. อีกยี่สิบ billion ผูก commercial milestone. แลกกับ Anthropic commit สั่ง AWS service เกินหนึ่งร้อย billion ในสิบปี และใช้ Trainium สอง สาม รวมหนึ่ง gigawatt ภายในสิ้นปี.

รวมกัน Google บวก Amazon ในสัปดาห์เดียว Anthropic ได้หกสิบห้า billion equity บวกสิบ gigawatt reserved compute. ARR ขึ้นจากเก้า billion ปลายปีที่แล้ว เป็นสามสิบ billion ในมีนา. เกือบสามจุดสามเท่าในสี่เดือน หลัก ๆ จาก Claude Code และ Opus.

CFO Anthropic เขียนใน press release ว่า ความต้องการ developer enterprise และ sharp rise in consumer usage ทำให้เกิด inevitable strain on infrastructure กระทบ reliability และ performance. แปลตรงคือ Claude เซิร์ฟไม่ทันแล้ว ต้องการเงินและ chip ก่อนเสีย market share.

pattern dual bet ของ Anthropic คือ master class ของ negotiation. ปกติ frontier lab เลือก primary cloud partner คนเดียว. Anthropic ขายตำแหน่ง Switzerland frontier model ให้ AWS กับ Google พร้อมกัน. แต่ละค่ายกลัวอีกฝ่ายผูกขาด ยอมจ่ายแพงเพื่อรักษา exposure. Anthropic เก็บ compute commitment ซ้อนทับเกินที่ใช้จริงในสามปี.

จุดเปราะคือ Anthropic ต้องทำ performance milestone ให้ได้สำหรับสามสิบ บวกยี่สิบ billion ที่ผูกอยู่. บีบให้ต้อง ship Claude Opus สี่จุดแปดหรือห้าจุดศูนย์ บวก Claude Agent Runtime ภายในหกถึงสิบสองเดือน. survival math เดียวกับ OpenAI ตอน GPT ห้าจุดห้า แค่จังหวะถัดไป.

สำหรับ OpenBridge ไม่ direct เกี่ยวแต่ implication ใหญ่. ถ้า Anthropic capacity เพิ่มสองสามเท่า ราคา Claude API จะ pressure ลงครึ่งหลังปี. OpenBridge ควรเตรียม model routing layer ภายในสามสิบวัน ให้ลูกค้า switch ระหว่าง Claude GPT Gemini Llama แบบ runtime.

Strategic position คำถามใหญ่กว่า. Claude เป็น hyperscaler blessed second model ในทุก major cloud. OpenBridge เจอ enterprise procurement default ไปใช้ Claude เพราะ bundle. คำตอบคือ อย่าเสียเวลา compete ที่ raw model layer focus ที่ Thai SaaS connector LINE OA integration และ revenue attribution ที่ hyperscaler ไม่แข่ง.

Action สิบสี่วัน หนึ่ง ออก BYO LLM pricing tier ลูกค้าเอา API key มาเอง OpenBridge เก็บค่า orchestration อย่างเดียว undercuts hyperscaler สามสิบ สี่สิบเปอร์เซ็นต์. สอง track Claude Bedrock latency vs Claude direct ถ้าช้ากว่าสามสิบเปอร์เซ็นต์ บอกลูกค้าใช้ direct API ผ่าน OpenBridge. สาม track Anthropic Q สอง earnings มิถุนา ดู disclosure performance milestone ถ้า miss คือ window OpenBridge เปลี่ยน default backend
