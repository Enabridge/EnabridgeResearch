---
date: 2026-04-28
slug: anthropic-project-deal-agent-marketplace
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of two abstract glowing orbs trading translucent geometric tokens across an empty marketplace stall, one orb noticeably brighter than the other, minimal flat shapes, muted indigo and warm coral palette, dramatic rim lighting, no text or logos or faces
image: images/26-04-29-0612-03-anthropic-project-deal-agent-marketplace.png
---

# Anthropic Project Deal — Claude agents 69 ตัวปิดดีล 186 รอบใน internal marketplace, ค้น "model gap" ที่คนตัวเล็กไม่รู้ว่าตัวเองเสียเปรียบ

## TL;DR
- Anthropic เปิดผลการทดลอง Project Deal: ให้ Claude agents ของพนักงาน 69 คน ซื้อขายของจริงใน Slack workspace — ปิดได้ 186 ดีล มูลค่ารวม $4,000+ โดย ไม่มีมนุษย์เข้าแทรก
- Opus 4.5 เอาชนะ Haiku 4.5 ชัด: sellers ที่ใช้ Opus ได้เงินเฉลี่ย +$2.68/ชิ้น, buyers ประหยัด +$2.45/ชิ้น, ทำดีลได้มากกว่า 2.07 ครั้ง
- ที่น่ากลัวกว่าคือ ผู้เข้าร่วมที่ใช้ Haiku ไม่รู้ว่าตัวเองเสียเปรียบ — rate fairness เท่ากับฝั่ง Opus — implication ใหญ่สำหรับ market ที่ agent เป็น default counterparty

## เกิดอะไรขึ้น

ธันวาคม 2025 Anthropic เปลี่ยนออฟฟิศ San Francisco ของตัวเองเป็น live classified marketplace แล้วทำสิ่งที่ AI lab อื่นยังไม่กล้า — มอบอำนาจการต่อรองทั้งหมดให้ Claude agent แทนพนักงาน พนักงาน 69 คนแต่ละคนได้งบ $100 ใน gift card, สัมภาษณ์กับ Claude ก่อนเพื่อให้ระบุ buying wishlist, selling preferences, และ personal instruction (เช่น "อย่าซื้อ vintage tech มากกว่า $30") inputs เหล่านี้ถูกแปลเป็น custom system prompt แล้ว agent ก็ถูกปล่อยใน Slack workspace ที่ทำหน้าที่เป็นตลาด

หลังจากนั้น zero human intervention — agent ไม่กลับมาถาม approval ก่อนปิดดีล ไม่ปรึกษาตอน bidding war สิ้นสุดสามวัน Anthropic เก็บข้อมูลได้ 186 ดีลที่ปิด มูลค่ารวม $4,000+ ครอบคลุม 500+ items ที่ list ทั้งของใหม่ ของมือสอง บริการเล็ก ๆ ของพนักงาน — รายละเอียดเรื่อง dynamics ที่เปิดออกมาในรายงานวันที่ 25-27 เมษา 2026 น่าสนใจกว่าตัวเลข

ทีมแบ่ง marketplace เป็น 4 รอบอิสระ: 2 รอบทุกคนใช้ Opus 4.5 เป็น agent ตัวเอง, อีก 2 รอบสุ่มแจก Opus หรือ Haiku 4.5 แบบ blind (ผู้เข้าร่วมไม่รู้ว่าตัวเองได้โมเดลไหน) ผลคือ **Opus ชนะ measurable**: sellers ฝั่ง Opus ได้เงินเฉลี่ย +$2.68/ชิ้น, buyers ฝั่ง Opus ประหยัด +$2.45/ชิ้น, จำนวนดีลที่ปิดสำเร็จมากกว่า ~2.07 ครั้ง/คน — capability gap แปลเป็น economic gap แทบ direct

แต่ที่ Anthropic ขยายเสียงเตือนคือ: post-experiment survey ผู้เข้าร่วม rate "ความเป็นธรรมของดีลที่ตนได้" เท่ากันแทบทุกตัวบ่งชี้ ไม่ว่าจะใช้ Opus หรือ Haiku — Anthropic เขียนใน blog ตรง ๆ ว่า "in real-world agent markets, participants on the losing side might not know they're worse off" ไม่มี perceptual signal ว่าตัวเองเสียเปรียบ ขณะที่ 46% ของผู้เข้าร่วมบอกว่าจะ "ยอมจ่าย" เพื่อใช้บริการแบบนี้ในอนาคต

## ทำไมสำคัญ

นี่เป็นการทดลอง agent-to-agent commerce ครั้งแรกที่มี เงินจริง ไม่ใช่ simulator มี reproducible methodology และ peer-checkable data — และ findings ของมันเขย่า assumption หลายอย่างของ industry ที่กำลังจะเปิดตลาด agent commerce อย่างจริงจังในปลายปี 2026 (Stripe, Visa, Shopify ล้วนทำ pilot อยู่)

อันแรก: **capability arbitrage จะไม่หายไปเอง** หลายคนคาดว่าโมเดลแต่ละค่ายจะ converge ที่ frontier เดียวกัน Project Deal บอกตรงข้าม — ความต่าง Opus กับ Haiku (โมเดลค่ายเดียวกัน รุ่นเดียวกันแค่ขนาดต่าง) แปลเป็นเงินจริงระดับ ~10% ของ transaction value ใน 3 วัน ถ้า scale เป็น marketplace ระดับ B2B หรือ commodity trading กระโดดเป็นเลขที่มีนัยทาง P&L ทันที โลกหลังจากนี้ enterprise ที่ใช้ "agent ราคาถูก" เพื่อประหยัด cost จะแพ้ enterprise ที่ใช้ "agent flagship" ในการ negotiate procurement, vendor contract, หรือ pricing

