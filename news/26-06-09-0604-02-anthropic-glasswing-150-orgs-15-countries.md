---
date: 2026-06-09
slug: anthropic-glasswing-150-orgs-15-countries
topic: use-case
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial illustration of a translucent glass shield expanding outward over a
  stylized world map, with Anthropic orange-amber glow at the center. Inside
  the shield, a swarm of digital "vulnerability bug" icons (small red exclamation
  marks) are being captured. Bold floating numerals overlaid: "150 orgs", "15+
  countries", "10,000 flaws found". Sectors as small labeled icons orbit the
  shield — a power plant, water droplet, hospital cross, signal tower, chip.
  Style: cinematic editorial, isometric, warm-cool contrast, photoreal glass +
  metal materials, ultra-high contrast typography legible at 200px thumbnail.
  1:1 aspect. No human faces. Anthropic logo small on shield center.
image: images/26-06-09-0604-02-anthropic-glasswing-150-orgs-15-countries.png
---

# Anthropic ขยาย Project Glasswing เข้า 150 องค์กรใน 15+ ประเทศ — agentic security ขยับสู่ critical infrastructure

## TL;DR
- 2 มิ.ย. Anthropic ประกาศขยาย Project Glasswing — โครงการให้ Claude Mythos สแกน vulnerability ใน critical software — เปิดให้อีก **150 องค์กรใน 15+ ประเทศ** เข้าใช้
- ตั้งแต่เปิดโครงการ partners ค้นพบ **10,000+ flaw ระดับ high/critical**, Anthropic scan 1,000+ open-source projects ด้วย Mythos เอง flag 23,019 issue โดย 90% ของ 1,752 รายที่ตรวจซ้ำ confirm ว่าเป็นจริง
- New cohort ขยายเข้า **power, water, healthcare, communications, hardware** — sector ที่หายไปจาก initial cohort, รวม NATO, ENISA, Samsung, SK Telecom

## เกิดอะไรขึ้น

วันที่ 2 มิ.ย. 2026 Anthropic ประกาศ Project Glasswing expansion phase 2 — เพิ่ม **150 องค์กรพันธมิตร** ใน **15+ ประเทศ** ให้เข้าถึง Claude Mythos รุ่นพิเศษที่ optimize สำหรับ vulnerability discovery ใน source code ของ critical infrastructure software ในรอบแรก (เปิดตัว Mar 2026) Glasswing มีพาร์ทเนอร์ใหญ่อย่าง Apple, Nvidia, Microsoft, CrowdStrike, Palo Alto Networks — แต่ Anthropic ยอมรับว่า initial cohort "ไม่ครอบคลุม" sector ที่สำคัญที่สุด

phase 2 จึง add **power, water, healthcare, communications, hardware** เข้ามา — รวมถึงองค์กรอย่าง **Okta, Samsung, SK Hynix, SK Telecom, NATO, ENISA** (cybersecurity agency ของ EU) สิ่งที่ Anthropic ขายให้ partner เหล่านี้คือสิทธิ์ใช้ Mythos เพื่อ scan codebase ของตัวเอง + ของ open-source dependency ที่พึ่งพา — ก่อนที่ attacker จะเจอ vulnerability เหล่านั้น

ตัวเลขที่ Anthropic เปิดในวันเดียวกัน: Glasswing partners ค้นพบและรายงาน **vulnerability ระดับ high/critical 10,000+ รายการ** ตั้งแต่เปิดโครงการ; Anthropic เอง scan **1,000+ open-source projects** ด้วย Mythos flagging **23,019 potential vulnerabilities** เมื่อ sample 1,752 รายที่จัดเป็น high/critical มา manual review พบว่า **มากกว่า 90% confirmed ว่าเป็น vulnerability จริง** — false positive rate ต่ำกว่า 10% ในงาน vulnerability discovery เป็น signal ที่แรงมาก เพราะ classical SAST tool ส่วนใหญ่ทำ false positive ระดับ 30–50%

Anthropic ยังประกาศว่าจะ **share vulnerability-finding tool** กับ trusted security team — implication คือ Mythos ที่ตอนนี้ access ได้แค่ใน partner program จะค่อยๆ เปิดเป็น product สำหรับ security vendor ในอนาคต Helm ที่ขับโครงการนี้คือ Logan Graham (Frontier Red Team lead) — บอกใน TechCrunch ว่าเป้าเป็น "stay ahead of malicious actors" ในยุคที่ attacker เริ่มใช้ AI หา vulnerability เร็วกว่า defender

## ทำไมสำคัญ

ตัวเลข **90% confirmed-true rate** บน 1,752 รายที่ตรวจซ้ำเป็นจุดเปลี่ยน — เพราะ AI security tool ที่ผ่านมาไม่เคยทำ precision ระดับนี้ในงาน vulnerability discovery จริง classical SAST/DAST/SCA tool false positive สูงมากจนทีม security เลิกใช้ output โดยตรง ต้องมี human triage ทุก finding — ถ้า Mythos ทำได้ 90%+ จริง (Anthropic admit ว่าตัวเลขนี้มาจาก subsample, ยังไม่ใช่ population) ก็เปลี่ยน economics ของ security operation ทั้งอุตสาหกรรม

