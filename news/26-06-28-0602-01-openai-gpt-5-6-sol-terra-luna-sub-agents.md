---
date: 2026-06-27
slug: openai-gpt-5-6-sol-terra-luna-sub-agents
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial illustration of three glowing celestial orbs labeled "SOL", "TERRA",
  and "LUNA" hovering in a stylized solar system over a dark indigo void. Sol —
  the largest orb at center — is fracturing open to reveal a cluster of tiny
  robotic sub-agent figures spilling outward, each linked by glowing orange
  filaments back to the parent star, visualizing "sub-agents inside the model."
  Large floating numerals "$5/$30" and "GPT-5.6" pin prominently beside Sol,
  with smaller price tags "$2.50/$15" on Terra and "$1/$6" on Luna. Render
  style: cinematic editorial illustration, isometric cosmic perspective, warm
  amber-orange glow at the center fading to deep indigo at the edges, high
  contrast typography legible at 200px thumbnail. No real human faces — only
  robotic silhouettes.
image: images/26-06-28-0602-01-openai-gpt-5-6-sol-terra-luna-sub-agents.png
---

# OpenAI GPT-5.6 — Sol / Terra / Luna + "Ultra" Mode ที่ spawn sub-agents ใน model เอง (USG-only preview)

## TL;DR
- 26 มิ.ย. OpenAI ปล่อย limited preview ของ GPT-5.6 family: **Sol** (flagship long-horizon agentic), **Terra** (balanced), **Luna** (low-cost) — เปิดให้ ~20 US-gov-approved partners เท่านั้น
- Pricing: Sol $5 in / $30 out, Terra $2.50/$15, Luna $1/$6 ต่อล้านโทเค็น — Sol แพงกว่า output ของ Opus 4.8 ($25) 20%
- ใหม่สุดคือ **"ultra" mode** — model spawn sub-agents ภายในตัวเองโดย runtime ไม่ต้องใช้ SDK external หรือ orchestration framework

## เกิดอะไรขึ้น

วันที่ 26 มิ.ย. 2026 OpenAI ประกาศ GPT-5.6 family — 3 รุ่นพร้อมกันในชื่อ astronomical Sol / Terra / Luna ที่ตอกย้ำ tiered positioning ตามแบบ Anthropic (Opus / Sonnet / Haiku) สิ่งที่ทำให้คนวงในตื่นเต้นไม่ใช่ benchmark — เพราะ OpenAI ยังไม่เปิด benchmark เต็ม — แต่เป็น **architectural change** ที่ฝัง agentic orchestration เข้าไปใน model ตรง ๆ Sol เป็น flagship ที่ OpenAI เรียกว่า "tuned for long-horizon agentic work" ส่วน "ultra" mode เป็น reasoning mode ใหม่ที่ model จะ spawn sub-agents ภายในตัวเองโดย runtime แทนที่จะใช้ Agents SDK external

ที่น่าสนใจคือ access จำกัดมาก — preview เปิดให้แค่ ~20 partner ที่ผ่านการ approve จาก US government สำหรับงาน defense/intelligence/critical infrastructure ตลาด commercial ทั่วไปต้องรออีกหลายเดือน นี่เป็น signal สองชั้น: หนึ่ง — OpenAI พร้อมตัดสินใจ delay commercial revenue เพื่อ secure government contract สอง — ตลาด USG กำลังเป็น forcing function ที่กำหนด feature set ของ frontier model (เห็นได้จาก OpenAI Atlassian Rovo, Anthropic Claude Gov, Palantir partnerships ก่อนหน้า)

ส่วน pricing เปิดเผยล่วงหน้า: Sol อยู่ที่ $5 input / $30 output ต่อล้านโทเค็น — Output แพงกว่า Claude Opus 4.8 ($25) ประมาณ 20% Terra ที่ $2.50/$15 อยู่ระหว่าง Sonnet กับ Opus และ Luna ที่ $1/$6 ตีตรงกับ tier ของ GPT-5-mini เดิม นอกจากนี้ในวันถัดมา (27 มิ.ย.) OpenAI ปิด deprecation window ของ GPT-4.5 อย่างเป็นทางการ — pipeline agent ที่ pin model 4.5 ไว้เสียทันที ผู้สังเกตวงในชี้ว่า adoption ของ Claude Code ในกลุ่ม developer แตะ 97% ขณะที่ governance coverage แค่ 33% — ช่องว่างนี้กำลังเปิดกว้างขึ้นพอดีจังหวะที่ frontier model surface กำลัง consolidate

## ทำไมสำคัญ

"Sub-agents inside the model" เป็น move ที่ commoditize agent orchestration layer ลึกกว่าที่ Anthropic ทำกับ Dynamic Workflows เมื่อ 30 พ.ค. — Anthropic Dynamic Workflows ยัง require Claude เขียน JavaScript ที่ runtime execute ใน Claude Code SDK ส่วน OpenAI ultra mode เคลม run ในระดับ model inference เอง ไม่มี runtime layer แยก หมายความว่า framework อย่าง LangChain/CrewAI/AutoGen ที่ขาย "multi-agent orchestration" เป็น value-add กำลังถูก squeeze จาก 2 ทาง: hyperscaler model lab (Anthropic, OpenAI) build เข้า platform โดยตรง

