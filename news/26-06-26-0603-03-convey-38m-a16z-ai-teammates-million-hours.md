---
date: 2026-06-26
slug: convey-38m-a16z-ai-teammates-million-hours
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of an empty open-plan office at dawn, with a single glowing
  desk in the foreground. On the desk sits a translucent crystal humanoid silhouette
  labeled "DIGITAL TEAMMATE", typing at a laptop. Around the room, faint customer
  logos float in soft blue (NBCU, Samsara, Unity, Faire, ChargePoint). A giant floating
  metric reads "1,000,000 HOURS AUTOMATED" and a banner pinned to the chair reads
  "$38M Series A — a16z". Render style: cinematic editorial illustration, soft golden
  morning light from window, warm-cool contrast, high-contrast typography legible at
  200px thumbnail, no real human faces — translucent silhouettes only.
image: images/26-06-26-0603-03-convey-38m-a16z-ai-teammates-million-hours.png
---

# Convey $38M Series A นำโดย a16z — "AI teammates" ไม่ใช่ "AI agents", ทำงานไปแล้ว 1 ล้านชั่วโมงให้ NBCUniversal/Samsara/Unity/Faire

## TL;DR
- 17 มิ.ย. Convey ปิด Series A $38M นำโดย Andreessen Horowitz (Joe Schmidt เข้า board), Khosla Ventures + Pear VC ร่วมรอบ; Rohan Chopra (ex-DoorDash 8 ปี) ก่อตั้ง
- Customer list จริง — NBCUniversal, Samsara, TelevisaUnivision, Unity, Faire, ChargePoint — รวมแล้วทำงาน automated ไปกว่า **1 ล้านชั่วโมง** (= 480 FTE-year ถ้าคิด 2,080 ชม./ปี/คน)
- Positioning ใหม่: ไม่ใช่ "agents that complete tasks" แต่เป็น "teammates that own an outcome" — non-technical operator build + manage ได้โดยไม่ต้องเขียน code

## เกิดอะไรขึ้น

วันที่ 17 มิ.ย. 2026 Convey ประกาศปิด Series A $38M นำโดย **Andreessen Horowitz** โดย partner Joe Schmidt จะเข้าเป็น board member, Khosla Ventures และ Pear VC ที่เป็น seed investor ก็ร่วมรอบนี้ด้วย Convey ก่อตั้งโดย **Rohan Chopra** ที่ใช้เวลา 8 ปีที่ DoorDash จนถึงระดับ leadership team — Chopra เห็นจากใน DoorDash ว่า ops team ใหญ่มาก ๆ ใช้คนมหาศาลทำงาน semi-structured ที่ workflow เปลี่ยนทุกสัปดาห์ — RPA ทำไม่ได้, traditional automation ก็ไม่ flexible พอ

ของจริงที่ Convey ขายไม่ใช่ feature — แต่เป็น **positioning** ทั้งตลาดวันนี้ขายคำว่า "AI agent" — task ที่จะ complete Convey เลี่ยงคำนี้โดยตั้งใจ, ใช้ "**digital teammate**" แทน Chopra อธิบายใน press release ว่า "teammate own an outcome" — ไม่ใช่ทำ task เสร็จแล้วจบ แต่รับผิดชอบผลลัพธ์ของกระบวนการทั้งกระบวนการ เช่น "ลด churn ของ customer tier 2 ลง 10%" ไม่ใช่ "ส่ง email 100 ฉบับ" message นี้ค่อนข้างคล้าย Cognition Devin (90% ของ code at Devin เขียนโดย Devin) — แต่ apply กับ ops ไม่ใช่ engineering

ตัวเลขที่ Convey เปิดเปิดเผยเอง — **มากกว่า 1 ล้านชั่วโมงของ work ถูก automated** ผ่าน platform (~480 FTE-year ถ้าคิดที่ 2,080 ชม./คน/ปี) Customer list ที่ confirm เป็น public reference: **NBCUniversal, Samsara, TelevisaUnivision, Unity, Faire, ChargePoint** — ทั้งหมดเป็นบริษัทระดับ Fortune 1000 หรือใกล้เคียง ไม่ใช่ tech startup ที่ try AI สนุก ๆ ที่ Convey เปิดเปลือกเล็กน้อยคือ workflow ที่ Faire ใช้ — ops team build digital teammate มา handle merchant onboarding ที่เคยใช้ analyst 8 คน, teammate ทำ 80% ของ workflow โดยไม่ต้องเขียน code

