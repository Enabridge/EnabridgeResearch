---
date: 2026-06-13
slug: claude-fable-5-mythos-public-release
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial hero illustration of a glowing silver model trophy labeled "FABLE 5"
  standing on a dark obsidian podium, with a translucent "95% SWE-BENCH VERIFIED"
  ribbon arcing above it like a comet trail, and a smaller shadowed "MYTHOS"
  silhouette receding into a vault doorway behind it suggesting the restricted
  parent model. Composition is centered 1:1, dramatic chiaroscuro lighting from
  upper-left, deep indigo background with warm gold rim light on the trophy,
  flat editorial style reminiscent of The Information cover art, big legible
  white-and-gold typography readable in a 200px thumbnail. No real human faces.
image: images/26-06-13-0603-01-claude-fable-5-mythos-public-release.png
---

# Anthropic เปิด Claude Fable 5 — Mythos-class รุ่นแรกที่ public ใช้ได้, ครอง 95% SWE-bench Verified

## TL;DR
- **9 มิ.ย.** Anthropic ปล่อย **Claude Fable 5** — รุ่น "**Mythos-class แรกที่ใช้กับ public ได้**" (Mythos = ทีม Glasswing cyberdefender ใช้อยู่แล้ว, ตอนนี้ derive ออกมาเป็น Fable 5 พร้อม safeguard)
- **95.0% SWE-bench Verified, 80.3% SWE-bench Pro** — top score ที่ Anthropic เคย ship, นำ Opus 4.8 (69.2%) ที่ฉันเองเป็น **+11 จุด** ใน Pro
- **Pricing $10/M input, $50/M output** — น้อยกว่าครึ่งของ Mythos Preview เดิม; ฟรีบน Pro/Max/Team plan ถึง **22 มิ.ย.**
- **Safeguard architecture**: ถ้า request เข้าโซน cyber/bio/chem/distillation → fall back ไป **Opus 4.8** อัตโนมัติ — แปลว่า "Mythos-grade score" จริง ๆ ใช้ได้แค่นอกโซนความเสี่ยง

## เกิดอะไรขึ้น

วันที่ 9 มิ.ย. Anthropic ประกาศ Claude Fable 5 พร้อมกับ Claude Mythos 5 — และเฟรมการเปิดตัวครั้งนี้เป็นจุดเปลี่ยน narrative ที่ทีมเคยรักษามาตลอดสามปี: **Mythos = restricted tier ที่เฉพาะคนใน Project Glasswing เห็น** กลายเป็น tier ที่ public ก็เข้าถึงได้แล้ว ผ่าน derivative ชื่อ Fable 5

จุดที่ทำให้ทีม research ทั่วโลกตื่นเช้านี้คือตัวเลข. Fable 5 ทำ **SWE-bench Verified ได้ 95.0%** — สูงสุดของ leaderboard ทุกค่ายจน Vellum กับ Morph LLM ที่ track score ทุก vendor ต้อง refresh chart; และบน **SWE-bench Pro** (benchmark agentic-coding ใหม่ที่ยากกว่า Verified) ทำได้ **80.3%** ทิ้ง Opus 4.8 ที่ยืน 69.2% — +11 จุด ใน benchmark ที่นักวิเคราะห์เคยมองว่า "saturated" แล้ว

ที่ทำให้เป็นข่าวเศรษฐกิจไม่ใช่ข่าว benchmark คือ **pricing**. Fable 5 ตั้งราคา $10 ต่อล้าน input token, $50 ต่อล้าน output — น้อยกว่าครึ่งของ Mythos Preview ที่ enterprise tier เคยจ่าย; และตั้งแต่ 9 ถึง 22 มิ.ย. รวมอยู่ใน Pro, Max, Team, seat-based Enterprise plan ฟรี — strategy ชัดว่าต้องการ **flood developer mindshare ก่อน Google ปล่อย Gemini 3.5 และ OpenAI ตอบโต้ GPT-5.5 Codex**

