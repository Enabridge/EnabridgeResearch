---
date: 2026-05-27
slug: anthropic-glasswing-mythos-10k-vulnerabilities
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  A towering magnifying glass held by a robotic arm scans a massive wall of
  glowing source code, revealing cracks and fractures that pulse red — each
  crack labeled with a tiny "0-DAY" tag. The number "10,000+" floats above
  in bold white text against a dark background. Below the wall, a long queue
  of small patch icons (band-aids, wrenches) stretches into the distance,
  only a few reaching the wall while the rest wait. The Anthropic logo glows
  faintly on the robotic arm. Style: cyberpunk editorial illustration,
  dramatic lighting, high contrast neon reds and blues on dark background,
  isometric perspective, legible at 200px thumbnail. No human faces.
image: images/26-05-27-0604-01-anthropic-glasswing-mythos-10k-vulnerabilities.png
---

# Claude Mythos พบช่องโหว่ 10,000+ จุดในเดือนเดียว — แต่แพตช์ตามไม่ทัน

## TL;DR
- Project Glasswing ของ Anthropic ใช้ Claude Mythos Preview สแกนซอฟต์แวร์สำคัญ พบช่องโหว่ high/critical severity กว่า **10,000 จุด** ภายในเดือนเดียว
- จาก 1,000 open-source projects ที่สแกน พบ 6,202 ช่องโหว่ แต่แพตช์แล้วเพียง **97 จุด** — maintainer บางรายขอให้ Anthropic ชะลอการรายงาน
- Signal ชัด: AI หาช่องโหว่ได้เร็วกว่ามนุษย์แพตช์ — cybersecurity กำลังเปลี่ยนจาก "หาไม่เจอ" เป็น "เจอแต่แก้ไม่ทัน"

## เกิดอะไรขึ้น

Anthropic เผยอัปเดต Project Glasswing เมื่อสัปดาห์ที่ผ่านมา (22–26 พ.ค.) ตัวเลขน่าตกใจ: Claude Mythos Preview — โมเดลที่ Anthropic ไม่เปิดให้ใช้ทั่วไปเพราะกังวลเรื่อง dual-use — สแกน codebase ของซอฟต์แวร์ระดับ critical infrastructure แล้วพบช่องโหว่ high-to-critical severity มากกว่า 10,000 จุดภายในเดือนเดียว รวมถึงบั๊กอายุ 27 ปีใน OpenBSD และบั๊กอายุ 16 ปีใน FFmpeg ที่ไม่เคยมีใครพบมาก่อน

ตัวเลขจาก Anthropic เอง: สแกน 1,000 open-source projects พบ 6,202 ช่องโหว่ high/critical จาก 23,019 ที่ตรวจเจอทั้งหมด ยืนยันเป็น true positive แล้ว 1,726 จุด ในจำนวนนี้ 1,094 จุดเป็น high/critical severity จริง แต่ที่แพตช์แล้ว? เพียง 97 จุด

partner ที่เข้าถึง Mythos Preview ตอนนี้คือยักษ์ใหญ่ด้าน security ทั้งนั้น — AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks การที่ Anthropic ไม่ปล่อยโมเดลนี้ให้สาธารณะ แต่เลือก "กำแพง trust" ผ่าน partner program เป็นการยอมรับว่าโมเดลนี้มีพลังทำลายสูงพอ ๆ กับพลังป้องกัน

ปัญหาใหญ่ที่สุดไม่ใช่การหาช่องโหว่ แต่คือการแพตช์ Help Net Security รายงานว่าเฉลี่ยแล้วการแพตช์บั๊ก high/critical ที่ Mythos พบใช้เวลาสองสัปดาห์ open-source maintainer บางรายถึงกับขอให้ Anthropic ชะลอการ disclose เพราะรับ report ไม่ไหว — เป็นปรากฏการณ์ "vulnerability flood" ที่ไม่เคยเกิดขึ้นมาก่อนในประวัติศาสตร์ cybersecurity

## ทำไมสำคัญ

นี่คือจุดเปลี่ยนที่ cybersecurity landscape พลิกจาก "offense-defense parity" ไปเป็น "AI-driven asymmetry" — AI หาช่องโหว่ได้เร็วกว่ามนุษย์แพตช์หลายเท่า ซึ่งหมายความว่าถ้า attacker ได้โมเดลระดับเดียวกัน ช่องโหว่ zero-day จะกลายเป็นสินค้าราคาถูก ไม่ใช่ของหายากอีกต่อไป

