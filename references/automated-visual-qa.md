# Automated Visual QA

Use this before final handoff, after SVG preview rendering and before or after PPTX export.

Automated checks do not replace human design judgment. They catch structural risks that commonly make decks feel weak: image-only pages, tiny text, repeated card grids, unsafe backgrounds, approximate text overlaps, and missing editable text.

## Required Script

Run:

```bash
python3 <skill_dir>/scripts/deck_visual_lint.py <project_path>
```

If preview PNGs are in a nonstandard folder:

```bash
python3 <skill_dir>/scripts/deck_visual_lint.py <project_path> --preview-dir <preview_png_dir>
```

Write the findings into `qa_report.md` under `Automated Visual Lint`.

## What It Checks

SVG-level:

- page count
- text count and editable text risk
- image count and image-only slide risk
- tiny font sizes
- approximate text bounding-box collisions
- text outside canvas
- forbidden or fragile SVG features
- repeated dense card-grid patterns

PNG-level when previews are available:

- average brightness
- contrast
- edge/detail intensity
- possible over-bright or over-busy backgrounds

Deck-level:

- too many pages with similar card-heavy structure
- too many image-heavy pages
- too many text-heavy pages
- lack of visual rhythm

## How To Interpret

Treat `ERROR` as blocking.

Treat `WARN` as a required review item:

- fix it when the issue is real
- mark it as accepted only when the deck's purpose justifies it, e.g. dense appendix pages

The script is conservative and best-effort. It cannot fully understand group transforms, complex typography, or the real semantic first-read. Always inspect the preview montage after running it.

## Common Fixes

| Finding | Likely Fix |
|---|---|
| low text count with images | rebuild title/labels natively; do not use full-slide screenshot |
| tiny font | split page, move detail to appendix, enlarge labels |
| possible overlap | adjust layout, line breaks, component spacing |
| bright/busy preview | darken background derivative, add safe-zone panel, simplify image |
| repeated card grid | reroute pages through `visual-form-router.md` |
| too many image-heavy pages | keep images for cover/anchors; use native exhibits for proof pages |

## Human Follow-Up

After the script, inspect:

- 25% montage first-read
- page rhythm
- whether selected style archetype is visible
- whether each page's component matches the claim
- whether generated images are doing real work
- whether the final PPTX remains editable
