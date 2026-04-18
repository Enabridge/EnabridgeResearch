#!/usr/bin/env python3
"""
Rebuild audio/index.json — the single source of truth the podcast feed reads.

Scans audio/*.json (per-episode metadata written by tts.py), enriches each
entry with the MP3 file size, and writes audio/index.json sorted newest first.

The enabridge-site feed fetches this one file from raw.githubusercontent.com —
so we avoid hitting the GitHub contents API (which has a 60 req/hr
unauthenticated rate limit) every time the feed rebuilds.

Usage:
    python3 scripts/update_index.py
"""
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = ROOT / "audio"
INDEX_PATH = AUDIO_DIR / "index.json"


def build_description(items: list[dict]) -> str:
    if not items:
        return ""
    lines = [f"{i['order']}. {i['title']}" for i in items]
    return "\n".join(lines)


def main() -> None:
    episodes = []
    for meta_path in sorted(AUDIO_DIR.glob("*.json")):
        if meta_path.name == "index.json":
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"[index] skip {meta_path.name}: {e}")
            continue

        audio_file = meta.get("audio_file")
        if not audio_file:
            print(f"[index] skip {meta_path.name}: no audio_file field")
            continue

        mp3_path = AUDIO_DIR / audio_file
        if not mp3_path.exists():
            print(f"[index] skip {meta_path.name}: mp3 missing ({audio_file})")
            continue

        episodes.append({
            "date": meta["date"],
            "iso_date": meta["iso_date"],
            "title": meta["title"],
            "description": build_description(meta.get("items", [])),
            "items": meta.get("items", []),
            "audio_file": audio_file,
            "audio_size_bytes": mp3_path.stat().st_size,
            "voice": meta.get("voice"),
            "model": meta.get("model"),
            "speed": meta.get("speed"),
            "script_char_count": meta.get("script_char_count"),
        })

    # Newest first (ISO date sorts correctly as string)
    episodes.sort(key=lambda e: e["iso_date"], reverse=True)

    index = {
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(episodes),
        "episodes": episodes,
    }

    AUDIO_DIR.mkdir(exist_ok=True)
    INDEX_PATH.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[index] wrote {INDEX_PATH} ({len(episodes)} episode(s))")


if __name__ == "__main__":
    main()
