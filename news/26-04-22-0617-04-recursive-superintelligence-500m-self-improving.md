---
date: 2026-04-22
slug: recursive-superintelligence-500m-self-improving
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: Editorial illustration of an abstract spiral of gears and neural threads looping back into itself, each revolution slightly larger than the last, minimal flat geometric shapes, muted violet and chartreuse palette, glowing center, soft radial gradient, no text no logos no faces
image:
---

# Recursive Superintelligence ปิด $500M ที่ valuation $4B — lab อายุ 4 เดือนจาก Socher/Rocktäschel, GV + Nvidia นำ, pitch ว่า "AI ที่ train ตัวเอง"

## TL;DR
- **21 เม.ย.** Recursive Superintelligence — AI lab incorporated **31 ธ.ค. 2025** (4 เดือนที่แล้ว) — ปิด **$500M** ที่ **valuation $4B**. GV + Nvidia เป็น anchor, round **oversubscribed เกือบ $1B**
- Founding team: **Richard Socher** (ex-Salesforce Chief Scientist, Einstein AI founder) + **Tim Rocktäschel** (ex-director DeepMind) + Josh Tobin/Jeff Clune/Tim Shi (ex-OpenAI). 20 คน
- Pitch: **"end-to-end self-improving AI"** — automate ทุก step ของ AI research pipeline (eval, data selection, training, post-training, research direction) โดย **ไม่ต้องมี human in the loop**
- Signal: **"model that improves itself" = new bet category ของ frontier lab** — Anthropic/OpenAI ยัง human-in-loop, Recursive ประกาศตัดทิ้ง = contrarian bet ที่ top tier VC ยอมเดิมพัน

## เกิดอะไรขึ้น

วันอังคารที่ 21 เม.ย. — ตรงกับวันที่ Bezos Prometheus ประกาศ round — **Recursive Superintelligence** ประกาศปิด **$500M round ที่ valuation $4B**. GV (Google Ventures) นำร่วมกับ **Nvidia**, round **oversubscribed ไปเกือบ $1B** ตามรายงาน. Lab นี้เพิ่งถูก incorporated ใน **ธ.ค. 2025 — 4 เดือนก่อน** — แปลว่าเส้นทางจาก incorporation ถึง $4B valuation **เร็วที่สุดในประวัติศาสตร์ venture ยุค AI**. เร็วกว่า Anthropic, เร็วกว่า xAI, เร็วกว่า Mistral

Founding team คือ **team ระดับ hall-of-fame ของ AI research**:
- **Richard Socher** — ex-Chief Scientist ของ Salesforce (สร้าง Einstein AI), ex-founder ของ MetaMind (ถูก Salesforce ซื้อ 2016), ex-CEO ของ you.com. คนที่ research + startup operator
- **Tim Rocktäschel** — Professor AI ที่ UCL + ex-director ของ Google DeepMind (ดูแล reasoning + multi-agent research)
- **Josh Tobin** — ex-OpenAI (robotics + simulation)
- **Jeff Clune** — ex-OpenAI (evolutionary AI + open-ended learning)
- **Tim Shi** — ex-OpenAI (agent research)

Total 20 คน. ratio $500M ÷ 20 = **$25M ต่อหัว**. ratio นี้เป็น outlier — Anthropic ในช่วงอายุเดียวกัน ~$5M/head, OpenAI ในช่วงอายุเดียวกัน ~$10M/head

Pitch ของ Recursive — ตามคำของ Socher ใน interview ก่อนหน้านี้ — คือ **"end-to-end self-improving AI"**: automate ทั้ง pipeline ของ AI research — (1) **evaluation** (model ประเมินตัวเอง), (2) **data selection** (model เลือก training data ของตัวเอง), (3) **training** (model update parameters), (4) **post-training** (RLHF + alignment โดย AI), (5) **research direction** (model เลือกว่าจะลองอะไรต่อ) — **โดยไม่ต้อง human in the loop**. นี่คือ thesis contrarian: ขณะที่ Anthropic/OpenAI/Google ยังเน้น "human oversight" เป็น safety layer, Recursive ประกาศตัดทิ้งเพื่อ **compound improvement rate**

## ทำไมสำคัญ

