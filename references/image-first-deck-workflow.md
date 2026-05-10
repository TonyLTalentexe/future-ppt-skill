# Image-First Deck Workflow

Use this reference when the user asks for a more beautiful, premium, cinematic, Image2-like, or generated-image-heavy PPT.

The goal is not to turn the deck into an image gallery. The goal is to let generated images create visual memory while native PowerPoint objects carry the facts.

## Core Rule

Generated imagery creates mood, metaphor, scale, and subject-specific objects.

Native PowerPoint carries:

- titles and subtitles
- names, organizations, people, companies, labs, papers, and citations
- metrics, charts, labels, legends, and callouts
- process diagrams, evidence cards, and decision text
- logos and any factual marks

If an image contains readable text, fake UI, fake labels, fake logos, or scientific-looking proof, reject it, crop it away, or cover it with native design structure. Do not ask the image model to render factual content.

## When To Use Image-First

Use it when:

- the user says the deck lacks design feeling or is too diagram-heavy
- the deck needs cover/section pages with stronger memory
- the topic benefits from cinematic science, technology, industry, space, material, city, network, lab, or object metaphors
- the user explicitly mentions Image2, Imagen, Gemini, GPT Image, Codex image generation, local image generation, or deep visual prompts

Do not use it blindly for dense evidence appendices, legal/procurement pages, or pages where exact screenshots and charts are the evidence.

## Visual Intensity Ladder

Choose an intensity per page before generating images.

| Page Type | Image Role | Effective Image Presence | Notes |
|---|---|---:|---|
| Cover | hero scene or dominant object | 70-100% | Can be visually strong if title has clean negative space |
| Section anchor | atmosphere or object metaphor | 55-75% | Short claim, minimal secondary text |
| Thesis page | dominant object plus native proof chips | 45-65% | Keep factual chips on opaque or semi-opaque native panels |
| Standard content page | subdued background or side object | 34-44% | Text and numbers must read first |
| Dense evidence page | texture only or no image | 25-38% | Use real evidence, charts, or native structure instead |

On every non-cover page, if the generated image is the first thing the eye reads at 25% zoom, the page fails. Create a darker, lower-visibility derivative or remove the image.

## Prompt Recipe

Write one prompt per slide asset. Avoid generic words like "future", "innovation", "technology background", and "high quality" unless the prompt also has a concrete object and scene.

Required prompt components:

1. Use case: presentation background, hero image, section divider, object illustration.
2. Narrative job: what the audience should feel or understand.
3. Concrete subject: one visual object or scene tied to the slide claim.
4. Environment: lab, cell interior, material lattice, power grid, mission control, star map, industrial route, city infrastructure, archive, etc.
5. Composition: title-safe band, card-safe zone, negative space, object position, crop intent.
6. Treatment: cinematic macro, premium editorial 3D, scientific visualization, isometric, aerial, material close-up.
7. Lighting and palette: match `spec_lock.md`; restrained glow; avoid noisy gradients.
8. Output constraints: 16:9, no text, no letters, no numbers, no logo, no watermark, no fake UI, no fake chart, no people/faces unless explicitly needed.
9. Native overlay plan: where titles, cards, metrics, and labels will sit.

Prompt skeleton:

```text
Presentation background, 16:9. [Narrative job]. A [concrete visual object] in [specific environment], [composition with title-safe/card-safe negative space], [camera or illustration treatment], [lighting and palette from the deck], [material and detail]. Premium editorial science/technology visualization. No text, letters, numbers, logo, watermark, fake UI, fake chart, fake labels, people, or faces. Designed for native PowerPoint title/cards overlaid outside the image.
```

## Built-In Image Generation Path

Codex host image generation is a valid production path. Do not conclude that image generation is unavailable only because terminal environment variables or CLI backends are missing.

Preferred order:

1. If the user explicitly names a backend and `ppt-master/scripts/image_gen.py` is configured for it, use that file-based backend.
2. If the user asks for Image2/Codex/local image generation, or the CLI backend is not configured, use the host `image_gen` capability.
3. Copy the selected generated file from `$CODEX_HOME/generated_images/...` or the host-provided output location into `<project_path>/images/`.
4. Keep the original generated file untouched; use project-local copies and derivatives for the deck.

Generate sequentially. After each generation, confirm:

- file exists
- image is 16:9 or can crop cleanly to 16:9
- no text-like artifacts, logos, fake UI, charts, or factual-looking proof
- subject and negative space match the slide job

## Information-Priority Derivatives

For non-cover slides, bake readability into the raster asset instead of relying on SVG image opacity. Some converters and QA tools handle transparent image references inconsistently, and preprocessed assets are easier to review.

Create a derivative per content slide:

- crop/resize to 1280x720 or 1920x1080
- desaturate slightly
- blend with black or the slide background
- optionally add a stronger dark safe zone behind the title or cards
- save as `<base>_info.png` or `<base>_bg34.png`

Recommended effective presence:

- cover: 70-100%
- section anchor: 55-75%
- standard content: 34-44%
- dense evidence: 25-38%

The derivative should still feel designed, but it must read second after the title, numbers, and main native diagram.

## Contact Sheet Gate

Before embedding image assets across a deck, create `image_asset_contact_sheet.png` in the project folder or `images/` folder.

The contact sheet should show:

- filename
- slide id
- role
- final derivative used, not only the raw generated image

Use the contact sheet to catch repeated motifs, over-bright backgrounds, generic wallpaper, and inconsistent palette before the PPTX export step.

## Embedding And Layering

Layer order:

1. Background color or base shape
2. Generated image/background derivative
3. Native dark scrims or safe-zone panels
4. Native diagrams, cards, charts, and callouts
5. Native title, key numbers, labels, and citations
6. Logo and page marks

For radial, center-anchor, loop, route-map, and network slides, connector lines must stay behind the center anchor and its text. The center text must be fully legible at thumbnail size.

Do not use a generated image to compensate for weak slide logic. If the information layer is unclear without the image, fix the slide brief or diagram first.

## QA Checks

During montage review, run the background dominance check:

- at 25% zoom, what do you see first?
- for P01, the hero image may be first or tied with the title
- for non-cover pages, the title, key number, or native object must read before the image
- if the image reads first, create a darker derivative, add a native safe zone, crop to reduce detail, or remove it

Generated-image QA must also confirm:

- no fake text, logos, UI, charts, seals, institution marks, or paper screenshots
- all factual content is native or sourced
- prompt provenance is recorded in `asset_prompt_pack.md`
- image role is specific to the slide, not generic technology wallpaper
- crop and safe zones match the overlay plan
- image improves the argument or emotional memory of the page

## Required Artifact Updates

When this workflow is used, update:

- `asset_prompt_pack.md`: include raw asset, final derivative filename, backend/model, prompt, negative prompt, status, and native overlay plan
- `visual_evidence_plan.md`: mark generated assets as atmospheric, metaphorical, or object-led, not factual evidence
- `qa_report.md`: include contact sheet path, background dominance verdict, fake-text/logos/UI check, crop fit, and overlay readability

Useful statuses:

- `Pending`: prompt written; no file yet
- `Generated`: raw image exists in project images
- `Generated-Derivative`: derivative exists and is used
- `Info-Priority-Derivative`: derivative is darkened/desaturated for content readability
- `Rejected`: image failed QA and must not be embedded
- `Replaced-Native`: image concept was replaced with native/source visual
