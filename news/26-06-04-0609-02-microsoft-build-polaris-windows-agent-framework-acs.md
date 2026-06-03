---
date: 2026-06-04
slug: microsoft-build-polaris-windows-agent-framework-acs
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Hero illustration: a giant Windows logo at center, but reimagined as a glowing
  control panel with four switches labeled "POLARIS", "WAF v1.0", "ACS", "MULTI-AGENT".
  Behind it, a faint ghost-silhouette of the OpenAI logo dissolving into pixels —
  the visual metaphor of Microsoft cutting the cord. A bold headline strip across
  the top reads "BUILD 2026" in heavy sans-serif. Style: dark teal + electric blue
  + magenta accents, clean editorial tech illustration, high-contrast so all four
  switch labels read clearly at 200px thumbnail. Square 1:1, no real human faces.
image: images/26-06-04-0609-02-microsoft-build-polaris-windows-agent-framework-acs.png
---

# Microsoft Build 2026: ตัดสาย OpenAI ด้วย Polaris + เปลี่ยน Windows เป็น Agent Host

## TL;DR
- Microsoft เปิด Project Polaris — โมเดล coding ของตัวเองแทน GPT-4 ใน GitHub Copilot, default ส.ค. 2026
- Windows Agent Framework v1.0 ออก MIT license พร้อม Cross-Agent Communication Bus + Memory Service
- เสนอ Agent Control Specification (ACS) — open standard governance policy ที่ travel กับ agent ข้าม framework

## เกิดอะไรขึ้น
ที่ Fort Mason Center วันที่ 2 มิ.ย. Satya Nadella เปิด keynote Build 2026 ด้วย message ที่ชัดมาก — Microsoft ไม่ใช่ "OpenAI distribution channel" อีกต่อไป Project Polaris คือ in-house coding model ที่บริษัทพัฒนาเองบน mixture-of-experts architecture, ใช้ chain-of-thought + tree-of-thought search ตอน inference และ run บน Maia AI accelerator ใน Azure Microsoft ประกาศว่าจะ replace GPT-4 Turbo เป็น default ของ Copilot subscriber ทั้งหมดในเดือน ส.ค. 2026 — มี optional fallback 3 เดือนให้ user แต่ส่งสัญญาณชัดว่าจะ migrate ทั้งฐาน

VS Code ก็ได้ multi-agent mode พร้อมกัน — orchestrator agent decompose task แล้ว delegate ให้ subagent ทำคู่ขนาน (linting, testing, doc, security review) พร้อมกัน แทนที่จะ serial เหมือนก่อน นี่คือคำตอบของ Microsoft ต่อ Claude Code ที่ Anthropic ใช้ subagent orchestration มาตั้งแต่ Opus 4.8

ฝั่ง infrastructure — Windows Agent Framework (WAF) v1.0 ออกเป็น MIT license เปิด open source เต็มรูปแบบ WAF มี 4 component หลัก: Agent Registration Service, Declarative Agent Manifest, Cross-Agent Communication Bus (gRPC-based), และ Memory Service สำหรับ conversational context — design เพื่อให้ agent run ได้บน local Windows, Windows 365 Cloud PC, และ Azure Arc edge device ใน manifest เดียว

และส่วนที่อาจ underrated ที่สุด — Microsoft เสนอ Agent Control Specification (ACS) เป็น open industry spec สำหรับ deterministic control ที่ checkpoint สี่จุด: input, LLM, state, tool execution, output policy ตัวนี้ "ติด" กับ agent ทำให้เคลื่อนข้าม Foundry, Microsoft Agent Framework, และ LangChain ได้โดยไม่ต้อง rewrite governance logic

## ทำไมสำคัญ
สิ่งที่เห็นชัดที่สุดคือ — Microsoft เริ่มเล่นเกม agentic infrastructure แบบ full-stack เหมือนที่ Google เล่นกับ ADK + A2A protocol ที่ Cloud Next สามเดือนก่อน Polaris คือ model layer, WAF คือ runtime layer, ACS คือ governance layer — สามชั้นที่ Microsoft control เองทั้งหมด ไม่ต้องพึ่ง OpenAI อีก นี่คือ pivot ที่ใหญ่กว่าที่หลายคนคิด เพราะ Microsoft เคยถือ $14B equity ใน OpenAI แต่กลยุทธ์ใหม่ชัดว่า Azure ต้องเป็น "platform ของ agent ทุกค่าย" ไม่ใช่ "OpenAI exclusive"

