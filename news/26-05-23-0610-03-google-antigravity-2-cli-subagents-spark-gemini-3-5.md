---
date: 2026-05-22
slug: google-antigravity-2-cli-subagents-spark-gemini-3-5
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Hero illustration showing a Google Antigravity logo at the center with a
  command-line terminal on the left and multiple subagent worker icons
  branching out in parallel on the right, like a fan of identical robotic
  arms each holding a tool. Large text overlay reads "ANTIGRAVITY 2.0" and
  "CLI" in bold, with a smaller "Gemini 3.5 Flash" badge. Composition:
  centered platform logo, terminal on the left rendering green-on-black
  code, parallel subagents on the right in Google brand colors (blue,
  yellow, red, green). Style: clean editorial tech illustration, isometric,
  flat vector with subtle gradients, Google blog aesthetic. No human faces.
image: images/26-05-23-0610-03-google-antigravity-2-cli-subagents-spark-gemini-3-5.png
---

# Google Antigravity 2.0 + agy CLI — กลายเป็น agent IDE เต็มตัว แทนที่ Gemini CLI ทิ้ง

## TL;DR
- Google เปิด **Antigravity 2.0** ที่ I/O 2026 (19 พ.ค.) + on-demand session 85 sessions เริ่ม 21 พ.ค. — เป็น standalone "agent-first development platform" ที่ replace Gemini CLI ทั้งหมด
- ของจริงคือ desktop IDE + **agy** CLI (Go-based) + SDK + Managed Agents API tier + Gemini Enterprise Agent Platform — เป็น stack เต็ม end-to-end
- ขับด้วย **Gemini 3.5 Flash** ที่ Google เคลม "outperform Gemini 3.1 Pro บน coding/agentic benchmark โดยเร็วกว่า frontier 4 เท่า" — multi-agent orchestration เป็น UX หลัก

## เกิดอะไรขึ้น

ที่ Google I/O 2026 — keynote วันที่ 19 พ.ค. แต่ developer track + 85 sessions on-demand เปิดวันที่ 21 พ.ค. — Google ประกาศ Antigravity 2.0 เป็นการรีลิสครั้งใหญ่ที่บอกตรง ๆ ว่า platform นี้ไม่ใช่ "Gemini CLI ตัวใหม่" อีกต่อไป แต่เป็น "agent-first development platform" แบบ standalone — Gemini CLI ตัวเก่าถูก deprecate ออกจาก roadmap

stack ที่ ship มาประกอบด้วย: desktop IDE ใหม่ที่ multi-agent orchestration เป็น centerpiece UX, **agy** CLI ที่เขียนใหม่ด้วย Go (Google บอกว่าเร็วกว่า predecessor เห็น ๆ), Antigravity SDK สำหรับ build agent ของตัวเอง, Managed Agents API tier (เหมือน Claude Managed Agents ที่ Anthropic เปิดเดือนก่อน), และเส้นทาง enterprise deploy ผ่าน Gemini Enterprise Agent Platform — ครบตั้งแต่ local dev จนถึง production multi-tenant

หัวใจของ UX คือ subagent orchestration — lead agent รับ high-level goal แล้ว delegate ไปยัง specialist subagent หลายตัวที่รันแบบ parallel แต่ละตัวมี context window, model, prompt, tool set ของตัวเอง รูปแบบเดียวกับที่ Claude Code, Anthropic's Managed Agents, OpenAI Codex ใช้ — แต่ Google ดัน UI ให้ developer เห็น tree ของ subagents และ rewind/branch ได้ใน IDE มี cross-platform terminal sandboxing, credential masking, hardened Git policies built-in สิ่งที่ขับทั้งหมดคือ Gemini 3.5 Flash ที่ Google เคลมว่า outperform Gemini 3.1 Pro บน coding/agentic benchmark แถมเร็วกว่า frontier model อื่น 4 เท่า

นอกเหนือจาก dev tool Google ก็ปล่อย **Gemini Spark** — general-purpose AI agent ที่ run background 24/7 ผูกกับ Google Workspace ทำ long-horizon task แบบ multi-day "ผู้ช่วยส่วนตัวที่ทำงานแทนคุณภายใต้คำสั่งของคุณ" ตามคำของ Sundar Pichai เปิดให้ Google AI Ultra subscriber ($100/เดือน) ก่อน

## ทำไมสำคัญ

นี่คือสัญญาณว่า **agent-IDE war เริ่มแล้วเต็มตัว** — Cursor (with Composer), Anthropic Claude Code, OpenAI Codex IDE, GitHub Copilot Workspace, และ Google Antigravity ทั้งห้าตัวกำลัง converge ไปสู่ pattern เดียวกัน: multi-subagent orchestration + sandboxed exec + scheduled background runs + IDE ที่ developer ดู agent ทำงานเหมือนดู colleague ทำงาน developer ที่ใช้แต่ละ tool ก็จะตัดสินใจตาม "ของไหนอยู่ใน workflow ของฉันอยู่แล้ว" — Antigravity ได้เปรียบที่ผูกกับ Workspace + Google Cloud + Gemini API ตั้งแต่แรก แต่เสียเปรียบที่ ecosystem yet to prove

