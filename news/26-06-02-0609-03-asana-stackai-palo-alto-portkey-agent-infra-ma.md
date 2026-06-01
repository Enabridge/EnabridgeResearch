---
date: 2026-06-02
slug: asana-stackai-palo-alto-portkey-agent-infra-ma
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial illustration of two giant corporate building blocks slamming
  together in mid-air, with sparks flying. Left block labeled "ASANA"
  catches a glowing puzzle piece marked "StackAI · $75M". Right block
  labeled "PALO ALTO NETWORKS" catches another puzzle piece marked
  "Portkey · $120-140M". Between them, a translucent layer cake labeled
  "AGENT INFRA STACK" shows four floors: Execution, Gateway, Observability,
  Control. Background: a digital marketplace skyline with stock ticker arrows
  pointing up. Style: clean editorial illustration, bold corporate colors
  (Asana coral pink, Palo Alto orange), cinematic dramatic lighting,
  high contrast, 1:1 aspect, text and dollar figures readable at 200px
  thumbnail. No real human faces.
image: images/26-06-02-0609-03-asana-stackai-palo-alto-portkey-agent-infra-ma.png
---

# 24 ชั่วโมงสอง deal — Asana ซื้อ StackAI ($75M), Palo Alto ซื้อ Portkey ($120-140M): เงิน enterprise agent ไหลเข้า infrastructure ไม่ใช่ product

## TL;DR
- 28 พ.ค. Asana ปิด acquisition StackAI (no-code AI workflow platform) ที่ ~$75M
- 29 พ.ค. Palo Alto Networks ปิด acquisition Portkey (AI gateway) ที่ $120–140M — ห่างกันเพียง 24 ชั่วโมง
- Pattern: enterprise budget สำหรับ AI agent กำลังย้ายจากการซื้อ agent product ไปสู่การซื้อ infrastructure layer (execution, gateway, observability, control)

## เกิดอะไรขึ้น

ช่วง 28–29 พ.ค. มี enterprise M&A สอง deal ปิดในเวลาห่างกันแค่ 24 ชั่วโมง — Asana ประกาศ acquisition StackAI ที่ ~$75M ในวันที่ 28 พ.ค. และ Palo Alto Networks ปิด acquisition Portkey ที่ estimated $120–140M ในวันที่ 29 พ.ค. ทั้งสอง deal ดูเหมือนไม่เกี่ยวกัน — Asana เป็น project management ที่ขยายเข้า AI workflow, Palo Alto เป็น cybersecurity ที่ขยายเข้า AI gateway — แต่ pattern ที่ซ่อนอยู่ตรงกัน

StackAI เป็น no-code AI workflow platform ที่ให้ enterprise user สร้าง agent ที่ทำงาน multi-step ได้โดยไม่ต้อง code — Asana ใช้เพื่อต่อยอด Asana Intelligence (AI feature ที่เปิดตัวเมื่อปลายปี 2025) ให้ user ของ Asana สร้าง agent ที่ทำงานในและนอก Asana ได้เลย deal นี้ใหญ่ใน category project management แต่เล็กในระดับ AI M&A — สะท้อนว่า Asana ไม่ได้ซื้อ technology ที่แตกต่าง แต่ซื้อ team และ go-to-market ของ no-code agent ที่พร้อม integrate

Portkey เป็น AI gateway ที่ทำหน้าที่ proxy + observability + cost control ระหว่าง enterprise application กับ LLM provider — ลูกค้าใช้สำหรับ rate limiting, fallback routing ระหว่าง model, logging ของ prompt และ response Palo Alto ซื้อเพื่อขยาย portfolio security จาก traditional network + endpoint เข้าสู่ AI traffic layer — เป็น strategic move ที่ตอบโจทย์ shadow AI ที่ Microsoft Agent 365 ก็พยายามแก้ จากอีกมุม

ที่น่าสังเกตคือ Cognizant ก็ประกาศในสัปดาห์เดียวกันว่า TriZetto Unify เปลี่ยน architecture ให้ AI agent เป็น "first-tier consumer" ผ่าน headless API model — เปิดตัว Electronic Prior Authorization เป็น first live agent-ready service สำหรับ healthcare ทั้งหมดนี้เกิดขึ้นในสัปดาห์เดียวกัน

## ทำไมสำคัญ

Pattern หลักของ M&A wave นี้คือ **เงิน enterprise agent ไหลเข้า infrastructure ไม่ใช่ end-product** ตรงกันข้ามกับ 12 เดือนก่อนหน้าที่ deal ใหญ่ส่วนใหญ่เป็น vertical agent (Sierra customer service, Cognition coding) ตอนนี้ smart money เริ่มซื้อ layer ที่ "อยู่ระหว่าง enterprise app กับ agent" — execution layer (StackAI), gateway layer (Portkey), observability layer (เริ่มเห็น Datadog, New Relic ตามมา), policy layer (NVIDIA OpenShell, ServiceNow Control Tower)

เหตุผลที่ pattern เปลี่ยน — enterprise CIO เริ่มยอมรับว่า "agent product จะมีหลายตัว ใช้หลายค่าย" ผ่านปีที่ผ่านมาเห็นชัดแล้วว่าไม่มี winner-takes-all ของ agent layer ดังนั้นสิ่งที่ทำเงินมากกว่าคือ infrastructure layer ที่ "agent ตัวไหนก็ต้องผ่าน" Portkey เป็น case ชัด — ถ้า enterprise ใช้ Claude + GPT + Gemini พร้อมกัน 5 ทีม Portkey ก็เป็น single chokepoint ที่ดู cost ดู usage ดู abuse ได้ทั้งหมด revenue multiple ของ layer แบบนี้คือ recurring infrastructure spend ไม่ใช่ usage-based ของ model