Signal 1 — **"self-improving model" คือ bet ใหม่ที่ top-tier VC ยอมเดิมพันแล้ว**. ก่อนปี 2026 thesis นี้ถูก classify เป็น "AGI-ish speculative" + ไม่มี lab ใหญ่ทำจริง. ตอนนี้ GV + Nvidia (ผู้ถือ infrastructure + ผู้ถือ distribution ของ Alphabet) **เข้าลงทุน $500M** สะท้อนว่า mainstream capital allocator **คำนวณว่า thesis นี้ประเมินได้ + มี asymmetric upside** — แม้ว่าความเสี่ยงคือ 80% model ไม่ converge

Signal 2 — **ratio $25M/head** สะท้อนว่า **talent concentration = key variable** ใน AI frontier lab ตอนนี้. Ilya Sutskever's SSI ราคาประเมิน $20B ที่ 2024 (seed), Thinking Machines ของ Mira Murati ราคาประเมิน $12B ที่ 2025 (seed), Recursive Superintelligence ราคาประเมิน $4B ที่ 4 เดือนอายุ. pattern คือ **VC ปรับ model การประเมิน**: ไม่ใช่ DCF, ไม่ใช่ revenue multiple, ไม่ใช่ model benchmark — คือ **"มีคนระดับ top 50 global researcher กี่คน × premium factor"**. ที่ Recursive มี 5+ คนในนั้น = $500M เป็น "talent deposit" ไม่ใช่ "business investment"

Signal 3 — **Rocktäschel เลิก DeepMind เข้า Recursive ตอนที่ DeepMind มี resource มากที่สุดในประวัติศาสตร์** = **brain drain ของ Big Tech AI lab เร่งขึ้น**. ปีที่แล้วเราเห็น Ilya/Mira/Jan Leike + Dario bros ออก OpenAI; ตอนนี้ Rocktäschel/Clune/Tobin/Shi ออก OpenAI + DeepMind พร้อม ๆ กัน. Talent ไปที่ไหน? **ไปที่ lab ที่ promise "ทำ thesis ที่ Big Tech ไม่ยอมทำ"** — self-improving model ใน Recursive's case, superintelligence-first ใน SSI's case, reasoning frontier ใน Thinking Machines' case. นี่คือเชื้อเพลิงของ **frontier fragmentation**: Big Tech ไม่สามารถ lock top researcher ได้อีกต่อไป

## มุม OpenBridge

**Direct relevance:** ต่ำ. Recursive เล่น frontier research ที่ยังไม่มี product. ไม่ overlap กับ OpenBridge

**แต่ strategic signal 2 ด้าน:**

