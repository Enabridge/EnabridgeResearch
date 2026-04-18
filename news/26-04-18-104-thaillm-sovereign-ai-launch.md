---
date: 2026-04-18
slug: thaillm-sovereign-ai-launch
topic: openbridge-trend
reading_time_min: 5
sources: 4
depth: deep
---

# ไทยเปิด "ThaiLLM" sovereign AI แห่งชาติ — KBTG + SCB 10X ใช้งานจริง, สัญญาณ agent ไทยมี foundation แล้ว

## TL;DR
- รัฐบาลไทย (กระทรวง อว. + NECTEC + พาร์ทเนอร์) เปิด **ThaiLLM** sovereign AI model ปลายมีนาคม-ต้นเมษายน 2026 ฟรีสำหรับทุกคน, มี 2 ขนาด, playground + API + download weights ที่ thaillm.or.th
- **KBTG** (THaLLE) และ **SCB 10X** (Typhoon) เริ่ม integrate เข้างานจริงแล้ว; Typhoon 2 มี multimodal (audio + vision) + agentic capability ผ่าน RAG/multi-agent workflow
- Signal ชัด: **ไทยมี "foundation layer" ภาษาไทยของตัวเอง** ทำให้ agent ไทยไม่ต้องพึ่ง GPT/Claude 100% — ตลาด vertical agent ไทยเริ่มเกิดขึ้นได้จริง

## เกิดอะไรขึ้น

กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม (อว.) ร่วม NECTEC + DEF (Digital Economy and Society Development Fund) + เอกชนไทย เปิด **ThaiLLM** เป็น AI foundation แห่งชาติ ปลายมีนาคม-ต้นเมษายน 2026 วางตัวเป็น "sovereign AI" สำหรับภาษาและวัฒนธรรมไทย

**ของที่ปล่อยออกมา:**
- 2 ขนาด model (ยังไม่เปิดพารามิเตอร์ชัด แต่แนวทาง NECTEC ระบุใช้ foundation จาก Pathumma + OpenThaiGPT + Typhoon + THaLLE)
- **Playground public** ที่ thaillm.or.th ทดลองฟรี
- **API developer** ฟรี
- **Weight download** สำหรับ fine-tune ใน environment ของตัวเอง

**นักเล่นระดับ corporate ที่ integrate จริงแล้ว:**
- **SCB 10X** — Typhoon 2 (5 model sizes, multimodal audio + vision, agentic via RAG/multi-agent workflow) ใช้ Gemma 3 12B เป็น base เพิ่มประสิทธิภาพภาษาไทย
- **KBTG** — THaLLE (KBTG's own Thai LLM) integrate เข้าโปรเจกต์ภายใน; KXVC (KBTG's VC arm) ประกาศ strategic partnership เพื่อ scale AI startup ไทย
- **SCBX + OPDC** — Typhoon ใช้กับ AI chatbot ภาครัฐ pilot

**Training ecosystem:** ตั้งแต่ปลายปี 2025 มี >700 นักศึกษา/นักวิจัยไทยเข้า bootcamp ThaiLLM ตั้งแต่พื้นฐานจนถึงการพัฒนา advanced

ช่วงเดียวกัน (ม.ค. 2026) **Google Cloud เปิด region ใหม่ที่ไทย** — pipeline infra crypto สำคัญสำหรับ enterprise ไทยที่ต้อง data residency compliance

## ทำไมสำคัญ

นี่คือ **"moment that matters" สำหรับ Thai AI ecosystem** ในรอบ 10 ปี สิ่งที่เปลี่ยน:

1. **Foundation layer ไทยเลิกพึ่ง GPT/Claude 100%** — ถึงแม้ quality ยัง behind แต่สำหรับ agent ที่ทำงานภาษาไทย (KYC document, contract review, call center) cost ต่ำกว่า + data residency ใน TH ราคาและ compliance ชนะ

2. **Bank + telco + gov align พร้อมกัน** — SCB 10X + KBTG + AIS NEXT + OPDC ใช้ ThaiLLM foundation ร่วม นี่คือ unique ของไทย — ในอเมริกา bank ใช้คนละ model, ของไทยมี common ground ที่ทำให้เกิด partnership เชิง data sharing/fine-tune ได้

3. **Typhoon 2 agentic capability** — SCB 10X ระบุชัดว่า Typhoon ใช้ใน RAG framework และ multi-agentic workflow ได้ ไม่ใช่แค่ chatbot; แปลว่า **"Thai agent stack"** เริ่มมี component ครบ (model + orchestration + domain data)

