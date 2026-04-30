# Design Contract Reference

Write `design_contract.md` and `spec_lock.md` before page generation.

## Design Contract

Human-readable contract:

```markdown
# Design Contract

## Style Positioning
- Inspiration:
- Audience:
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
- Breathing pages:
- Dense pages:

## Visual Rules
- One-page-one-job rule:
- Chart language:
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
