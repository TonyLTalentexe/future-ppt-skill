---
name: future-ppt
description: Convert mature Chinese or English documents, reports, interview drafts, research notes, or strategy materials into editable, launch-quality PowerPoint decks. Use when the user asks to 做PPT, 生成PPT, 文档转PPT, 汇报材料, 发布会风格PPT, 可编辑PPT, 固化PPT工作流, or wants a deck with audience/purpose/style needs alignment, narrative claim-evidence-implication compilation, explicit template/style archetype selection, page component routing, style extraction, art direction, visual evidence planning, source/asset strategy, Figma-assisted design-system/reference extraction, Canva-assisted template/brand/design ideation, optional Figma/Canva reference drafts, automated visual lint, and QA before delivery.
---

# Future PPT

Turn mature source material into a native editable PPTX through a production workflow:

`needs alignment → source import → narrative compiler → slide brief matrix + visual router → art direction + component plan → visual evidence plan → design contract → optional Figma/Canva/generated-image assist → page SVGs → automated visual lint + QA → native PPTX export`

This skill is a workflow wrapper around `ppt-master` plus Codex judgment. It exists to prevent jumping directly from a document into slide design before audience, purpose, content boundaries, and style archetype are clear.

## Required Tools

- Prefer local `ppt-master` at `${PPT_MASTER_HOME:-$HOME/tools/ppt-master}`.
- If missing, clone `https://github.com/hugohe3/ppt-master` to that path.
- If a local UTF-8 guard exists, run it after editing Chinese Markdown/SVG/Python files.
- Use `rsvg-convert` when available for SVG preview PNGs.
- When the Figma plugin is available, treat it as an optional design source, review surface, or Figma Slides deliverable path.
- When the Canva plugin is available, treat it as an optional template/brand-kit/reference-design/moodboard layer, not as the default final production path.
- Treat image generation as a first-class optional asset-production layer for conceptual backgrounds, hero atmosphere, section dividers, and non-factual illustrative scenes. Prefer `${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/image_gen.py` when a requested/configured backend can write files directly; otherwise use the host `image_gen` capability when the user asks for Image2/Imagen/Gemini/Codex/local image generation, when the deck needs a high-design image-first pass, or when CLI environment variables are not configured. Do not decide image generation is unavailable only from missing shell API keys.
- When local professional agent workflows are available, use them as methodology references through `references/agency-agent-workflow.md`.
- The default final artifact remains native editable PPTX unless the user explicitly asks for Figma Slides, Canva, or multiple deliverables.

## Default Dark Neon Style

Unless the user provides another explicit visual direction or reference deck, every future PPT defaults to the dark-neon style in `references/dark-neon-default.md`:

- pure black background, bold white primary type, no decorative gradients as page background
- high-saturation neon accents: cyan, magenta, yellow, neon green
- extremely minimal dark-mode composition with chart/data emphasis carried by neon strokes, dots, bars, and keywords
- if the project has a real brand logo asset, place it in the top-right corner, scaled small enough to brand the page without competing with the title

When using a real brand asset, copy it into the project `images/` directory and add it as a small bitmap mark while keeping text, diagrams, and charts native editable. If no brand asset is provided, use native typography/page marks instead of inventing a logo.

Important: this default style is only a visual skin. It does not replace art direction. Every deck still needs a visual evidence plan and subject-specific imagery, diagrams, charts, or source screenshots when those would make the point clearer.

Important: do not let the default style collapse into a deck of rigid logic diagrams. High-design PPTs need a rhythm of cinematic anchor visuals, object metaphors, data/evidence pages, and native diagrams. Use `references/cinematic-visual-language.md` when a deck needs stronger visual memory, cover/section imagery, object-led pages, or generated images from image models such as GPT Image / Imagen / Gemini. If the user asks for a more beautiful deck, Image2-style visuals, or more use of Codex/local image generation, also use `references/image-first-deck-workflow.md` so generated imagery improves the design without overpowering the information layer.

## Workflow

### 1. Align Needs Before Production

Read `references/needs-alignment-and-style-archetypes.md` at the start of serious PPT tasks.

