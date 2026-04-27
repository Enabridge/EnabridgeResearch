---
date: 2026-04-28
slug: jpmorgan-ai-mandate-65k-engineers
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a vast modern corporate headquarters with rows of identical workstations, each glowing softly as if synchronized to one rhythm, a translucent dashboard hovering above showing tier indicators, muted navy and gold palette, minimal flat shapes, dramatic top-down perspective, no text, no logos, no faces
image: images/26-04-28-0606-02-jpmorgan-ai-mandate-65k-engineers.png
---

# JPMorgan ผูก performance review เข้ากับการใช้ AI tool — 65,000 engineers ถูก track ทุกคน

## TL;DR
- JPMorgan เพิ่ม "AI tool adoption" เป็น formal criteria ใน performance review สำหรับ engineers 65,000 คน — ตั้งแต่ปลายมีนาคม 2026
- Internal dashboard แบ่งเป็น light user / heavy user / non-user, manager เห็น team adoption rate รายสัปดาห์
- 450+ AI use cases อยู่ใน production แล้ว, โต $1.5B savings, productivity +10–20% — แต่จุดเปลี่ยนคือ "ใช้ AI" กลายเป็น KPI ไม่ใช่ optional skill

## เกิดอะไรขึ้น

ตั้งแต่ปลายมีนาคม 2026 JPMorgan Chase ออก internal performance framework ใหม่ ที่ผูก "การใช้ AI tool" เป็น measurable component ของ performance review สำหรับพนักงาน software และ security engineering ราว 65,000 คน — โดยมี dashboard tracking GitHub Copilot usage แยกเป็น 3 tier: light user, heavy user, non-user ผู้จัดการแต่ละ team จะได้รับรายงาน adoption rate เป็นประจำ

นี่ไม่ใช่ recommendation soft ๆ แล้ว — internal documents ที่หลุดออกมาระบุชัดว่า performance review จะประเมินทั้ง "what you achieve" และ "how you achieve it" — โดย AI tool adoption ถูกจัดอยู่ในหมวดหลัง engineers ที่ไม่ใช้ AI tool แม้จะ deliver งานปกติ ก็จะได้คะแนน "how" ต่ำลง ส่งผลถึง bonus, promotion, และ exit risk

ตัวเลข deployment ของ JPMorgan เองเล่าเรื่องเร็วมาก: 450+ AI use cases อยู่ใน production แล้ว มีเป้าจะแตะ 1,000 ภายในสิ้นปี 2026, LLM Suite (chat tool ภายในที่ wrap GPT/Claude) มี active user 200,000+ คน, productivity ของ engineer ที่ใช้ coding assistant ขยับขึ้น 10–20% — และ AI initiatives รวมแล้วประหยัดได้ $1.5B จาก fraud, trading, operations พร้อมเพิ่ม revenue $220M+ จาก credit card upgrades และอีก $100M จาก commercial bank suggestions

ในเวลาเดียวกัน JPMorgan กำลังเริ่ม pilot Anthropic Claude Code ตั้งแต่เมษายน 2026 และ scope ของ tools ที่ "นับ" ใน performance score กำลังขยาย — ไม่ใช่แค่ Copilot อีกต่อไป

## ทำไมสำคัญ

นี่คือจุดเปลี่ยน — บริษัทที่ regulated หนักที่สุดในโลก, มี risk culture conservative ที่สุด, ตอนนี้ทำให้การใช้ AI กลายเป็น performance gate ไม่ใช่ optional skill เมื่อ JPMorgan ทำได้ คนอื่นใน financial services ตามภายใน 6–12 เดือนแน่นอน คาดเห็น Goldman, Citi, BofA ทำ similar framework ใน Q3–Q4 2026

ที่น่าสนใจกว่าคือ comparison กับ wave ก่อน: ตอน cloud migration ปี 2014–2018 บริษัทใหญ่ใช้เวลาเกือบ 5 ปีกว่าจะ formalize "cloud-first" เป็น performance criteria แต่ AI adoption รอบนี้ใช้เวลาแค่ 18 เดือนตั้งแต่ Copilot GA — เพราะ measurement ทำได้ง่ายกว่ามาก (telemetry มาตั้งแต่ tool, ไม่ต้องมี cultural assessment)

