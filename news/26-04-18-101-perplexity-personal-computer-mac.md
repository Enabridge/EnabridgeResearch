---
date: 2026-04-18
slug: perplexity-personal-computer-mac
topic: agentic-ai
reading_time_min: 6
sources: 4
depth: deep
---

# Perplexity เปิด "Personal Computer" เปลี่ยน Mac mini ให้กลายเป็น AI agent 24/7 ที่ราคา $200/เดือน

## TL;DR
- Perplexity ปล่อย Personal Computer for Mac วันที่ 16 เม.ย. 2026 — agent ฝังระบบที่คุม Mail, Finder, Slack, Messages, Notes, Calendar + Comet browser ได้ผ่าน native apps
- แนะนำให้รันบน Mac mini เปิดตลอด 24 ชม. เพื่อให้ agent ทำงานต่อแม้ laptop ปิด — pattern "home server สำหรับ agent" เกิดแล้ว
- ใช้ได้เฉพาะ Perplexity Max ($200/เดือน) — **ไม่ให้** plan Pro ($20) ใช้, signal ชัดว่า agent เต็มรูปแบบคือ enterprise-grade SKU ไม่ใช่ consumer

## เกิดอะไรขึ้น

Perplexity ประกาศเปิดตัว **Personal Computer for Mac** วันที่ 16 เมษายน 2026 ทยอยปล่อยให้สมาชิก Max ที่อยู่ใน waitlist ก่อน กดปุ่ม Command ซ้ายขวาพร้อมกันจะเปิด agent แล้วสั่งงานด้วย text หรือเสียงได้

ของที่ต่างจาก Comet browser (ออกก่อนหน้า) คือ Personal Computer ทะลุขึ้นไปถึง **OS layer** — เข้าถึง file system, native Mac apps (Mail, Finder, Slack, Messages, Notes, Calendar) พร้อมเชื่อม Comet browser ในตัว เปิด ≥20 frontier models ใต้ฝากระโปรง แล้ว orchestrate หลาย model ให้ทำงานไปพร้อมกัน

Hardware ขั้นต่ำ: Mac รุ่นไหนก็ได้ที่เป็น macOS 14 Sonoma+ แต่ Perplexity แนะนำ **Mac mini** โดยเฉพาะ เพราะอยากให้ agent "รันตลอด 24 ชม." ทำงานแทนผู้ใช้แม้ laptop ปิดอยู่ นี่เป็นครั้งแรกที่ AI vendor ระดับ top-tier ออกมาบอกตรง ๆ ว่า **"ซื้อ hardware เฉพาะทางเพื่อรัน agent คุ้ม"**

ราคา: ต้องเป็นสมาชิก **Perplexity Max ที่ $200/เดือน** ($2,400/ปี) — plan Pro $20/เดือนใช้ไม่ได้ ราคาห่างกัน 10 เท่าสะท้อน positioning ชัดว่าเป็น productivity tool สำหรับคนทำงาน high-value ไม่ใช่ consumer app

## ทำไมสำคัญ

นี่คือ **"agent OS" moment แรกของฝั่ง consumer/prosumer** ที่มีของจริง ทำ demo ได้ ราคาชัด platform ชัด ไม่ใช่ vaporware แบบ Rabbit R1 หรือ Humane pin ที่ล้มไป Perplexity ใช้ Mac ที่คนซื้ออยู่แล้วเป็น substrate — ไม่ต้องซื้อ hardware ใหม่ ไม่ต้อง learning curve แบบเปลี่ยน platform

Signal สำคัญ 3 อย่าง: (1) **Persistence เป็น feature ใหม่** — agent ที่รัน 24/7 ไม่ใช่ session-based เหมือน ChatGPT ทำให้เกิด use case "agent ดูอีเมลทั้งคืน" "agent ติดตาม deadline ในปฏิทิน" ที่เคยทำไม่ได้ (2) **Desktop = ใหม่อีกครั้ง** — 10 ปีที่ผ่านมาทุกอย่างย้ายขึ้น cloud, แต่ agent ต้องการ local context (files, apps, personal data) ทำให้ desktop กลับมาสำคัญ (3) **Multi-model orchestration ฝัง OS** — Perplexity บอกตรง ๆ ว่าใช้ ≥20 model แปลว่า routing layer ที่เคยอยู่ฝั่ง app กำลังย้ายลงไป OS level

## Competitive landscape

**ใครได้ประโยชน์:**
- **Apple** — เข้าใกล้ปลายทาง "Mac = agent appliance" โดยไม่ต้องสร้างเอง; Mac mini unit economics ($599 hardware + $200/เดือน software ของ Perplexity) คือ recurring ecosystem ที่ Apple ฝันมา 10 ปี
- **Perplexity** — ได้ ARPU ที่ $2,400/ปี/user เทียบกับ ChatGPT Plus $240/ปี คือ 10x; ถ้าเจาะ knowledge worker ได้แค่ 200K คน = $480M ARR ใหม่
- **Frontier model labs** (OpenAI, Anthropic, Google) ผ่าน API — Perplexity จ่ายค่า token ใช้ ≥20 model

