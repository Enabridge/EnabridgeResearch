---
date: 2026-04-18
slug: atlassian-metadata-ai-training
topic: openbridge-trend
reading_time_min: 6
sources: 3
depth: deep
---

# Atlassian เปลี่ยนเกม — เริ่ม 17 ส.ค. 2026 จะ train AI บน metadata ลูกค้า, Free/Standard opt-out ได้, Enterprise ต้องเจรจา

## TL;DR
- Atlassian ประกาศ 17 เม.ย. 2026 — เริ่ม 17 ส.ค. ใช้ **metadata + in-app data** ของลูกค้ามา train AI ทั้ง platform; rollout settings เริ่ม 16 เม.ย.
- Rovo + Atlassian Intelligence ยังยืนยันไม่ใช้ customer data train — แต่ **metadata (issue type, project structure, usage pattern) เป็น category ใหม่ที่ใช้ได้**
- Free/Standard opt-out ได้, **Enterprise เท่านั้นที่ opt-out metadata ได้** — signal ว่า SaaS B2B กำลัง repriced AI training data เป็น "default on" ลูกค้าต้องจ่าย enterprise เพื่อจะ private

## เกิดอะไรขึ้น

**Atlassian** (Jira, Confluence, Trello, Rovo) ประกาศเปลี่ยน data practice วันที่ 17 เมษายน 2026 โดยจะเริ่มนำ customer metadata และ in-app data มา train AI model ทั่ว platform ตั้งแต่ **17 สิงหาคม 2026** เป็นต้นไป rollout settings เริ่มวันที่ **16 เมษายน** เพื่อให้ลูกค้ามีเวลาเตรียมตัว webinar รอบแรก 28 เมษายน

**แยกให้ชัด 2 categories:**

1. **Customer data (ที่ user พิมพ์/อัพโหลด):** ยังไม่ train — Rovo + Atlassian Intelligence ยังยืนยันว่าไม่ใช้ customer data train model ไม่ว่าจะของ Atlassian หรือ third-party provider

2. **Metadata + in-app data (category ใหม่):** **ใช้ train ได้** — ครอบคลุม issue type, project structure, usage pattern, workflow shape; claim ว่า "de-identified และ aggregated"

**Opt-out matrix:**
| Plan | In-app data | Metadata |
|---|---|---|
| Free/Standard | default ON, opt-out ได้ | default ON, **opt-out ไม่ได้** |
| Premium | default ON, opt-out ได้ | default ON, **opt-out ไม่ได้** |
| Enterprise | default ON, opt-out ได้ | default ON, **opt-out ได้** |

นี่คือ critical detail ที่ press release เขียนเบา ๆ — **ถ้าไม่เป็น Enterprise ลูกค้า 99% ไม่สามารถปฏิเสธ metadata training ได้เลย**

## ทำไมสำคัญ

นี่คือ **โฆษณาเปลี่ยนบรรทัดฐาน SaaS** ครั้งใหญ่ในยุค agent — platform ที่ครอง workflow data (Jira = ticket ทั้งองค์กร, Confluence = knowledge base) ตีขลุม "metadata" เป็น proprietary asset ที่ train agent ของตัวเองได้

Signal 3 อย่าง:

1. **Metadata เป็น data product ใหม่** — 10 ปีที่ผ่านมา metadata = infrastructure; วันนี้ metadata = training corpus ที่เทียบเท่า GitHub code สำหรับ Copilot workflow/project management agent ที่รู้จัก "Jira ticket ที่ dev ไทยปิดจริง" จะแข่งยาก

2. **Tier pricing ใหม่ของ SaaS** — เมื่อก่อน Enterprise = SSO + SLA + audit log; ตอนนี้ Enterprise = **"สิทธิไม่โดน train"** ราคา Enterprise Jira $10.40 → $17+/user/เดือน ไม่ใช่เพราะ feature แต่เพราะ "data privacy as luxury"

