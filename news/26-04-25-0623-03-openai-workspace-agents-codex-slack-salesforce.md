---
date: 2026-04-25
slug: openai-workspace-agents-codex-slack-salesforce
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: Editorial illustration of a vast luminous office hallway lined with rows of softly glowing geometric workstations, each radiating thin streams of light that converge into a central pulsing orb suspended overhead, minimal flat geometric shapes, muted slate blue and warm orange palette, soft gradient background, dramatic ceiling lighting, no text no logos no faces
image: images/26-04-25-0623-03-openai-workspace-agents-codex-slack-salesforce.png
---

# OpenAI ส่ง Workspace Agents เข้า GA — Custom GPTs ตาย, Codex-powered "always-on co-worker" เสียบเข้า Slack/Salesforce/Notion ตรง, ฟรีถึง 6 พ.ค.

## TL;DR
- **24 เม.ย.** OpenAI เปิด **Workspace Agents** สู่ general availability บน Business ($20/user/mo) + Enterprise + Edu + Teachers — เข้ามาแทน **Custom GPTs** ที่ launch ปี 2023 อย่างเป็นทางการ
- Powered by **Codex** (cloud-based, partially open-source agentic harness ของ OpenAI), agent run **24/7 always-on** ใน cloud, scheduled execution, multi-step task across native connectors: **Slack, Google Drive, Microsoft 365, Salesforce, Notion, Atlassian Rovo, SharePoint**, ขยายผ่าน custom MCPs
- **Pricing model: ฟรีถึง 6 พ.ค. 2026** จากนั้น **credit-based pricing** (ตัวเลขยังไม่ disclose) — admin ควบคุม tool/action permission ระดับ granular, approval workflow, monitoring ผ่าน Compliance API
- Signal: OpenAI **ปฏิเสธบทบาท runtime-under-Google** อย่างเป็นทางการ — แทนที่จะรอ Gemini Enterprise ดูด workload, OpenAI เอา 800M+ ChatGPT user เป็น **distribution layer** สำหรับ enterprise agent ตรง; กลยุทธ์ "agent ทุกตัวอยู่ใน ChatGPT app เดียว" ที่ Bret Taylor (Sierra) ทำใน B2B ครึ่งทาง

## เกิดอะไรขึ้น

วันศุกร์ที่ 24 เม.ย. ภายในไม่กี่ชั่วโมงหลัง Google ประกาศ $40B ลง Anthropic, OpenAI ปล่อยข่าว GA ของ **Workspace Agents** อย่างเงียบ ๆ บนบล็อก openai.com — ไม่มี livestream ไม่มี Sam Altman tweet ใหญ่ — แต่เนื้อหาคือ end of life formal ของ **Custom GPTs** ผลิตภัณฑ์ที่ OpenAI launch ปี 2023 ที่ Sam Altman เคยพูดว่าเป็น "future of GPT". Custom GPTs ที่อยู่ใน GPT Store ตอนนี้กลายเป็น **legacy mode** — และ enterprise customer ทั้งหมดถูก migrate ไปใช้ Workspace Agents โดยอัตโนมัติ

ความแตกต่างหลักจาก Custom GPTs: Workspace Agents ทำงาน **autonomously ใน cloud** (ไม่ต้อง user เปิด ChatGPT app), **scheduled execution** (รัน task อัตโนมัติทุกชั่วโมง/วัน), เชื่อมตรงกับ third-party SaaS ผ่าน native connectors แทนที่ต้องสร้าง custom action เอง. ตัวอย่าง use case ที่ OpenAI ยกขึ้นใน blog post: "scrape product feedback from web → summarize → post to Slack channel ทุก 8 ชม.", "draft Gmail follow-up emails based on Salesforce CRM data ทุกเช้า", "compile weekly stand-up จาก Notion + GitHub activity"

หัวใจของ technical foundation คือ **Codex** — agentic harness ของ OpenAI ที่ launch ในปี 2025 และเร่ง iterate ใน Q1 2026 (ดูข่าว Codex Mac เม.ย.). Codex ให้ workspace agent มี **persistent file/code/tool/memory** — agent สามารถ build artifact หลาย session, เก็บ state ระหว่าง run, และ collaborate กับ human/agent อื่นใน workspace เดียวกัน. นี่ทำให้ Workspace Agents แตกต่างจาก ChatGPT Plus agent ที่จบทุก task ใน single conversation: agent มี "memory + working directory" เหมือน software engineer