**ใครถูก disrupt:**
- **Chrome/Arc/Browser category** — ถ้า agent OS ครอบ desktop ได้ browser จะเหลือแค่ render engine
- **Zapier/Make/n8n** — automation tool ที่ต้อง config workflow ล่วงหน้า; agent ที่เข้าถึง apps จริงจะ config-less
- **ChatGPT desktop app** — OpenAI ต้องขยับเร็ว ไม่งั้นเสีย desktop moment
- **Rabbit/Humane clones** — ตาย hardware ใหม่ไม่ต้องแล้ว ใช้ Mac ที่มีอยู่

**Moat analysis:**
- Moat ของ Perplexity ไม่ใช่โมเดล (เช่า API) ไม่ใช่ data (ยังไม่เยอะ) แต่เป็น **OS integration depth + UX craft** — กว่าคู่แข่งจะลอกการเชื่อม Mail/Finder/Messages/Calendar ให้เสถียรใช้เวลา 6–12 เดือน
- ความเสี่ยง: Apple ออก Apple Intelligence ใส่ agent แบบเดียวกันฟรีเมื่อไร — Perplexity เหลือ moat แค่ multi-model choice + non-Apple ecosystem

## Entrepreneur's take

ถ้าเป็น founder ตอนนี้ signal ที่ต้องอ่าน: **"agent layer ย้ายจาก web เข้ามา OS"** ของที่ตามมาคือ:

1. **Vertical agent OS** — "Perplexity for lawyers / for accountants / for doctors" ที่ทำ integration ลึกกับ domain-specific software (LexisNexis, QuickBooks, EMR) แทน Mail/Finder ทั่วไป Max $200 คือ price anchor ที่ professional service จ่ายได้

2. **Agent OS บน Windows/Linux** — Perplexity ลง Mac ก่อน แต่ enterprise ใช้ Windows เยอะ ช่องว่างอยู่ตรงนี้ (คู่แข่ง Microsoft Copilot แต่ยัง fragmented ข้าม Office vs desktop)

3. **"Mac mini for X" packaged appliance** — ขาย bundle hardware + config + agent ให้ SMB ที่ไม่รู้จะ setup Mac mini + Perplexity Max ยังไง margin ดี ไม่ใช่ race-to-zero

4. **Local memory / context layer** — agent ต้องการ long-term memory ของ user; ตอนนี้ Perplexity เก็บเอง แต่ถ้ามี open-source alternative ที่ user own data ได้เอง (เช่น MCP-based memory store) จะเกิด

**ระวัง:** feature-level startup ที่แข่ง Mail agent, Calendar agent, Slack agent โดด ๆ — platform จะกลืนใน 6 เดือน pick **domain** ที่ Perplexity ไม่แตะ หรือ **layer** ที่ platform-agnostic

## Risks & ของที่ press release ไม่ได้บอก

- **Technical:** รัน ≥20 model พร้อมกันบน Mac mini (RAM 16GB base) จะมี latency กับ cost หนักมาก Perplexity ไม่เปิดตัวเลขว่า token cost ต่อ user เฉลี่ย/เดือน — อาจขาดทุนต่อ user แบบ Cursor ในช่วงแรก
- **Business:** $200/เดือนคือ psychological barrier สูง churn rate จะเป็นตัววัดจริง หลัง 3 เดือนแรก ถ้า retention <70% = model พัง
- **Security/Privacy:** agent เข้าถึง Mail + Messages + Files = ถ้าถูก prompt injection ผ่าน email ที่ไม่รู้จัก → data exfiltration ได้ Perplexity ยังไม่พูดชัดเรื่อง sandbox model
- **Platform dependency:** Apple อาจเปลี่ยน macOS API ทำให้ agent เข้าถึง apps ไม่ได้ — เคยเห็นกับ Hazel, Alfred, Raycast ที่ต้องไล่แก้ทุกรอบ
- **ของที่ไม่พูด:** Perplexity Max subscriber จริงมีกี่คน? บริษัทไม่เคยเปิด — ตัวเลข ARR ที่เคยอ้าง ~$150M มีคำถามเรื่อง churn/reactivation rate

## Historical parallel

**Wave ใกล้ที่สุด: Dropbox/Evernote ~2010** — ตอน cloud storage เริ่ม mass market ใคร integrate OS ลึกสุดชนะ (Dropbox กลืน folder sync) คนที่ทำ feature ทับ (Box, SugarSync, ฯลฯ) ไม่รอด Dropbox ใช้เวลาน้อยกว่า 3 ปีโตจาก 0 ถึง 100M user

**Wave ที่ไกลขึ้น: Siri/Alexa ปี 2014–2018** — voice assistant ล้มเพราะทำอะไรจริงไม่ได้ (task completion <30%) Perplexity มีข้อได้เปรียบเพราะ LLM ทำ task completion ได้ >80% บน knowledge work แต่ lesson เดิมยังอยู่: **distribution ≠ adoption** Amazon ใส่ Alexa ใน 500M device ก็ไม่ทำให้คนใช้; Perplexity ต้องพิสูจน์ว่าคน "ใช้" ไม่ใช่แค่ "ดาวน์โหลด"

