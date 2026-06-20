---
date: 2026-06-18
slug: baseten-1-5b-13b-inference-routing
topic: openbridge-trend
reading_time_min: 4
sources: 2
image_prompt: |
  Editorial illustration of an enormous translucent funnel-shaped router built from glowing geometric prism segments, dozens of luminous data-streams in different colors pour in from the top representing different AI model providers, the funnel routes them into a single neon green output beam exiting the bottom, a small bold neon tag reading "$13B" floats prominently beside the funnel as the dominant readable element, the funnel sits inside an abstract financial-trading-floor environment with subtle ticker silhouettes in the background, minimal flat geometric shapes with isometric perspective, deep navy and emerald palette with magenta and cyan rim light, dramatic editorial mood, soft gradient background, no real human faces, no other readable text or brand logos.
image: images/26-06-21-0602-04-baseten-1-5b-13b-inference-routing.png
---

# Baseten ระดม $1.5B ที่ $13B valuation — ขึ้น 160% ใน 6 เดือน ตอกย้ำว่า "inference layer" คือสนามรบที่ทุน VC สู้กันแรงที่สุดในตอนนี้

## TL;DR
- **18 มิ.ย.** The Information รายงาน Baseten กำลังระดม **$1.5B ที่ valuation $13B** — co-led โดย **Spark Capital, Sands Capital, Altimeter, Wellington Management**
- **160% jump ใน <6 เดือน**: Series E เม.ย.-พ.ค. $300M ที่ $5B → ตอนนี้ $13B; Series D เมื่อ 9 เดือนก่อน $150M; **round นี้ split-priced** (บางคนได้ที่ $11B)
- Baseten คือ **inference platform ที่ route request ไป model ที่เหมาะที่สุด** เน้น open-source model เพื่อ cost — เป็น OpenRouter pattern แต่ enterprise/dedicated มากกว่า
- Signal: "inference gold rush" ที่ VC วาง infrastructure layer เป็น highest-margin bet — สำคัญกว่า model layer สำหรับ OpenBridge เพราะเป็นที่ที่ integration platform แข่งจริง

## เกิดอะไรขึ้น

วันที่ 18 มิ.ย. The Information รายงานว่า **Baseten** — startup AI infrastructure ใน San Francisco ที่ก่อตั้งปี 2019 — กำลังปิด round ใหม่ที่ระดม **$1.5 พันล้านที่ valuation $13 พันล้าน**. co-leads คือ Spark Capital, Sands Capital, Altimeter Capital และ Wellington Management — combination ของ growth equity + public market crossover fund ที่บอกว่า round นี้ position สำหรับ IPO ภายใน 12-18 เดือน. ที่น่าตกใจกว่าตัวเลขคือ **velocity**: Baseten ปิด Series E ขนาด $300M ที่ valuation $5B แค่ **5 เดือนก่อน** (ม.ค. 2026); Series D ขนาด $150M ปิด 9 เดือนก่อนหน้านั้น. **valuation ขึ้น 160% ใน 6 เดือน** — pace ที่ปกติเห็นเฉพาะใน core lab (OpenAI, Anthropic, xAI) ไม่ใช่ infrastructure layer

โครงสร้างที่ The Information สังเกตน่าสนใจ: **round split-priced** — บาง investor ได้ที่ $11B (ส่วนใหญ่เป็น existing investor + tier-1 ที่ negotiate ได้), บางคนเข้าที่ $13B (new crossover fund ที่ทาง Baseten ต้องการ public-market signal). pattern นี้ปกติเห็นใน down round หรือ structured round — แต่ Baseten ใช้เป็นเครื่องมือ price discovery: ทดสอบว่า public-market mindset จะรับ $13B ไหม โดยให้ existing investor lock margin ของตัวเอง. นี่คือสัญญาณว่า IPO window กำลังเปิดและ Baseten เตรียมเข้าตลาด

product ของ Baseten ตรงจุด: **inference platform** ที่ company มาฝาก model (open-source หรือ custom) แล้ว Baseten run inference + route request ไปที่ instance ที่เร็วและถูกที่สุด. ต่างจาก OpenRouter (route ระหว่าง closed model providers via API) — Baseten เน้น **dedicated deployment + open-source weight** สำหรับ enterprise ที่ต้อง latency ต่ำ + ควบคุม cost + ไม่อยาก share data กับ OpenAI/Anthropic. กลยุทธ์การวาง position บน **"inference gold rush"** ที่ทุน VC กำลังหว่านลงทั้งวงการ inference (Together AI ~$5B, Fireworks AI ~$4B, Groq, Cerebras infrastructure plays)

## ทำไมสำคัญ

