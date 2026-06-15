---
date: 2026-06-15
slug: snowflake-coco-72-percent-ade-bench
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a glowing Snowflake-blue snowflake logo at the center of
  a data warehouse, with two smaller robotic agents standing in second and third
  place on a podium nearby, labeled "Claude Code 65.1%" and "Codex 65.1%". The
  central snowflake bears a large gold numeral "72.1% ADE-Bench" floating above it,
  with a smaller tag "CoCo" pinned at its base. Behind the podium, rows of glowing
  data cubes stretch into the distance. Render style: cinematic editorial
  illustration, isometric perspective, deep arctic-blue background with cyan and
  silver accent light, dramatic depth, high-contrast typography legible at 200px
  thumbnail. No real human faces — only robotic silhouettes.
image: images/26-06-16-0603-04-snowflake-coco-72-percent-ade-bench.png
---

# Snowflake CoCo 72.1% ADE-Bench — vertical coding agent ที่ตี Claude Code + Codex ด้วยข้อมูลที่ general-purpose ไม่มี

## TL;DR
- Snowflake Summit 2026 (1–4 มิ.ย.) เปิดตัว CoCo (Cortex Code) — coding agent ที่ scored **72.1%** บน ADE-Bench (data-engineering benchmark ของ dbt Labs) เทียบ Claude Code + OpenAI Codex ที่ 65.1% ทั้งคู่
- 7,100+ Snowflake customers กำลัง build บน CoCo แล้ว — รวม Cognizant ที่มี 2,250 users, 30+ enterprise use cases, 1.3M+ AI requests
- Ship ผ่าน Desktop, Slack bot, mobile, VS Code, Excel extension และ Claude Code extension — model-agnostic, plug-and-play ในทุก editor

## เกิดอะไรขึ้น

ที่ Snowflake Summit 2026 (1–4 มิ.ย., San Francisco) Snowflake เปิดตัว **CoCo** — coding agent ที่ rebrand จาก Cortex Code — พร้อมตัวเลข benchmark ที่ทำให้ทั้งวง engineering หยุดดู: **72.1%** บน ADE-Bench (Analytics Data Engineering benchmark ที่ dbt Labs สร้าง) เทียบ **65.1%** ของทั้ง Claude Code และ OpenAI Codex — gap 7 จุดที่ statistically significant และ practical relevant สำหรับงาน data engineering ที่ดูเหมือนตรงไปตรงมาแต่ความจริงเต็มไปด้วย context: schema, lineage, governance, dbt models, dimension models, semantic layers

ของจริงที่ทำให้ CoCo ชนะคือ — มันรู้ **เนื้อในของ Snowflake** ที่ general-purpose agent ไม่รู้ Claude Code + Codex ฉลาดในการเขียนโค้ด แต่ไม่รู้ว่าใน Snowflake instance ของลูกค้ามีตาราง schema, ใครเป็น owner, มี policy อะไร, dimension ไหน aggregate ไหน CoCo ฝังตัวใน Snowflake metadata + governance layer พร้อมเข้า — เหมือนกับ DBA ที่ทำงานในบริษัทมา 10 ปี เทียบ contractor ใหม่ที่เพิ่งเข้า nuance นี้คือ "**moat ของ vertical agent คือ context ที่ horizontal agent ไม่สามารถมี**"

CoCo ship ใน 6 surface พร้อม: Desktop app, Slack bot, mobile, VS Code extension, Excel extension, และ Claude Code extension — สังเกตว่ามี Claude Code extension เป็น distribution surface นี่เป็น **co-opetition** ที่น่าสนใจ — Snowflake ใช้ Anthropic เป็น model layer underneath (ผ่าน $200M Cortex partnership ที่ปิด ธ.ค. 2025) แต่ก็แข่งกับ Claude Code ใน workflow data engineering ลูกค้าใช้ Claude Code เป็น editor → call CoCo เป็น specialized agent ผ่าน MCP-style extension