OpenAI ยกตัวอย่าง integration depth: agent บน Slack สามารถ "อ่าน thread channel ที่ user ทำงานอยู่, ดึง file จาก Google Drive ที่ link ใน thread, query Salesforce contact ที่ mention, และ draft response กลับมา" — ทั้งหมดในการ invoke ครั้งเดียว. **Multi-app, multi-step, multi-context** — pattern ที่ Bret Taylor's Sierra ทำใน B2B customer service และ Decagon ทำใน enterprise support, แต่ตอนนี้เป็น **horizontal product** ที่ทุก enterprise ใช้ได้

ในเชิง governance, OpenAI สร้าง enterprise control ที่ครบ: admin กำหนดว่า agent สามารถใช้ tool ใดบ้าง (whitelist/blacklist), ต้อง require approval สำหรับ destructive action (edit spreadsheet, send email, create calendar event, post to Slack), และ monitor ทุก agent run ผ่าน **Compliance API** ที่ stream event ไป SIEM (Splunk, Datadog, Microsoft Sentinel). agent run history เก็บ 90 วัน + immutable audit log สำหรับ regulated industry

Pricing มี twist สำคัญ: **ฟรีถึง 6 พ.ค. 2026** = 12 วันให้ enterprise ทั่วโลก wireup workflow โดยไม่มี cost concern. หลังจากนั้น **credit-based pricing** — OpenAI ยังไม่ disclose rate การ์ด แต่แหล่งข่าว VentureBeat คาดว่าจะอยู่แถว **$0.50-2.00 per agent run** ขึ้นกับ tool/model ที่ใช้. นี่คือ pattern เดียวกับที่ Microsoft ใช้กับ Copilot Studio ปลายปีที่แล้ว — frontload free trial, lock workflow, charge ตาม consumption

## ทำไมสำคัญ

Pattern ที่หนักที่สุดคือ **OpenAI ปฏิเสธบทบาท "runtime-under-Google" อย่างเป็นทางการ**. หลังจาก Gemini Enterprise Agent Platform ของ Google เปิด 22 เม.ย. (control plane + A2A + 200+ models รวม Claude), หลายคนใน VC Twitter พูดว่า OpenAI จะถูกบีบให้เป็น "runtime provider เสียบใต้ control plane" เหมือน database vendor ใต้ Snowflake. ดีล Google-Anthropic $40B ในวันเดียวกันก็ตอกย้ำ thesis นั้น — Google "ซื้อหุ้นในตลาด enterprise" ที่ตัวเองแพ้

Workspace Agents คือ **counter-positioning**: OpenAI ไม่ขายเข้า enterprise IT ผ่าน data lake, ไม่ขายผ่าน API gateway, ไม่ขายผ่าน partner consulting — OpenAI ขายตรง **knowledge worker คนเดียว** ในองค์กรที่เปิด ChatGPT Plus/Team/Business ($20/user/mo). 800M+ ChatGPT user (จำนวนล่าสุดที่ Sam disclose), 5M+ paid Business seat — distribution ที่ Google Cloud ใช้เวลา 5 ปียังไม่ได้แต้ม. Workspace Agents เปลี่ยน **ChatGPT จาก chatbot เป็น operating system** ของ knowledge worker — ตรงกับ playbook ที่ Microsoft ใช้กับ Office 365 ในยุค 2010

จุดที่ OpenAI ยังเสียเปรียบ vs Google: **ไม่มี data lake** (Google มี BigQuery + OneLake ใน Azure คู่แข่ง), **ไม่มี API gateway 30k+ enterprise** (Google มี Apigee), **ไม่มี A2A protocol cross-vendor** (Google ผูก Linux Foundation). OpenAI กำลัง bet ว่า **distribution > infrastructure** — ถ้า ChatGPT app เป็น habit daily ของ knowledge worker, IT แผนกจะต้อง integrate ระบบหลังบ้านเข้า ChatGPT ไม่ใช่ในทางกลับกัน. Bret Taylor (CEO Sierra, OpenAI board) ที่เคยเป็น Salesforce co-CEO น่าจะเป็นผู้ออกแบบ playbook นี้