Signal ที่ตามมา: vendor ที่ขาย AI dev tools จะแข่งกันที่ "telemetry depth" ไม่ใช่ raw capability อีกต่อไป — เพราะ enterprise CIO ต้องการ proof of usage ส่งผู้บริหาร ตัว tool ไหนที่ produce dashboard adoption ได้ละเอียด อยู่ในตำแหน่งดีกว่าตัวที่ "เก่งกว่า" แต่ใช้แล้ววัดยาก นี่อธิบายว่าทำไม Microsoft Copilot ยังครองตลาด enterprise แม้ Cursor / Claude Code จะดีกว่าในเชิง technical — เพราะ admin telemetry ละเอียดที่สุด

## มุม OpenBridge

ตรง use case OpenBridge มาก: ลูกค้าเป้าหมายของเราคือทีมที่จะใช้ AI agent ทำ workflow integration, ตอนนี้ผู้บริหารระดับ CIO ต้องส่ง dashboard adoption ให้บอร์ด — แปลว่า product ของเราต้อง emit telemetry ที่ดี (เช่น "agent X ทำ task Y สำเร็จกี่ครั้ง, save time เท่าไหร่ ต่อ user, ต่อ team") ตั้งแต่ day one ไม่ใช่ feature later

Adjacent insight: ถ้า JPMorgan ลงทุนระดับนี้กับ engineer adoption แล้ว ก็แปลว่าทีม non-engineer (operations, finance, sales) เป็น next frontier ที่ยังไม่ถูก mandate — แต่จะตามมาแน่นอน OpenBridge มี window 12 เดือนที่จะเข้าตลาด non-engineer integration use case (เช่น sales ops, finance ops connecting tools) ก่อนที่ enterprise จะเริ่ม mandate adoption ใน function เหล่านั้น และเริ่ม consolidate vendor — ตอนนี้ตลาดยัง fragment, openings ยังกว้าง

## Sources
- [JPMorgan Ties Engineer Performance Reviews to AI Tool Adoption for 65,000 Staff (Let's Data Science)](https://letsdatascience.com/blog/jpmorgan-tracks-65000-engineers-ai-usage-performance-reviews)
- [JPMorgan Chase ties software engineers' performance ratings to AI use (NewsBytes)](https://www.newsbytesapp.com/news/business/jpmorgan-chase-ties-software-engineers-performance-ratings-to-ai-use/tldr)
- [JPMorgan begins tracking how employees use AI at work (AI News)](https://www.artificialintelligence-news.com/news/jpmorgan-begins-tracking-how-employees-use-ai-at-work/)
- [JPMorgan Chase's AI Strategy 2026 case study (Kernel Growth)](https://kernelgrowth.io/human-oversight-ai-jpmorgan-strategy/)

---

## Audio script
ข่าวที่สองวันนี้ เรื่องที่ผมว่าจะเปลี่ยน norm ของ enterprise AI adoption ทั้งวงการ JPMorgan ตั้งแต่ปลายมีนาคมที่ผ่านมา ผูกการใช้ AI tool เป็น performance review formal สำหรับ engineer 65,000 คน มี dashboard track GitHub Copilot usage แบ่ง 3 tier light user, heavy user, non-user ผู้จัดการเห็น adoption rate ของ team รายสัปดาห์ คือไม่ใช่ recommendation soft ๆ แล้ว ถ้าไม่ใช้ AI tool คะแนน how-you-achieve ต่ำ กระทบ bonus กระทบโปรโมท ตัวเลขของ JPMorgan เองก็โหดนะครับ มี 450 use case ใน production แล้ว เป้าจะแตะ 1,000 ภายในสิ้นปี LLM Suite ภายในมี active user 200,000 คน save ได้ 1.5 พันล้านดอลลาร์จาก fraud trading operations มุมมองผมคือ ตอน cloud migration ใช้เวลา 5 ปีกว่าจะ formalize cloud-first เป็น KPI แต่ AI รอบนี้ใช้เวลา 18 เดือนเอง เพราะ telemetry มาตั้งแต่ tool measurement ง่ายกว่ามาก สำหรับ OpenBridge มี implication ตรงเลยครับ product เราต้อง emit telemetry ดี ตั้งแต่ day one ไม่ใช่ feature later เพราะลูกค้าระดับ CIO ตอนนี้ต้อง report dashboard adoption ให้บอร์ด tool ไหน produce dashboard ได้ละเอียดได้เปรียบ ต่อให้เก่งน้อยกว่าก็ยังชนะครับ
