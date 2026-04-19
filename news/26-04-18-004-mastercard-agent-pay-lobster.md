---
date: 2026-04-18
slug: mastercard-agent-pay-lobster
topic: use-case
reading_time_min: 2
sources: 2
---

# Mastercard + Lobster.cash ให้ AI agent รูด Mastercard เดิมของลูกค้าได้โดยไม่โชว์เลขการ์ด

## TL;DR
- Lobster.cash (โดย Crossmint) integrate **Mastercard Agent Pay** + **Verifiable Intent** — agent รูด Mastercard เดิมได้โดยไม่ expose card details
- Rollout แรกให้ OpenClaw ที่มี agent deploy **มากกว่า 1 ล้านตัว** บน 20+ messaging platforms
- Verifiable Intent พัฒนากับ Google, align กับ AP2 (Agent Payments Protocol) + UCP (Universal Commerce Protocol)

## เกิดอะไรขึ้น
16 เม.ย. 2026 Lobster.cash (บริษัทในเครือ Crossmint) ประกาศ integrate **Mastercard Agent Pay** เปิดให้ AI agent ทำธุรกรรมแทนเจ้าของบัตรได้ โดยใช้บัตร Mastercard ที่ลูกค้าถืออยู่แล้ว — agent ไม่เห็นเลขบัตรจริง

Framework ที่ใช้คือ **Verifiable Intent** — trust layer ที่ Mastercard co-develop กับ Google align กับ **AP2 (Agent Payments Protocol)** และ **UCP (Universal Commerce Protocol)** ทำให้การยืนยันเจตนาของเจ้าของบัตรก่อน agent รูด เป็นมาตรฐาน ไม่ใช่ของเฉพาะ vendor

Rollout initial ไปที่ **OpenClaw** ซึ่งเคลมว่ามี agent deploy มากกว่า **1 ล้านตัว** ใน 20+ messaging platforms — ผ่าน Lobster.cash ผู้ใช้ตั้ง policy ได้ว่า agent จ่ายได้ที่ไหน กี่ครั้ง ใช้ payment method อะไรบ้าง

Crossmint จะเปิด early access ก่อน broad availability

## ทำไมสำคัญ
นี่คือ **"AP2/UCP จาก paper สู่ production"** ครั้งแรกที่มีผู้เล่นระดับ Mastercard เอา protocol ไปใช้จริงกับ real card ที่มีคนถือเป็นล้าน

Pattern สำคัญ: agent ไม่ได้ **ถือเงิน** — agent มี "intent" ที่ verify ได้ ผู้ใช้มี **programmable guardrails** (limit, merchant allow-list, frequency) เปลี่ยน trust model จาก "เชื่อ agent" เป็น "เชื่อ framework"

Signal ต่อตลาด: agent commerce กำลัง **lock in protocol layer** ใครไม่ align กับ AP2/UCP ตอนนี้ ปีหน้าจะ integrate เข้ายาก

## มุม OpenBridge
- ถ้า OpenBridge มี product ที่ agent ต้อง "จ่ายเงิน / ซื้อของ / ทำ commerce action" **ควรคุม Verifiable Intent + AP2 spec ให้เข้าใจวันนี้** — ไม่ใช่รอเป็น standard
- Policy layer ของ Lobster.cash (where/how-often/which-method) เป็น UX pattern ที่ลูกค้า enterprise ไทยจะถามหา — copy ได้
- OpenClaw มี agent 1M+ บน messaging → messaging-first agent distribution เป็น channel ที่ OpenBridge ประเมินได้ (LINE OA ไทยตรง ๆ เลย)

## Sources
- [Lobster.cash partners with Mastercard to enable secure AI agent payments for all existing card holders — PR Newswire](https://www.prnewswire.com/news-releases/lobstercash-partners-with-mastercard-to-enable-secure-ai-agent-payments-for-all-existing-card-holders-302743740.html)
- [Crossmint's Lobster.cash Integrates Mastercard Agent Pay for Agentic Commerce — Bitcoin News](https://news.bitcoin.com/crossmints-lobster-cash-integrates-mastercard-agent-pay-for-agentic-commerce/)

---

## Audio script
เรื่องสุดท้ายของวันนี้เป็นเรื่องใหญ่ในฝั่ง agent commerce Mastercard จับมือกับ Lobster.cash ของ Crossmint เปิดให้ AI agent รูดบัตร Mastercard เดิมของลูกค้าได้ โดยไม่เห็นเลขบัตรจริง เขาใช้ framework ที่ชื่อ Verifiable Intent พัฒนาร่วมกับ Google align กับ protocol AP2 กับ UCP ที่เป็นมาตรฐาน agent payment rollout แรกไปที่ OpenClaw ที่มี agent ใช้งานมากกว่า 1 ล้านตัว กระจายอยู่บน 20 กว่า messaging platform ที่น่าสนใจคือผู้ใช้ตั้ง policy ได้เองว่า agent จ่ายได้ที่ไหน กี่ครั้ง ใช้ method ไหนบ้าง เปลี่ยน trust model จากเชื่อ agent เป็นเชื่อ framework สำหรับ OpenBridge ผมว่าต้องจับตาสองเรื่อง หนึ่งถ้า product เราต้องมี agent ทำ commerce action ต้องเข้าใจ AP2 กับ Verifiable Intent ตั้งแต่วันนี้ ไม่งั้นปีหน้า integrate เข้ายาก สอง messaging-first agent distribution แบบ OpenClaw นี่คือรูปแบบที่ LINE OA ไทยเอาไปทำตรง ๆ ได้เลย
