---
date: 2026-05-20
slug: openai-erdos-conjecture-ai-math-proof
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A luminous chessboard-like plane covered in glowing dots connected by thin
  golden lines of exactly equal length, forming an intricate non-grid pattern
  that breaks out of a rigid square lattice. In the center, a large translucent
  AI brain silhouette hovers above the plane, projecting light beams that
  rearrange the dots into the new configuration. Bold text "80 YEARS SOLVED"
  is rendered in the upper third, with a small "Erdős 1946" label crossed out
  in red. The background is deep mathematical blackboard green with faint chalk
  equations. Style: scientific editorial illustration, high contrast, geometric
  precision, 1:1 aspect. No human faces — the AI is represented as an abstract
  glowing brain silhouette only.
image: images/26-05-24-0603-02-openai-erdos-conjecture-ai-math-proof.png
---

# OpenAI หักล้างข้อคาดการณ์ทางคณิตศาสตร์อายุ 80 ปี — ครั้งแรกที่ AI "คิดเอง" แล้วพิสูจน์ได้จริง

## TL;DR
- โมเดลภายในของ OpenAI หักล้าง (disprove) ข้อคาดการณ์ด้าน discrete geometry ของ Paul Erdős ที่ค้างมาตั้งแต่ปี 1946 — เป็น open problem กลาง ๆ ของสาขา ไม่ใช่ปัญหาชายขอบ
- โมเดลไม่ได้ถูก fine-tune สำหรับปัญหานี้ ไม่ได้ค้นหาคำตอบที่มีอยู่แล้ว และไม่มีมนุษย์ช่วยนำทาง — ได้รับโจทย์แล้วสร้าง proof ขึ้นมาเอง
- Fields medalist Tim Gowers เรียกว่า "milestone in AI mathematics" — proof ผ่านการตรวจสอบจากนักคณิตศาสตร์ภายนอกหลายคน

## เกิดอะไรขึ้น

เมื่อวันที่ 20 พฤษภาคม 2026 OpenAI ประกาศว่า internal reasoning model ของบริษัทสามารถหักล้าง conjecture สำคัญใน discrete geometry ได้อย่างอิสระ ปัญหาที่ว่าคือ planar unit distance problem ซึ่ง Paul Erdős — นักคณิตศาสตร์ชาวฮังการีผู้เป็นตำนาน — ตั้งไว้ตั้งแต่ปี 1946 โจทย์ถามว่า "ถ้ามี n จุดบนระนาบ จำนวนคู่ของจุดที่ห่างกันพอดี 1 หน่วยมากที่สุดได้เท่าไร?" มาเกือบ 80 ปี นักคณิตศาสตร์เชื่อว่า square grid เป็นคำตอบที่ดีที่สุด

โมเดลของ OpenAI พบ construction family แบบใหม่ที่เอาชนะ grid — และพิสูจน์มันทางคณิตศาสตร์ เครื่องมือหลักที่ proof ใช้มาจาก algebraic number theory โดยเฉพาะ infinite class field towers และทฤษฎีบท Golod-Shafarevich จากทศวรรษ 1960 ซึ่งเป็นเทคนิคที่ไม่มีใครเคยเอามาใช้กับปัญหา unit distance มาก่อน — นี่คือ creative leap ไม่ใช่ brute-force search

สิ่งที่ทำให้เรื่องนี้ต่างจาก AI math claims ที่ผ่านมาคือ — โมเดลไม่ได้ถูก train เฉพาะสำหรับปัญหานี้ ไม่ได้ retrieve solution ที่มีอยู่แล้ว และไม่มีมนุษย์ guide step-by-step มันได้รับ problem statement แล้วสร้าง proof ขึ้นมาเอง Proof ผ่านการตรวจสอบจากกลุ่มนักคณิตศาสตร์ภายนอก รวมถึง Noga Alon จาก Princeton ซึ่งเรียกปัญหานี้ว่า "one of Erdős's favorite problems" และ Thomas Bloom — คนเดียวกับที่เคยฉีก OpenAI math claim ครั้งก่อน — ก็ให้ supportive statement รอบนี้ Fields medalist Tim Gowers ถึงกับเรียกว่า "a milestone in AI mathematics"

## ทำไมสำคัญ

