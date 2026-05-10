# Visual Form Router

Use this while converting `claim_evidence_implication.md` into `slide_brief_matrix.md`.

The router maps information structure to visual form. It prevents defaulting to generic cards, funnels, or decorative diagrams.

## Routing Table

| Information Structure | Primary Question | Preferred Visual Forms | Evidence Mode |
|---|---|---|---|
| one strong claim | What must land? | claim hero, single metric, object + proof | proof metric, source note, speaker notes |
| list of conclusions | What are the few takeaways? | executive summary board, conclusion cards | source line per conclusion |
| two variables | What position or tradeoff matters? | 2x2, axis map, scatter | plotted evidence, labels |
| many comparable items | Which is better/worse? | ranked table, benchmark chart, heatmap | metrics, source notes |
| change over time | What changed and when? | timeline, curve, roadmap | dated facts, milestones |
| process or plan | What happens next? | roadmap, stage gate, swimlane | actions, owners, gates |
| mechanism or causality | Why does it work? | mechanism diagram, loop, system stack | causal labels, inputs/outputs |
| ecosystem or network | Who connects to whom? | network map, orbit map, landscape map | source-backed nodes |
| hierarchy | What sits above/below? | pyramid, stack, tree, capability ladder | classification evidence |
| portfolio choice | Where should we focus? | portfolio matrix, opportunity map | attractiveness/fit metrics |
| risk and uncertainty | What could go wrong? | risk matrix, sensitivity table, scenario page | likelihood/impact/mitigation |
| source proof | Why should we trust it? | source proof card, citation panel, screenshot crop | primary source |
| talent comparison | Who fits and why? | talent landscape map, tiering matrix, evidence cards | fact/inference/action split |
| technical detail | How exactly? | mechanism, architecture, annotated figure, appendix table | citations and exact labels |

## Routing Process

For each planned page:

1. Read the page claim from `claim_evidence_implication.md`.
2. Identify the information structure, not the topic.
3. Pick one primary visual form.
4. Pick one evidence mode.
5. Choose a component from `page-component-library.md`.
6. Write `why_this_visual` in the slide brief.

## Bad Routing Patterns

Avoid these:

- using three cards because the source has three paragraphs
- using a radial map because it looks impressive but the data is not relational
- using a funnel when the story is actually a maturity ladder
- using a generated background when the page needs source proof
- using a dense table in a live launch page
- using a hero claim page for a decision that needs risk visibility

## Density Routing

Use reading mode from `needs_alignment_brief.md`:

- live: claim hero, assertion + exhibit, simple axis map, simplified roadmap
- leave-behind: assertion + exhibit, tables, source cards, appendix pages
- both: mainline uses simplified components; appendix carries tables and sources

## Visual Rhythm Routing

For decks longer than 8 pages, plan rhythm:

- avoid 3+ dense pages in a row unless the deck is a technical appendix
- insert section/anchor page after major narrative shifts
- use object-first or cinematic pages only when they support the argument
- mix charts/tables with diagrams and source proof; do not make every page a card grid

## Router QA

Fail the matrix if:

- more than 40% of mainline pages use the same component without a narrative reason
- more than 30% of pages are generic card grids
- a page's `why_this_visual` says only "clear" or "nice-looking"
- a visual form does not match the information structure
- evidence-heavy claims are routed to atmospheric image pages