จุดที่ Google เลือก strategic คือ "agents not chatbots" thesis — Gemini Spark, agentic Search information agents, Antigravity 2.0 ทั้งหมดเป็น signal เดียวกันว่า Google ตัดสินใจว่า roadmap ปีหน้าคือ background agent ไม่ใช่ chat UI การ deprecate Gemini CLI ทิ้งและ replace ด้วย Antigravity CLI ภายในรอบเดียวก็แปลว่า Google ยอม disrupt user base ตัวเองเพื่อ commit เต็มตัวกับ agent paradigm — Microsoft กับ OpenAI ที่ยัง support chat-first product จะต้องตัดสินใจตามว่าจะ pivot แค่ไหน

หนึ่งจุดอ่อนที่นักวิจารณ์ชี้คือ Gemini Spark ล็อกอยู่หลัง Google AI Ultra ที่ราคา $100/เดือน — ฐานผู้ใช้ที่จะทดสอบ real-world load จะเล็กกว่า Gemini Free หรือ ChatGPT ปกติมาก Spark จะเป็น flagship แบบ "Apple Vision Pro ของ Google AI" หรือจะ scale ลงมาที่ tier ถูกกว่าได้ไหม คือคำถามที่ยังไม่มีคำตอบ

## มุม OpenBridge

OpenBridge เป็น integration platform — ความเสี่ยงตรงคือ **Gemini Spark ที่ผูกกับ Workspace + Gmail แบบ deep integration อาจกินตลาด workflow automation ระดับ SMB** ที่เคยเป็นพื้นที่ของ Zapier, Make, n8n SMB ที่ใช้ Google Workspace อยู่แล้ว ไม่ต้อง integrate อะไรเพิ่ม — Spark ทำให้ "send weekly report from Sheets to email + Slack" กลายเป็นคำสั่งภาษาธรรมชาติ

แต่จุดที่ OpenBridge เกาะได้คือ **cross-vendor integration** — Spark จะแข็งใน Google ecosystem แต่อ่อนเมื่อ workflow ต้อง touch Salesforce + HubSpot + Notion + Linear พร้อมกัน OpenBridge ที่ position ตัวเองเป็น "agent-ready integration layer" ระหว่างหลายระบบ + ให้ enterprise control + audit log จะมีพื้นที่ — แต่ต้องรีบ ship MCP support (ดู brief #1 ที่ MCP spec กำลังจะ stabilize) เพื่อให้ Antigravity SDK + Claude + Codex ใช้ OpenBridge เป็น tool ได้ทันที

## Sources
- [Google launches Antigravity 2.0 at I/O 2026 — TechCrunch](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool/)
- [Google Launches Antigravity 2.0 — Standalone Agent-First Platform — MarkTechPost](https://www.marktechpost.com/2026/05/19/google-launches-antigravity-2-0-at-i-o-2026-a-standalone-agent-first-platform-with-cli-sdk-managed-execution-and-enterprise-support/)
- [Google introduces Gemini Spark, a 24/7 agentic assistant — TechCrunch](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/)

---

## Audio script
ข่าวที่สาม Google ที่ I/O 2026 ปล่อย Antigravity 2.0 เป็น agent-first development platform แบบ standalone และตัดสินใจ deprecate Gemini CLI ตัวเก่าออกจาก roadmap stack ของ Antigravity ใหม่ครบตั้งแต่ desktop IDE ที่ multi-agent orchestration เป็น centerpiece CLI ใหม่ชื่อ agy ที่เขียนด้วย Go SDK สำหรับ build agent ของตัวเอง Managed Agents API tier และเส้นทาง enterprise deploy ผ่าน Gemini Enterprise Agent Platform ขับด้วย Gemini 3.5 Flash ที่ Google เคลมว่าเร็วกว่า frontier model อื่น 4 เท่า UX หลักคือ subagent orchestration ที่ lead agent delegate งานไปยัง specialist subagent หลายตัวพร้อมกัน developer เห็น tree ของ subagent ใน IDE และ rewind ได้ Google ยังปล่อย Gemini Spark personal agent ที่รันตลอด 24 ชั่วโมงเข้ากับ Workspace + Gmail แบบ deep integration ความหมายคือ agent IDE war เริ่มเต็มตัวแล้ว Cursor Claude Code Codex Copilot Workspace และ Antigravity ทั้งหมด converge ไปสู่ pattern เดียวกัน Google เลือก commit เต็มตัวกับ agent paradigm ยอม disrupt user base ของ Gemini CLI ทิ้ง สำหรับ OpenBridge ความเสี่ยงคือ Spark ที่ผูกกับ Google Workspace อาจกินตลาด workflow automation ระดับ SMB ที่ใช้ Google ecosystem แต่ถ้า OpenBridge รีบ ship MCP support ให้ Antigravity เรียกใช้ OpenBridge เป็น tool ได้ก็จะได้พื้นที่ cross-vendor ที่ Spark อ่อนครับ
