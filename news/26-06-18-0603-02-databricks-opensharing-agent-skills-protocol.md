---
date: 2026-06-17
slug: databricks-opensharing-agent-skills-protocol
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a glowing central data hub labeled "OPENSHARING"
  with multi-colored connecting cables radiating out to floating cubes labeled
  "AGENT SKILLS", "ML MODELS" and "UNSTRUCTURED DATA". A bold orange Databricks
  logo flame sits at the hub center. Smaller labels "ZERO-COPY", "VENDOR-NEUTRAL"
  and "LINUX FOUNDATION" arc around the hub. Composition is symmetric radial,
  isometric perspective, deep navy background with bright orange and teal cables.
  Style is technical editorial illustration, high-contrast, brand marks and
  typography legible at 200px thumbnail size, no real human faces. 1:1 aspect
  ratio.
image: images/26-06-18-0603-02-databricks-opensharing-agent-skills-protocol.png
---

# Databricks เปิด OpenSharing — open protocol สำหรับแชร์ agent skill + ML model + unstructured data ข้าม platform เป็น zero-copy

## TL;DR
- 16 มิ.ย. ที่ Data + AI Summit 2026 (30,000+ คน, ดำเนินอยู่ขณะนี้) Databricks ร่วมกับ Linux Foundation เปิด OpenSharing — open protocol สำหรับแชร์ agent skill, ML model artifact, unstructured data ข้าม platform/org
- ต่อยอดจาก Delta Sharing (Databricks contribute ปี 2021) — ใช้ zero-copy REST architecture เดิมแต่ขยายไปยัง assets ใหม่ในยุค agent
- เปิด GitHub วันแรกพร้อม native support ใน Databricks platform — vision คือ "share intelligence ไม่ใช่แค่ data" + run app ตรงที่ data อยู่

## เกิดอะไรขึ้น

วันที่ 16 มิถุนายน 2026 ในช่วง Day 2 ของ Databricks Data + AI Summit ที่ Moscone Center, San Francisco (มีผู้เข้าร่วม 30,000+ คน, ยังดำเนินอยู่ถึง 18 มิ.ย.) Databricks ร่วมมือกับ Linux Foundation เปิดตัว **OpenSharing** — open, vendor-neutral protocol สำหรับการแชร์ AI assets ข้าม organization และ platform หลัก vision ตามที่ Databricks อธิบายในประกาศคือ "Data sharing was just the beginning. The next wave is about sharing intelligence, running apps where your data lives, and instant access to the data and AI products you depend on"

ที่ทำให้ OpenSharing น่าสนใจคือมัน **ไม่ใช่ของใหม่ทั้งหมด** — เป็น evolution ของ Delta Sharing ที่ Databricks เปิด open source ตั้งแต่ปี 2021 และกลายเป็น de facto standard สำหรับ zero-copy data sharing ระหว่าง warehouse OpenSharing เอา zero-copy REST architecture เดิม + ขยาย scope ไปยังสามอย่างใหม่ที่ enterprise กำลังจะแชร์กันในยุค agentic: (1) **agent skills** — proprietary tools/functions ที่ agent ใช้, (2) **trained ML model artifacts** — checkpoints, weights, fine-tuned heads, (3) **unstructured data volumes** — PDF/image/audio ที่ agent ต้องเข้าถึง

Use case ที่ Databricks ยกขึ้นมา concrete — สมมติว่าบริษัท data provider ต้องการแชร์ proprietary agent skill ให้ลูกค้า เพื่อให้ data ของตัวเอง usable โดย agent ของลูกค้า แทนที่จะต้อง deliver file ที่ลูกค้าต้อง copy + update ตลอด, OpenSharing ให้ zero-copy access ตรงที่ source — agent skill อยู่ที่ provider, ลูกค้าเรียกใช้ผ่าน standard API, มี discovery + authorization layer ของตัวเอง Linux Foundation รับเป็น project ทำให้ governance ออกจาก Databricks เป็น vendor-neutral

