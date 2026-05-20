---
date: 2026-05-21
slug: karpathy-anthropic-claude-improves-claude-pretraining-recursive
topic: agentic-ai
reading_time_min: 3
sources: 5
image_prompt: |
  An editorial isometric scene in deep teal, warm cream, and electric
  orange — tech-magazine cover style. Center: a stylized brain-shaped data
  center labeled "CLAUDE PRETRAINING" with a glowing recursive loop arrow
  curving out, looping through a smaller second brain labeled "CLAUDE
  AGENT" and arcing back into the main brain — illustrating "Claude trains
  Claude". To the left, a silhouette figure in a hoodie carries a tagged
  briefcase reading "KARPATHY · EX-OPENAI · EX-TESLA" walking from a faded
  OpenAI logo toward Anthropic's coral logo. Above the scene a billboard
  reads "AI THAT TRAINS AI" with three stacked numbers: "FOUNDING OPENAI
  MEMBER", "PRE-TRAINING TEAM", "RECURSIVE COMPUTE EDGE". Dramatic rim
  lighting, ultra-sharp text rendering, high contrast for 200px thumbnail
  readability, 1:1 aspect, no real human faces — silhouette only.
image:
---

# Andrej Karpathy ออก OpenAI/Tesla ไป Anthropic pretraining — สร้างทีมเอา Claude ไป train Claude ตัวเอง = recursive compute edge

## TL;DR
- 19 พ.ค. — Andrej Karpathy (founding member OpenAI, อดีต Tesla AI senior director, founder Eureka Labs) ประกาศย้ายเข้า **Anthropic pretraining team** ใต้ team lead **Nick Joseph** สัปดาห์นี้
- Mission ของทีมใหม่: **ใช้ Claude agent เร่ง pretraining research** ของ Claude ตัวเอง — recursive loop ที่ Anthropic เดิมพันว่าจะรักษา competitive edge ได้แม้ compute budget เล็กกว่า OpenAI / Google
- ดีลนี้ + Stainless acquisition (วันเดียวกัน) = **ภาพ Anthropic ที่ pivot จาก challenger ไปเป็น "ดูดทรัพยากร frontier ของคู่แข่ง"** — talent, infrastructure, ecosystem พร้อมกัน

## เกิดอะไรขึ้น

19 พฤษภาคม 2026 — Andrej Karpathy ประกาศบน X ว่ากำลังย้ายเข้า **Anthropic pretraining team** สัปดาห์นี้ ใต้ team lead Nick Joseph. ใครคือ Karpathy — เป็น **founding member ของ OpenAI** ก่อนย้ายไป Tesla เป็น Senior Director of AI ที่นำทีม computer vision หลัง Autopilot. หลังออก Tesla 2022 เปิด Eureka Labs (AI-native education startup) + content educator ที่ทรงอิทธิพลใน AI Twitter ที่นิยาม **"Software 1.0/2.0/3.0"** framework ที่ now mainstream

Mission ของทีมใหม่ที่ Karpathy จะ build — **ใช้ Claude agent เร่ง pretraining research** ของ Claude เอง. Anthropic อธิบายเป็น "recursive loop" — Claude agent ช่วย research, code, analyze data ที่ใช้ pre-train next-gen Claude. ที่ Anthropic เดิมพันคือ **algorithmic efficiency จะชนะ pure compute scale** — สำคัญมากเพราะ OpenAI + Google มี compute budget มากกว่า Anthropic 5-10x (จาก partnership Microsoft + Google Cloud ของตัวเอง)

Karpathy พูดที่ Sequoia AI Ascent ก่อนหน้านี้ว่า "LLMs กลายเป็น new programmable layer ของ digital work" และ context window จะเป็น "lever หลักของ programmer". มุมมองนี้ตรงกับ Anthropic pitch ที่ Boris Cherny (Claude Code creator) ก็พูดที่ AI Ascent ว่า "coding is solved" — Claude Code แตะ **$2.5B run-rate revenue** ก่อน Feb funding round. Karpathy + Anthropic = match ทาง vision ที่ชัดมาก: agent ทำ knowledge work, ไม่ใช่แค่ chatbot