อันที่สอง: **invisible loss คือ regulatory crisis ที่กำลังจะมาถึง** ถ้าผู้บริโภคไม่ "รู้สึก" ว่าตัวเองเสียเปรียบ — กลไกตลาดอย่าง word-of-mouth, online review, complaint จะไม่ทำงานเลย หน่วยงานคุ้มครองผู้บริโภค, FTC, EU Commission จะต้องเขียนกฎใหม่ที่ basis ไม่ใช่ "user experience" แต่เป็น "agent disclosure + capability parity" — Anthropic ใส่บรรทัดนี้ไว้ใน blog เองว่า "policy frameworks don't exist yet, society needs to move quickly"

อันที่สาม: ผู้บริโภค 46% บอก ยอมจ่าย ใน situation ที่ตัวเองอาจเสียเปรียบโดยไม่รู้ตัว — แปลว่า demand จะวิ่งก่อน regulation ไกลมาก agent commerce กำลังจะกลายเป็นสนามแข่งใหม่ที่ winner-take-most ไม่ใช่เพราะ network effect แต่เพราะ capability gap

## มุม OpenBridge

ตรง relevant สูง: ถ้า OpenBridge จะเข้าโลก agent commerce หรือ agent-mediated B2B workflow ในปีนี้-ปีหน้า (procurement bot, vendor negotiation, lead routing ที่ agent ตัดสินใจเอง) มี implication 3 ข้อ

(1) **Model selection คือ economic decision ไม่ใช่ cost decision** ห้าม default flat-fee ที่ลูกค้าเลือก "model ราคาถูก" ได้เพราะมันถูก — ต้อง surface trade-off ให้ชัดว่า "คุณกำลัง trade $X expected value ต่อ transaction เพื่อประหยัด $Y inference cost" ตัวเลข Project Deal ($2.45-2.68/ชิ้น) เป็น proxy ดี ๆ สำหรับเริ่มต้น

(2) **Audit trail ของ agent decision เป็น differentiation ที่ขายได้** ถ้า user ไม่รู้ว่าตัวเองเสียเปรียบโดยอัตโนมัติ คนที่จะรู้ได้คือ system ที่ log + analyze decision quality ย้อนหลัง — feature นี้ enterprise buyer ขนาดใหญ่จะเริ่มต้องการเป็น compliance baseline ใน 6-12 เดือน

(3) **Multi-agent neutrality** OpenBridge ในฐานะ broker layer มี leverage ที่ vendor-locked agent platform ไม่มี — สามารถบังคับ "capability parity check" ระหว่าง agent ที่เข้ามา negotiate ใน workflow เดียวกันได้ เป็น value prop ที่จะตอบโจทย์กฎ regulatory ที่กำลังจะออก

## Sources
- [Project Deal: our Claude-run marketplace experiment (Anthropic)](https://www.anthropic.com/features/project-deal)
- [Anthropic created a test marketplace for agent-on-agent commerce (TechCrunch)](https://techcrunch.com/2026/04/25/anthropic-created-a-test-marketplace-for-agent-on-agent-commerce/)
- [Anthropic says stronger AI models cut better deals, and the losers don't even notice (The Decoder)](https://the-decoder.com/anthropic-says-stronger-ai-models-cut-better-deals-and-the-losers-dont-even-notice/)
- [Anthropic's AI agent-to-agent marketplace experiment: The legal frameworks don't exist (Legal IT Insider)](https://legaltechnology.com/2026/04/27/anthropics-ai-agent-to-agent-marketplace-experiment-the-legal-frameworks-dont-exist/)

---

## Audio script
Anthropic เพิ่งเปิดผลการทดลองที่ชื่อว่า Project Deal ทำเมื่อ ธันวาปีที่แล้ว ในออฟฟิศ San Francisco ตัวเอง ให้พนักงาน 69 คน ปล่อย Claude agent ของตัวเอง ไปซื้อขายของกันใน Slack ด้วยเงินจริง ๆ ผ่าน gift card สามวัน ปิดไป 186 ดีล มูลค่ารวมสี่พันกว่าดอลลาร์ ที่น่าสนใจกว่าตัวเลขคือ Anthropic แบ่งคนเป็น 4 กลุ่ม สุ่มแจก agent ที่ใช้ Opus 4.5 กับ Haiku 4.5 แบบ blind ผู้เข้าร่วมไม่รู้ว่าตัวเองได้โมเดลไหน ผลคือ Opus ชนะชัด sellers ฝั่ง Opus ได้เงินเฉลี่ยมากกว่า สองดอลลาร์หกสิบแปดเซ็นต์ต่อชิ้น buyers ประหยัดได้สองดอลลาร์สี่สิบห้าเซ็นต์ ปิดดีลได้มากกว่าสองครั้งต่อคน แต่ที่น่ากลัวกว่านั้นคือ คนที่ใช้ Haiku ไม่รู้สึกว่าตัวเองเสียเปรียบ rate ความเป็นธรรมเท่ากันเลย Anthropic เขียนเองว่า ในตลาด agent จริง ๆ คนที่อยู่ฝั่งแพ้อาจไม่รู้ด้วยซ้ำว่าตัวเองแพ้อยู่ อันนี้คือ implication ใหญ่ ไม่ใช่แค่ ethics แต่ economic regulation จะต้องเขียนใหม่ และ enterprise ที่ใช้ agent ราคาถูกประหยัด cost อาจจะกำลังเสีย expected value ระดับสิบเปอร์เซ็นต์ของ transaction โดยไม่รู้ตัว
