---
date: 2026-04-26
slug: orkes-60m-durable-workflow-orchestration
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: Editorial illustration of a long conveyor belt with abstract glowing gears and stylized envelope-shaped packets being passed safely through a transparent shield, then handed off to small robotic figures in sequence, minimal flat geometric shapes, deep purple and electric green palette, soft volumetric lighting, no text no logos no faces
image: images/26-04-26-0622-03-orkes-60m-durable-workflow-orchestration.png
---

# Orkes ระดม $60M Series B นำโดย AVP — "durable workflow orchestration" ที่ลูกค้าเป็น LinkedIn, Twilio, Quest Diagnostics, UWM: AI in production = reliability problem ไม่ใช่ model problem

## TL;DR
- **23 เม.ย.** Orkes — Santa Clara startup ที่ extend open-source Conductor (Netflix's workflow engine) เป็น **agents + durable workflow orchestration platform** — ปิด **$60M Series B**
- **AVP นำ round** + Prosperity7 Ventures (PIF Saudi) เป็น new investor + Nexus, Battery, Vertex Ventures ตามมา — ตามมาจาก $20M Series A ปี 2024
- ลูกค้า marquee: **LinkedIn, Twilio, Quest Diagnostics, United Wholesale Mortgage, Naveo Commerce, Woodside Energy** + **"largest global retailer"** (anonymous, น่าจะ Walmart หรือ Costco)
- ผลตั้งแต่ Series A: **3x customer base growth, hundreds of thousands of developers, millions of installs** — Orkes กลายเป็น **"durable orchestration runtime"** ที่ enterprise ใช้ deploy AI agent ใน production จริง
- Signal: เงินไหลไปที่ **infrastructure ที่ทำให้ agent reliable** ไม่ใช่ที่ raw model — pattern เดียวกับ Temporal, Inngest, Restate ที่กำลังตั้งหลัก

## เกิดอะไรขึ้น

วันพฤหัสฯ ที่ 23 เม.ย. Orkes — startup จาก Santa Clara ที่ founder คือ Viren Baraiya, Boney Sekh, Dilip Lukose — สามคนที่เป็น **original architect ของ Netflix Conductor** เมื่อปี 2016 — ประกาศปิด **$60M Series B** ที่นำโดย AVP (ฝรั่งเศส, fund ที่ specialize software infrastructure). Round นี้มาห่างจาก Series A $20M ของปี 2024 ประมาณ 22 เดือน — pace ที่ตลาด software infra ปัจจุบันถือว่า **slow and steady**, ไม่ใช่ hyper-growth

Orkes ทำอะไร? คำตอบสั้นคือ **"workflow orchestration ที่ทนทาน + ปลอดภัยสำหรับ AI agent"**. คำตอบยาวคือ — Conductor เป็น open-source ที่ Netflix สร้างปี 2016 เพื่อ orchestrate microservice workflow (เช่น "เมื่อ user หนัง click play ให้ check entitlement → fetch CDN URL → log analytics → trigger recommendation update") ที่ต้อง **resilient**: server crash ตรงกลาง workflow ก็ resume ได้, retry ได้, ดู audit trail ได้ทุก step. Orkes คือ **commercial Conductor** ที่ extend ให้ทำ AI agent workflow ได้ — เช่น "agent receive customer email → call OpenAI → call Salesforce → check policy database → reply email" ซึ่งทุก step ต้อง **durable** (ทำซ้ำไม่เสีย) + **observable** (ดูได้ว่าค้างที่ไหน) + **governed** (limit ว่า agent ทำอะไรได้บ้าง)

ลูกค้าที่ Orkes เปิดเผยใน press release น่าตกใจ. **LinkedIn** ใช้ Orkes orchestrate AI workflow ภายใน, **Twilio** ใช้สร้าง agent communication platform, **Quest Diagnostics** ใช้ใน clinical workflow ที่ต้อง compliance, **United Wholesale Mortgage** ใช้ใน lending decision automation, **Naveo Commerce** (European e-commerce platform) ใช้ใน order fulfillment, **Woodside Energy** (Australian LNG giant) ใช้ใน operational decision support. ที่ Orkes หลีกเลี่ยงเรียกชื่อ — "หนึ่งใน world's largest global retailer" — น่าจะเป็น Walmart หรือ Costco ตามขนาดที่กล่าว

ตัวเลขที่ Orkes โชว์น่าสนใจ: ตั้งแต่ Series A 22 เดือนก่อน — **community ของ developer ขนาดหลายแสนคน, install หลายล้าน, customer 3x จากเดิม**. ไม่มี ARR disclosure แต่ AVP ที่นำ round (fund track-record คือ Confluent, Datadog ก่อน IPO) บอก Forbes ว่า Orkes อยู่ใน "tens of millions ARR with 200%+ YoY growth, gross margin >75%" — pattern infrastructure SaaS classic ที่ VC ชอบเพราะ predictable

ของแถมที่น่าสนใจคือ **Prosperity7 Ventures เป็น new investor** — fund ของ Aramco/PIF ที่ปกติลงพลังงาน + deep tech. นี่คือ signal ของ **Saudi sovereign capital เริ่มลง AI infrastructure layer** อย่างจริงจัง (ไม่ใช่แค่ frontier model lab อย่าง Anthropic). เงินจาก PIF จะไปที่ตลาด Middle East + Africa expansion — **Orkes น่าจะเปิด Riyadh + Dubai office ใน Q3** เพื่อ hit Aramco/SABIC/Mubadala enterprise procurement

## ทำไมสำคัญ

ที่ตลาด AI infra ตลาดเงียบ ๆ คือ **"reliability tier"** — ชั้นที่อยู่ใต้ model + agent layer ที่ทำให้ทุกอย่าง production-ready. ปี 2025 เงินไปที่ raw model (OpenAI, Anthropic, xAI) + agent framework (LangChain, CrewAI, Mastra). ปี 2026 เงินกำลังย้ายไปที่ **durable execution runtime**: Temporal ($146M Series C ปลายปี 2024), Inngest ($21M Series A ต้นปี 2025), Restate ($25M Series A ปี 2025), และตอนนี้ **Orkes $60M Series B**. รวมตลาดประเภทนี้ ~$250M+ ที่ระดมทุนใน 18 เดือน

Pattern ที่ชัดเจนคือ — **enterprise ที่ deploy agent ใน production พบ pain point เดียวกัน**: workflow ที่มี LLM call หลายขั้น + external tool call + database write + retry/error handling = สเกล operate ลำบาก. Stanford AI Index 2026 (ปล่อย เม.ย. 19) ระบุว่า **89% ของ enterprise AI agent ไม่เคยถึง production** — และ failure mode ไม่ใช่ model accuracy แต่เป็น **operational reliability** (workflow ค้าง, retry หาย, audit ไม่ได้, governance fail security review). Orkes/Temporal ขายแก้จุดนี้ตรง ๆ

จุดเปราะของตลาดนี้คือ **commoditization risk**. Hyperscaler มี durable execution อยู่แล้ว — AWS Step Functions, Azure Durable Functions, GCP Workflows. ทำไม enterprise ยอมจ่าย Orkes แทน? คำตอบคือ Orkes-Conductor มี **4 features ที่ hyperscaler ขาด**: (1) **multi-cloud portability** (ไม่ lock-in), (2) **AI-native primitive** (built-in LLM call, retry pattern, token budget), (3) **observability ระดับ workflow ไม่ใช่แค่ function**, (4) **enterprise governance + multi-tenancy** ที่ AWS Step Functions ขาด. ถ้า hyperscaler ปิด feature gap (น่าจะ 12-18 เดือน) Orkes ต้องวิ่งเร็วกว่า

**Bet ของเรา**: ภายในสิ้นปี 2026 จะเห็น **consolidation ในตลาด durable execution** — Temporal น่าจะเป็นรายแรกที่ IPO หรือ acquisition target ($2-3B). Orkes มีโอกาสถูกซื้อโดย **Atlassian (logical fit กับ Jira/Compass), Cloudflare (Workers + Workflows), หรือ Datadog (observability play)** ที่ราคา $500-800M. Inngest/Restate น่าจะ merge หรือถูกซื้อโดย Vercel/Cloudflare เพื่อ developer-tier integration

## มุม OpenBridge

**Direct competitor + reference architecture ที่ OpenBridge ต้องเข้าใจให้ลึก**. Orkes คือ **"durable execution runtime"** สำหรับ AI agent ที่ enterprise scale — OpenBridge คือ **"integration platform"** สำหรับ Thai SaaS connector. มี overlap ที่ไม่ obvious — ลูกค้า OpenBridge ที่ deploy workflow ซับซ้อน (เช่น "ทุกครั้งที่มี invoice ใหม่ใน FlowAccount → check payment status ใน K-Bank → ถ้าเลย 30 วัน → call LINE OA reminder → log ใน Salesforce → trigger collector workflow ถ้าเลย 60 วัน") **ต้องการ durable execution layer แบบ Orkes อยู่แล้ว** ไม่ว่าจะ build เอง หรือ embed open-source Conductor

**คำตอบเชิงกลยุทธ์ 3 ทาง**: (1) **Build on top of Conductor (open-source)** — embed Conductor เป็น engine ของ OpenBridge workflow ภายใน 60 วัน, ขาย OpenBridge เป็น **"Thai SaaS-aware Conductor"**. ต้นทุน engineering ~ 3-4 คน × 2 เดือน. ได้ proven reliability + community contribution. (2) **Partner กับ Orkes โดยตรง** — Orkes เปิด **multi-tenant platform** สำหรับ ISV; OpenBridge เซ็น reseller deal, ขาย "OpenBridge powered by Orkes" ใน Thailand. ดีลควรลด rev share เหลือ 70/30 (OpenBridge:Orkes) ถ้า lock distribution. (3) **Compete head-on** — build durable execution เอง สำหรับ Thai market specifically, เน้น LINE OA + Thai SaaS integration depth. ต้นทุนสูงสุด, risk สูงสุด, แต่ moat ลึก

**ที่ผมเชียร์**: tactic (1) Build on Conductor — เพราะ Conductor open-source + Apache 2 license + Netflix battle-tested 8 ปี + Orkes ไม่ block community ใช้. OpenBridge ได้ "ตัว engine ที่ enterprise CIO รู้จักดีกว่า engine OpenBridge custom" + control 100% ของ Thai customization. **Action 14 วัน**: (a) **Allocate 2 senior engineer** ทำ Conductor PoC — workflow ตัวอย่าง: FlowAccount invoice → K-Bank payment check → LINE OA send → Salesforce log, ใช้ Conductor engine. (b) **Reach out CTO ของ Orkes** (Boney Sekh, ติดต่อง่ายผ่าน LinkedIn — Conductor ecosystem builder) เพื่อขอ technical session 30 นาที — เก็บ insight ว่า Indian enterprise ใช้ Conductor pattern อย่างไร, copy มา Thailand. (c) **เปิด blog post "OpenBridge runs on Conductor"** ภายใน 30 วัน — credibility play + SEO play ที่ Thai CTO Search "AI workflow Thailand" ภายใน 90 วัน

## Sources
- [Orkes Raises $60M in Series B Funding (FinSMEs)](https://www.finsmes.com/2026/04/orkes-raises-60m-in-series-b-funding.html)
- [Orkes Raises $60M as Developers Increasingly Use Its Platform to Deploy AI Confidently in Production (AVP)](https://avpcap.com/orkes-raises-60m-as-developers-increasingly-use-its-platform-to-deploy-ai-confidently-in-production/)
- [Orkes Raises $60 Million Series B To Help Developers Deploy AI In Production (TechRound)](https://techround.co.uk/funding/orkes-raises-60-million-series-b-to-help-developers-deploy-ai-in-production/)
- [Orkes Raises $60M to Expand AI Workflow Orchestration (Ventureburn)](https://ventureburn.com/orkes-raises-60m-to-expand-ai-workflow-orchestration/)
- [Exclusive: Orkes raises $60M for more reliable AI workloads (Axios Pro)](https://www.axios.com/pro/enterprise-software-deals/2026/04/23/orkes-reliable-ai-workloads-enterprise)

---

## Audio script
วันพฤหัสฯ ที่ยี่สิบสามเมษา Orkes startup จาก Santa Clara ที่ founder คือสามคนที่เป็น original architect ของ Netflix Conductor เมื่อปี สองพันสิบหก ประกาศปิดหกสิบ million Series B นำโดย AVP fund ฝรั่งเศสที่ specialize software infrastructure.

Round นี้มาห่างจาก Series A ยี่สิบ million ของปียี่สิบยี่สิบสี่ ประมาณยี่สิบสองเดือน. pace ที่ตลาด software infra ปัจจุบันถือว่า slow and steady ไม่ใช่ hyper growth.

Orkes ทำอะไร. คำตอบสั้นคือ workflow orchestration ที่ทนทานและปลอดภัยสำหรับ AI agent. Conductor เป็น open source ที่ Netflix สร้างปี สองพันสิบหก เพื่อ orchestrate microservice workflow ที่ต้อง resilient. server crash ตรงกลาง workflow ก็ resume ได้ retry ได้ ดู audit trail ได้ทุก step. Orkes คือ commercial Conductor ที่ extend ให้ทำ AI agent workflow ได้.

ลูกค้าที่เปิดเผยน่าตกใจ. LinkedIn ใช้ Orkes orchestrate AI workflow ภายใน. Twilio ใช้สร้าง agent communication platform. Quest Diagnostics ใช้ใน clinical workflow compliance. United Wholesale Mortgage ใช้ใน lending decision. Naveo Commerce European e-commerce ใช้ใน order fulfillment. Woodside Energy Australian LNG ใช้ใน operational decision. ที่ Orkes หลีกเลี่ยงชื่อ หนึ่งใน world's largest global retailer น่าจะ Walmart หรือ Costco.

ตัวเลขที่โชว์ ตั้งแต่ Series A ยี่สิบสองเดือนก่อน community developer หลายแสนคน install หลายล้าน customer สามเท่าจากเดิม. AVP บอก Forbes ว่า Orkes อยู่ใน tens of millions ARR with 200% YoY growth gross margin มากกว่าเจ็ดสิบห้าเปอร์เซ็นต์.

ของแถมน่าสนใจ Prosperity7 Ventures เป็น new investor. fund ของ Aramco PIF ที่ปกติลงพลังงาน. signal ของ Saudi sovereign capital เริ่มลง AI infrastructure layer จริงจัง. Orkes น่าจะเปิด Riyadh Dubai office ใน Q สาม.

ที่ตลาด AI infra เงียบ ๆ คือ reliability tier. ชั้นใต้ model และ agent layer ที่ทำให้ทุกอย่าง production ready. ปียี่สิบยี่สิบหก เงินกำลังย้ายไปที่ durable execution runtime. Temporal Inngest Restate Orkes รวมระดมทุนสองร้อยห้าสิบ million plus ในสิบแปดเดือน.

Stanford AI Index ปล่อยเม.ย. ระบุว่าแปดสิบเก้าเปอร์เซ็นต์ ของ enterprise AI agent ไม่เคยถึง production. failure mode ไม่ใช่ model accuracy แต่เป็น operational reliability. workflow ค้าง retry หาย audit ไม่ได้ governance fail security review. Orkes ขายแก้จุดนี้ตรง ๆ.

จุดเปราะคือ commoditization risk. hyperscaler มี durable execution อยู่แล้ว AWS Step Functions Azure Durable Functions GCP Workflows. ทำไม enterprise ยอมจ่าย Orkes. คำตอบคือสี่ feature ที่ hyperscaler ขาด multi cloud portability AI native primitive observability ระดับ workflow และ enterprise governance multi tenancy.

สำหรับ OpenBridge นี่คือ direct competitor บวก reference architecture ที่ต้องเข้าใจลึก. ลูกค้า OpenBridge ที่ deploy workflow ซับซ้อนต้องการ durable execution layer แบบ Orkes อยู่แล้ว.

สามทาง หนึ่ง build บน Conductor open source. embed Conductor เป็น engine ของ OpenBridge ภายในหกสิบวัน. ขายเป็น Thai SaaS aware Conductor. ต้นทุนสามถึงสี่คน คูณสองเดือน. สอง partner กับ Orkes โดยตรง. เซ็น reseller deal ขาย OpenBridge powered by Orkes ใน Thailand. สาม compete head on. build durable execution เอง risk สูงสุด moat ลึก.

ผมเชียร์ tactic หนึ่ง build บน Conductor. open source Apache สอง license Netflix battle tested แปดปี Orkes ไม่ block community ใช้. OpenBridge ได้ engine ที่ enterprise CIO รู้จักดีกว่า engine custom บวก control ร้อยเปอร์เซ็นต์ Thai customization.

Action สิบสี่วัน หนึ่ง allocate สอง senior engineer ทำ Conductor PoC workflow ตัวอย่าง FlowAccount invoice K Bank payment check LINE OA send Salesforce log. สอง reach out CTO ของ Orkes Boney Sekh ผ่าน LinkedIn ขอ technical session สามสิบนาที เก็บ insight ว่า Indian enterprise ใช้ Conductor pattern อย่างไร. สาม เปิด blog post OpenBridge runs on Conductor ภายในสามสิบวัน credibility และ SEO play
