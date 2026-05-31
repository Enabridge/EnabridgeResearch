---
date: 2026-05-31
slug: anthropic-965b-opus-48-mythos
topic: agentic-ai
reading_time_min: 6
sources: 6
image_prompt: |
  Editorial hero illustration: a colossal stylized "$965B" carved from indigo marble
  rising above a small "OpenAI" silhouette pedestal at its base, dramatic chiaroscuro
  side-lighting from the right, golden filaments of light streaming up from data-server
  silhouettes labeled "Claude Enterprise" forming the marble's foundation, in the upper
  corner a small Anthropic spiral mark glowing amber. Flat editorial poster style, muted
  navy and amber palette, high contrast for 200px thumbnail, square 1:1 composition,
  no real human faces, allow logos and text.
image: images/26-06-01-0609-01-anthropic-965b-opus-48-mythos.png
---
# Anthropic ทะยานข้าม OpenAI ที่ $965B — $47B ARR, Opus 4.8, Mythos กำลังเปิดให้ทุกคน

## TL;DR
- **Anthropic ระดม $65B รอบใหม่ valuation $965B** (28 พ.ค.) — แซง OpenAI ทั้ง market value และ revenue ที่ report. ARR ตอนนี้ **$47 พันล้าน** (เพิ่มจาก ~$5B ปลายปีที่แล้ว)
- **Opus 4.8 ออกพร้อมกัน** — 42 วันหลัง Opus 4.7 (ช่วงห่างสั้นที่สุดในประวัติ Opus series). misaligned behavior ลดลง 4 เท่า; top OpenAI GPT-5.5 และ Gemini 3.1 Pro ใน benchmark agentic coding, financial analysis, computer use
- **Mythos กำลังเปิดให้ "ทุกลูกค้าในไม่กี่สัปดาห์"** — model ที่หา 0-day ใน FFmpeg อายุ 16 ปี, chain Linux kernel privilege escalation, และ OpenBSD integer overflow อายุ 27 ปี
- **BMS deploy Claude ให้ 30,000 พนักงาน** เป็น "shared intelligence platform" — pharma single-vendor AI deal ขนาดใหญ่ที่สุดเท่าที่เคยมีมา

## เกิดอะไรขึ้น

วันที่ 28 พฤษภาคม Anthropic ประกาศปิด funding round ใหม่ที่ระดม **$65 พันล้าน** ที่ valuation **$965 พันล้าน** — ตัวเลขที่ทำให้ Anthropic กลายเป็น **AI startup ที่มีมูลค่าสูงที่สุดในโลก** แซง OpenAI ทั้งใน market cap และ reported revenue เป็นครั้งแรกตั้งแต่ Claude เปิดตัว. ตัวเลข ARR ที่ Anthropic ยอมเปิดเผยคือ **$47 พันล้าน** — เพิ่มจาก ~$5B ปลายปี 2025 = **เกือบ 10 เท่าใน 6 เดือน**

ในวันเดียวกัน Anthropic ปล่อย **Claude Opus 4.8** — 42 วันหลัง Opus 4.7 ออก (เป็น release cadence ที่สั้นที่สุดในประวัติ Opus series). evaluation ภายในของ Anthropic เองบอกว่า Opus 4.8 มี rate ของ misaligned behavior (deception + cooperation กับ misuse) **ลดลง ~4 เท่า** จาก 4.7, และ top OpenAI GPT-5.5 + Google Gemini 3.1 Pro ใน benchmark **agentic coding, financial analysis, computer use** — สามอันที่ enterprise buyer สนใจที่สุด

ที่ทำให้นักลงทุนถึงยอมจ่าย $965B คือ **Mythos**. Anthropic บอกในประกาศเดียวกันว่ากำลังจะเปิด Mythos-class models ให้ "ทุกลูกค้าในไม่กี่สัปดาห์" — preview ก่อนหน้านี้จำกัดให้แค่ Apple, Amazon, JPMorgan Chase, Palo Alto Networks. Mythos ออกแบบเฉพาะ **cybersecurity + autonomous coding + long-running agents** — ผลงานที่ผ่านมาคือหา 0-day vulnerability ใน FFmpeg ที่ automated test ตี 5 ล้านครั้งแล้วไม่เจอ (อายุ 16 ปี), chain หลาย vuln ของ Linux kernel ให้ทำ privilege escalation จาก user ทั่วไปไปเป็น root, และเจอ integer overflow ใน OpenBSD อายุ 27 ปี