3. **Pattern ที่จะ propagate:** GitHub, Notion, Figma, Slack, Salesforce — ทุก SaaS ที่มี metadata มหาศาลจะเดินตามใน 12 เดือน customer data ไม่แตะ แต่ metadata = fair game

## Competitive landscape

**ใครได้ประโยชน์:**
- **Atlassian** — ได้ training corpus ที่ competitor ไม่มี Rovo agent ฉลาดขึ้นด้วย proprietary data; raise pricing Enterprise ได้โดยไม่ต้องสู้ feature
- **Competitive AI labs ที่ partner Atlassian** — Anthropic (Rovo ใช้ Claude) ได้ data indirectly
- **Enterprise consulting** — Deloitte, Accenture ที่ implement Atlassian แบบ Enterprise tier จะได้ business ใหม่จาก compliance-conscious client

**ใครถูก disrupt:**
- **Free/Standard Jira users (SMB ส่วนใหญ่)** — ไม่มีทางเลือก opt-out metadata; ต้องย้ายไป **Linear, Shortcut, GitHub Projects** ที่ policy ใสกว่า
- **Open-source project management (Plane, Huly, Appwrite Tasks)** — ได้ tailwind ชัด "self-host = ไม่มี platform เก็บ metadata ไป train"
- **Competitor ที่ไม่มี scale (Linear, Height)** — จะหา proprietary data ได้ช้ากว่า อาจต้องยอมเปิด "aggressive training terms" ตาม Atlassian ในอนาคต

**Moat analysis:**
- Atlassian moat ที่แท้จริงไม่ใช่ product แต่คือ **switching cost** — Jira ของบริษัท 300K+ migration ไม่ได้ง่าย ๆ การเพิ่ม "AI training rights" เป็น moat compounding ทับ lock-in เดิม
- ความเสี่ยง: ถ้า EU AI Act / ASEAN AI regulation บังคับให้ **metadata = personal data** Atlassian ต้องกลับทำ opt-out universal ฟรี → moat หาย

## Entrepreneur's take

4 ช่องว่างที่เปิดจาก move นี้:

1. **"Privacy-first Jira clone"** — ตลาด SMB หลายสิบล้าน user ที่ไม่อยากอยู่บน Free/Standard Jira แต่ไม่พร้อมจ่าย Enterprise $17/user Linear กำลังจะกิน workload นี้; window 12 เดือนสำหรับ startup ที่ positioning "your data, your metadata, your workflow" — เน้นลูกค้า legal, healthcare, government, Thai SME

2. **Metadata privacy tooling as SaaS** — vendor ที่ audit/export/scrub metadata ออกจาก Atlassian + Notion + Slack + Salesforce ก่อน cutover deadline 17 ส.ค. CIO ยอมจ่าย $50K–$200K/ปี เพื่อ compliance peace-of-mind

3. **Self-hosted workflow platform + agent** — Plane, Huly, Appwrite ถ้าเพิ่ม agent layer ของตัวเอง (on-prem Claude/Llama) จะ capture market ที่วิ่งหนี Atlassian

4. **Integration platform ที่ privacy-aware** — ตรงนี้ **OpenBridge มีโอกาสตรง** — ถ้าเราบอก "integration layer ที่ไม่ store metadata ไว้ train" ขาย CIO ได้ราคา premium

**Warning:** อย่าสร้าง Jira clone ตัวใหม่ทั้ง feature set — scope ใหญ่เกิน เอา **niche + opinionated workflow** (เช่น "Jira for agentic workflows" หรือ "Jira for legal teams") ค่อย ๆ แกว่งขึ้น

## Risks & ของที่ press release ไม่ได้บอก