อีกประเด็น — pattern นี้คือ **early signal ของ consolidation รอบใหญ่** ก่อนหน้านี้ AI infrastructure ตลาดเปิดมีหลาย startup competing — gateway แค่ตัวเดียวก็มี Portkey, Helicone, LiteLLM, Kong AI Gateway, Cloudflare AI Gateway แข่งกันอยู่ การที่ Palo Alto ตัดสินใจซื้อ Portkey แทนที่จะรอ market shake out หมายความว่า incumbent enterprise vendor เห็นว่าหน้าต่างกำลังจะปิด — และต้องการ inhouse capability ก่อนที่ category ราคาจะแพงเกินซื้อ

## มุม OpenBridge

สำหรับ OpenBridge — pattern นี้คือ **validation ที่ตรงกับ thesis ของเรา** OpenBridge อยู่ใน layer ที่ pattern นี้ predict ว่าจะเป็น winner — integration backbone ที่ neutral, multi-vendor, ทำงานกับทุก agent ค่าย Portkey ที่ valuation $120–140M หลังจาก ARR แค่ไม่กี่ล้าน — ทำให้เรารู้ว่า enterprise วันนี้ยอมจ่ายแพงสำหรับ infrastructure piece ที่ defensible หมายความว่า OpenBridge ที่ ship product ที่ neutral และมี enterprise feature (audit, RBAC, SSO, observability) ครบ จะมี exit option ที่ชัดเจน — buyer ที่เป็นไปได้คือ ServiceNow, Salesforce, Microsoft, Atlassian, หรือ infrastructure player เช่น Datadog, Snowflake, Cloudflare

อีกมุม — Asana + StackAI สะท้อนว่า horizontal SaaS ที่มี user-facing surface ใหญ่ (project management, CRM, support) จะซื้อ no-code agent layer เข้ามา embedded ใน product ตัวเองตลอด 12 เดือนหน้า OpenBridge สามารถ position ตัวเองเป็น "Stripe ของ agent integration" — เป็น infra ที่ SaaS vendor เหล่านี้ฝัง white-label ลงไปใน product ของพวกเขา แทนที่จะต้องไป acquire startup เล็ก ๆ พัฒนาเอง — เป็น distribution model ที่ scale เร็วและ defensible ผ่าน switching cost ของ integration ที่ฝังแน่นใน workflow ของลูกค้า

## Sources
- [Enterprise AI Agent Stack Takes Shape: Asana and Palo Alto Buy Execution and Security Layers — Tech Times](https://www.techtimes.com/articles/317470/20260531/enterprise-ai-agent-stack-takes-shape-asana-palo-alto-buy-execution-security-layers.htm)
- [Daily AI Agent News — May 29, 2026 — AI Agent Store](https://aiagentstore.ai/ai-agent-news/daily/2026-05-30)
- [Microsoft Agent 365 GA Context — Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)
- [Microsoft takes Agent 365 out of preview as shadow AI becomes an enterprise threat — VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)

---

## Audio script
สวัสดีครับ Yoh สัปดาห์ที่แล้วมี enterprise M และ A สอง deal ปิดในเวลาห่างกันแค่ ยี่สิบสี่ ชั่วโมง วันที่ ยี่สิบแปด พฤษภาคม Asana ซื้อ StackAI no code AI workflow platform ที่ประมาณ เจ็ดสิบห้าล้านดอลลาร์ และวันที่ ยี่สิบเก้า Palo Alto Networks ซื้อ Portkey AI gateway ที่ประมาณ หนึ่งร้อยยี่สิบ ถึง หนึ่งร้อยสี่สิบล้านดอลลาร์ สอง deal นี้ดูไม่เกี่ยวกัน แต่ pattern ที่ซ่อนอยู่ชัดมาก คือเงิน enterprise agent กำลังย้ายจากการซื้อ agent product ไปซื้อ infrastructure layer ที่อยู่ระหว่าง enterprise app กับ agent ทั้ง execution layer gateway layer observability และ policy layer เพราะ CIO ยอมรับแล้วว่าจะใช้ agent หลายตัวหลายค่าย ดังนั้นสิ่งที่ทำเงินมากกว่าคือ infrastructure ที่ agent ทุกตัวต้องผ่าน Portkey ที่ valuation ขนาดนี้หลังจาก ARR แค่ไม่กี่ล้าน บอกว่า enterprise ยอมจ่ายแพงสำหรับ infra piece ที่ defensible สำหรับ OpenBridge นี่คือ validation ตรงกับ thesis ของเรา เพราะเราอยู่ใน layer เดียวกัน buyer ที่เป็นไปได้คือ ServiceNow Salesforce Microsoft Atlassian หรือ infrastructure player เช่น Datadog Snowflake Cloudflare และอีกมุมที่สำคัญคือ horizontal SaaS เริ่มซื้อ no code agent layer เข้ามา embed ใน product ตัวเอง OpenBridge สามารถ position เป็น Stripe ของ agent integration ให้ SaaS vendor เหล่านี้ฝัง white label ลงไปแทนที่จะ acquire startup เล็ก ๆ พัฒนาเอง เป็น distribution model ที่ scale เร็วและ defensible ครับ
