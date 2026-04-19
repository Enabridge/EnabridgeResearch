---
date: 2026-04-19
slug: rebar-14m-vertical-ai-hvac
topic: use-case
reading_time_min: 5
sources: 4
image_prompt: Editorial illustration of an architectural blueprint being automatically annotated with glowing symbols and bounding boxes, computer vision overlay effect, minimal flat shapes, muted blueprint-blue and warm orange palette, dramatic lighting, no text no logos no faces
image:
---

# Rebar ปิด Series A $14M — vertical AI ที่ทำ HVAC quote เร็วขึ้น 60-70% + win rate 2-3× โดย founded แค่ 18 เดือน

## TL;DR
- **Rebar** (NY, founded ต.ค. 2024) ปิด **Series A $14M** นำโดย Prudence — Zero Infinity Partners, Founder Collective, Villain Capital, Optimist Ventures ร่วม
- ใช้ **computer vision** อ่าน construction blueprint อัตโนมัติ: ระบุ + นับ + categorize HVAC/electrical/plumbing equipment → ออก bill of materials + quote
- ผลลัพธ์ลูกค้า: **quote generation เร็วขึ้น 60-70%**, win rate สูงขึ้น **2-3×** (early data จาก customer interviews)
- **ARR doubled ใน 6 สัปดาห์แรกของ 2026** — growth rate ที่แทบไม่เห็นใน construction tech

## เกิดอะไรขึ้น

Rebar ประกาศปิด Series A $14M เมื่อ 10 เม.ย. 2026 นำโดย Prudence — VC ที่ focus vertical software. บริษัท founded ต.ค. 2024 ที่ New York โดย Aaron Shapiro (CEO, เคย Huge agency) + co-founder จาก engineering background; ตอนนี้ทีม ~25 คน

**Core product** ฟังดูง่ายแต่ทำยากมาก — **AI operating system สำหรับ commercial HVAC/electrical/plumbing supplier**. ปัญหาคือ supplier เหล่านี้ต้องอ่าน construction blueprint (pdf หลาย 100 หน้า) แล้วคำนวณออกมาว่า project ใหม่ต้องใช้ compressor/damper/duct/panel เท่าไหร่ ราคารวมเท่าไหร่ — ตอนนี้ใช้คนนั่ง annotate blueprint ใช้เวลา 4-8 ชั่วโมงต่อโครงการ

**Rebar ใช้ proprietary computer vision model** (train บน blueprint dataset เฉพาะ) อ่าน blueprint อัตโนมัติ:
- ระบุทุก equipment (rooftop unit, air handler, VAV box, fire damper, ฯลฯ)
- นับจำนวน + categorize ตาม spec
- match กับ catalog ของ supplier → ออก bill of materials
- generate quote ที่ส่งลูกค้าได้ทันที

**ตัวเลขที่ investor ซื้อ:**
- **60-70% faster quote generation** เทียบ manual
- **Win rate สูงขึ้น 2-3×** — ไม่ใช่แค่เร็ว แต่ราคาแม่นกว่า + ส่งทันคู่แข่ง (ขาไวสำคัญเพราะ construction bid ปิดใน 72 ชม.)
- **ARR doubled ใน 6 สัปดาห์แรกของ 2026** — ถ้า annualized = growth rate ~500%+ YoY
- **Construction การตลาด US** = $2T/year; HVAC segment alone = $200B/year; supplier share = ~20% = $40B TAM

Shapiro บอก Crunchbase ว่า "เราไม่ใช่ horizontal AI tool. เราขาย HVAC supplier ที่ specific — คนที่เข้าใจว่า duct diameter 18 vs 20 นิ้ว ต่างกันอย่างไรในราคา project $5M"

## ทำไมสำคัญ

**Rebar = signal ของ "vertical AI 2.0" — ลงลึกมากกว่าแค่ horizontal copilot.** ปี 2023-2024 AI tool ส่วนใหญ่เป็น "ChatGPT wrapper สำหรับ industry X" — เปลี่ยน system prompt เฉย ๆ, moat ต่ำ. Rebar ลงลึก:
- **proprietary dataset** ของ blueprint annotated (ไม่มีใน public)
- **computer vision model** train เฉพาะ (ไม่ใช่ CLIP หรือ generic vision)
- **domain-specific post-processing** (code compliance, product compatibility, regional spec)
- **workflow integration** กับ supplier catalog (Trane, Carrier, Daikin, Johnson Controls)

**Comparable:** บริษัทใกล้เคียง — **iBeam** (concrete/rebar takeoff), **Togal.AI** (blueprint AI general), **Billd** (construction fintech) — แต่ Rebar เป็นคนเดียวที่โฟกัส HVAC supplier side (ไม่ใช่ general contractor หรือ sub); narrow อย่างแรง, moat ลึก

**Pattern ที่เห็น:** investor อย่าง Prudence, Founder Collective, Villain Capital เริ่มเทเงินเข้า **vertical AI ที่เป็น "boring industry"** — HVAC, construction, legal discovery, medical billing, insurance claim. เพราะ:
1. Horizontal AI (ChatGPT, Copilot) ถูก commoditize ใน 2025-2026 แล้ว
2. Vertical AI มี **data moat + workflow moat** ที่ยาก disrupt
3. Boring industry = CFO ชอบเพราะ ROI วัดได้ชัด (quote 4 ชม. → 1 ชม. = $500/quote × 1,000 quotes/year = savings ชัดเจน)

