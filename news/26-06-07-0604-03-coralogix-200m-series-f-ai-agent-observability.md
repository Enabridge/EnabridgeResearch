---
date: 2026-06-07
slug: coralogix-200m-series-f-ai-agent-observability
topic: openbridge-trend
reading_time_min: 3
sources: 5
image_prompt: |
  Editorial illustration of a glowing watchtower lighthouse at the center of a
  cinematic night cityscape, with sweeping radar beams scanning over hundreds of
  small robotic agent silhouettes running across translucent data pipelines and
  rooftops below. Bold floating numerals "$200M Series F" and "$1.6B valuation"
  hover above the lighthouse, with a smaller "Coralogix" tag pinned at the base.
  The watchtower has the visual language of an observability dashboard — line
  graphs, log streams, metric grids glowing on its sides. Cinematic editorial
  style, moody dark blue and amber lighting, dramatic depth, high-contrast
  typography legible at 200px thumbnail. No real human faces — only robotic
  silhouettes and data infrastructure.
image: images/26-06-07-0604-03-coralogix-200m-series-f-ai-agent-observability.png
---

# Coralogix $200M Series F ที่ $1.6B — VC กำลังเทเงินเข้า "observability for AI agents" ว่าเป็น category ใหม่

## TL;DR
- 3 มิ.ย. **Coralogix ปิด Series F $200M** นำโดย **Advent + CPPIB** + Greenfield Partners + Brighton Park Capital — valuation $1.6B post-money, total raised $550M
- **Revenue growth >60% YoY**, มี **~30 customers ที่จ่ายมากกว่า $1M ต่อปี** — มากกว่า 50% ของ enterprise customers ใช้ Olly (Coralogix AI agent) หรือ AI ของตัวเอง investigate incident ผ่าน CLI/agentic interface
- Pattern: VC เห็น **"observability stack เดิมรับ AI agent traffic ไม่ไหว"** — เกิดเป็น category ใหม่ "AI-native observability" ที่ Datadog/Splunk ต้องตามให้ทัน

## เกิดอะไรขึ้น

วันที่ 3 มิ.ย. 2026 **Coralogix** — startup observability ที่ HQ Boston ก่อตั้งโดยทีม Israeli — ประกาศปิด **Series F $200M นำโดย Advent + Canada Pension Plan Investment Board (CPPIB)** ร่วมกับ Greenfield Partners และ Brighton Park Capital valuation post-money อยู่ที่ **$1.6B** ทำให้ total raised แตะ **$550M** — นี่คือ Series F ใหญ่สุดของ vertical observability ในรอบ 12 เดือนที่ผ่านมา และเป็น signal ที่ทำให้ Datadog (mkt cap ~$50B) กับ Splunk (Cisco) ต้องอ่านอย่างละเอียด

Coralogix โต **revenue >60% YoY** มี **~30 customers ที่จ่ายมากกว่า $1M ต่อปี** — ตัวเลขที่บอกว่าไม่ใช่ SMB play แต่เป็น mid-to-large enterprise ที่จ่ายเงินจริง Ariel Assaraf (CEO) บอก TechCrunch ตรง ๆ ว่า "**มากกว่า 50% ของ enterprise customers ใช้ Olly หรือ AI ของตัวเอง investigate incident ผ่าน CLI หรือ agentic interface**" — ไม่ใช่ใช้ Coralogix dashboard แบบเดิมอีกต่อไป **AI agent กลายเป็น primary interface ของ observability ภายในเวลา 18 เดือน**

Advent + CPPIB เป็น growth fund ที่ไม่ลงทุนใน startup ทั่วไป — ลง mid-to-late stage ที่มี clear path to $5B+ exit เท่านั้น การที่ทั้งสองร่วม round หมายความว่า financial model ของ Coralogix (revenue, retention, growth, margin) **ผ่าน due diligence ที่เข้มงวด** — pattern เดียวกับที่ Stripe, Snowflake, Databricks ได้รับตอน late-stage growth ตัว Coralogix vision ที่ขายให้ VC คือ "observability stack เดิม (built for human ops engineer) รับ AI agent traffic ไม่ไหว เพราะ agent gen log + trace + metric เร็วและเยอะกว่ามนุษย์ 100–1000 เท่า"