ACS คือ move ที่อันตรายที่สุดสำหรับคู่แข่ง — ถ้า enterprise adopt ACS เป็น governance layer พวกเขาจะ lock-in ที่ control plane ไม่ใช่ที่ model ทำให้ vendor swap model ง่ายขึ้น แต่ swap governance ยากขึ้น เป็นคนละเกมกับ MCP (connectivity) และ A2A (inter-agent) — และ Microsoft กำลังพยายาม own layer นี้ก่อนใครจะมา standardize

อีกมุมที่น่าสนใจ — Microsoft เปิด WAF เป็น MIT license, นี่ไม่ใช่บริษัทที่เคย open-source อะไรง่าย ๆ การที่ออก license แบบเสรีที่สุดบอกว่า Microsoft ต้องการให้ developer และ enterprise adopt เร็ว ๆ ก่อนที่ Google ADK หรือ LangGraph จะ lock community ลงไป

## มุม OpenBridge
ACS คือสิ่งที่ OpenBridge ต้องอ่านละเอียดที่สุดในรอบนี้ — เพราะ governance ที่ "travel with the agent" คือ pattern เดียวกับที่ integration platform ต้องการ เวลา agent ของ enterprise วิ่งข้าม workflow ข้าม system policy ก็ต้องตามไปด้วย ถ้า ACS adopt กว้างจริง OpenBridge อาจ build ไม่ต้องคิด policy framework เอง แต่ adopt ACS แล้วโฟกัสที่ workflow + connector layer แทน

อีกมุม — Multi-agent VS Code mode แสดง pattern ที่ enterprise จะคุ้นเคยเร็ว: orchestrator + specialist subagent นี่คือ design pattern ที่ B2B automation tool ต้อง support ภายในปีนี้ ไม่งั้นจะถูกมองว่าเป็น "single-agent legacy" ของแต่ก่อน OpenBridge ต้องคิดให้ดีว่า workflow engine ของตัวเองจะ host หรือ orchestrate multi-agent ใน mode ไหน

## Sources
- [Microsoft Build 2026 Recap — All AI Announcements](https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/)
- [Microsoft offers devs a better way to control AI agent behavior — TechCrunch](https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/)
- [GitHub Copilot Replaces GPT-4 With Project Polaris — TechTimes](https://www.techtimes.com/articles/317596/20260602/github-copilot-replaces-gpt-4-project-polaris-ships-multi-agent-vs-code-build.htm)
- [Microsoft Build 2026: Windows becomes the platform for AI agents](https://windowsnews.ai/article/microsoft-build-2026-windows-becomes-the-platform-for-ai-agents.420503)

---

## Audio script
Microsoft Build 2026 ที่ Fort Mason เมื่อวันที่ 2 มิถุนายน ส่งสัญญาณชัดว่าบริษัทกำลังตัดสายพึ่งพา OpenAI Project Polaris คือ coding model ใน-house ของ Microsoft ใช้ mixture-of-experts architecture จะ replace GPT-4 Turbo เป็น default ของ GitHub Copilot subscriber ทั้งหมดในเดือนสิงหาคม VS Code ได้ multi-agent mode มี orchestrator agent กระจายงานให้ subagent ทำคู่ขนาน linting, testing, doc, security review พร้อมกัน นี่คือคำตอบของ Microsoft ต่อ Claude Code ฝั่ง infrastructure Windows Agent Framework v1.0 ออก MIT license เปิด open source เต็มรูปแบบ มี cross-agent communication bus, memory service, agent manifest ใช้ run agent ได้ทั้งใน Windows local, Windows 365 Cloud PC, และ Azure Arc edge device ส่วนที่ underrated ที่สุดคือ Agent Control Specification หรือ ACS เป็น open spec สำหรับ governance policy ที่ travel ข้าม framework ได้ ทั้งใน Foundry, Microsoft Agent Framework และ LangChain สำหรับ integration platform แบบ OpenBridge — ACS น่าจับตามาก เพราะอาจกลายเป็น governance layer ที่ใช้ร่วมกันได้ ทำให้บริษัทไม่ต้อง build policy framework เอง แต่โฟกัสที่ workflow และ connector layer แทน
