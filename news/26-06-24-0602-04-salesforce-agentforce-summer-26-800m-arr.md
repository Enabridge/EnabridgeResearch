---
date: 2026-06-16
slug: salesforce-agentforce-summer-26-800m-arr
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  Hero illustration of Salesforce Agentforce multi-agent orchestration reaching $800M ARR.
  Central visual metaphor: a stylized conductor's podium at the center labeled "Atlas Reasoning
  Engine 3.0" with a glowing baton, conducting an orchestra of small specialized agent icons
  arranged in concentric arcs around it — each agent labeled with a business function like
  "Sales", "Service", "Marketing", "Commerce". An MCP plug icon connects from the side, and a
  small Slack hash-icon hangs at the bottom. Foreground: bold metric card "$800M ARR · +169% YoY"
  and below "29,000 deals · 2.4B agentic work units". Salesforce cloud logo top-right.
  Composition: centered 1:1 square, conductor podium 50% of frame, deep navy blue background with
  bright cyan and Salesforce-blue accents, high contrast white type. Style: clean editorial
  vector illustration in Stratechery hero art aesthetic, no real human faces, text crisp and
  legible at 200px thumbnail.
image: images/26-06-24-0602-04-salesforce-agentforce-summer-26-800m-arr.png
---

# Salesforce Agentforce Summer '26 GA — $800M ARR และจุดเริ่มของ multi-agent ระดับ enterprise

## TL;DR
- Salesforce Summer '26 ปล่อย Agentforce Multi-Agent Orchestration GA (รัน wave จาก 13-15 มิ.ย.) — agent หลายตัวทำงานทีม share context ผ่าน primary agent
- Atlas Reasoning Engine 3.0 เป็น coordination layer; ใช้ agent description routing แบบ no fixed decision tree; รองรับ MCP + A2A protocol
- Agentforce ARR แตะ $800M (+169% YoY), ปิด 29,000 deal ในปีที่ผ่านมา, log 2.4 พันล้าน agentic work unit รวมกับ Slack

## เกิดอะไรขึ้น

15 มิถุนายน Salesforce ปล่อย Summer '26 release wave สู่ลูกค้าทั่วโลก โดยตัวเอกของรอบนี้คือ Agentforce Multi-Agent Orchestration ที่ graduate จาก beta เป็น GA. โครงสร้างของ multi-agent setup ใหม่นี้ใช้ primary agent เป็น single point of contact ของลูกค้า — มันรับ request แล้ว route ไปยัง specialist subagent ตามภาระงาน (sales, service, marketing, commerce) โดยที่ subagent share context ระหว่างกัน. ความเปลี่ยนแปลงสำคัญที่ทำให้นี่ไม่ใช่แค่ "chain agent" ปกติคือ Atlas Reasoning Engine 3.0 — coordination layer ใหม่ที่อ่าน description + instruction + action ของแต่ละ subagent แล้วตัดสินใจเอง ว่าใครควรทำ ไม่มี fixed decision tree. ผลคือ "quality ของ agent description คือ quality ของ routing" — คำที่เขียนผิดทำให้ traffic ไปผิด agent.

ตัวเลข business ที่ Salesforce ปล่อยมาในรอบเดียวกันคือเรื่องที่นักลงทุนจับตา. Agentforce ทำ ARR แตะ $800M เพิ่ม 169% YoY, ปิด 29,000 deal ในปีที่ผ่านมา, log "agentic work unit" รวม 2.4 พันล้านครั้งใน Agentforce + Slack. ที่สำคัญ Summer '26 ยังเปิด MCP support ใน Tableau (อ่าน data ผ่าน MCP server) และเริ่มมี A2A (agent-to-agent) protocol — แปลว่า Agentforce ไม่ได้พยายามเป็น closed garden มันรองรับ standard ที่ Anthropic, Google, Microsoft กำลัง push ในระดับ industry.

ในเวลาเดียวกัน Salesforce ประกาศร่วม ServiceNow ผ่าน Cognizant Neuro AI platform (18 มิ.ย.) ให้ ServiceNow AI agent วิ่ง interoperate กับ Salesforce และระบบ enterprise อื่น — นี่คือ signal ว่า cross-vendor agent orchestration เริ่มเป็นมาตรฐานการขาย ไม่ใช่ aspiration.

## ทำไมสำคัญ

$800M ARR + 169% YoY ไม่ใช่ตัวเลขเล่น ๆ. มันแปลว่า Agentforce กลายเป็น line item ใน enterprise software budget ของลูกค้าจริง — และโตเร็วกว่าผลิตภัณฑ์ Salesforce ตัวอื่น ๆ ในประวัติศาสตร์บริษัท. 2.4 พันล้าน agentic work unit ก็เป็น metric ที่ทำให้นักวิเคราะห์เริ่มเปลี่ยนวิธีคิด — work output ที่ AI ทำกำลังเทียบเคียงกับ human work unit ในระดับ measurable. Marc Benioff เริ่ม flip narrative จาก "AI augments employees" ไปทาง "agentic labor is a new line item" ในไตรมาสที่แล้ว ตอนนี้มีตัวเลขรองรับ.

