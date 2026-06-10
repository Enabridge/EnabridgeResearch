#!/usr/bin/env python3
"""
OpenAI TTS variant of scripts/tts.py — used by the remote Code routine
(cloud), which has OPENAI_API_KEY but no GCP credentials.

Drop-in replacement: same CLI (--slug), same output contract
(audio/{slug}.mp3 + audio/{slug}.json + audio/{slug}.txt). The metadata
JSON is compatible with update_index.py.

Mac-side Cowork task continues to use tts.py (Google Chirp 3 HD).

Usage:
    python3 scripts/tts_openai.py --slug 26-06-04-0609
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    sys.exit("ต้อง: pip install openai")


ROOT = Path(__file__).resolve().parent.parent


def extract_audio_script(md_text: str) -> str | None:
    m = re.search(r"##\s*Audio script\s*\n+(.*?)(?=\n##\s|\Z)", md_text, re.DOTALL)
    if not m:
        return None
    return m.group(1).strip()


def extract_title(md_text: str) -> str:
    m = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    return m.group(1).strip() if m else "(no title)"


def parse_slug(slug: str) -> tuple[str, str, str]:
    parts = slug.split("-")
    if len(parts) != 4 or len(parts[3]) != 4:
        raise ValueError(f"slug must be YY-MM-DD-HHMM, got: {slug}")
    yy, mm, dd, hhmm = parts
    hh, mi = hhmm[:2], hhmm[2:]
    iso_date = f"20{yy}-{mm}-{dd}T{hh}:{mi}:00+07:00"
    dt = datetime.strptime(f"20{yy}-{mm}-{dd} {hh}:{mi}", "%Y-%m-%d %H:%M")
    human_intro = f"{dt.strftime('%d %B %Y')} เวลา {hh}:{mi}"
    title_suffix = f"{yy}-{mm}-{dd} {hh}:{mi}"
    return iso_date, human_intro, title_suffix


def build_daily_script(slug: str) -> tuple[str, list[dict], str, str]:
    news_dir = ROOT / "news"
    briefs = sorted(
        p for p in news_dir.glob(f"{slug}-*.md")
        if not p.name.endswith("-index.md")
    )
    if not briefs:
        sys.exit(f"ไม่เจอ brief สำหรับ {slug} ใน {news_dir}")

    iso_date, intro_label, title_suffix = parse_slug(slug)

    thai_ordinals = ["แรก", "ที่สอง", "ที่สาม", "ที่สี่", "ที่ห้า",
                     "ที่หก", "ที่เจ็ด", "ที่แปด", "ที่เก้า", "ที่สิบ"]

    parts = [
        f"สวัสดีครับ นี่คือ Enabridge AI Brief รอบ {intro_label} ครับ.",
        f"รอบนี้มี {len(briefs)} เรื่อง เน้น Agentic AI, business use case, และ trend ที่เอามาใช้กับ OpenBridge ได้.",
        "",
    ]
    items = []
    for i, brief_path in enumerate(briefs, 1):
        md = brief_path.read_text(encoding="utf-8")
        script = extract_audio_script(md)
        title = extract_title(md)
        if not script:
            print(f"[warn] {brief_path.name} ไม่มี '## Audio script' — ข้าม")
            continue
        ordinal = thai_ordinals[i - 1] if i <= len(thai_ordinals) else f"ที่ {i}"
        parts.append(f"เรื่อง{ordinal}.")
        if script and script[-1] not in ".!?":
            script = script + "."
        parts.append(script)
        parts.append("")
        items.append({"file": brief_path.name, "title": title, "order": i})

    parts.append("ทั้งหมดนี้คือ brief ของรอบนี้. ขอให้วันนี้เป็นวันที่ดีครับ. แล้วเจอกันรอบหน้า.")
    return "\n".join(parts), items, iso_date, title_suffix


# OpenAI TTS limit ~4096 chars per request. Stay safely under to give
# headroom for combined-character expansion in some edge cases.
CHUNK_CHARS = 3500


def split_into_chunks(text: str, max_chars: int = CHUNK_CHARS) -> list[str]:
    """Split text at sentence/paragraph boundaries so each chunk ≤ max_chars."""
    if len(text) <= max_chars:
        return [text]
    # Prefer paragraph breaks, then sentence terminators
    paragraphs = text.split("\n\n")
    chunks: list[str] = []
    buf = ""
    for p in paragraphs:
        if len(buf) + len(p) + 2 <= max_chars:
            buf = (buf + "\n\n" + p) if buf else p
            continue
        if buf:
            chunks.append(buf)
            buf = ""
        # paragraph itself too long — split by sentence
        if len(p) <= max_chars:
            buf = p
            continue
        sentences = re.split(r"(?<=[.!?])\s+", p)
        for s in sentences:
            if len(buf) + len(s) + 1 <= max_chars:
                buf = (buf + " " + s) if buf else s
            else:
                if buf:
                    chunks.append(buf)
                buf = s
    if buf:
        chunks.append(buf)
    return chunks


def generate_audio(text: str, out_path: Path, voice: str, model: str,
                   instructions: str | None, speed: float) -> None:
    client = OpenAI()
    chunks = split_into_chunks(text)
    print(f"[tts] {len(chunks)} chunk(s), voice={voice}, model={model}, speed={speed}x")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        for i, chunk in enumerate(chunks, 1):
            print(f"[tts] chunk {i}/{len(chunks)} ({len(chunk)} chars)")
            params: dict = {
                "model": model,
                "voice": voice,
                "input": chunk,
                "response_format": "mp3",
            }
            # gpt-4o-mini-tts: speed via instructions (no numeric speed param)
            # tts-1 / tts-1-hd: numeric `speed` param (0.25–4.0)
            if model == "gpt-4o-mini-tts":
                if instructions:
                    instr = instructions
                    if speed and abs(speed - 1.0) > 0.01:
                        pct = int(round((speed - 1.0) * 100))
                        if pct > 0:
                            instr = instr + f" พูดเร็วกว่าปกติประมาณ {pct} เปอร์เซ็นต์."
                        else:
                            instr = instr + f" พูดช้ากว่าปกติประมาณ {abs(pct)} เปอร์เซ็นต์."
                    params["instructions"] = instr
            else:
                if speed and abs(speed - 1.0) > 0.01:
                    params["speed"] = speed
            with client.audio.speech.with_streaming_response.create(**params) as r:
                for audio_bytes in r.iter_bytes():
                    f.write(audio_bytes)
    print(f"[tts] wrote {out_path} ({out_path.stat().st_size // 1024} KB)")


THAI_INSTRUCTIONS = (
    "พูดภาษาไทยให้เป็นธรรมชาติ น้ำเสียงผู้ประกาศข่าวเศรษฐกิจ-เทคโนโลยี "
    "ที่ให้ข้อมูลกระชับ ชัดเจน เป็นมิตร ไม่ดราม่า อ่านตัวเลขและศัพท์อังกฤษ "
    "(เช่น Anthropic, MCP, agentic) ให้ออกเสียงถูกแบบที่คนไอทีไทยอ่านจริง."
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True,
                    help="Timestamp slug YY-MM-DD-HHMM (e.g. 26-06-04-0609)")
    ap.add_argument("--voice", default="sage",
                    help="OpenAI TTS voice (default: sage — works decently for Thai)")
    ap.add_argument("--model", default="tts-1-hd",
                    help="OpenAI TTS model (default: tts-1-hd — explicit numeric speed control. "
                         "alt: gpt-4o-mini-tts has better voice steering but doesn't honor speed reliably)")
    ap.add_argument("--speed", type=float, default=1.3,
                    help="Speech speed multiplier (default 1.3 = +30%%, matches Mac Cowork). "
                         "For gpt-4o-mini-tts speed is steered via instructions; "
                         "for tts-1/tts-1-hd it's the numeric API `speed` param (0.25–4.0).")
    ap.add_argument("--dry-run", action="store_true",
                    help="Build + save script only, skip API call")
    args = ap.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("ไม่เจอ OPENAI_API_KEY ใน env")

    script, items, iso_date, title_suffix = build_daily_script(args.slug)
    audio_dir = ROOT / "audio"
    audio_dir.mkdir(exist_ok=True)

    script_path = audio_dir / f"{args.slug}.txt"
    script_path.write_text(script, encoding="utf-8")
    print(f"[tts] script → {script_path} ({len(script)} chars)")

    out_mp3 = audio_dir / f"{args.slug}.mp3"
    if not args.dry_run:
        generate_audio(script, out_mp3, args.voice, args.model, THAI_INSTRUCTIONS, args.speed)

    meta = {
        "date": args.slug,
        "iso_date": iso_date,
        "title": f"Daily AI Brief — {title_suffix}",
        "items": items,
        "script_char_count": len(script),
        "audio_file": out_mp3.name,
        "voice": args.voice,
        "model": f"openai-{args.model}",
        "speed": args.speed,
    }
    meta_path = audio_dir / f"{args.slug}.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[tts] meta → {meta_path}")


if __name__ == "__main__":
    main()
