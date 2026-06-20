---
date: 2026-06-20
slug: john-jumper-deepmind-anthropic-nobel
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial illustration of a glowing helical protein ribbon shaped like a stylized bridge spanning between two abstract corporate towers — the left tower carries a faint geometric "G" silhouette glowing in muted blue, the right tower a faint geometric "A" silhouette glowing in warm amber, a single luminous human silhouette walks across the protein bridge toward the amber side carrying a small Nobel-medal-shaped disc that emits soft golden particles, minimal flat geometric shapes with subtle isometric perspective, deep navy background with cyan and amber rim light, dramatic sci-fi editorial mood, no real human faces (silhouette only), no readable text or logos beyond the abstract G and A letterforms.
image: images/26-06-21-0602-02-john-jumper-deepmind-anthropic-nobel.png
---

# Nobel laureate John Jumper ย้ายค่าย — จาก DeepMind ไป Anthropic หลังเก้าปี เป็นการประกาศใหม่ว่า "AI for science" frontier ย้ายเข้าฝั่ง Claude

## TL;DR
- **20 มิ.ย.** John Jumper — ผู้คว้า **Nobel Prize เคมี 2024** จาก AlphaFold — ประกาศลาออกจาก Google DeepMind หลังทำงาน **9 ปี**, ไปร่วม Anthropic
- Bloomberg รายงานช่วงท้ายที่ DeepMind เขาทำเรื่อง **Google's coding tools** ที่ "struggled to commercialize" — pattern ที่ตรงกับ Claude Code revenue $2.5B run-rate ของ Anthropic
- เขายังไม่ระบุ title ใหม่; statement จาก X: "GDM is a special place, and I'll still be excited to hear about what amazing things they discover next" — สุภาพแบบมีนัยยะ
- Signal: หลังดีล Google $40B → Anthropic เม.ย. ที่ผ่านมา ทุนไหลทิศทางหนึ่ง — talent ที่จะ "นิยาม frontier ถัดไป" (AI สำหรับ biology + science) ก็เริ่มไหลตามทิศเดียวกัน

## เกิดอะไรขึ้น

ช่วงเช้าวันศุกร์ที่ 20 มิ.ย. John Jumper โพสต์บน X ว่ากำลังลาออกจาก Google DeepMind หลังทำงานเกือบ 9 ปี เพื่อไปร่วม Anthropic. Jumper ไม่ใช่นักวิจัยทั่วไป — เขาเป็น **co-winner ของ Nobel Prize เคมีปี 2024** ร่วมกับ Demis Hassabis สำหรับ AlphaFold, โมเดลที่ทำนายโครงสร้าง 3D ของ protein จาก amino acid sequence ทำให้ **structural biology ทั้งวงการเปลี่ยน workflow** ภายใน 3 ปี และเปิดประตูให้ drug discovery, enzyme engineering, vaccine design ที่ก่อนหน้านี้ใช้เวลา 5-10 ปีต่อ target

ที่น่าสนใจกว่าตัวการย้าย คือ **บริบทตอนปลาย** ที่ Jumper อยู่ที่ DeepMind. Bloomberg รายงานว่าช่วงท้ายเขาทำงานกับ Google's coding tools ที่ "the company has struggled to commercialize" — ภาษาทูตของการบอกว่า Gemini Code Assist กับ Antigravity ยังไม่ได้ traction ที่จะแข่งกับ Claude Code. นี่ไม่ใช่เรื่องบังเอิญ: ในไตรมาสที่ Anthropic disclose Claude Code revenue ที่ **$2.5B annualized** (เม.ย. 2026) และ Google ลงเงิน $40B ใน Anthropic ส่วนหนึ่งเพื่อ "ensure the world's most valuable AI workloads run on our compute" — Jumper เห็นจากในวงในก่อนใครว่า momentum อยู่ที่ใคร

statement ที่ Jumper เลือกใส่ใน X อ่านสุภาพแต่เลือกคำมีนัยยะ: **"GDM is a special place, and I'll still be excited to hear about what amazing things they discover next."** ไม่มี "thanks Demis", ไม่มี mission alignment statement — มี implicit เพียงว่า "I'm leaving to be where I think the next discovery happens". ในวัฒนธรรม Google ที่ founder ส่วนใหญ่ออกเงียบ ๆ การที่ Nobel laureate ออกแบบประกาศต่อสาธารณะใน X เป็น signal เชิงสถานะที่ Anthropic จะใช้ recruit ทีม biology + science ต่อไป