**(1) Capital reshuffling:** $500M ที่ Recursive + $10B ที่ Prometheus (21 เม.ย. วันเดียวกัน) = **$10.5B flow เข้า AI lab ใน 24 ชั่วโมง**. เมื่อ capital ขนาดนี้เคลื่อน, price ของทั้ง AI ecosystem ปรับขึ้น — รวมไปถึง **Thai AI-adjacent SaaS ที่จะเริ่ม raise ใน Q3-Q4**. OpenBridge ควร lock **term sheet + runway** ในไตรมาสที่ตลาดยัง frothy — ไม่ใช่รอ valuation reset ปลายปี (ถ้ามี). อย่างน้อยเปิด conversation กับ 3-5 local VC + 1-2 regional (Jungle Ventures, Monk's Hill, Openspace) ใน 30 วัน

**(2) Model commoditization acceleration:** ถ้า Recursive thesis ทำงาน (model improves itself) = **model cost curve จะ drop เร็วกว่า exponential ปัจจุบัน**. Implication สำหรับ OpenBridge: AI integration layer ที่สร้างมูลค่าผ่าน "ช่วยเลือก/ควบคุม model" จะ **ลดมูลค่าลง**; ที่สร้างมูลค่าผ่าน **connector specificity + local context** จะยิ่งมีมูลค่า. ยืนยัน thesis ที่ correct ของ OpenBridge: เน้น Thai SaaS connector depth (FlowAccount, PEAK, LINE OA, SCB Connect) ไม่ใช่ "best LLM routing". 12-18 เดือนข้างหน้า LLM จะ commoditize; Thai SaaS connector จะไม่

**Tactical 30 วัน:** ไม่ต้อง pivot; reinforce core thesis. ใช้ Recursive/Prometheus announcement เป็น data point ใน investor deck ว่า "model layer commoditizing, connector layer defensible" — investor ไทย หลัง Q1 2026 headline จะ primed ให้เข้าใจ

## Sources
- [Recursive Superintelligence Raises $500M at $4B Valuation (Implicator)](https://www.implicator.ai/recursive-superintelligence-raises-500m-from-gv-and-nvidia-at-4b-valuation/)
- [Recursive Superintelligence Raises $500M Funding Round (Ventureburn)](https://ventureburn.com/recursive-superintelligence-raises-500m-funding-round/)
- [Four-month-old Recursive Superintelligence raises $500m (Sifted)](https://sifted.eu/articles/recursive-superintelligence-500m)
- [Self-improving AI startup Recursive Superintelligence pulls in $500 million (The Decoder)](https://the-decoder.com/self-improving-ai-startup-recursive-superintelligence-pulls-in-500-million-just-four-months-after-founding/)
- [GV, Nvidia back a four-month-old AI lab in a $500M raise (TechFundingNews)](https://techfundingnews.com/recursive-superintelligence-500m-funding-gv-nvidia-4b-valuation/)

---

## Audio script
วันอังคารที่ยี่สิบเอ็ดเม.ย. วันเดียวกับ Bezos Prometheus. Recursive Superintelligence ปิด round ห้าร้อยล้านที่ valuation สี่พันล้าน. GV กับ Nvidia นำ. round oversubscribed เกือบหนึ่งพันล้าน. lab incorporated ธ.ค. สองห้า. สี่เดือนที่แล้ว. เส้นทางจาก incorporation ถึง สี่พันล้าน เร็วที่สุดในประวัติศาสตร์ venture ยุค AI. เร็วกว่า Anthropic xAI Mistral.

founding team ระดับ hall of fame. Richard Socher อดีต Chief Scientist Salesforce สร้าง Einstein AI. Tim Rocktäschel ex director DeepMind. Josh Tobin Jeff Clune Tim Shi ex OpenAI. total ยี่สิบคน. ratio ห้าร้อยล้านต่อยี่สิบ equal ยี่สิบห้าล้านต่อหัว. outlier. Anthropic ในช่วงอายุเดียวกันห้าล้านต่อหัว. OpenAI สิบล้านต่อหัว.

pitch คือ end to end self improving AI. automate ทุก step ของ AI research pipeline evaluation data selection training post training research direction. ไม่ต้องมี human in the loop. thesis contrarian. Anthropic OpenAI Google ยังเน้น human oversight เป็น safety layer. Recursive ประกาศตัดทิ้งเพื่อ compound improvement rate.

signal หนึ่ง self improving model คือ bet ใหม่ที่ top tier VC ยอมเดิมพัน. ก่อน ยี่สิบยี่สิบหก thesis นี้ AGI ish speculative ไม่มี lab ใหญ่ทำจริง. ตอนนี้ GV Nvidia ลง ห้าร้อยล้าน. mainstream capital allocator คำนวณว่า thesis ประเมินได้. มี asymmetric upside. แม้ความเสี่ยงแปดสิบเปอร์เซ็นต์ไม่ converge.

signal สอง ratio ยี่สิบห้าล้านต่อหัว. talent concentration equal key variable. Ilya SSI ยี่สิบพันล้านที่ seed. Mira Thinking Machines สิบสองพันล้านที่ seed. Recursive สี่พันล้านที่สี่เดือนอายุ. VC ปรับ model การประเมิน. ไม่ใช่ DCF revenue multiple benchmark. คือ top global researcher กี่คนคูณ premium factor. Recursive มีห้าบวกในนั้น. ห้าร้อยล้านเป็น talent deposit ไม่ใช่ business investment.

signal สาม Rocktäschel เลิก DeepMind ตอน DeepMind มี resource เยอะสุดในประวัติศาสตร์. brain drain Big Tech AI lab เร่ง. ปีที่แล้ว Ilya Mira Jan Leike Dario ออก OpenAI. ตอนนี้ Rocktäschel Clune Tobin Shi. Talent ไป lab ที่ promise ทำ thesis ที่ Big Tech ไม่ยอมทำ. frontier fragmentation. Big Tech lock top researcher ไม่ได้อีกต่อไป.

สำหรับ OpenBridge. direct relevance ต่ำ. strategic signal สองด้าน. หนึ่ง capital reshuffling. สิบจุดห้าพันล้านไหลเข้า AI lab ใน ยี่สิบสี่ชั่วโมง. Thai AI adjacent SaaS ควร lock term sheet runway ในไตรมาสที่ตลาด frothy. สอง model commoditization เร่ง. ถ้า Recursive thesis work model cost curve drop เร็วกว่า exponential. OpenBridge value ที่ connector specificity plus local context จะมีมูลค่ามากขึ้น. LLM จะ commoditize. Thai SaaS connector จะไม่
