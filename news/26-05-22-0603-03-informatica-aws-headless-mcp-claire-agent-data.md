---
date: 2026-05-22
slug: informatica-aws-headless-mcp-claire-agent-data
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric cross-section of an enterprise data warehouse — a sleek
  cobalt corporate cube labeled "INFORMATICA + CLAIRE AGENT" with internal
  glowing data shelves; on the right side of the cube glowing API rails labeled
  "MCP SERVERS" extend outward, plugging into a translucent AWS-orange cloud
  cluster containing modules labeled "BEDROCK AGENTCORE", "AWS AGENT REGISTRY",
  "AMAZON QUICKSIGHT". On the left, three smaller customer-side cubes labeled
  "DATABRICKS", "SNOWFLAKE", "ORACLE" plug in via parallel rails. Above floats
  a billboard reading "HEADLESS DATA MANAGEMENT FOR AGENTS" with stacked
  numbers "MCP-NATIVE", "ANY PLATFORM", "GOVERNED". Deep navy and AWS-amber
  rim lighting, ultra-sharp text rendering, high contrast for 200px thumbnail
  readability, 1:1 aspect, no real human faces.
image: images/26-05-22-0603-03-informatica-aws-headless-mcp-claire-agent-data.png
---

# Informatica + AWS เปิด Headless MCP — ดัน CLAIRE Agent skill เป็น data layer ของ Bedrock AgentCore

## TL;DR
- 20 พ.ค. ที่ Informatica World 2026 — Salesforce/Informatica + AWS เปิด **Headless Data Management** ที่ทำให้ **MCP server + CLAIRE Agent skill ของ Informatica ใช้งานข้าม AWS AI services** รวมถึง AWS Agent Registry + Amazon Quick + Bedrock AgentCore
- ปลดล็อก gap ใหญ่ที่สุดของ enterprise agent deployment: data ที่ trusted, governed, context-rich — ที่ก่อนหน้านี้ enterprise data team ต้อง build ใหม่ทุก agent ทุก platform
- Pattern เดียวกับที่ Anthropic ทำ MCP Tunnel (19 พ.ค.) — vendor ต่างค่ายเริ่ม converge รอบ MCP เป็น **standard interface ระหว่าง enterprise data กับ agent runtime**

## เกิดอะไรขึ้น

20 พฤษภาคม 2026 ที่ Informatica World 2026 — **Informatica (เพิ่งถูก Salesforce ปิดดีล acquire $8B ปลายปี 2025)** ประกาศ deeper integration กับ AWS ในรูปแบบที่เรียกว่า **"Headless Data Management"**. ความหมายของ headless ในที่นี้คือ Informatica แยก **MCP server + CLAIRE Agent skill** ออกจาก Informatica UI/console ดั้งเดิม แล้วเปิดให้ใช้งานข้าม AWS AI services โดยตรง — รวมถึง **AWS Agent Registry, Amazon QuickSight, และ Bedrock AgentCore**

กลไกคือ — Informatica มีของที่ enterprise data team ใช้ทำ data integration + governance + quality control มาหลายสิบปี (CLAIRE คือ AI metadata engine ที่รัน lineage + classification + recommendation ของ Informatica). การ wrap CLAIRE + data pipeline เป็น **MCP server-native interface** แปลว่า agent ที่รันบน Bedrock AgentCore (หรือ AWS Agent Registry ที่เป็น discovery layer) สามารถ "ถาม" Informatica ได้ตรง ๆ ว่า "table นี้คืออะไร, ใครเป็นเจ้าของ, มี PII ไหม, last refresh เมื่อไหร่" โดยไม่ต้องผ่าน custom integration

นี่คือสิ่งที่ Cdata research call ว่า "**unreliable data is the #1 barrier to enterprise AI**". 78% ของ production agent team เจอปัญหาเดียวกัน — agent มี LLM ที่ฉลาด, มี tool ครบ, แต่ data ที่ดึงมา query เป็น stale/duplicate/unauthorized/no-context. Informatica แก้ตรงนี้โดยให้ CLAIRE serve metadata + trusted data ผ่าน MCP — agent ไม่ต้องเดา schema, ไม่ต้องสุ่ม query, ไม่ต้องเสี่ยง compliance violation