นี่ไม่ใช่ครั้งแรกที่ AI ช่วยทำคณิตศาสตร์ — DeepMind เคยใช้ AlphaProof แก้ปัญหา IMO ได้ แต่นั่นเป็น competition-level problems ที่มี solution อยู่แล้ว ไม่ใช่ open problems ที่ยังไม่มีใครแก้ได้ สิ่งที่ต่างคือ Erdős conjecture เป็น "central conjecture in a subfield" ที่นักคณิตศาสตร์ระดับ world-class พยายามแก้มานาน — และ AI ทำได้โดยไม่มีมนุษย์ช่วย

Pattern ที่เห็นคือ AI reasoning models กำลังเข้าสู่ phase ใหม่ — จาก "ช่วยมนุษย์ทำงาน" เป็น "ทำงานที่มนุษย์ยังทำไม่ได้" ซึ่งมี implication ทั้งสองด้าน: ฝั่ง optimist บอกว่านี่คือ proof point ของ AI ที่จะเร่ง scientific discovery; ฝั่ง cautious ก็ตั้งคำถามว่า ถ้า AI สามารถสร้าง proof ที่มนุษย์ตรวจสอบยาก ๆ ได้ เราจะ verify อย่างไรในระยะยาว ระวังว่า OpenAI เป็นทั้งผู้พัฒนาและผู้ announce — ต้องรอ peer review ที่สมบูรณ์กว่านี้ แม้ external check เบื้องต้นจะผ่าน

## มุม OpenBridge

ไม่ direct เกี่ยวกับ product ของ OpenBridge แต่ adjacent insight สำคัญคือ — ถ้า reasoning model สามารถแก้ปัญหาที่ต้องการ creative leap ในระดับนี้ได้ capability ของ AI agents ที่ทำงาน business workflow จะไม่หยุดอยู่แค่ "ทำ task ซ้ำ ๆ ตาม rule" อีกต่อไป ภายใน 12-18 เดือน agent ที่ OpenBridge orchestrate อาจต้อง handle tasks ที่ต้อง reasoning หลายขั้น ข้ามหลาย domain — ซึ่งเปลี่ยน value proposition จาก "automation" เป็น "augmented decision-making" ที่ pricing power สูงกว่ามาก

## Sources
- [An OpenAI model has disproved a central conjecture in discrete geometry — OpenAI](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)
- [OpenAI claims it solved an 80-year-old math problem — for real this time — TechCrunch](https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/)
- [OpenAI Reasoning Model Disproves 80-year-old Erdős Geometry Conjecture — Dataconomy](https://dataconomy.com/2026/05/21/openai-model-disproves-erdos-geometry-conjecture/)

---

## Audio script
เรื่องถัดมาเป็นเรื่องที่น่าตื่นเต้นมาก OpenAI ประกาศว่า reasoning model ภายในของบริษัทสามารถหักล้างข้อคาดการณ์ทางคณิตศาสตร์ที่ค้างมา 80 ปีได้ด้วยตัวเอง ปัญหาที่ว่าคือ planar unit distance problem ที่ Paul Erdős ตั้งไว้ตั้งแต่ปี 1946 ถามว่าถ้ามี n จุดบนระนาบ จะจัดให้มีคู่จุดที่ห่างกันพอดี 1 หน่วยได้มากที่สุดเท่าไร ตลอด 80 ปี นักคณิตศาสตร์เชื่อว่า square grid ดีที่สุด แต่โมเดลของ OpenAI เจอ construction แบบใหม่ที่เอาชนะ grid ได้ โดยใช้เทคนิคจาก algebraic number theory ที่ไม่เคยมีใครเอามาใช้กับปัญหานี้มาก่อน ที่สำคัญคือโมเดลไม่ได้ถูก train เฉพาะสำหรับปัญหานี้ ไม่ได้ค้นหาคำตอบที่มีอยู่แล้ว และไม่มีมนุษย์ช่วยนำทาง Fields medalist Tim Gowers เรียกว่า milestone in AI mathematics นี่อาจเป็นครั้งแรกที่ AI ทำสิ่งที่มนุษย์ยังทำไม่ได้ในทางคณิตศาสตร์จริง ๆ ไม่ใช่แค่ช่วยมนุษย์ทำเร็วขึ้นครับ