USG-only preview เป็น pattern ที่จะเห็นบ่อยขึ้น — frontier capability ที่ดีที่สุดจะ release ไป government/defense ก่อน commercial หลายเดือน เพราะ (1) ราคาที่ USG ยอมจ่ายต่อ token สูงกว่า enterprise commercial 5–10 เท่า (2) compliance/security review เปิดทาง defensible moat (3) USG case study เป็น marketing asset ที่ทรงพลังที่สุดสำหรับ Fortune 100 ตามมา ใครที่ทำงานในตลาด commercial AI ต้อง factor delay นี้เข้าใน roadmap — capability gap ระหว่าง USG tier และ commercial tier จะกว้างขึ้น 6–12 เดือนเป็น norm

## มุม OpenBridge

Sub-agents inside the model หมายความว่า OpenBridge ยิ่งห้ามขายเป็น "orchestration platform" — เพราะทั้ง Anthropic และ OpenAI กำลังบีบ layer นั้นจาก 2 ฟากแล้ว ทาง position ที่ defensible คือ **"tool + data fabric ที่ sub-agent เรียกเข้ามาใช้"** — Sol/Terra/Luna ที่ spawn sub-agent ใน model จะยิ่งต้องการ tool surface ที่กว้างและ data ที่ contextual เพราะ sub-agent หนึ่งตัว = หนึ่ง tool call/data lookup OpenBridge ต้องเตรียม MCP-native connector marketplace ที่ scale ได้ระดับ "1 session = 100+ tool invocations"

Pricing ที่ Sol แพงกว่า Opus 4.8 20% แต่ Luna ถูกกว่า Haiku สะท้อนกลยุทธ์ tiered routing ที่ enterprise ลูกค้าจะใช้ — งานง่ายไป Luna, งาน complex ไป Sol, งานกลางๆ ไป Terra OpenBridge ต้อง build smart routing layer ที่ส่ง request ไป tier ที่ถูกต้องโดย customer ไม่ต้องคิดเอง — ถ้าทำได้ดี ลดต้นทุนลูกค้า 60–80% โดย quality เท่าเดิม นี่เป็น value prop ที่ neutral integration layer จะส่งมอบได้ดีกว่า model vendor (ที่ incentive ขายให้ใช้ tier บนสุด)

## Sources
- [Previewing GPT-5.6 — OpenAI](https://openai.com/index/previewing-gpt-5-6-sol/)
- [OpenAI unveils GPT-5.6 Sol, Terra, and Luna models but only accessible to limited preview partners — VentureBeat](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)
- [OpenAI Previews GPT-5.6 With Sol, Terra, and Luna Tiered Models, New Reasoning Modes — MarkTechPost](https://www.marktechpost.com/2026/06/26/openai-previews-gpt-5-6-with-sol-terra-and-luna-tiered-models-new-reasoning-modes-limited-access/)

---

## Audio script
สวัสดีครับ Yoh เมื่อวานนี้ OpenAI ปล่อย limited preview ของ GPT-5.6 family ทีเดียว 3 รุ่น Sol สำหรับงาน long-horizon agentic, Terra สำหรับงานกลาง, Luna สำหรับงานเบา ราคา Sol อยู่ที่ 5 ดอลลาร์ input และ 30 ดอลลาร์ output ต่อล้านโทเค็น แพงกว่า Claude Opus 4.8 ประมาณ 20% สิ่งที่ทำให้คนวงในตื่นเต้นไม่ใช่ราคา แต่เป็น ultra mode ที่ model spawn sub-agents ภายในตัวเองโดย runtime แทนที่จะใช้ Agents SDK external นี่ลึกกว่า Dynamic Workflows ที่ Anthropic ปล่อยเมื่อปลายเดือน พ.ค. เพราะ orchestration ไม่ต้องผ่าน runtime layer ใด ๆ access ตอนนี้จำกัดให้แค่ประมาณ 20 partner ที่ผ่านการ approve จาก US government เท่านั้น สำหรับงาน defense, intelligence, critical infrastructure ตลาด commercial ทั่วไปต้องรออีกหลายเดือน นี่เป็น pattern ใหม่ที่ frontier capability ที่ดีที่สุดจะออก USG ก่อน commercial 6 ถึง 12 เดือน สำหรับ OpenBridge มีสองประเด็นต้อง take away หนึ่ง ทั้ง Anthropic และ OpenAI กำลังบีบ orchestration layer จาก 2 ฟาก OpenBridge ต้อง position เป็น tool plus data fabric ที่ sub-agent เรียกใช้ ไม่ใช่ orchestration platform สอง pricing tiered ของ Sol Terra Luna เปิดโอกาสให้ build smart routing layer ที่ส่ง request ไป tier ที่ถูกต้องโดยอัตโนมัติ ลดต้นทุนลูกค้าได้ 60 ถึง 80% โดยคุณภาพเท่าเดิม นี่เป็น value prop ที่ neutral integration layer ส่งมอบได้ดีกว่า model vendor แน่นอนครับ