แต่ insight ที่ลึกกว่านั้น — Salesforce ยอมเปิด MCP + A2A คือ admission ว่า closed agent ecosystem แพ้แน่ ๆ. Salesforce ครองข้อมูล CRM แต่ workflow จริงของ enterprise วิ่งข้าม Slack, ServiceNow, SAP, Workday, Atlassian. ถ้า Agentforce ไม่พูดภาษามาตรฐาน customer จะไป assemble agent บน platform กลาง (เช่น LangChain, n8n, หรือ custom) แล้ว Salesforce กลายเป็นแค่ data source. การเปิด MCP/A2A คือ defensive move เพื่อให้ Agentforce อยู่ใน flow ของ multi-vendor agent orchestration ที่กำลังเกิด.

POV: ปี 2026 ครึ่งหลังจะเป็นช่วงที่ "agent description quality" กลายเป็น craft ใหม่ — เหมือน prompt engineering ของปี 2023 แต่ระดับ org. คำที่เขียนใน agent description = traffic control = revenue impact. คาดว่าจะมี vendor ใหม่เกิดเพื่อทำ "agent description optimization" คล้าย SEO consultancy ในอดีต.

ระวัง: ตัวเลข ARR เป็น Salesforce เคลม, "agentic work unit" เป็น definition ของ Salesforce เอง — ไม่ใช่ industry standard. 29,000 deal ก็ไม่ได้บอก ACV (average contract value) — เป็นไปได้ว่า deal เล็กเยอะมากเพื่อ boost count.

## มุม OpenBridge

นี่คือ news ที่ matter ที่สุดของรอบนี้สำหรับ OpenBridge. ถ้า Salesforce ที่เคย bundle ทุกอย่างยังต้องเปิด MCP + A2A เพื่อให้ Agentforce อยู่รอด — แปลว่า "agent interoperability layer" คือสมรภูมิจริงของ 12 เดือนหน้า. OpenBridge ที่อยู่ฝั่ง integration platform มีโอกาสตำแหน่งเป็น "vendor-neutral agent orchestration" — รับ MCP server ใด ๆ, route request ระหว่าง Agentforce subagent + Claude Tag + Copilot agent + custom in-house agent ในรอบเดียว. POV ที่ defensible: ลูกค้า SEA mid-market จะไม่ใช้ Salesforce stack ทั้งหมด แต่จะ pick-and-mix — point นี้ทำให้ "neutral orchestration" valuable.

อย่างที่สอง — Atlas 3.0 ใช้ "agent description" ในการ routing. นี่คือ pattern ที่ OpenBridge ควร adopt เร็ว: connector + workflow ทุกตัวควรมี "agent-readable description" ในรูปแบบที่ MCP / A2A เข้าใจได้ ไม่ใช่แค่ doc สำหรับมนุษย์อ่าน. ถ้าทำตั้งแต่ตอนนี้ OpenBridge connector library จะ plug เข้า agent orchestration ของลูกค้าได้แทบจะอัตโนมัติ — เป็น moat ที่สร้างยากถ้ารอ.

## Sources
- [Salesforce Summer 2026 Product Release Announcement](https://www.salesforce.com/news/stories/summer-2026-product-release-announcement/)
- [Salesforce Agentforce Multi-Agent Orchestration Hits GA: Agent Descriptions Now Drive Reliability (TechTimes)](https://www.techtimes.com/articles/318456/20260616/salesforce-agentforce-multi-agent-orchestration-hits-ga-agent-descriptions-now-drive-reliability.htm)
- [Agentforce Reaches $800M ARR as Multi-Agent Era Begins (Enterprise DNA)](https://enterprisedna.co/resources/news/salesforce-summer-26-agentforce-800m-arr-multi-agent-2026/)
- [Salesforce Announces Summer '26: Agentforce Goes Multi-Agent, Tableau Gets MCP (ACTGSYS)](https://actgsys.com/en/blog/salesforce-agentforce-summer-26-multi-agent-sme-2026-06)

---

## Audio script
สวัสดีครับ Yoh ข่าวสุดท้ายของรอบนี้ Salesforce ปล่อย Summer '26 release ตัวเอกคือ Agentforce Multi-Agent Orchestration GA ครับ โครงสร้างคือมี primary agent เป็น single point of contact ลูกค้า แล้ว route ไปยัง specialist subagent ตามภาระงาน sales service marketing commerce ทุกตัว share context กัน Engine ใหม่ที่ทำหน้าที่ routing คือ Atlas Reasoning Engine 3.0 ใช้ agent description ในการตัดสินใจไม่มี fixed decision tree ตัวเลขที่นักลงทุนจับตาคือ Agentforce ARR แตะแปดร้อยล้านดอลลาร์ โตหนึ่งร้อยหกสิบเก้าเปอร์เซ็นต์ YoY ปิดสองหมื่นเก้าพัน deal ในปีที่ผ่านมา log agentic work unit รวมสองพันสี่ร้อยล้านครั้ง ที่สำคัญสุดคือ Salesforce ยอมเปิด MCP support ใน Tableau แล้วเริ่มมี A2A agent-to-agent protocol นี่คือ admission ว่า closed agent ecosystem แพ้แน่ ลูกค้า enterprise workflow จริงวิ่งข้าม Slack ServiceNow SAP Workday Atlassian Salesforce ต้องพูดภาษามาตรฐาน implication ที่ตรงสุดสำหรับ OpenBridge คือ ถ้า Salesforce ยังต้องเปิด MCP กับ A2A แปลว่า agent interoperability layer คือสมรภูมิจริงของสิบสองเดือนหน้า OpenBridge มีโอกาสตำแหน่งเป็น vendor-neutral agent orchestration รับ MCP server ใด ๆ route request ระหว่าง Agentforce Claude Tag Copilot agent custom in-house agent ในรอบเดียว แค่นี้ครับ
