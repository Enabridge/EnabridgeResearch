---
date: 2026-05-28
slug: willison-claude-code-codex-pmf
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  Two towering vending machines stand side by side in a futuristic lobby.
  The left machine bears the Anthropic logo and dispenses glowing blue
  "Claude Code" cartridges; the right machine shows the OpenAI logo and
  dispenses green "Codex" cartridges. A long queue of developer silhouettes
  stretches behind both machines, wallets open. Above the machines, a neon
  sign reads "PMF" in bold capital letters. Dollar signs and usage graph
  arrows pointing up float in the background. Style: retro-futuristic
  editorial illustration, bold flat colors, high contrast, clean
  composition legible at 200px thumbnail. No real human faces.
image: images/26-05-28-0609-03-willison-claude-code-codex-pmf.png
---

# Simon Willison ชี้ — Claude Code และ Codex "found product-market fit" แล้ว ตลาด AI coding agent เข้าสู่ยุค revenue จริง

## TL;DR
- Simon Willison (27 พ.ค.) วิเคราะห์ว่า Anthropic (Claude Code/Cowork) และ OpenAI (Codex) ต่าง "found product-market fit" กับ coding agent products — ไม่ใช่แค่ hype อีกต่อไป
- ทั้งสองบริษัทปรับ pricing ให้ enterprise จ่ายตาม API token usage จริง — signal ว่า unit economics ใช้งานได้ในระดับ production
- ประกอบกับ Cognition $492M ARR ข่าว coding agent ไม่ใช่ "ของเล่น dev" อีกต่อไป แต่เป็น billion-dollar category

## เกิดอะไรขึ้น

Simon Willison — นักพัฒนาที่เป็นหนึ่งใน trusted voices ของวงการ AI tooling — เผยแพร่บทวิเคราะห์เมื่อ 27 พ.ค. 2026 ในหัวข้อ "I think Anthropic and OpenAI have found product-market fit" เป็น analysis ที่ขึ้น Hacker News front page และถูก discuss อย่างกว้างขวาง ประเด็นหลักคือ: ทั้ง Claude Code/Cowork ของ Anthropic และ Codex ของ OpenAI ไม่ใช่ "experimental feature" อีกต่อไป แต่เป็น products ที่มี product-market fit จริง — developer ใช้ทุกวัน ยอมจ่ายเงิน และ retention สูง

สิ่งที่ Willison ชี้ให้เห็นคือ pricing convergence — ทั้ง Anthropic และ OpenAI ปรับราคา enterprise tier ให้ตรงกับ API token pricing จริง OpenAI อัปเดต Codex pricing เมื่อ 2 เมษายน 2026 เปลี่ยนจาก per-message เป็น per-token แล้วขยายไป ChatGPT Enterprise ทุก plan เมื่อ 23 เมษายน Anthropic ก็ทำเช่นเดียวกันกับ Claude Code — enterprise cost = API price ไม่มี markup ซ่อน

ในบริบทเดียวกัน frontier race ระหว่าง Google, OpenAI และ Anthropic ถูกอธิบายว่า "effectively neck-and-neck" — ทุกบริษัทอยู่ในระดับ capability ใกล้เคียงกัน ดังนั้นสิ่งที่แยกชนะ-แพ้ ไม่ใช่ model intelligence แต่คือ product experience, pricing และ ecosystem ซึ่ง coding agent เป็นสนามแข่งที่เห็นชัดที่สุด

Willison ยังสังเกตว่า OpenAI แอบ adopt "skills" mechanism ของ Anthropic ใน ChatGPT และ Codex โดยไม่ประกาศ — แสดงว่า product innovations ของฝ่ายหนึ่งถูก replicate อย่างรวดเร็วโดยอีกฝ่าย ทำให้ competition ยิ่ง fierce และ moat ที่แท้จริงอยู่ที่ ecosystem + distribution ไม่ใช่ feature

## ทำไมสำคัญ

เมื่อ trusted observer อย่าง Willison ประกาศว่า AI coding agents "found PMF" ในสัปดาห์เดียวกับที่ Cognition ปิดรอบ $1B ที่ $26B valuation ด้วย $492M ARR — นี่ไม่ใช่ coincidence แต่เป็น category validation ที่ชัดเจน AI coding agent กลายเป็น market ที่มีขนาดใหญ่พอที่ venture firms ลงทุน billion-dollar rounds และ enterprise จ่ายเงินจริงทุกเดือน

pattern ที่น่าจับตาคือ "pricing = API usage" — ทั้ง Anthropic และ OpenAI ยอมให้ enterprise จ่ายตาม token consumption จริง ไม่มี bundling หรือ seat-based pricing แบบ SaaS ดั้งเดิม นี่คือ pricing model ใหม่ที่เหมาะกับ agentic products — agent ทำงานมากก็จ่ายมาก ทำงานน้อยก็จ่ายน้อย ถ้า model นี้ work สำหรับ coding agent ก็น่าจะ work สำหรับ agent ใน vertical อื่น ๆ ด้วย

## มุม OpenBridge

สำหรับ OpenBridge มีสอง takeaway ที่ชัด: **หนึ่ง** — pricing model "pay per token consumed" ที่ coding agents ใช้เป็น blueprint สำหรับ OpenBridge ในการ price agent-based integration services ไม่ต้อง invent pricing model ใหม่ ตลาดกำลังบอกว่า usage-based pricing เป็นที่ยอมรับ

**สอง** — ถ้า moat ของ AI agent ไม่ใช่ model intelligence แต่คือ ecosystem + distribution ตามที่ Willison วิเคราะห์ OpenBridge ในฐานะ integration layer ที่เชื่อม agents กับ enterprise tools ก็เป็น ecosystem play โดยธรรมชาติ — ยิ่ง connector เยอะ ยิ่ง sticky ยิ่ง moat กว้าง

## Sources
- [I think Anthropic and OpenAI have found product-market fit — Simon Willison](https://simonwillison.net/2026/May/27/product-market-fit/)
- [HN Discussion: I think Anthropic and OpenAI have found product-market fit](https://news.ycombinator.com/item?id=48296794)
- [OpenAI and Anthropic dig in against each other on AI jobs apocalypse — Axios](https://www.axios.com/2026/05/27/ai-hype-doom-openai-anthropic)
- [How Google plans to win the AI war — Axios](https://www.axios.com/2026/05/21/google-ai-anthropic-openai-war)

---

## Audio script
เรื่องสุดท้ายวันนี้ครับ Simon Willison ซึ่งเป็น trusted voice ของวงการ AI tooling เขียนบทวิเคราะห์เมื่อวานนี้ว่า Claude Code ของ Anthropic กับ Codex ของ OpenAI ต่าง found product-market fit แล้ว ไม่ใช่แค่ hype อีกต่อไป developer ใช้ทุกวันยอมจ่ายเงินจริง สิ่งที่น่าสนใจคือทั้งสองบริษัทปรับ pricing ให้ enterprise จ่ายตาม API token จริง ไม่มี bundling ซ่อน ประกอบกับข่าว Cognition 492 ล้านดอลลาร์ ARR ทำให้ AI coding agent กลายเป็น billion-dollar category ที่พิสูจน์แล้ว Willison ยังชี้ว่า moat ไม่ใช่ model intelligence แต่คือ ecosystem กับ distribution สำหรับ OpenBridge takeaway คือ usage-based pricing เป็น blueprint ที่ใช้ได้ และ integration layer ที่เชื่อม agent กับ enterprise tools เป็น ecosystem play ที่สร้าง moat ได้จริงครับ
