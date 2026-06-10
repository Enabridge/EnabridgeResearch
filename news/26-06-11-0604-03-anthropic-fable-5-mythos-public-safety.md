---
date: 2026-06-11
slug: anthropic-fable-5-mythos-public-safety
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of twin glowing orbs side by side on a dark stage —
  the left orb labeled "FABLE 5" wrapped in a translucent amber shield, the
  right orb labeled "MYTHOS 5" naked and surrounded by red caution tape with
  a "Glasswing" lab tag. Large floating typography "$10 / $50" anchors the
  top, with a smaller tag "60% price cut" pinned between them. Render style:
  cinematic editorial illustration, symmetrical staging, warm Anthropic
  orange-amber light on left grading to deep crimson on right, dramatic
  spotlight, high-contrast typography legible at 200px thumbnail. No real
  human faces.
image: images/26-06-11-0604-03-anthropic-fable-5-mythos-public-safety.png
---

# Claude Fable 5 ออกสู่สาธารณะ — Anthropic แยก "public" กับ "restricted" model ตัวเดียวกัน เป็นครั้งแรก ส่ง safety architecture เป็น product feature

## TL;DR
- 9 มิ.ย. Anthropic ปล่อย Claude Fable 5 (public) + Claude Mythos 5 (restricted via Project Glasswing) — เป็น **model ตัวเดียวกัน** แต่ Fable มี safety classifier ที่บล็อก cyber/bio/chem queries
- ราคา $10/$50 ต่อล้าน input/output token — **ลดจาก Mythos Preview $25/$125 = ลด 60%** support output ได้ถึง 128k tokens
- Available บน Microsoft Foundry + GitHub Copilot ในวันเดียวกัน — Anthropic ขายช่องทาง enterprise distribution ผ่าน partner platform ไม่พึ่ง direct API อย่างเดียวแล้ว

## เกิดอะไรขึ้น

วันที่ 9 มิ.ย. 2026 Anthropic ทำสิ่งที่ไม่เคยทำมาก่อนในวงการ frontier model — ปล่อยรุ่นใหม่ **2 ชื่อพร้อมกันที่เป็นโมเดลตัวเดียวกัน** Claude Fable 5 เปิดให้ public ทุกคนใช้, Claude Mythos 5 จำกัดเฉพาะ trusted-access program ที่ชื่อ Project Glasswing น้ำหนัก, capability, ราคา เหมือนกันทุกอย่าง — ต่างที่ Fable 5 มี "safety classifier" ที่ refuse query ใน domain เสี่ยงสูง (cybersecurity, biology, chemistry, distillation) แล้ว fall back ไปหา Opus 4.8 ส่วน Mythos 5 ไม่มี classifier และตอบทั้งหมดได้

นี่คือ architectural choice ที่บอกอะไรเยอะมาก — Anthropic ไม่ได้ "train safety เข้าไปใน weight" อย่างเดียวอีกแล้ว แต่แยก policy layer ออกมาเป็น runtime classifier ที่ swap ได้ — ลูกค้าระดับ government, biosecurity lab, frontier security researcher ที่ผ่าน Project Glasswing จะได้ใช้ raw capability ส่วน public ใช้ version ที่ guard rail ติดมาแล้ว นี่คือ playbook ที่ social network เคยใช้ (Twitter pre-Musk มี internal team trust & safety แยกจาก algorithm team) แต่ frontier model ไม่เคยทำให้ visible ขนาดนี้

**ราคา $10 input / $50 output ต่อล้าน token** — ลดจาก Claude Mythos Preview ที่ $25/$125 ลง 60% ทันที output ได้สูงถึง 128k token (เทียบกับ Opus 4.8 ที่ 64k) จุดนี้สำคัญสำหรับงาน agentic ที่ต้องการ generate report ยาว, code refactor ขนาดใหญ่, หรือ multi-step plan ที่ chain นาน — Fable 5 ทำได้ใน single call โดยไม่ต้องแบ่ง session

