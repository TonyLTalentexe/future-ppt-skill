# Dark Neon Default

Use this as the default PPT aesthetic when no stronger style reference is supplied.

## Visual Identity

- Background: pure black `#000000`.
- Primary text: pure white `#FFFFFF`, bold or extra-bold.
- Secondary text: cool gray, restrained, never low-contrast.
- Accent palette: cyan `#00F5FF`, magenta `#FF2BD6`, yellow `#FFE600`, neon green `#39FF14`.
- Layout: extreme minimal dark mode, generous negative space on claim pages, tighter but still scanable structure on analysis pages.
- Brand asset: optional. Use only real user-provided logos or bundled project assets.

## Logo Rule

- Default placement: top-right corner on every slide when a real logo is provided.
- Recommended 16:9 SVG coordinates: top-right safe area, scaled small enough to avoid competing with the title.
- Keep transparent-background PNG logos intact; do not redraw them as fake text or pseudo-marks.
- If the title or chart genuinely conflicts with the logo, reduce width before moving it.

## Implementation

- Copy the real logo asset into the deck project `images/` directory.
- Add the logo as a small `<image>` brand mark on every SVG page before finalization.
- Do not add opacity to the `<image>` tag; the SVG QA checker treats image opacity as a forbidden pattern.
- In PPTX QA, one approved media asset is acceptable when the only media asset is the real logo.

## Composition Rules

- No beige, brown, corporate blue, or washed gradient themes unless the user explicitly requests them.
- Do not use gradient blobs, orbs, or decorative bokeh as background.
- Keep text, charts, diagrams, and labels native editable in the PPTX.
- Generated or bitmap images are acceptable for backgrounds, subject images, or brand marks, but not as whole-slide screenshots.
- Use neon color only to encode emphasis, data, topology, or hierarchy; avoid turning every element bright.

## Tone

The deck should feel like a premium future-industry board briefing: black field, white conviction, neon evidence.