วันเดียวกัน 19 พ.ค. — Anthropic ประกาศ acquisition ของ Stainless ($300M+) ที่ตัด SDK tooling supply ของ OpenAI/Google/Cloudflare. 2 ข่าวคู่กันบอกภาพชัด — **Anthropic อยู่ใน talent + infrastructure offensive mode**. ก่อนหน้านี้ Anthropic recruit Mike Krieger (อดีต Instagram co-founder) เป็น CPO, Jared Kaplan เป็น Chief Science Officer, Tom Brown (lead author GPT-3) เป็น co-founder. Karpathy เพิ่มชื่อใหญ่ที่สุดของวงการเข้า roster

## ทำไมสำคัญ

ดีลนี้สำคัญด้วย 3 reason. หนึ่ง — **Anthropic ยอมเดิมพันบน strategy "recursive compute"** = ใช้ Claude train Claude. ถ้าได้ผล Anthropic จะ generate next-gen model ที่ใช้ compute น้อยกว่า OpenAI / Google ได้ — เพราะ Claude ทำ research/curation/synthesis เร็วกว่า human researcher 10-50x. Strategy นี้ตรงกับ "Software 3.0" vision ของ Karpathy ที่ argued ว่า prompt + agent คือ new programming surface — Anthropic เอา vision นี้มาใช้กับ R&D process เอง

สอง — **talent gravity ของ Anthropic ตอนนี้ดูดคนจากทุกที่**. Karpathy คือ co-founder #2 ของ OpenAI (ตามหลัง Greg Brockman) ที่ออกไปทำ Eureka Labs แล้วกลับมา join AI lab — เลือก Anthropic แทน OpenAI ทั้งที่เป็น alumni เป็น signal สำคัญ. ก่อนหน้านี้ Jan Leike (former OpenAI superalignment co-lead) ก็มา Anthropic เมื่อ 2024. ระยะ 12 เดือน — รอดูใครจะตามมาอีก. ที่จะตามมาแน่ ๆ = talent ของ Tesla AI / xAI / Meta FAIR ที่ shipping pressure สูง

สาม — **recursive AI = thesis ที่ Anthropic ใช้ขายให้ Bloomberg / Wall Street / sovereign investor**. Anthropic round valuation ล่าสุด ~$170B (Mar 2026) ขึ้นได้เพราะ argument ว่า AI ที่ accelerate AI research จะ scale laws ใหม่. ดีล Karpathy validate thesis นี้ใน public — ถ้า key paper ออกในปีหน้าที่แสดง "Claude-assisted pretraining → 2-3x training efficiency", round หน้า Anthropic อาจถึง **$300-400B valuation**. Move นี้คือ R&D bet ที่ public signaling ออกมาเข้มข้น

## มุม OpenBridge

ไม่ direct เกี่ยว — Karpathy ทำ pretraining research, OpenBridge ทำ integration layer. แต่ adjacent insight ที่สำคัญ: **"recursive AI" คือ pattern ที่ OpenBridge ก็ apply ได้**. แทนที่จะให้ engineer manual build connector ใหม่สำหรับแต่ละ API — OpenBridge สามารถใช้ Claude/GPT/Gemini agent อ่าน OpenAPI spec ของลูกค้า + generate MCP server + connector pattern แบบ recursive (similar กับ Stainless ที่ Anthropic เพิ่งซื้อ). Pattern นี้ลดเวลา onboarding ลูกค้าใหม่จาก 4-6 สัปดาห์ เหลือ 2-3 วัน

อีก angle — **Karpathy's "Software 3.0" framing เป็น vocabulary ที่ OpenBridge ควรใช้ขาย enterprise**. ลูกค้า Thai bank / insurance / telco ตอนนี้ confused กับ "agentic AI" vs "automation" vs "RPA". Karpathy framing ที่ว่า "agent = new programming layer, prompt = code, MCP server = library" คือ mental model ที่ฟังเข้าใจง่าย + ถูกอ้างใน boardroom level. OpenBridge ต้อง position ตัวเองเป็น **"Software 3.0 distribution layer สำหรับ Thai enterprise"** — language ที่ executive ใหม่จะ adopt อย่างรวดเร็ว

