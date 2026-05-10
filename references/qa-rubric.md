# QA Rubric

Write `qa_report.md` after export and preview.

## Automated QA

Required checks:

| Check | Pass Criteria |
|---|---|
| `needs_alignment_brief.md` | exists for serious decks; audience, purpose/decision, content contract, style archetype, and assumptions are documented |
| `claim_evidence_implication.md` | exists; every mainline page has claim, evidence, implication, confidence, source trace, and main/appendix status |
| visual router / component plan | every slide brief has `visual_form`, `selected_component`, and `why_this_visual` tied to information structure |
| `svg_quality_checker.py <project>` | 0 errors before finalize |
| `svg_quality_checker.py <project>/svg_final --format ppt169` | 0 errors after finalize |
| `spec_lock drift` | none |
| `visual_evidence_plan.md` | exists; every page has an asset strategy and provenance |
| generated assets | if used, `asset_prompt_pack.md` exists; every generated file has prompt provenance, backend/model or host `image_gen` path, file existence status, and no fake text/logos/UI/factual proof |
| image-first contact sheet | if multiple generated images/backgrounds are used, `image_asset_contact_sheet.png` exists and shows the final embedded derivatives |
| background dominance | if generated backgrounds are used, P01 may be hero-led; every non-cover page has title/key number/native diagram reading before the background at 25% zoom |
| PPTX export | succeeds |
| native check | text runs present; media count is explainable by approved logos, source images, screenshots, or generated backgrounds; no image-only slide text |
| `deck_visual_lint.py <project>` | runs; ERROR findings are fixed; WARN findings are fixed or explicitly accepted in `qa_report.md` |
| notes | one note file per SVG |
| previews | PNG pages + montage rendered |
| layering/scale | network/loop/map slides have center anchors above connectors, no connector bleed through labels, and dominant objects scaled above secondary nodes |
| Canva/Figma artifacts | extraction/candidate links documented when used |
| agency micro-pipeline | if used, `agent_workflow_plan.md`, `claim_spine.md`, and final Reality Checker verdict documented |

## Human QA Dimensions

Score 1-10:

| Dimension | Questions |
|---|---|
| needs alignment | Does the deck match the real audience, purpose, reading mode, and decision/action needed? |
| narrative spine | Does every mainline page have a clear claim, evidence, and implication? |
| information architecture | Does each page have one job? Is the sequence logical? |
| narrative arc | Does the deck have beginning/middle/end, pacing, and a clear decision destination? |
| visual-form matching | Is the chosen diagram/chart the right form for the information? |
| visual evidence strength | Does the dominant visual clarify, prove, or emotionalize the point rather than decorate it? |
| visual rhythm and memorability | Does the deck alternate logic diagrams with cinematic/object-led anchor pages where appropriate? |
| asset quality/provenance | Are sourced/generated/Canva/Figma-inspired assets high quality, relevant, and credited? |
| generated image control | If AI images are used, do they have strong composition, native overlay safety, no fake evidence, and a clear narrative job? |
| image-first information hierarchy | On non-cover pages, does the information layer read before the generated background? |
| aesthetic consistency | Does every page obey the style contract? |
| style archetype fit | Does the deck use the selected archetype's composition/table/chart logic rather than a generic template skin? |
| component fit | Does each page use a visual component that matches the information structure? |
| brand consistency | Are logo, palette, typography, voice, and do-not-use rules respected? |
| layout readability | Are title, labels, and visual objects readable at thumbnail size? |
| layer/scale discipline | Are foreground anchors, labels, and masks on top of connectors/backgrounds? Does scale reinforce the intended hierarchy? |
| launch quality | Does the page have a memorable dominant read? |
| editability | Are text, labels, and major shapes editable? |

## Release Threshold

- MVP acceptable: no automated QA failures; average human QA >= 8
- Production acceptable: no automated QA failures; no page below 8 in layout readability; visual-form matching >= 8.5; visual evidence strength >= 8.5; Reality Checker verdict is `READY` or residual risks are explicitly accepted

## Common Failure Modes

- The slide is a paragraph with decoration.
- The deck starts designing before audience, purpose, decision/action, and content exclusions are clear.
- The deck summarizes source sections instead of compiling claim/evidence/implication.
- Page headlines are topic labels instead of assertions.
- Evidence exists but the implication is missing.
- A mature template style is copied as surface decoration rather than translated into composition, chart/table logic, and pacing.
- The selected style archetype mismatches the context, e.g. launch-style drama for a technical due diligence deck or consulting density for a live product reveal.
- The deck is a sequence of rigid logic diagrams with no cinematic anchor, object metaphor, or visual breathing page.
- Generated images are used as generic background wallpaper rather than subject-specific visual objects.
- Generated backgrounds are too bright or detailed, so the audience reads the image before the slide's title, number, or native diagram.
- The visual form does not match the information structure.
- The selected page component is generic or repetitive; the deck becomes a sequence of similar cards.
- Neon/gradient accents become decorative noise instead of information hierarchy.
- Dense labels ruin launch-style readability.
- Connector lines, arrows, or grids sit above the center node or cross the center text.
- A semi-transparent center node lets relationship lines bleed through the label area.
- Scale is applied only to shapes, not to the full visual group including text, stroke, mask, and occlusion area.
- Reference PPT style is copied superficially instead of translated into constraints.
- Final PPT is an image deck rather than native editable shapes.
- The page uses attractive but generic imagery that does not improve trust or comprehension.
- Generated images contain text-like marks, fake UI, fake logos, invented labels, or scientific-looking "evidence".
- Generated images were embedded without prompt provenance or review status.
- Generated image opacity is handled only in SVG instead of using a reviewed, content-safe raster derivative for information-heavy pages.
- Canva/Figma output is pasted into PowerPoint instead of being rebuilt as native editable structure.
- The visual evidence plan is skipped, so pages default to cards, glow, and icons.
- Fantasy approval: `qa_report.md` says "excellent" or "ready" without rendered evidence and specific issue review.
- No handoff continuity: narrative, brand, design system, assets, and QA each make independent decisions that do not reconcile.