**Critical point: Convey ไม่ open code editor ให้ user เลย** — ใช้ no-code config + natural language เท่านั้น Operator ของลูกค้า (ไม่ใช่ developer) เป็นคน build teammate เอง พร้อม human-in-the-loop checkpoint ที่ owner กำหนด — เป็น product design ที่ตรงกับสิ่งที่ enterprise AI report ของ Fivetran ระบุว่า governance gap คือ bottleneck ใหญ่สุด

## ทำไมสำคัญ

**"AI teammate" vs "AI agent" คือ semantic war ที่จะกำหนด pricing model ของตลาดในอีก 2 ปี** — agents = task-based pricing (per token, per call, per task) teammates = outcome-based pricing (per FTE-replaced, per hour saved, per goal-met) ที่สอง model ต่างกันไม่ใช่แค่ revenue recognition แต่ต่างกันที่ "ลูกค้าซื้ออะไรจริง" Convey เก็บ implicit ว่า 1 ล้านชั่วโมง = ROI ที่ใช้ pitch ให้ CFO ไม่ใช่ CTO — และตลาด enterprise procurement ส่วนใหญ่กำลังจะ shift ไปทางนี้ Klarna ก็เปิดมาว่า AI agent save $60M = 853 FTE workload — ลำดับ unit นั้นเอง

**$38M Series A ที่ a16z lead ในจังหวะนี้คือ pattern signal สำคัญ** ตอนนี้ Series A median ของ agentic startup อยู่ที่ $51.9M, $100M+ round ถือเป็น standard — Convey $38M ต่ำกว่า median แต่ a16z lead = signal ที่ตลาด "look for product proof, not just team + thesis" Convey แสดง 1 ล้านชั่วโมง + Fortune 1000 customer ก่อน, ได้ Series A ที่ "ขนาดเหมาะกับ stage" — ไม่ overcap valuation, board ได้ partner ใหญ่ที่ลึก enterprise (Joe Schmidt มาจาก fintech background)

**Pattern ที่ stack กับข่าวอื่นในรอบนี้** — Klarna, JPMorgan, Convey ล้วนพูดเป็น "FTE-equivalent saved" / "hours automated" / "$ saved" CFO-language กำลังจะ dominate AI procurement story ในครึ่งหลังของ 2026 — vendor ที่ pitch ด้วย benchmark score (HumanEval, MMLU) จะแพ้กับ vendor ที่ pitch ด้วย dollars-saved

## มุม OpenBridge

มี 3 เรื่องที่ OpenBridge ต้องเรียนจาก Convey:

**หนึ่ง — pricing narrative ต้อง flip จาก usage-based → outcome-based** ตอนนี้ integration platform ทั่วโลก (Workato, Zapier, Make) ขาย per-task, per-step — OpenBridge ในยุค AI teammate ควร offer "OpenBridge Subscription per teammate-hour" model ตัวอย่าง: ลูกค้าจ่าย $X per 1,000 hours ที่ teammate ใช้ OpenBridge dispatch tool call / data pull / API write ผ่าน billing นี้ลูกค้าวัด ROI ได้ตรง CFO ไม่ต้องแปลงจาก token

**สอง — non-technical operator คือ end-user ตัวจริง** Convey ไม่เปิด code editor ให้ user — ทั้ง platform คือ no-code + natural language operator ของลูกค้า (process owner, ops manager) build teammate เองได้ OpenBridge ต้อง consider ว่า admin UI ของเราเข้าใจง่ายแค่ไหนสำหรับคนที่ไม่ใช่ developer — ไม่ใช่แค่ developer-friendly เพราะ buyer ของ OpenBridge ในเฟสถัดไปอาจไม่ใช่ CTO แต่เป็น COO/CFO ที่ implement teammate ใน ops

