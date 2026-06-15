---
date: 2026-06-15
slug: arcade-60m-series-a-agent-action-layer
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a glowing security gate at the heart of a vast enterprise
  data hall, with dozens of small robotic agent silhouettes lining up to pass through
  scanners that stamp each one with a glowing ID badge. Above the gate, large floating
  numerals "$60M Series A" and "Arcade" are rendered in bold sans-serif type, with a
  smaller tag "secure action layer" pinned below. A faint audit-log scroll unfurls in
  the background, showing rows of agent IDs and actions. Render style: cinematic
  editorial illustration, isometric perspective, deep navy and cobalt background with
  warm amber accent light from the gate, dramatic depth, high-contrast typography
  legible at 200px thumbnail. No real human faces — only robotic silhouettes.
image: images/26-06-16-0603-01-arcade-60m-series-a-agent-action-layer.png
---

# Arcade $60M Series A — "ตัวแทนคนไหนทำอะไร ในนามใคร" กลายเป็นคำถามแพงที่สุดใน production AI

## TL;DR
- 15 มิ.ย. Arcade.dev ปิด Series A $60M นำโดย SYN Ventures + Morgan Stanley + Wipro strategic — รวม total funding $72M (จากรอบ seed $12M ปี 2025)
- Position ตัวเองเป็น "secure action layer" ระหว่าง agent กับ enterprise system: authorization + audit trail + reliability ที่พิสูจน์ได้ว่า "agent ตัวไหน ทำ action อะไร ในนาม user คนไหน ต่อ system ใด"
- Founding team มาจาก Okta, Redis, MongoDB, Snowflake, Airbyte — เลือก enterprise infra layer ที่ Fortune 500 ใช้เป็น default

## เกิดอะไรขึ้น

วันที่ 15 มิ.ย. 2026 Arcade.dev ประกาศปิด Series A $60M นำโดย SYN Ventures ซึ่งเป็น cyber-focused VC ตัวจริง — ที่น่าสนใจคือ strategic investor 2 รายเป็น **Morgan Stanley** (เพื่อใช้ในงาน financial services) และ **Wipro** (Indian IT services giant) ไม่ใช่ pure tech VC แบบที่ AI startup ส่วนใหญ่ยกขึ้นเวที รวมรอบ seed $12M ปี 2025 ทำให้ Arcade ระดมรวม $72M ใน 14 เดือน — pace ของ company ที่ลูกค้า enterprise สั่งซื้อก่อน product GA

Arcade ขายตัวเองด้วยประโยคเดียว: "secure action layer behind every production AI agent" ปัญหาที่แก้คือ — เมื่อ enterprise ปล่อย agent ที่ทำ action จริงในระบบ (call API, query DB, ส่งอีเมล, อนุมัติ transaction) ทีม security ต้องตอบให้ได้ว่า **agent ตัวไหน ทำ action อะไร ในนาม user คนไหน ต่อ system ใด** — คำถามง่ายๆ ที่ระบบ identity ปัจจุบันตอบไม่ได้ เพราะ OAuth/SSO ถูกออกแบบสำหรับ human user หนึ่งคนต่อ session ไม่ใช่ agent หนึ่งตัวที่ act บน behalf ของ user หลายคน

Product มี 3 layer ทับกัน: **Authorization** — agent ได้ access ตามสิทธิ user เจ้าของ scope แค่ action ที่กำลังทำ ไม่ใช่ access ทั้งบัญชี **Reliability** — tools ถูกออกแบบให้ agent เรียกซ้ำได้ มี retry/idempotency อย่างที่ deterministic system ไม่ต้องการ และ **Governance** — audit trail ครบทุก action ที่ agent ทำ พร้อม signed attestation ว่าใครเป็นเจ้าของ Founder team มาจาก Okta, Redis, MongoDB, Snowflake, Airbyte — โดย CEO Alex Salazar เคยเป็น VP ที่ Okta — ทีมที่รู้จัก enterprise identity ระดับลึก

Arcade ไม่ใช่บริษัทเดียวในสมรภูมินี้ — Anthropic เพิ่งเปิด MCP tunnels (พ.ค.) ทำ self-hosted sandboxes, Vercel ซื้อ Context AI เพื่อขุดในด้าน supply chain ของ MCP, NSA ออก guidance MCP security ในเดือน พ.ค. เช่นกัน Arcade เลือก position ที่ specific มาก — ไม่แตะ runtime หรือ orchestration แต่จับ **identity + action layer** ที่ enterprise ลูกค้าต้องการเพื่อ deploy agent ใน production ระดับ compliance

## ทำไมสำคัญ

ปี 2025 คำถามคือ "agent ทำอะไรได้บ้าง" — ปี 2026 คำถามเปลี่ยนเป็น "agent ทำอะไรลงไปแล้วและพิสูจน์ได้ไหม" Arcade เป็น signal ชัดว่า enterprise market กำลังย้ายจาก experimentation เข้า production และเมื่อย้ายแล้ว ทุก action ที่ agent ทำต้อง audit ได้ — เหมือนที่ทุก API call ใน fintech ต้อง audit ได้ ทุก database write ใน healthcare ต้อง audit ได้ ตรงนี้คือ infrastructure layer ที่ regulator จะ insist และ enterprise security team จะ require เป็น precondition ก่อน sign deployment

Investor mix ก็เป็น signal — **Morgan Stanley** ใส่เงินไม่ใช่เพื่อ financial return แต่เพื่อ ensure ว่ามี solution ที่ใช้ได้ในงาน wealth management/compliance ของตัวเอง **Wipro** ใส่เพื่อให้ system integrator มี secure middleware ที่ขายให้ enterprise client ได้ pattern นี้คือเดียวกับที่ Splunk เคยมีในช่วง 2010-2015 — strategic investor ที่ใช้ product เป็นลูกค้าก่อนจะเป็น investor นั่นแปลว่า traction มีจริงในกลุ่ม F500 ไม่ใช่แค่ developer adoption