Distribution gap — ภายในวันเดียวกัน Microsoft Foundry ประกาศ Claude Fable 5 available บน Azure (เปิดให้ enterprise Microsoft customer ที่ไม่ได้ใช้ Claude direct API อยู่แล้ว) และ GitHub Copilot enable เป็น default option Anthropic ไม่พึ่ง direct channel อย่างเดียวอีกแล้ว — multi-cloud, multi-platform distribution คือ pattern เดียวกับ Microsoft 365 ที่ขายผ่านทั้ง Apple Store + ตัวเอง + reseller

TechCrunch รายงาน context ที่น่าสนใจคือ Anthropic ปล่อย Fable 5 หลังจาก **เพิ่ง warning ว่า AI กำลังอันตรายเกินไป** (มีรายงานก่อนหน้าจาก Anthropic Safety team) — การปล่อยอย่างนี้กับ public พร้อม classifier hard-block คือ "ไม่ใช่ว่าเราหยุดเสี่ยง แต่เราเสนอ commercial model ใหม่ที่ผูกระดับการเข้าถึงเข้ากับการประเมินผู้ใช้"

## ทำไมสำคัญ

Move นี้ทำให้ **safety architecture กลายเป็น "product feature ขาย"** ไม่ใช่แค่ "ภาระต้นทุน" ที่ทุก lab ต้องแบก — เป็นครั้งแรกที่ frontier model lab แยก capability tier ตามระดับ vetting ของผู้ใช้อย่างชัดเจน นั่นคือ price discrimination ที่ตั้งใจ — government หรือ biosecurity research ที่ต้องการ raw capability พร้อมจ่ายแพงกว่า/ผ่าน due diligence หนักกว่า, enterprise/developer ทั่วไปจ่ายราคาเดียวกันแต่ได้ guard rail ฟรี

60% price cut เป็น signal ใหญ่กว่าที่เห็น — frontier model pricing กำลังลงเร็ว serving cost ลง infrastructure scale efficiency เพิ่ม ตอนนี้ Fable 5 ราคาเดียวกับ Opus 4.8 ($5/$25? — ไม่, Fable คือ $10/$50 ซึ่งสูงกว่า Opus 4.8 ที่ $5/$25) — แสดงว่า Anthropic positioning Fable 5 เป็น "premium next-tier" สำหรับงานที่ต้องการ capability สูงสุด ไม่ใช่ replacement Opus 4.8 ที่ยังเป็น default workhorse pattern นี้ลอก iPhone Pro/Pro Max — มี tier ที่จ่ายมากขึ้นเพื่อ capability เพิ่มเติม

Distribution ผ่าน Microsoft Foundry + GitHub Copilot ใน day-1 คือ **Anthropic-Microsoft alliance เริ่มเปิดเผยตัว** — OpenAI ก็ขาย Microsoft Azure ผ่าน partnership เดิม Microsoft ตอนนี้กลายเป็น "Switzerland" ที่ขายทุก model ของทุก lab ต่อให้ลูกค้า ลูกค้า enterprise ที่ใช้ Azure จะ swap จาก GPT-5.5 → Fable 5 → Gemini Ultra ได้ภายใน config — ทำให้ Microsoft เป็น distribution monopoly ของ frontier model ในตลาด enterprise

## มุม OpenBridge

เรื่องนี้ส่งเสริม positioning ของ OpenBridge ที่ควรจะเป็น — **multi-vendor neutral** เพราะถ้า Microsoft Foundry กลายเป็น distribution layer ของทุก model ลูกค้า enterprise ก็คาดหวังว่า OpenBridge ทำเหมือนกัน ขั้นต่ำต้อง support Claude (Fable 5, Opus 4.8), OpenAI (GPT-5.5+), Gemini ภายใน config switch — ไม่ใช่ rebuild integration ทุกครั้งที่ลูกค้า swap model

