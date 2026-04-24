---
date: 2026-04-24
slug: microsoft-onelake-mcp-fabric-ga
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a vast underground lake of glowing data streams with a glass key descending from above unlocking a gateway in the lake surface, streams of light radiating upward through the opening, minimal flat geometric shapes, muted deep teal and amber palette, soft gradient background, dramatic rim lighting, no text no logos no faces
image: images/26-04-24-0613-04-microsoft-onelake-mcp-fabric-ga.png
---

# Microsoft ปล่อย OneLake MCP + Fabric Local MCP GA — "ส่งกุญแจ data lake ให้ AI agent" เปิดสนามให้ agent เข้าถึงข้อมูล enterprise ผ่าน MCP เป็น default

## TL;DR
- **21 เม.ย.** Microsoft ประกาศ **OneLake MCP Generally Available** + **Fabric Local MCP GA** — AI agent (GitHub Copilot, Claude, Cursor, ChatGPT custom GPT) เชื่อม **OneLake enterprise data** ผ่าน MCP ได้โดยตรง, operate ผ่าน Azure identity + Fabric permission ไม่ต้อง custom API
- **Fabric Remote MCP ยัง preview** — cloud-hosted variant สำหรับ agent ที่ไม่ต้อง local setup; ship timeline ปลาย Q2
- Microsoft Fabric อ้าง **50,000+ organizations** ใช้ OneLake เป็น data lake หลัก — ตอนนี้ทุกรายเปิด agent native access ได้ทันทีโดยไม่ต้องเปลี่ยน data stack
- Signal: **hyperscaler ทั้งสามเปิด MCP native data access ในสัปดาห์เดียว** (Google Apigee MCP bridge + Microsoft OneLake MCP + AWS Bedrock MCP connectors เมื่อ 15 เม.ย.) = MCP ข้ามจุด protocol war จบ เข้า **commodity data access layer**

## เกิดอะไรขึ้น

วันอังคาร 21 เม.ย. ทีม Fabric product group เผยแพร่ 2 blog post เงียบ ๆ ที่เปลี่ยน landscape ของ enterprise data lake มากกว่าที่ headline จะสะท้อน. Post หลัก "Give your AI agent the keys to OneLake: OneLake MCP (Generally Available)" และ post คู่ "Fabric Local MCP is now generally available" — 2 GA release ในวันเดียวกัน ไม่ได้อยู่ใน keynote FabCon (ที่จบไปมี.ค.) แต่ slip เข้า production ในช่วงก่อน Cloud Next เพื่อ **block narrative Google** ก่อน 24 ชั่วโมง

**OneLake MCP** คืออะไร: MCP server ที่ expose OneLake data plane ให้ AI agent ใช้งาน **ผ่าน conversational language**. Agent ถาม "ใน workspace finance มี table ไหนที่มี column 'customer_id' และ 'invoice_date' ที่ใช้ reconciliation ได้บ้าง?" — OneLake MCP ตอบพร้อม schema + sample row + usage metadata. Agent ต่อด้วย "join 2 tables นี้แล้ว filter Q1 2026 export เป็น Parquet เข้า workspace analytics" — executed ภายใน OneLake permission ที่ existing user มี. Tools ครอบคลุม: **file system APIs** (browse, read, write), **table APIs** (schema + metadata discovery), **workspace/item discovery** (help agent navigate)

จุดที่ต่างจาก generic MCP server: **Azure identity + Fabric permission native**. Agent ไม่ได้วิ่งใต้ service account ที่มี god-mode — ใช้ **existing user identity** ที่ trigger session. ถ้า user มีสิทธิ์ dataset finance-prod agent ได้; ถ้าไม่ = agent ปฏิเสธ request พร้อม error message ชัด. Model เดียวกันที่ทุก enterprise expect จาก data security review — Microsoft ship มาพร้อม compliance framework (SOC 2, HIPAA, FedRAMP Moderate baseline) จาก Fabric tier ที่มีอยู่แล้ว

