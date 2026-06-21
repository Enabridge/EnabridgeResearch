---
date: 2026-06-21
slug: noam-shazeer-leaves-google-openai
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a single chess-like piece silhouette walking from a
  large glowing Google "G" cube on the left to a black OpenAI flower-logo cube
  on the right, leaving a glowing footprint trail. Massive bold text "Attention
  Is All You Need" arcs across the top in subtle ghosted style, with a smaller
  tag "10 years" pinned near the destination cube and "Architecture Research
  Lead" below it. Render style: cinematic editorial illustration, isometric
  perspective, cool blue lighting on left fading to warm amber on right,
  high-contrast typography legible at 200px thumbnail. No real human faces —
  silhouette only.
image: images/26-06-22-0602-02-noam-shazeer-leaves-google-openai.png
---

# Noam Shazeer ออกจาก Google ไป OpenAI — Transformer paper co-author ย้ายค่าย ลีดงาน "architecture research" ในยุคที่ทุก lab กำลังหาก้าวต่อจาก attention

## TL;DR
- 17 มิ.ย. Noam Shazeer — VP Engineering ของ Google, co-lead Gemini, co-author "Attention Is All You Need" — ประกาศย้ายไป OpenAI ในตำแหน่งหัวหน้า architecture research
- Sam Altman บอก "อยากชวน Shazeer ตั้งแต่ OpenAI ก่อตั้ง — ใช้เวลา 10 ปี" สื่อต่างประเทศมองเป็น signal ใหญ่ที่สุดของ "ตลาด talent ของ frontier AI ตอนนี้ราคาสูงเกินกว่าที่ Google รักษาคนได้"
- การเคลื่อนไหวเกิดน้อยกว่า 2 ปีหลัง Shazeer + Daniel De Freitas กลับเข้า DeepMind ในส.ค. 2024 หลัง Google ซื้อ Character.AI ในดีล ~$2.7B

## เกิดอะไรขึ้น

17 มิถุนายน Noam Shazeer ประกาศบน X ว่า "ตื่นเต้นที่จะแชร์ว่าผมจะไปร่วม OpenAI" — ข้อความสั้นๆ ไม่กี่บรรทัด แต่กระทบ industry ทั้งวงการในไม่กี่ชั่วโมง เพราะ Shazeer เป็น VP Engineering ของ Google, co-lead Gemini, และที่สำคัญที่สุดเป็น **co-author ของเปเปอร์ "Attention Is All You Need" ปี 2017** — เปเปอร์ที่เปิดตัว Transformer architecture ซึ่งเป็นพื้นฐานของ GPT, Claude, Gemini, Llama, Mistral ทุกตัวในวันนี้ คนที่ไม่ได้อยู่ใน AI deeply ก็จะคุ้นชื่อจาก Character.AI ที่เขาก่อตั้ง

OpenAI ออกประกาศแยกว่า Shazeer จะเข้ามาในตำแหน่ง **"lead for architecture research"** — focus ที่ "core structural blueprints to power future generations of AI" Sam Altman ส่ง message สาธารณะที่ฟังดู personal มากกว่า corporate ว่า "อยากทำงานกับ Shazeer ตั้งแต่ OpenAI ก่อตั้งช่วงต้นๆ" และแซวว่า "ใช้เวลา 10 ปี" เพื่อให้สิ่งนี้เกิด ตอนนี้ยังไม่มีตัวเลข compensation package แต่ The Information และ CNBC รายงานว่า "อยู่ในช่วงสูงผิดปกติแม้ตามมาตรฐาน frontier talent"

การเคลื่อนไหวเกิดขึ้นน้อยกว่า 2 ปีหลัง Google ดึง Shazeer และ Daniel De Freitas (co-founder Character.AI) กลับเข้า DeepMind ในเดือนสิงหาคม 2024 ผ่านดีล acqui-hire + license ที่มูลค่ารวมประมาณ $2.7B (Google จ่ายค่า license ให้ Character.AI ใช้เทคโนโลยี LaMDA-derived เป็นค่าตอบแทน) ตอนนั้นมองกันว่าเป็น "Google ดึงผู้ก่อตั้ง Transformer กลับบ้าน" — กลับเข้ามาเป็นผู้นำ Gemini แทน รอบนี้ตรงข้าม Google กำลังขึ้น Gemini 3.5 Pro และเตรียมปล่อย Gemini 4 ใน Q4 ตามที่ Pichai บอกในงบ Q1 — การเสีย co-lead คนสำคัญในไตรมาสนี้คือ timing ที่แย่ที่สุด

