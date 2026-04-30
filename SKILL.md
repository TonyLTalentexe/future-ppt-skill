---
name: future-ppt
description: Convert mature Chinese or English documents, reports, interview drafts, research notes, or strategy materials into editable, launch-quality PowerPoint decks. Use when the user asks to 做PPT, 生成PPT, 文档转PPT, 汇报材料, 发布会风格PPT, 可编辑PPT, 固化PPT工作流, or wants a deck with explicit style extraction, prompt-driven visual direction, slide-level information architecture, and QA before delivery.
---

# Future PPT

Turn mature source material into a native editable PPTX through a production workflow:

`source document -> document deconstruction -> slide brief matrix -> design contract -> page SVGs -> QA -> native PPTX export`

This skill is a workflow wrapper around `ppt-master` plus agent judgment. It exists to prevent jumping directly from a document into slide design.

## Required Environment

- Codex or another agent runtime that supports local skills, file I/O, and shell commands.
- Python 3.10+.
- `ppt-master` cloned locally. Default discovery order:
  - `$PPT_MASTER_HOME`
  - `~/tools/ppt-master`
  - `./ppt-master`
- Optional but recommended: `rsvg-convert` for SVG preview PNGs.
- Optional for DOCX conversion fallback: `python-docx`.

## Workflow

### 1. Establish Inputs

Identify:

- source content document(s)
- optional reference PPT for style extraction
- optional style prompt, e.g. "纯黑底、白色粗体、霓虹 CMYG 点缀"
- expected output length and use case

If the user does not specify page count, choose by narrative load. For MVP tests, use 5-10 pages; for production, create as many pages as the Slide Brief Matrix requires.

### 2. Locate `ppt-master`

Set a shell variable before commands:

```bash
PPT_MASTER_HOME="${PPT_MASTER_HOME:-$HOME/tools/ppt-master}"
```

If missing:

```bash
git clone https://github.com/hugohe3/ppt-master "$PPT_MASTER_HOME"
```

### 3. Create Project

```bash
python3 "$PPT_MASTER_HOME/skills/ppt-master/scripts/project_manager.py" init <project_name> --format ppt169 --dir <base_dir>
python3 "$PPT_MASTER_HOME/skills/ppt-master/scripts/project_manager.py" import-sources <project_path> <source_files...> --copy
```

If DOCX conversion fails because `mammoth` is missing, extract with `python-docx` and save a Markdown source into `sources/`.

### 4. Deconstruct Before Designing

Create `slide_brief_matrix.md` before generating slides. Do not skip this. Each page must define:

- page type
- page job
- core message
- information load
- source content
- visual form
- why this visual fits
- editable elements
- speaker-note intent

Use `references/slide-brief-matrix.md`.

### 5. Lock Design

Create both:

- `design_contract.md`: human-readable style contract
- `spec_lock.md`: machine-readable color, font, page rhythm, and forbidden values

Support three style sources:

- preset style: e.g. launch black, consulting, academic, government, dark tech
- reference PPT extraction: inspect colors, fonts, layout rhythm, chart language, image posture
- style prompt: translate prompt into exact HEX, typography, density, visual rules

Use `references/design-contracts.md`.

### 6. Generate Pages

Generate SVG pages into `svg_output/`. Keep each page faithful to its slide brief and `spec_lock.md`.

Rules:

- one page, one job
- big text for live-presentation pages
- choose visual form based on information structure, not decoration
- no whole-slide bitmap as final output
- use generated images only as background/atmosphere/source assets; keep text, charts, diagrams, and labels native editable

### 7. QA And Export

Run in order:

```bash
python3 "$PPT_MASTER_HOME/skills/ppt-master/scripts/svg_quality_checker.py" <project_path>
python3 "$PPT_MASTER_HOME/skills/ppt-master/scripts/total_md_split.py" <project_path>
python3 "$PPT_MASTER_HOME/skills/ppt-master/scripts/finalize_svg.py" <project_path>
python3 "$PPT_MASTER_HOME/skills/ppt-master/scripts/svg_quality_checker.py" <project_path>/svg_final --format ppt169
python3 "$PPT_MASTER_HOME/skills/ppt-master/scripts/svg_to_pptx.py" <project_path> -s final
```

Then run:

```bash
python3 <skill_dir>/scripts/check_pptx_native.py <exported.pptx>
```

Render PNG previews and a montage. Inspect visually. Use `references/qa-rubric.md` and write `qa_report.md`.

### 8. Deliver

Final response should include:

- exported PPTX path
- preview montage path
- intermediate artifacts: `slide_brief_matrix.md`, `design_contract.md`, `qa_report.md`
- automated QA results
- unresolved issues and recommended next iteration

## Quality Bar

For launch-style decks inspired by Xiaomi:

- pure single-page claim whenever possible
- high contrast and strong typography
- one dominant visual object
- low prose density
- clear rhythm between breathing and dense pages
- no generic "title + three cards" unless the brief truly requires modular comparison

For dense report decks, preserve clarity through page-level briefs, not by cramming paragraphs into boxes.