มอง strategic — Anthropic ที่ assemble talent + infrastructure + ecosystem ครบทุกชั้นภายในเดือนเดียว = vendor ที่ OpenBridge ควร bet หนัก. ภายใน 6-12 เดือน Anthropic จะมี: pretraining edge จาก Karpathy team, SDK pipeline จาก Stainless, enterprise reach จาก PwC, Wall Street footprint, MCP infra ครบ. OpenBridge ที่ pitch ตัวเองเป็น "Claude-first integration partner ใน SEA" จะได้ co-marketing + enterprise lead generation ที่ payback สูงกว่า bet OpenAI / Google

## Sources
- [OpenAI co-founder Andrej Karpathy joins Anthropic (Axios)](https://www.axios.com/2026/05/19/anthropic-openai-karpathy-andrej-claude)
- [Anthropic hires OpenAI co-founder Andrej Karpathy, former Tesla AI leader (CNBC)](https://www.cnbc.com/2026/05/19/anthropic-hires-openai-cofounder-andrej-karpathy-former-tesla-ai-lead.html)
- [OpenAI co-founder Andrej Karpathy joins Anthropic's pre-training team (TechCrunch)](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/)
- [Anthropic hires OpenAI co-founder Andrej Karpathy to lead Claude pre-training research (The New Stack)](https://thenewstack.io/andrej-karpathy-anthropic-pretraining/)
- [Why Anthropic hired OpenAI co-founder and Software 3.0 proponent Karpathy and acquired the dev tools company Stainless (R&D World)](https://www.rdworldonline.com/why-anthropic-hired-openai-co-founder-and-software-3-0-proponent-karpathy-and-acquired-the-dev-tools-company-stainless/)

---

## Audio script
สวัสดีครับโย้ ข่าวที่สี่ของวานนี้ Andrej Karpathy founding member ของ OpenAI อดีต Tesla senior director AI founder Eureka Labs ประกาศย้ายเข้า Anthropic pretraining team สัปดาห์นี้ ใต้ team lead Nick Joseph mission ของทีมใหม่ที่ Karpathy build คือใช้ Claude agent เร่ง pretraining research ของ Claude เอง recursive loop ที่ Anthropic เดิมพันว่าจะรักษา competitive edge ได้แม้ compute budget เล็กกว่า OpenAI กับ Google 5-10 เท่า

Karpathy เป็นคนนิยาม Software 1.0 2.0 3.0 framework ที่ตอนนี้ mainstream เคยพูดที่ Sequoia AI Ascent ว่า LLMs กลายเป็น new programmable layer ของ digital work ตรงกับ Anthropic pitch ที่ Boris Cherny พูดที่งานเดียวกันว่า coding is solved Claude Code แตะ 2.5 พันล้านดอลลาร์ run-rate revenue ก่อน funding กุมภาพันธ์ วันเดียวกัน 19 พ.ค. Anthropic ประกาศ Stainless acquisition 300 ล้านดอลลาร์ 2 ข่าวคู่กันบอกภาพ Anthropic อยู่ใน talent infrastructure offensive mode

ทำไมสำคัญ Anthropic ยอมเดิมพันบน recursive compute strategy ถ้าได้ผล Anthropic generate next-gen model ที่ใช้ compute น้อยกว่า OpenAI Google ได้ Karpathy เป็น co-founder OpenAI ที่กลับมา join AI lab เลือก Anthropic แทน OpenAI เป็น signal สำคัญ talent gravity ของ Anthropic ตอนนี้ดูดคนจากทุกที่ Jan Leike Mike Krieger Jared Kaplan Tom Brown Karpathy เพิ่มชื่อใหญ่ที่สุดเข้า roster

มุม OpenBridge ไม่ direct เกี่ยว แต่ adjacent insight สำคัญ recursive AI คือ pattern ที่ OpenBridge ก็ apply ได้ ใช้ Claude GPT Gemini agent อ่าน OpenAPI spec ของลูกค้า generate MCP server connector pattern แบบ recursive ลดเวลา onboarding จาก 4-6 สัปดาห์เหลือ 2-3 วัน อีก angle Software 3.0 framing เป็น vocabulary ที่ OpenBridge ควรใช้ขาย enterprise ลูกค้า Thai bank insurance telco confused กับ agentic AI vs automation vs RPA Karpathy framing ที่ agent คือ new programming layer prompt คือ code MCP server คือ library คือ mental model ที่ฟังเข้าใจง่ายและถูกอ้างใน boardroom OpenBridge ต้อง position เป็น Software 3.0 distribution layer สำหรับ Thai enterprise ครับ
