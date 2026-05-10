# Figma Integration Reference

Use this reference only when the user provides a Figma URL, asks to use Figma, wants Figma Slides, or a Figma design system can improve the deck.

## Boundary

- Default to native editable PPTX via `ppt-master`.
- Use Figma as style evidence, design-system discovery, ideation, or a parallel Figma Slides deliverable.
- Do not silently replace a requested PowerPoint with a Figma Slides deck.
- Do not use whole-slide screenshots as the final PPTX pages. Text, diagrams, charts, labels, and major shapes must remain editable in PowerPoint.

## Required Figma Practices

- Before any `use_figma` call, load the `figma-use` skill and follow its API rules.
- For full Figma screen construction from code or a multi-section layout, also load `figma-generate-design`.
- Prefer `get_design_context`, `get_screenshot`, `get_libraries`, and `search_design_system` for read/extraction work before writing custom Figma JavaScript.
- Every `use_figma` write must return created or mutated node IDs.
- Treat Figma tokens/components as design evidence. Translate them into explicit PPT constraints: HEX colors, font families, sizes, margins, spacing, chart rules, and forbidden values.

## Mode 1: Figma Reference Extraction

Use when the user provides a Figma URL as a visual reference.

1. Extract `fileKey` and, when present, `nodeId` from the URL.
2. If no `nodeId` is present, use read-only `use_figma` to list pages and top-level frames, then choose the relevant frame before screenshotting.
3. Use `get_screenshot` for the reference node.
4. Use `get_design_context` when a node is provided and style/code metadata would help.
5. Use `get_libraries` and `search_design_system` when the deck should follow a published design system.
6. If needed, use read-only `use_figma` to inspect pages, local styles, variables, and frame geometry.
7. Write `<project_path>/figma_style_extract.md` with:
   - reference URL, file key, node ID, and screenshot artifact
   - palette and semantic color roles
   - typography and size hierarchy
   - margin/grid/spacing rhythm
   - chart, diagram, icon, and image language
   - page rhythm and density observations
   - constraints that must not be copied directly
8. Translate the extraction into `visual_evidence_plan.md`, `design_contract.md`, and `spec_lock.md`.

## Mode 2: Design-System Assisted PPT

Use when the user wants the deck to align with an existing Figma design system.

Search broadly and simply. Useful queries:

- colors: `background`, `surface`, `text`, `brand`, `accent`, `gray`, `blue`, `green`, `red`
- typography: `heading`, `title`, `body`, `caption`
- spacing and shape: `space`, `spacing`, `gap`, `radius`, `border`
- deck components: `chart`, `metric`, `card`, `table`, `timeline`, `tag`

Keep only values that can be executed in SVG/PPT:

- convert color tokens to HEX in `spec_lock.md`
- map text styles to concrete font family, weight, size, and line-height
- convert spacing/radius tokens into numeric slide units or SVG coordinates
- describe components as visual language, not as imported UI widgets
- map useful component patterns to deck archetypes and page-level visual evidence categories

## Mode 3: Figma Slides Ideation Or Deliverable

Use `generate_deck` only after `slide_brief_matrix.md` and `design_contract.md` exist.

The prompt to `generate_deck` must be self-contained and include:

- title, audience, use case, objectives, and tone
- slide-by-slide outline derived from the slide brief matrix
- role for every slide, with varied layouts and no repeated role more than twice in a row
- concrete content and visual direction per slide
- enforceable rules from `design_contract.md`
- palette and theme from `spec_lock.md`

Decision rules:

- If Figma Slides is the requested deliverable, return the Figma Slides URL and note that the result is editable in Figma.
- If native PPTX is the requested deliverable, use Figma Slides only as a moodboard/reference option and continue through `ppt-master`.
- If the user wants both, generate native PPTX and a Figma Slides version, then clearly label them as separate artifacts.

## Mode 4: Figma-Assisted QA

Use when a Figma reference or Figma Slides draft exists.

Add a Figma section to `qa_report.md`:

- reference artifacts used
- palette/typography/rhythm match
- pages that diverge from the reference and why
- issues visible in screenshots: cropped text, weak hierarchy, over-dense labels, inconsistent spacing
- whether the final PPTX still passes native editability checks

Figma visual quality does not replace automated PPTX QA. Always still run the SVG quality checks, export, native-element check, preview render, and montage inspection.