**สาม — Fortune 1000 reference customer = playbook ที่ต้องทำเหมือนกัน** Convey ใช้ Faire/NBCU/Samsara/Unity/ChargePoint สร้าง credibility ตั้งแต่ Series A OpenBridge ต้องคิดว่า reference customer 3-5 รายแรกที่ public ได้ในตลาดไทย/SEA ใครบ้าง — และ workflow ที่ deploy ที่ลูกค้าวัด ROI ได้ตรง ๆ คืออะไร เพราะ funding round ถัดไป VC จะถามคำถามนี้แน่นอน

## Sources
- [Convey Raises $38 Million Series A Led by Andreessen Horowitz — BusinessWire](https://www.businesswire.com/news/home/20260617486214/en/Convey-Raises-$38-Million-Series-A-Led-by-Andreessen-Horowitz-to-Automate-Enterprise-Operations-with-AI-Teammates)
- [Convey's $38M Bet on Enterprise AI Teammates — AI CERTs News](https://www.aicerts.ai/news/conveys-38m-bet-on-enterprise-ai-teammates/)
- [Convey Raises $38M Series A Led by Andreessen Horowitz — JustAINews](https://justainews.com/companies/funding-news/convey-raises-38m-series-a-led-by-andreessen-horowitz/)
- [Convey raises $38M from a16z for AI 'teammates' — The Next Web](https://thenextweb.com/news/convey-38-million-series-a-a16z-ai-teammates)
- [Convey Raises $38M Series A — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/convey-raises-38-million-series-144600199.html)

---

## Audio script
สวัสดีครับ Yoh ข่าวที่สามวันนี้ Convey เพิ่งปิด Series A 38 ล้านดอลลาร์ นำโดย a16z โดยมี Joe Schmidt เข้า board พร้อมกับ Khosla กับ Pear VC ที่เป็น seed investor ร่วมรอบด้วย ผู้ก่อตั้งคือ Rohan Chopra อดีต DoorDash 8 ปีถึงระดับ leadership team สิ่งที่ทำให้ Convey ต่างจาก agent startup ทั่วไปคือ positioning เขาเลี่ยงคำว่า AI agent โดยตั้งใจ แล้วใช้คำว่า digital teammate แทน Chopra อธิบายว่า teammate own an outcome ไม่ใช่ทำ task เสร็จแล้วจบ แต่รับผิดชอบผลลัพธ์ของกระบวนการทั้งกระบวนการ ตัวเลขที่เปิดคือ Convey ทำงาน automated ไปแล้วมากกว่า 1 ล้านชั่วโมง คิดเป็น 480 FTE-year ลูกค้าระดับ Fortune 1000 ที่ confirm public แล้วคือ NBCUniversal Samsara TelevisaUnivision Unity Faire ChargePoint workflow ที่ Faire ใช้คือ merchant onboarding ที่เคยใช้ analyst 8 คน teammate ทำได้ 80% โดยไม่ต้องเขียน code Convey ไม่เปิด code editor ให้ user เลย ใช้ no-code config กับ natural language เท่านั้น operator ของลูกค้า build teammate เองโดยที่ไม่ใช่ developer ความหมายต่อตลาดคือ AI teammate กับ AI agent คือ semantic war ที่จะกำหนด pricing model ของตลาดในอีก 2 ปี agent จะถูก pricing per token per call แต่ teammate จะ pricing per FTE replaced per hour saved per goal met เป็น CFO-language ไม่ใช่ CTO-language สำหรับ OpenBridge มี 3 เรื่องที่ต้องเรียน หนึ่งคือ pricing narrative ต้อง flip จาก usage-based ไป outcome-based offer per teammate-hour ที่ใช้ OpenBridge ลูกค้าวัด ROI ตรง CFO สองคือ buyer ของ OpenBridge เฟสถัดไปอาจไม่ใช่ CTO แต่เป็น COO หรือ CFO admin UI ต้อง non-developer-friendly สามคือ ต้องคิด Fortune reference customer 3 ถึง 5 รายแรกในไทย SEA ที่วัด ROI ได้ตรง เพราะ VC ถามคำถามนี้แน่นอนในรอบถัดไปครับ
