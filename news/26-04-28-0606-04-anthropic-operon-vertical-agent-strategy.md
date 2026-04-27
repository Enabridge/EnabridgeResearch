---
date: 2026-04-28
slug: anthropic-operon-vertical-agent-strategy
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a stylized DNA helix being assembled by autonomous robotic arms in a clean laboratory environment, warm purple and emerald palette, minimal flat shapes, soft volumetric lighting, sense of careful precision, no text, no logos, no faces
image:
---

# Anthropic Operon — vertical agent ตัวแรก signals การ split ของตลาดที่ลึกกว่าที่ใครคิด

## TL;DR
- Anthropic กำลัง test "Operon" — Claude Desktop mode สำหรับ biology/computational science โดยเฉพาะ พบจาก code analysis ก่อน announce
- Features เฉพาะทาง: phylogenetic tree, CRISPR screen design, single-cell RNA analysis, protein language models — ไม่ใช่ general agent ที่ "พอใช้"
- Signal สำคัญกว่า product ตัวเดียว: Anthropic เลือก go vertical ไม่ใช่ horizontal — ทิศทางที่ OpenAI ยังลังเลอยู่

## เกิดอะไรขึ้น

Anthropic กำลัง dogfood internal feature ที่ชื่อ "Operon" — Claude Desktop mode พิเศษสำหรับงานวิจัย biology และ computational science โดยเฉพาะ ที่น่าสนใจคือมันถูก **discovered ก่อน announced** — TestingCatalog และ researcher คนอื่น ๆ ขุดเจอใน build ของ Claude Desktop ตั้งแต่กลางเมษายน 2026 ก่อนที่ Anthropic จะมี blog post อย่างเป็นทางการ

Operon ไม่ใช่ "Claude แต่งตัวเป็นนักชีววิทยา" — มันมี environment, tool, และ workflow ที่ specific มาก: รองรับ CRISPR screen design, single-cell RNA quality control & analysis, phylogenetic tree construction, protein language model integration, และ session/project management แบบที่นักวิจัยใช้จริง พร้อม Plan Mode (ทำตาม approval แต่ละ step) และ Auto Mode (autonomous ภายใต้ framework ที่นักวิจัยกำหนด) — เห็นชัดว่าออกแบบโดยปรึกษากับนักวิจัยจริง

Operon ต่อยอดจาก Anthropic's "AI for Science" program ที่ตั้งกลางปี 2025, ตามด้วย Claude for Life Sciences ปลายปี 2025 ที่มี connector ไป PubMed, Benchling, 10x Genomics และล่าสุด partnership กับ Owkin ที่เพิ่ง launch Pathology Explorer agent — เป็น sequence ที่บอกว่า Anthropic ลงทุน vertical biology อย่างเป็นระบบ ไม่ใช่ side project

ที่ยังไม่ชัดคือ pricing model — Operon จะอยู่ใน Claude Pro/Max หรือเป็น tier แยก, รวมถึง model ใต้ engine ก็ยังไม่ confirm (น่าจะเป็น Claude Opus 4.7 หรือ specialized variant)

## ทำไมสำคัญ

นี่คือ first concrete signal ว่า Anthropic เลือก strategy ต่างจาก OpenAI ชัดเจน — OpenAI พยายามเป็น "everything for everyone" (ChatGPT, Codex, Workspace Agents, Sora, Operator), ขณะที่ Anthropic กำลังเลือก beachhead ที่ specific แล้ว dominate (Claude Code สำหรับ engineering, Operon สำหรับ science, ก่อนหน้านี้คือ Claude for Enterprise สำหรับ regulated industries)

Pattern เทียบกับยุค SaaS: ตอน Salesforce ครอง CRM, NetSuite ครอง ERP — vertical specialist ชนะ horizontal ในตลาดที่ workflow เฉพาะทางสำคัญกว่า reach กว้าง วิทยาศาสตร์ชีวภาพคือตลาดแบบนั้น 100% — researcher ไม่อยาก prompt-engineer Claude ให้ทำ CRISPR ทุกครั้ง อยากเปิด Operon แล้วทำเลย

ข้อมูลทางการเงินเสริม signal นี้: Anthropic ARR แตะ $30B แล้ว, แซง OpenAI's $25B — และ growth driver หลักคือ Claude Code ($1B ARR ภายใน 6 เดือนหลัง GA) เป็น vertical product ตัวแรก ถ้า Operon ตามรอย Claude Code ได้ — biology/biotech ตลาด US เพียวอย่างเดียวก็ใหญ่หลายพันล้านดอลลาร์ และ TAM โตเร็วกว่า general AI assistant