If the user asks for a quick 1-3 page sample, style test, direction preview, or "先做几页看看效果", also read `references/rapid-sample-mode.md` and use Rapid Sample Mode. Rapid samples may use compact planning artifacts, but still need needs assumptions, claim/evidence/implication, visual routing, rendered preview, visual lint, and native PPTX export.

Before making pages, identify the audience, decision/action needed, use context, desired style archetype, content boundaries, and forbidden material. Create `needs_alignment_brief.md` before `slide_brief_matrix.md`.

Ask up to three concise questions when the missing answers would materially change the deck. Prioritize:

- audience + decision/action needed
- must-include and must-not-include content
- style archetype or reference direction, e.g. McKinsey-style consulting, BCG-style strategic narrative, Xiaomi/launch, investor/IC, government, academic/technical, operating review, talent/research map

Do not ask questions that can be inferred from the source document, path, meeting title, prior conversation, or user-provided reference. If the user says "直接做", "先出一版", or urgency is clear, proceed with explicit assumptions in `needs_alignment_brief.md` and note those assumptions in the final handoff.

Mature PPT templates and consulting styles should be learned as composition logic, information hierarchy, chart/table grammar, and pacing. Do not copy proprietary masters, exact slide designs, watermarks, or brand marks without permission.

### 2. Establish Inputs

Identify:

- source content document(s)
- optional reference PPT for style extraction
- optional mature template/reference style to learn from: consulting, McKinsey-style, BCG-style, Xiaomi/launch, investor/IC, government, academic, operating review, or user-provided template
- optional Figma URL, Figma design system, or Figma Slides target
- optional Canva design URL, Canva brand kit, Canva brand template, or Canva reference/moodboard target
- optional image-generation preference, e.g. Imagen, Gemini, OpenAI image model, Image2-style workflow, or host-native `image_gen`
- optional image-first/high-design expectation: how many pages may use generated images, and whether non-cover pages must stay information-priority
- optional local agent/workflow reference
- optional style prompt, e.g. "纯黑底、白色粗体、霓虹 CMYG 点缀"
- audience, purpose, decision/action needed, reading mode, and time budget from `needs_alignment_brief.md`
- content contract: must include, nice to have, must not include, sensitive/uncertain content, required evidence, appendix expectations
- expected output length and use case
- expected final deliverable: native PPTX, Figma Slides, Canva design, or multiple outputs

If the user does not specify page count, choose by narrative load. For MVP tests, use 5-10 pages; for production, create as many pages as the Slide Brief Matrix requires.

Default deliverable decision:

- If the user asks for "PPT", "PowerPoint", "可编辑 PPT", or gives no format preference, produce native PPTX through `ppt-master`.
- If the user explicitly asks for "Figma Slides", "Figma 里做一版", "用 Figma 出方案", or wants collaborative Figma editing, use the Figma Slides path in `references/figma-integration.md`.
- If the user explicitly asks for "Canva", "Canva 里做一版", "用 Canva 模板", or gives a Canva design URL, use the Canva path in `references/canva-integration.md` as a reference, moodboard, or separate Canva deliverable.
- If the user provides a Figma URL as a visual reference, use Figma only to extract style evidence and screenshots, then translate it into `design_contract.md` and `spec_lock.md`.
- If the user provides a Canva URL as a visual reference, read its pages/content/thumbnails through Canva tools, then translate findings into `design_contract.md`, `visual_evidence_plan.md`, and `spec_lock.md`.

### 3. Create Project

Use `ppt-master`:

```bash
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/project_manager.py init <project_name> --format ppt169 --dir <base_dir>
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/project_manager.py import-sources <project_path> <source_files...> --copy
```

If DOCX conversion fails because `mammoth` is missing, extract with `python-docx` and save a Markdown source into `sources/`.

For branded runs, also create `<project_path>/images/` and copy the logo asset there before generating SVG pages.

### 4. Compile Narrative Before Designing

Read `references/narrative-compiler.md`, then create `claim_evidence_implication.md`.

Do this before `slide_brief_matrix.md`. The deck must have:

