---
date: 2026-06-09
slug: microsoft-mai-models-build-2026-openai-decoupling
topic: agentic-ai
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial illustration of two oversized chess pieces facing off on a fractured
  glass board — a Microsoft-branded king on the left labeled "MAI-Code-1-Flash"
  glowing turquoise, and a smaller OpenAI-branded rook on the right dimmed and
  receding. Above the board float giant bold numerals "+16 pts SWE-Bench" and
  "60% fewer tokens" in chrome typography. Background: Azure datacenter skyline
  in soft cyan-blue gradient with circuit-board overlay. Style: cinematic
  editorial, dramatic side-lighting, photoreal materials, ultra-high contrast so
  numbers + brand logos remain legible at 200px thumbnail. 1:1 aspect. No human
  faces — only chess pieces and logos.
image: images/26-06-09-0604-01-microsoft-mai-models-build-2026-openai-decoupling.png
---

# Microsoft ปล่อย MAI 7 รุ่นที่ Build 2026 — เริ่มปลด OpenAI จาก Copilot stack จริงจัง

## TL;DR
- 2 มิ.ย. Microsoft เปิด MAI 7 รุ่นที่ Build 2026 นำโดย **MAI-Code-1-Flash** (5B active params, GA ใน GitHub Copilot ทันที) และ **MAI-Thinking-1** (35B active, 256K context)
- MAI-Code-1-Flash claim +16 จุดเหนือ Claude Haiku 4.5 บน SWE-Bench Pro (51.2% vs 35.2%) และใช้โทเค็นน้อยลง 60% บน SWE-Bench Verified — ราคา $0.75/$4.50 ต่อล้านโทเค็น ถูกกว่า Haiku
- Strategic message ชัด — Microsoft ไม่ได้แทน OpenAI แต่ "เพิ่ม leverage" ในการต่อรอง compute cost ขณะให้ลูกค้า enterprise อีก option ที่ data ไม่ออกจาก Azure tenant

## เกิดอะไรขึ้น

วันที่ 2 มิ.ย. ที่ Build 2026 ใน San Francisco, Mustafa Suleyman ขึ้น keynote เปิด MAI family 7 รุ่นพร้อมกัน — เป็นการ ship in-house model ที่ใหญ่ที่สุดของ Microsoft ตั้งแต่ก่อตั้ง Microsoft AI division หัวหอกของ family นี้คือ **MAI-Code-1-Flash** — coding model 5 billion active parameters ที่ launch GA ใน GitHub Copilot ทันที — และ **MAI-Thinking-1** reasoning model 35B active parameters, 256K context window ที่ Microsoft claim เทียบเท่า Claude Sonnet 4.6 บน internal raters

ตัวเลขที่ Microsoft โชว์ตรงๆ: MAI-Code-1-Flash ชนะ Claude Haiku 4.5 บน SWE-Bench Pro ที่ **51.2% vs 35.2%** (+16 จุด) และทำคะแนน 85.8% บน Microsoft adversarial coding benchmark ของตัวเอง ที่สำคัญกว่า benchmark คือ efficiency — model นี้ solve harder problems ด้วยโทเค็นน้อยลง **60%** บน SWE-Bench Verified ราคา GitHub Copilot list ที่ $0.75 input / $4.50 output ต่อล้านโทเค็น — ถูกกว่า Haiku 4.5 ที่เป็น tier เดียวกัน

MAI-Thinking-1 ทำ 97% บน AIME 25 และ 53% บน SWE-Bench Pro — Microsoft positioning ว่าเป็น Copilot-native reasoning model ที่รัน on Azure infrastructure ของตัวเอง ไม่ต้องผ่าน OpenAI API ทั้งสองรุ่นเข้า GitHub Copilot Pro+, Business, Enterprise ทันทีพร้อม Microsoft 365 Copilot routing layer ที่ Microsoft เพิ่งเปิดเมื่อ Build — Copilot ตอนนี้ route request ระหว่าง GPT, Claude, และ MAI ตาม cost/latency/quality profile โดย admin ตั้งค่าได้

Microsoft ไม่ได้บอกตรงๆ ว่าจะ replace OpenAI — แต่ message จาก Suleyman keynote ใช้คำว่า "self-sufficiency" และเน้นว่า MAI รันบน Azure ของตัวเองโดยไม่ต้องจ่ายค่า inference ออกข้างนอก analysts ที่ CNBC สัมภาษณ์ตี dot ตรงเป๊ะ — Microsoft "now has leverage to negotiate compute costs" กับ OpenAI และทำให้ลูกค้า enterprise มี option ที่ data ไม่หลุดออกจาก managed tenant

## ทำไมสำคัญ

Microsoft ลงทุน OpenAI ~$14B ตั้งแต่ 2019 และ OpenAI ก็เป็น default model หลังบ้านของ Copilot, GitHub Copilot, Azure OpenAI Service มาตลอด — ตอนนี้ Microsoft กำลัง **build out exit ramp** ในเชิงเทคนิคและเชิง commercial พร้อมกัน MAI-Code-1-Flash เข้า GitHub Copilot ในวันเดียวกับ launch ไม่ใช่ภายหลัง 6 เดือน เป็น tell ว่า Microsoft จะกด traffic ของ Copilot ให้วิ่งผ่าน MAI ในส่วนที่ทำได้ทันที — ทุก request ที่ route ไป MAI คือ revenue ที่ไม่ต้องส่งให้ OpenAI

