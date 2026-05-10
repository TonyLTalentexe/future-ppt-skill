# Generated Image Assets

Use this reference when a PPT needs AI-generated imagery as a real design asset, not as last-minute decoration.

Generated images can improve a deck when they create a memorable atmosphere or conceptual object that sourced images cannot provide. They can also weaken a deck when they pretend to be evidence. The boundary is strict: generated images may support mood, metaphor, and composition; factual claims, labels, charts, logos, UI, paper screenshots, citations, and scientific proof stay native or sourced.

When the deck needs a more polished, cinematic, high-design feel, pair this reference with `cinematic-visual-language.md`. When the user wants Image2/Codex/local image generation used broadly across the deck, also use `image-first-deck-workflow.md`. In that mode, generated images should create memorable objects or scenes while native PowerPoint remains the information layer.

## When To Generate

Use generated images for:

- cover heroes with controlled negative space
- section dividers
- cinematic anchor pages with one dominant object
- visual metaphors that make a strategic idea memorable
- abstract scientific or technological environments
- conceptual metaphors such as route maps, operating systems, virtual labs, or computational worlds
- background textures where the image supports a native diagram or headline
- non-factual editorial illustrations where the audience will not mistake the image for evidence

Do not generate:

- real people portraits unless the user explicitly wants synthetic people
- institution logos, seals, certificates, paper screenshots, UI screenshots, or charts
- microscopy/cell images that will be read as real experimental evidence
- maps or geographic scenes that need exactness
- text-heavy images; all text should be native PowerPoint text

## Required Artifact: `asset_prompt_pack.md`

Create this before generating or embedding any generated asset.

```markdown
# Asset Prompt Pack

## Deck Style Anchor

Shared visual language:

## Image Resource List

| filename | slide | role | dimensions | aspect_ratio | backend/model | status | provenance_note |
|---|---|---|---|---|---|---|---|
| cover_virtual_cell_world.png | P01 | hero background | 1920x1080 | 16:9 | preferred: Imagen/Gemini/OpenAI; actual: TBD | Pending | AI-generated conceptual atmosphere; not factual evidence |

## Prompts

### cover_virtual_cell_world.png

- slide/use: P01 cover hero
- narrative job: make the audience feel the scale shift from wet lab cells to computable living systems
- native overlay plan: title on left third; all labels and logo native
- crop-safe region: preserve empty dark space on left; detailed object on right
- prompt:
- negative prompt:
- alt text:
- review notes:
```

Status values:

- `Pending`: prompt planned; file not generated yet
- `Generated`: file exists in `<project_path>/images/`
- `Generated-Derivative`: raw image exists and a cropped/resized derivative is used in slides
- `Info-Priority-Derivative`: raw image was darkened/desaturated/blended into a content-safe background derivative
- `Needs-Manual`: generation attempted once plus one retry and failed
- `Rejected`: generated file exists but failed quality/risk review and must not be used
- `Replaced-Native`: generation was dropped in favor of a native diagram or sourced asset

## Deep Prompt Stack

Each prompt should include these layers, in this order:

1. **Use case and role**: presentation background, hero asset, section divider, conceptual illustration.
2. **Narrative job**: the feeling or argument the image must carry.
3. **Subject**: concrete visual objects, not vague nouns like "future" or "innovation". Prefer one recognizable object for anchor pages.
4. **Context/environment**: lab, computational space, cell interior, city, network, archive, boardroom, etc.
5. **Composition**: rule of thirds, central object, left negative space, top-safe title band, object scale.
6. **Camera or illustration treatment**: macro, aerial, isometric, editorial 3D, cinematic, scientific visualization, vector-like.
7. **Lighting and color grade**: exact palette from `spec_lock.md`, contrast, glow level, dark/light background.
8. **Material and detail**: glass, membrane, particles, grid, fiber, paper, metal, volumetric light, restrained texture.
9. **Output constraints**: aspect ratio, resolution, no text, no logo, no watermark, no fake UI.
10. **Negative prompt**: ban artifacts and anything that could be mistaken for evidence.