**Customer traction** เป็นของจริง — **7,100+ Snowflake customers** กำลัง build บน CoCo แล้ว Cognizant report สาธารณะ: **2,250 users, 30+ enterprise use cases, 12+ custom skills, 90+ accelerators, 1.3M+ AI requests** ตัวเลขนี้ใหญ่กว่า production deployment ของ general-purpose agent หลายตัว และที่สำคัญ — มันมาจากลูกค้าหนึ่งราย ไม่ใช่ aggregate ที่ vendor บอกเอง Cognizant ใช้ CoCo ใน contract delivery ที่ client ปลายทางจ่ายเงิน — ระดับ production จริง

Snowflake รอบนี้ยังเปิด **Datastream** (managed Apache Kafka streaming) ไปด้วย — message ที่รวมกันคือ "Snowflake เป็น platform เดียวที่จัดการทั้ง batch (warehouse), stream (Datastream), agent (CoCo) บน governed data" ซึ่งคือการทำ vertical integration ที่ Databricks ก็พยายามตามแบบนี้

## ทำไมสำคัญ

**Vertical agents กำลังเอาชนะ horizontal agents ในงาน high-context** — CoCo ไม่ใช่กรณีโดดเดี่ยว Hebbia ชนะใน financial documents, Harvey ชนะใน legal, CoCounsel ชนะใน legal research, Cursor + Windsurf ยังต้องเร่งใน general coding pattern ทั่วไปคือ: foundation model เก่งทำ "30-second task" ทั่วๆ ไป แต่งานที่ต้องการ context มากกว่า 200K token ของ enterprise schema/data/policy นั้น **agent ที่ฝังในระบบเจ้าของข้อมูลจะเก่งกว่าเสมอ** — moat ไม่ใช่ model weights แต่เป็น privileged access ต่อ context

**Co-opetition pattern** ระหว่าง Snowflake-Anthropic เป็น template ใหม่ — Snowflake จ่าย Anthropic $200M เพื่อใช้ Claude model + เป็น launch partner ของ Fable 5 แต่ก็แข่ง Claude Code โดยตรงในผลิตภัณฑ์ CoCo สมการนี้ทำงานได้เพราะ revenue mix: Anthropic ได้ token spend, Snowflake ได้ data warehouse spend + agent license spend ทั้งคู่โต พร้อมกัน Anthropic ไม่ลงไปแข่งใน vertical data agent เพราะจะ alienate cloud data platform partner ทุกราย

ที่ต้องจับตา — ถ้า CoCo ทำได้ที่ Snowflake แล้ว — **Databricks ต้องตอบใน Q3/Q4** ด้วย agent ของตัวเองที่ specific เท่าๆ กัน (มี Genie + Mosaic อยู่ แต่ยังไม่ benchmark ชน CoCo สาธารณะ) และทุก vertical SaaS ใหญ่ๆ (Salesforce, ServiceNow, Workday, SAP) จะมี vertical agent ของตัวเองภายใน 12 เดือน — เพราะถ้าไม่มี ลูกค้าจะใช้ Claude Code/Codex มา query ระบบเขาเอง โดยไม่ผ่านการขายอะไรเพิ่ม

## มุม OpenBridge

นี่คือ **คำเตือนที่ OpenBridge ต้องเอาจริง** — ถ้า horizontal integration platform ไม่มี "vertical context" ที่ลึก, vertical SaaS แต่ละราย (Snowflake, Salesforce, Workday) จะมี agent ของตัวเองที่ "เข้าใจระบบของตัวเอง" ดีกว่า integration platform เข้าใจ และ agent vertical จะ pull ลูกค้าออกจาก integration layer ของเรา ทางออกคือ — OpenBridge ต้องเลือก vertical 2-3 อันที่จะ "**ฝัง context**" ลึกพอ ๆ กับ vertical agent — ไม่ใช่แค่ adapter แต่เป็น semantic layer + governance map + relationship graph ของ data ใน vertical นั้น

อีกประการ — **MCP เป็นกลไกที่ vertical agent กับ horizontal platform อยู่ร่วมกันได้** — CoCo มี Claude Code extension ผ่าน MCP style แสดงว่า extension pattern ทำให้ vertical agent "ปรากฏใน editor ใดก็ได้" OpenBridge ควร position ตัวเองเป็น MCP server ที่ Claude Code / Cursor / Windsurf / Codex สามารถ install ได้ใน 1 คำสั่ง — แทนที่จะรอ developer เปิด editor ของเราเอง การ meet developer ใน editor ที่พวกเขาใช้อยู่ แล้วแสดง integration capability ผ่าน MCP คือ distribution strategy ที่ leverage installed base ของ horizontal agent ในขณะที่เราเป็น "tool layer ที่พวกเขา reach for"

