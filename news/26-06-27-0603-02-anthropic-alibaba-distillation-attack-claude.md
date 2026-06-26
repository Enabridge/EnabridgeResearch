---
date: 2026-06-24
slug: anthropic-alibaba-distillation-attack-claude
topic: openbridge-trend
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial illustration of a glowing orange Claude logo orb in a fortified
  vault, with thousands of tiny shadowy figures siphoning streams of light
  through fake account portals on the wall toward a distant red Alibaba/Qwen
  silhouette in the background. Large floating numerals "28.8M exchanges"
  and "25,000 accounts" hover prominently above the scene, with smaller
  tags "Apr–Jun 2026" and "distillation" pinned to a wall report. Render
  style: cinematic editorial illustration, dramatic chiaroscuro lighting
  warm amber from Claude vault contrasted against cool red shadow on the
  far side, high-contrast typography legible at 200px thumbnail. No real
  human faces — only silhouettes.
image: images/26-06-27-0603-02-anthropic-alibaba-distillation-attack-claude.png
---

# Anthropic แจ้ง Senate — Alibaba รัน 28.8 ล้าน query ผ่าน 25,000 บัญชีปลอม distill Claude สำเร็จระดับใหญ่ที่สุดที่เคยมี

## TL;DR
- 24 มิ.ย. Anthropic ส่งหนังสือ Senate + White House กล่าวหา Alibaba (ผ่าน Qwen research arm) ว่ารัน distillation attack ใหญ่สุดที่เคยมีต่อ Claude — 28.8M exchanges, ~25,000 fake accounts, ระหว่าง 22 เม.ย. – 5 มิ.ย. 2026
- Campaign target เฉพาะ agentic reasoning + software engineering capability ของ Claude — segment ที่ Anthropic mark ว่า "frontier capability" และเป็น 40%+ revenue
- Pattern ก่อนหน้ามี DeepSeek/Moonshot/MiniMax (รวม 16M exchanges) — เป็น signal ว่า distillation จาก US frontier model เป็น nation-state-level strategy ของจีน, ไม่ใช่ individual research

## เกิดอะไรขึ้น

24 มิ.ย. 2026 Anthropic ส่งจดหมายเป็นทางการถึง U.S. Senate และ White House กล่าวหาว่า **Alibaba** โดยเฉพาะหน่วย Qwen AI research division — รัน **distillation attack** ขนาดใหญ่ที่สุดเท่าที่ Anthropic เคย detect ต่อ Claude ตั้งแต่ 22 เม.ย. ถึง 5 มิ.ย. 2026 รวม **28.8 ล้าน exchange** ผ่าน **~25,000 fraudulent accounts** ที่สมัครด้วย credential ปลอม + payment proxy หลายชั้น Anthropic อ้างว่าระบุตัวตน operator ที่ "affiliated with Alibaba" ได้ผ่าน account fingerprint, payment trail, และ query pattern ที่ตรงกับ training data harvesting

ของจริงที่สำคัญคือ **target** — campaign นี้ไม่ได้ลอกความรู้ทั่วไป แต่ focus ที่ **agentic reasoning** (multi-step planning, tool use orchestration) และ **software engineering** (code synthesis, debugging, repository-level edit) ซึ่งเป็น capability ที่ Anthropic เรียกว่า "frontier" และเป็นจุดที่ Claude Code ครองตลาด 40% ของ generative AI coding market เลข Mordor Intelligence มิ.ย. 2026 บอกว่าตลาด AI coding tools มีมูลค่า $9.3B ในปี 2026 และโต 26% ต่อปี — Anthropic ระบุว่า Alibaba เลือก target capability ที่เป็น revenue engine โดยตรง ไม่ใช่ research curiosity

เทียบเคียงกับเหตุการณ์ก่อน — กุมภาพันธ์ 2026 Anthropic เคย disclose ว่า DeepSeek, Moonshot และ MiniMax รัน distillation attack รวม 16M exchanges ผ่าน 24,000 accounts ครั้งนั้น Anthropic แค่ ban + tighten verification campaign Alibaba ครั้งนี้ใหญ่กว่า ~80% และ Anthropic ตัดสินใจ escalate ถึง White House และ Senate Intelligence Committee ตรง ๆ — บอกเป็น "nation-state-level concern" ที่ไม่ใช่แค่ ToS violation