Bad prompt:

```text
futuristic virtual cell, neon style, high quality
```

Better prompt:

```text
Presentation hero background, 16:9. A conceptual scientific visualization of a virtual cell as a computable living system: translucent cell membrane on the right third, layered organelle-like networks, faint simulation grid, orbital data paths, and small luminous particles suggesting molecular dynamics. Deep black background with controlled cyan, magenta, yellow, and neon-green accents matching a dark launch deck. Cinematic macro-scientific composition, sharp central subject, soft volumetric light, restrained glow, generous empty dark space on the left for native title text, no text inside the image, no logo, no watermark, no fake microscopy, no fake labels, no charts.
```

## Backend Selection

Use the first available path that matches the user's request and can produce files in the project. Codex host `image_gen` is a valid production path; do not conclude that image generation is unavailable only because terminal environment variables or CLI backends are missing.

1. If the user explicitly names a backend such as Imagen, Gemini, OpenAI, Qwen, or Seedream and `ppt-master/scripts/image_gen.py` is configured for it, use that file-based backend.
2. If the user explicitly asks for Image2-style, Codex built-in, or local image generation, use the host `image_gen` capability and then copy the selected result into `<project_path>/images/`.
3. If no backend is specified and `ppt-master/scripts/image_gen.py` has a configured `IMAGE_BACKEND`, use it.
4. If the CLI backend is not configured but the host `image_gen` capability is available, use host `image_gen` instead of falling back to placeholders.
5. If no backend can run, still produce `asset_prompt_pack.md` and mark images `Needs-Manual`; continue with native diagrams or placeholders rather than blocking the whole deck.

Useful local check:

```bash
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/image_gen.py --list-backends
```

Generation command pattern:

```bash
python3 ${PPT_MASTER_HOME:-$HOME/tools/ppt-master}/skills/ppt-master/scripts/image_gen.py \
  "<prompt>" \
  --negative_prompt "<negative prompt>" \
  --aspect_ratio 16:9 \
  --image_size 1K \
  --output <project_path>/images \
  --filename cover_virtual_cell_world
```

Generate one image at a time. Confirm the file exists before generating the next image.

When using the host `image_gen`, preserve the original generated file and copy a project-local version into `<project_path>/images/`. If the host stores images under `$CODEX_HOME/generated_images/...`, treat that location as provenance and the project copy as the deck asset.

For non-cover pages, create a content-safe derivative before embedding. Crop/resize to 16:9, desaturate slightly, blend with black or the slide background, and save a clearly named derivative such as `p05_network_bg34.png` or `p07_core_info.png`. Prefer this baked raster derivative over relying on SVG `<image opacity>` for readability.

## Embedding Rules

- Save generated files in `<project_path>/images/` using the filename from `asset_prompt_pack.md`.
- Reference from slide SVGs with `<image href="../images/<filename>.png" .../>`.
- Keep native overlays separate: title, labels, logo, citations, charts, callouts, and legends remain editable.
- Put generated image layers below native panels, diagrams, center anchors, labels, and logos.
- For content pages, use the final information-priority derivative in the SVG, not the bright raw generation.
- Use crop geometry deliberately; do not stretch a generated image to hide poor composition.
- If the image needs text-like marks to look useful, the image is the wrong asset.
- If the image could fit any technology deck, the prompt is too generic. Add subject-specific objects, materials, environment, and narrative job.

When many generated assets are used, create `image_asset_contact_sheet.png` before export. The contact sheet should show the final derivative that will be embedded, not only the raw generated image.

## Review Gate

Before final export, render the slide and check:

- no fake text, marks, logos, seals, UI, or charts
- no visual claim that looks like factual microscopy, paper evidence, or real institution proof
- native text remains readable on top of the image
- for non-cover pages, title/key number/native diagram reads before the image at 25% zoom
- crop keeps the intended subject and negative space
- image style matches the deck's palette and does not fight the native diagram language
- the slide is stronger with the image than with a native diagram or source visual

Record results in `qa_report.md`.
