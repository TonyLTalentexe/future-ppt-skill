# Art Direction And Visual Evidence

Use this before generating SVG pages. The goal is to make the deck visually convincing, not merely styled.

## First Principles

- One idea per slide: split overloaded pages instead of shrinking everything.
- Start each analytical slide with an assertion headline, then support it with visual evidence and an implication.
- Use visuals to do work that words cannot: show structure, comparison, mechanism, scale, evidence, context, or emotion.
- Do not add images for decoration. Every image must be representational, organizational, explanatory, data-bearing, source/proof, or controlled atmosphere.
- Favor consistent grids, repeated components, and a small number of page archetypes so the deck feels designed as a system.
- Use strong hierarchy: one dominant object, one headline, one takeaway. Secondary labels must not compete with the main read.
- Build slides that still communicate when forwarded without a presenter: assertion headline, visible evidence, compact caption, and speaker notes.
- Balance native logic diagrams with cinematic anchor visuals or object metaphors when the deck needs design impact. A deck that is all funnels, cards, and radial maps may be correct but visually forgettable.

## Required Artifact: `visual_evidence_plan.md`

Create this file after `slide_brief_matrix.md` and before `design_contract.md`. Use `claim_evidence_implication.md` to verify each page's claim and evidence, then use `visual-form-router.md` and `page-component-library.md` to select the visual form and component.

```markdown
# Visual Evidence Plan

| page_id | audience_takeaway | claim | implication | component | dominant_visual | visual_evidence_category | asset_plan | source/provenance | native_editability_plan | thumbnail_read | risk |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P03 | ... | ... | ... | timeline / career arc | timeline + portrait/photo | source / organizational | use scholar metric callout + career timeline | local/source/public/generated | timeline and labels native; portrait optional bitmap | title + metric + arc visible | avoid tiny labels |
```

For important decks, also create or embed a `Visual Object Brief` for anchor pages. See `cinematic-visual-language.md`.

## Visual Evidence Categories

- **Representational**: portrait, product screenshot, institution logo, actual object, cell image, lab photo.
- **Organizational**: timeline, stack, matrix, map, system architecture, route diagram.
- **Explanatory**: mechanism, process, causal loop, before/after, annotated model.
- **Data**: chart, table, metric strip, benchmark result, citation count, funding amount.
- **Source/proof**: paper title screenshot, publication card, quote chip, citation callout.
- **Atmospheric**: generated or sourced background that sets tone; use sparingly and never as the only reason a slide exists.
- **Object/metaphor**: a large generated, sourced, or native visual object that makes an abstract idea memorable; factual content remains native or sourced.

## Asset Strategy

For every page, choose one:

- **Native-only**: best for clean diagrams, charts, matrices, timelines, and executive logic.
- **Public/source image**: use when an actual person, place, product, paper, cell image, or screenshot increases trust.
- **Generated image**: use for conceptual backgrounds, abstract scientific environments, cover imagery, or section dividers when no source image is appropriate.
- **Generated object/scene**: use for cinematic anchor pages or visual metaphors when a large visual object helps the audience feel scale, network, transition, or urgency.
- **Canva/Figma reference**: use as style or layout inspiration, then rebuild final PPT elements natively.
- **No image intentionally**: allowed only when the native diagram is already the visual evidence.

If any page uses **Generated image**, run `references/generated-image-assets.md` before SVG generation and create `asset_prompt_pack.md`. Generated assets must have filenames, prompt provenance, backend/model or host `image_gen` path, and status before they are embedded.

If generated images are used as a recurring deck language, run `references/image-first-deck-workflow.md`. Define which pages are allowed to be strong image-led pages and which pages require information-priority derivatives. P01 may be visually dominant; non-cover pages must let title, key number, native diagram, or evidence cards read before the image at 25% zoom.

If a deck feels visually dry or overly diagrammatic, run `references/cinematic-visual-language.md` and convert selected cover/section/thesis pages into object-first anchor pages.

## Image Quality Rules

- Prefer fewer, larger, more meaningful visuals over many small decorative thumbnails.
- Place labels next to the parts of the image/diagram they explain.
- Credit sources for public images, screenshots, charts, and statistics in notes or small captions.
- Avoid clip art, generic stock photos, decorative science backgrounds, and unrelated icons.
- If using AI-generated images, keep them as controlled backgrounds, hero atmosphere, conceptual illustrations, or section assets. Keep all factual labels, charts, diagrams, logos, source proof, and citations native or sourced.
- For information-heavy pages with generated backgrounds, use a darkened/desaturated raster derivative rather than relying only on SVG image opacity.
- For scientific/technical decks, prefer diagrams, mechanism illustrations, annotated screenshots, microscopy/source visuals, and data charts over generic photos.

## Generated Image Prompt Discipline

Generated image prompts must be specific enough to control composition, not just style. Each generated asset needs:

- narrative job: what feeling or argument the image carries
- subject and environment: concrete objects and setting
- composition/crop: where title and native overlays will sit
- camera or illustration treatment
- lighting/color grade tied to `spec_lock.md`
- negative constraints: no text, watermark, logo, fake UI, fake labels, or factual-looking evidence
- image intensity and native overlay plan: cover can be strong; content pages need safe zones and subdued backgrounds

Do not ask image generation models to make readable slide text, charts, citations, diagrams, or logos. Generate the visual field; build the information layer natively.

## Layering And Scale Rules

For networks, loops, maps, and center-node diagrams, read `layering-and-scale.md` before drawing the page.

- Define the dominant anchor and its intended scale before placing connectors.
- Draw relationship lines below nodes and center anchors.
- Center anchors and their text must sit on top of the relationship layer.
- If connector lines pass through a center node, use an opaque backplate/mask or terminate the lines at the node boundary.
- Do not let transparency or small scale make the anchor weaker than surrounding nodes.

## Page Archetype Menu

Use a small set of archetypes per deck:

- Hero claim + primary visual
- Cinematic anchor visual
- Object metaphor + native claim overlay
- Assertion-evidence slide
- Timeline / migration path
- System stack / layered architecture
- Mechanism loop / process flow
- 2-axis map / 2x2 matrix
- Evidence card + source proof
- Benchmark chart / metric strip
- Dense reference table
- Closing judgment board

If the deck has too many unique layouts, simplify to 5-7 archetypes and vary content within them.

For reusable component rules, load `page-component-library.md`. For mapping information structure to visual form, load `visual-form-router.md`.

## Thumbnail QA

Render a montage and inspect at thumbnail size. A page fails if:

- the headline is not legible
- the dominant visual cannot be recognized
- every element has equal visual weight
- labels collide or require zooming
- connector lines or grid marks cross center-anchor labels
- the center object is lower in layer order than relationships around it
- on non-cover pages, a generated background dominates the title, key metric, or native diagram
- the deck has no memorable anchor object or cinematic page
- every page uses the same abstract logic-diagram language
- the page looks like a text box with decorations
- the image is attractive but does not clarify the point
- the selected component does not match the claim/evidence/implication plan

Fix by changing the visual form or asset, not by adding more decoration.
