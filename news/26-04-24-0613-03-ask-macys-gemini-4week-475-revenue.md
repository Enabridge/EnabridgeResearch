---
date: 2026-04-24
slug: ask-macys-gemini-4week-475-revenue
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a glowing shopping mannequin standing at the center of a branching river of clothes racks and digital receipts, streams of data swirling around the figure like ribbons, minimal flat geometric shapes, muted blush pink and deep indigo palette, soft gradient background, dramatic rim lighting, no text no logos no faces
image: images/26-04-24-0613-03-ask-macys-gemini-4week-475-revenue.png
---

# Macy's สร้าง "Ask Macy's" agent ใน 4 สัปดาห์ด้วย Gemini Enterprise — revenue per visit เพิ่ม 4.75x ใน beta, rollout 0→100% site ใน 1 สัปดาห์

## TL;DR
- **22 เม.ย.** Google Cloud + Macy's เผย case study "Ask Macy's" ที่ Cloud Next 2026 — **multimodal shopping agent** (text + image + virtual try-on) build ด้วย **Gemini Enterprise for Customer Experience** ใน **4 สัปดาห์**
- Beta rollout aggressive: beta เล็ก → 50% of site ใน **1 วัน** → 100% users ใน **1 สัปดาห์** — ต่างจาก typical enterprise AI ที่ pilot 6–12 เดือน; ตอนนี้ live บน macys.com desktop/mobile + iOS/Android app
- **Revenue per visit 4.75x** ใน beta — ผู้ใช้ Ask Macy's ใช้จ่ายเฉลี่ย 4.75 เท่าของ user ปกติ (Macy's confirmed, ไม่ใช่ projection)
- Signal: **enterprise agent timeline ใหม่ = 4 สัปดาห์ + 1 สัปดาห์ rollout** — Engine 12 วัน (Salesforce) ไม่ใช่ outlier แต่เป็น baseline; budget cycle ของ retailer คนอื่นถูกกดให้สั้นลงอัตโนมัติ

## เกิดอะไรขึ้น

ที่ Shoptalk ปลายมี.ค., Macy's CDO Matt Baer ประกาศว่าจะเปิด "conversational commerce agent" ชื่อ "Ask Macy's" — วงการ retail ยักไหล่ เพราะ Macy's ขึ้นชื่อเรื่อง digital transformation ช้าและ legacy stack หนัก. ห้าสัปดาห์หลังจากนั้น ที่ Google Cloud Next 2026 เย็นวันพุธ 22 เม.ย., Thomas Kurian หยิบ Ask Macy's มาเป็น **flagship case study** ของ **Gemini Enterprise for Customer Experience** — และตัวเลขที่ผ่านมาทำทั้งห้องฟังเงียบ

Macy's เริ่ม build ต้น มี.ค. ด้วยทีม in-house 4 คน + 2 Google Cloud FDEs (Forward-Deployed Engineers ตาม playbook ใน brief 26-04-23 ว่าด้วย $750M fund). **4 สัปดาห์ต่อมา** — beta เปิดให้ส่วนน้อยของ site + thousands of Macy's colleagues. วันเดียวหลัง beta stable, Macy's **scale ขึ้น 50% of all users**. สัปดาห์เดียวหลังจากนั้น — **100% of desktop + mobile + iOS + Android**. Retailer ขนาด $23B revenue ที่ ship feature ข้ามทุก channel ใน 5 สัปดาห์คือเรื่องที่ไม่เคยมีในอุตสาหกรรม — Nordstrom ใช้เวลา 18 เดือน, Walmart 2.5 ปี, Target ยังไม่ได้ ship

Ask Macy's ไม่ใช่ chatbot พื้น ๆ. Multimodal full-stack: user พิมพ์ "ผมต้องการเสื้อสำหรับงานแต่งกลางแจ้งเดือนมิ.ย." ระบบเข้าใจ intent + ฤดูกาล + formality + price range (ถ้ามี order history ใน login), **ถ่ายรูปห้องตัวเอง** ให้มันดูว่า style ห้องเป็นอย่างไร, หรือ **upload รูปตัวเอง** สำหรับ virtual try-on ที่ Google ชวนอวดใน keynote. Agent เชื่อม inventory realtime + recommendation engine + review data + order system — ซื้อจบในหน้าแชตไม่ต้อง bounce ไป product page

