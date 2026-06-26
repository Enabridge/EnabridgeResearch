---
date: 2026-06-24
slug: openai-jalapeno-broadcom-custom-inference-chip
topic: openbridge-trend
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial illustration of a glowing red chili-pepper-shaped silicon wafer
  labeled "JALAPEÑO" at the center of a cinematic data center hallway, with
  rows of server racks receding into orange-glowing horizon. Above the chip,
  large floating numerals "~50% cheaper" and "9 months" hover prominently,
  with smaller pinned tags "OpenAI × Broadcom" and "10 GW by 2029". An NVIDIA
  GPU silhouette in cool blue stands faded in the background, dwarfed by the
  pepper-chip in warm orange foreground. Render style: cinematic editorial
  illustration, dramatic perspective, high-contrast typography legible at
  200px thumbnail, warm amber-orange foreground against deep cool blue depth.
  No real human faces.
image: images/26-06-27-0603-01-openai-jalapeno-broadcom-custom-inference-chip.png
---

# OpenAI ปล่อย Jalapeño — chip แรกของตัวเอง ออกแบบเสร็จใน 9 เดือน, inference ถูกลง ~50% เทียบ Nvidia, deploy ปลายปี

## TL;DR
- 24 มิ.ย. OpenAI + Broadcom เปิด Jalapeño — ASIC ตัวแรกของ OpenAI ออกแบบเฉพาะ LLM inference, ผลทดสอบ early lab ลด cost per token ~50% เทียบ Nvidia generation ปัจจุบัน
- Tape-out ใน 9 เดือน (เร็วที่สุดเท่าที่ ASIC ระดับนี้เคยทำได้) — ใช้ Claude/GPT ของตัวเอง accelerate design + optimization process
- Deploy ก้อนแรกปลายปี 2026, ปูทาง 10-gigawatt commitment ถึงปี 2029 ร่วมกับ Microsoft และ partner — เริ่ม vertical stack ที่ผ่าน Nvidia ไปเลย

## เกิดอะไรขึ้น

วันที่ 24 มิ.ย. 2026 OpenAI ประกาศร่วมกับ Broadcom เปิดตัว **Jalapeño** — chip ตัวแรกที่ OpenAI ออกแบบเอง สำหรับ LLM inference โดยเฉพาะ ไม่ใช่ training Sam Altman เรียกมันว่า "the best inference platform" สำหรับโมเดล frontier ของ OpenAI Broadcom รับผิดชอบ silicon implementation, networking และ packaging, OpenAI ออกแบบ architecture โดยใช้ insight จาก research team ของตัวเองว่า kernels, memory movement และ serving pattern ไหนที่ workload จริงต้องการ

ตัวเลขที่ทำให้ตลาดสะดุ้งคือ pace กับ cost — Jalapeño tape-out ใน **9 เดือน** จาก initial design ซึ่ง Broadcom บอกว่าเร็วที่สุดที่ ASIC ระดับ reticle-size เคยทำได้ และ OpenAI ใช้ Claude/GPT ของตัวเอง accelerate ขั้น design + verification (ตัวอย่างของ "AI building AI" ที่ Anthropic เพิ่งเตือนเรื่องนี้เมื่อ 4 มิ.ย.) Performance per watt ของ Jalapeño เทียบ Nvidia Blackwell และ Google TPU เท่ากันในเชิง throughput แต่ **cost per inference token ลดลงราว 50%** ตาม OpenAI lab benchmark — ตัวเลขนี้ยังไม่ถูก verify โดย third party แต่ Broadcom ก็ยืนยันเลขในรอบ analyst call

แผน deploy คือ initial batch ปลายปี 2026 แล้วขยายเป็น gigawatt-scale data center ร่วมกับ Microsoft และ partner รายอื่นในช่วง 3 ปีถัดไป รวมเป็น **commitment 10 GW ถึงปี 2029** ซึ่งถ้าทำได้ตามแผนจะเป็นการลด exposure ของ OpenAI ต่อ Nvidia roadmap อย่างมีนัยสำคัญ Jalapeño เป็น chip ตัวแรกใน "multi-generation compute platform" ที่ OpenAI วางไว้ — แปลว่ายังมีรุ่น 2, 3 ตามมา และน่าจะออกแบบให้แต่ละรุ่น optimize สำหรับ model family ใหม่ที่ launch พร้อมกัน

ตัวเลขนี้ออกในจังหวะที่ delicate มาก — 1 มิ.ย. OpenAI ยัง spend $1.35 ต่อทุก $1 revenue และ Anthropic เพิ่งจะ confidentially file IPO ด้วย run-rate $47B+ ขณะที่ OpenAI อ้าง run-rate ที่สูงกว่าแต่ margin ต่ำ Jalapeño คือ direct response ต่อ unit economics ของตัวเอง ไม่ใช่ research vanity project

## ทำไมสำคัญ

ของจริงที่เปลี่ยนคือ **bargaining power ใน inference economy** ตอนนี้ทุกคนที่ขาย LLM API ต้องจ่าย Nvidia margin (~75% gross margin บน H100/B200) — ถ้า Jalapeño deliver 50% lower cost ได้จริง OpenAI จะกดราคา API ลงต่อเนื่องโดยไม่ทำลาย margin ตัวเอง pattern นี้คือสิ่งที่ Google ทำได้กับ TPU มา 10 ปี และเป็นเหตุผลที่ Gemini Flash ขายได้ $0.075/$0.30 ต่อล้านโทเค็น ขณะที่ OpenAI กับ Anthropic ขายแพงกว่า 10–20 เท่า การที่ OpenAI build chip เองหมายความว่าราคา GPT-5.5 อาจไม่ใช่ pricing floor อีกต่อไป