ผลที่ตามมา 60-90 วัน: **Microsoft ตื่น**. Copilot in Word/Excel/Teams overlap กับ Workspace Agents ตรง ๆ — ถ้าผู้ใช้บริษัท ใช้ ChatGPT Workspace Agent ทำงานข้าม Slack + Google Drive + Salesforce ได้ดีกว่า Copilot, **Office 365 attach rate จะตก**. คาดว่า Build 2026 (พ.ค.) Microsoft จะตอบโต้ด้วย Copilot Workspaces GA + เร่ง M365 Copilot ให้เชื่อม third-party SaaS ดีขึ้น (ปัจจุบันเชื่อมแต่ Microsoft stack). ดีลกับ AI coding startup (Zed, Sourcegraph, Supermaven) จะมาในช่วง 30 วันเป็น defensive play

ข้อสังเกตเชิงกลยุทธ์: **Workspace Agents = "Custom GPTs done right"** หลัง Custom GPTs ล้มเหลวในการ scale (GPT Store ไม่ทำเงินเลย แม้ Sam จะประกาศ revenue share). ความต่าง: Custom GPTs เป็น chatbot template ใน ChatGPT, Workspace Agents เป็น **always-on cloud worker ที่ทำงานข้ามแอป**. นี่คือ admission ว่า OpenAI cycle ผลิตภัณฑ์ปี 2023-2024 ผิดทาง — ตอนนี้กลับมาใหม่พร้อม learning ว่า "agent must do work, not just chat"

## มุม OpenBridge

**Direct competitive overlap — ต้องอ่านอย่างระวัง:** Workspace Agents pitch **เกือบเท่ากับ OpenBridge** — "build agent ที่ทำงานข้าม Slack, Google Drive, Salesforce, Notion ได้". จุดต่างที่ OpenBridge ถือไว้: (1) **Thai SaaS connectors** ที่ ChatGPT ไม่มี — FlowAccount, PEAK, LINE OA, Wongnai, K-Cloud; (2) **multi-model routing** (Claude + GPT + DeepSeek) แทน OpenAI lock-in; (3) **on-prem deployment option** สำหรับลูกค้าที่ data residency Thai. ทั้งสามจุดต้องเร่ง marketing ใน 30 วันก่อน enterprise CIO Thai เริ่มเปิด Workspace Agents บน Plus/Team plan ที่ขายในไทย

**Product action 14 วัน:** (1) **เปรียบเทียบ feature matrix** — สร้างเอกสาร "OpenBridge vs Workspace Agents" ที่ honest แสดง where Workspace Agents ดีกว่า (ChatGPT distribution, Codex maturity) และ where OpenBridge ดีกว่า (Thai SaaS, model neutrality, sovereignty); ใช้เป็น sales tool ตรงสำหรับ Thai customer ที่ถามว่า "ทำไมไม่ใช้ ChatGPT แทน"; (2) **เปิด API connector สำหรับ Slack + Notion + Atlassian** ให้เร็วที่สุด — Workspace Agents มี connector เหล่านี้ในกล่อง, OpenBridge ต้อง match ภายใน 30 วันไม่งั้นเสีย parity; (3) **build "Workspace Agents Migration" path** — ลูกค้าที่เริ่มทดลอง Workspace Agents ใน free trial ตั้งแต่ตอนนี้ (ฟรีถึง 6 พ.ค.) จะมี workflow logic ที่อาจ port มา OpenBridge ได้; ออก documentation + import tool

**Strategic signal:** **credit-based pricing ของ OpenAI** ที่จะเริ่ม 6 พ.ค. = **opportunity ใหญ่สำหรับ OpenBridge**. ลูกค้าที่ใช้ Workspace Agents ฟรี 12 วันแล้วเจอ bill จริง (คาด $0.50-2.00 per run) จะเริ่มมอง alternative — OpenBridge ที่ใช้ DeepSeek V4 backend (ดูข่าวก่อนหน้า) สามารถ offer same workflow ที่ราคา **80-90% ถูกกว่า**. แนะนำ tactic: เปิด landing page "OpenBridge — Agents like ChatGPT, but 5-10x cheaper for Thai workflow" launch 1 พ.ค. รับ traffic จาก Workspace Agents pricing announcement