อัตราแพตช์ 97 จาก 1,094 (ไม่ถึง 9%) ภายในเดือนเดียว ชี้ให้เห็นว่า bottleneck ของ cybersecurity ในยุค AI ไม่ใช่ "detection" อีกต่อไป แต่คือ "remediation" — การหา ง่าย แต่การแก้ ยังช้าเหมือนเดิม นี่คือโอกาสมหาศาลสำหรับ startup ที่ทำ automated patching, AI-assisted code fix, หรือ vulnerability prioritization

ในมุมกลับ สิ่งนี้ยิ่งตอกย้ำว่าทำไม Anthropic ถึงไม่ปล่อย Mythos ให้สาธารณะ — ถ้า attacker มี tool ระดับนี้ พร้อม codebase เดียวกัน ช่องโหว่ 10,000+ จุดก็คือ attack surface 10,000+ จุด ที่ยังไม่ได้แพตช์ การที่ NSA ออก MCP security guidance ในสัปดาห์เดียวกัน (ดู brief ถัดไป) ไม่ใช่เรื่องบังเอิญ

## มุม OpenBridge

สำหรับ OpenBridge สิ่งที่เห็นคือ **AI-driven security scanning กำลังกลายเป็น default workflow** ไม่ใช่ optional — enterprise จะต้อง integrate AI security scanning เข้ากับ CI/CD pipeline เป็นเรื่องปกติ ถ้า OpenBridge มี MCP connector สำหรับ security scanning tools (เช่น Snyk, SonarQube, Semgrep) ที่ทำงานร่วมกับ AI agent ได้ นี่คือ use case ที่ขายตัวเอง

อีกมุมคือ "vulnerability prioritization as a service" — เมื่อ AI พบช่องโหว่เป็นพัน enterprise ต้องการ tool ที่ช่วย prioritize ว่าอันไหนแก้ก่อน ซึ่งต้อง context จาก production environment, business impact, dependency graph — ข้อมูลเหล่านี้กระจายอยู่ตามระบบต่าง ๆ ที่ OpenBridge ถนัดเชื่อม

## Sources
- [Anthropic: Claude Mythos identified 10,000+ software flaws — Help Net Security](https://www.helpnetsecurity.com/2026/05/26/anthropic-project-glasswing-update/)
- [Project Glasswing: Securing critical software for the AI era — Anthropic](https://www.anthropic.com/glasswing)
- [Anthropic says Mythos has already found more than 10,000 vulnerabilities — Engadget](https://www.engadget.com/2180028/anthropic-claude-mythos-preview-project-glasswing-update/)
- [Project Glasswing: Anthropic says Claude found 10,000 critical software flaws in a month — Interesting Engineering](https://interestingengineering.com/ai-robotics/anthropic-project-glasswing-10000-software-vulnerabilities)
- [Anthropic's Project Glasswing Finds 'More Than 10,000' Critical Bugs, Expands To Additional Partners — Benzinga](https://www.benzinga.com/markets/private-markets/26/05/52759147/anthropics-project-glasswing-finds-more-than-10000-critical-bugs-expands-to-additional-pa)

---

## Audio script
สวัสดีครับ Yoh ข่าวแรกวันนี้เป็นเรื่องใหญ่ครับ Anthropic อัปเดต Project Glasswing โปรเจกต์ที่ใช้ Claude Mythos Preview ซึ่งเป็นโมเดลที่ไม่เปิดให้สาธารณะใช้ ไปสแกนหาช่องโหว่ในซอฟต์แวร์สำคัญ ตัวเลขน่าตกใจมากครับ พบช่องโหว่ระดับ high กับ critical กว่าหมื่นจุดภายในเดือนเดียว รวมถึงบั๊กอายุ 27 ปีใน OpenBSD ที่ไม่เคยมีใครเจอมาก่อน แต่ปัญหาคือแพตช์ตามไม่ทัน จากกว่าพันจุดที่ยืนยันแล้วว่าร้ายแรง แพตช์ไปได้แค่ 97 จุด open source maintainer บางรายขอให้ Anthropic ชะลอการรายงานเพราะรับไม่ไหว นี่คือจุดเปลี่ยนของ cybersecurity ครับ ปัญหาไม่ใช่หาไม่เจออีกต่อไป แต่คือเจอแล้วแก้ไม่ทัน ถ้า attacker ได้โมเดลระดับเดียวกัน zero day จะกลายเป็นสินค้าราคาถูก สำหรับ OpenBridge นี่คือ signal ว่า AI security scanning จะกลายเป็น default workflow ใน enterprise และ integration layer ที่เชื่อม scanning tools เข้ากับ CI/CD pipeline คือโอกาสที่ชัดเจนครับ