**Lesson ที่ apply:** winner ของ agent OS wave ไม่ใช่คน ship เร็วสุด แต่คนที่ทำให้ user สร้าง habit ได้ใน 30 วันแรก — metric ที่ Yoh ควรติดตามคือ DAU/MAU ratio ของ Perplexity Max (ถ้า >50% คือจริง)

## มุม OpenBridge
- **Pattern ที่เอามาใช้เลย:** agent ต้องการ persistent compute + local context — OpenBridge integration platform ควรเพิ่ม "always-on connector" mode ที่ run agent listen event แทน user ต้อง trigger (เหมือน cron → webhook → agent)
- **โอกาส:** ทำ "OpenBridge for Perplexity Personal Computer" = agent ใน Mac mini เรียก integration ของ OpenBridge ไปทำงาน cross-app ผ่าน MCP server ฝั่ง OpenBridge — price anchor ที่ $200/เดือนทำให้คนยอมจ่าย add-on ได้ง่ายขึ้น

## Sources

**Primary:**
- [Perplexity Launches Personal Computer for Mac, Turning a Mac mini Into an Always-On AI Agent — MacRumors](https://www.macrumors.com/2026/04/16/perplexity-personal-computer-for-mac/)
- [Perplexity's Personal Computer AI assistant feature launches on Mac for subscribers — 9to5Mac](https://9to5mac.com/2026/04/16/perplexitys-personal-computer-ai-assistant-feature-launches-on-mac-for-subscribers/)

**Independent verification:**
- [Perplexity launches AI assistant Personal Computer for Mac subscribers — TechBriefly](https://techbriefly.com/2026/04/17/perplexity-launches-ai-assistant-personal-computer-for-mac-subscribers/)

**Analysis/Opinion:**
- [Perplexity Personal Computer Review: Worth $200/Month? — FindSkill](https://findskill.ai/blog/perplexity-personal-computer-guide/)

---

## Audio script
เรื่องที่หนึ่งของวันนี้ Perplexity เปิดตัวของใหม่ชื่อ Personal Computer สำหรับ Mac เมื่อวันพฤหัสที่ผ่านมา ฟังชื่อเหมือนของเล่น แต่จริง ๆ มันคือ agent ที่รันบน Mac ของเราแล้วคุม Mail, Finder, Slack, Messages, Notes, Calendar รวมถึง Comet browser ของ Perplexity เองได้หมด กด Command ซ้ายขวาพร้อมกัน แล้วสั่งเป็นข้อความหรือเสียง

ที่น่าสนใจคือ Perplexity แนะนำตรง ๆ เลยว่าให้รันบน Mac mini แล้วเปิดทิ้งไว้ตลอด 24 ชั่วโมง เพื่อให้ agent ทำงานต่อแม้ laptop ของเราปิดอยู่ นี่คือแนวคิด agent OS ที่เกิดจริงครั้งแรก คือเรามี Mac mini หนึ่งเครื่องเป็น server ส่วนตัวของเราที่คอย monitor inbox, ตามงานในปฏิทิน, reply Slack แทนเราได้ทั้งวัน ไม่ใช่ session แบบ ChatGPT ที่เปิดแล้วปิด

ราคา $200 ต่อเดือน เฉพาะสมาชิก Perplexity Max เท่านั้น plan Pro $20 ใช้ไม่ได้ นี่คือ signal ว่าเขามอง agent เต็มรูปเป็น productivity tool ระดับ enterprise ไม่ใช่ consumer app

มุม entrepreneur มี 3 ช่องว่างที่น่าสนใจ หนึ่งคือ vertical agent OS สำหรับ lawyer, accountant, doctor ที่ integrate ลึกกับ software เฉพาะทาง สองคือ agent OS บน Windows และ Linux ที่ Perplexity ยังไม่แตะ สามคือ layer memory context แบบ local ที่ user ควบคุม data เอง

ความเสี่ยงที่ต้องจับตา คือ churn — $200 ต่อเดือนคือ psychological barrier สูงมาก ถ้า 3 เดือนแรก retention ต่ำกว่า 70% เปอร์เซ็นต์ โมเดลพัง อีกอย่างคือ Apple ถ้าใส่ agent แบบนี้ฟรีใน macOS ปีหน้า Perplexity เหลือ moat แค่ multi-model choice

เทียบ pattern เก่า คือ Dropbox ยุค 2010 ตอน cloud storage เริ่ม mass market ใคร integrate OS ลึกสุดชนะ pattern วันนี้คล้ายกัน แต่ lesson ที่สำคัญจาก Siri กับ Alexa คือ distribution ไม่เท่ากับ adoption ของที่ต้องวัดจริงคือ habit formation ใน 30 วันแรก ไม่ใช่ download count

สำหรับ OpenBridge signal ที่ใช้ได้เลยคือ เรา ควรเพิ่ม always-on connector mode ที่ให้ agent listen event แทนที่ user ต้อง trigger แต่ละครั้ง เหมือน cron ยิง webhook เข้า agent ทำให้ integration platform ของเราเข้ากับ pattern agent 24/7 ที่กำลังมา แค่นี้สำหรับเรื่องนี้
