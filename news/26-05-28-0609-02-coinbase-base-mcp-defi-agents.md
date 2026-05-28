---
date: 2026-05-28
slug: coinbase-base-mcp-defi-agents
topic: openbridge-trend
reading_time_min: 3
sources: 5
image_prompt: |
  A glowing MCP protocol connector symbol at the center radiates golden
  light outward, bridging two worlds: on the left, a sleek AI chat
  interface with a conversation bubble reading "Swap 1 ETH"; on the right,
  a stylized blockchain ledger with interconnected blocks and token icons
  (ETH diamond, generic DeFi symbols). The Coinbase "C" logo and "Base"
  wordmark float subtly near the bridge. A large padlock icon with an
  OAuth checkmark sits at the base of the bridge. Style: clean fintech
  editorial illustration, dark navy background, electric blue and gold
  palette, isometric perspective, bold shapes legible at 200px thumbnail.
  No real human faces.
image: images/26-05-28-0609-02-coinbase-base-mcp-defi-agents.png
---

# Coinbase เปิด Base MCP — AI agent สั่ง swap, lend, transfer crypto ผ่านแชทได้แล้ว

## TL;DR
- Coinbase เปิดตัว Base MCP (26 พ.ค.) — MCP gateway ให้ AI agents อย่าง Claude และ ChatGPT สั่ง execute ธุรกรรม DeFi onchain ผ่าน natural language
- ใช้ OAuth 2.1 + user-controlled approval window ทุก transaction — server ไม่ถือ private key ไม่สั่งธุรกรรมเอง
- Signal สำคัญ: MCP กำลังกลายเป็น universal protocol ที่ไม่จำกัดแค่ software dev — ตอนนี้ถึง financial infrastructure แล้ว

## เกิดอะไรขึ้น

วันที่ 26 พ.ค. 2026 Base — Ethereum L2 ที่ Coinbase incubate — เปิดตัว Base MCP อย่างเป็นทางการ เป็น MCP gateway ที่ให้ AI agents เช่น Claude และ ChatGPT เชื่อมต่อกับ crypto wallet ของผู้ใช้ แล้วสั่งทำธุรกรรม DeFi ผ่าน natural language ได้เลย — ไม่ว่าจะ swap token, transfer funds, track portfolio หรือ interact กับ DeFi protocols ทั้งหมดผ่านหน้าต่างแชท

สิ่งที่ Coinbase ออกแบบมาอย่างระมัดระวังคือ security model — Base MCP ใช้ OAuth 2.1 ในการ authenticate ระหว่าง AI agent กับ Base Account ของผู้ใช้ server ไม่ถือ private key และไม่สามารถ execute transaction ได้เอง ทุก transaction ที่ AI เสนอจะต้องผ่าน approval window แยกที่แสดง expected asset changes ก่อนผู้ใช้กดยืนยัน — เป็น "human-in-the-loop" ที่ออกแบบมาสำหรับโลก crypto โดยเฉพาะ

launch แรกรองรับ DeFi protocols หลัก ๆ อย่าง Uniswap, Morpho และ Moonwell โดย Coinbase มองว่า AI agents และ conversational interfaces จะกลายเป็น gateway หลักที่คนใช้ crypto และค้นพบ onchain apps ในอนาคต Fortune รายงานว่า Base MCP เป็นส่วนหนึ่งของ push ที่ใหญ่กว่าระหว่าง Coinbase กับ Stripe ที่ต้องการ redefine technical underpinning ของ online commerce

## ทำไมสำคัญ

Base MCP เป็น proof point ว่า MCP กำลังกลายเป็น "USB-C ของ AI agents" — universal connector ที่ไม่จำกัดแค่การเชื่อม AI กับ code editor หรือ database แต่ขยายไปถึง financial infrastructure ที่มี real money flow ถ้า MCP สามารถรองรับ DeFi transactions ที่มี security requirements ระดับ custody ได้ protocol อื่น ๆ ที่ต้องการ agent connectivity ก็ไม่มีข้อแก้ตัวที่จะไม่ support MCP อีกต่อไป

ในมุมกลับ การที่ Coinbase เลือก "user-controlled approvals" แทน "autonomous transactions" สะท้อน maturity ของ ecosystem — หลัง NSA ออก MCP security guidance เมื่อสัปดาห์ก่อน (ดู brief 26-05-27-0604-02) industry กำลังเรียนรู้ว่า "agentic ≠ autonomous" — agent ที่ดีต้องมี guardrails ที่ออกแบบมาสำหรับ domain ของตัวเอง

## มุม OpenBridge

สำหรับ OpenBridge นี่คือ **signal ว่า MCP integration layer มีโอกาสในทุก vertical ไม่ใช่แค่ software dev** — ถ้า crypto/DeFi ที่มี compliance complexity สูงมากยัง adopt MCP ได้ B2B workflow automation, supply chain, fintech ก็ไม่น่าจะมีอุปสรรค

อีกมุมที่ practical — OAuth 2.1 + approval window pattern ที่ Base MCP ใช้เป็น blueprint ที่ดีสำหรับ OpenBridge ในการออกแบบ MCP connector สำหรับ enterprise ที่ต้องการ human-in-the-loop approval ก่อน agent execute action ที่มี business impact สูง เช่น payment approval, contract signing, or inventory adjustment

## Sources
- [Coinbase pushes further into AI payments with new MCP for Base network — Fortune](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/)
- [Base Launches MCP Gateway Letting Claude and ChatGPT Execute Onchain DeFi Actions — Bitcoin.com](https://news.bitcoin.com/base-launches-mcp-gateway-letting-claude-and-chatgpt-execute-onchain-defi-actions/)
- [Coinbase's Base launches AI tool for ChatGPT to manage crypto wallets and DeFi apps — CoinDesk](https://www.coindesk.com/tech/2026/05/26/coinbase-s-base-launches-ai-tool-for-chatgpt-to-manage-crypto-wallets-and-defi-apps/)
- [Coinbase-incubated Base blockchain rolls out MCP gateway to AI interfaces — The Block](https://www.theblock.co/post/402631/coinbase-base-mcp-gateway-ai-interfaces-claude-chatgpt)
- [Base MCP Links AI Agents Like ChatGPT to Blockchain Actions — Blockchain News](https://blockchain.news/news/base-mcp-ai-agents-blockchain-actions)

---

## Audio script
เรื่องที่สองครับ Coinbase เปิดตัว Base MCP เมื่อวานนี้ เป็น MCP gateway ที่ให้ AI agents อย่าง Claude กับ ChatGPT เชื่อมต่อกับ crypto wallet แล้วสั่งทำธุรกรรม DeFi ผ่านแชทได้เลย ไม่ว่าจะ swap token โอนเงิน หรือ interact กับ DeFi protocols ที่น่าสนใจคือ security model ที่ใช้ OAuth 2.1 กับ approval window ทุก transaction ต้องผ่านการยืนยันจากผู้ใช้ก่อน server ไม่ถือ private key เลย ทำไมเรื่องนี้สำคัญ เพราะมันพิสูจน์ว่า MCP กำลังกลายเป็น universal connector จริง ๆ ไม่ใช่แค่เชื่อม AI กับ code editor แต่ขยายไปถึง financial infrastructure ที่มีเงินจริงไหลอยู่ สำหรับ OpenBridge signal คือ MCP integration layer มีโอกาสในทุก vertical ถ้า crypto ที่ compliance เยอะมากยัง adopt ได้ B2B automation ก็ไม่น่ามีอุปสรรคครับ
