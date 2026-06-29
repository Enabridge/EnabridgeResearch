---
date: 2026-06-30
slug: anthropic-tier-consolidation-rate-limits
topic: openbridge-trend
reading_time_min: 3
sources: 5
image_prompt: |
  Editorial illustration of three stacked metallic platform tiers labeled
  "START", "BUILD", and "SCALE" rising upward like a podium, with three
  identical glowing Claude orbs (one orange Opus, one purple Sonnet, one cyan
  Haiku) sitting at equal heights across the top — symbolizing rate-limit
  parity. Behind them a tall bar chart climbs from "$9B" to "$30B" to "$47B"
  with a steep upward arrow. Large floating numerals "3 tiers" and "$47B
  run-rate" hover prominently above the scene. Render style: cinematic
  editorial illustration, isometric perspective, warm Anthropic amber-orange
  with cool teal accents, dramatic depth, high-contrast typography legible at
  200px thumbnail. No human figures — only architectural elements.
image: images/26-06-30-0603-03-anthropic-tier-consolidation-rate-limits.png
---

# Anthropic ยุบ tier API เหลือ 3 ระดับ + rate limit Sonnet/Haiku เท่า Opus — signal ว่า demand โตเร็วกว่าระบบ tier เดิม

## TL;DR
- 27 มิ.ย. Anthropic ยุบ usage tier ของ Claude API เหลือ 3 ระดับ — Start / Build / Scale — และให้ rate limit ของ Sonnet กับ Haiku **เท่ากับ Opus** ที่ทุกระดับ
- "Most organizations move to a higher tier, no organization receives lower limits than before, no action required" — แปลว่าทุก customer ได้ของเพิ่ม ไม่มีใครเสีย
- Context: Anthropic run-rate revenue พุ่งจาก $9B (ปลาย 2025) → $30B (เม.ย. 2026) → $47B (พ.ค. 2026) — โต **80 เท่า** ใน 18 เดือน, Claude Code อย่างเดียว $2.5B run-rate

## เกิดอะไรขึ้น

วันที่ 27 มิ.ย. 2026 Anthropic ออก release note แบบเงียบ ๆ — แต่เป็นการเปลี่ยน billing/quota structure ครั้งใหญ่ที่สุดของ Claude API ในรอบปี usage tier เดิมที่มี 4-5 ระดับ (ขึ้นกับ historical billing) ถูก consolidate เหลือ 3 ระดับ: **Start** (เริ่มต้น), **Build** (app ที่เริ่มมี traffic), **Scale** (production workload ใหญ่)

ของจริงที่สำคัญกว่าการยุบ tier คือ **rate limit ของ Claude Sonnet และ Haiku ตอนนี้เท่ากับ Claude Opus ที่ทุก tier** ก่อนหน้านี้ rate limit ของ Opus มักจะต่ำกว่าเพราะ inference cost สูงกว่า — ทำให้ developer ต้อง engineer workaround คือเรียก Sonnet ที่ rate limit สูงกว่า แม้ task จะเหมาะกับ Opus มากกว่า ตอนนี้ pattern นี้หายไป — Anthropic บอกชัดว่า "no action required, most orgs move up" คือไม่ต้องทำอะไรเลย ระบบ migrate ให้อัตโนมัติ และไม่มีใครได้ rate limit ต่ำลง

Context ที่ทำให้ตัดสินใจครั้งนี้สำคัญ — Anthropic เปิด revenue trajectory ใน Q1-Q2 2026 ที่ทำลายทุก benchmark ของ enterprise software:
- $87M run-rate ม.ค. 2024
- $1B run-rate ธ.ค. 2024
- **$9B run-rate ปลาย 2025**
- $14B ก.พ. 2026
- $19B มี.ค. 2026
- **$30B เม.ย. 2026** (โต ~10 เท่าใน 12 เดือน)
- **$47B run-rate พ.ค. 2026**

Dario Amodei บอกเองว่า pace นี้ outstrip company forecast **ไป 8 เท่า** — และ Claude Code product เดี่ยว ๆ run-rate ทะลุ $2.5B โตจาก ~$1.2B ต้นปี 2026 พร้อมกับ deal Series H ที่ปิด $65B ที่ valuation $965B และ rumor Series I อีก $50B ที่ valuation $900B (TechCrunch รายงานเม.ย.)

ฝั่ง supply Anthropic ขยาย partnership Google + Broadcom ได้ compute **3.5 gigawatt** ของ TPU รุ่นใหม่ (เริ่ม 2027) บวกกับ 1GW ที่กำลัง online ปี 2026 — เป็น **4.5 เท่า expansion** ของ compute base ภายใน 18 เดือน Mizuho analysts ประเมิน Broadcom จะรับ $21B AI revenue จาก Anthropic ปี 2026 และ $42B ในปี 2027 — ตัวเลข supply chain ที่ทำให้ Anthropic กล้ายกเพดาน rate limit ได้

## ทำไมสำคัญ

การยุบ tier เหลือ 3 + ยกเพดาน Sonnet/Haiku ให้เท่า Opus = **Anthropic บอกตลาดว่า supply pressure คลายแล้ว** ปีที่แล้ว rate limit เป็นปัจจัยที่ทำให้ startup หลายเจ้าเลือก provider อื่น (OpenAI, Gemini) ทั้งที่ Claude คุณภาพดีกว่าใน task ของตัวเอง — เพราะไม่มั่นใจว่า scale production ขึ้นไปแล้วจะโดน throttle ตอนนี้ Anthropic remove friction นี้ทั้งหมด พร้อม message ว่า "ใช้ตัวที่เหมาะกับงาน ไม่ต้อง downgrade เพราะ rate limit"