Pattern ใหญ่ที่ deal นี้ confirm: **stack ของ AI ตอนนี้แบ่งเป็น 3 layer ที่ทุนแห่ลงเหมือนกัน — model lab (Anthropic $1T sec, OpenAI $500B), routing/inference layer (OpenRouter $1.3B, Baseten $13B, Together $5B), application/agent layer (Cursor $60B, Cognition $26B)**. สอง layer outer (model + app) ทุกคนเห็นชัดเจน. แต่ middle layer — inference routing — เพิ่งจะเป็น mainstream คำพูดเดือนนี้ และ VC เริ่มเข้าใจว่า **margin ของ infrastructure layer สูงกว่า model layer** เพราะไม่ต้องเผา CapEx training (Anthropic เผา $30B compute ใน Q1 alone) + ไม่ต้องเผา GTM ของ app layer

จุดที่ Baseten differentiate จาก OpenRouter ชัด — และเป็นจุดที่น่าจับตา: **OpenRouter เป็น marketplace สำหรับ public API**, Baseten เป็น **deployment platform สำหรับ private + open-source model**. enterprise ที่ใช้ Llama/DeepSeek/Mistral/Qwen หรือ fine-tune ของตัวเอง ตลาดนี้ใหญ่กว่าที่หลายคนคิด — ตามรายงาน a16z "State of Enterprise AI 2026" ~40% ของ enterprise inference workload run บน open-source model แล้ว (จาก 18% ปีก่อน) เพราะ economics ดีขึ้น 3-10x ที่ scale. Baseten อยู่ในกลางของ migration นี้ — ทุก enterprise ที่ตัดสินใจ "ออกจาก OpenAI dependency" ผ่าน Baseten

ผลกระทบกับ OpenAI/Anthropic: **closed model ยังครอง premium tier แต่กำลังเสีย middle tier** ให้ open-source-on-Baseten. คาดว่าจะเห็น Anthropic + OpenAI ตอบโต้ด้วย "managed dedicated inference" tier ของตัวเอง (Anthropic Claude on Bedrock dedicated, OpenAI Azure Dedicated Capacity) ภายใน Q3 — แต่ economics ของ closed model จะแพงกว่า 2-4x ที่ workload เดียวกัน. Baseten ตำแหน่งดี: **ขายให้ enterprise ที่ต้องการ "ความสบายใจ" ของ managed service โดยไม่ต้องจ่าย Claude/GPT margin**

## มุม OpenBridge

**Direct strategic implication:** Baseten = blueprint ว่า "infrastructure middleware ทำได้ $13B valuation". OpenBridge ในฐานะ integration platform อยู่ adjacent layer (orchestration + connector vs inference), แต่ playbook คล้ายกัน: **เป็น neutral middleware ที่ enterprise จ่ายเพื่อหลีกเลี่ยง vendor lock-in**. ที่ Baseten ขาย "วิ่ง model ไหนก็ได้, optimize cost ให้", OpenBridge ขาย "เชื่อม SaaS ไหนก็ได้, orchestrate agent ให้". narrative parity ที่ฟัง CFO จะ resonate

**Action 30-60 วัน:** (1) **Build "inference router" layer ใน OpenBridge** ที่ route LLM call ของลูกค้าไปยัง provider ที่เหมาะ — Claude สำหรับ reasoning หนัก, GPT-5.5 สำหรับ multi-modal, Llama-3.5/DeepSeek-V4 บน Together/Baseten สำหรับ bulk classification + summarization. ลูกค้า Thai SMB ไม่อยากเลือกเอง — OpenBridge เลือกให้แล้ว charge premium 15-20%; (2) **Partner กับ Baseten หรือ Together AI** เพื่อ host fine-tuned Thai model ของลูกค้า (Typhoon-2, OpenThaiGPT, SCB10X model) ที่ลูกค้า train แล้วไม่อยาก operate เอง — OpenBridge เป็น orchestration + integration, Baseten เป็น inference. clean handoff

**Strategic warning:** Baseten + Together + Fireworks กำลัง integrate "agent runtime" + "tool registry" ใน inference platform ของตัวเอง (ดู Together's recent partnership กับ LangChain, Fireworks' new agent SDK). ถ้า inference layer เริ่ม encroach เข้า orchestration territory, OpenBridge ต้อง **differentiate ที่ business logic + Thai SaaS connector + vertical compliance** — ไม่ใช่ generic agent framework. **window 6-9 เดือน** ก่อน inference layer commoditize orchestration

**Vertical signal:** ที่ valuation $13B + IPO trajectory, Baseten กำลังจะกลายเป็น "Snowflake ของ inference" — public company ที่ enterprise CIO ใส่ stack แบบ default. OpenBridge ที่ partner ตั้งแต่ก่อน IPO จะได้ co-sell ที่ enterprise tier — เริ่ม partnership conversation เร็ว ๆ คุ้มกว่ารอ