ที่น่าสนใจเทียบเคียงคือ Broadcom — บริษัทเดียวที่ออกแบบ custom chip ให้ Google (TPU), OpenAI (Jalapeño), Meta (MTIA), และ ByteDance position ของ Broadcom กลายเป็น "Switzerland of custom AI silicon" — neutral chipmaking partner ที่ทุก hyperscaler ใช้ ตลาด Nvidia แทนที่จะแบ่ง share กับคู่แข่งโดยตรง ตอนนี้กำลังถูก slice ไปทีละ workload โดย Broadcom + customer แต่ละราย Nvidia ยัง dominant ใน training แต่ inference (ซึ่งเป็น 80%+ ของ AI compute spend ตามตัวเลข Stanford HAI) เริ่มเปิดประตูให้ ASIC

Pace 9 เดือนคือ signal ที่ใหญ่กว่าตัวเลข 50% — สำหรับวงการ semiconductor cycle 18–24 เดือนคือ norm และ Jalapeño บีบครึ่ง ส่วนหนึ่งเพราะ OpenAI ใช้ Codex/GPT ทำ RTL synthesis และ verification ซึ่งถ้า pattern นี้ทำซ้ำได้ chip generation ถัดไปจะ ship ทุก 9–12 เดือน คาดหวังได้ — แทนที่จะเป็น 2 ปี และ Anthropic จะถูก force ตามมา

## มุม OpenBridge

ระยะสั้น nothing changes — Jalapeño ยังไม่ deploy จริงจน Q4 2026 แต่ระยะกลาง OpenBridge ควรจัด pricing model ให้ทนกับ scenario "inference cost ลดลง 50% ภายใน 12 เดือน" ถ้าราคา per-call ลดครึ่ง customer จะคาดหวัง "more tokens per dollar" ทันที — flat-rate / unlimited tier ที่ pricing ตอนนี้ดู safe อาจกลายเป็น margin trap ถ้า OpenAI/Anthropic เปลี่ยน pricing ครั้งเดียว และ OpenBridge มี long-term contract ผูกราคา ลูกค้าจะหา leverage มา renegotiate ทันที

ที่ตามมาเป็น signal ระยะยาวคือ **vertical stack กลับมา** — OpenAI design chip + train model + ขาย API + build agent runtime (Operator, Codex, Daybreak) — ทุกชั้น ครบสตอรี่ที่ Apple ทำใน mobile หรือ Google ใน search OpenBridge ที่อยู่กลางสายพานต้อง decide ว่าจะ position เป็น "neutral integration layer ระหว่างหลาย vertical stack" หรือยอมเลือกข้าง pattern ตลาดบ่งบอกว่า "neutrality" จะ premium ขึ้น เพราะลูกค้า enterprise กลัว vendor lock-in กับ stack เดียว — แต่ neutrality ต้อง investment ใน MCP, A2A, multi-model routing ที่ deep พอจะใช้งานจริง ไม่ใช่ทำแค่หน้าฉาก

## Sources
- [OpenAI and Broadcom unveil LLM-optimized inference chip — OpenAI](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
- [OpenAI unveils first chip as part of Broadcom deal in effort to 'build the full stack' — CNBC](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
- [OpenAI unveils first custom AI inference chip, Jalapeño, with Broadcom — VentureBeat](https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models)
- [Broadcom and OpenAI unveil custom-built Jalapeño inference processor — Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle)
- [OpenAI unveils its first custom chip, built by Broadcom — TechCrunch](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
- [OpenAI's First Custom AI Chip Targets 50% Cheaper Inference: Jalapeño Unveiled — TechTimes](https://www.techtimes.com/articles/319012/20260624/openais-first-custom-ai-chip-targets-50-cheaper-inference-jalapeno-unveiled.htm)

---

## Audio script
สวัสดีครับ Yoh เช้านี้ OpenAI กับ Broadcom ปล่อย Jalapeño chip ตัวแรกที่ OpenAI ออกแบบเอง สำหรับ LLM inference โดยเฉพาะ ที่น่าสนใจคือ tape-out ใน 9 เดือน เร็วที่สุดเท่าที่ ASIC ระดับนี้เคยทำได้ และ OpenAI ใช้ Claude กับ GPT ของตัวเอง accelerate ขั้น design กับ verification ผล lab benchmark บอกว่า cost per inference token ลดลงราว 50% เทียบ Nvidia generation ปัจจุบัน แต่ performance per watt อยู่ระดับเดียวกับ Blackwell และ Google TPU แผนคือ deploy batch แรกปลายปี 2026 แล้วขยายเป็น gigawatt scale ร่วมกับ Microsoft รวม 10 gigawatt ถึงปี 2029 ส่งผลให้ Nvidia margin ตลาด inference เริ่มถูก slice อย่างเป็นทางการ ที่น่าสังเกตอีกอย่างคือ Broadcom กลายเป็น Switzerland of custom AI silicon ออกแบบ chip ให้ทั้ง Google, OpenAI, Meta และ ByteDance สำหรับ OpenBridge ระยะสั้นยังไม่กระทบ แต่ระยะกลาง pricing model ต้องทนกับ scenario inference cost ลดครึ่งใน 12 เดือน flat rate tier ที่ดู safe ตอนนี้อาจกลายเป็น margin trap ถ้าลูกค้า renegotiate และที่สำคัญกว่านั้น vertical stack ของ OpenAI กำลังครบทุกชั้น OpenBridge ต้อง decide ว่าจะ position เป็น neutral integration layer ระหว่าง stack หรือยอมเลือกข้าง ตลาดบ่งบอกว่า neutrality จะ premium ขึ้น แต่ต้อง invest ใน MCP กับ multi-model routing ให้ deep พอจะใช้จริงครับ