Pattern ที่เห็นซ้ำ ๆ ในวงการ frontier model lab: **Anthropic ขายเร็วกว่า ship hardware ได้** มาตลอด 12 เดือน รอบนี้ดูเหมือนจะเป็นรอบแรกที่ supply catch up กับ demand ในระดับที่ลด rate limit constraint ลงได้ — เป็น datapoint เชิงโครงสร้างที่บอกว่า phase "supply-constrained" ที่กดดัน price ขึ้นเรื่อย ๆ อาจกำลังเข้าสู่ phase "demand-driven differentiation" ที่ provider แข่งกันที่ feature และ UX แทน

อีกมุมที่น่าสังเกต: tier consolidation จาก 5+ → 3 = **simplification ที่ตรงกับ enterprise sales playbook ของ Stripe/AWS** ในยุคที่ Anthropic ขยายทีม FDE (Forward Deployed Engineer) ตามที่เปิดตัวกับ Fujitsu/OpenAI สูตรเดียวกัน การมี 3 tier ที่ขายง่ายเป็น precondition ที่ enterprise sales scale ได้ — เปลี่ยนจาก self-serve developer-led growth ไป enterprise contract-led ชัดเจน

ตัวเลข $47B run-rate ที่ Anthropic ทำได้ในเดือนพ.ค. — ถ้าเทียบกับ OpenAI ที่ public กล่าวว่า $10B ARR ปลายปี 2024 และ Reuters รายงาน projected $11.6B ปี 2025 → Anthropic แซง OpenAI ไปแล้วใน run-rate revenue (แต่ OpenAI มี subscription consumer ที่ Anthropic ไม่มี ทำให้ตัวเลข total revenue ปี 2026 น่าจะยังใกล้กัน)

## มุม OpenBridge

**OpenBridge ที่ build agent บน Claude API ควรรีบ migrate ตัวเลือก default จาก Opus 4.8 ไป "model-of-best-fit"** — เดิมต้องเลือก Opus เพราะมั่นใจ rate limit ตอนนี้ใช้ Sonnet 4.6 สำหรับ task ส่วนใหญ่ที่ไม่ต้อง deep reasoning ได้แล้ว lower cost per call (~5x) โดยไม่กังวล throttle ลูกค้าจะเห็น margin ดีขึ้นทันที

ตัวเลข run-rate $47B + supply expansion 4.5x = **Anthropic เป็น vendor ที่ปลอดภัยที่สุดในการ commit roadmap ในระยะ 18 เดือน** เทียบกับ OpenAI ที่เพิ่งโดน government-gate GPT-5.6 → enterprise customer ที่ต้องการ availability guarantee จะ tilt ไปฝั่ง Claude มากขึ้น OpenBridge ใน positioning ควร emphasize "Claude-native + multi-vendor compatible" — Claude-first แต่ไม่ lock-in

Tier consolidation 3 ระดับเป็น blueprint สำหรับ OpenBridge pricing เอง — ลูกค้า B2B ชอบ pricing tier ที่จำง่าย map กับ stage ของบริษัทตัวเอง (just starting / scaling / enterprise) มากกว่า usage-based ที่คำนวณยาก ลองเทียบกับ pricing tier ปัจจุบันของ OpenBridge ว่ามีระดับมากเกินไปไหม

## Sources
- [Anthropic Release Notes — June 2026 Latest Updates — Releasebot](https://releasebot.io/updates/anthropic)
- [Anthropic says it hit a $30 billion revenue run rate after 'crazy' 80x growth — VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth)
- [Anthropic's run-rate revenue hits $47 billion — Simon Willison](https://simonwillison.net/2026/May/29/anthropic/)
- [Anthropic expands partnership with Google and Broadcom for multiple gigawatts of next-generation compute — Anthropic](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- [Anthropic secures access to 3.5 gigawatts of compute capacity in Google and Broadcom partnership — Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/anthropic-secures-access-3-5-124717374.html)

---

## Audio script
เรื่องที่สาม Yoh วันที่ 27 มิถุนา Anthropic ออก release note แบบเงียบๆ แต่เปลี่ยน billing structure ของ Claude API ครั้งใหญ่ที่สุดในรอบปี ยุบ usage tier เหลือสามระดับ Start Build Scale และให้ rate limit ของ Sonnet กับ Haiku เท่ากับ Opus ที่ทุก tier

ก่อนหน้านี้ rate limit ของ Opus ต่ำกว่าเพราะ inference cost สูง ทำให้ developer ต้องเรียก Sonnet ที่ rate สูงกว่า แม้ task จะเหมาะกับ Opus มากกว่า ตอนนี้ pattern นี้หายไป Anthropic บอกว่าทุก org migrate ขึ้น tier อัตโนมัติ ไม่มีใครได้ rate ลดลง

Context สำคัญมาก Anthropic run-rate revenue พุ่งจาก 9 billion ปลาย 2025 ไป 30 billion เมษา ไป 47 billion พฤษภา โต 80 เท่าใน 18 เดือน Dario บอกเองว่า outstrip forecast ของบริษัทไป 8 เท่า บวกกับ deal Broadcom Google ที่ได้ compute 3.5 gigawatt expansion 4.5 เท่า

มุม OpenBridge ควรรีบ migrate default จาก Opus 4.8 ไป model-of-best-fit ใช้ Sonnet สำหรับ task ส่วนใหญ่ได้แล้ว ลด cost per call ห้าเท่าโดยไม่กังวล throttle margin ดีขึ้นทันที และ Anthropic เป็น vendor ที่ปลอดภัยที่สุดในระยะ 18 เดือน ควร emphasize positioning Claude-native multi-vendor compatible ครับ
