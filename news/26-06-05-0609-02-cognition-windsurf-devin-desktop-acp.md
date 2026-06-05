---
date: 2026-06-05
slug: cognition-windsurf-devin-desktop-acp
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A dramatic editorial illustration of a sleek dark IDE window labeled
  "DEVIN DESKTOP" in bold white letters at the top center, with a glowing
  blue Kanban board inside showing three columns labeled "LOCAL", "CLOUD",
  and "ACP AGENTS". A faded ghost of the old Windsurf logo dissolves into
  pixels on the left edge while a bright Devin logo rises on the right.
  Floating chips around the IDE labeled "CODEX", "CLAUDE", "OPENCODE"
  connect via glowing protocol lines to the center. Style: cinematic
  editorial illustration, deep navy background, neon cyan and warm orange
  highlights, isometric composition, high contrast, text legible at 200px
  thumbnail. No real human faces.
image: images/26-06-05-0609-02-cognition-windsurf-devin-desktop-acp.png
---

# Cognition ฆ่าแบรนด์ Windsurf — relaunch เป็น Devin Desktop พร้อม ACP เปิดทาง agent ของใครก็เข้ามาได้

## TL;DR
- 2 มิ.ย. Cognition ปิดแบรนด์ Windsurf — relaunch เป็น Devin Desktop, IDE แรกที่รองรับ Agent Client Protocol (ACP) ตั้งแต่วัน 1
- Mercedes-Benz บีบโปรเจกต์ modernize legacy 8 เดือนเหลือ 8 วัน, Itaú (บราซิล) ใช้ Devin auto-fix security vuln 70%
- Devin Local เขียนใหม่ใน Rust ลด token usage 30%, รองรับ subagents — รองรับ Codex, Claude Agent, OpenCode ผ่าน ACP

## เกิดอะไรขึ้น

วันที่ 2 มิถุนายน Cognition AI ประกาศปิดแบรนด์ Windsurf อย่างเป็นทางการ (ที่เพิ่งซื้อมาเมื่อต้นปี) แล้ว rebrand เป็น "Devin Desktop" — IDE ที่ build บน codebase Windsurf เดิม แต่เปลี่ยนตัวเองให้กลายเป็น "agent command center" สำหรับ developer การประกาศนี้ไม่ใช่แค่เปลี่ยนชื่อ — มันคือการยอมรับว่า thesis เดิม "IDE-first AI assistant" ถูกแทนที่ด้วย "agent-first IDE" — และ Cognition กำลัง force ทั้งตลาดไปทางนั้น

ฟีเจอร์ที่เป็น headline คือ ACP — Agent Client Protocol — open-source protocol ที่ Devin Desktop รองรับตั้งแต่ launch ผลคือ user สามารถสลับ run Codex, Claude Agent, OpenCode หรือ agent ของใครก็ได้ใน editor เดียวกัน นี่เป็นครั้งแรกที่ IDE ใหญ่ ๆ ยอมเปิด protocol ระดับ agent (เทียบกับ MCP ที่เน้น tools/data) — แปลว่า Cognition ยอมเสียโอกาส lock-in user ในระยะสั้น เพื่อเป็น default platform layer ในระยะยาว Agent Command Center ใหม่ใช้ Kanban view เห็น local + cloud agents ทุกตัวพร้อมกัน, มี "Spaces" สำหรับ share context ระหว่าง agent (PRs + files + sessions)

ด้าน local agent — Cognition rewrite Cascade ใหม่หมดเป็น Rust ตั้งชื่อว่า Devin Local อ้างว่า token-efficient เพิ่ม 30% และรองรับ subagents (pattern เดียวกับ Claude Code dynamic workflows) — user ที่อยู่ Windsurf เดิมจะได้ update OTA อัตโนมัติ, Cascade legacy ยังใช้ได้ถึง 1 ก.ค. ก่อนถูกเลิก

ตัวเลข enterprise ที่ Cognition โชว์เป็น proof point ของ rebrand: usage ของ Devin โต 10 เท่าตั้งแต่มกราคม 2026 และโต ~50% MoM ต่อเนื่อง 6 เดือน Mercedes-Benz รายงานว่าใช้ Devin บีบ legacy modernization project ที่เคยประเมิน 8 เดือนเหลือ 8 วัน Itaú Unibanco (ธนาคารใหญ่สุดของบราซิล) บอกว่า Devin auto-fix security vulnerabilities 70% แล้ว — ลูกค้ารายอื่น: Goldman Sachs, Citi, Dell, Santander, Palantir, NASA, US Army & Navy

## ทำไมสำคัญ

มีสามชั้นที่ต้องเข้าใจ ชั้นแรก — Cognition เพิ่งซื้อ Windsurf เมื่อต้นปีในดีล $1B หลัง Google "เกือบ" จะซื้อ — แล้วฆ่าแบรนด์ภายใน 5-6 เดือน ปกติ acquirer ที่จ่ายแพงขนาดนี้จะรักษาแบรนด์ไว้อย่างน้อย 1-2 ปี การที่ Cognition กล้าฆ่าแบรนด์เร็วขนาดนี้บอกว่าเขาเชื่อว่า "Devin" คือ brand equity จริง และ Windsurf user base ก็ migrate ได้ — ถ้าคิดผิดจะเสีย user หลักล้าน