ข่าวอีกข้างคือ **OpenAI** เพิ่งดึง Yi Tay (อดีต Brain → Reka founder) เข้าทีม research เดือนพ.ค., เพิ่ม Liam Fedus (ผู้ออกแบบ FLAN) ในตำแหน่ง model architecture, และตอนนี้ Shazeer — pattern ที่ชัดมากคือ OpenAI กำลังสะสมคนที่ "ออกแบบ architecture ใหม่หลัง Transformer" ไม่ใช่แค่ "scale Transformer ต่อ" ซึ่งสัมพันธ์กับคำพูดของ Altman ในงาน Stratechery interview เดือนพ.ค. ที่บอกว่า "GPT-6 จะไม่ใช่แค่ scale-up GPT-5 — มี architecture innovation ใหม่"

## ทำไมสำคัญ

Shazeer ไม่ใช่ "vice president ทั่วไป" — เขาเป็นหนึ่งใน **5 คนในโลก** ที่มี deep understanding ทั้งการสร้าง Transformer (2017) + การสร้าง chatbot ที่ retain user ระดับ consumer (Character.AI) + การ lead model training ระดับ flagship (Gemini) profile นี้หายากมากเพราะคน lab ส่วนใหญ่เก่งด้านใดด้านหนึ่ง การที่ Google ปล่อยเขาไปได้แปลว่า counter-offer ไม่ทันหรือไม่มี — ทั้งสองกรณีเป็น **signal ใหญ่ว่า OpenAI ออกของที่ Google แมตช์ไม่ได้** (น่าจะเป็น equity + autonomous research mandate ผสมกัน)

Pattern ที่น่าจับตาคือ "architecture research" ที่ OpenAI ตั้ง Shazeer ขึ้นเป็นหัวหน้า — คำนี้ไม่ใช่ "scaling research" แปลว่า Altman เชื่อว่า **gain ในรอบถัดไปจะมาจาก architecture ใหม่ ไม่ใช่ compute เพิ่ม** ซึ่งสำคัญกว่าที่ฟังดู เพราะถ้า OpenAI ถูก ราคาของ GPU จะ matter น้อยลงในการกำหนด leader (Anthropic, xAI ที่มี compute น้อยกว่าจะได้เปรียบหรือไม่ขึ้นกับว่า architecture leap จริงหรือไม่) ถ้าผิด การลงทุน infra ของ Microsoft + Oracle ที่ $500B+ จะยังเป็นที่ตั้งเดิม

ผลกระทบต่อ Google ลึกกว่าที่หน้าจอข่าวบอก — Demis Hassabis กับ Sergey Brin กำลังรีออร์กกองทัพ DeepMind อยู่แล้ว (ตามรายงาน The Information) และ Gemini 3.5 Pro ยัง pending launch การเสีย co-lead 1 คนใน flagship effort หมายความว่า roadmap อาจล่าช้า 1-2 quarter หรืออย่างน้อย Google ต้องตอบคำถามนักลงทุนเรื่องนี้ในการประชุมงบ Q2 ที่จะมาถึงในเดือนหน้า

## มุม OpenBridge

ไม่ direct เกี่ยวกับ OpenBridge เลย แต่มี adjacent insight ที่สำคัญ — **ถ้า architecture leap ของ OpenAI สำเร็จ ค่า inference จะลดลงเร็วกว่าที่ planning ตอนนี้** OpenBridge ที่ pricing model พึ่ง LLM call cost ต้อง model scenario ใหม่ว่า "ถ้า GPT-6 ราคา 1/10 ของ GPT-5 ที่ทำงาน equivalent quality, gross margin ของ product เราเปลี่ยนยังไง" — เป็น risk และ opportunity พร้อมกัน