**เทียบ Hilbert ($28M a16z) ที่ brief เมื่อเช้า:** ทั้งคู่เป็น vertical AI — Hilbert ขาย retail/QSR (pricing decisions), Rebar ขาย HVAC supplier (quoting). Pattern เดียวกัน: **narrow vertical + hard numbers + revenue share หรือ per-outcome pricing**. กลาย ๆ ว่า a16z กับ Prudence เห็น thesis ตรงกันในสัปดาห์เดียว

## มุม OpenBridge

**Vertical AI = คือโอกาสของ OpenBridge สำหรับ Thai SMB.** HVAC ในไทยก็มีปัญหาเดียวกัน — Hatari, Panasonic, Mitsubishi, Daikin ขายผ่าน supplier 100+ ราย ที่ต้อง quote ตาม blueprint สถาปนิก. Thai construction industry = ~$60B/year; HVAC segment ~$6B. ถ้า OpenBridge build หรือ partner กับ Rebar-equivalent ไทย (หรือ reseller Rebar เลย) = niche $100-500M revenue opportunity

**Pattern ที่ copy ได้ทันที:**
1. **Proprietary training data** — OpenBridge มีลูกค้าเจ้าใหญ่ที่ให้ data หรือไม่? ถ้ามี Thai-specific dataset = moat จริง
2. **Per-outcome pricing** — เลิกคิด SaaS flat fee; คิด % ของ revenue ที่ลูกค้าสร้างจากการใช้เรา (เหมือน Rebar + Hilbert)
3. **Narrow vertical, deep integration** — แทน "AI platform for SMB" ลองเลือก 1 vertical ที่ OpenBridge รู้จักดี (e-commerce ops? logistics? accounting?) แล้วลงลึกมาก — เลียนแบบ Rebar ที่ลงไปถึงระดับ "duct diameter spec"

**ระวัง platform risk จาก foundation model vendor.** Rebar ไม่เปิดเผยว่าใช้ model ไหน — น่าจะ fine-tune open weight (CLIP derivative หรือ Qwen2-VL). ถ้าใช้ Claude vision หรือ GPT vision ผ่าน API = margin ลง + ราคา API อาจขึ้นโดยไม่ทัน. **OpenBridge ควรมี plan B ด้าน model supply** ตั้งแต่วันแรก

## Sources
- [Crunchbase News — Rebar Lands $14M for AI HVAC Quotes](https://news.crunchbase.com/real-estate-property-tech/ai-generated-hvac-quotes-rebar-seriesa/)
- [BusinessWire — Rebar Closes $14M Series A Led by Prudence](https://www.businesswire.com/news/home/20260310158768/en/Rebar-Closes-$14M-Series-A-Led-by-Prudence-to-Rapidly-Scale-its-AI-Platform-for-HVAC-Electrical-and-Plumbing-Industries)
- [BriefGlance — Rebar Raises $14M to Overhaul Construction Trades](https://briefglance.com/articles/rebar-raises-14m-to-overhaul-construction-trades-with-vertical-ai)
- [Ventureburn — Rebar Raises $14M to Expand AI Platform](https://ventureburn.com/rebar-raises-14-million-hvac-ai/)

---

## Audio script
Rebar ปิด Series A 14 ล้านดอลลาร์นำโดย Prudence. บริษัท founded ตุลาคม 2024 ที่นิวยอร์ก — founded แค่ 18 เดือน ปิด A แล้ว. Product คือ AI ที่อ่าน construction blueprint อัตโนมัติสำหรับ HVAC supplier.

ตัวเลขที่ investor ซื้อ — quote generation เร็วขึ้น 60 ถึง 70% เทียบ manual, win rate สูงขึ้น 2 ถึง 3 เท่า, และ ARR double ใน 6 สัปดาห์แรกของปี 2026. Growth rate แบบนี้ไม่ค่อยเห็นใน construction tech.

ทำไมสำคัญ? เพราะ Rebar คือ signal ของ vertical AI 2.0 — ลงลึกกว่าแค่ ChatGPT wrapper. บริษัทมี proprietary dataset ของ blueprint annotated ตัวเอง, computer vision model train เฉพาะ, domain-specific post-processing สำหรับ code compliance, และ workflow integration กับ supplier catalog อย่าง Trane, Carrier, Daikin.

Pattern investor เริ่มเทเงินเข้า boring industry — HVAC, construction, legal discovery, medical billing — เพราะ horizontal AI ถูก commoditize ไปแล้ว แต่ vertical AI มี data moat จริง CFO ชอบเพราะ ROI วัดได้ เทียบกับ Hilbert ที่ a16z ลงเมื่อเช้า — pattern เดียวกัน vertical แคบ ตัวเลขชัด per-outcome pricing.

สำหรับ OpenBridge — Thai construction industry 60 พันล้านดอลลาร์ต่อปี HVAC 6 พันล้าน. มีโอกาสชัดที่ OpenBridge หรือ partner จะสร้าง Rebar ไทย. Pattern copy ได้ทันที — proprietary Thai dataset, per-outcome pricing, narrow vertical ลงลึกเหมือน Rebar. เลิกเป็น AI platform กว้าง ๆ — เลือก 1 vertical ที่เรารู้จริงแล้วทำลึกให้ไม่มีใครตาม.