ชั้นสอง — ACP เป็น move เชิงกลยุทธ์ที่น่าสนใจมาก เพราะมันคือ "embrace and extend" สำหรับตลาด IDE ปกติบริษัทที่อยู่อันดับ 1-2 จะปิด ecosystem ของตัวเอง (Cursor ทำแบบนั้น) แต่ Cognition เลือก open standard เพื่อสู้กับ Cursor (ยังอันดับ 1 ด้วย $2B ARR + SpaceX option $60B) ผลคือ developer ที่ใช้ Codex หรือ Claude Code สามารถมาใช้ Devin Desktop เป็น "shell" ได้โดยไม่ต้องทิ้ง agent หลัก — แปลว่า Cognition จะกลายเป็น aggregation layer แทนที่จะเป็น agent layer ตรง ๆ

ชั้นสาม — pattern เริ่มชัดเจน: protocol war ของปี 2026 ไม่ใช่แค่ MCP สำหรับ tools/data อีกต่อไป มี ACP (agent-to-IDE), A2A (agent-to-agent ของ Google), AGNTCY (Cisco/IBM) เพิ่มเข้ามา OpenBridge ที่ build บน MCP อย่างเดียวต้องเริ่ม map landscape ของทั้ง 4 protocol นี้ก่อนที่ลูกค้าจะถามว่า "support ACP มั้ย"

## มุม OpenBridge

มุมที่ตรงสุดสำหรับ OpenBridge: ACP คือ protocol ระดับ agent ที่ใกล้กับสิ่งที่ OpenBridge กำลังทำที่สุด — agent ที่ live ใน workflow ของลูกค้า แล้วต้องคุยกับ agent อื่น คำถามที่ต้อง decide ในสัปดาห์นี้: เราจะ adopt ACP เพื่อเป็น "OpenBridge-compatible agent server" ที่ IDE ใด ๆ ก็ต่อเข้ามาได้ ไหม? ถ้าใช่ — เราขายเป็น "ลูกค้าใช้ Devin Desktop / Cursor / VS Code ก็ได้ แต่ workflow logic อยู่ใน OpenBridge" ถ้าไม่ทำ — เสี่ยงโดน positioned เป็น proprietary platform ที่ developer team ปฏิเสธเพราะ lock-in

ที่ติดใจอีกอย่าง: Mercedes-Benz 8 เดือน→8 วัน เป็น case study ที่ enterprise sales ของเราเอาไปใช้ได้ตรง — แต่ต้องระวัง claim ของ Cognition เพราะยังไม่มี third-party verification ในการนำเสนอลูกค้า OpenBridge ควรใช้ pattern "Cognition อ้างว่า..." ตามด้วย point ของเราว่า "OpenBridge ช่วยเชื่อม Devin/Claude Code เข้ากับ system จริงของคุณ" — sell integration layer ไม่ใช่ agent

## Sources
- [Windsurf is now Devin Desktop](https://devin.ai/blog/windsurf-is-now-devin-desktop/)
- [Cognition launches Devin Desktop, an agent-neutral IDE built on Windsurf to manage local and cloud agents](https://digg.com/ai/4dcuzcpo)
- [Devin Desktop FAQ](https://docs.devin.ai/desktop/devin-desktop-faq)
- [Windsurf Is Now Devin Desktop: Devin Local, ACP, and What the Rebrand Actually Changes](https://chatforest.com/builders-log/windsurf-devin-desktop-rebrand-devin-local-acp-builder-guide/)
- [AI Coding Agents: Cognition's $26B Raise Bets Agent-First Architecture Beats IDE Tools](https://www.techtimes.com/articles/317354/20260529/ai-coding-agents-cognitions-26b-raise-bets-agent-first-architecture-beats-ide-tools.htm)

---

## Audio script
ข่าวที่สองวันนี้เป็นเรื่อง agentic AI ของจริงครับ Cognition AI เจ้าของ Devin ตัดสินใจปิดแบรนด์ Windsurf ที่เพิ่งซื้อมาแค่ 5-6 เดือนก่อนในดีล 1 พันล้านดอลลาร์ แล้วเปลี่ยนชื่อ IDE ใหม่เป็น Devin Desktop ฟีเจอร์ที่เป็น headline คือ Agent Client Protocol หรือ ACP — protocol แบบ open-source ที่เปิดให้ agent ของใครก็เข้ามารันใน IDE นี้ได้ ทั้ง Codex, Claude Agent, OpenCode user สลับใช้ได้อิสระ นี่เป็นครั้งแรกที่ IDE ใหญ่ยอมเปิด protocol ระดับ agent — Cognition ยอมเสีย lock-in ระยะสั้น เพื่อเป็น default platform ระยะยาว ตัวเลขที่น่าสนใจสุดคือ Mercedes-Benz บีบ project modernize ระบบเก่า 8 เดือนเหลือ 8 วัน Itaú Unibanco ของบราซิล ใช้ Devin auto-fix security vulnerability ได้ถึง 70% มีลูกค้าระดับ Goldman, Citi, Dell, NASA และกองทัพสหรัฐใช้แล้ว Devin Local รุ่นใหม่เขียนใหม่ด้วยภาษา Rust ลด token ลง 30% รองรับ subagents สำหรับ OpenBridge มุมที่ต้องคิดคือ ACP ใกล้กับสิ่งที่เราทำที่สุด เราจะ adopt มั้ย ถ้า adopt เราขายเป็น OpenBridge-compatible agent server ที่ IDE ใดก็ตามต่อเข้ามาได้ ถ้าไม่ทำ เสี่ยงโดนมองเป็น proprietary platform ที่ developer team ปฏิเสธ
