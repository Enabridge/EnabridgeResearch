---
date: 2026-06-25
slug: anthropic-400k-sessions-domain-expertise
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial split illustration in two stacked panels. Top panel: a silhouette of a software engineer at a laptop with 5 small action icons floating above the keyboard (file, gear, terminal, browser, commit). Bottom panel: a silhouette of a finance accountant in a blazer at the same laptop with 12 action icons floating above — significantly denser cluster, glowing brighter. Both silhouettes face away from camera. Center divider has a bold sans-serif label "5 vs 12 ACTIONS / PROMPT" rendered large and crisp for thumbnail readability. Muted slate-blue background, single warm desk lamp, flat editorial style, dramatic contrast. 1:1, no real human faces.
image: images/26-06-25-0603-02-anthropic-400k-sessions-domain-expertise.png
---

# Anthropic วิเคราะห์ Claude Code 400,000 sessions — domain expertise ชนะ coding background, expert prompt 1 ครั้ง agent ทำ 12 action vs novice 5 action

## TL;DR
- Anthropic ปล่อย research report 23 มิ.ย. — วิเคราะห์ **400,000 interactive sessions จาก 235,000 คน** (ต.ค. 2025 – เม.ย. 2026) ใน Claude Code แบบ privacy-preserving
- finding หลัก: **occupation อะไรก็สำเร็จในระดับใกล้เคียง software engineer** — accountant, lawyer, biologist, marketer ใช้ Claude Code complete coding task ที่ verify ได้ (test pass / commit เกิดจริง) ในอัตราใกล้กัน. **domain expertise > coding skill**
- expert prompt 1 ครั้ง → agent ทำ **12 action / สร้าง 3,200 words** vs novice 5 action / 600 words
- verified success rate: novice 15% / intermediate–expert 28–33%
- 7 เดือนผ่านไป — sessions ที่ใช้ debug ลด **เกือบครึ่ง**, สัดส่วนใช้ end-to-end agentic (deploy + run + analyze + write docs) เพิ่ม. coding agent กำลังกลายเป็น "general work agent" จริง ๆ ไม่ใช่แค่ pair programmer

## เกิดอะไรขึ้น

Anthropic ปล่อย paper ชื่อ **"Agentic coding and persistent returns to expertise"** — งานวิจัยขนาดใหญ่ที่สุดที่ vendor coding agent เคยปล่อยมา. data set = 400,000 session จาก 235,000 user, ระยะเวลา 7 เดือน. methodology privacy-preserving (aggregate-only, no raw transcript), จัดกลุ่ม user ตาม occupation ที่ self-reported + measure success ด้วย verifiable signal — test pass, commit เข้า repo, deploy command run สำเร็จ — ไม่ใช่ self-report ว่า "พอใจ"

finding ที่จะเป็น quote ของอุตสาหกรรมไปอีกหลายเดือน: **"On coding tasks, every major occupation succeeds at nearly the same rate as software engineers, on average"**. คนทำบัญชี, lawyer, marketer, biology PhD ใช้ Claude Code แล้วได้ผลลัพธ์ที่ verify ได้ในอัตราใกล้ ๆ กับ engineer. นี่คือการ flip กลับ assumption ของวง agentic ทั้งวงที่ pitch กันมาว่า "AI coding tool ทำให้ทุกคนเป็น engineer". ความจริงคือ **มันทำให้ engineer ไม่ใช่ bottleneck อีกแล้ว — domain knowledge ของแต่ละ vertical กลับมาเป็น scarce resource**

หลักฐานเชิงปริมาณที่ชัดที่สุดอยู่ใน **action-per-prompt metric**: novice user → agent ทำ ~5 action ต่อคำสั่ง 1 ครั้ง, generate ~600 words output. expert (in their own domain — ไม่ใช่ expert coder) → agent ทำ **~12 action / 3,200 words**. แปลตรง ๆ คือคนที่รู้ domain ของตัวเองสามารถสั่ง agent ได้ **เข้มข้นขึ้น 2.4 เท่า** ต่อ prompt — เพราะ context, edge case, success criterion ที่เขาฝังในคำสั่งทำให้ agent เลือก action ที่ถูกในชั้นเดียว ไม่ต้องวน clarify

success rate ตามระดับ expertise: **novice 15% / intermediate–expert 28–33%** ของ session แตะ "strictest verified success" ของ Anthropic. gap 2x นี้สำคัญ เพราะมันบอกว่าค่า investment ของ enterprise ไปทาง **ฝึก domain people ให้ใช้ agent เป็น** สูงกว่าการ **จ้าง engineer มาเขียน wrapper**