- one-sentence thesis tied to audience and decision/action
- source inventory with evidence strength and uncertainty
- 3-6 chapter-level claims for serious decks
- page-level claim, evidence, implication, confidence, and source trace
- mainline vs appendix split
- explicit exclusions for content that should not appear or should move to appendix

For analytical, consulting, IC, board, technical, and talent decks, page headlines should usually be assertion headlines, not topic labels. If a page has no implication, cut it, merge it, or move it to appendix.

### 5. Deconstruct Before Designing

Create `slide_brief_matrix.md` before generating slides. Do not skip this. Each page must define:

- page type
- page job
- target audience read: live claim, leave-behind proof, or appendix detail
- source claim from `claim_evidence_implication.md`
- core message
- information load
- source content
- visual form
- selected component from `references/page-component-library.md`
- why this visual fits
- visual evidence asset: actual image/chart/diagram/source screenshot/generated asset, or "none intentionally"
- asset source and usage note: local, public URL, generated, Canva/Figma reference, or original native drawing
- editable elements
- speaker-note intent

Use `references/slide-brief-matrix.md`, `references/visual-form-router.md`, and `references/page-component-library.md`.

The visual form must route from information structure, not decoration. If more than 30% of pages become generic card grids, revise the matrix before generating slides.

### 5A. Optional Agency Micro-Pipeline

Use this when the user mentions local/professional agents, asks to improve design workflow, criticizes design quality, or the deck is high-stakes.

Read `references/agency-agent-workflow.md`, then create lightweight versions of the relevant agent artifacts:

- `agent_workflow_plan.md`: phases, roles, handoffs, gates, retry policy
- `claim_spine.md`: Visual Storyteller pass with narrative arc, proof objects, and pacing
- `brand_guardian_audit.md`: brand consistency and do-not-use rules
- `asset_prompt_pack.md`: generated/source image prompts when imagery is needed; for generated imagery, include backend/model preference, prompt, negative prompt, filename, final derivative filename, aspect ratio, crop intent, status, and native overlay plan
- `asset_risk_review.md`: required when people, culture, institutions, logos, or factual-looking generated assets appear

Do not simulate a huge multi-agent bureaucracy for a small deck. Borrow the discipline: clear role passes, evidence-based gates, and final skepticism.

### 6. Lock Design

Before `design_contract.md`, create `visual_evidence_plan.md` and run the art-direction pass in `references/art-direction.md`. The design contract must obey `needs_alignment_brief.md`.

Create both:

- `design_contract.md`: human-readable style contract
- `spec_lock.md`: machine-readable color, font, page rhythm, and forbidden values

Support four style sources:

- preset style: e.g. launch black, consulting, academic, government, dark tech
- needs-aligned archetype: e.g. McKinsey-style consulting, BCG-style strategic narrative, Xiaomi/launch, investor/IC, government, academic/technical, operating review, talent/research map
- reference PPT extraction: inspect colors, fonts, layout rhythm, chart language, image posture
- style prompt: translate prompt into exact HEX, typography, density, visual rules

Use `references/design-contracts.md`. If an archetype was selected, read `references/style-archetype-playbooks.md` and translate the chosen archetype into page grammar, chart/table posture, density policy, image posture, and forbidden moves.

### 6A. Mandatory Art Direction Pass

Read `references/art-direction.md`. Do not start SVG generation until every slide has:

- one-sentence audience takeaway
- dominant visual object or clear reason not to use one
- visual evidence category: representational / organizational / explanatory / data / source / atmospheric
- asset plan and provenance
- selected component and visual-form route
- thumbnail-read hierarchy: what is visible at 25% zoom
- layer stack and scale risk when the slide uses networks, loops, maps, center nodes, or overlapping visual systems

If more than 30% of pages are text boxes with decorative accents, revise the matrix before generating slides.

If the deck feels like a sequence of rigid logic diagrams, read `references/cinematic-visual-language.md` and revise the page rhythm before generating SVGs. At minimum, important decks should identify anchor pages that can carry a cinematic image, object metaphor, atmospheric field, or large visual object instead of another small-card diagram.

### 6B. Optional Generated Image Asset Pass