ในวันเดียวกัน Crunchbase รายงานว่า Coralogix อยู่ใน **top 10 funding rounds ของสัปดาห์** ร่วมกับ enterprise software + space tech megarounds — confirm ว่า late-stage VC กำลัง rotate เงินกลับเข้า enterprise infrastructure หลังจากที่ปี 2024–25 หนักไปที่ foundation model lab

## ทำไมสำคัญ

นี่ไม่ใช่แค่ "Coralogix ได้เงิน" — นี่คือ **first major signal ว่า VC ยอมรับ "AI-native observability" เป็น category ใหม่** ไม่ใช่ feature ของ Datadog/Splunk เหตุผลเทคนิคชัด: AI agent **gen telemetry เร็วและเยอะกว่ามนุษย์ operator มาก** — agent หนึ่งตัวรัน background tools 50–100 calls ต่อ task, ทุก call gen log + trace + metric ในระบบ Foxconn MoMClaw ที่มีหลายร้อย agents = telemetry volume ที่ระเบิดทุกชั่วโมง observability stack เดิมที่ design มาสำหรับ "10 microservices, 100 RPS" จะระเบิดถ้า scale แบบนี้

Pattern ที่ลึกกว่า: **AI agent กลายเป็น user หลักของ observability tool** ไม่ใช่ human DevOps engineer Olly (Coralogix AI agent) + customer-built AI = >50% ของ enterprise usage — หมายความว่า UI/UX ของ observability tool กำลังถูก reshape โดย "AI-first interface" (CLI, agentic, API) ส่วน dashboard กราฟิกที่ Datadog ใช้เวลา 10 ปี build จะกลายเป็น secondary แต่ Datadog ก็มี Bits AI agent ของตัวเอง — ใครจะ ship เร็วกว่า + integrate ลึกกว่า จะชนะ

Coralogix valuation $1.6B = **8.9x ARR ตามที่ TechCrunch คำนวณ** (ARR ~$180M) — multiple ระดับนี้สูงกว่า Datadog (~10x) เพราะ growth rate สูงกว่า แต่ก็แสดงว่า public market premium ของ AI-native = 2x ของ legacy observability ถ้า Coralogix รักษาการเติบโต 60%+ ได้อีก 2 ปี = IPO ที่ valuation $5–10B เป็นไปได้

## มุม OpenBridge

Observability for AI agent **เป็น layer ที่ adjacent กับ OpenBridge โดยตรง** — ทุก agent ที่เรียกใช้ MCP server ของ OpenBridge gen telemetry ที่ enterprise security/ops team อยาก inspect (รวมถึง audit trail สำหรับ governance) **OpenBridge ควร build OpenTelemetry-compatible output ตั้งแต่วันแรก** ให้ Coralogix, Datadog, Splunk ingest ได้ตรง ๆ — ไม่ต้อง build observability ของตัวเอง แต่ partner กับ category leader

อีกมุมที่สำคัญ: ถ้า Olly + customer AI = >50% ของ Coralogix usage **agentic-first interface กำลังจะกลายเป็น default ของทุก enterprise tool** — รวมถึง integration platform OpenBridge ต้องคิดว่า **agent ของลูกค้าเรียก OpenBridge ผ่านอะไร** — MCP? CLI? Natural language API? ถ้ายังเป็น web dashboard อย่างเดียวจะตกขบวนเร็ว pattern นี้ตรงกับ Rayfin (Microsoft + Replit) + Sierra Ghostwriter — ทุกเจ้ายอมรับว่า "human ใน dashboard" = legacy UX