ในจดหมาย Anthropic เสนอ 3 มาตรการเป็นทางการ: (1) export control บน "high-volume API access" สำหรับเอนทิตีจีน, (2) mandatory screening pattern ของ query ปริมาณสูงโดย US frontier lab, (3) coordinated industry-government action เพื่อแบ่งปัน detection signature ระหว่าง OpenAI, Google, Anthropic, Microsoft Alibaba ปฏิเสธโดยตรงและบอกว่า "ไม่มี policy รัน distillation attack" — แต่ Pentagon เพิ่ง classify Alibaba เป็น "Chinese military company" เมื่อต้นเดือน making การ rebuttal ยากกว่าเดิม

## ทำไมสำคัญ

เรื่องนี้เปลี่ยน **threat model** ของ API platform ทุกราย — distillation 28.8M exchange คือ scale ที่ rate limit แบบทั่วไป ไม่ catch ทันแน่นอนถ้า attacker grouping account หลายหมื่นแบบ horizontal Anthropic ตอบโต้ด้วยการเสนอ **verification + payment screening + query pattern fingerprint** ซึ่งหมายความว่า industry pattern กำลังย้ายจาก "API key + Stripe" เป็น "KYC ระดับธนาคาร" สำหรับ frontier model — ทุก enterprise platform ที่ resell หรือ proxy frontier model API จะต้อง implement compliance layer แบบเดียวกัน ไม่ใช่แค่ relay token

มี angle เชิงภูมิรัฐศาสตร์ที่ใหญ่กว่า — Anthropic ใช้เคสนี้ lobby export control เป็นทางการ ซึ่งถ้า Congress ผ่าน "AI export control" คล้าย chip export control ของ Bureau of Industry and Security ตอนนี้ "API access" จะถูก treat เป็น dual-use technology ที่ต้องขอ license ส่งออก สำหรับ AI startup ใน Asia (รวมไทย, สิงคโปร์, มาเลย์) นี่หมายความว่า upstream model access อาจไม่ free flow อีกต่อไป — ต้องมี audit trail, customer attestation, end-use clause ในสัญญา ราคา compliance จะกระชับ margin ของ reseller/integration tier

ที่ subtle กว่านั้น Anthropic ส่ง message ทาง market ด้วย — บริษัทที่กำลังจะ IPO ต้อง demonstrate ว่า "moat" ของ frontier capability ไม่หายไปง่ายผ่าน distillation การ frame ตัวเองว่าเป็น "victim ของ state-level theft" คือการบอก investor ว่า "moat ของเรามีค่ามากพอจะถูก attack ระดับนี้" — และพร้อม push policy ที่ปกป้อง moat ต่อ ถ้า Anthropic ผลักดัน export control สำเร็จ มันจะเป็นการสร้าง regulatory moat ที่ทำให้ Chinese open model (Qwen, DeepSeek) ตามไม่ทันใน US enterprise market

## มุม OpenBridge

Direct relevance: OpenBridge ที่ proxy frontier model API ต้อง prepare สำหรับ "compliance layer ระดับธนาคาร" ที่จะตามมาภายใน 12 เดือน — ไม่ใช่แค่ verify email + Stripe แต่ต้อง implement KYC, sanctions screening, query pattern fingerprinting, anomaly alerting ลูกค้า enterprise จะถาม "ระบบของคุณตรวจ distillation attack ได้ไหม" เป็นคำถาม sales อันดับต้น ๆ ภายใน Q3 OpenBridge ที่ตอบไม่ได้จะเสีย deal ระดับ Fortune 500 ทันที — ในทางกลับกัน ถ้า build feature นี้ได้ก่อน นี่คือ pricing premium ที่ defensible

