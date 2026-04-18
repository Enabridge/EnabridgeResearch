#!/usr/bin/env python3
"""
Generate daily podcast audio from brief .md files using OpenAI TTS.

Usage:
    python scripts/tts.py --date 26-04-18
    python scripts/tts.py --date 26-04-18 --voice nova --model gpt-4o-mini-tts

Reads:  news/YY-MM-DD-NNN-*.md (excluding -index.md)
Writes: audio/YY-MM-DD.mp3 + audio/YY-MM-DD.json (metadata)
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
    sys.exit("ต้อง: pip install openai python-dotenv --break-system-packages")

try:
    from dotenv import load_dotenv
except ImportError:
    sys.exit("ต้อง: pip install python-dotenv --break-system-packages")


ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


def extract_audio_script(md_text: str) -> str | None:
    """Pull the content under '## Audio script' heading."""
    m = re.search(r"##\s*Audio script\s*\n+(.*?)(?=\n##\s|\Z)", md_text, re.DOTALL)
    if not m:
        return None
    return m.group(1).strip()


def extract_title(md_text: str) -> str:
    """Pull the first H1 as the title."""
    m = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    return m.group(1).strip() if m else "(no title)"


def build_daily_script(date_slug: str) -> tuple[str, list[dict]]:
    """Compose the full daily audio script and return (text, item_meta)."""
    news_dir = ROOT / "news"
    briefs = sorted(
        p for p in news_dir.glob(f"{date_slug}-*.md")
        if not p.name.endswith("-index.md")
    )
    if not briefs:
        sys.exit(f"ไม่เจอ brief สำหรับ {date_slug} ใน {news_dir}")

    # Parse human date for intro
    yy, mm, dd = date_slug.split("-")
    date_obj = datetime.strptime(f"20{yy}-{mm}-{dd}", "%Y-%m-%d")
    intro_date = date_obj.strftime("%d %B %Y")  # Thai readers still parse OK

    parts = [
        f"สวัสดีครับ นี่คือ Enabridge Daily AI Brief ของวันที่ {intro_date}",
        f"วันนี้มี {len(briefs)} เรื่อง เน้น Agentic AI, business use case, และ trend ที่เอามาใช้กับ OpenBridge ได้",
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
        parts.append(f"เรื่องที่ {i}")
        parts.append(script)
        parts.append("")
        items.append({
            "file": brief_path.name,
            "title": title,
            "order": i,
        })

    parts.append("ทั้งหมดนี้คือ brief ของวันนี้ ขอให้วันนี้เป็นวันที่ดีครับ แล้วเจอกันใหม่พรุ่งนี้")
    return "\n".join(parts), items


THAI_INSTRUCTIONS = (
    "Speak in natural Thai with a warm, professional tone — "
    "like a morning news anchor briefing a friend. "
    "Pronounce Thai words with correct tones and native rhythm. "
    "English technical terms (MCP, agentic, orchestration) keep in English, "
    "pronounced naturally within Thai sentences. "
    "Energetic brisk pace — about 30% faster than normal narration, "
    "but still clear enunciation with brief pauses between stories."
)


def generate_audio(text: str, out_path: Path, voice: str, model: str,
                   instructions: str | None = None,
                   speed: float = 1.0) -> None:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    # OpenAI TTS has a ~4096 char limit per call. Chunk if needed.
    MAX = 3800
    chunks = []
    remaining = text
    while remaining:
        if len(remaining) <= MAX:
            chunks.append(remaining)
            break
        cut = remaining.rfind("\n", 0, MAX)
        if cut < MAX // 2:
            cut = remaining.rfind(" ", 0, MAX)
        if cut < 0:
            cut = MAX
        chunks.append(remaining[:cut])
        remaining = remaining[cut:].lstrip()

    print(f"[tts] {len(chunks)} chunk(s), voice={voice}, model={model}, speed={speed}x")
    if instructions and model.startswith("gpt-4o"):
        print(f"[tts] instructions: {instructions[:80]}...")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        for i, chunk in enumerate(chunks, 1):
            print(f"[tts] chunk {i}/{len(chunks)} ({len(chunk)} chars)")
            kwargs = dict(
                model=model,
                voice=voice,
                input=chunk,
                response_format="mp3",
            )
            # gpt-4o-mini-tts and gpt-4o-tts accept an `instructions` param
            # for tone/accent guidance — older tts-1* models ignore it.
            if instructions and model.startswith("gpt-4o"):
                kwargs["instructions"] = instructions
            # `speed` is supported across all TTS models (0.25–4.0, default 1.0)
            if speed != 1.0:
                kwargs["speed"] = speed
            resp = client.audio.speech.create(**kwargs)
            f.write(resp.content)
    print(f"[tts] wrote {out_path} ({out_path.stat().st_size // 1024} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YY-MM-DD (e.g. 26-04-18)")
    ap.add_argument("--voice", default="coral",
                    help="alloy|ash|ballad|coral|echo|fable|nova|onyx|sage|shimmer|verse "
                         "(default: coral — warm, works well with Thai)")
    ap.add_argument("--model", default="gpt-4o-mini-tts",
                    help="gpt-4o-mini-tts (best multilingual, DEFAULT) | "
                         "gpt-4o-tts (best quality, pricier) | "
                         "tts-1-hd (older, worse Thai)")
    ap.add_argument("--instructions", default=THAI_INSTRUCTIONS,
                    help="Tone/style guidance (only used by gpt-4o-* models). Pass '' to disable.")
    ap.add_argument("--speed", type=float, default=1.3,
                    help="Speech speed 0.25–4.0 (default: 1.3 = 30%% faster than normal)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Build + save script only, skip API call")
    args = ap.parse_args()

    script, items = build_daily_script(args.date)
    audio_dir = ROOT / "audio"
    audio_dir.mkdir(exist_ok=True)

    # Always save the script text for debugging
    script_path = audio_dir / f"{args.date}.txt"
    script_path.write_text(script, encoding="utf-8")
    print(f"[tts] script → {script_path} ({len(script)} chars)")

    out_mp3 = audio_dir / f"{args.date}.mp3"
    if not args.dry_run:
        generate_audio(script, out_mp3, args.voice, args.model,
                       instructions=args.instructions or None,
                       speed=args.speed)

    # Metadata for RSS feed
    meta = {
        "date": args.date,
        "iso_date": datetime.strptime(f"20{args.date}", "%Y-%m-%d").strftime("%Y-%m-%dT07:00:00+07:00"),
        "title": f"Daily AI Brief — {args.date}",
        "items": items,
        "script_char_count": len(script),
        "audio_file": out_mp3.name,
        "voice": args.voice,
        "model": args.model,
        "speed": args.speed,
    }
    meta_path = audio_dir / f"{args.date}.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[tts] meta → {meta_path}")


if __name__ == "__main__":
    main()