4. **Policy tailwind** — รัฐบาลลงทุน + DEF funding + 700 คน trained = ไม่ใช่ PR stunt; มี ecosystem building ต่อเนื่อง

## Competitive landscape

**ใครได้ประโยชน์:**
- **SCB 10X** — first-mover advantage ใน Thai AI; Typhoon เป็น de-facto Thai LLM standard; portfolio startup ที่ลงทุนจะ leverage ได้
- **KBTG / KXVC** — same playbook คนละ angle; financial services vertical
- **Thai AI startup ที่สร้างบน ThaiLLM** — เข้าถึง weights + API ฟรี, ไม่ต้องจ่าย OpenAI $0.02/1K token
- **Google Cloud Thailand** — cloud region ใหม่ได้ enterprise workload; partnership กับ ThaiLLM ตรง ๆ
- **นักศึกษา/นักวิจัยไทย** — 700+ คน trained แล้ว เริ่มเห็น Thai AI engineer supply ที่ international market ต้องการ

**ใครถูก disrupt:**
- **OpenAI/Anthropic enterprise sales ในไทย** — ลูกค้ากลางเล็กจะใช้ ThaiLLM + fine-tune แทน; ต้องเหลือแค่ use case top-tier reasoning
- **Consulting/integrator ไทย** ที่ขาย "GPT wrapper" เป็น main service — ต้องย้ายไป integration ระดับลึก หรือ domain expertise
- **Translation/localization service** — agent ที่เข้าใจไทย native จะกินส่วนงาน routine translation

**Moat analysis:**
- **Model moat ของ ThaiLLM** ไม่ใช่ benchmark (ยังต่ำกว่า GPT-4o) แต่คือ **Thai data moat + data residency** ซึ่งเขียนไว้ในกฎเกณฑ์ภาครัฐ → enterprise ที่ regulated ไม่มีทางเลือก
- **Typhoon moat:** SCB 10X มี financial services dataset ที่ fine-tune แล้ว, คู่แข่งไทยอื่นไม่มี
- **ความเสี่ยง:** ถ้า Google/Microsoft ออก Thai-optimized model ฟรี (เหมือน Gemma-Thai) หรือ Apple Intelligence รองรับไทย, moat หายไปครึ่ง

## Entrepreneur's take

5 ช่องว่างที่ **ไทยเปิดแล้ว** จากการมี ThaiLLM foundation:

1. **Vertical Thai agent สำหรับอุตสาหกรรมที่ regulated** — ประกันภัย, โรงพยาบาล, กฎหมาย, ราชการ, การศึกษา — ที่ต้อง data residency + ภาษาไทย + compliance ลูกค้ายอมจ่าย enterprise price ($10K–$100K/ปี) เพราะไม่มีทางเลือก OpenAI

2. **"OpenBridge for Thai business"** — integration platform ไทยที่ connect SaaS ไทย (FlowAccount, Peak, Builk, Page365) + ThaiLLM agent → ตรงนี้คือ thesis หลักของ OpenBridge อยู่แล้ว

3. **Call center agent ภาษาไทย** — Typhoon 2 audio support แปลว่า speech-to-speech Thai agent ทำได้ ตลาด BPO/call center ไทยใหญ่, unit economics ดี

4. **Agentic RPA สำหรับเอกสารไทย** — สัญญา, ใบเสร็จ, ภพ.30, ภงด — OCR + understanding + action; Typhoon OCR + agent workflow = ชุด SKU ที่ SME ไทยจ่ายได้

5. **Training + certification service** — 700 คน trained ยังน้อยไป; bootcamp / corporate training / certification สำหรับ enterprise ที่อยาก deploy ThaiLLM เอง — มี business unit economics ดี low capex

**Warning:** อย่าแข่งสร้าง "Thai LLM ตัวใหม่" — รัฐลงทุนแล้ว, SCB/KBTG ลงทุนแล้ว, field ปิดสำหรับ startup รายเล็ก ให้เล่น **application + vertical + distribution** แทน

## Risks & ของที่ press release ไม่ได้บอก

