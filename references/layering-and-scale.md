# Layering And Scale

Use this before generating SVG pages that contain networks, loops, route maps, center nodes, system stacks, connector lines, or overlapping visual objects.

Layering and scale are readability controls, not decoration. A page can pass XML validation and still fail if connector lines sit above the visual anchor, or if a center node is too transparent or too small to dominate the diagram.

## Z-Order Contract

Draw SVG elements in this order, back to front:

1. Background fill.
2. Subtle grid, non-semantic texture, or atmosphere.
3. Source images or generated background images.
4. Connector lines, routes, arrows, and low-emphasis relationships.
5. Peripheral nodes, cards, labels, and secondary chips.
6. Dominant-object mask or backplate that interrupts connectors behind the anchor.
7. Center anchor shape and center anchor text.
8. Critical callouts, badges, page number, and logo.

For SVG-to-PPTX conversion, later SVG elements normally become visually higher layers. Therefore center anchors and their text should be emitted after connector lines and peripheral nodes unless the slide intentionally needs another foreground object.

## Center Anchor Pattern

When a page has a central object such as `人才资产`, `崔屹系`, `Virtual Cell`, `平台`, or `Operating System`:

- keep generated backgrounds, texture fields, and large atmospheric images below all connectors and nodes
- draw connector lines first
- draw an opaque or nearly opaque backplate over the connector crossing area
- draw the center circle/card on top of the backplate
- draw the center label last
- keep center text out of any line crossing path

Do not rely on semi-transparent fill to protect readability. If connectors pass under the anchor, either:

- use a solid or 0.96+ opacity center fill/backplate, or
- split connector lines so they stop at the anchor boundary, or
- place a black/panel-colored mask between connectors and center node.

## Scale Contract

Before drawing, define a scale role for every major object:

| Role | Minimum Guidance |
|---|---|
| center anchor | visually 1.25-1.6x stronger than surrounding nodes; label >= 18px |
| peripheral node/card | secondary to anchor; label >= 12px, preferred >= 14px |
| connector line | visible but subordinate; opacity usually 0.45-0.75 |
| headline | dominant page read; not smaller than important node labels |
| footnote/source | small but not competing with diagram |

Scale includes text, stroke, fill opacity, and occlusion area. A large circle with transparent fill may still read as too weak if lines bleed through it.

## Network / Loop QA

After rendering, inspect the slide at full size and in the montage:

- center anchor text is not crossed by lines, arrows, node borders, or grid artifacts
- center anchor is visually on top of the relationship layer
- generated background detail does not sit visually above or behind the center label strongly enough to reduce readability
- connectors terminate cleanly or disappear behind a mask/backplate
- the center object still reads first at thumbnail size
- no secondary card is visually heavier than the anchor unless that is the intended story
- logo and page/footer sit above background but do not compete with the diagram

If a slide fails this QA, fix by changing layer order, opacity, masks, line termination, or object scale. Do not fix by adding glow around the text; that usually hides the underlying structural problem.