อีกบทเรียนคือ **safety classifier ที่แยกออกจาก model** เป็น architectural pattern ที่ OpenBridge ทำได้ — เพราะถ้า OpenBridge เป็น integration hub ที่ traffic ของ agent วิ่งผ่าน เราอยู่ใน position ที่ apply classifier ของตัวเองก่อน hand off ไปหา model ได้ — เช่น filter PII, redact credential, block query ที่ violate enterprise policy ลูกค้า enterprise ที่กังวลเรื่อง compliance (โดยเฉพาะใน healthcare, finance, government) จะยินดีจ่ายสำหรับ layer นี้แน่นอน

มุมสุดท้าย — **128k output tokens** จะเปลี่ยน workflow design ของ agentic tool หลายตัว ก่อนหน้านี้ agent ต้อง chain หลาย call เพราะ output limit 4k–8k ทำให้ context fragmentation สูง Fable 5 ทำให้ single-call agent ทำงานยาวได้แทบจะ "ไม่ต้อง chain" สำหรับ task ทั่วไป OpenBridge ที่ออกแบบ workflow runtime ควรเตรียม support output token ขนาดนี้แต่ต้น (รวมถึง logging, audit, cost tracking ที่ทำกับ long output ได้)

## Sources
- [Anthropic releases Claude Fable, a version of Mythos, days after warning AI is becoming too dangerous — TechCrunch](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)
- [Introducing Claude Fable 5 and Claude Mythos 5 — Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)
- [Claude Fable 5 available today in Microsoft Foundry: Powering the next era of autonomous agents — Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/claude-fable-5-available-today-in-microsoft-foundry-powering-the-next-era-of-autonomous-agents/)
- [Claude Fable 5 is generally available for GitHub Copilot — GitHub Changelog](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/)
- [Claude Mythos pricing in 2026: Fable 5 costs, Mythos 5 costs, and what every model actually runs — CloudZero](https://www.cloudzero.com/blog/claude-mythos-pricing/)

---

## Audio script
สวัสดีครับ Yoh ข่าวที่สามวันนี้คือ Anthropic ปล่อย Claude Fable 5 และ Claude Mythos 5 พร้อมกัน 9 มิถุนายน เป็นโมเดลตัวเดียวกัน แต่ Fable 5 เปิดให้ public ใช้ Mythos 5 จำกัดเฉพาะ trusted access ผ่าน Project Glasswing น้ำหนัก capability ราคา เหมือนกัน ต่างที่ Fable 5 มี safety classifier ที่บล็อก query domain เสี่ยงสูงพวก cyber biology chemistry แล้ว fall back ไปหา Opus 4.8 Mythos 5 ไม่มี classifier ตอบหมดทุกอย่าง นี่คือ architectural choice ที่บอกว่า Anthropic แยก policy layer ออกจาก weight ของ model แล้ว ลูกค้า government หรือ biosecurity research ได้ raw capability ผ่าน Project Glasswing public ได้ guard rail ฟรี ราคา 10 input 50 output ต่อล้าน token ลดจาก Mythos Preview เดิม 60% output token ได้สูงถึง 128k tokens ใหญ่กว่า Opus 4.8 สองเท่า Microsoft Foundry กับ GitHub Copilot enable เป็น default ในวันเดียวกัน Anthropic ไม่พึ่ง direct channel อย่างเดียวแล้ว สำหรับ OpenBridge มีสามมุม หนึ่ง multi-vendor neutral สำคัญมาก ลูกค้าคาดหวังว่า OpenBridge swap model ได้ใน config ไม่ต้อง rebuild สอง classifier layer คือ pattern ที่ OpenBridge ทำได้ ใส่ filter PII redact credential block policy ก่อน hand off ไปหา model เป็น layer ที่ลูกค้า compliance heavy จ่ายได้ สาม 128k output token เปลี่ยน workflow design ของ agent ส่วนใหญ่ ไม่ต้อง chain หลาย call แล้ว แต่ logging audit cost tracking ต้องเตรียม support long output ตั้งแต่ต้นครับ
