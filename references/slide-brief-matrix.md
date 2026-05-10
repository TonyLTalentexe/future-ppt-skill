# Slide Brief Matrix Reference

Create this before any SVG page generation.

## Required Columns

| Field | Meaning |
|---|---|
| page_id | `P01`, `P02`, etc. |
| page_type | cover / problem / model / analysis / evidence / strategy / transition / conclusion / appendix |
| page_job | The one task this page performs |
| target_read | live claim / leave-behind proof / appendix detail |
| source_claim | Page claim from `claim_evidence_implication.md` |
| core_message | The one sentence viewers must remember |
| information_load | light / medium / dense |
| source_content | Source paragraphs, section names, or data used |
| visual_form | e.g. big statement, axis map, ladder, matrix, curve, flywheel, timeline, comparison table |
| selected_component | Primary component from `page-component-library.md` |
| why_this_visual | Why the visual form matches the information structure |
| visual_evidence_asset | Actual image/chart/diagram/source screenshot/generated asset, or `none intentionally` |
| asset_source_usage | Local file, public URL, generated asset, Canva/Figma reference, or original native drawing; include credit/usage notes when relevant |
| editable_elements | Text, shapes, labels, chart marks, lines, groups |
| speaker_note_intent | What the presenter should say |

## Visual Form Selection

Select visual forms based on `needs_alignment_brief.md` and `claim_evidence_implication.md`, not only on content structure. A senior executive deck usually needs implication-first exhibits; a launch deck needs claim-first breathing pages; a technical review needs mechanisms and evidence; an operating review needs KPI/action tables.

Use `visual-form-router.md` before choosing the visual form, then use `page-component-library.md` before drawing the slide.

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

## Archetype Influence

| Archetype | Slide Matrix Bias |
|---|---|
| McKinsey-style consulting | assertion headlines, exhibit-first analysis, clear implication, restrained appendix |
| BCG-style strategic narrative | market/opportunity maps, portfolio matrices, transformation journeys |
| Xiaomi/launch | one claim per page, large type, hero visuals, low prose density |
| Investor/IC | thesis, proof, risk, ask, downside, decision page, appendix evidence |
| Government/official report | formal hierarchy, policy/context/action, conservative charts and tables |
| Academic/technical | problem-method-result, mechanisms, citations, technical appendix |
| Operating review | KPI, variance, root cause, owner/action, roadmap |
| Talent/research map | landscape, ranking/tiering, evidence cards, network/funnel, next actions |

## Visual Evidence Selection

The matrix is not complete until each page has a dominant visual strategy. Choose one:

- representational evidence: actual person, institution, product, paper, dataset, microscope/cell image, interface screenshot
- organizational evidence: timeline, stack, map, matrix, architecture, ecosystem, route diagram
- explanatory evidence: mechanism, process, causal loop, model comparison, annotated transformation
- data evidence: chart, metric strip, benchmark, citation/funding/publication count, table
- source/proof evidence: paper card, quote chip, citation panel, website/document screenshot
- controlled atmosphere: generated or sourced hero/section background; use sparingly and keep factual content native
- none intentionally: only when the native diagram/table itself is the evidence

Avoid using a decorative stock image as the visual plan. If the image does not increase trust, comprehension, or emotional focus, replace it with a diagram, data object, or source proof.

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
target_read: leave-behind proof
source_claim: "High complexity changes the meaning of the same decision level"
core_message: High complexity changes the meaning of the same decision level
information_load: medium
source_content: "C 产品复杂度" section, paragraphs 45-71
visual_form: 2-axis map
selected_component: 2x2 / Axis Map
why_this_visual: L and C are independent variables; combinations matter
visual_evidence_asset: native 2-axis map with three benchmark candidate points
asset_source_usage: original native drawing; source paragraphs cited in speaker notes
editable_elements: title, axes, tick labels, point labels, curve, takeaway
speaker_note_intent: Explain that a C6-L4.5 person may beat a C1-L5 person
```