และเพื่อ prove ว่า ARR $47B ไม่ใช่แค่ token revenue จาก hobbyist, Anthropic ปล่อยข่าวคู่กัน: **Bristol Myers Squibb (BMS) เซ็น strategic agreement** deploy Claude Enterprise เป็น "shared intelligence platform" ให้ **30,000 พนักงานทั่ว R&D, clinical, manufacturing, commercial และ corporate** — pharma single-vendor AI deal ขนาดใหญ่ที่สุดเท่าที่เคยประกาศมา. BMS บอกชัดว่าจะใช้ Claude Code เร่ง software dev, ฝัง agentic workflow เข้าทุก step ของ drug pipeline (รวมถึง flagging manufacturing deviation แบบ real-time), และ connect Claude เข้ากับ proprietary scientific data ที่ silo มา 30 ปี

## ทำไมสำคัญ

ตัวเลขที่สำคัญที่สุดไม่ใช่ $965B แต่เป็น **$47B ARR** — แปลว่า revenue multiple ของ Anthropic อยู่ที่ ~20x, **ต่ำกว่า** OpenAI ที่ประมาณ 30-40x ARR ในรอบล่าสุด. นั่นแปลว่า late-stage investor มอง Anthropic เป็น **business ที่ economic ติด ground แล้ว** ไม่ใช่ moonshot. ในวงการ enterprise software นี่คือ inflection point — เหมือนตอน Salesforce ผ่าน $1B ARR ปี 2009 เปลี่ยน narrative จาก "SaaS bubble?" เป็น "SaaS is the default"

Mythos ขยายไป general availability คือ **second inflection** ที่อาจ define ปี 2026-2027. Model ที่หา 0-day อายุ 27 ปีได้แบบ autonomous = เปลี่ยน economics ของทั้ง security industry: red team consulting (~$30B market) ส่วนใหญ่กลายเป็น commoditized; ในทาง flip side มัน lower bar ให้ attacker — กังวลตรงนี้ใหญ่พอที่ CETaS (Centre for Emerging Technology and Security ของ UK) และ Bain & Company ทั้งคู่ออก report เตือนแยกกันว่า "AI cybersecurity wake-up call". Anthropic จำกัด preview ไว้ที่ 4 บริษัทอเมริกัน — ตอนนี้กำลังจะ release wide, แปลว่าอีกไม่กี่สัปดาห์ทุก SaaS ที่มี exposed endpoint = subjective ของ Mythos-class agent ที่ทำงาน 24/7

Pattern ที่เห็นชัดในรอบนี้: **Anthropic ทำ enterprise; OpenAI ทำ consumer**. Cognition $1B ที่ระดมสัปดาห์ก่อน, Cursor หลายร้อยล้าน, BMS 30K seats — ทั้งหมดใช้ Claude เป็น backbone. OpenAI ยังครอง consumer mindshare ผ่าน ChatGPT, แต่ enterprise budget cycle ของ 2026 H2 บอกว่า **Claude Enterprise คือ default choice** สำหรับ regulated industry (pharma, finance, defense). ถ้า trajectory นี้ยืน 2 quarter ติด — narrative "OpenAI vs Anthropic" จะเปลี่ยนเป็น "OpenAI = ChatGPT brand, Anthropic = AI infrastructure of enterprise"

## มุม OpenBridge

**Bet ของ OpenBridge บน Claude ในชั้น orchestration ได้ proof point ระดับ macro แล้ว** — Anthropic ผ่าน $47B ARR + valuation premium = signal ว่า platform risk ต่ำลงมาก. ถ้า OpenBridge ทำ integration กับ Claude tool use / MCP เป็น first-class, ตอนนี้คือเวลา double down — ไม่ใช่ hedge ไปทุก provider. SMB ไทยกำลังตามทาง pharma/finance ของ US ภายใน 12-18 เดือน