ปลายอีกด้าน — AWS ได้สิ่งที่ขาดมาตลอด: **enterprise data foundation layer ที่ regulated industry ยอมรับ**. AWS Bedrock มี model ครบ, AgentCore มี runtime + payment + memory, AWS Agent Registry มี discovery — แต่ data layer ของลูกค้าจริงอยู่ใน Informatica/Collibra/Alation. การที่ Informatica เปิด MCP-native interface ใส่ AWS Agent Registry แปลว่า agent บน Bedrock จะ "ค้นเจอ + เชื่อถือได้" ข้อมูลของลูกค้าตั้งแต่ deploy day 1 — ไม่ต้องเสีย 6 เดือนทำ data prep ก่อน

## ทำไมสำคัญ

นี่คือสัญญาณว่า **MCP กำลังกลายเป็น universal interface ระหว่าง enterprise data system กับ agent runtime** — ไม่ใช่แค่ Anthropic feature อีกต่อไป. Timeline ใน 2 สัปดาห์ที่ผ่านมาเรียงตามนี้: Atlassian เปิด Teamwork Graph MCP + third-party agent (8 พ.ค.), Cloudflare เปิด enterprise MCP reference architecture, Anthropic เปิด MCP Tunnel + Self-Hosted Sandbox (19 พ.ค.), วันนี้ Informatica + AWS เปิด headless MCP. ทุก vendor — model, data, infra, SaaS — converge ที่จุดเดียวกัน

มอง 12 เดือนข้างหน้า — เราจะเห็น **MCP server marketplace ที่จัดเรียงตาม trust tier**. Tier 1 (sovereign data): Informatica, Collibra, Alation, Snowflake, Databricks — ผ่าน enterprise audit แล้ว. Tier 2 (SaaS standard): Salesforce, ServiceNow, Workday, Notion, Atlassian — ผ่าน vendor security review. Tier 3 (community): public registry ที่นับล่าสุดแตะ 9,400 server — caveat emptor. AWS Agent Registry กับ Anthropic MCP catalog กำลังแข่งเป็น **directory authority** ของ tier เหล่านี้

อีก signal — **Salesforce ใช้ Informatica เป็น aggressive play ใน enterprise data game**. Salesforce ลงทุน $8B ซื้อ Informatica เมื่อปลายปีที่แล้ว — ตอนนี้ใช้ Informatica เป็น proxy เข้าตลาด AWS-native enterprise (ที่ Agentforce ของ Salesforce เอง compete ได้ยากเพราะลูกค้า AWS-first ไม่อยาก lock in Salesforce stack). Move นี้ฉลาด — แทนที่จะดัน Agentforce ตรง ๆ ดันสิ่งที่ลูกค้า AWS อยากได้อยู่แล้ว (data foundation ที่ AWS-native) — แต่ติด Salesforce brand + data graph ไว้ด้านหลัง

## มุม OpenBridge

นี่คือ wake-up call ที่ OpenBridge ควรอ่านลึก. **Headless + MCP pattern ที่ Informatica เพิ่งทำคือ exact play ที่ integration vendor ทุกค่ายจะต้องทำใน 12 เดือนข้างหน้า** — รวมถึง OpenBridge เอง. ลูกค้า Thai bank ที่กำลัง deploy agent บน Bedrock/Claude/Gemini ไม่ต้องการ OpenBridge UI หรือ console — เขาต้องการ **OpenBridge MCP server ที่ agent ของเขา query ได้โดยตรง**. ถ้า OpenBridge ยังขาย UI-led integration อยู่ — ลูกค้า next-gen จะมองว่าตกยุค

Action item ระยะ 90 วัน: **wrap OpenBridge connector library ใหม่ทั้งหมดเป็น MCP server-native interface**. ทุก connector ที่ OpenBridge เคยสร้างให้ลูกค้า (CRM, ERP, BSS, banking core) ต้องมี MCP wrapper ที่ขึ้น public registry + private registry ของลูกค้าได้. ทำเป็น **"OpenBridge MCP Hub"** — directory ของ Thai/SEA enterprise connector ที่ certify ผ่าน BOT/MAS/BNM แล้ว. ใส่บน AWS Agent Registry + Anthropic MCP catalog + Google ADK marketplace ทั้งหมด