Use this when `visual_evidence_plan.md` includes generated assets, the user asks for Imagen/Gemini/Image2/Codex/local image generation, the user criticizes weak design, or a cover/section/concept page needs stronger atmosphere than native shapes can provide.

Read `references/generated-image-assets.md`. For high-design or image-led decks, also read `references/image-first-deck-workflow.md`. Then:

- create or update `asset_prompt_pack.md`
- write an image resource list with raw filename, final derivative filename, slide, role, dimensions/aspect ratio, status, backend/model preference, and provenance note
- use deep prompts, not generic style words: narrative job, subject, environment, composition, camera/lens or illustration treatment, lighting, material texture, palette, negative constraints, crop-safe region, and native overlay plan
- for image-led decks, combine this with `references/cinematic-visual-language.md`: generated images should create memorable objects or atmospheres, not generic tech wallpaper
- generate assets sequentially; when using host `image_gen`, copy selected outputs from `$CODEX_HOME/generated_images/...` or the host-provided output location into `<project_path>/images/`; when using a file backend, generate directly into `<project_path>/images/`; retry once on failure, then mark the asset `Needs-Manual`
- for non-cover slides, create information-priority derivatives by cropping/resizing, darkening/desaturating, and baking the intended visibility into the raster asset; do not rely on SVG `<image opacity>` as the main readability control
- create `image_asset_contact_sheet.png` before embedding many generated assets, especially when most slides have backgrounds
- make P01/cover visually strong when useful, but make content-page backgrounds subordinate: at 25% zoom, title, key number, or native diagram must read before the generated image
- keep factual slide content native: no generated chart labels, fake paper screenshots, fake institution marks, fake UI, fake logos, or fake scientific evidence
- record every generated file, prompt, backend/model or fallback, and status in the project artifacts

If generated imagery fails quality review, revise the prompt, create a darker information-priority derivative, or replace the image with a native diagram/source visual. Do not hide weak AI imagery behind glows.

### 6C. Optional Figma Assist

Use this only when the user provides a Figma reference, asks to use Figma, wants Figma Slides, or the plugin can materially improve design quality.

Read `references/figma-integration.md`, then choose one mode:

- **Reference extraction**: use Figma screenshots/design context/design-system search to derive palette, typography, spacing, composition rhythm, and chart language; write `figma_style_extract.md`; convert findings into `design_contract.md` and `spec_lock.md`.
- **Figma Slides ideation**: after `slide_brief_matrix.md` and `design_contract.md` exist, generate a Figma Slides draft or options only when requested. Treat it as a deliverable or moodboard, not a replacement for native PPTX unless explicitly chosen.
- **Review aid**: use Figma screenshots or canvas inspection to compare generated pages against the reference style; record findings in `qa_report.md`.

Never let Figma-generated output skip the matrix, contract, native-element editability rules, or automated PPTX QA.

### 6D. Optional Canva Assist

Use this when the user provides a Canva design, asks for Canva, wants brand templates/brand kits, or the deck needs stronger visual ideation before native PPTX production.

Read `references/canva-integration.md`, then choose one mode:

- **Canva reference extraction**: read pages/content/notes/thumbnails from an existing Canva design; write `canva_style_extract.md`; translate findings into design and asset rules.
- **Brand/template alignment**: use Canva brand kits or brand templates to discover approved colors, fonts, logos, locked elements, page types, and image language.
- **Creative candidate / moodboard**: after the slide brief matrix exists, use Canva presentation generation or template exploration to produce a visual candidate only with the required outline-review flow and user approval.
- **Asset inspiration**: use Canva only to guide the asset plan; rebuild final text, diagrams, charts, and labels as native PPTX elements whenever final deliverable is PowerPoint.

Never use Canva output as a whole-slide bitmap deck unless the user explicitly accepts a non-native visual mockup.

### 7. Generate Pages

Generate SVG pages into `svg_output/`. Keep each page faithful to its slide brief and `spec_lock.md`.

Rules:

