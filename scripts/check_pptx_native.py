#!/usr/bin/env python3
"""Check whether a PPTX appears to contain editable native slide content."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_pptx_native.py <deck.pptx>", file=sys.stderr)
        return 2

    pptx = Path(sys.argv[1])
    if not pptx.exists():
        print(f"error: file not found: {pptx}", file=sys.stderr)
        return 2

    with zipfile.ZipFile(pptx) as zf:
        names = zf.namelist()
        media = [name for name in names if name.startswith("ppt/media/")]
        slides = sorted(
            name for name in names
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
        )
        print(f"deck: {pptx}")
        print(f"slides: {len(slides)}")
        print(f"media_count: {len(media)}")
        if media:
            for name in media[:20]:
                print(f"media: {name}")
            if len(media) > 20:
                print(f"media: ... {len(media) - 20} more")

        total_text_runs = 0
        for index, slide in enumerate(slides, 1):
            xml = zf.read(slide).decode("utf-8", errors="ignore")
            text_runs = re.findall(r"<a:t>(.*?)</a:t>", xml)
            total_text_runs += len(text_runs)
            sample = " | ".join(text_runs[:4])
            print(f"slide {index}: text_runs={len(text_runs)} sample={sample}")

    if not slides:
        print("status: FAIL no slides found")
        return 1
    if total_text_runs == 0:
        print("status: WARN no editable text runs found")
        return 1
    print("status: PASS editable text runs found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