## Sources
- [Snowflake CoCo Redefines Enterprise AI Development as the Coding Agent — Snowflake Press](https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/)
- [Snowflake CoCo: AI Coding Agent for the Modern Data Stack — Snowflake Blog](https://www.snowflake.com/en/blog/snowflake-coco-ai-coding-agent-modern-data-stack/)
- [Snowflake thinks it knows what's really slowing developers down — The New Stack](https://thenewstack.io/snowflake-coco-coding-agent/)
- [AI agents free 1,300 hours, cut costs as Cognizant scales Snowflake CoCo — Stock Titan](https://www.stocktitan.net/news/CTSH/cognizant-accelerates-enterprise-ai-adoption-with-snowflake-s-cortex-956mbwmq62wf.html)
- [Snowflake and Anthropic Announce $200 Million Partnership — Snowflake Press](https://www.snowflake.com/en/news/press-releases/snowflake-and-anthropic-announce-200-million-partnership-to-bring-agentic-ai-to-global-enterprises/)

---

## Audio script
สวัสดีครับ Yoh ข่าวสุดท้ายเช้านี้เรื่อง vertical agent ที่ตี horizontal agent ใน benchmark ที่สำคัญ Snowflake เปิดตัว CoCo ที่ Summit 2026 ปลายเดือนพฤษภาคมถึงต้นมิถุนายน scored 72.1 เปอร์เซ็นต์บน ADE-Bench ที่ dbt Labs สร้างขึ้น เทียบกับ Claude Code และ OpenAI Codex ที่ได้ 65.1 เปอร์เซ็นต์ทั้งคู่ Gap เจ็ดจุดที่ statistically significant ของจริงที่ทำให้ CoCo ชนะคือมันรู้เนื้อในของ Snowflake schema lineage governance dbt model ที่ general-purpose agent ไม่รู้ เหมือน DBA ที่ทำงานในบริษัทมาสิบปีเทียบ contractor ใหม่ที่เพิ่งเข้า nuance นี้คือ moat ของ vertical agent คือ context ที่ horizontal agent ไม่สามารถมี Customer traction เป็นของจริง 7,100 ลูกค้า Snowflake กำลัง build บน CoCo Cognizant report สาธารณะ 2,250 users 30 use cases 12 custom skills 90 accelerators 1.3 ล้าน AI requests ตัวเลขจากลูกค้าหนึ่งราย ไม่ใช่ aggregate ที่ vendor บอก Snowflake รอบนี้ยังเปิด Datastream เป็น managed Kafka streaming message ที่รวมคือ platform เดียวที่จัดการทั้ง batch stream agent บน governed data Pattern ที่กำลังชัดคือ vertical agents กำลังเอาชนะ horizontal agents ในงาน high-context Hebbia ชนะ finance Harvey ชนะ legal CoCounsel ชนะ legal research Cursor Windsurf ต้องเร่งใน general coding มุม OpenBridge มีคำเตือนตรงๆ ถ้า horizontal integration platform ไม่มี vertical context ที่ลึก vertical SaaS แต่ละรายจะมี agent ของตัวเองที่เข้าใจระบบของตัวเองดีกว่าเรา ทางออกคือเลือกสองถึงสาม vertical ที่จะฝัง context ลึกเท่า vertical agent ไม่ใช่แค่ adapter แต่เป็น semantic layer governance map relationship graph อีกประการ MCP เป็นกลไกให้ vertical agent กับ horizontal platform อยู่ร่วมกันได้ OpenBridge ควร position ตัวเองเป็น MCP server ที่ Claude Code Cursor Windsurf Codex install ได้ในหนึ่งคำสั่ง แทนที่จะรอ developer เปิด editor ของเราเอง การ meet developer ใน editor ที่เขาใช้อยู่ แล้วแสดง capability ผ่าน MCP คือ distribution strategy ที่ leverage installed base ของ horizontal agent ครับ
