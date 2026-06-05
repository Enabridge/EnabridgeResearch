---
date: 2026-06-05
slug: coralogix-200m-ai-agent-observability
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  A dramatic editorial illustration of a glowing control room with a wall
  of dark monitors showing live waveforms and traces, each labeled
  "AGENT-1", "AGENT-2", "AGENT-3" in bright cyan text. A massive central
  screen displays "CORALOGIX +$200M" in bold orange numerals with a smaller
  "$1.6B" badge. Bright red anomaly lines spike across one monitor while
  a green checkmark glows on another. The Coralogix logo is etched into
  the dark wall above. Style: cinematic editorial illustration, deep navy
  and black background, neon cyan and warm orange accents, isometric
  composition, high contrast, text legible at 200px thumbnail. No real
  human faces.
image: images/26-06-05-0609-03-coralogix-200m-ai-agent-observability.png
---

# Coralogix ระดม $200M Series F — เดิมพันว่า observability คือชั้นโครงสร้างใหม่ของ AI agents

## TL;DR
- 3 มิ.ย. Coralogix ปิด Series F $200M, valuation $1.6B post-money, นำโดย Advent + CPPIB
- Thesis: AI agents autonomous = ต้องมี monitoring/telemetry layer ใหม่ที่ logs/metrics/traces เดิมไม่พอ
- Revenue +60% YoY, ~30 ลูกค้าจ่าย >$1M/ปี (IBM, Tradeweb, JFrog), built-in agent ชื่อ Olly + MCP interface

## เกิดอะไรขึ้น

วันที่ 3 มิถุนายน 2026 Coralogix — บริษัท observability ที่ก่อตั้งใน Israel ปี 2014 และตอนนี้ HQ อยู่ Boston — ประกาศปิด Series F $200 million ที่ valuation $1.6 billion post-money รอบนี้นำโดย Advent International กับ Canada Pension Plan Investment Board (CPPIB) ร่วมด้วย Greenfield Partners และ Brighton Park Capital — รวมระดมทุนทั้งหมดถึงปัจจุบัน $550M

Thesis ของรอบนี้ตรงไปตรงมา: AI agents ที่กำลัง deploy เข้า production ในอัตราที่ระเบิด — Salesforce อ้าง 8,000 customers ใช้ Agentforce, ServiceNow + Accenture ทำ FDE program ที่ 300+ pre-built agents — ทุกตัวต้องการ telemetry layer ใหม่ที่ logs/metrics/traces แบบเดิม (ของยุค microservices) จับไม่ได้ Coralogix vote ว่าตัวเองคือ infrastructure layer ที่จะทำให้องค์กรเห็นว่า agent ทำอะไรจริง ตัดสินใจอะไร และ fail ที่ไหน — เป็น "agent-washing detector" ในตัว

Olly — built-in AI agent ของ Coralogix — กับ MCP server interface ที่เพิ่งปล่อย เป็น product layer ที่ทำให้ enterprise ลูกค้า query telemetry ผ่าน natural language ได้ (เชื่อม Claude/Codex เข้ามาตรง ๆ) จากตัวเลขเอง: revenue โต 60%+ ในปีที่ผ่านมา, ~30 ลูกค้าจ่ายเกิน $1M/ปี, มี customer 5,000+ รวม IBM, Tradeweb และ JFrog — ARR ที่แท้จริงไม่ได้เปิดเผย แต่ valuation $1.6B / Revenue multiple ของ observability ปกติ 12-15x → ประมาณ ARR ~$100-130M

แค่ 3 วันก่อน Datadog ก็ประกาศ acquire LangSmith ($350M ตามรายงาน Reuters) เพื่อเข้าตลาดเดียวกันนี้ — สัญญาณว่า observability + AI agent กำลังกลายเป็น category สงคราม

## ทำไมสำคัญ

สามตัวอย่าง pattern ที่ทำให้รอบนี้สำคัญ หนึ่ง — VC ที่นำคือ Advent + CPPIB ไม่ใช่ early-stage AI fund แต่เป็น "growth + infrastructure" capital เดียวกับที่เคยลง Datadog, Splunk และ Dynatrace แปลว่า public market กำลัง classify "AI agent observability" เป็น category infrastructure จริง ไม่ใช่ AI application — ซึ่งให้ multiple สูงกว่า + ทนวัฏจักรกว่า

สอง — Coralogix ไม่ได้ pivot ทั้งบริษัทไปขาย AI observability แบบ pure play แต่ใช้ฐาน observability ลูกค้า enterprise เดิม (12 ปีของ logs/metrics/traces) แล้ว stack agent monitoring ลงบน data layer เดียวกัน นี่คือ moat ที่ pure-play AI observability startup (Helicone, Arize, Patronus, Langfuse) สู้ได้ยาก เพราะลูกค้า enterprise ไม่อยาก deploy observability stack ใหม่อีกอัน — ตลาดกำลัง consolidate ไปทาง vendor ที่จับ "both worlds" ได้