## Sources
- [AI inference startup Baseten reportedly raising $1.5B months after its last mega-round (TechCrunch)](https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/)
- [Baseten raising $1.5B at $13B valuation co-led by Spark, Sands, Altimeter, Wellington (The Information via TechCrunch)](https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/)

---

## Audio script
วันที่สิบแปดมิถุนา. The Information รายงาน Baseten กำลังปิดรอบใหม่. ระดม หนึ่งพันห้าร้อยล้านเหรียญ ที่ valuation หนึ่งหมื่นสามพันล้าน. co lead Spark Capital Sands Capital Altimeter Wellington Management. growth equity บวก public market crossover fund. position สำหรับ IPO ใน สิบสองถึงสิบแปดเดือน.

velocity น่าตกใจ. Baseten ปิด Series E สามร้อยล้าน ที่ valuation ห้าพันล้านเหรียญ แค่ห้าเดือนก่อน. Series D หนึ่งร้อยห้าสิบล้าน เก้าเดือนก่อนหน้านั้น. valuation ขึ้นหนึ่งร้อยหกสิบเปอร์เซ็นต์ใน หกเดือน. pace ที่ปกติเห็นเฉพาะใน core lab. OpenAI Anthropic xAI. ไม่ใช่ infrastructure layer.

โครงสร้างที่ The Information สังเกต. round split priced. บาง investor ได้ที่ หนึ่งหมื่นหนึ่งพันล้าน. existing investor บวก tier one ที่ negotiate ได้. บางคนเข้าที่ หนึ่งหมื่นสามพันล้าน. new crossover fund ที่ Baseten ต้องการ public market signal. เครื่องมือ price discovery ทดสอบว่า public market จะรับไหม.

product ของ Baseten ตรงจุด. inference platform. company มาฝาก model open source หรือ custom แล้ว Baseten run inference. route request ไปที่ instance ที่เร็วและถูกที่สุด. ต่างจาก OpenRouter ที่ route ระหว่าง closed model providers. Baseten เน้น dedicated deployment open source weight สำหรับ enterprise ที่ต้อง latency ต่ำ ควบคุม cost ไม่อยาก share data กับ OpenAI Anthropic.

pattern ใหญ่. stack AI ตอนนี้แบ่งเป็นสาม layer. model lab Anthropic OpenAI. routing inference Baseten OpenRouter Together Fireworks. application Cursor Cognition. middle layer inference routing เพิ่งเป็น mainstream เดือนนี้. VC เริ่มเข้าใจว่า margin infrastructure สูงกว่า model layer. ไม่ต้องเผา CapEx training. ไม่ต้องเผา GTM ของ app.

Baseten ต่างจาก OpenRouter ที่จุดสำคัญ. OpenRouter marketplace สำหรับ public API. Baseten deployment platform สำหรับ private open source model. enterprise ที่ใช้ Llama DeepSeek Mistral Qwen หรือ fine tune ตัวเอง. รายงาน a16z สี่สิบเปอร์เซ็นต์ของ enterprise inference workload run บน open source แล้ว ขึ้นจาก สิบแปดเปอร์เซ็นต์ปีก่อน. ทุก enterprise ที่ตัดสินใจออกจาก OpenAI dependency ผ่าน Baseten.

สำหรับ OpenBridge. Baseten blueprint ว่า infrastructure middleware ทำได้ valuation หมื่นสามพันล้าน. OpenBridge อยู่ adjacent layer. playbook คล้ายกัน. neutral middleware ที่ enterprise จ่ายเพื่อหลีกเลี่ยง vendor lock in.

action สามสิบถึงหกสิบวัน. หนึ่ง build inference router ใน OpenBridge ที่ route LLM call ของลูกค้าไป provider ที่เหมาะ. Claude สำหรับ reasoning หนัก. GPT 5.5 สำหรับ multi modal. Llama DeepSeek บน Baseten สำหรับ bulk classification. ลูกค้า Thai SMB ไม่อยากเลือกเอง OpenBridge เลือกให้ charge premium สิบห้าถึงยี่สิบเปอร์เซ็นต์. สอง partner กับ Baseten หรือ Together AI เพื่อ host fine tuned Thai model ของลูกค้า. Typhoon OpenThaiGPT SCB10X. OpenBridge orchestration บวก integration. Baseten inference. clean handoff.

warning. Baseten Together Fireworks กำลัง integrate agent runtime ใน inference platform. ถ้า inference layer encroach orchestration territory OpenBridge ต้อง differentiate ที่ business logic บวก Thai SaaS connector บวก vertical compliance. window หกถึงเก้าเดือนก่อน inference layer commoditize orchestration
