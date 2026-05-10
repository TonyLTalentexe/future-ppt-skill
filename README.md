# Future PPT Skill

`future-ppt` is a Codex skill for turning mature documents, reports, research notes, and strategy materials into **native editable PowerPoint decks**.

It is designed as a small PPT production system: first align the audience and decision context, then compile the narrative, route each page to the right visual form, generate SVG pages, lint the deck, and export a native PPTX through [`ppt-master`](https://github.com/hugohe3/ppt-master).

## What Is New In This Version

This iteration upgrades the original open-source skill from a basic document-to-slides workflow into a stronger presentation workflow:

- needs alignment before production
- rapid sample mode for quick 1-3 page direction previews
- claim / evidence / implication narrative compiler
- style archetype playbooks, including consulting, launch, IC, government, technical, operating review, and talent/research decks
- visual-form router
- reusable page component library
- image-first workflow for generated image assets without sacrificing information hierarchy
- automated visual lint script for SVG decks
- stronger QA rubric for editability, rhythm, layering, and generated assets

## Production Flow

```text
needs alignment
-> source import
-> narrative compiler
-> slide brief matrix + visual router
-> art direction + component plan
-> visual evidence plan
-> design contract
-> optional Figma / Canva / generated-image assist
-> page SVGs
-> automated visual lint + QA
-> native PPTX export
```

## What This Skill Optimizes For

- Native editable PPTX, not whole-slide screenshots
- Decision-oriented narrative, not document slicing
- Page-level claim / evidence / implication
- Explicit visual-form and component selection per page
- Stronger design language through archetypes and reusable components
- Generated images as atmosphere or metaphor, never factual evidence
- Visual QA before handoff

## Requirements

| Layer | Requirement | Notes |
|---|---|---|
| Agent runtime | Codex with local skills, file I/O, and shell access | Built for Codex Desktop/local skill use |
| PPT engine | `ppt-master` | Recommended: latest main or v2.4.0+ |
| Python | 3.10+ | Used by helper scripts and `ppt-master` |
| Render preview | `rsvg-convert` optional | Useful for PNG previews/montages |
| Image generation | optional | Use host image generation or configured `ppt-master` backends |

Set `PPT_MASTER_HOME` if your `ppt-master` checkout is not at `$HOME/tools/ppt-master`:

```bash
export PPT_MASTER_HOME="$HOME/tools/ppt-master"
```

## Install

Clone into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/TonyLTalentexe/future-ppt-skill.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/future-ppt"
```

Install `ppt-master`:

```bash
mkdir -p "$HOME/tools"
git clone https://github.com/hugohe3/ppt-master "$HOME/tools/ppt-master"
```

## Example Prompts

```text
Use $future-ppt to turn this mature industry report into a 10-page editable PPT.
Position it as an investor/IC memo deck. Start with needs alignment and keep risks visible.
```

```text
用 future-ppt 基于这个行业研究文档快速做 2-3 页 PPT 小样。
定位是行业研报，信息量要足，先让我看方向和效果。
```

```text
用 future-ppt 把这个成熟文档做成一份可编辑 PPT。
定位是行业研报，信息量要足，但要有视觉结构感。
先做需求对齐、claim/evidence/implication，再生成页面。
```

```text
Use $future-ppt to make this technical report into a launch-style deck.
Use generated images only as conceptual backgrounds; keep all facts, charts, and labels native.
```

## Expected Artifacts

Serious runs should produce:

- `needs_alignment_brief.md`
- `claim_evidence_implication.md`
- `slide_brief_matrix.md`
- `visual_evidence_plan.md`
- `design_contract.md`
- `spec_lock.md`
- `asset_prompt_pack.md` when generated/source imagery is used
- `svg_output/`
- `svg_final/`
- `preview_montage.png`
- `visual_lint.json`
- `qa_report.md`
- `exports/*.pptx`

Rapid sample runs may produce compact versions of the same planning artifacts and 1-3 finished slides. See `references/rapid-sample-mode.md`.

## QA Helpers

Check whether the exported deck has editable text:

```bash
python3 scripts/check_pptx_native.py path/to/deck.pptx
```

Run best-effort visual lint on a `ppt-master` project:

```bash
python3 scripts/deck_visual_lint.py path/to/project \
  --svg-dir path/to/project/svg_final \
  --preview-dir path/to/project/preview_png \
  --json-out path/to/project/visual_lint.json
```

`deck_visual_lint.py` checks for common risks such as image-only slides, tiny text, likely text overlap, over-bright/busy previews, repeated card-grid patterns, and low type hierarchy. It is a review aid, not a replacement for human montage inspection.

## Repository Layout

```text
future-ppt-skill/
├── SKILL.md
├── agents/openai.yaml
├── examples/
├── references/
│   ├── needs-alignment-and-style-archetypes.md
│   ├── narrative-compiler.md
│   ├── rapid-sample-mode.md
│   ├── style-archetype-playbooks.md
│   ├── visual-form-router.md
│   ├── page-component-library.md
│   ├── image-first-deck-workflow.md
│   ├── automated-visual-qa.md
│   └── ...
└── scripts/
    ├── check_pptx_native.py
    └── deck_visual_lint.py
```

## Open-Source Boundary

This repository contains the reusable skill workflow and helper scripts. It intentionally does not include private source documents, generated client decks, internal research artifacts, or licensed presentation templates.

Use mature templates as references for composition logic, chart/table grammar, density, and pacing. Do not copy proprietary slide masters, brand marks, watermarks, or exact layouts without permission.

## License

MIT