สาม — สัญญาณที่ใหญ่กว่าคือ "agent-washing" หรือ enterprise leader 84% เคยเจอ AI agent ที่ marketing แบบ autonomous แต่จริง ๆ ทำได้แค่ retrieval (จาก Sinequa research) Coralogix ขาย "ground truth telemetry" ที่ proof ว่า agent ทำงานจริงหรือเปล่า — pattern เดียวกับช่วงปี 2018 ที่ Datadog ขาย proof ว่า microservices ทำงานจริงหรือไม่ ตอนทุกคน lift-and-shift ไป cloud คนที่ขาย "ความจริง" ได้ดีในยุคนี้ — wins ใหญ่

## มุม OpenBridge

มุมตรงสุด: ลูกค้า enterprise ของ OpenBridge ก็จะถาม "เรา audit/monitor agent ที่ run ผ่าน OpenBridge ยังไง" ภายใน 6-12 เดือน — observability ไม่ใช่ optional feature อีกต่อไป มัน table stake สอง option หลัก: (ก) build ของเราเอง — เปลือง resource + ขาย เป็น feature ของ platform, (ข) integrate กับ Coralogix/Datadog/Langfuse ทันที — เร็วและไม่ต้องสู้ตลาดที่ infrastructure capital เพิ่ง pour เข้ามา $200M

แนะนำ (ข) แต่ทำให้ "first-class" — คือใน OpenBridge config มี dropdown เลือก observability provider ได้ตั้งแต่ setup ไม่ใช่ต้อง integrate ผ่าน webhook OpenAPI ทีหลัง สิ่งที่ Coralogix ออก MCP interface แล้วทำให้เราเชื่อมเข้ามา native ได้ (agent ใน OpenBridge → ส่ง telemetry ผ่าน MCP → Coralogix) — pitch สำหรับ enterprise sales จะกลายเป็น "deploy agent ผ่าน OpenBridge แล้ว monitor ผ่าน observability stack ที่คุณใช้อยู่แล้ว ไม่ต้องเปลี่ยน vendor" เป็น sweet spot

อีกประเด็นที่ใช้ในการ positioning: OpenBridge ไม่ต้องแข่ง observability — แข่ง orchestration/integration แล้วยอมเป็น data source ของ observability tool หลายเจ้า ทำให้เรา neutral + ไม่ถูกมองว่าจะกลืน budget ของ DevOps team

## Sources
- [Coralogix raises $200M on bet that someone needs to watch the AI agents](https://techcrunch.com/2026/06/03/coralogix-raises-200m-in-race-to-build-the-monitoring-layer-for-ai-agents/)
- [Coralogix Raises $200M to Scale the Observability Backbone for the Age of AI](https://coralogix.com/blog/coralogix-raises-200m-to-scale-the-observability-backbone-for-theage-of-ai/)
- [Coralogix Raises $200M Series F to Advance AI-Native Observability Platform](https://www.hpcwire.com/bigdatawire/this-just-in/coralogix-raises-200m-series-f-to-advance-ai-native-observability-platform/)
- [Why Coralogix Raised a $200M Series F](https://newmarketpitch.com/blogs/news/coralogix-series-f-why)
- [Observability provider Coralogix nabs $200M investment](https://siliconangle.com/2026/06/03/observability-provider-coralogix-nabs-200m-investment/)

---

## Audio script
ข่าวที่สามวันนี้เป็นเรื่อง infrastructure ของ AI agent ครับ Coralogix บริษัท observability เก่าแก่ 12 ปี ที่ก่อตั้งใน Israel ปิดดีล Series F 200 ล้านดอลลาร์เมื่อวันที่ 3 มิถุนายน ที่ valuation 1.6 พันล้านดอลลาร์ นำโดย Advent กับ Canada Pension Plan Investment Board ที่น่าสนใจคือ VC ที่นำรอบนี้ไม่ใช่ early-stage AI fund แต่เป็น infrastructure capital เดียวกับที่ลง Datadog, Splunk แปลว่าตลาดกำลัง classify AI agent observability เป็น category infrastructure จริง Thesis ของ Coralogix ตรงประเด็น คือ AI agent ที่ deploy production มากขึ้นเรื่อย ๆ ทุกตัวต้องการ telemetry แบบใหม่ที่ logs metrics traces ของยุค microservices จับไม่ได้ ตัวเลข Coralogix revenue โต 60 เปอร์เซ็นต์ปีที่แล้ว มี customer ที่จ่ายเกิน 1 ล้านดอลลาร์ต่อปี ราว 30 ราย รวม IBM, Tradeweb, JFrog ที่น่าสังเกตคือ 3 วันก่อน Datadog ก็เพิ่งซื้อ LangSmith 350 ล้าน — สัญญาณว่าตลาดนี้กำลังเข้าสู่สงคราม consolidation สำหรับ OpenBridge มุมที่สำคัญ ลูกค้า enterprise จะถามว่า audit agent ที่รันผ่าน OpenBridge ยังไง ภายใน 6-12 เดือน คำตอบที่ดีคืออย่า build เอง integrate กับ Coralogix หรือ Datadog ทันที ทำให้เป็น first-class option ใน config เลย แล้ว positioning ของ OpenBridge ก็จะกลายเป็น orchestration ที่ neutral ไม่แข่งกับ DevOps budget
