---
date: 2026-05-31
slug: openrouter-113m-series-b-25t-tokens-ai-gateway
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a colossal glowing OpenRouter router hub at the center of
  an isometric scene, with multiple thick fiber-optic data cables radiating outward
  to logos of Anthropic, OpenAI, Google, Meta, NVIDIA, and Mistral on the perimeter.
  Massive floating numerals "$1.3B valuation" and "25T tokens/week" dominate the upper
  third of the frame, with a smaller "$113M Series B" tag near the central hub. A
  faint upward growth curve labeled "5T → 25T in 6 months" arcs behind the hub.
  Style: cinematic editorial illustration, isometric perspective, electric cyan and
  Google blue lighting, high contrast, large bold typography legible at 200px
  thumbnail. No real human faces.
image: images/26-05-31-0610-02-openrouter-113m-series-b-25t-tokens-ai-gateway.png
---

# OpenRouter ระดมทุน $113M Series B ที่ $1.3B — CapitalG นำ, NVIDIA/ServiceNow/Snowflake/Databricks ตามมา เป็น signal ว่า AI router คือ infrastructure layer ที่ทุก hyperscaler ต้องมีไว้

## TL;DR
- 26–27 พ.ค. OpenRouter ปิด Series B $113M ที่ $1.3B post-money — เท่า 2.4 เท่าจาก Series A ($547M) เมื่อ มิ.ย. 2025
- นำโดย Alphabet CapitalG ร่วมกับ NVentures (NVIDIA), ServiceNow Ventures, MongoDB Ventures, Snowflake Ventures, Databricks Ventures + a16z และ Menlo Ventures
- Weekly volume กระโดดจาก 5T → 25T tokens ใน 6 เดือน (5x), serve 8M+ developers ผ่าน 400+ models — บนเส้นทางสู่ quadrillion tokens/year

## เกิดอะไรขึ้น

26 พ.ค. 2026 OpenRouter ประกาศปิด Series B มูลค่า $113 million ที่ valuation $1.3 billion — เพิ่มขึ้น 2.4 เท่าจาก Series A ที่ $547M (มิ.ย. 2025) นำโดย **CapitalG** ซึ่งเป็น growth fund อิสระของ Alphabet — น่าสังเกตว่า Google เลือกลง CapitalG ไม่ใช่ GV หมายความว่าเป็น strategic bet ขนาดใหญ่ ไม่ใช่ early-stage portfolio play

รายชื่อ co-investor น่าสนใจกว่าเงิน — **NVentures (NVIDIA), ServiceNow Ventures, MongoDB Ventures, Snowflake Ventures, Databricks Ventures** ทั้งหมดอยู่ในรอบเดียวกัน รวมกับ existing investors a16z และ Menlo Ventures นี่คือ "everyone wants in" play ที่ infrastructure player ทุกราย — chip maker, data warehouse, ServiceNow agent platform, MongoDB — ตัดสินใจ co-invest ใน middleware ที่จะ route AI workload ของลูกค้าตัวเอง

ตัวเลขที่ทำให้รอบนี้ปิดได้คือ growth: **weekly volume กระโดดจาก 5 trillion tokens → 25 trillion tokens ภายใน 6 เดือน** (5x) บริษัท claim ว่ากำลังจะทะลุ quadrillion tokens (10^15) ในปีนี้ และ serve developer 8 ล้านคน+ ที่ build บน 400+ models ผ่าน single API นี่คือ scale ที่บอกว่า OpenRouter ไม่ใช่ "API aggregator สำหรับ hackathon" อีกต่อไป — มันเป็น routing layer ที่ enterprise workload จริงเชื่อมต่อ

OpenRouter ก่อตั้งปี 2023 โดย Alex Atallah (อดีตผู้ร่วมก่อตั้ง OpenSea) และ Louis Vichy — model business คือ take fee % ของ token ที่ route ผ่าน, ลูกค้าได้ provider failover + price-quality routing + unified billing ฝั่ง model lab ก็ได้ traffic เพิ่ม ไม่ต้อง build sales channel เอง

## ทำไมสำคัญ

Pattern ที่ underrated ที่สุดในรอบนี้คือ **"control plane wars" ใน AI** — ตลอด 6 เดือนที่ผ่านมา VC ไม่ได้เทเงินไปที่ frontier model lab อย่างเดียวอีกแล้ว แต่เทไปที่ "infrastructure layer ที่ทำให้ model ใช้ได้ใน production" — OpenRouter ที่ router, Catena Labs ที่ banking-for-agents, Cloudflare ที่ MCP governance ทั้งหมดเป็น control plane ที่ commoditize foundation model layer ลง

CapitalG ลงเป็น lead แทน GV เป็น signal ว่า Google ไม่ได้กังวลว่า OpenRouter จะ route ลูกค้าออกจาก Gemini — เพราะ Gemini เป็น 1 ใน 400 models ที่ route ผ่านอยู่แล้ว ลงทุนใน router = ลงทุนใน "ตัวเลือก" ของลูกค้า ไม่ใช่ตัวเอง พูดอีกแบบคือ Google ยอมรับว่าตลาด multi-model จะอยู่ต่อไป และ neutral router คือ winner ของ landscape นั้น