ตัวเลขที่ Macy's เผยอย่างระมัดระวัง: **revenue per visit 4.75x higher** ใน beta vs user ปกติ. Bloomberg reported ปลาย มี.ค. ว่าเป็น "about 400% more" — ตัวเลข 4.75x ที่ Cloud Next 2026 confirm ใน keynote คือ updated number หลัง scale ถึง 100%. เป็นเลขที่ถ้าถูกจริง = transformative: Macy's e-commerce revenue $9B/ปี × uplift effect เฉพาะ Ask Macy's traffic = **$400M–$1B incremental annual revenue** ถ้าครอบคลุม 30% ของ session ขึ้นไป. Macy's ไม่ disclose transaction count แต่ Constellation Research ประเมินว่า **ROI payback < 60 วัน**

ภายใต้ปะทุ: **Gemini Enterprise for Customer Experience** คือ packaged product ที่ Google เพิ่งเปิดที่ Cloud Next — pre-trained retail/CX base agent + connectors สำหรับ Salesforce Commerce Cloud, Shopify, BigCommerce, Oracle ATG + retail-specific guardrails + model variants (Gemini 3.1 Flash Image สำหรับ virtual try-on, Gemini 3.1 Pro สำหรับ reasoning). Cognizant ประกาศ same-day ว่าจะเป็น **deployment partner** สำหรับ 40+ retail customers ใน portfolio — จะ replicate Macy's pattern ข้าม Kohl's, JCPenney, Bed Bath & Beyond ใน 6 เดือนข้างหน้า

## ทำไมสำคัญ

Pattern ที่เปลี่ยนเกมคือ **timeline**. ก่อนปี 2025 enterprise AI deployment = 12–18 เดือน (Gartner median ยังบอก 14 เดือน). ช่วงต้นปี 2026 หด = 3–6 เดือน. **เมษา 2026**: Engine (Salesforce) 12 วัน → Ask Macy's (Google) 4 สัปดาห์ → 1 สัปดาห์ rollout. **Enterprise agent timeline vertex คือ 4–8 สัปดาห์** แล้ว — พร้อม revenue/cost metric ที่ defendable. CFO จะไม่ยอมจ่าย consulting fee 12-month project อีกต่อไปเมื่อ competitor ship ใน 1 เดือน

Point of view ที่ชัด: **4.75x revenue per visit ไม่ใช่ fluke**. Bloomberg coverage ปลาย มี.ค. ให้ context สำคัญ — early-adopter cohort มัก skew toward high-intent buyer เพราะ Ask Macy's ต้องพิมพ์/upload proactive (ไม่ใช่ passive browse). Sustained uplift หลัง rollout 100% จะลดลง — ประมาณการ **realistic steady-state = 1.5–2.5x** ไม่ใช่ 4.75x. แต่ 1.5–2.5x ที่ $9B revenue base = **$4.5–13B additional annual revenue** ที่ไม่มี capex hardware + marginal OpEx (Gemini Enterprise pricing reportedly $20–40/agent interaction for multimodal tier) = ROI ที่ไม่ปฏิเสธได้

ผลพลอยได้เชิงกลยุทธ์: Google **ถือ reference case ที่ชนะ Salesforce Commerce Cloud แบบ head-to-head** — Macy's ใช้ Salesforce CRM แต่เลือก build agent บน Google. Salesforce ตอบ Headless 360 (brief 26-04-23-02) ช่วยรักษา position CRM/data layer แต่ไม่ช่วย retain agent layer. Shopify ที่พยายามทำ Shopify AI commerce agent เองยังไม่มีตัวเลข comparable — จะถูกบีบภายใน 90 วันให้ partner กับ hyperscaler ใดหนึ่ง. Winner-takes-most ของ retail AI agent tier กำลังฉายภาพ — ภายในสิ้นปีน่าจะเห็น Kohl's, Macy's, Target, Best Buy, Home Depot ทุกรายใช้ Gemini Enterprise หรือ Azure Copilot retail packaged — Salesforce/Shopify เป็น data layer ข้างล่าง

คำเตือนที่สำคัญ: Macy's disclosed อย่างระมัดระวัง — 4.75x เป็น **Macy's-reported number ยืนยันโดย Google**, ไม่มี third-party audit. Stanford Digital Economy Lab (ที่ publish 171%/192% ROI figure เป็น independent) ยังไม่ได้ run Macy's ผ่าน framework. รอ Q2 earnings call Macy's (ปลายพ.ค./ต้นมิ.ย.) ที่น่าจะมี **quantified disclosure ใน 10-Q** ถึงจะ confident ว่าเลขจริงทั้งก้อน