**Fabric Local MCP GA** คือ server variant ที่ run ใน developer machine — ให้ **GitHub Copilot, Claude Code, Cursor** เชื่อมต่อ Fabric API ได้ตรงผ่าน MCP. Use case: developer ถาม Cursor "เขียน notebook ที่ clean duplicated customer record ใน workspace customer-analytics" — Cursor ใช้ Fabric Local MCP ตรวจ workspace หา duplicate pattern เขียน PySpark notebook + run validation + push กลับ Fabric. Microsoft บอกว่าเปิด **open-source** ซึ่งน่าสังเกต — ส่งสัญญาณว่าอยากให้ framework adoption โต (และ commoditize data-access protocol ก่อน Google Apigee จะ dominate)

สิ่งที่ยัง preview: **Fabric Remote MCP** — cloud-hosted MCP server ที่ agent ไม่ต้อง local install. Microsoft ระบุว่า GA target Q2 2026 ปลาย. ยังไม่มี pricing disclosure แต่คาดว่า bundle ในแพ็ก Fabric Capacity tier F64/F128 เหมือน feature อื่น

## ทำไมสำคัญ

Pattern ที่ตกผลึกในสัปดาห์เดียวคือ **MCP ข้ามจุด protocol war จบ เข้า commodity layer ของ enterprise data access**. 14 เม.ย.: AWS Bedrock MCP connectors GA (ตอบรับ Cloudflare reference architecture). 21 เม.ย.: Microsoft OneLake MCP GA + Fabric Local MCP GA. 22 เม.ย.: Google Apigee MCP bridge + Gemini Enterprise Agent Platform. **3 hyperscaler** เปิด native MCP data access สำหรับ enterprise data stack ของตัวเองภายใน **7 วัน**. ไม่มีใครตัดสินใจเชิง strategy แข่ง MCP อีกต่อไป — ทุกคนรู้ว่าจะอยู่นอกวง ecosystem ถ้าไม่ support

จุดที่ Microsoft ได้ unique advantage: **OneLake installed base**. Fabric ถึง FabCon 2026 มี **50,000+ organizations** ใช้ (Microsoft ranges claim), คิดตาม Microsoft Q3 FY26 earnings ที่ Fabric revenue จะเกิน $3B annualized ในครึ่งปีหลัง. ทั้งกลุ่มนี้ตอนนี้ **เปิด agent native access ได้ทันทีโดยไม่ต้องเปลี่ยน stack** — ไม่เหมือน Databricks/Snowflake ที่ต้องไปหา partner MCP server ข้างนอก. Compute pull-through effect: agent ที่เรียก OneLake = Azure OpenAI compute + Fabric compute ถูก utilized มากขึ้น — margin ขึ้นทันทีจาก capacity ที่ลูกค้าซื้อไว้อยู่แล้ว

Strategic read: **Microsoft ไม่พยายามเป็น agent control plane ชน Gemini Enterprise** — แต่เดิมพันว่าเป็น **data/storage layer ใต้** ของ agent stack ทุกตัว. ถ้าลูกค้าใช้ Google Gemini Enterprise แต่ data อยู่ OneLake = Microsoft ได้ compute + storage fee. ถ้าลูกค้าใช้ ChatGPT Workspace Agents + OneLake = เหมือนกัน. **Switzerland positioning** ที่ Google พยายามทำกับ model (host Claude/Llama/Mistral) แต่ Microsoft ทำกับ data layer — เล่น neutral แต่เก็บ margin จากทุกฝั่ง

ที่ต้องจับตา 60–90 วัน: **Databricks ตอบอย่างไร**. Databricks Unity Catalog MCP ที่ preview ตั้งแต่เดือนเม.ย. ต้น + Mosaic AI Agent Framework ที่เพิ่ง GA — ถ้าตอบช้า จะเสีย mid-market enterprise ที่ยังไม่ commit OneLake vs Databricks. Snowflake ยังไม่มี MCP GA announcement — ถ้าเกิน Databricks ด้วย จะสูญ data platform share 3–5 points ภายในปี

## มุม OpenBridge