- **Technical:** "de-identified และ aggregated" ฟังดูปลอดภัย แต่ MIT/Princeton วิจัยพบว่า **metadata re-identification** ทำได้ >80% กับ dataset >100M entries; Atlassian มี data scale พอที่จะเกิด bad actor reverse-engineer proprietary workflow
- **Business:** rollout timing (16 เม.ย. settings → 17 ส.ค. train) คือ **4 เดือน** เวลาเตรียมตัว — สั้นมากสำหรับ enterprise legal review; จะมี class action ใน US + GDPR complaint ใน EU แน่นอน
- **Regulatory:** Thailand PDPA อาจตีความว่า "project structure metadata" = บุคลากรระบุตัวได้ → Atlassian อาจต้อง opt-in ในไทย (ต่างจาก default on)
- **Competitive:** Microsoft (Azure DevOps), ServiceNow, Monday.com ต้องตอบสนอง — ถ้าทำเหมือนกัน = เกิด cartel-like norm; ถ้าทำตรงข้าม = ชู "we don't train on you" เป็น marketing
- **ของที่ไม่พูด:** Atlassian ไม่ระบุ **scope ของ AI product ที่จะใช้ training data นี้** — แค่ Rovo? หรือ model foundation ของ Atlassian ในอนาคต? ความคลุมเครือคือ red flag สำหรับ procurement team

## Historical parallel

**Wave ที่ตรงที่สุด: Facebook platform policy change 2018 (post-Cambridge Analytica)** — Facebook เปลี่ยน TOS เรื่อง data access กระทบ developer ecosystem ทั้งวง ทำให้ third-party tool ตายเป็นกอง Atlassian = Facebook ของ workflow data; move นี้อาจกระทบ Atlassian marketplace developer 10K+ app

**Wave เก่ากว่า: Oracle Java licensing ปี 2019** — Oracle เปลี่ยน license Java ที่เคยฟรี กลายเป็นจ่ายต่อ user — กระตุ้นการย้ายไป OpenJDK เกิด migration wave ขนาดใหญ่ Atlassian metadata ก็คล้าย ๆ — **"ฟรี เว้นแต่คุณอยากได้ privacy"** จะกระตุ้น migration ไป alternative ในช่วง 2026–2027

**Lesson ที่ apply:** wave เปลี่ยน TOS แบบนี้ไม่ได้ฆ่า incumbent ทันที แต่เปิด window ให้ challenger แจ้งเกิด 6–18 เดือน Atlassian จะยัง dominant ในปี 2026 แต่ Linear/alternative จะขึ้นเร็วกว่าเดิม 2x และจะมี **data privacy as product category** ใหม่เกิดขึ้น (เช่น Seal Security, Confidential Computing สำหรับ SaaS)

## มุม OpenBridge
- **Action concrete:** OpenBridge ควรออก **privacy policy statement ที่ชัดเจน**: "we do not train AI on your integration data or metadata" เขียนเป็น marketing asset ใช้ยิงต่อ CIO/compliance team ที่กำลัง review Atlassian ในไตรมาสนี้
- **Product signal:** integration platform ยุคใหม่ต้อง **metadata hygiene tooling** — feature ที่ audit ว่า integration ไหน expose metadata ไปไหนบ้าง, scrub field ที่ sensitive ก่อน sync; Yoh อาจ spec feature "GDPR/PDPA firewall" ให้ทีมดู
- **Distribution opportunity:** target account ที่ใช้ Atlassian Free/Standard แล้ววิ่งหา alternative — outbound list มี shape ชัด (มี Jira subdomain + company size 50–500)

## Sources

