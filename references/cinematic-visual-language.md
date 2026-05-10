# Cinematic Visual Language

Use this when the user wants a deck with stronger design feeling, when a deck looks like a series of rigid logic diagrams, or when generated-image models such as GPT Image / Imagen / Gemini can create better anchor visuals.

The goal is not to make the deck decorative. The goal is to give the deck visual memory: a few pages should have a clear object, scene, atmosphere, or cinematic frame that the audience can remember after the meeting.

## Design Principle

Pretty PPTs usually have rhythm:

- **anchor visual pages**: one large object or atmosphere, short claim, minimal text
- **native diagram pages**: logic, mechanism, system, route, workflow
- **evidence pages**: source cards, metrics, screenshots, tables, charts
- **decision pages**: crisp recommendation boards

If every page is a diagram, the deck becomes intellectually clear but visually dry. If every page is a generated image, the deck becomes pretty but untrustworthy. Use both. When many pages use generated images, apply `image-first-deck-workflow.md`: cover pages may be visually strong, while non-cover pages need subdued, information-priority backgrounds.

## Anchor Visual Modes

Choose one mode for important cover, section, or thesis pages:

| Mode | Use When | Visual Posture |
|---|---|---|
| Cinematic atmosphere | The page needs emotion, scale, or awe | full-bleed or 60-75% canvas image with native title overlay |
| Object metaphor | The page needs a memorable concept | one dominant object: battery core, constellation, bridge, lens, compass, control room, data crystal |
| Material macro | The topic is science/technology/materials | close-up material landscape, electrode layers, membrane texture, particles, lattice |
| Spatial map | The topic is networks or ecosystems | star map, city grid, orbital routes, terrain map, mission control board |
| Editorial hybrid | The page needs both proof and mood | large image/object plus native evidence chips or metrics |

For business/executive decks, usually 25-40% of slides can be anchor or object-led pages. Dense appendix/report decks may use fewer. A 10-12 page important deck should normally have at least 2-4 visually memorable anchor pages.

## Image Intensity Discipline

Generated images should have different strength by page role:

- cover: strong hero image or object can dominate if title space is clean
- section anchor: cinematic but simple; short native claim on top
- thesis/content page: image supports one native diagram, metric, or claim
- dense evidence page: image is absent or reduced to a dark texture

For non-cover pages, the audience should read the title, key number, native diagram, or decision text before the image. If the image is the first read in a preview montage, darken/desaturate it, create an information-priority derivative, crop away detail, or remove it.

## Object-First Brief

Before writing prompts or drawing SVG, define the object:

```markdown
## Visual Object Brief

| page_id | claim | visual_object | why_this_object | image_mode | native_overlay | risk |
|---|---|---|---|---|---|---|
| P01 | talent map becomes an operating system | energy-storage constellation | shows route + network + scale | generated hero | title left, labels native | avoid generic starfield |
```

Good visual objects are concrete:

- energy-storage constellation
- glowing battery core in a black void
- orbital route map around a material crystal
- mission-control table with route lights
- molecular/material lattice turning into a city grid
- bridge between overseas research stars and Chinese industrial nodes

Weak visual objects are vague:

- technology background
- innovation
- futuristic energy
- abstract science
- AI network

## Generated Image Prompt Pattern

Use this pattern for image-led slides:

```text
Presentation anchor image, 16:9. [Narrative job]. A single dominant [visual object] in [specific environment], [composition and negative space], [camera/lens or illustration treatment], [lighting/color grade tied to spec_lock], [material/texture/detail], premium editorial science/technology style, suitable for native Chinese title overlay, no readable text inside image, no logo, no watermark, no fake UI, no chart, no institution seal.
```

Add a negative prompt:

```text
text, letters, watermark, logo, fake UI, fake chart, fake labels, fake institution seal, stock photo, people, faces, clutter, blurry, low quality, oversaturated gradient, random sci-fi decoration
```

## Advanced Energy Examples

### Cover

Visual object: energy-storage talent constellation.

Prompt direction:

```text
Presentation anchor image, 16:9. Show advanced energy storage talent as a navigable constellation, not a list. A deep black star-map-like field with six luminous route clusters implying solid-state batteries, sodium-ion batteries, flow batteries, compressed-air storage, flywheel/gravity storage, and hydrogen storage. One elegant central energy core connects to orbital research and industry nodes. Premium scientific editorial visualization, restrained cyan, magenta, yellow, neon green, and electric blue, generous empty space on the left for native title text, crisp lines, cinematic darkness, no text, no logo, no fake charts, no people.
```

### Overseas Network Page

Visual object: origin star with alumni orbit.

Prompt direction:

```text
A single bright origin star representing a research lab, with smaller orbiting stars spreading toward a subtle map-like horizon, dark premium background, thin luminous trails, sense of overseas-to-China bridge, clean negative space for native labels, no map labels, no text, no logos.
```

### Industrial Conversion Page

Visual object: material lattice becoming city power grid.

Prompt direction:

```text
A macro energy material lattice on the left gradually transforming into a clean city-scale power grid on the right, dark cinematic presentation background, restrained neon route colors, premium scientific visualization, no text, no logos, no fake UI.
```

## Native Overlay Rules

- All titles, labels, metrics, route names, source notes, and logos stay native PowerPoint objects.
- Generated images should provide scene, object, texture, scale, and emotion.
- Do not ask an image model to draw Chinese text, data labels, company names, or charts.
- Compose images with negative space where native text will sit.
- Avoid busy images behind dense data.
- Use native dark panels, scrims, and center anchors above the image layer when content needs protection.
- On radial/network/loop pages, connector lines and generated backgrounds stay behind the center anchor and its text.

## Visual Rhythm QA

During montage review, fail the deck if:

- every page is a logic diagram, card grid, funnel, or radial map
- generated images look like generic tech wallpaper and could fit any topic
- anchor images do not have one recognizable object
- images compete with native text or make it hard to read
- non-cover backgrounds are the first read at 25% zoom
- there is no breathing page after multiple dense evidence pages
- object scale is too timid: the visual is present but not memorable

Fix by replacing one or more logic pages with an object-first page, not by adding decorative background images behind the same diagram.