- **Technical:** ThaiLLM benchmark ยังต่ำกว่า GPT-4o, Claude 4 — สำหรับ agent ที่ต้อง complex reasoning (legal, medical diagnosis) ยังไม่พร้อม production solo; ต้อง hybrid กับ frontier model
- **Business:** DEF funding เป็น government grant — ถ้าปี 2027 รัฐบาลเปลี่ยนหรือ priority เปลี่ยน, continuity project เสี่ยง; sustainability funding model ยังไม่ชัด (ฟรีตอนนี้ แต่ scale API cost ใครจ่าย?)
- **Compliance:** PDPA ไทยยังไม่ชัดเจน 100% เรื่อง training data sourcing — ThaiLLM train บน corpus อะไร? ถ้ามี Thai copyrighted text (ข่าวหนังสือพิมพ์, หนังสือ) อาจเจอฟ้องเหมือน NYT vs OpenAI
- **Ecosystem fragmentation:** Pathumma + OpenThaiGPT + Typhoon + THaLLE ยังไม่ converge; developer ต้องเลือก stack เสี่ยง lock-in ที่ทำงานไม่ได้ cross-model
- **ของที่ไม่พูด:** ไม่มีตัวเลข DAU/MAU playground; ไม่มี API call volume; **traction จริงหรือเป็นแค่ภาพ launch?** คำถามสำคัญที่ยังไม่มีคำตอบ

## Historical parallel

**Wave ที่ตรงสุด: France's Mistral / Germany's Aleph Alpha 2023–2024** — Mistral ได้รัฐบาล backing + enterprise partnership + ระดมทุน €2B+; แต่ Aleph Alpha ไม่สามารถ scale ได้เทียบ จุดต่าง: **founder quality + open-source strategy + commercial discipline** ThaiLLM ต้องเรียนจาก Mistral ไม่ใช่ Aleph Alpha

**Wave ก่อน: South Korea Naver HyperCLOVA 2021** — เกาหลีลงทุน sovereign AI ก่อน, ยังใช้ในประเทศแต่ไม่ break ออกตลาดภูมิภาค; ไทยต้องคิดตั้งแต่วันแรกว่า ThaiLLM จะ serve แค่ไทย หรือขยายไป Cambodia/Laos/Myanmar (ASEAN LLM thesis)?

**Wave เก่ากว่า: National software initiatives 1990s–2000s** ของ Japan (TRON), France (Minitel) — ส่วนใหญ่ล้มเพราะไม่ compete ในตลาดเปิด; ที่ต่างของ AI ยุคนี้คือ **open-weights = global developer access** ถ้า ThaiLLM เปิด weights + license ถูก developer ต่างชาติจะ contribute

**Lesson:** sovereign AI ที่ชนะต้อง **(1) open-source + permissive license (2) enterprise partnership ต่อเนื่อง (3) founder-led/operator-led ไม่ใช่ bureaucrat-led** ThaiLLM มีสัญญาณ (1) และ (2) แล้ว; (3) ยังต้องดู

## มุม OpenBridge
- **Thesis validation สำหรับ OpenBridge:** ไทยมี foundation ภาษาไทยแล้ว + enterprise ไทยเริ่ม integrate → **demand สำหรับ "integration platform + Thai agent"** จะโตไตรมาสนี้; OpenBridge positioning ตรงเลย
- **Action concrete:** ต่อ MCP / integration กับ **Typhoon API** ของ SCB 10X + **THaLLE** ของ KBTG เป็น priority ใน 30 วัน; marketing ชู "OpenBridge + ThaiLLM" เป็น Thai-native agent stack; ยิงเข้า SCB 10X portfolio company เป็น channel แรก
- **Partnership opportunity:** คุย SCB 10X + KXVC โดยตรงในฐานะ co-builder ของ Thai agent ecosystem; offer ลดราคา OpenBridge ให้ portfolio company เพื่อ lock ecosystem adoption

## Sources