**Direct relevance: OneLake MCP GA คือการพิสูจน์ pattern ที่ OpenBridge ต้อง copy ทันที**. OpenBridge ตอนนี้ wrap Thai SaaS APIs (FlowAccount, PEAK, LINE OA) ไว้เป็น connector. **ขั้นต่อไป** = expose ทั้งหมดเป็น **MCP server tier** ที่ลูกค้าใช้ Cursor/Claude Code/ChatGPT custom GPT/Grok ดึง Thai data operation ได้ตรง. คือไม่ใช่แค่ให้ agent run บน OpenBridge — แต่ให้ **external agent ใด ๆ** เข้าถึง Thai SaaS data ผ่าน OpenBridge MCP gateway

**Product action ภายใน 30 วัน**: (1) ออก **"OpenBridge MCP Gateway" v1** — expose 5 Thai SaaS (FlowAccount, PEAK, LINE OA, Shopee Seller, Lazada Seller) เป็น MCP server + OAuth-based permission ที่ใช้ login ของ user ต้นทาง; (2) **documentation + quickstart** สำหรับ 3 use case (Cursor + OpenBridge MCP → Thai SMB finance report, Claude Code + OpenBridge MCP → LINE OA campaign analysis, ChatGPT Team + OpenBridge MCP → sales pipeline)

**Strategic framing**: เกมของ OpenBridge ไม่ใช่ build control plane แข่ง Google/Microsoft — **แต่เป็น "OneLake สำหรับ Thai SMB operational data"** — expose data + workflow ของ SMB stack ไทยที่ hyperscaler ไม่ซีเรียส. Pricing model: MCP tier แบบ usage-based ($0.01/tool call, $500 monthly minimum) + enterprise tier สำหรับ Bank/Telco ที่ต้อง compliance. Moat: **Thai API idiosyncrasy** — FlowAccount auth flow, LINE OA rate limit, PEAK tax report format, Shopee seller center UX quirks — รู้จักดีพอจะ wrap เป็น clean MCP tool ได้ = 12–18 เดือน ก่อน competitor

**Watch signal**: ถ้า Microsoft/Google ประกาศ **LINE OA official MCP connector** (OpenAI GPT-5.5 Workspace น่าจะมาก่อน) ใน Q2 = window ของ OpenBridge ในตลาด Thai SMB จะแคบลงจาก 12–18 เดือน → 3–6 เดือน. ต้อง lock **exclusive beta partner** กับ FlowAccount/PEAK อย่างน้อย 1 รายภายใน 45 วันเพื่อ create integration depth ที่ copy ไม่ได้ง่าย