trend ที่ Anthropic เน้นในตอนท้าย: 7 เดือนของ data ชี้ว่า **session ที่ใช้ debug ลดเกือบครึ่ง** — แทนที่ user จะใช้ Claude Code มา fix bug, ตอนนี้ใช้ deploy, run, analyze data, เขียน document. **Claude Code กำลังเลิกเป็น "AI coding assistant" แล้วกลายเป็น "agentic OS layer"** — ที่ engineer ใช้น้อยลง, ที่ domain worker ใช้มากขึ้น

## ทำไมสำคัญ

นี่เป็น first-party data ที่บอกความจริงที่ vendor อื่นไม่กล้าพูด: **scaling agentic AI ไม่ใช่เรื่อง model capacity แต่เป็นเรื่อง user expertise distribution**. ถ้า Cursor, Windsurf, Replit, Devin ปล่อย analysis แบบนี้น่าจะได้ pattern คล้ายกัน — แต่ไม่มีใครกล้า publish เพราะ implication ของมัน **กระเทือน TAM model ของตัวเอง**. ถ้า coding agent ขายให้ engineer อย่างเดียว market = 30 ล้าน developer ทั่วโลก. ถ้าขายให้ "ทุก domain worker ที่มี laptop" market = 1+ พันล้าน. Anthropic เปิด data นี้ออกมาตอนนี้เพราะกำลังจะ IPO ที่ valuation $965B ในเดือน ต.ค. — เขาต้องการ narrative ที่ extend TAM ออกไปจาก dev tool

อีกหนึ่ง implication ที่ enterprise CIO ต้องอ่านระหว่างบรรทัด: **เริ่ม shift budget จาก "buy more coding seat" ไปทาง "buy domain training + lightweight agent surface"**. accountant ที่รู้ Thai accounting law + ใช้ Claude Code สั่ง agent run python pandas บน export ของ Xero/QuickBooks/PEAK = output ที่ engineer ภายในทำเองยังช้ากว่า. CIO ที่ยังคิดว่า "agent = developer productivity tool" จะถูกแซงโดย CIO ที่ deploy agent ให้ทั้งบริษัท

ที่น่าจับตาคือ Anthropic publish ข้อมูลนี้ก่อน Salesforce Dreamforce (15–17 ก.ย.) แค่ 3 เดือน. Marc Benioff pitch มาตลอดว่า "Agentforce runs the world" — แต่ Agentforce ออกแบบสำหรับ "structured CRM workflow with predefined agent skill". Anthropic data เพิ่งโชว์ว่า **ของจริงเกิดเมื่อ domain worker เขียน prompt ผสม context ของตัวเอง** — model ตรงข้ามกับ pre-built skill catalog. ถ้า Salesforce ไม่ pivot ไป "BYO agent + connect Agentforce data" pattern, Claude Code/ChatGPT business desktop จะ eat ส่วน workflow automation จาก below

## มุม OpenBridge

**Strategic insight:** OpenBridge **ไม่ควร positioning เป็น "agent platform"** — competition กับ Anthropic/OpenAI/Microsoft ที่ตัว model + UI surface คุมตลาดอยู่แล้วจะแพ้. positioning ที่ data ของ Anthropic บอกโดยอ้อมคือ **"connector + domain context provider สำหรับ Thai SME"** — ตอบโจทย์ "accountant ไทยที่อยากใช้ Claude Code จัดการ FlowAccount + PromptPay + LINE OA" โดยที่ OpenBridge เป็น **MCP server ที่ embed domain expertise ของ Thai SaaS ecosystem**

**Product pivot 30 วัน:**
1. **เลิกโฆษณา "build your own AI agent"** — domain worker ส่วนใหญ่ไม่ build agent, เขาใช้ agent (Claude, ChatGPT, Copilot) สั่งงาน. positioning ของ OpenBridge ควรเป็น **"plug Thai SaaS ของคุณเข้า agent ที่คุณใช้อยู่"**
2. **build "domain prompt library" สำหรับ vertical ไทย** — accountant, retail, salon, restaurant, freight — แต่ละ vertical มี starter prompt 10 ตัวที่ทำงานจริงผ่าน OpenBridge MCP. ตัวอย่าง: "ดู transaction ใน K-Plus เดือนนี้ที่ยังไม่ออกใบเสร็จใน FlowAccount แล้วสร้างใบเสร็จ + ส่ง LINE OA ลูกค้า". prompt library เป็น distribution channel — free tier เข้าได้จาก ChatGPT/Claude Code โดยตรง
3. **measure metric เลียนแบบ Anthropic** — track ใน MCP server: action-per-prompt, verified completion rate. ปล่อย public dashboard ในไตรมาส 4 — เป็น **proof of OpenBridge value** ที่ enterprise sales จับต้องได้

