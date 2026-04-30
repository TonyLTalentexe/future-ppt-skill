# QA Rubric

Write `qa_report.md` after export and preview.

## Automated QA

Required checks:

| Check | Pass Criteria |
|---|---|
| `svg_quality_checker.py <project>` | 0 errors before finalize |
| `svg_quality_checker.py <project>/svg_final --format ppt169` | 0 errors after finalize |
| `spec_lock drift` | none |
| PPTX export | succeeds |
| native check | media count low/zero; text runs present |
| notes | one note file per SVG |
| previews | PNG pages + montage rendered |

## Human QA Dimensions

Score 1-10:

| Dimension | Questions |
|---|---|
| information architecture | Does each page have one job? Is the sequence logical? |
| visual-form matching | Is the chosen diagram/chart the right form for the information? |
| aesthetic consistency | Does every page obey the style contract? |
| layout readability | Are title, labels, and visual objects readable at thumbnail size? |
| launch quality | Does the page have a memorable dominant read? |
| editability | Are text, labels, and major shapes editable? |

## Release Threshold

- MVP acceptable: no automated QA failures; average human QA >= 8
- Production acceptable: no automated QA failures; no page below 8 in layout readability; visual-form matching >= 8.5

## Common Failure Modes

- The slide is a paragraph with decoration.
- The visual form does not match the information structure.
- Neon/gradient accents become decorative noise instead of information hierarchy.
- Dense labels ruin launch-style readability.
- Reference PPT style is copied superficially instead of translated into constraints.
- Final PPT is an image deck rather than native editable shapes.
