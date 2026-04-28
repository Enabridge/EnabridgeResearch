---
date: 2026-04-28
slug: microsoft-openai-cloud-exclusivity-end
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of two intertwined chains slowly breaking apart over a stylized cloud landscape, gold light bleeding through the gap, minimal flat geometric shapes, muted teal and warm amber palette, dramatic side lighting, no text or logos
image: images/26-04-29-0612-01-microsoft-openai-cloud-exclusivity-end.png
---

# Microsoft–OpenAI หย่ากันแบบสุภาพ — exclusivity จบ, revenue share โดน cap, AGI clause หาย

## TL;DR
- 27 เม.ย. 2026 Microsoft กับ OpenAI ประกาศ restructure deal ที่ผูกกันมาตั้งแต่ 2019: cloud exclusivity จบ, OpenAI ขายผ่าน AWS/GCP ได้เลย, revenue share ระหว่างกันถูก cap (ไม่เปิดตัวเลข), license สิ้นสุด 2032 และไม่ exclusive แล้ว
- Microsoft ไม่ต้อง "ตัดสินใจ" อีกต่อไปว่า OpenAI ถึง AGI หรือยัง — clause ที่เคยเป็น tripwire กฎหมาย ถูกถอดออก
- สำหรับ enterprise buyer และ integration platform: ChatGPT/Codex/Sora เปิดทางให้ deploy บน multi-cloud เป็นทางการ — vendor lock-in แบบเก่ากำลังจะตาย

## เกิดอะไรขึ้น

หลังคุยกันมาเป็นปี ในที่สุดวันจันทร์ที่ 27 เม.ย. 2026 Satya Nadella กับ Sam Altman ก็ออก joint blog เปิดยุคใหม่ของ Microsoft–OpenAI partnership อย่างเป็นทางการ — และเนื้อใน restructured deal นี้ใหญ่กว่าที่ pundit ส่วนใหญ่คาด

ข้อแรกที่กระแทกตลาดสุดคือ **cloud exclusivity จบลง** OpenAI สามารถ "serve all of its products" ผ่าน AWS, Google Cloud, หรือ cloud อื่นใดก็ได้ตามที่ลูกค้า enterprise ต้องการ ก่อนหน้านี้ OpenAI ผูกอยู่กับ Azure แบบ exclusive ทำให้บริษัทใหญ่ที่ standardize บน AWS หรือ GCP ต้อง work around เพื่อใช้ ChatGPT Enterprise — จากนี้ไป Microsoft ยังเป็น "primary cloud provider" และ product OpenAI จะ "ship first on Azure" แต่หลังจากนั้นไหลออกได้ทุกที่

ข้อสองคือ **revenue share โดน cap สองทาง**: Microsoft จะหยุดจ่าย revenue share ให้ OpenAI ทันที (เป็นเหตุให้ MSFT ราคาเด้งใน after-hours), ส่วน OpenAI ยังจ่าย Microsoft 20% ของรายได้ต่อจนถึง 2030 แต่ตอนนี้ "capped at an undisclosed total" — แปลว่ามี ceiling แล้ว ไม่ใช่ open-ended อีก โครงสร้างนี้ทำให้ทั้งสองฝั่งมี runway ตัดสินใจอนาคตของตัวเองได้อิสระขึ้น โดยเฉพาะ OpenAI ที่เพิ่งระดมทุน $122B รอบล่าสุด

ข้อสามที่นัก governance ฮือฮาคือ **AGI clause ถูกถอดออก** เดิมในสัญญามีข้อที่ระบุว่าถ้า OpenAI board ประกาศว่าโมเดลของตน "ถึง AGI" Microsoft จะหมดสิทธิ์ใช้ IP นั้น — clause นี้เป็นปริศนากฎหมายมาหลายปี (ใครเป็นคนตัดสินว่า "ถึง AGI"?) วันนี้หายไปจากสัญญา แทนด้วย license ปกติที่ครอบคลุมถึง 2032 และ "ไม่ exclusive แล้ว" Microsoft จะใช้ IP ของ OpenAI ต่อได้แต่ OpenAI ก็ license ให้คนอื่นได้ด้วย

อีกผลพลอยได้ที่สื่อจับตามาก: deal นี้เคลียร์ทาง legal ให้ OpenAI ทำสัญญา compute $50B กับ Amazon ได้ — ก่อนหน้านี้ Microsoft อาจขัด exclusivity ได้ แต่ตอนนี้ปลดล็อกแล้ว

## ทำไมสำคัญ

นี่ไม่ใช่ "การเลิก" — เป็น "การจัดความสัมพันธ์ใหม่ให้ทั้งคู่ scale ต่อได้โดยไม่ฆ่ากัน" Microsoft ได้ Azure เป็น default home ของ OpenAI ต่อ และไม่ต้องแบกค่า revenue share ที่ pressure margin ของ Azure อีก ส่วน OpenAI ปลดโซ่ที่หน่วงการขายมา 6 ปี — คนที่อยากซื้อ ChatGPT Enterprise แต่ติดที่บริษัทตัวเอง standardize บน AWS หรือ GCP จะปิดดีลได้เร็วขึ้นมาก สำหรับ Sam Altman นี่คือชัยชนะ ส่วน Nadella ก็ได้ predictability กลับมา