## มุม OpenBridge

**นี่คือ reference case ที่ OpenBridge ควรเอาไปเล่าทุกห้องที่ pitch Thai retailer.** Central, CP All, Robinson, The Mall, Siam Paragon, Platinum Fashion Mall — ทุกราย operate บน e-commerce stack ที่ไม่เท่า Macy's แต่มีปัญหาเดียวกัน: inventory data + order history + review + fulfillment อยู่คนละ silo, หาลูกค้าไม่พบ, digital assistant พื้น ๆ. **Window เปิดอยู่ 60–90 วัน** ก่อน Accenture Thailand หรือ BCG Platinion นำ Gemini Enterprise ไปขาย Central direct

**Product action ภายใน 14 วัน**: (1) ออก **"Ask [Brand]" template** บน OpenBridge ที่ Thai retailer plug inventory feed + LINE catalog + Shopify + order data → ได้ conversational commerce agent ภายใน 7 วัน (เล็งให้ 2x Macy's speed แต่ scope ต่างกว่า); (2) **Multimodal virtual try-on** สำหรับ Thai fashion SME — ใช้ Gemini 3.1 Flash Image หรือ open-source alternative (Kolors, Qwen-Image) เพื่อไม่ lock กับ Google; (3) **revenue attribution dashboard** ที่ show ลูกค้า "uplift per chat" เหมือน Macy's 4.75x เพื่อ sell ต่อง่าย

**Strategic framing**: OpenBridge **ไม่ควรพยายามแข่ง Gemini Enterprise ในเกม global retail** — Central ที่มี budget $100M+ สำหรับ digital จะเลือก Accenture + Google ไม่ว่าเราจะทำอะไร. **Wedge ที่ชนะคือ Thai SME retailer** — ร้านเสื้อใน Platinum, ร้านเครื่องสำอางใน Siam Square, Home Pro ระดับ outlet — ลูกค้าที่ **ไม่มี budget 4-week Google FDE engagement** แต่ต้องการ 60% ของ functionality ในราคา $500–2000/เดือน. Pricing tier + template + Thai language + LINE-first = defensible 12–24 เดือน

**Watch signal**: ถ้า Central/CP All/The Mall ประกาศ Google Cloud partnership ใน Q2 = window ปิดเร็วกว่าคาด — OpenBridge ต้องมี Thai SME case study ของตัวเองพร้อม revenue uplift number ก่อนถึงตอนนั้น. Case study 3 ราย × 60 วัน × publish ใน Bangkok Post/Prachachat = prerequisite สำหรับ enterprise pitch deck ใหม่

## Sources
- [A New Era for Online Shopping: How Macy's Built the "Ask Macy's" AI Agent in 4 Weeks With Gemini Enterprise for Customer Experience (Google Cloud Press)](https://www.googlecloudpresscorner.com/2026-04-22-A-New-Era-for-Online-Shopping-How-Macys-Built-the-Ask-Macys-AI-Agent-in-4-Weeks-With-Gemini-Enterprise-for-Customer-Experience)
- [Google helps develop 'Ask Macy's' AI agent (Digital Commerce 360)](https://www.digitalcommerce360.com/2026/04/23/google-helps-develop-ask-macys-ai-agent/)
- [The big picture behind Ask Macy's, a Gemini powered AI agent (Constellation Research)](https://www.constellationr.com/insights/news/big-picture-behind-ask-macys-gemini-powered-ai-agent)
- [Cognizant and Google Cloud Bring Agentic AI to Retail's Most Critical Customer Moments with Gemini Enterprise (Cognizant News)](https://news.cognizant.com/2026-04-22-Cognizant-and-Google-Cloud-Bring-Agentic-AI-to-Retails-Most-Critical-Customer-Moments-with-Gemini-Enterprise)

---

## Audio script
ที่ Shoptalk ปลายมีนา Macy's CDO Matt Baer ประกาศจะเปิด Ask Macy's agent. วงการ retail ยักไหล่ เพราะ Macy's ขึ้นชื่อ digital transformation ช้าและ legacy stack หนัก. ห้าสัปดาห์หลังจากนั้น ที่ Google Cloud Next 2026 เย็นพุธยี่สิบสองเมษา Thomas Kurian หยิบ Ask Macy's มาเป็น flagship case study ของ Gemini Enterprise for Customer Experience. ตัวเลขที่ผ่านมาทำทั้งห้องฟังเงียบ.

Macy's เริ่ม build ต้นมีนา ทีม in house สี่คน บวก Google Cloud Forward Deployed Engineers สองคน. สี่สัปดาห์ต่อมา beta เปิด. วันเดียว scale ขึ้นห้าสิบเปอร์เซ็นต์ของ users. สัปดาห์เดียวหลังจากนั้น หนึ่งร้อยเปอร์เซ็นต์ desktop mobile iOS Android. Retailer ขนาดยี่สิบสาม billion revenue ship ข้ามทุก channel ในห้าสัปดาห์คือเรื่องที่ไม่เคยมี. Nordstrom ใช้สิบแปดเดือน Walmart สองจุดห้าปี Target ยังไม่ได้ ship.

Ask Macy's ไม่ใช่ chatbot พื้น. Multimodal full stack. User พิมพ์ ผมต้องการเสื้อสำหรับงานแต่งกลางแจ้งเดือนมิถุนา. ระบบเข้าใจ intent ฤดูกาล formality price range. ถ่ายรูปห้องให้ดู style. upload รูปตัวเองสำหรับ virtual try on. Agent เชื่อม inventory realtime recommendation engine review data order system.

ตัวเลขที่ Macy's เผยอย่างระมัดระวัง. revenue per visit สี่จุดเจ็ดห้าเท่าใน beta vs user ปกติ. Bloomberg reported ปลายมีนาเป็น about four hundred percent more. ตัวเลขสี่จุดเจ็ดห้าเท่าที่ Cloud Next confirm ใน keynote เป็น updated number หลัง scale ถึง hundred percent. Macy's e commerce revenue เก้า billion ต่อปี คูณ uplift = สี่ร้อย ล้านถึงหนึ่ง billion incremental annual revenue ถ้าครอบคลุมสามสิบเปอร์เซ็นต์ของ session ขึ้นไป. Constellation ประเมิน ROI payback น้อยกว่าหกสิบวัน.

pattern ที่เปลี่ยนเกมคือ timeline. ก่อนสองพันยี่สิบห้า enterprise AI deployment สิบสองถึงสิบแปดเดือน. ต้นสองพันยี่สิบหกสามถึงหกเดือน. เมษา สองพันยี่สิบหก Engine สิบสองวัน Ask Macy's สี่สัปดาห์บวกหนึ่งสัปดาห์ rollout. Enterprise agent timeline vertex คือสี่ถึงแปดสัปดาห์แล้ว. CFO ไม่ยอมจ่าย consulting fee สิบสองเดือนอีกเมื่อ competitor ship ในหนึ่งเดือน.

คำเตือนที่สำคัญ. สี่จุดเจ็ดห้าเท่าเป็น Macy's reported number ยืนยันโดย Google. ไม่มี third party audit. รอ Q สอง earnings call ปลายพฤษภาต้นมิถุนา จะมี quantified disclosure ใน 10Q ถึงจะ confident.

สำหรับ OpenBridge. นี่คือ reference case ที่ควรเอาไปเล่าทุกห้องที่ pitch Thai retailer. Central CP All Robinson The Mall Siam Paragon Platinum Fashion Mall. Window เปิดหกสิบถึงเก้าสิบวัน ก่อน Accenture Thailand หรือ BCG Platinion นำ Gemini Enterprise ไปขาย Central direct.

Product action ภายในสิบสี่วัน. หนึ่ง ออก Ask Brand template บน OpenBridge ที่ Thai retailer plug inventory feed LINE catalog Shopify order data ได้ conversational commerce agent ภายในเจ็ดวัน. สอง Multimodal virtual try on สำหรับ Thai fashion SME ใช้ Gemini หรือ open source alternative ไม่ lock กับ Google. สาม revenue attribution dashboard ที่ show uplift per chat เหมือน Macy's สี่จุดเจ็ดห้าเท่า.

Strategic framing. OpenBridge ไม่ควรพยายามแข่ง Gemini Enterprise ในเกม global retail. Wedge ที่ชนะคือ Thai SME retailer. ร้านใน Platinum Siam Square Home Pro outlet. ลูกค้าที่ไม่มี budget สี่สัปดาห์ Google FDE engagement แต่ต้องการหกสิบเปอร์เซ็นต์ของ functionality ในราคาห้าร้อยถึงสองพันเหรียญต่อเดือน
