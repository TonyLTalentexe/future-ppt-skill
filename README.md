# Future PPT Skill

`future-ppt` is a Codex skill for turning mature documents into **native editable PowerPoint decks** through a production workflow:

```text
source document
-> document deconstruction
-> slide brief matrix
-> design contract
-> page SVGs
-> QA
-> native PPTX export
```

It is designed to cooperate with [ppt-master](https://github.com/hugohe3/ppt-master): the agent owns content decomposition, style control, page briefs, and QA; `ppt-master` handles SVG validation, post-processing, and native PPTX export.

## What This Skill Optimizes For

- Editable PPTX, not whole-slide screenshots
- Slide-level information architecture before design
- Prompt-driven or reference-PPT-driven style control
- Explicit visual-form selection per page
- QA across information design, aesthetics, layout, and export safety

## Environment Compatibility

| Layer | Requirement | Notes |
|---|---|---|
| Agent runtime | Codex with local skills, file I/O, and shell access | Tested as a Codex Desktop local skill |
| OS | macOS or Linux recommended | Windows should work if `ppt-master` and Python deps are configured |
| Python | 3.10+ | Used by `ppt-master` and helper scripts |
| PPT engine | `ppt-master` | Recommended v2.4.0+ |
| Render preview | `rsvg-convert` optional | Used to create PNG previews/montages from SVG |
| DOCX fallback | `python-docx` optional | Useful when `ppt-master` DOCX conversion lacks `mammoth` |
| Image generation | optional | Use Codex image generation or `ppt-master` image backends for atmosphere/background assets only |

The workflow was tested with:

- macOS
- Codex Desktop
- Python 3.14 system runtime for simple scripts
- `ppt-master` main branch around v2.4.0
- `rsvg-convert`

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/<your-org-or-user>/future-ppt-skill.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/future-ppt"
```

Install or clone `ppt-master`:

```bash
mkdir -p "$HOME/tools"
git clone https://github.com/hugohe3/ppt-master "$HOME/tools/ppt-master"
```

Optionally set:

```bash
export PPT_MASTER_HOME="$HOME/tools/ppt-master"
```

## Usage

Example prompt:

```text
Use $future-ppt to turn this mature document into an editable launch-quality PPT.
Use the attached reference PPT for style extraction. Keep the output native editable.
```

Chinese prompt example:

```text
用 future-ppt 把这个成熟文档做成一份可编辑 PPT。
先做页面分镜表，再按“纯黑底、白色粗体、霓虹 CMYG 点缀”的发布会风格生成。
```

## Workflow Artifacts

Every serious run should produce:

- `slide_brief_matrix.md`
- `design_contract.md`
- `design_spec.md`
- `spec_lock.md`
- `svg_output/`
- `svg_final/`
- `exports/*.pptx`
- `previews/montage.png`
- `qa_report.md`

## Repository Layout

```text
future-ppt-skill/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── design-contracts.md
│   ├── qa-rubric.md
│   └── slide-brief-matrix.md
└── scripts/
    └── check_pptx_native.py
```

## Design Philosophy

Do not design slides directly from raw documents. First define each page's job, information load, and visual form. Once every page is a clear production unit, decks can scale from 5 pages to 50 pages while staying coherent under a shared design contract.

## License

MIT