- one page, one job
- every analytical page expresses claim, evidence, and implication
- big text for live-presentation pages
- choose visual form based on information structure, not decoration
- use the selected component family from `page-component-library.md` unless there is a documented reason to deviate
- alternate visual modes deliberately: cinematic anchor visuals, object metaphors, native diagrams, evidence/data pages, and decision pages
- for network, loop, map, stack, and center-anchor pages, read `references/layering-and-scale.md` and apply its z-order and scale contract before drawing SVG
- use actual visual evidence where it improves comprehension: photos, screenshots, charts, mechanism diagrams, architecture diagrams, maps, portraits, institution/product marks, or generated scene assets
- keep decorative assets subordinate; if an image does not clarify the message, remove it
- no whole-slide bitmap as final output
- use generated images only as controlled backgrounds, hero atmosphere, conceptual illustrations, or section assets; keep text, charts, diagrams, labels, logos, and factual evidence native or sourced
- when referencing generated images in SVG, use `<image href="../images/<filename>" .../>` and keep native overlays outside the bitmap
- for image-first decks, use preprocessed information-priority background files on non-cover pages; titles, numbers, labels, center anchors, and cards must sit on top of generated imagery with enough native dark backing to read cleanly
- on cinematic/object-first pages, let one visual object occupy a meaningful share of the canvas; do not reduce every idea to equal-weight cards

### 8. QA And Export

Run in order:

```bash
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/svg_quality_checker.py <project_path>
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/total_md_split.py <project_path>
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/finalize_svg.py <project_path>
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/svg_quality_checker.py <project_path>/svg_final --format ppt169
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/svg_to_pptx.py <project_path> -s final
```

Then run:

```bash
python3 <skill_dir>/scripts/check_pptx_native.py <exported.pptx>
```

Render PNG previews and montage. Then run:

```bash
python3 <skill_dir>/scripts/deck_visual_lint.py <project_path> --json-out <project_path>/visual_lint.json
```

Inspect visually. Use `references/qa-rubric.md` and `references/automated-visual-qa.md`, then write `qa_report.md`.

QA must include a narrative section: deck thesis, page claim/evidence/implication coverage, mainline/appendix split, and any unsupported or assumption-based claims.

If the agency micro-pipeline was used, the final QA must include an Evidence Collector section and a Reality Checker verdict. The default final verdict is `NEEDS WORK` until rendered evidence proves otherwise.

If generated imagery was used, QA must include a generated-asset section: file existence, prompt provenance, backend/model or host `image_gen` path, contact sheet path when applicable, no fake text/logos/UI, no factual hallucination, crop fit, overlay readability, and whether the image actually improves the slide's argument.

If image-first or generated-background pages were used, QA must include a background-dominance check: at 25% zoom, P01 may allow the hero image to dominate, but every non-cover page must let title, key number, or native diagram read before the background. If a content-page image is the first read, mark the slide `NEEDS WORK` and create a darker information-priority derivative or remove the image.

If any slide uses a center anchor, radial network, loop, route map, or overlapping connectors, QA must include a layering/scale check: center anchor and its text sit above connectors, connector lines do not bleed through labels, and dominant objects remain larger than secondary nodes at thumbnail size.

QA must also include a component/rhythm check for important decks: if most slides are card grids, funnels, radial maps, or abstract logic diagrams with no cinematic anchor/object-led pages, or if the component choice does not match the claim's information structure, mark the deck `NEEDS WORK` for design impact even when automated checks pass.

### 9. Deliver

Final response should include:

- exported PPTX path
- Figma/Canva URLs or reference artifacts when used
- preview montage path
- intermediate artifacts: `needs_alignment_brief.md`, `claim_evidence_implication.md`, `slide_brief_matrix.md`, `visual_evidence_plan.md`, `design_contract.md`, `asset_prompt_pack.md` when used, `qa_report.md`, and agency artifacts when used
- image-first artifacts when used: `image_asset_contact_sheet.png` and final generated-image derivative list
- automated QA results: `check_pptx_native.py`, `deck_visual_lint.py`, and visual montage review
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

If a produced deck feels visually thin, do not simply add glow, cards, or random illustrations. Re-run the art-direction pass, replace text-only pages with stronger visual evidence, and regenerate the weakest pages.
