#!/usr/bin/env python3
"""Best-effort visual lint for future-ppt SVG decks.

This script intentionally uses lightweight heuristics. It should surface
layout and rhythm risks for human review, not replace rendered QA.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageFilter, ImageStat
except Exception:  # pragma: no cover - optional dependency
    Image = None
    ImageFilter = None
    ImageStat = None


SVG_NS = "{http://www.w3.org/2000/svg}"


@dataclass
class Finding:
    level: str
    page: str
    code: str
    message: str


@dataclass
class PageStats:
    page: str
    text_count: int
    image_count: int
    rect_count: int
    path_count: int
    min_font: float | None
    max_font: float | None
    text_chars: int
    possible_overlaps: int
    avg_luma: float | None = None
    contrast: float | None = None
    edge_detail: float | None = None


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def parse_float(value: str | None) -> float | None:
    if not value:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", value)
    return float(match.group(0)) if match else None


def inherited_font_size(elem: ET.Element) -> float | None:
    value = elem.get("font-size") or elem.attrib.get("style", "")
    if "font-size" in value and ";" in value:
        match = re.search(r"font-size\s*:\s*([0-9.]+)", value)
        return float(match.group(1)) if match else None
    return parse_float(elem.get("font-size"))


def text_content(elem: ET.Element) -> str:
    return "".join(elem.itertext()).strip()


def iter_svg_files(project: Path, svg_dir: Path | None) -> list[Path]:
    candidates: list[Path] = []
    if svg_dir:
        candidates.append(svg_dir)
    candidates.extend([project / "svg_final", project / "svg_output"])
    for candidate in candidates:
        if candidate.exists():
            files = sorted(candidate.glob("*.svg"))
            if files:
                return files
    return sorted(project.rglob("*.svg"))


def infer_preview_dirs(project: Path, preview_dir: Path | None) -> list[Path]:
    dirs: list[Path] = []
    if preview_dir:
        dirs.append(preview_dir)
    for name in (
        "png_final",
        "png_output",
        "previews",
        "preview",
        "rendered",
        "exports",
        "qa",
    ):
        dirs.append(project / name)
    return [d for d in dirs if d.exists()]


def find_preview(svg: Path, preview_dirs: list[Path]) -> Path | None:
    stems = {svg.stem, svg.stem.replace("slide_", ""), svg.stem.replace("page_", "")}
    pngs: list[Path] = []
    for directory in preview_dirs:
        pngs.extend(directory.glob("*.png"))
    for png in pngs:
        if png.stem in stems:
            return png
    page_num = re.search(r"(\d+)", svg.stem)
    if page_num:
        number = page_num.group(1).lstrip("0") or "0"
        for png in pngs:
            png_num = re.search(r"(\d+)", png.stem)
            if png_num and (png_num.group(1).lstrip("0") or "0") == number:
                return png
    return None


def preview_stats(path: Path) -> tuple[float, float, float] | tuple[None, None, None]:
    if Image is None or ImageStat is None or ImageFilter is None:
        return None, None, None
    try:
        image = Image.open(path).convert("L").resize((320, 180))
        stat = ImageStat.Stat(image)
        avg_luma = float(stat.mean[0])
        contrast = float(stat.stddev[0])
        edges = image.filter(ImageFilter.FIND_EDGES)
        edge_detail = float(ImageStat.Stat(edges).mean[0])
        return avg_luma, contrast, edge_detail
    except Exception:
        return None, None, None


def approx_text_boxes(text_elems: Iterable[ET.Element]) -> list[tuple[float, float, float, float, str]]:
    boxes: list[tuple[float, float, float, float, str]] = []
    for elem in text_elems:
        text = text_content(elem)
        if not text:
            continue
        x = parse_float(elem.get("x"))
        y = parse_float(elem.get("y"))
        font = inherited_font_size(elem) or 18.0
        if x is None or y is None:
            continue
        width = max(8.0, len(text) * font * 0.55)
        height = font * 1.25
        boxes.append((x, y - height, x + width, y + height * 0.25, text[:32]))
    return boxes


def count_overlaps(boxes: list[tuple[float, float, float, float, str]]) -> int:
    overlaps = 0
    for i, a in enumerate(boxes):
        ax1, ay1, ax2, ay2, _ = a
        area_a = max(0.0, ax2 - ax1) * max(0.0, ay2 - ay1)
        if area_a <= 0:
            continue
        for b in boxes[i + 1:]:
            bx1, by1, bx2, by2, _ = b
            ix1, iy1 = max(ax1, bx1), max(ay1, by1)
            ix2, iy2 = min(ax2, bx2), min(ay2, by2)
            inter = max(0.0, ix2 - ix1) * max(0.0, iy2 - iy1)
            if inter and inter / area_a > 0.18:
                overlaps += 1
    return overlaps


def lint_svg(svg: Path, preview_dirs: list[Path]) -> tuple[PageStats, list[Finding]]:
    findings: list[Finding] = []
    page = svg.stem
    try:
        root = ET.parse(svg).getroot()
    except ET.ParseError as exc:
        stats = PageStats(page, 0, 0, 0, 0, None, None, 0, 0)
        return stats, [Finding("ERROR", page, "svg_parse", f"cannot parse SVG: {exc}")]

    elems = list(root.iter())
    text_elems = [e for e in elems if local_name(e.tag) == "text"]
    image_count = sum(1 for e in elems if local_name(e.tag) == "image")
    rect_count = sum(1 for e in elems if local_name(e.tag) == "rect")
    path_count = sum(1 for e in elems if local_name(e.tag) == "path")
    texts = [text_content(e) for e in text_elems if text_content(e)]
    fonts = [inherited_font_size(e) for e in text_elems]
    fonts = [f for f in fonts if f is not None]
    boxes = approx_text_boxes(text_elems)
    overlaps = count_overlaps(boxes)

    preview = find_preview(svg, preview_dirs)
    avg_luma, contrast, edge_detail = preview_stats(preview) if preview else (None, None, None)

    stats = PageStats(
        page=page,
        text_count=len(texts),
        image_count=image_count,
        rect_count=rect_count,
        path_count=path_count,
        min_font=min(fonts) if fonts else None,
        max_font=max(fonts) if fonts else None,
        text_chars=sum(len(t) for t in texts),
        possible_overlaps=overlaps,
        avg_luma=avg_luma,
        contrast=contrast,
        edge_detail=edge_detail,
    )

    if len(texts) == 0:
        findings.append(Finding("ERROR", page, "no_text", "no SVG text elements found; final slide may be image-only"))
    elif image_count and len(texts) < 2:
        findings.append(Finding("WARN", page, "image_low_text", "image present with very little text; verify native title/labels exist"))

    if stats.max_font is not None and stats.max_font < 24:
        findings.append(Finding("WARN", page, "small_title", f"largest font is {stats.max_font:.1f}px; title may be too small"))
    if stats.min_font is not None and stats.min_font < 10:
        findings.append(Finding("WARN", page, "tiny_text", f"smallest font is {stats.min_font:.1f}px; likely unreadable in PPT"))
    if stats.text_chars > 900:
        findings.append(Finding("WARN", page, "text_heavy", f"{stats.text_chars} text characters; consider appendix or split page"))
    if overlaps:
        findings.append(Finding("WARN", page, "possible_overlap", f"{overlaps} approximate text overlaps detected"))

    for x1, y1, x2, y2, sample in boxes:
        if x1 < -5 or y1 < -5 or x2 > 1300 or y2 > 740:
            findings.append(Finding("WARN", page, "text_outside_canvas", f"text may exceed canvas: {sample!r}"))
            break

    fragile = []
    for elem in elems:
        name = local_name(elem.tag)
        if name in {"foreignObject", "style", "script", "animate", "animateTransform"}:
            fragile.append(name)
        if name == "g" and elem.get("opacity") is not None:
            fragile.append("g opacity")
    if fragile:
        findings.append(Finding("WARN", page, "fragile_svg", "fragile SVG features: " + ", ".join(sorted(set(fragile)))))

    if avg_luma is not None:
        if image_count and avg_luma > 92 and contrast > 54:
            findings.append(Finding("WARN", page, "bright_busy_preview", f"preview may be bright/busy: luma={avg_luma:.1f}, contrast={contrast:.1f}"))
        if image_count and edge_detail is not None and edge_detail > 26:
            findings.append(Finding("WARN", page, "busy_background", f"preview has high edge/detail intensity: {edge_detail:.1f}"))

    return stats, findings


def deck_level_findings(stats: list[PageStats]) -> list[Finding]:
    if not stats:
        return [Finding("ERROR", "deck", "no_svg", "no SVG files found")]
    findings: list[Finding] = []
    total = len(stats)
    image_heavy = sum(1 for s in stats if s.image_count > 0 and s.text_count < 5)
    card_heavy = sum(1 for s in stats if s.rect_count >= 8 and s.image_count == 0)
    text_heavy = sum(1 for s in stats if s.text_chars > 900)
    if image_heavy / total > 0.45:
        findings.append(Finding("WARN", "deck", "too_image_heavy", f"{image_heavy}/{total} pages are image-heavy; verify native information layer"))
    if card_heavy / total > 0.5:
        findings.append(Finding("WARN", "deck", "repeated_card_grid", f"{card_heavy}/{total} pages look card-heavy; check visual rhythm"))
    if text_heavy / total > 0.35:
        findings.append(Finding("WARN", "deck", "too_text_heavy", f"{text_heavy}/{total} pages exceed text density threshold"))
    font_maxes = [s.max_font for s in stats if s.max_font is not None]
    if font_maxes and statistics.median(font_maxes) < 30:
        findings.append(Finding("WARN", "deck", "low_type_hierarchy", f"median max font is {statistics.median(font_maxes):.1f}px"))
    return findings


def print_report(project: Path, stats: list[PageStats], findings: list[Finding]) -> None:
    errors = [f for f in findings if f.level == "ERROR"]
    warns = [f for f in findings if f.level == "WARN"]
    print(f"# Deck Visual Lint\n")
    print(f"project: {project}")
    print(f"pages_checked: {len(stats)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warns)}\n")
    print("| page | text | images | rects | paths | min_font | max_font | chars | overlaps | luma | contrast | edge |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for s in stats:
        def fmt(value: float | int | None) -> str:
            if value is None:
                return ""
            if isinstance(value, float):
                return f"{value:.1f}"
            return str(value)

        print(
            f"| {s.page} | {s.text_count} | {s.image_count} | {s.rect_count} | {s.path_count} | "
            f"{fmt(s.min_font)} | {fmt(s.max_font)} | {s.text_chars} | {s.possible_overlaps} | "
            f"{fmt(s.avg_luma)} | {fmt(s.contrast)} | {fmt(s.edge_detail)} |"
        )
    if findings:
        print("\n## Findings\n")
        for f in findings:
            print(f"- {f.level} `{f.code}` [{f.page}]: {f.message}")
    else:
        print("\nNo findings. Still inspect the rendered montage manually.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--svg-dir", type=Path)
    parser.add_argument("--preview-dir", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    project = args.project_path.resolve()
    if not project.exists():
        print(f"error: project path not found: {project}", file=sys.stderr)
        return 2

    svg_files = iter_svg_files(project, args.svg_dir)
    preview_dirs = infer_preview_dirs(project, args.preview_dir)
    all_stats: list[PageStats] = []
    all_findings: list[Finding] = []

    for svg in svg_files:
        stats, findings = lint_svg(svg, preview_dirs)
        all_stats.append(stats)
        all_findings.extend(findings)

    all_findings.extend(deck_level_findings(all_stats))
    print_report(project, all_stats, all_findings)

    if args.json_out:
        payload = {
            "project": str(project),
            "stats": [asdict(s) for s in all_stats],
            "findings": [asdict(f) for f in all_findings],
        }
        args.json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    return 1 if any(f.level == "ERROR" for f in all_findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