มอง long game — **data + governance layer คือที่ที่ OpenBridge ควร moat ตัวเอง, ไม่ใช่ workflow orchestration**. เพราะ workflow orchestration กำลังถูก commoditize ทุกค่าย (Spark, AgentCore, Anthropic Managed Agent ทำได้หมด). แต่ "data ที่ Thai regulator ยอมรับ + governed + audit-trail พร้อม" คือสิ่งที่ vendor ต่างชาติทำเองไม่ได้ — และเป็น niche ที่ Informatica เพิ่งพิสูจน์ว่ามี Salesforce ยอมจ่าย $8B ซื้อ. OpenBridge ควรเรียนรู้จาก deal นี้ว่า **data trust layer มีราคา** — ไม่ใช่แค่ pipe กับ adapter

## Sources
- [Informatica from Salesforce Delivers the Trusted Data Foundation Every AI Agent Needs (Salesforce Newsroom)](https://www.salesforce.com/news/press-releases/2026/05/20/informatica-delivers-trusted-data-foundation/)
- [Informatica Announces Headless Data Management for AWS to Power Trusted, Enterprise-Ready Agentic Workflows (Salesforce Newsroom)](https://www.salesforce.com/news/press-releases/2026/05/20/informatica-announces-headless-data-management-aws/)
- [Salesforce: Informatica Announces Headless Data Management for AWS (MarketScreener)](https://www.marketscreener.com/news/salesforce-informatica-announces-headless-data-management-for-aws-to-power-trusted-enterprise-rea-ce7f5ad9da89f02d)
- [Salesforce and AWS Deepen Collaboration to Launch Agentforce 360 for AWS (Salesforce Newsroom)](https://www.salesforce.com/news/stories/agentforce-360-for-aws-announcement/)
- [MCP Is Now Enterprise Infrastructure: MCP Dev Summit North America 2026 (Agentic AI Foundation)](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/)

---

## Audio script
สวัสดีครับโย้ ข่าว MCP น่าสนใจของเมื่อวาน Informatica ที่เพิ่งถูก Salesforce ปิดดีล acquire แปดพันล้านเมื่อปลายปีที่แล้ว ประกาศ deeper integration กับ AWS ในรูปแบบที่เรียกว่า Headless Data Management ความหมายคือ Informatica แยก MCP server กับ CLAIRE Agent skill ออกจาก UI ดั้งเดิม แล้วเปิดให้ใช้ข้าม AWS AI services โดยตรง รวมถึง AWS Agent Registry Amazon QuickSight Bedrock AgentCore

ปัญหาที่แก้คือ unreliable data is the number one barrier to enterprise AI เจ็ดสิบแปดเปอร์เซ็นต์ของ production agent team เจอปัญหาเดียวกัน agent มี LLM ฉลาด มี tool ครบ แต่ data ที่ดึงมา query เป็น stale duplicate ไม่มี context Informatica แก้โดยให้ CLAIRE serve metadata กับ trusted data ผ่าน MCP agent ไม่ต้องเดา schema ไม่ต้องเสี่ยง compliance violation

ทำไมสำคัญ MCP กำลังกลายเป็น universal interface ระหว่าง enterprise data system กับ agent runtime สองสัปดาห์ที่ผ่านมา Atlassian Cloudflare Anthropic Informatica ทุก vendor converge ที่จุดเดียวกัน เราจะเห็น MCP server marketplace ที่จัดเรียงตาม trust tier Tier หนึ่งคือ sovereign data Informatica Collibra Snowflake Tier สองคือ SaaS standard Tier สามคือ community registry นับล่าสุดเก้าพันสี่ร้อย server

มุม OpenBridge นี่คือ wake-up call ลูกค้า Thai bank ที่ deploy agent บน Bedrock Claude Gemini ไม่ต้องการ OpenBridge UI หรือ console เขาต้องการ OpenBridge MCP server ที่ agent ของเขา query ได้โดยตรง action item เก้าสิบวันคือ wrap OpenBridge connector library ใหม่ทั้งหมดเป็น MCP server-native interface ทำเป็น OpenBridge MCP Hub directory ของ Thai SEA enterprise connector ที่ certify ผ่าน BOT MAS BNM แล้วใส่บน AWS Agent Registry กับ Anthropic catalog บทเรียนจาก Salesforce ซื้อ Informatica แปดพันล้านคือ data trust layer มีราคา ไม่ใช่แค่ pipe กับ adapter ครับ