มี opportunity บน positioning ด้วย — OpenBridge อยู่ในตำแหน่ง neutral integration layer ที่สามารถ aggregate signal cross-customer ได้ ถ้า design ระบบ central anomaly detection ที่ pool signal จากลูกค้าหลายรายโดยไม่ leak data (federated detection) แต่ละลูกค้าจะ benefit จาก threat intelligence ของลูกค้ารายอื่น — pattern ที่ Cloudflare ทำกับ DDoS detection หรือ Crowdstrike ทำกับ endpoint นี่คือ business model ที่ scale ตามจำนวนลูกค้า ไม่ใช่ตาม token volume — และเป็น lock-in ที่แท้จริง

## Sources
- [Anthropic Accuses Alibaba Of Running 29 Million Fake Queries to Clone Claude — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-accuses-alibaba-of-running-29-million-fake-queries-to-clone-claude/)
- [Anthropic accuses Alibaba of campaign to 'brazenly' and 'illicitly' extract AI capabilities — CNBC](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html)
- [Anthropic claims that China's Alibaba used 25,000 fake accounts and 28.8 million exchanges to illicitly 'distill' its Claude model — Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude)
- [Alibaba Ran Largest Known AI Theft Campaign Against Claude, Anthropic Tells Senate — TechTimes](https://www.techtimes.com/articles/319105/20260625/alibaba-ran-largest-known-ai-theft-campaign-against-claude-anthropic-tells-senate.htm)
- [Inside Anthropic's Claims of Distillation Attack by Alibaba — Cybersecurity Magazine](https://cybermagazine.com/news/inside-anthropics-claims-of-distillation-attack-by-alibaba)
- [Anthropic Writes To White House Accusing Alibaba Of "Illicitly" Accessing Claude AI Models — Stocktwits](https://stocktwits.com/news-articles/markets/equity/anthropic-writes-to-white-house-accusing-alibaba-of-illicitly-accessing-claude-ai-models/cZKyprTR7Qd)

---

## Audio script
ครับ Yoh เรื่องที่สองวันนี้ Anthropic ส่งหนังสือถึง Senate กับ White House เป็นทางการ กล่าวหา Alibaba ผ่านหน่วย Qwen research arm ว่ารัน distillation attack ขนาดใหญ่ที่สุดเท่าที่เคย detect ต่อ Claude ตั้งแต่ 22 เมษายน ถึง 5 มิถุนายน รวม 28.8 ล้าน exchange ผ่าน 25,000 บัญชีปลอม ที่ target ตรง ๆ คือ agentic reasoning กับ software engineering capability ของ Claude ซึ่งเป็น revenue engine ที่ Claude Code ครองตลาด AI coding 40% เทียบกับเหตุการณ์ DeepSeek กับ Moonshot เมื่อกุมภาพันธ์ที่ผ่านมา ครั้งนี้ใหญ่กว่า 80% และ Anthropic ตัดสินใจ escalate ถึง Senate Intelligence Committee ตรง ๆ บอกว่าเป็น nation state level concern ในจดหมาย Anthropic เสนอสามมาตรการ หนึ่ง export control บน high volume API access สำหรับเอนทิตีจีน สอง mandatory screening pattern ของ query ปริมาณสูง สาม coordinated industry government action เพื่อแบ่งปัน detection signature ระหว่าง frontier lab สำหรับ OpenBridge มีสองเรื่องที่ต้อง take away หนึ่ง threat model ของ API platform เปลี่ยน ต้อง prepare compliance layer ระดับธนาคารภายใน 12 เดือน ทั้ง KYC sanctions screening กับ anomaly detection ลูกค้า enterprise จะถามเรื่องนี้เป็นคำถาม sales อันดับต้น ๆ ภายใน Q3 ปีนี้ สอง มี opportunity บน positioning ถ้า OpenBridge design federated detection ที่ pool signal cross customer โดยไม่ leak data ลูกค้าทุกรายจะ benefit จาก threat intelligence ของลูกค้ารายอื่น pattern แบบที่ Cloudflare ทำกับ DDoS หรือ Crowdstrike ทำกับ endpoint นี่คือ business model ที่ scale ตาม customer count ไม่ใช่ token volume ครับ
