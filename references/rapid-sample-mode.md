# Rapid Sample Mode

Use this when the user asks for a quick 1-3 page PPT sample, style test, direction preview, or "先做几页看看效果".

The goal is speed with enough process discipline to test the workflow. Do not run the full production ceremony, but do not skip narrative judgment.

## When To Use

Use rapid sample mode when:

- the user asks for 1-3 pages
- the user wants to evaluate style or workflow quality
- the source document is mature but the output is explicitly a preview
- time matters more than exhaustive coverage

Do not use it for final board decks, client deliverables, regulatory/official decks, or high-stakes decision materials unless the user explicitly asks for a quick concept first.

## Minimum Artifacts

Create lightweight versions of:

- `needs_alignment_brief.md`
- `claim_evidence_implication.md`
- `slide_brief_matrix.md`
- `visual_evidence_plan.md`
- `design_contract.md`
- `qa_report.md`

Skip or defer:

- large agency workflow artifacts
- full appendix planning
- generated image contact sheet, unless generated images are used
- multiple style directions, unless the user asks

## Page Count Guidance

For 1 page:

- show the core thesis and 2-4 proof anchors.
- use `Claim Hero + Native Proof` or `Assertion + Exhibit`.

For 2 pages:

- P01: thesis / reframing
- P02: market / mechanism / route, depending on source

For 3 pages:

- P01: thesis / reframing
- P02: market, mechanism, or evidence structure
- P03: route, risk, decision, or next-step plan

## Default Archetype

If the user says "industry report", "research note", or "信息量要足", default to:

- style: industry research / investor judgment
- reading mode: quick leave-behind
- density: medium-high
- visual posture: native exhibits, comparison cards, roadmap/risk board
- image posture: no generated image unless visual concept is central

## Rapid Workflow

1. Infer needs from the user request and source path; ask only if the missing answer would change the sample.
2. Read the document's executive summary, main section headings, conclusion, data tables, product route, and risks.
3. Write a compact `claim_evidence_implication.md`.
4. Route pages through `visual-form-router.md` and choose components from `page-component-library.md`.
5. Build 1-3 SVG pages.
6. Run:

```bash
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/svg_quality_checker.py <project_path>
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/finalize_svg.py <project_path>
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/svg_quality_checker.py <project_path>/svg_final --format ppt169
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/svg_to_pptx.py <project_path> -s final
python3 <skill_dir>/scripts/deck_visual_lint.py <project_path>
python3 <skill_dir>/scripts/check_pptx_native.py <exported.pptx>
```

7. Render a preview montage and inspect it before delivery.

## Quality Bar

Rapid samples can be incomplete, but they should still show:

- one clear thesis
- one visual form per page
- enough information density to test the target use case
- editable native text and shapes
- no obvious text overlap or unreadable labels
- no private source material embedded in open-source examples

## Handoff Language

When delivering, state that this is a direction preview, not the final production deck. Mention:

- selected positioning
- pages generated
- preview montage
- QA results
- what should improve in a full version