ปมที่ทำให้ benchmark ตัวเลขสวยต้องอ่านด้วยตาเหล่: Fable 5 ทำ score Mythos-class จริงเฉพาะ "outside safeguard zone." Anthropic บอกชัดว่า request ใด ๆ ที่ touch cybersecurity, biology, chemistry, model distillation → ถูก reject แล้ว fall back ไป **Opus 4.8** อัตโนมัติ. แปลว่า workflow agentic ที่เกี่ยวกับ security research, vulnerability triage, หรือแม้แต่ pentest tooling = ยังได้ Opus 4.8 ไม่ใช่ Fable 5

Simon Willison เขียน first impression ภายในไม่กี่ชั่วโมงว่า "feels meaningfully smarter on long-horizon agent tasks than Opus 4.8" — โดยเฉพาะ multi-file refactor และ test-driven debugging ที่ต้อง plan 30-50 step ติดกัน. นี่คือ signal ว่า **gap ระหว่าง code assistant (Copilot, Cursor) กับ autonomous coding agent (Devin, Codex) ปิดลงไปอีก** จากฝั่ง model layer

## ทำไมสำคัญ

นี่ไม่ใช่แค่ "Anthropic ship รุ่นใหม่." นี่คือ **Anthropic เปลี่ยน positioning ของ tier system** — จากเดิมที่ enterprise ต้องไป gate ของ Mythos ผ่าน Glasswing program (และจ่ายแพง) ตอนนี้ derivative ของน้ำหนักเดียวกันเปิดให้ public แล้ว แค่มี filter layer ครอบ. นั่นคือ message ทาง strategy ที่ **public Anthropic API จะไม่ใช่ tier รอง — มันคือ Mythos ที่ใส่ guardrail**

แต่ trade-off ที่ enterprise buyer ต้องคำนึงคือ **safeguard layer ทำให้ behavior model ไม่ predictable ในโซน adjacent**. Cybersecurity team ที่ใช้ Claude code agent triage CVE — request บางตัวจะ silently downgrade ไป Opus 4.8 กลางทาง โดย agent ไม่ได้แจ้ง deterministic. นั่นคือ **failure mode ใหม่ที่ MLOps team ยังไม่มี playbook** — และจะเป็น top complaint ของ Q3 ในกลุ่ม security tooling vendor

Pattern ที่เห็น: **Anthropic เริ่ม decouple "model capability" ออกจาก "model availability"**. แทนที่จะกัก capability ไว้กับ tier (Opus > Sonnet > Haiku), Anthropic เลือก ship capability เต็มไปกับ public แต่ใส่ guardrail conditional — model decision-tree เปลี่ยนจาก **"ใช้ tier ไหน"** เป็น **"request domain ไหน"**. นี่คือ template ที่ Google และ OpenAI น่าจะ copy เพราะมัน scale ได้กับ enterprise compliance ดีกว่า hard tier gating

ที่ต้องตามต่อ: **Anthropic Mythos 5 ที่ส่งให้ Glasswing partner** (cyberdefenders) มี safeguard ปลด — แปลว่ายังมี "model ที่ตอบ vuln research ตรง ๆ" อยู่ในมือคู่ค้ารัฐ. ระยะยาวนี่จะกลายเป็น issue ทาง public policy: ใครได้ unsafeguarded Mythos? Anthropic เป็นคน decide unilaterally หรือมี oversight? ตอนนี้ยังเป็น contract decision, แต่ถ้า Fable 5 prove ว่า "safe enough for public" ขณะที่ Mythos ปลด guard อยู่กับรัฐ — narrative นี้จะร้อนใน Q4

## มุม OpenBridge

**Action immediate ที่สุด:** ถ้า OpenBridge หรือลูกค้าใช้ Anthropic API บน production — switch evaluation pipeline ของ agent ใด ๆ ที่ทำ multi-step code generation มาลอง Fable 5 สัปดาห์นี้เลย ราคาถูกกว่าครึ่ง + score สูงกว่า = unfair-not-to-try. ทำ A/B กับ Opus 4.8 บน workload จริงสัก 100 case ก่อน 22 มิ.ย. (วันที่ราคา free trial หมด) — มี data ตัดสินใจไป commit Q3

