# Design Contract Reference

Write `design_contract.md` and `spec_lock.md` before page generation.

## Design Contract

Human-readable contract:

```markdown
# Design Contract

## Style Positioning
- Inspiration:
- Audience:
- Purpose / decision needed:
- Reading mode:
- Selected archetype:
- Why this archetype fits:
- Emotional register:
- What this deck must feel like:
- What it must avoid:

## Palette
- Background:
- Main text:
- Accent colors:
- Usage rules:

## Typography
- Title:
- Body:
- Emphasis:
- Minimum readable size:

## Page Rhythm
- Anchor pages:
- Cinematic/object pages:
- Breathing pages:
- Dense pages:
- Appendix / leave-behind pages:
- Component families allowed:
- Component families forbidden:

## Visual Evidence Strategy
- Dominant visual categories:
- Cinematic/object-led anchor pages:
- Image/source posture:
- Diagram/chart posture:
- AI-generated image boundary:
- Image-first intensity ladder:
- Information-priority derivative rule:
- Asset credit/provenance rule:

## Figma/Canva Assist
- Figma reference or system used:
- Canva reference, brand kit, or template used:
- Extracted rules adopted:
- Rules intentionally rejected:

## Visual Rules
- One-page-one-job rule:
- Audience fit rule:
- Claim/evidence/implication rule:
- Chart language:
- Table language:
- Component language:
- Image posture:
- Decoration boundary:

## Forbidden
- ...
```

## `spec_lock.md`

Machine-readable contract. Only list values that may appear in SVG.

```markdown
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## colors
- bg: #000000
- text: #FFFFFF
- text_secondary: #B8B8B8
- cyan: #00F5FF
- magenta: #FF2BD6
- yellow: #FFE600
- neon_green: #39FF14

## typography
- font_family: "Microsoft YaHei", "PingFang SC", Arial, sans-serif
- body: 20
- title: 36
- subtitle: 26
- annotation: 14
- cover_title: 82

## page_rhythm
- P01: anchor
- P02: breathing
- P03: dense

## forbidden
- rgba()
- `<style>`, `class`, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<script>`, `<iframe>`, `<symbol>`+`<use>`
- `<g opacity>`
```

## Style Source Modes

### Preset Style

Choose from or adapt:

- launch-black: pure black, white bold type, neon accents, Xiaomi-style stage rhythm
- premium-consulting: white/off-white, restrained accent, high chart clarity
- dark-tech: deep charcoal, muted glow, technical diagrams
- government-report: formal red/blue, authoritative hierarchy
- academic-defense: serif/sans mix, structured evidence and citations

### Needs-Aligned Archetype

Load `needs-alignment-and-style-archetypes.md` and `style-archetype-playbooks.md` when selecting a design language from audience and purpose.

Translate the selected archetype into:

- page archetypes: executive summary, exhibit, comparison, roadmap, launch claim, evidence appendix, etc.
- composition logic: assertion headline, exhibit-first, hero-object, dashboard, formal report, technical mechanism
- chart/table grammar: what kinds of tables, charts, captions, and footnotes are expected
- density and reading mode: live presentation, leave-behind, or both
- forbidden moves: styles that would undermine the audience's trust

### Component Contract

Load `page-component-library.md` and define:

- primary component families used in this deck
- where each component is allowed: mainline, proof page, appendix, section anchor
- chart/table density per component
- native editability rules
- repeated component limits: avoid making most pages the same card grid unless the deck is intentionally a catalog

### Reference PPT Extraction

Inspect:

- dominant colors and accent colors
- font family and weights
- title placement and size
- margin system
- use of images vs native shapes
- chart language
- page rhythm: cover, section, analysis, conclusion

Translate findings into `design_contract.md` and `spec_lock.md`; do not blindly copy every visual artifact.

### Canva / Figma Reference Extraction

When the visual source is Canva or Figma, extract the system instead of copying the surface:

- palette roles, not just visible colors
- typography hierarchy, not just font names
- grid, margins, density, and page rhythm
- image posture: full bleed, cropped editorial, isolated object, screenshot, proof card, or no image
- chart/table/diagram language
- repeated components and where they are allowed
- visual evidence categories that make the reference feel credible

Record extracted rules in `canva_style_extract.md` or `figma_style_extract.md`, then translate them into this contract and `spec_lock.md`.

### Prompt Style

Translate style prompt into exact constraints. Example:

User: "极致极简的深色模式，纯黑底色，纯白粗体主文字，Cyan/Magenta/Yellow/Neon Green 点缀。"

Contract:

- `bg = #000000`
- `text = #FFFFFF`
- accents = `#00F5FF`, `#FF2BD6`, `#FFE600`, `#39FF14`
- big claims in 54-82px bold
- no paragraph cards
- charts and emphasis only use neon colors

## Asset And Editability Contract

Every final PowerPoint should remain editable. Define:

- native elements: titles, labels, diagrams, tables, charts, arrows, callouts
- acceptable bitmap elements: logo, portrait, source screenshot, microscopy/cell image, generated atmosphere, product/institution image
- forbidden bitmap usage: whole-slide screenshots used as final pages, image-only text, non-editable charts, decorative image collages
- provenance: source URL/file/generation prompt/Canva or Figma reference for each non-native asset

## Layer And Scale Contract

For any network, route map, loop, or center-anchor slide, include explicit rules:

- layer stack: background → grid → connectors → peripheral nodes → center mask/backplate → center anchor → center text → logo/footer
- center anchor scale: specify radius/box size, label size, and opacity/backplate rule
- connector policy: terminate at anchor boundary or pass below an opaque mask
- thumbnail rule: center anchor must be recognized before secondary nodes at 25% zoom

## Cinematic Visual Contract

For high-design decks, define:

- visual rhythm: which pages are cinematic anchors, object metaphors, native diagrams, evidence pages, and decision pages
- anchor object: the concrete thing the audience should remember
- generated image role: atmosphere/object/scene only; native overlays carry all factual content
- negative-space rule: where title and metrics will sit
- generic-image ban: no tech wallpaper that could fit any deck

## Image-First Contract

When generated images are used across many pages, define:

- page intensity: cover, section anchor, thesis/content, dense evidence
- effective image presence: strong for cover; subdued for non-cover information pages
- derivative naming: raw asset and final content-safe derivative filename
- overlay protection: native dark panels, scrims, center masks, and title-safe zones
- first-read rule: on non-cover pages, title/key number/native diagram must read before the image at 25% zoom
- contact sheet rule: `image_asset_contact_sheet.png` required before embedding many generated assets