ข่าวรอบ Summit ใหญ่กว่าแค่ OpenSharing — Day 2 ยังมี **Unity AI Gateway** updates + Catalog Federation demo จาก Mastercard + featured session จาก Anthropic, OpenAI, Cognition, CrewAI, Glean, LangChain, LlamaIndex, Lovable, Replit — Databricks ตำแหน่งตัวเองชัดเจนว่าเป็น "data + agent infrastructure platform" ที่ทุก agent vendor ต้องวิ่งผ่าน ไม่ใช่ AI lab แข่งทำ frontier model วันที่ 17 มิ.ย. (Day 3) มี Data After Hours ที่ Oracle Park พร้อม The Chainsmokers — งานระดับนี้บอก scale ของ ecosystem

## ทำไมสำคัญ

OpenSharing คือ **direct response ต่อ MCP** — Anthropic เปิด Model Context Protocol ปี 2024 และโตเป็น standard ของ "agent ↔ tool" ระหว่างปีที่ผ่านมา (97M downloads/month, 9,400+ public servers) แต่ MCP ออกแบบให้ agent เชื่อมเข้า tool ของ enterprise เป็นหลัก — ไม่ได้แก้ปัญหา "enterprise A อยากแชร์ tool/skill ให้ enterprise B โดยที่ data ไม่ leave A" OpenSharing เติม layer ที่ MCP ไม่ทำ: cross-org skill distribution + zero-copy ทำให้ทั้งสอง protocol น่าจะอยู่ด้วยกัน MCP สำหรับ agent ↔ tool, OpenSharing สำหรับ org ↔ org

Pattern ใหญ่กว่าคือ **open protocol wars** ที่กำลังเกิด — MCP (Anthropic + community), A2A (Google + Linux Foundation, รวม ACP เข้าแล้ว), OpenSharing (Databricks + Linux Foundation) ทั้งสามตัวอยู่ภายใต้ Linux Foundation governance ส่งสัญญาณว่า hyperscaler/vendor หลักไม่อยากให้ใครคนใดคนหนึ่งคุม layer integration ของ agent era — บทเรียนจาก HTTP/HTTPS ที่ไม่ผูกกับ vendor ทำให้ web flourish, ตอนนี้ทุกคนพยายาม replicate model เดียวกันให้ AI layer ที่ Linux Foundation governance + open spec

Databricks เลือก timing สวย — ประกาศพร้อมกับ Summit ที่ Anthropic/OpenAI ส่ง session มาเอง = neutrality message เด่นว่า **OpenSharing ไม่ใช่ proprietary protocol ของ Databricks** ถ้าทำสำเร็จจะกลายเป็น HTTP ของ agent skill distribution — ที่ทุก SaaS vendor ต้อง expose skill ของตัวเองผ่าน เพราะเป็น standard ที่ลูกค้าต้องการ Snowflake, Microsoft Fabric (ที่เพิ่งประกาศ Rayfin ที่ Build 2026) จะต้องเลือกข้าง support หรือเปิด protocol ของตัวเองแข่ง

## มุม OpenBridge

นี่คือ **ข่าวที่ตรงกับ thesis ของ OpenBridge ที่สุดในรอบนี้** — OpenSharing คือ infrastructure layer ที่ enterprise A แชร์ tool/skill/data ให้ enterprise B โดยที่ data ไม่ออกจาก A — เป็น exact pain point ที่ B2B integration platform แก้มาตลอด 20 ปี (EDI, API gateway, iPaaS) แต่ตอนนี้ scope ขยายไปยัง agent skill + ML model OpenBridge ถ้าทำ implementation ของ OpenSharing protocol ตั้งแต่วันแรก จะกินตำแหน่ง "first OpenSharing-native integration platform" ก่อนที่ Workato, MuleSoft, Boomi จะ react

ที่สำคัญกว่า protocol คือ **distribution layer** — OpenSharing เป็น spec, ไม่ใช่ marketplace ใครก็ตามที่ build "Hugging Face ของ agent skill" บน OpenSharing — discovery + ranking + reviews + billing — จะเป็น winner ขั้นต่อไป Databricks มี Marketplace ของตัวเองแล้ว แต่ผูกกับ Databricks platform OpenBridge มี opportunity build neutral marketplace ที่ enterprise พ้อม skill provider/consumer ลง list + transact โดยใช้ OpenSharing protocol underlying — vertical marketplace สำหรับ banking/insurance/manufacturing น่าจะ scope แรกที่ทำได้