25T tokens/week คือตัวเลขที่ทำให้เห็นภาพชัด — Anthropic claim ARR $47B จาก Claude API + Code, OpenAI claim revenue $122B ARR (รอบ funding ล่าสุด) — แต่ OpenRouter ที่ route ทั้งหมดนี้กำลัง process 25T tokens ต่อสัปดาห์ = ~1.3 quadrillion/ปี ถ้าสมมุติ blended price $5/M tokens, OpenRouter อยู่ในเส้นทาง gross volume $6.5B/ปี take rate แค่ 1-2% ก็คือ ARR $65-130M ซึ่งสนับสนุน $1.3B valuation ได้ — และยังโตได้อีกถ้า take rate ปรับขึ้นเมื่อ enterprise feature เพิ่มขึ้น

## มุม OpenBridge

OpenRouter pattern คือ blueprint ตรง ๆ ที่ OpenBridge ต้องดู — **routing layer ใน model space ราคาแพง** $1.3B valuation จาก take-rate model บน multi-vendor traffic แปลว่า "integration layer ที่ neutral" คือ business model ที่ตลาดยอมจ่ายเงินสูงให้ ถ้า OpenBridge build "MCP server routing + connector marketplace + neutral billing" ที่อยู่ระหว่าง enterprise และ AI agent vendor หลายเจ้า — มี playbook ตรง ๆ ให้ดูแล้ว

อีกมุม — รายชื่อ investor บอก partner landscape ที่น่าจะมาก่อน Series B ของ OpenBridge เอง: ServiceNow, MongoDB, Snowflake, Databricks ทุกรายอยากเป็น context store สำหรับ AI agent ของลูกค้า ถ้า OpenBridge เปิดให้ agent ที่ run บน Claude/GPT/Gemini เข้าถึง enterprise data ใน 4 รายนี้ผ่าน MCP — เราคือ middleware ที่ทั้ง 4 fund ต้องอยากร่วมรอบ ไม่ต่างจาก OpenRouter ที่ทุกราย co-invest

แต่ก็ต้องระวัง — **MCP servers + connector marketplace = winner-take-most game** OpenRouter ปิด volume lead ที่ทำให้ network effect ทำงาน ใครก็ตามที่จะมา compete ต้อง bootstrap volume ก่อน — และ enterprise customer จะเลือกตัวที่มี model coverage มากสุดเสมอ OpenBridge ต้อง choose battle: ถ้าจะแข่งกับ Cloudflare/OpenRouter ใน middleware layer ต้องมี vertical edge (เช่น focus Asia/SEA enterprise data sovereignty) ไม่อย่างนั้นจะถูก commodity squeeze

## Sources
- [OpenRouter Raises $113M Series B — OpenRouter Announcement](https://openrouter.ai/announcements/series-b)
- [OpenRouter more than doubles valuation to $1.3B in a year — TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/)
- [OpenRouter Hits $1.3B Valuation After $113M Series B Led by Google's CapitalG — The AI Insider](https://theaiinsider.tech/2026/05/27/openrouter-hits-1-3b-valuation-after-113m-series-b-led-by-googles-capitalg/)
- [OpenRouter Raises $113 Million CapitalG-led Series B as Weekly Volume Explodes to 25T Tokens — Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/openrouter-raises-113-million-capitalg-131500093.html)
- [AI Gateway OpenRouter Raises $113M From Google and NVIDIA to Route Between Their Models — Tech Times](https://www.techtimes.com/articles/317353/20260529/ai-gateway-openrouter-raises-113m-google-nvidia-route-between-their-models.htm)

---

## Audio script
สวัสดีครับ Yoh ข่าวที่สอง OpenRouter ปิด Series B 113 ล้านดอลลาร์ที่ valuation 1.3 พันล้าน นำโดย CapitalG ของ Alphabet พร้อมกับ NVentures ของ NVIDIA, ServiceNow Ventures, MongoDB Ventures, Snowflake Ventures, Databricks Ventures ทั้งหมดอยู่รอบเดียวกัน เรียกได้ว่าเป็น everyone wants in play เพราะทุก infrastructure player อยากอยู่ใน routing layer ที่ลูกค้าตัวเอง use ตัวเลขที่ทำให้รอบนี้ปิดได้คือ weekly volume กระโดดจาก 5 ล้านล้าน tokens เป็น 25 ล้านล้าน tokens ภายใน 6 เดือน เป็น 5 เท่า บนเส้นทางสู่ quadrillion tokens ต่อปี serve developer 8 ล้านคนผ่าน 400 models pattern ที่ underrated สุดคือ control plane wars VC เลิกเทเงินที่ frontier model lab อย่างเดียวแล้ว แต่เทไปที่ infrastructure layer ที่ทำให้ model ใช้ได้ใน production OpenRouter คือ routing, Catena คือ banking for agents, Cloudflare คือ MCP governance ทั้งหมดเป็น control plane ที่ commoditize foundation model layer ลง สำหรับ OpenBridge นี่คือ blueprint ตรงๆ routing layer ที่ neutral ราคาแพงและตลาดจ่ายเงินสูง ถ้า OpenBridge build MCP server routing บวก connector marketplace บวก neutral billing ระหว่าง enterprise และ agent vendor หลายเจ้า มี playbook ให้ดูแล้ว แต่ต้องระวัง เป็น winner take most ต้อง choose battle ถ้าจะเข้า middleware ต้องมี vertical edge เช่น focus Asia enterprise data sovereignty ไม่งั้นจะถูก commodity squeeze จาก Cloudflare กับ OpenRouter เองครับ