มอง strategically: ตลาด AI กำลังเข้าสู่เฟสที่ **โมเดลและ cloud ไม่จำเป็นต้องผูกกันอีก** Anthropic ขายผ่าน AWS เป็นหลักแต่ก็ไหลเข้า Google Cloud ($30B+ ARR), Google มี Gemini ที่ federate ผ่าน partner cloud ได้, ตอนนี้ OpenAI ก็เปิด multi-cloud — model layer กับ infrastructure layer แยกขั้นกันชัด เหมือนตอน database ปลดตัวเองจาก OS ในยุค 2010s deal Microsoft-OpenAI ปี 2019 เป็น artifact ของยุคที่ใครได้ AI lab ก่อน คนนั้นชนะ — ปี 2026 เกมเปลี่ยนเป็น distribution wins

อีก signal ที่ไม่ควรพลาดคือ **AGI clause หาย** ไม่ใช่แค่ legal cleanup — มันแปลว่าทั้งสองบริษัทไม่ treat AGI เป็น discrete event ที่จะ "เกิด" ในสัญญาอีกต่อไป practitioner ส่วนใหญ่มอง AGI เป็น continuous capability curve ไม่ใช่ moment of singularity และตอนนี้ contract ใหญ่ที่สุดในโลก AI ก็สะท้อน worldview นี้แล้ว

## มุม OpenBridge

สำหรับ integration platform แบบ OpenBridge นี่คือ structural tailwind สามชั้น: (1) ลูกค้า enterprise ที่ standardize บน AWS หรือ GCP จะเริ่มซื้อ OpenAI แบบ native ทำให้ traffic ผ่าน MCP/agent gateway ของ AWS Bedrock และ Vertex AI โตเร็ว — platform ที่ broker ระหว่างหลาย model provider จะมี surface area ใหญ่ขึ้น (2) vendor lock-in เป็น argument ที่ใช้ขายลูกค้าได้น้อยลงเพราะ buyer รู้แล้วว่า model layer แลกได้ — ต้องขาย integration value, governance, observability แทน (3) deal นี้ normalize multi-cloud AI deployment ในระดับ Fortune 500 — RFP ใหม่จะเริ่มเขียนว่า "must support GPT, Claude, Gemini interchangeably" เป็น default

ข้อเตือน positioning: ห้ามเล่าเรื่อง "เราเชื่อม OpenAI ได้" เป็น core value prop อีก — ทุกคนเชื่อมได้ ใน 2026 differentiation ต้องอยู่ที่ orchestration ระหว่าง model + governance + cost routing — ที่ Cloudflare เรียก AI Gateway, ที่ Databricks เรียก AI Gateway, ที่ Vertex เรียก Model Garden ทุกคนวิ่งเข้า layer เดียวกัน คนที่ไม่ขยับขึ้นไปจะโดน commoditize

## Sources
- [The next phase of the Microsoft-OpenAI partnership](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
- [OpenAI shakes up partnership with Microsoft, capping revenue share payments (CNBC)](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- [Microsoft, OpenAI rework partnership as cloud flexibility grows (CIO Dive)](https://www.ciodive.com/news/microsoft-openai-rework-partnership/818606/)
- [OpenAI ends Microsoft legal peril over its $50B Amazon deal (TechCrunch)](https://techcrunch.com/2026/04/27/openai-ends-microsoft-legal-peril-over-its-50b-amazon-deal/)

---

## Audio script
เมื่อวานนี้ Microsoft กับ OpenAI ออกประกาศ restructure deal กันแบบเงียบ ๆ แต่เนื้อใน หนักมาก คือ cloud exclusivity ที่ผูกกันมาตั้งแต่ปี 2019 จบลงแล้ว OpenAI ขายผ่าน AWS หรือ Google Cloud ได้เลย Microsoft ยังเป็น primary cloud อยู่ก็จริง แต่ลูกค้า enterprise ที่ standardize บน cloud อื่นไม่ต้อง work around อีกต่อไป ที่ฮือฮากว่านั้นคือ AGI clause ที่เคยอยู่ในสัญญา ที่ระบุว่า ถ้า OpenAI ประกาศว่าถึง AGI Microsoft จะหมดสิทธิ์ใช้ IP — clause นี้ถูกถอดออก แทนด้วย license ปกติยาวถึงปี 2032 ที่ไม่ exclusive แล้ว revenue share ก็โดน cap สองทาง Microsoft หยุดจ่าย OpenAI, OpenAI ยังจ่าย Microsoft 20% ถึงปี 2030 แต่มี ceiling แล้ว สำหรับเรา signal สำคัญคือตลาด AI กำลังเข้าเฟสที่ model layer กับ cloud layer แยกขั้นกัน เหมือน database แยกจาก OS ในยุค 2010 ใครขาย integration platform ในปี 2026 ห้ามเล่าเรื่อง "เราเชื่อม OpenAI ได้" เป็น value prop อีก เพราะทุกคนเชื่อมได้แล้ว ต้องขาย orchestration governance routing เป็น layer ที่สูงขึ้นไปแทน