คำเตือน: OpenSharing ยังเป็น GA วันแรก spec อาจจะเปลี่ยน 6-12 เดือนข้างหน้า ลงทุน implementation ตอนนี้คือ bet ว่า Databricks + Linux Foundation จะ steward protocol ให้ stable — ดู A2A และ MCP roadmap pattern เป็น reference จะรู้ว่า Linux Foundation governance ทำงานเร็วและตอบสนอง feedback ดี risk acceptable ถ้า OpenBridge join governance committee ตั้งแต่ต้น เพื่อ shape protocol ให้ตรงกับ integration use case ของลูกค้า enterprise

## Sources
- [Databricks Announces OpenSharing, a New Open Standard for Sharing of Data and AI Assets Across Platforms and Organizations — Databricks](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing)
- [Linux Foundation Announces OpenSharing Project to Standardize AI Asset and Data Exchange — Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-opensharing-project-to-standardize-ai-asset-and-data-exchange)
- [Announcing New OpenSharing and Marketplace capabilities for the AI era — Databricks Blog](https://www.databricks.com/blog/announcing-new-opensharing-and-marketplace-capabilities-ai-era)
- [Databricks Summit 2026 Day 2: Agentic AI and Catalog Federation Move From Lab to Enterprise — TechTimes](https://www.techtimes.com/articles/318450/20260616/databricks-summit-2026-day-2-agentic-ai-catalog-federation-move-lab-enterprise.htm)
- [AI governance at Data + AI Summit 2026: What's new with Unity AI Gateway — Databricks Blog](https://www.databricks.com/blog/ai-governance-data-ai-summit-2026-whats-new-unity-ai-gateway)

---

## Audio script

ข่าวที่สอง Databricks เปิด protocol ใหม่ชื่อ OpenSharing ในงาน Data and AI Summit ที่ San Francisco วันที่สิบหก มิถุนายน ร่วมกับ Linux Foundation จะทำหน้าที่ governance protocol นี้เปิดให้ enterprise แชร์ agent skill model artifact และ unstructured data ข้าม org ข้าม platform โดย zero copy ต่อยอดจาก Delta Sharing ที่ Databricks contribute ปี 2021 และกลายเป็น standard ของ data warehouse แชร์กัน

vision ที่ Databricks บอกชัดมาก — data sharing แค่จุดเริ่มต้น คลื่นต่อไปคือ share intelligence ไม่ใช่ share data รัน app ตรงที่ data อยู่ ไม่ใช่ย้าย data มา app ตัวอย่าง use case — บริษัท data provider แชร์ proprietary agent skill ให้ลูกค้า แทนที่ลูกค้าต้อง copy file ทุกครั้งที่ update ใช้ standard API เรียกใช้ตรงที่ source

นี่คือ direct response ต่อ MCP ของ Anthropic ที่โต 97 ล้าน download ต่อเดือน MCP ทำเรื่อง agent คุย tool ภายใน org เดียวกัน OpenSharing ทำเรื่อง org ถึง org cross boundary ทั้งสอง protocol น่าจะอยู่ด้วยกัน MCP สำหรับ agent คุย tool OpenSharing สำหรับ org แชร์กัน pattern ใหญ่คือ open protocol wars Linux Foundation รับ governance ของ MCP A2A และ OpenSharing พร้อมกัน hyperscaler ทุกเจ้าไม่อยากให้ใคร dominant การ integration layer

สำหรับ OpenBridge นี่คือข่าวที่ตรงกับ thesis ที่สุดในรอบนี้ OpenSharing คือ infrastructure ที่ B2B integration platform แก้ปวด head มาสี่สิบปี OpenBridge ถ้า implement OpenSharing protocol วันแรก จะเป็น first OpenSharing native integration platform ก่อน Workato MuleSoft Boomi react opportunity ใหญ่กว่าคือ build neutral marketplace ของ agent skill บน OpenSharing เหมือน Hugging Face แต่สำหรับ enterprise skill ไม่ใช่ model