## Sources
- [Introducing workspace agents in ChatGPT (OpenAI)](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
- [OpenAI unveils Workspace Agents, a successor to custom GPTs for enterprises (VentureBeat)](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more)
- [OpenAI launches workspace agents for enterprise automation (TechBuzz AI)](https://www.techbuzz.ai/articles/openai-launches-workspace-agents-for-enterprise-automation)
- [OpenAI launched 24/7, always-on Workspace Agents in ChatGPT (TestingCatalog)](https://www.testingcatalog.com/openai-launched-24-7-always-on-workspace-agents-in-chatgpt/)
- [OpenAI Replaces Custom GPTs With Workspace Agents Built for Team Workflows (Reworked)](https://www.reworked.co/digital-workplace/openai-launches-workspace-agents-for-enterprise-workflow-automation/)

---

## Audio script
วันศุกร์ยี่สิบสี่เมษา. OpenAI เปิด Workspace Agents เข้า general availability เงียบ ๆ. ไม่มี keynote ไม่มี Sam Altman tweet ใหญ่. แต่เนื้อหาคือ end of life formal ของ Custom GPTs. ที่ Sam เคยพูดเป็น future of GPT ตอนปี 2023.

Workspace Agents ต่างจาก Custom GPTs สามจุด. หนึ่ง รัน autonomously ใน cloud ไม่ต้องเปิด ChatGPT app. สอง scheduled execution รันทุกชั่วโมงทุกวัน. สาม native connector ตรงกับ Slack Google Drive Microsoft 365 Salesforce Notion Atlassian Rovo SharePoint.

heart of the foundation คือ Codex. agentic harness ของ OpenAI. ให้ workspace agent มี persistent file code tool memory. agent build artifact หลาย session เก็บ state ระหว่าง run. workspace agent มี memory plus working directory เหมือน software engineer.

example use case. agent บน Slack อ่าน thread channel ดึง file จาก Google Drive query Salesforce contact draft response กลับมา. ทั้งหมดใน invoke ครั้งเดียว. multi app multi step multi context.

governance ครบ. admin whitelist tool. require approval สำหรับ destructive action. monitor ผ่าน Compliance API stream ไป SIEM. agent run history เก็บเก้าสิบวัน immutable audit log.

pricing twist สำคัญ. ฟรีถึงหกพ.ค. สิบสองวันให้ enterprise wireup workflow โดยไม่มี cost concern. หลังจากนั้น credit based. คาดศูนย์จุดห้าถึงสองเหรียญต่อ agent run.

pattern ที่หนัก. OpenAI ปฏิเสธบทบาท runtime under Google อย่างเป็นทางการ. หลัง Gemini Enterprise สองสิบสองเมษา หลายคนพูด OpenAI จะถูกบีบเป็น runtime ใต้ control plane. ดีล Google Anthropic สี่หมื่นล้านในวันเดียวกันตอกย้ำ. Workspace Agents คือ counter positioning.

OpenAI ขายตรง knowledge worker คนเดียว. ผ่าน ChatGPT Plus Team Business ที่ยี่สิบเหรียญ user ต่อเดือน. แปดร้อยล้าน user ห้าล้าน paid Business seat. distribution ที่ Google Cloud ใช้ห้าปียังไม่ได้.

จุดที่ OpenAI ยังเสียเปรียบ. ไม่มี data lake. ไม่มี API gateway สามหมื่น enterprise. ไม่มี A2A protocol cross vendor. OpenAI bet distribution มากกว่า infrastructure. Bret Taylor ที่เคยเป็น Salesforce co CEO น่าจะ design playbook นี้.

สำหรับ OpenBridge. overlap อันตราย. pitch ใกล้กันมาก. ต่างที่ Thai SaaS connector ChatGPT ไม่มี. multi model routing. on prem deployment.

สิ่งที่ต้องทำสามข้อใน 14 วัน. หนึ่ง เปรียบเทียบ feature matrix OpenBridge vs Workspace Agents honest sales tool. สอง เปิด API connector Slack Notion Atlassian ภายใน 30 วันไม่งั้นเสีย parity. สาม build Workspace Agents Migration path ลูกค้าที่ทดลองตอนนี้ port กลับ OpenBridge.

opportunity ใหญ่ที่สุด. credit based pricing OpenAI หกพ.ค. ลูกค้าเจอ bill จริงจะมอง alternative. OpenBridge ใช้ DeepSeek V4 backend offer same workflow แปดสิบเก้าสิบเปอร์เซ็นต์ถูกกว่า. landing page Agents like ChatGPT but five to ten times cheaper for Thai workflow launch หนึ่งพ.ค.
