---
date: 2026-04-18
slug: cloudflare-code-mode-mcp
topic: agentic-ai
reading_time_min: 2
sources: 1
---

# Cloudflare ลด token ของ MCP ลง 99.9% — จาก 1.17M เหลือ ~1,000

## TL;DR
- Cloudflare เปิด **Code Mode MCP server** ให้ agent เรียก API ผ่านโค้ดแทนการ dump tool spec เข้า context
- 2,500+ endpoint ที่เคยกิน ~1.17M tokens ตอนนี้เหลือ ~1,000 tokens — ลดลง 99.9%
- เปลี่ยนวิธีคิดเรื่องให้ agent เข้าถึง API ขนาดใหญ่ แบบประหยัดและปลอดภัยขึ้น

## เกิดอะไรขึ้น
Cloudflare เปิดตัว MCP server ตัวใหม่ชื่อ **Code Mode** เมษา 2026 แทนที่จะยัด tool schema ทุกตัวเข้า context window ให้ LLM อ่าน (ซึ่งกิน token มหาศาลเมื่อ API มี endpoint เยอะ) Code Mode ให้ agent เขียน code สั้น ๆ เรียก API แทน

ตัวเลขที่ Cloudflare เคลม: 2,500+ API endpoint ที่ทำงานด้วย MCP แบบเดิมกิน **1,170,000 tokens** ต่อ session — Code Mode ลดเหลือ **~1,000 tokens** เท่ากับ 99.9%

ทำงานใน sandbox แยก ให้ agent execute code ได้อย่างมี isolation ไม่กระทบระบบหลัก

## ทำไมสำคัญ
Pattern นี้ตอบโจทย์ปัญหา "context explosion" ที่ทีมหลายคนเจอตอน agent ต้องคุยกับ API enterprise-scale — เป็นครั้งแรกที่มี infrastructure-level solution ออกจาก vendor ใหญ่

ถ้า pattern นี้กลายเป็น standard (คาดว่าจะโดน copy ภายใน 2–3 เดือน) agent-to-API integration จะถูกและเร็วขึ้นมาก — ลด barrier ของการเอา agent ไปคุย SaaS/ERP/legacy system

## มุม OpenBridge
- ถ้า OpenBridge แตะ integration layer / agent connector ตัวนี้เป็น blueprint ที่ควรศึกษา — "code-as-tool" vs "tool-as-spec"
- ทดสอบดูว่า pattern เดียวกันใช้ได้กับ connector เราไหม — ถ้าใช่ marketing angle "agent-ready, token-efficient" ขายได้ทันที

## Sources
- [Cloudflare Launches Code Mode MCP Server to Optimize Token Usage for AI Agents — InfoQ](https://www.infoq.com/news/2026/04/cloudflare-code-mode-mcp-server/)

---

## Audio script
เรื่องแรกของวันนี้ Cloudflare เปิด MCP server ตัวใหม่ชื่อ Code Mode ประเด็นคือ แต่เดิมเวลาเราให้ agent คุยกับ API ที่มี endpoint เยอะ ๆ มันต้องยัด tool spec ทุกตัวเข้า context กิน token มหาศาล Cloudflare บอกว่า 2,500 endpoint เดิมกินหนึ่งล้านกว่า token ตอนนี้ Code Mode ลดเหลือพันเดียว คือหายไป 99.9% วิธีคือให้ agent เขียน code สั้น ๆ เรียก API แทนการอ่าน spec ทั้งก้อน รันใน sandbox แยก สำหรับทีม OpenBridge ผมว่าน่าจับตา เพราะถ้า pattern นี้กลายเป็น standard เร็ว ๆ นี้ การต่อ agent กับ SaaS enterprise จะถูกและเร็วขึ้นมาก คุ้มที่ทดสอบดูว่าเอาแนวคิด code-as-tool มาใช้กับ connector เราได้ไหม
