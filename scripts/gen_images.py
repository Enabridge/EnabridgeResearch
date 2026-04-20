#!/usr/bin/env python3
"""
Generate hero images for briefs via OpenAI DALL-E 3.

For each news/YY-MM-DD-HHMM-*.md (excluding -index):
  - Parse frontmatter
  - If `image:` is already filled → skip
  - If `image_prompt:` exists → call DALL-E, save PNG to news/images/,
    rewrite frontmatter with `image: images/<filename>.png`

Usage:
    python3 scripts/gen_images.py --slug 26-04-19-0700
    python3 scripts/gen_images.py --slug 26-04-19-0700 --size 1024x1024 --quality standard
"""
import argparse
import os
import re
import sys
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    sys.exit("ต้อง: pip install openai --break-system-packages")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # GHA จะ inject env vars ผ่าน workflow อยู่แล้ว — .env ไม่จำเป็น

try:
    import requests
except ImportError:
    sys.exit("ต้อง: pip install requests --break-system-packages")


ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = ROOT / "news"
IMAGES_DIR = NEWS_DIR / "images"


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(md: str) -> tuple[dict, str, str]:
    """Return (frontmatter_dict, frontmatter_block_raw, body)."""
    m = FRONTMATTER_RE.match(md)
    if not m:
        return {}, "", md
    fm_text = m.group(1)
    fm = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, m.group(0), md[m.end():]


def upsert_frontmatter_line(fm_block: str, key: str, value: str) -> str:
    """Set frontmatter key=value, either replacing or appending before the closing ---."""
    # [ \t]* keeps the match on one line. \s* previously swallowed the newline
    # after "image:" so the value landed on the next line (invalid YAML).
    pattern = re.compile(rf"^{re.escape(key)}:[ \t]*.*$", re.MULTILINE)
    if pattern.search(fm_block):
        return pattern.sub(f"{key}: {value}", fm_block)
    # Insert before the closing ---
    return fm_block.replace("\n---\n", f"\n{key}: {value}\n---\n", 1)


def sanitize_prompt(prompt: str) -> str:
    """Strip quote wrappers + enforce editorial illustration style."""
    p = prompt.strip().strip('"').strip("'")
    # Hard append style guard — protects against prompts that wandered into photo-realistic people
    style_tail = (
        "Editorial illustration, flat vector shapes, no text, no logos, no human faces, "
        "muted palette of slate blue #8caaee, coral #f2cdcd, teal #94e2d5, soft cream #f5e0dc, "
        "dark background #11111b."
    )
    return f"{p}. {style_tail}"


def generate_one(client: OpenAI, prompt: str, size: str, quality: str) -> bytes:
    resp = client.images.generate(
        model="dall-e-3",
        prompt=sanitize_prompt(prompt),
        size=size,
        quality=quality,
        n=1,
    )
    img_url = resp.data[0].url
    r = requests.get(img_url, timeout=30)
    r.raise_for_status()
    return r.content


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True,
                    help="Timestamp slug YY-MM-DD-HHMM (e.g. 26-04-19-0700)")
    ap.add_argument("--size", default="1024x1024",
                    choices=["1024x1024", "1792x1024", "1024x1792"])
    ap.add_argument("--quality", default="standard", choices=["standard", "hd"],
                    help="standard=$0.04, hd=$0.08 per image (DALL-E 3)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    briefs = sorted(
        p for p in NEWS_DIR.glob(f"{args.slug}-*.md")
        if not p.name.endswith("-index.md")
    )
    if not briefs:
        sys.exit(f"[images] ไม่เจอ brief สำหรับ {args.slug}")

    for brief_path in briefs:
        md = brief_path.read_text(encoding="utf-8")
        fm, fm_block, body = parse_frontmatter(md)

        if fm.get("image"):
            print(f"[images] {brief_path.name}: มี image อยู่แล้ว — ข้าม")
            continue

        prompt = fm.get("image_prompt")
        if not prompt:
            print(f"[images] {brief_path.name}: ไม่มี image_prompt — ข้าม")
            continue

        # slug ของ brief: YY-MM-DD-NNN-slug → ใช้ทั้งชื่อเป็น filename ของรูป
        image_filename = f"{brief_path.stem}.png"
        image_path = IMAGES_DIR / image_filename

        if args.dry_run:
            print(f"[images] DRY RUN: would gen {image_filename} with prompt: {prompt[:80]}...")
            continue

        print(f"[images] {brief_path.name}: gen → {image_filename}")
        try:
            data = generate_one(client, prompt, args.size, args.quality)
        except Exception as e:
            print(f"[images] FAIL {brief_path.name}: {e}")
            continue

        image_path.write_bytes(data)
        print(f"[images] wrote {image_path} ({len(data) // 1024} KB)")

        # Update frontmatter
        rel = f"images/{image_filename}"
        new_fm_block = upsert_frontmatter_line(fm_block, "image", rel)
        brief_path.write_text(new_fm_block + body, encoding="utf-8")
        print(f"[images] updated frontmatter: image: {rel}")

    print(f"[images] done for {args.slug}")


if __name__ == "__main__":
    main()