ที่น่าสนใจกว่า benchmark คือ **60% fewer tokens** บน SWE-Bench Verified — เพราะ Microsoft จ่ายค่า inference เป็น cost จริงในงบ Azure ทุก token ที่ประหยัดได้จาก MAI = margin ที่กลับเข้า P&L ของ Microsoft AI ทั้งหมด ในขณะที่ token ที่วิ่งผ่าน OpenAI = COGS ที่ส่งออกไป สำหรับ business ที่ token spend ของ Copilot สูงในระดับ billion ต่อปี การ shift 30–50% ของ workload ไป MAI คือ margin swing เป็นพันล้านเหรียญต่อปี

Move นี้ตอบ pattern ที่เห็นทั่วอุตสาหกรรม — Amazon ทำกับ Trainium + Nova, Google ทำกับ Gemini + TPU, ตอนนี้ Microsoft ทำกับ MAI + Azure — **hyperscaler ทุกรายต้องการ vertical stack ของตัวเอง** ใครยังพึ่ง model lab ภายนอกอย่างเดียวจะถูก margin compress จาก inference layer ทันที สิ่งที่ต่างคือ Microsoft ไม่ได้ฆ่า OpenAI relationship — ใช้ routing layer ที่บอกว่า "เราจะ route ไปอันดีที่สุดในแต่ละ task" ซึ่ง implicit คือ MAI ในกรณีที่ economics ดีกว่า

## มุม OpenBridge

Routing layer ของ Microsoft Copilot คือ pattern ที่ enterprise customer ของ OpenBridge จะ demand ในอีก 6–12 เดือน — "ขอ route prompt ระหว่าง Claude, GPT, MAI, Gemini โดยอัตโนมัติตาม cost/latency/policy" ถ้า OpenBridge build **model-agnostic routing + observability layer** เป็น first-class feature ก็จะเป็น tier ที่ลูกค้าจ่ายเพิ่ม ไม่ใช่แค่ integration tool ธรรมดา positioning ที่ใช่คือ "OpenBridge ทำให้ workflow ของคุณ swap model ระหว่างวิ่งได้โดยไม่ต้อง redeploy"

Token economics ที่ MAI-Code-1-Flash ใช้น้อยลง 60% เป็น signal ว่า **ราคา inference จะลงต่อเนื่อง** workflow ที่วันนี้ "แพงเกินทำ" จะ break-even ภายใน 12 เดือน OpenBridge ควร design billing model ที่ assume ราคา inference ลง 2–3 เท่าใน 12 เดือน และ price product ตาม value ที่ส่งให้ลูกค้า ไม่ใช่ตาม token markup เพราะ markup margin จะหายไปเร็วมาก

## Sources
- [Microsoft unveils new AI models to lessen reliance on OpenAI — CNBC](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [Building a hill-climbing machine: Launching seven new MAI models — Microsoft AI](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)
- [Introducing MAI-Code-1-Flash — Microsoft AI](https://microsoft.ai/news/introducingmai-code-1-flash/)
- [MAI-Code-1-Flash is now available for GitHub Copilot — GitHub Changelog](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/)
- [Microsoft launches seven in-house AI models to cut developer costs — Windows Central](https://www.windowscentral.com/software-apps/microsoft-launches-seven-in-house-ai-models-to-cut-developer-costs-and-reduce-reliance-on-openai)
- [Microsoft Build 2026: MAI keynote transcript — Microsoft AI](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/)

---

## Audio script
สวัสดีครับ Yoh เช้านี้ข่าวใหญ่จาก Microsoft Build 2026 — Mustafa Suleyman ขึ้น keynote เปิด MAI 7 รุ่นพร้อมกัน เป็นการ ship in-house model ที่ใหญ่ที่สุดของ Microsoft ตั้งแต่ตั้ง Microsoft AI division ตัวหัวหอกคือ MAI-Code-1-Flash โมเดล coding 5 พันล้าน active parameters ที่เข้า GitHub Copilot GA ในวันเดียวกัน และ MAI-Thinking-1 reasoning model 35 พันล้าน active 256K context ตัวเลขที่ Microsoft โชว์คือ MAI-Code-1-Flash ชนะ Claude Haiku 4.5 บน SWE-Bench Pro ที่ 51.2 vs 35.2 บวก 16 จุด และใช้โทเค็นน้อยลง 60% บน SWE-Bench Verified ราคา $0.75 input $4.50 output ต่อล้านโทเค็น ถูกกว่า Haiku 4.5 message ที่ Microsoft ส่งคือคำว่า self-sufficiency Suleyman ไม่ได้บอกตรงๆ ว่าจะ replace OpenAI แต่ analyst ที่ CNBC พูดว่า Microsoft ตอนนี้มี leverage ต่อรอง compute cost กับ OpenAI ได้แล้ว และมี option ที่ data ไม่หลุดออกจาก Azure tenant สำหรับลูกค้า enterprise สิ่งที่ตัด dot คือ 60% fewer tokens — Microsoft จ่ายค่า inference เป็น cost จริงในงบ Azure ทุก token ที่ประหยัดได้ คือ margin ที่กลับเข้า P&L ส่วน token ที่วิ่งผ่าน OpenAI คือ COGS ที่ส่งออกไป ถ้า Copilot shift 30 ถึง 50% ของ workload มา MAI margin swing คือพันล้านเหรียญต่อปี สำหรับ OpenBridge มุมที่ต้อง take away คือ Copilot routing layer ระหว่าง Claude GPT MAI Gemini จะเป็น feature ที่ลูกค้า enterprise demand ในอีก 6 ถึง 12 เดือน ถ้า OpenBridge build model agnostic routing plus observability เป็น first class feature นี่คือ tier ที่ลูกค้าจ่ายเพิ่ม positioning ที่ใช่คือ swap model ระหว่างวิ่งได้โดยไม่ต้อง redeploy และต้อง price product ตาม value ไม่ใช่ตาม token markup เพราะราคา inference จะลงเร็วมากครับ