Implication ระยะกลาง: Anthropic จะปล่อย vertical product เพิ่มอีก 2–3 ตัวภายใน 12 เดือน — น่าจับตา legal (แข่ง Harvey), financial services (แข่ง Hebbia), healthcare clinical decision support และ OpenAI จะถูกบีบให้ตามมา หรือ stay horizontal แล้วเสียส่วนแบ่งใน high-value verticals

## มุม OpenBridge

ไม่ direct เกี่ยว biology — แต่ adjacent insight สำคัญ: pattern "Anthropic dogfood-then-announce" คือ playbook ที่ company สมัยใหม่ใช้ — build silently, leak intentionally, gather feedback ก่อน formal launch ลด PR risk และเพิ่ม community advocacy ตั้งแต่ก่อน GA OpenBridge ควรพิจารณา approach นี้: build feature ที่ visible ใน production (ไม่ hide flag) ให้ early users discover/talk เอง, แทนที่จะรอ formal announcement

ที่สำคัญกว่าคือ vertical strategy lesson — OpenBridge ก็ควรเลือก vertical beachhead ที่ specific ก่อน expand horizontal ตัวเลือกที่ฟิตที่สุดสำหรับเราอาจเป็น: integration agent สำหรับ mid-market SaaS company ในเอเชียตะวันออกเฉียงใต้ (segment ที่ Workato/Boomi ละเลย และยังไม่มี vendor ที่ understand context ภาษา/ระเบียบ regional ดีพอ) จุดยืน "vertical agent for SEA B2B integration" ฟังดูแคบ แต่นั่นแหละคือจุดแข็ง — ตามแบบ Operon ที่แคบแล้ว dominate

## Sources
- [Claude Operon Leak Reveals Anthropic's Biology AI (Geeky Gadgets)](https://www.geeky-gadgets.com/claude-operon-leak/)
- [Anthropic tests Claude Operon for scientific research in biology (TestingCatalog)](https://www.testingcatalog.com/anthropic-tests-claude-operon-for-scientific-research-in-biology/)
- [Owkin's Pathology Explorer launches with Anthropic's Claude (Owkin)](https://www.owkin.com/newsfeed/owkins-specialized-biological-ai-agent-pathology-explorer-launches-with-anthropics-claude-for-healthcare-and-life-sciences)
- [Anthropic ARR run-rate revenue surpasses $30B (ARR Club)](https://www.arr.club/anthropic/anthropic-arr-run-rate-revenue-surpasses-30b-up-from-9b-at-end-of-2025)

---

## Audio script
ข่าวสุดท้าย Anthropic กำลัง dogfood feature ใหม่ชื่อ Operon เป็น Claude Desktop mode เฉพาะสำหรับงานวิจัย biology และ computational science เจอจาก code analysis ก่อน announce อย่างเป็นทางการด้วย Operon ไม่ใช่ Claude แต่งตัวเป็นนักชีววิทยานะครับ มี tool และ workflow specific มาก รองรับ CRISPR screen design, single-cell RNA analysis, phylogenetic tree, protein language model มี Plan Mode กับ Auto Mode ออกแบบโดยปรึกษากับนักวิจัยจริง สิ่งที่ผมว่าสำคัญกว่า product ตัวเดียวคือ signal ว่า Anthropic เลือก strategy ต่างจาก OpenAI ชัดเจนแล้ว OpenAI พยายามเป็น everything for everyone ChatGPT Codex Workspace Agents Sora Operator แต่ Anthropic เลือก beachhead ที่ specific แล้ว dominate Claude Code สำหรับ engineering, Operon สำหรับ science, Claude for Enterprise สำหรับ regulated industries เทียบกับยุค SaaS เลยครับ ตอน Salesforce ครอง CRM, NetSuite ครอง ERP, vertical specialist ชนะ horizontal ในตลาดที่ workflow เฉพาะทางสำคัญกว่า reach กว้าง ตัวเลขเสริม signal นี้คือ Anthropic ARR แตะ 30 พันล้านแล้ว แซง OpenAI ที่ 25 และ growth driver หลักคือ Claude Code ที่เป็น vertical product ตัวแรก สำหรับ OpenBridge lesson ตรงนี้คือ เราก็ควรเลือก vertical beachhead specific ก่อน อย่าพยายามเป็น horizontal ผมว่า integration agent สำหรับ mid-market SaaS ในเอเชียตะวันออกเฉียงใต้ น่าจะใช่ครับ Workato Boomi ละเลยและไม่ understand context regional ดีพอ