**Hiring implication:** อย่าจ้าง engineer เพิ่มสำหรับ build connector — **จ้าง "domain SME contractor"** (accountant ที่มี CPA, retail ops ที่เคยรัน 30 สาขา) มา write prompt + test agent flow. cost effective กว่า, output match user reality ของลูกค้า. ตรงตาม insight ของ Anthropic ที่ว่า expertise > coding skill ในยุค agentic

## Sources
- [Anthropic — Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise)
- [TheRouter.ai — What 400K Claude Code Sessions Reveal About Domain Expertise and Model Tier Routing](https://therouter.ai/news/anthropic-claude-code-expertise-routing-session-data-2026/)
- [TechTimes — AI Coding Agents Reward Domain Expertise, Not Coding Skill: Anthropic Study of 400K Sessions](https://www.techtimes.com/articles/318955/20260623/ai-coding-agents-reward-domain-expertise-not-coding-skill-anthropic-study-400k-sessions.htm)
- [TIGZIG — What Decides Whether a Coding Session Succeeds? Anthropic's New Study Says Domain Expertise, Not Coding Background](https://www.tigzig.com/post/anthropic-claude-code-expertise-survey-jun2026)

---

## Audio script
Anthropic ปล่อย research ใหญ่ที่สุดในวงการ agentic วันที่ยี่สิบสามมิถุนา. paper ชื่อ Agentic coding and persistent returns to expertise. data จากสี่แสน session ของ Claude Code. สองแสนสามหมื่นห้าพันคน. เก็บเจ็ดเดือนตั้งแต่ตุลาปีที่แล้วถึงเมษานี้.

finding ที่จะถูก quote ไปอีกหลายเดือน. คนทำบัญชี lawyer marketer biology PhD ใช้ Claude Code complete coding task ที่ verify ได้ในอัตราใกล้กับ software engineer. flip กลับ assumption ของวง agentic ทั้งวง. AI coding tool ไม่ได้ทำให้ทุกคนเป็น engineer. มันทำให้ engineer ไม่ใช่ bottleneck แล้ว. domain knowledge ของแต่ละ vertical กลับมาเป็น scarce resource.

หลักฐานเชิงตัวเลขชัดที่สุด. novice prompt หนึ่งครั้ง agent ทำห้า action สร้างหกร้อยคำ. expert prompt หนึ่งครั้ง agent ทำสิบสอง action สร้างสามพันสองร้อยคำ. คนที่รู้ domain สั่ง agent ได้เข้มข้นกว่าสองจุดสี่เท่า. success rate verified strictest. novice สิบห้าเปอร์เซ็นต์. expert ยี่สิบแปดถึงสามสิบสามเปอร์เซ็นต์. gap สองเท่า.

trend ใหญ่ที่สุด. เจ็ดเดือนผ่านไป session ที่ใช้ debug ลดเกือบครึ่ง. user เปลี่ยนไปใช้ deploy run analyze data เขียน document. Claude Code เลิกเป็น coding assistant แล้ว. กำลังกลายเป็น agentic OS layer สำหรับ knowledge worker ทุก domain.

implication สำหรับ enterprise CIO. ย้าย budget จาก buy more coding seat ไป buy domain training + lightweight agent surface. accountant ที่รู้กฎหมายภาษีไทย + Claude Code run python บน export ของ Xero PEAK FlowAccount เร็วกว่า engineer ภายในทำเอง.

สำหรับ OpenBridge. อย่า position เป็น agent platform. แพ้ Anthropic OpenAI Microsoft แน่ ๆ. ให้ position เป็น connector + domain context provider สำหรับ Thai SME. plug Thai SaaS เข้า agent ที่ user ใช้อยู่. action สามสิบวัน. หนึ่ง เลิกโฆษณา build your own AI agent. สอง build domain prompt library สำหรับ vertical ไทย. accountant retail salon restaurant freight. สาม measure action per prompt + verified completion ใน MCP server แล้วเปิด public dashboard ไตรมาสสี่. hiring implication. อย่าจ้าง engineer เพิ่ม. จ้าง domain SME contractor มาเขียน prompt + test flow. ตรงตามที่ Anthropic data บอก expertise ชนะ coding skill ในยุคนี้.