**Primary:**
- [Thailand Launches "ThaiLLM": A Sovereign AI Foundation for the Nation — NSTDA](https://www.nstda.or.th/en/news/news-years-2026/thaillm.html)
- [Introducing 'Typhoon 2': Advancing Thai LLMs — SCB 10X](https://www.scb10x.com/en/blog/introducing-typhoon-2-thai-llm)

**Independent verification:**
- [Thailand Develops Production-Grade AI Tools For Real-World Business Applications](https://www.chiangraitimes.com/ai/thailand-builds-production-grade-ai-tools-for-real-business-use/)

**Analysis/Context:**
- [SCB 10X joins AI2 Incubator's $80M Fund III to launch 70 Applied AI startups — The Story Thailand](https://www.thestorythailand.com/en/17/10/2025/164922/)

---

## Audio script
เรื่องที่สี่ เรื่องไทย รัฐบาลไทยโดยกระทรวง อว. ร่วมกับ NECTEC และพาร์ทเนอร์เอกชน เปิดตัว ThaiLLM sovereign AI แห่งชาติ ช่วงปลายมีนาคมถึงต้นเมษายนปีนี้ ฟรีสำหรับทุกคน มี playground ให้ลองที่เว็บ thaillm.or.th มี API ให้ developer และ download weights ไปรันเอง fine-tune เองได้

ที่สำคัญคือ KBTG กับ SCB 10X เริ่ม integrate ของจริงแล้ว SCB 10X มี Typhoon 2 ที่เป็น multimodal รองรับทั้ง audio และ vision และ agentic capability ผ่าน RAG กับ multi-agent workflow KBTG มี THaLLE ของตัวเอง KXVC ซึ่งเป็น VC arm ของ KBTG ประกาศ strategic partnership scale AI startup ไทย พร้อมกันนี้ตั้งแต่ปลายปี 2025 มีนักศึกษาและนักวิจัยไทยมากกว่า 700 คนผ่าน bootcamp ThaiLLM แล้ว

signal ที่ใหญ่สุด คือไทยมี foundation layer ภาษาไทยของตัวเองแล้ว agent ไทยไม่ต้องพึ่ง GPT หรือ Claude ร้อยเปอร์เซ็นต์อีกต่อไป สำหรับงานที่ regulated เช่น ธนาคาร ประกัน โรงพยาบาล ราชการ ที่ต้อง data residency ใน TH — ThaiLLM ชนะเรื่อง compliance เรื่องราคา

มุม entrepreneur มี 5 ช่องที่เปิดแล้ว หนึ่งคือ vertical Thai agent สำหรับอุตสาหกรรม regulated ที่ยอมจ่ายราคา enterprise สองคือ integration platform ไทยที่ connect SaaS ไทยกับ ThaiLLM agent — ตรงนี้คือ thesis OpenBridge อยู่แล้ว สามคือ call center agent ภาษาไทยที่ใช้ Typhoon audio สี่คือ agentic RPA สำหรับเอกสารไทย สัญญา ใบเสร็จ ภพ.30 ภงด ห้าคือ training certification service สำหรับ enterprise ที่อยาก deploy ThaiLLM เอง คำเตือน อย่าแข่งสร้าง Thai LLM ตัวใหม่ รัฐลงทุนแล้ว field ปิดสำหรับรายเล็ก ให้เล่น application layer แทน

ความเสี่ยงที่ต้องรู้ คือ benchmark ThaiLLM ยังต่ำกว่า GPT-4o กับ Claude 4 งาน complex reasoning ยังไม่พร้อม production solo ต้อง hybrid กับ frontier model อีกอันคือ sustainability — ตอนนี้ DEF funding รัฐ ฟรี แต่พอ scale API cost ใครจ่าย ยังไม่ชัด และ ecosystem ยัง fragment Pathumma OpenThaiGPT Typhoon THaLLE ยังไม่ converge

เทียบ pattern ต่างประเทศ ใกล้สุดคือ Mistral ของฝรั่งเศสที่ระดม €2B+ ได้ กับ Aleph Alpha ของเยอรมันที่ scale ไม่ได้ — ความต่างอยู่ที่ founder quality open-source strategy กับ commercial discipline ThaiLLM ต้องเรียนจาก Mistral ไม่ใช่ Aleph Alpha

สำหรับ OpenBridge นี่คือ thesis validation ตรง ๆ demand integration platform บวก Thai agent จะโตไตรมาสนี้ Action คือต่อ MCP กับ Typhoon API ของ SCB 10X และ THaLLE ของ KBTG เป็น priority ใน 30 วัน และคุย SCB 10X กับ KXVC โดยตรงในฐานะ co-builder ของ Thai agent ecosystem ยิง portfolio company เขาเป็น channel แรก แค่นี้สำหรับเรื่องสุดท้าย

สรุปวันนี้ 4 เรื่อง agent OS ฝั่ง consumer ที่ Perplexity นำ, agent orchestration IDE ที่ Windsurf เปิดเกมใหม่, SaaS B2B ใหญ่เริ่มเก็บ metadata เทรน AI ที่ Atlassian จุดไฟ, และไทยมี foundation AI ของตัวเองแล้ว ขอให้วันนี้เป็นวันที่ดีครับ เจอกันใหม่พรุ่งนี้