Pattern ของ "ดึง co-author paper ของ field มาทำ architecture research" ก็เป็น signal ให้ startup คิดถึง **research talent ที่ position ตัวเองเป็น "individual contributor with autonomous mandate"** — model ที่ OpenAI ใช้แตกต่างจาก Google ที่มี hierarchy ใหญ่ ในยุคที่ talent หายาก, startup เล็กที่ให้ space + equity + decision authority จะดึงคนได้ที่ Google + Microsoft ดึงไม่ได้

สุดท้าย Shazeer เคยก่อตั้ง Character.AI — ที่ทำ chatbot retention level สูงที่สุดในตลาด consumer AI เคยมีรายงานว่า user spend > 2 ชั่วโมง/วันใน app ก่อน Google ซื้อ insight ที่ valuable คือ "agent ที่ลูกค้า OpenBridge ใช้ใน B2B context ก็ต้องมี retention loop ที่ดี" — ไม่ใช่แค่ technical correctness แต่เป็น UX ที่ทำให้ admin/ops ที่เลือกใช้ tool รู้สึกว่า "agent นี้คือเพื่อนร่วมงาน" ไม่ใช่ "command-line ที่บางครั้งเรียก"

## Sources
- [Google Gemini co-lead Noam Shazeer leaves for OpenAI — CNBC](https://www.cnbc.com/2026/06/18/google-gemini-co-lead-noam-shazeer-leaves-for-openai.html)
- [Gemini's co-lead is leaving Google to join OpenAI — 9to5Google](https://9to5google.com/2026/06/17/geminis-co-lead-is-leaving-google-to-join-openai/)
- [Noam Shazeer — Wikipedia](https://en.wikipedia.org/wiki/Noam_Shazeer)
- [Google VP Engineering Gemini Co-Lead Leaves For OpenAI — Yahoo Tech](https://tech.yahoo.com/ai/gemini/articles/google-vp-engineering-gemini-co-133051476.html)
- [Google's Noam Shazeer leaving organisation to join rival OpenAI — Silicon Republic](https://www.siliconrepublic.com/business/googles-noam-shazeer-leaving-organisation-join-rival-openai)

---

## Audio script
สวัสดีครับโยห์ ข่าวใหญ่ของวงการ AI วันนี้คือ Noam Shazeer ประกาศย้ายจาก Google ไป OpenAI Shazeer คือใคร เขาคือ co-author ของเปเปอร์ Attention Is All You Need ปี 2017 ที่เปิดตัว Transformer architecture พื้นฐานของ GPT Claude Gemini ทุกตัวในวันนี้ เป็น VP Engineering ของ Google และ co-lead ของ Gemini เพิ่งกลับเข้า Google ได้ไม่ถึงสองปี หลังจากที่ Google ซื้อ Character AI ของเขาในดีลมูลค่าประมาณ 2.7 พันล้านเหรียญ Sam Altman บอกว่าอยากชวน Shazeer ตั้งแต่ OpenAI ก่อตั้ง ใช้เวลา 10 ปี ตำแหน่งที่ Shazeer จะเข้ามาคือหัวหน้า architecture research โฟกัสเรื่อง core blueprint สำหรับ AI รุ่นถัดไป สำคัญตรงที่คำว่า architecture ไม่ใช่ scaling แปลว่า Altman เชื่อว่า gain รอบถัดไปมาจากการคิด architecture ใหม่ ไม่ใช่แค่เพิ่ม compute ถ้าถูก ราคา GPU จะ matter น้อยลงในการกำหนด leader ถ้าผิด infra spend ของ Microsoft กับ Oracle ที่ลงไปแล้วครึ่งล้านล้านดอลลาร์จะยังเป็นที่ตั้งเดิม สำหรับ OpenBridge มีสองมุม หนึ่ง ถ้า architecture leap สำเร็จจริง inference cost จะลดเร็วกว่า planning ตอนนี้ pricing model ของ product ที่พึ่ง LLM call ต้อง stress-test ใหม่ สอง Shazeer เคยทำ Character AI ที่ retention level สูงที่สุดในตลาด consumer AI insight นั้นใช้กับ B2B agent ได้ครับ