**ที่ต้อง watch คือ Mythos rollout**. ถ้า Mythos GA ในเดือนหน้า + ราคา accessible = OpenBridge มี opportunity ทำ **"managed Mythos for SMB"** — wrap Mythos audit ในชั้น compliance ของไทย (PDPA + ISO 27001), ขายเป็น quarterly security audit service ($10-30K/quarter). ตลาดนี้ในไทยยังไม่มีใคร own; first-mover ได้ทั้งหมด. แต่ต้องระวัง — ถ้า OpenBridge expose endpoint เอง = Mythos ทั่วโลกที่ run โดย attacker จะ scan OpenBridge เอง ภายในสัปดาห์แรกที่ release wide

## Sources
- [Fortune — Anthropic leapfrogs OpenAI with a record $965 billion valuation](https://fortune.com/2026/05/29/anthropic-raises-65-billion-at-record-965-billion-valuation-promises-mythos-ai-model-in-wide-release-in-coming-weeks-releases-claude-opus-4-8/)
- [BMS Press Release — Strategic Agreement with Anthropic to Position Claude Enterprise as the Shared Intelligence Platform](https://news.bms.com/news/details/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx)
- [Contract Pharma — BMS to Deploy Claude Agentic AI Across 30,000 Employees](https://www.contractpharma.com/breaking-news/bms-to-deploy-claude-agentic-ai-across-30000-employees/)
- [Bain & Company — Claude Mythos and the AI Cybersecurity Wake-Up Call](https://www.bain.com/insights/claude-mythos-and-ai-cybersecurity-wake-up-call/)
- [CNBC — Anthropic's Mythos set off a cybersecurity 'hysteria'](https://www.cnbc.com/2026/05/08/anthropic-mythos-ai-cybersecurity-banks.html)
- [TheStreet — Anthropic drops new Claude model as OpenAI IPO race heats up](https://www.thestreet.com/technology/anthropic-drops-new-claude-model-as-openai-ipo-race-heats-up)

---

## Audio script
สัปดาห์นี้ Anthropic ทำเรื่องที่ปีก่อนคนยังคิดว่าเป็นไปไม่ได้. ปิด funding round 65 พันล้านเหรียญ valuation 965 พันล้าน. แซง OpenAI เป็นครั้งแรกทั้ง market cap และ revenue. ARR ตอนนี้อยู่ที่ 47 พันล้าน. เพิ่มจาก 5 พันล้านปลายปีที่แล้วเกือบ 10 เท่าใน 6 เดือน.

ในวันเดียวกันปล่อย Opus 4.8. ห่างจาก 4.7 แค่ 42 วัน. cadence สั้นที่สุดในประวัติ Opus series. misaligned behavior ลด 4 เท่า. top GPT-5.5 และ Gemini 3.1 Pro ใน benchmark agentic coding financial analysis และ computer use. 3 อันที่ enterprise CIO สนใจที่สุด.

ที่ทำให้นักลงทุนยอมจ่าย 965 พันล้านคือ Mythos. กำลังจะเปิดให้ทุกลูกค้าในไม่กี่สัปดาห์. Mythos เคยหา zero-day ใน FFmpeg อายุ 16 ปี ที่ automated test ตี 5 ล้านครั้งไม่เจอ. chain Linux kernel privilege escalation. และเจอ integer overflow ใน OpenBSD อายุ 27 ปี. ตอน preview จำกัดให้แค่ Apple Amazon JPMorgan และ Palo Alto Networks.

และเพื่อยืนยันว่า 47 พันล้าน ARR ไม่ใช่แค่ hobbyist Anthropic ปล่อยข่าวคู่กัน. Bristol Myers Squibb deploy Claude Enterprise ให้พนักงาน 30,000 คน เป็น shared intelligence platform. pharma single-vendor AI deal ใหญ่ที่สุดในประวัติศาสตร์. ใช้ทั้ง drug pipeline manufacturing และ corporate function.

สำหรับ OpenBridge. bet ของเราบน Claude ในชั้น orchestration ได้ proof point ระดับ macro แล้ว. ถึงเวลา double down ไม่ใช่ hedge. และต้อง watch Mythos GA — ถ้าออกเดือนหน้า มี opportunity ทำ managed Mythos audit service สำหรับ SMB ไทย. แต่ต้องระวัง endpoint ของตัวเอง เพราะ Mythos ทั่วโลกที่ attacker คุมจะ scan OpenBridge ภายในสัปดาห์แรก.