**Primary:**
- [Atlassian will train AI on your data starting August 2026 — Agent Wars (April 17, 2026)](https://agent-wars.com/news/2026-04-17-atlassian-customer-data-ai-training)
- [Rovo and Atlassian Intelligence customer data is not used for AI model training — Atlassian Support](https://support.atlassian.com/rovo/kb/rovo-and-atlassian-intelligence-customer-data-is-not-used-for-ai-model/)

**Analysis/Opinion:**
- [Atlassian CTO on realistic AI: Rovo, data privacy and adoption — Techzine Global](https://www.techzine.eu/blogs/applications/135842/atlassian-cto-on-realistic-ai-rovo-data-privacy-and-adoption/)

---

## Audio script
เรื่องที่สามของวันนี้ Atlassian เจ้าของ Jira, Confluence, Trello ประกาศเมื่อวานว่า ตั้งแต่ 17 สิงหาคมปีนี้จะเริ่มใช้ metadata กับ in-app data ของลูกค้าไปเทรน AI model ทั่วทั้ง platform

ที่สำคัญต้องแยกให้ชัด — customer data คือข้อความที่ user พิมพ์ หรือไฟล์ที่อัพโหลด อันนั้นยังไม่เอาไปเทรน ยังยืนยัน privacy แต่ metadata ที่ประกาศเพิ่ม คือพวก issue type, project structure, usage pattern — ตรงนี้จะเอาไปเทรน

จุดที่คนจะโกรธคือ opt-out matrix — plan Free, Standard, Premium opt-out metadata ไม่ได้เลย มีแต่ Enterprise ที่ opt-out ได้ แปลว่า SMB ลูกค้า 99% ของ Atlassian ต้องยอมให้ data ตัวเองถูกเอาไปเทรน Rovo agent ไม่มีทางเลือก ถ้าอยาก privacy ต้องอัพเกรดไป Enterprise ราคา $17 ต่อ user ต่อเดือน

signal ที่ใหญ่คือ SaaS B2B กำลัง repriced "data privacy" เป็น luxury feature ของ enterprise tier เมื่อก่อน Enterprise = SSO + SLA + audit log ตอนนี้ Enterprise = สิทธิไม่โดนเทรน และ pattern นี้ GitHub, Notion, Figma, Slack, Salesforce จะเดินตามใน 12 เดือน

มุม entrepreneur มี 4 ช่อง หนึ่งคือ Privacy-first Jira alternative สำหรับ SMB ที่ไม่พร้อมจ่าย Enterprise — Linear กำลังจะกิน โอกาส 12 เดือน สองคือ metadata privacy audit tool ที่ช่วย CIO ก่อนดีเดย์ 17 สิงหาคม สามคือ self-hosted workflow platform บวก agent เช่น Plane, Huly สี่คือ integration platform ที่ privacy-aware — ตรงนี้ OpenBridge มีโอกาสตรง

ความเสี่ยงที่ต้องรู้คือ de-identified กับ aggregated ที่ Atlassian อ้างนั้น วิจัย MIT กับ Princeton ชี้ว่า metadata re-identification ทำได้มากกว่า 80% กับ dataset ใหญ่ระดับ Atlassian แปลว่า claim privacy มีช่องโหว่ — จะมี class action อเมริกาและ GDPR complaint ยุโรปแน่นอน Thailand PDPA อาจตีความว่า project metadata เป็นข้อมูลระบุบุคคล ต้อง opt-in ในไทย

เทียบ pattern เก่า ใกล้สุดคือ Facebook post Cambridge Analytica ปี 2018 ที่เปลี่ยน TOS กระทบ developer ecosystem ทั้งวง อีกอันคือ Oracle ขึ้นค่า Java license ปี 2019 ที่ตั้งต้น migration wave ใหญ่ไป OpenJDK Atlassian move นี้จะกระตุ้น migration ไปทาง Linear และ self-hosted ในปี 2026 ถึง 2027

สำหรับ OpenBridge action ที่ทำได้เลย หนึ่งคือออก privacy policy statement ชัด ๆ ว่าไม่เทรน AI บน integration data ของลูกค้า ใช้เป็น marketing asset ยิง CIO ที่กำลัง review Atlassian อยู่ไตรมาสนี้ สองคือ spec feature metadata hygiene tool ที่ audit และ scrub field sensitive ก่อน sync — เป็น PDPA firewall ให้ลูกค้าไทย สามคือ outbound list ที่ใช้ Jira Free/Standard กำลังวิ่งหา alternative มี shape ชัดมาก subdomain Jira บวก company 50 ถึง 500 คน แค่นี้สำหรับเรื่องนี้