## Sources
- [Give your AI agent the keys to OneLake: OneLake MCP (Generally Available) (Microsoft Fabric Blog)](https://blog.fabric.microsoft.com/en-us/blog/give-your-ai-agent-the-keys-to-onelake-onelake-mcp-generally-available/)
- [Agentic Fabric: How MCP is turning your data platform into an AI-native operating system (Microsoft Fabric Blog)](https://blog.fabric.microsoft.com/en-us/blog/agentic-fabric-how-mcp-is-turning-your-data-platform-into-an-ai-native-operating-system/)
- [Use AI agents with OneLake through MCP (Microsoft Learn)](https://learn.microsoft.com/en-us/fabric/onelake/onelake-local-mcp)
- [FabCon and SQLCon 2026: What's new in Microsoft OneLake (Microsoft Fabric Blog)](https://blog.fabric.microsoft.com/en-us/blog/fabcon-and-sqlcon-2026-whats-new-in-microsoft-onelake/)

---

## Audio script
วันอังคารยี่สิบเอ็ดเมษา ทีม Fabric product group เผยแพร่สอง blog post เงียบ. OneLake MCP Generally Available กับ Fabric Local MCP GA. สอง GA release ในวันเดียวกัน ไม่ได้อยู่ใน FabCon keynote แต่ slip เข้า production ในช่วงก่อน Cloud Next เพื่อ block narrative Google ก่อนยี่สิบสี่ชั่วโมง.

OneLake MCP คือ MCP server ที่ expose OneLake data plane ให้ AI agent ใช้ผ่าน conversational language. Agent ถามใน workspace finance มี table ไหนที่มี column customer id และ invoice date ที่ใช้ reconciliation ได้บ้าง. ระบบตอบพร้อม schema sample row usage metadata. Agent ต่อด้วย join สอง tables filter Q หนึ่ง สองพันยี่สิบหก export เป็น Parquet เข้า workspace analytics. Executed ภายใน OneLake permission ที่ existing user มี.

จุดที่ต่างจาก generic MCP server คือ Azure identity และ Fabric permission native. Agent ไม่ได้วิ่งใต้ service account god mode. ใช้ existing user identity. ถ้า user มีสิทธิ์ dataset finance prod agent ได้. ถ้าไม่ agent ปฏิเสธ request พร้อม error message ชัด.

Fabric Local MCP GA คือ server variant ที่ run ใน developer machine. ให้ GitHub Copilot Claude Code Cursor เชื่อมต่อ Fabric API ได้ตรงผ่าน MCP. Developer ถาม Cursor เขียน notebook ที่ clean duplicated customer record. Cursor ใช้ Fabric Local MCP ตรวจ workspace หา duplicate pattern เขียน PySpark notebook run validation push กลับ Fabric.

pattern ที่ตกผลึกในสัปดาห์เดียวคือ MCP ข้ามจุด protocol war จบ เข้า commodity layer ของ enterprise data access. สิบสี่เมษา AWS Bedrock MCP connectors GA. ยี่สิบเอ็ดเมษา Microsoft OneLake MCP GA. ยี่สิบสองเมษา Google Apigee MCP bridge. สาม hyperscaler เปิด native MCP data access ภายในเจ็ดวัน.

Microsoft ได้ unique advantage จาก OneLake installed base ห้าหมื่น organizations. ทั้งกลุ่มนี้เปิด agent native access ได้ทันทีโดยไม่ต้องเปลี่ยน stack. ไม่เหมือน Databricks Snowflake ที่ต้องไปหา partner MCP server ข้างนอก.

Microsoft ไม่พยายามเป็น agent control plane ชน Gemini Enterprise. แต่เดิมพันว่าเป็น data storage layer ใต้ agent stack ทุกตัว. Switzerland positioning ที่ Google พยายามทำกับ model แต่ Microsoft ทำกับ data layer. เล่น neutral แต่เก็บ margin จากทุกฝั่ง.

สำหรับ OpenBridge. OneLake MCP GA คือการพิสูจน์ pattern ที่ OpenBridge ต้อง copy ทันที. ขั้นต่อไปคือ expose Thai SaaS ทั้งหมดเป็น MCP server tier ที่ลูกค้าใช้ Cursor Claude Code ChatGPT custom GPT ดึง Thai data operation ได้ตรง. ไม่ใช่แค่ให้ agent run บน OpenBridge แต่ให้ external agent ใด ๆ เข้าถึง Thai SaaS data ผ่าน OpenBridge MCP gateway.

Product action ภายในสามสิบวัน. ออก OpenBridge MCP Gateway v หนึ่ง expose ห้า Thai SaaS FlowAccount PEAK LINE OA Shopee Seller Lazada Seller เป็น MCP server พร้อม OAuth based permission ที่ใช้ login ของ user ต้นทาง. Documentation quickstart สำหรับสาม use case.

Strategic framing. OpenBridge ไม่ใช่ build control plane แข่ง Google Microsoft. แต่เป็น OneLake สำหรับ Thai SMB operational data. Pricing MCP tier usage based หนึ่งเซ็นต์ต่อ tool call minimum ห้าร้อยเหรียญต่อเดือน enterprise tier สำหรับ Bank Telco.

Watch signal. ถ้า Microsoft Google ประกาศ LINE OA official MCP connector ใน Q สอง window OpenBridge แคบลงจากสิบสองถึงสิบแปดเดือน เหลือสามถึงหกเดือน. ต้อง lock exclusive beta partner กับ FlowAccount PEAK อย่างน้อยหนึ่งรายภายในสี่สิบห้าวัน
