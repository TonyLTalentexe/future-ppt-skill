# Narrative Compiler

Use this after needs alignment and source import, before `slide_brief_matrix.md`.

The job is to convert a mature document into a decision-ready narrative spine. Do not start slide design until the deck has a clear thesis, claim sequence, evidence plan, and appendix split.

## Required Artifact: `claim_evidence_implication.md`

```markdown
# Claim Evidence Implication

## Deck Thesis
- audience:
- decision_or_action:
- one_sentence_thesis:
- success_criterion:

## Source Inventory
| source_section | useful_claims | evidence | uncertainty | main_or_appendix |
|---|---|---|---|---|

## Narrative Spine
| chapter | claim | role_in_argument | must_prove | likely_pages |
|---|---|---|---|---|

## Page Claim Plan
| page_id | page_role | claim | evidence | implication | confidence | source_trace | main_or_appendix |
|---|---|---|---|---|---|---|---|

## Exclusions
| content | reason | destination |
|---|---|---|

## Open Risks
| risk | affected_page | mitigation |
|---|---|---|
```

## Compile Steps

1. **Inventory the source**
   - Extract useful facts, arguments, examples, numbers, people, organizations, timelines, and unresolved questions.
   - Mark evidence strength: primary/source, quantified, expert judgment, weak/inferred, unsupported.

2. **Choose the deck thesis**
   - Write one sentence that names the judgment the deck should make easier.
   - If the user only wants background, make the thesis an orientation claim, not a recommendation.

3. **Build the narrative spine**
   - Use 3-6 chapter claims for serious decks.
   - Each chapter must either diagnose, compare, explain, prove, recommend, or close a decision.

4. **Split mainline and appendix**
   - Mainline contains what the audience must understand to act.
   - Appendix contains detail, source proof, long tables, technical depth, and optional backup.

5. **Create page claims**
   - Every page needs a claim, evidence, and implication.
   - If a page cannot name its implication, merge it, cut it, or move it to appendix.

## Claim Types

| Type | Use When | Good Headline Shape |
|---|---|---|
| Diagnosis | explaining the problem | "The bottleneck is shifting from X to Y" |
| Insight | revealing a non-obvious pattern | "The same metric hides two different talent profiles" |
| Comparison | ranking or choosing | "Option A wins on speed, but B controls strategic risk" |
| Mechanism | explaining why something works | "Three feedback loops make the platform compound" |
| Opportunity | sizing or prioritizing | "The near-term wedge is small but strategically central" |
| Risk | surfacing uncertainty | "The largest risk is not technical readiness, but transferability" |
| Recommendation | telling the audience what to do | "Prioritize a small expert pod before broad market sourcing" |
| Decision | asking for action | "Approve the next-step outreach list and validation plan" |

## Headline Rules

Good PPT headlines are claims, not topics.

Weak:

- "Technology Roadmap"
- "Key Experts"
- "Market Analysis"

Better:

- "The roadmap is converging around three validation bottlenecks"
- "The expert pool is deep, but the industry-transfer subset is narrow"
- "Market scale is less decisive than deployment-cycle fit"

For consulting, IC, board, and executive decks, every analytical page should have an assertion headline. For launch decks, the headline can be a short emotional claim, but it still needs a clear page job.

## Evidence Rules

Every claim needs at least one evidence mode:

- source fact: document section, paper, screenshot, quote, chart, database, public source
- quantified proof: metric, ranking, benchmark, count, trend
- structural proof: mechanism, architecture, causal loop, process
- comparative proof: table, 2x2, waterfall, matrix, ranked options
- judgment proof: clearly labeled expert interpretation or assumption

Never let generated imagery act as evidence. Generated imagery can make the claim memorable; evidence must be native, sourced, or explicitly reasoned.

## Mainline Budget

Use the audience and reading mode from `needs_alignment_brief.md`:

- live senior presentation: 8-15 mainline pages, lower text density, more speaker notes
- leave-behind report: 15-35 pages, stronger captions and appendix
- IC/board: 10-20 mainline pages plus risk/source appendix
- launch/inspiration: 6-14 pages, strong pacing, few dense pages
- technical review: as many pages as needed, but keep mechanisms and evidence separated

## Narrative QA

Before slide design, fail the plan if:

- the deck thesis is missing or generic
- page headlines are topic labels instead of claims
- a major claim has no evidence
- evidence pages do not say what the audience should conclude
- too much source detail sits in the mainline
- risks are hidden in a deck meant for investment, technical, or executive judgment
- the appendix split is undefined for a dense source document

Fix the narrative before improving visuals. A beautiful deck with a weak claim spine is still weak.