**Positioning consideration:** OpenBridge ขาย integration platform ที่ workflow ส่วนใหญ่ไม่ touch โซน cyber/bio/chem — แปลว่า safeguard fallback แทบไม่ trigger บน use case ของลูกค้า SMB ไทย. นี่คือ **ของขวัญ pricing** ที่ทีม product ควร model ทันที: ถ้า cost ลง 50%, margin ขึ้นเท่าไร, หรือ pass-through ลูกค้าเพื่อ underprice competitor?

**เตือนสำหรับ product team:** อย่า hardcode model name "claude-fable-5" ใน production config — Anthropic prove แล้วว่า refresh tier เร็ว (Opus 4.7 → 4.8 → Fable 5 ใน 6 สัปดาห์); ใช้ alias หรือ routing layer ที่ swap ได้ runtime ไม่ต้อง redeploy

## Sources
- [Anthropic — Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [TechCrunch — Anthropic's Claude Fable 5 is a version of Mythos the public can access today](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)
- [Simon Willison — Initial impressions of Claude Fable 5](https://simonwillison.net/2026/Jun/9/claude-fable-5/)
- [Morph LLM — SWE-bench Pro Leaderboard: Claude Fable 5 leads at 80.3%](https://www.morphllm.com/swe-bench-pro)
- [Tom's Hardware — Claude Fable 5 brings Mythos to the masses](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-fable-5-brings-mythos-to-the-masses-anthropics-next-frontier-model-is-state-of-the-art-on-nearly-all-tested-benchmarks)

---

## Audio script
ข่าวใหญ่ที่สุดของสัปดาห์สำหรับ founder ที่ใช้ Anthropic. Claude Fable 5 ออกแล้วเมื่อ 9 มิ.ย. นี่คือรุ่นแรกของ Mythos-class ที่ public เข้าถึงได้. ก่อนหน้านี้ Mythos เป็น tier ลับที่เฉพาะทีม Glasswing ของ cyberdefender ใช้.

ตัวเลข benchmark สวยที่สุดเท่าที่ Anthropic เคย ship. SWE-bench Verified 95 percent. SWE-bench Pro 80.3 percent. นำ Opus 4.8 อยู่ 11 จุดเต็ม ๆ. Simon Willison เขียนภายในไม่กี่ชั่วโมงว่าเก่งขึ้นชัดเจนกับ task agentic ยาว ๆ 30-50 step ติดกัน.

ที่จริงจังกว่าคือ pricing. 10 ดอลลาร์ต่อล้าน input token. 50 ดอลลาร์ต่อล้าน output. น้อยกว่าครึ่งของ Mythos Preview เดิม. และฟรีบน Pro Max Team Enterprise plan ถึง 22 มิ.ย. strategy ชัดว่า Anthropic ต้องการ flood developer mindshare ก่อน Google ตอบ Gemini 3.5 และ OpenAI ตอบ GPT-5.5 Codex.

แต่ปมที่ต้องอ่านระหว่างบรรทัด. Fable 5 ทำ Mythos-class score จริงเฉพาะนอก safeguard zone. ถ้า request touch cybersecurity bio chem หรือ distillation. agent จะ silently fall back ไป Opus 4.8 อัตโนมัติ. นี่คือ failure mode ใหม่ที่ MLOps ยังไม่มี playbook. agent ไม่ได้บอกว่า downgrade แล้ว.

สำหรับ OpenBridge. workflow ส่วนใหญ่ของลูกค้า SMB ไทยไม่ touch โซนเสี่ยงพวกนี้. แปลว่า safeguard fallback แทบไม่ trigger. นี่คือของขวัญ pricing ที่ทีม product ต้อง model ทันที. ถ้า cost ลง 50 percent. margin ขึ้นเท่าไร. หรือ pass through ลูกค้าเพื่อ underprice competitor. และอย่า hardcode model name ใน production. ใช้ routing layer ที่ swap ได้ runtime. เพราะ Anthropic prove แล้วว่า refresh tier เร็วทุก 6 สัปดาห์.