โครงการนี้ยังเป็น case ที่ชัดที่สุดว่า **agentic AI ทำงานเป็น "frontier red team" จริง** ไม่ใช่ค้นหาด้วย regex แล้ว flag — Mythos run autonomous workflow: read code → reason about attack surface → write PoC → verify exploit → report ทั้ง chain นี่คือ workload ที่เคย require senior security engineer หลายชั่วโมงต่อ finding — ตอนนี้ scale ได้ทั่ว 1,000 open-source project ใน batch เดียว ที่ Klarna โชว์ในงาน customer service ($60M saved + work ของ 853 employee) — Glasswing เป็น parallel ในงาน security ที่ economics ใหญ่กว่า

Sector expansion เข้า critical infrastructure (power, water, healthcare) ก็ส่ง message เชิง policy — Anthropic positioning ตัวเองเป็น "AI lab ที่ทำให้ critical software ปลอดภัยขึ้น" ก่อน regulator จะมาบังคับ pattern นี้ปกติคือ vendor ที่ proactive จะได้เป็น default vendor ของ regulator ที่ออก standard (ดู Microsoft กับ ISO 27001) — Anthropic กำลัง play book นี้กับ AI security

## มุม OpenBridge

Project Glasswing เป็น proof point ว่า **agentic AI ที่ทำงาน autonomous บน code/data ของลูกค้าโดยตรง** เป็น use case ที่ enterprise ยอมจ่าย — เพราะ vulnerability ก่อนคนอื่นเจอ = saving จาก breach หลายสิบล้านเหรียญ OpenBridge ไม่ได้ทำ security tool โดยตรง แต่ pattern ที่นำมาใช้ได้คือ "agent ที่วิ่งใน customer environment, ทำงาน autonomous, รายงาน finding กลับ" — same pattern, different domain เช่น integration health agent ที่ scan workflow ของลูกค้า แล้ว flag bottleneck/risk/inefficiency ก่อนเกิดปัญหา

อีกมุมที่สำคัญคือ **trust + permission model** ที่ Anthropic ใช้ — partner ต้อง qualify security requirements ก่อนได้สิทธิ์เข้าถึง Mythos OpenBridge ก็ควรมี tier ที่ "deep agent" เข้าถึงได้แค่ลูกค้าที่ผ่าน security review — เพราะ enterprise ที่ระมัดระวังจะรู้สึก safe กว่าถ้ารู้ว่า capability ระดับสูงไม่ได้ ship by default ต้อง enable manual

## Sources
- [Anthropic expands Mythos to 150 additional organizations in more than 15 countries — CNBC](https://www.cnbc.com/2026/06/02/anthropic-mythos-ai-project-glasswing.html)
- [Expanding Project Glasswing — Anthropic](https://www.anthropic.com/news/expanding-project-glasswing)
- [Anthropic scales Claude Mythos to critical infrastructure in 15+ countries — TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
- [Anthropic expanding access to Project Glasswing — CyberScoop](https://cyberscoop.com/anthropic-project-glasswing-expansion-critical-infrastructure-claude-mythos/)
- [Anthropic expands Project Glasswing to 150 organizations in more than 15 countries — Help Net Security](https://www.helpnetsecurity.com/2026/06/03/anthropic-project-glasswing-expansion/)
- [Project Glasswing: An initial update — Anthropic](https://www.anthropic.com/research/glasswing-initial-update)

---

## Audio script
สวัสดีครับ Yoh วันที่ 2 มิ.ย. Anthropic ประกาศ Project Glasswing phase 2 — ขยายเพิ่มอีก 150 องค์กรพันธมิตรใน 15 ประเทศ ให้เข้าถึง Claude Mythos รุ่นพิเศษที่ทำ vulnerability discovery ใน source code ของ critical infrastructure รอบนี้เพิ่ม sector ที่หายไปในรอบแรก คือ power water healthcare communications hardware รวมพาร์ทเนอร์ที่น่าสนใจอย่าง NATO ENISA Samsung SK Hynix SK Telecom Okta ตัวเลขที่ Anthropic เปิดแรงมาก partner ทั้งหมดเจอ vulnerability ระดับ high กับ critical รวมกัน 10,000 รายการตั้งแต่เปิดโครงการ Anthropic เอง scan open-source project มากกว่า 1,000 โครงการ flag potential vulnerability 23,019 รายการ ที่สำคัญที่สุดคือ confirm rate — sample 1,752 รายที่ manual review พบว่ามากกว่า 90% เป็น vulnerability จริง — false positive ต่ำกว่า 10% ในขณะที่ classical SAST tool ทำ false positive 30 ถึง 50% นี่คือจุดเปลี่ยนของ economics ใน security operation ทั้งอุตสาหกรรม pattern ที่เห็นคือ Mythos ทำงาน autonomous full chain — read code reason about attack surface write PoC verify exploit แล้วรายงาน เป็น workload ที่เคย require senior security engineer หลายชั่วโมงต่อ finding ตอนนี้ scale ได้ทั่ว 1,000 project ใน batch เดียว สำหรับ OpenBridge มี take away สองข้อ หนึ่ง agentic AI ที่ทำงาน autonomous บน data ของลูกค้าเป็น use case ที่ enterprise ยอมจ่ายแพง pattern เดียวกันใช้ใน integration health agent ที่ scan workflow ของลูกค้า แล้ว flag bottleneck หรือ risk ก่อนเกิดปัญหา สอง trust กับ permission model — Anthropic บังคับ partner ต้อง qualify security requirement ก่อนได้ access OpenBridge ก็ควรมี tier ที่ deep agent ไม่ ship by default ลูกค้า enterprise ที่ระมัดระวังจะรู้สึก safer ครับ
