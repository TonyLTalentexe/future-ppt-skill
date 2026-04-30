# Slide Brief Matrix Reference

Create this before any SVG page generation.

## Required Columns

| Field | Meaning |
|---|---|
| page_id | `P01`, `P02`, etc. |
| page_type | cover / problem / model / analysis / evidence / strategy / transition / conclusion / appendix |
| page_job | The one task this page performs |
| core_message | The one sentence viewers must remember |
| information_load | light / medium / dense |
| source_content | Source paragraphs, section names, or data used |
| visual_form | e.g. big statement, axis map, ladder, matrix, curve, flywheel, timeline, comparison table |
| why_this_visual | Why the visual form matches the information structure |
| editable_elements | Text, shapes, labels, chart marks, lines, groups |
| speaker_note_intent | What the presenter should say |

## Visual Form Selection

| Information Structure | Preferred Visual |
|---|---|
| one strong claim | giant type / launch statement |
| hierarchy or maturity levels | ladder / stack / pyramid |
| two independent variables | 2-axis map / 2x2 matrix |
| growth, acceleration, transition | curve / slope / timeline |
| components around one object | orbit / hub-spoke / circuit |
| process or sequence | flow / roadmap / chevron process |
| tradeoffs or options | comparison table / ranked list |
| decision threshold | threshold ladder / stage gate |
| feedback loop | flywheel / cycle |

## Density Budget

- light: one claim + one visual object; usually no more than 8 text runs
- medium: one chart/diagram + labels + one takeaway; usually 9-22 text runs
- dense: table/matrix/comparison; use only when the page is a leave-behind or analysis page

If a page exceeds its density budget, split it or move detail into notes.

## Example

```yaml
page_id: P07
page_type: analysis
page_job: Explain why L and C must be assessed together
core_message: High complexity changes the meaning of the same decision level
information_load: medium
source_content: "C 产品复杂度" section, paragraphs 45-71
visual_form: 2-axis map
why_this_visual: L and C are independent variables; combinations matter
editable_elements: title, axes, tick labels, point labels, curve, takeaway
speaker_note_intent: Explain that a C6-L4.5 person may beat a C1-L5 person
```