## ทำไมสำคัญ

หลายคนจะอ่านข่าวนี้เป็นเรื่อง individual career move. มอง pattern ลึกขึ้น — เป็นข่าวเชิง **"frontier ถัดไปย้ายฝั่ง"**. ตลอด 5 ปีที่ผ่านมา DeepMind ครองภาพ "AI for science" — AlphaFold, AlphaProteo, AlphaGenome, GraphCast (สภาพอากาศ), MaterialsGNoME (วัสดุ). Anthropic เล่นเกม "frontier model สำหรับ enterprise + coding". การที่ Jumper ย้ายไปฝั่ง Anthropic ส่งสัญญาณว่าทีม Anthropic มี mandate (และ budget) ที่จะเข้า AI for science แบบจริงจัง — ไม่ใช่ side project. คาดว่าจะเห็น "Claude for Science" หรือ analogue ของ AlphaFold ที่ build บน Claude Opus 4.8 + Dynamic Workflows ภายใน 12-18 เดือน

ตัว setup ของ Anthropic ก็พร้อม: TPU 5GW จาก Google + Trainium จาก Amazon + valuation $350B primary / $1T secondary + Claude Code platform ที่ Jumper รู้จากใน. Anthropic ไม่ต้อง start from scratch เหมือนตอน DeepMind เริ่ม AlphaFold ปี 2018 — มี base model ที่ reasoning ดีพอจะใช้เป็น scientific assistant แล้ว. คำถามคือ **"AI for science" workflow ที่ใช้ Claude เป็น orchestrator + subagent + tool fabric** จะดูเป็นยังไง? Jumper คือคนที่รู้ blueprint นั้นดีที่สุดในวงการ — เขาเพิ่งใช้เวลา 7 ปีสร้างมันที่ DeepMind

ผลกระทบฝั่ง Google ที่หนักที่สุดคือ narrative loss. DeepMind พึ่ง "Nobel laureate-grade research culture" เป็น recruit pitch มาตลอด. การที่ Hassabis (CEO + co-laureate) มีอยู่ที่ Google ยังไม่พอ — ผู้ร่วม Nobel เลือกออก. คาดว่า Sundar Pichai จะตอบโต้ด้วย counter-offer ระดับ retention package $50-200M สำหรับ top 20 researchers ใน DeepMind ภายใน 30 วัน (เคยทำตอน Noam Shazeer ออกไป Character.AI ปี 2023). Google เริ่มเสีย "talent gravity" เป็นครั้งแรกอย่างเปิดเผยตั้งแต่ Anthropic founders ออกจาก OpenAI ปี 2021

## มุม OpenBridge

**ไม่ direct เกี่ยว แต่...** signal ที่ Jumper ย้ายไป Anthropic = confirm trajectory ว่า **Claude จะเป็น default substrate ของ "deep workflow" agent** ใน vertical ที่ต้อง reasoning หนัก (science, legal, finance audit, medical). OpenBridge ที่ position เป็น "Claude-first integration platform" สำหรับ Thai enterprise ได้ทัศนะ tailwind นี้ตรง — ลูกค้าที่กำลังพิจารณา "ใช้ AI วาง infrastructure 3 ปี" เริ่มเห็น Anthropic เป็น safer bet มากกว่า 6 เดือนก่อน

**Vertical opportunity:** ในไทยมีอุตสาหกรรมที่ analogue กับ "AI for science" อยู่ — **agro-biotech** (CP Foods, Betagro, มหิดล), **medical research** (จุฬาฯ AI lab, Bumrungrad data), **materials/aviation** (PTT, TAT). ถ้า Anthropic เปิด "Claude for Science" tier ภายใน Q3-Q4, OpenBridge สามารถเป็น first-mover integrator ที่ build connector ไป **LIMS (lab info management)**, **ELN (electronic lab notebook)**, **bioinformatics pipeline** ของ Thai R&D team ที่ตอนนี้ไม่มีใครเชื่อมให้. ตลาดเล็ก แต่ margin สูงและ defensible