Series F $200M ยัง confirm thesis ว่า **infrastructure layer ของ AI agent stack คือที่ที่ VC ลงเงินใหญ่สุดในปี 2026** — observability (Coralogix), governance (Noma + Geordie), routing (OpenRouter), orchestration (Sierra) ทุกเลเยอร์ราคาแพง OpenBridge อยู่ตรง integration layer ที่ยัง emerging — โอกาส VC ลงเงินใหญ่ใน 12–18 เดือนสูง ถ้า growth + customer retention อยู่ในกรอบเดียวกับ Coralogix

## Sources
- [Coralogix raises $200M on bet that someone needs to watch the AI agents — TechCrunch](https://techcrunch.com/2026/06/03/coralogix-raises-200m-in-race-to-build-the-monitoring-layer-for-ai-agents/)
- [Coralogix Raises $200M to Scale the Observability Backbone for the Age of AI — Coralogix](https://coralogix.com/coralogix-raises-200m-to-scale-the-observability-backbone-for-the-age-of-ai/)
- [Coralogix raises $200M to scale the observability backbone for the age of AI — Advent International](https://www.adventinternational.com/news/coralogix-raises-200m-to-scale-the-observability-backbone-for-the-age-of-ai/)
- [Coralogix raises $200M led by Advent and CPPIB to monitor systems — Axios Pro](https://www.axios.com/pro/enterprise-software-deals/2026/06/03/coralogix-200m-observability-advent-cppib)
- [The Week's 10 Biggest Funding Rounds (June 5, 2026) — Crunchbase News](https://news.crunchbase.com/venture/biggest-funding-rounds-june-5-2026/)

---

## Audio script
สวัสดีครับ Yoh เช้านี้มีข่าว funding ที่ส่ง signal สำคัญ Coralogix startup observability ที่ HQ Boston ปิด Series F 200 ล้านดอลลาร์เมื่อ 3 มิ.ย. นำโดย Advent กับ Canada Pension Plan Investment Board valuation 1.6 พันล้านดอลลาร์ post-money total raised 550 ล้าน Coralogix โต revenue มากกว่า 60% YoY มี 30 customers ที่จ่ายมากกว่า 1 ล้านดอลลาร์ต่อปี ตัวเลขที่น่าสนใจสุดคือ CEO Ariel Assaraf บอก TechCrunch ตรง ๆ ว่ามากกว่า 50% ของ enterprise customers ใช้ Olly หรือ AI ของตัวเอง investigate incident ผ่าน CLI หรือ agentic interface ไม่ใช่ใช้ dashboard แบบเดิมอีกต่อไป AI agent กลายเป็น primary interface ของ observability ภายในเวลา 18 เดือน Pattern ที่ลึกกว่าคือ AI agent gen telemetry เร็วและเยอะกว่ามนุษย์ 100 ถึง 1000 เท่า observability stack เดิมรับไม่ไหว VC ยอมรับว่า AI-native observability เป็น category ใหม่ ไม่ใช่ feature ของ Datadog Splunk การที่ Advent กับ CPPIB ร่วมรอบ pattern เดียวกับ Stripe Snowflake Databricks ตอน late-stage หมายความว่า Coralogix ผ่าน due diligence ที่เข้มงวดมาก สำหรับ OpenBridge มีสองเรื่อง หนึ่ง OpenBridge ควร build OpenTelemetry-compatible output ตั้งแต่วันแรกให้ category leader ingest ได้ตรง ๆ ไม่ต้อง build observability ของตัวเอง สอง agentic-first interface กำลังจะกลายเป็น default ของทุก enterprise tool ต้องคิดว่า agent ของลูกค้าเรียก OpenBridge ผ่าน MCP CLI natural language API ถ้ายัง web dashboard อย่างเดียวจะตกขบวนเร็ว นอกจากนั้น Series F 200 ล้าน confirm ว่า infrastructure layer ของ AI agent stack คือที่ที่ VC ลงเงินใหญ่สุดในปี 2026 OpenBridge อยู่ตรง integration layer โอกาส VC ลงเงินใหญ่ใน 12 ถึง 18 เดือนสูงครับ