ที่ต้องจับตาคือ — Arcade เลือกที่จะเป็น **horizontal layer** (ไม่ได้สร้าง agent เอง) นั่นทำให้ neutral ต่อ Claude/GPT/Gemini/Grok และ neutral ต่อ Salesforce/ServiceNow/SAP/Workday นี่เป็น defensible position ที่ Anthropic หรือ OpenAI build เองยาก เพราะการเป็น neutral ขัดกับ business model ของ foundation model lab — model lab จะ default ให้ใช้ model + runtime ของตัวเอง ไม่ใช่ทำ neutral identity layer ที่รองรับคู่แข่ง

## มุม OpenBridge

นี่คือเรื่องที่ใกล้ OpenBridge ที่สุดในรอบเดือน — Arcade ขาย **identity + audit layer** ระหว่าง agent กับ enterprise system ซึ่งเป็น adjacent กับ OpenBridge ที่ขาย **integration + tool fabric** ระหว่าง agent กับ enterprise system ทั้งสองเลเยอร์ต้องอยู่ด้วยกันใน stack ของลูกค้า — คำถามคือ OpenBridge จะ **integrate** กับ Arcade (ปล่อย Arcade handle auth ระหว่าง agent กับ tool ที่เรา proxy) หรือ **compete** กับ Arcade (build identity proxy ของเราเอง) คำตอบขึ้นกับว่าลูกค้า enterprise มอง integration platform ว่าควรมี identity built-in หรือควร plug entity แยก

Lesson 2: **strategic investor มากกว่า traction VC** — Arcade ดึง Morgan Stanley + Wipro เพราะทั้งสองรายเป็น "ลูกค้าตัวจริง + go-to-market partner" ในรอบเดียว OpenBridge ควรคิด pattern เดียวกัน — รอบ funding ครั้งหน้าควรพยายามให้มี SI หรือ vertical anchor (เช่น a regional bank, a logistics carrier) เป็น strategic ใส่เงินด้วย ไม่ใช่ pure tech VC อย่างเดียว เพราะ enterprise B2B sale ที่ scale ต้องการ go-to-market partner ที่ "เซ็นเช็คเป็น investor" มา channel deal ให้ได้จริง

## Sources
- [Arcade Raises $60M to Become the Secure Action Layer Behind Every Production AI Agent — BusinessWire](https://www.businesswire.com/news/home/20260615229631/en/Arcade-Raises-$60M-to-Become-the-Secure-Action-Layer-Behind-Every-Production-AI-Agent)
- [Arcade Raises $60 Million to Control AI Agents — PYMNTS](https://www.pymnts.com/news/investment-tracker/2026/arcade-raises-60-million-to-control-ai-agents/)
- [Arcade.dev Raises $60 Million to Secure AI Agents — WSJ via Moomoo](https://www.moomoo.com/hant/news/post/71548562/arcadedev-raises-60-million-to-secure-ai-agents-wsj)
- [Arcade: The MCP Runtime for Production AI Agents — arcade.dev](https://www.arcade.dev/)
- [Arcade.dev Scores $12M to Solve the Biggest Security Problem with AI Agents — BusinessWire (2025)](https://www.businesswire.com/news/home/20250318815130/en/Arcade.dev-Scores-$12M-to-Solve-the-Biggest-Security-Problem-with-AI-Agents)

---

## Audio script
สวัสดีครับ Yoh เช้านี้มีดีลที่ใกล้ OpenBridge ที่สุดในรอบเดือน Arcade.dev ปิด Series A หกสิบล้านดอลลาร์เมื่อวานนี้ นำโดย SYN Ventures พร้อม strategic investor สองรายที่น่าสนใจมาก Morgan Stanley และ Wipro รวมกับ seed สิบสองล้านจากปีที่แล้ว ทำให้ Arcade ระดมเงินรวมเจ็ดสิบสองล้านในสิบสี่เดือน Arcade ขายตัวเองด้วยประโยคเดียวว่า secure action layer ของ production AI agent ปัญหาที่แก้คือเมื่อ enterprise ปล่อย agent ที่ทำ action จริง security team ต้องตอบให้ได้ว่า agent ตัวไหน ทำ action อะไร ในนาม user คนไหน ต่อ system ใด คำถามง่ายๆ ที่ระบบ identity ปัจจุบันตอบไม่ได้ เพราะ OAuth ออกแบบสำหรับ human user ไม่ใช่ agent ที่ act บน behalf ของ user หลายคน Product มีสาม layer ทับกัน authorization ที่ให้ agent ได้สิทธิตาม user เจ้าของ scope แค่ action ที่ทำ reliability ที่ให้ tool เรียกซ้ำได้แบบ idempotent และ governance ที่มี audit trail ทุก action Founder team มาจาก Okta Redis MongoDB Snowflake Airbyte ของจริงระดับ Fortune 500 default มุม OpenBridge มีสองเรื่อง หนึ่ง Arcade เป็น adjacent กับเรามาก ขาย identity ระหว่าง agent กับ enterprise system เราขาย integration ต้องตัดสินใจว่าจะ integrate หรือ compete สอง ดู pattern strategic investor ที่ Arcade ใช้ Morgan Stanley กับ Wipro ใส่เงินเพราะเป็นลูกค้าตัวจริงและ go-to-market partner รอบ funding ครั้งหน้าของเราควรมี SI หรือ vertical anchor ใส่ด้วย ไม่ใช่ pure tech VC อย่างเดียวครับ