**Action 30-60 วัน:** เริ่ม conversation กับมหิดล + จุฬาฯ AI lab ว่ามี research workflow ตัวไหนที่ต้องการ "Claude + custom MCP tool" — เก็บ requirement ไว้ใน playbook. เมื่อ Anthropic ประกาศ science tier (น่าจะภายใน 12 เดือนตามที่คาดจาก Jumper hire) OpenBridge จะมี pipeline พร้อม convert ทันที — ไม่ต้องเริ่ม cold

## Sources
- [Nobel laureate John Jumper is leaving DeepMind for rival Anthropic (TechCrunch)](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/)
- [John Jumper announces departure from Google DeepMind after nearly 9 years (X / Bloomberg via TechCrunch)](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/)
- [Anthropic Nobel-grade biology hire — context on Claude Code $2.5B run-rate and Google $40B Anthropic deal (Bloomberg / Anthropic prior disclosures)](https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic)

---

## Audio script
ช่วงเช้าวันศุกร์ยี่สิบมิถุนา. John Jumper โพสต์บน X ว่าลาออกจาก Google DeepMind หลังทำงานเกือบเก้าปี เพื่อไปร่วม Anthropic.

Jumper ไม่ใช่นักวิจัยทั่วไป. เขาเป็น co winner ของ Nobel Prize เคมี ปี สองศูนย์สองสี่ ร่วมกับ Demis Hassabis สำหรับ AlphaFold. โมเดลที่ทำนายโครงสร้าง 3D ของ protein จาก amino acid sequence. เปลี่ยน workflow ของ structural biology ทั้งวงการในสามปี. เปิดประตู drug discovery vaccine design ที่ก่อนหน้านี้ใช้ห้าถึงสิบปีต่อ target.

บริบทตอนปลายของเขาที่ DeepMind น่าสนใจ. Bloomberg รายงานว่าช่วงท้ายเขาทำกับ Google coding tools ที่ struggled to commercialize. ภาษาทูตของการบอกว่า Gemini Code Assist และ Antigravity ยังตามไม่ทัน Claude Code. ในไตรมาสเดียวกันที่ Anthropic disclose Claude Code revenue สองพันห้าร้อยล้านต่อปี และ Google ลง สี่หมื่นล้านใน Anthropic เพื่อให้ workload วิ่งบน TPU. Jumper เห็นจากในวงในก่อนใครว่า momentum อยู่ที่ใคร.

statement ที่เขาเลือกใส่ใน X. GDM is a special place and I'll still be excited to hear about what amazing things they discover next. ไม่มี thanks Demis ไม่มี mission alignment statement. มี implicit เพียงว่า I'm leaving to be where I think the next discovery happens.

pattern ใหญ่. ไม่ใช่ career move. เป็น frontier ถัดไปย้ายฝั่ง. ตลอดห้าปี DeepMind ครองภาพ AI for science. AlphaFold AlphaProteo AlphaGenome GraphCast MaterialsGNoME. Anthropic เล่นเกม frontier model สำหรับ enterprise และ coding. การที่ Jumper ย้ายฝั่ง ส่งสัญญาณว่า Anthropic มี mandate และ budget เข้า AI for science แบบจริงจัง. คาดว่าจะเห็น Claude for Science ภายในสิบสองถึงสิบแปดเดือน.

ผลกระทบ Google ที่หนักที่สุดคือ narrative loss. DeepMind พึ่ง Nobel laureate grade research culture เป็น recruit pitch มาตลอด. การที่ผู้ร่วม Nobel เลือกออก เป็นครั้งแรกที่ Google เสีย talent gravity เปิดเผยตั้งแต่ Anthropic founders ออกจาก OpenAI ปี สองศูนย์สองหนึ่ง.

สำหรับ OpenBridge. ไม่ direct แต่ Claude จะเป็น default substrate ของ deep workflow agent ใน vertical ที่ต้อง reasoning หนัก. ลูกค้าที่กำลังพิจารณาใช้ AI วาง infrastructure สามปี เริ่มเห็น Anthropic เป็น safer bet มากกว่าหกเดือนก่อน. ในไทยมีอุตสาหกรรม analogue กับ AI for science. agro biotech medical research materials aviation. ถ้า Anthropic เปิด Claude for Science tier ใน Q3 Q4 OpenBridge สามารถเป็น first mover integrator ที่ build connector ไป LIMS ELN bioinformatics pipeline ของ Thai R และ D team. เริ่ม conversation กับมหิดลและจุฬา AI lab ภายในสามสิบถึงหกสิบวัน
