# Agency Agent Micro-Pipeline

Use this when the user mentions local agents, asks for stronger design quality, asks to "try harder", or when a deck is important enough that one-pass production is risky.

This reference distills local professional/agency-style workflows into a PPT-specific process. Do not paste private agent files into a deck project. Convert their roles into concrete artifacts and gates.

## Core Doctrine

- Evidence over claims: every quality statement needs rendered proof, source notes, or measurable checks.
- No phase advances without a gate: narrative, design system, visual evidence, render QA, and final readiness must each pass.
- Default to `NEEDS WORK` during QA. First versions normally need revision.
- Use structured handoffs so context does not disappear between narrative, design, asset, build, and QA steps.
- Maximum 3 retry cycles for a stubborn slide or deck-level defect; then escalate by decomposing or changing the approach.

## Role Map For PPT Work

| Local agent pattern | PPT role | Required artifact |
|---|---|---|
| Agents Orchestrator | Pipeline owner and gatekeeper | `agent_workflow_plan.md` |
| Visual Storyteller | Narrative arc, pacing, visual metaphor | `claim_spine.md` and updates to `slide_brief_matrix.md` |
| Brand Guardian | Brand integrity and consistency | `brand_guardian_audit.md` and `design_contract.md` |
| UX Architect / UI Designer | Design system, tokens, slide components | `spec_lock.md`, component/archetype rules in `design_contract.md` |
| Image Prompt Engineer | Generated/source asset prompts | `asset_prompt_pack.md` when generated imagery is used |
| Inclusive Visuals Specialist | Human/cultural/identity image risk review | `asset_risk_review.md` when people, institutions, places, or cultural imagery appears |
| Evidence Collector | Screenshot/contact-sheet QA | QA section in `qa_report.md` with visual evidence issues |
| Reality Checker | Final readiness verdict | final verdict in `qa_report.md` |

## Required Micro-Pipeline

### 1. Orchestrator Setup

Create `agent_workflow_plan.md` for substantial decks.

```markdown
# Agent Workflow Plan

| Phase | Role | Input | Output | Gate |
|---|---|---|---|---|
| Narrative | Visual Storyteller | source notes | claim_spine.md | every slide has a claim + proof object |
| Brand | Brand Guardian | brand assets/reference | design_contract.md | palette/type/logo rules are explicit |
| System | UX/UI | design_contract.md | spec_lock.md + archetypes | tokens and component rules are executable |
| Assets | Image Prompt / Inclusive Visuals | visual_evidence_plan.md | asset_prompt_pack.md / asset_risk_review.md | assets are relevant, credible, and safe |
| Build | PPT executor | matrix + specs | native PPTX | automated checks pass |
| QA | Evidence Collector / Reality Checker | rendered pages | qa_report.md | final verdict justified by evidence |
```

Also record retry policy: `Attempt 1`, `Attempt 2`, `Attempt 3`, then escalate by redesigning the weak slide rather than decorating it.

### 2. Visual Storyteller Pass

Create or update `claim_spine.md`:

- beginning: why this deck exists and the audience tension
- middle: evidence progression and conflicts/tradeoffs
- end: decision, recommendation, or next question
- emotional rhythm: which pages are anchor, breathing, dense, proof, or decision pages
- visual metaphor: the deck's repeated organizing image, e.g. stack, route map, loop, funnel, operating system, maturity gate

Every non-appendix slide must have:

- assertion title
- proof object
- support note
- intended audience reaction

### 3. Brand Guardian Pass

Create `brand_guardian_audit.md` when a brand, organization, event, or default style matters.

Check:

- logo use: authentic local/official asset only; no pseudo-logo drawings
- palette roles: semantic color names, not random accent reuse
- typography: exact font stack and hierarchy
- voice: board brief, launch stage, academic, government, investor, or editorial
- do-not-use list: forbidden colors, decorative styles, icons, image treatments, language tone
- accessibility: contrast and small-text risk

Translate only executable rules into `design_contract.md` and `spec_lock.md`.

### 4. UX/UI Design-System Pass

Before drawing pages, define a small slide component library:

- canvas grid and margin system
- title block positions
- footer/page-label/logo treatment
- chart language
- table language
- route/stack/loop/map/card archetypes
- density budgets for light, medium, dense, and appendix slides
- minimum sizes for labels, captions, and notes

If two slides use similar information, reuse a component or archetype instead of inventing a new layout.

### 5. Asset Prompt And Risk Pass

Use this when a page needs generated or sourced imagery.

For `asset_prompt_pack.md`, each asset prompt must include:

- backend/model preference and fallback path, e.g. Imagen/Gemini/OpenAI/host-native/image_gen
- output filename and expected dimensions
- narrative job
- subject
- context/environment
- composition/camera
- lighting/color grade
- material/texture or illustration treatment
- style reference
- aspect ratio
- negative constraints
- intended slide and crop area
- native overlay plan: which text, labels, logo, and callouts remain editable outside the bitmap
- status: `Pending`, `Generated`, `Needs-Manual`, `Rejected`, or `Replaced-Native`

For `asset_risk_review.md`, check:

- no fake text, logos, seals, institution marks, or UI screenshots
- no generic stock-photo human representation
- no culturally inaccurate clothing, architecture, symbols, or geography
- no clone faces or unrealistic anatomy in generated people images
- generated factual visuals are labeled as conceptual or replaced with native diagrams
- generated scientific-looking imagery is not used as proof, microscopy, benchmark output, source screenshot, or paper evidence
- prompt provenance and backend/model are recorded for every generated asset

Scientific/technical decks should prefer native diagrams, charts, paper/source cards, and annotated screenshots over generated decorative imagery.

### 6. Evidence Collector Pass

After export, render the PPTX to PNG pages and a montage. In `qa_report.md`, include:

- rendered preview path
- what the contact sheet actually shows
- 3-5 issues found on first pass, or a clear explanation of why fewer issues remain after fixes
- exact slide IDs changed after QA
- before/after note when a slide was redrawn

Visual QA must trust screenshots over intention. If a rendered page has text collision, weak hierarchy, or tiny labels, it fails even if the SVG source looked acceptable.

### 7. Reality Checker Pass

Final verdict defaults to `NEEDS WORK`.

Only mark `READY` when:

- automated QA passes
- native editability check passes
- montage has no visible collisions
- every page has a claim and proof object
- brand rules are followed
- sources/provenance are documented for factual claims and non-native assets
- residual risks are explicitly listed

Avoid inflated scores. A first "good" deck can still be `NEEDS WORK` if the contact sheet lacks variety, proof, or executive clarity.

## PPT Handoff Template

Use inside `agent_workflow_plan.md` or `qa_report.md` when a phase changes.

```markdown
## Handoff: [Role] -> [Role]

- Input:
- Output:
- Acceptance criteria:
- Evidence required:
- Known risks:
- Next action:
```

## What To Borrow From The Local Agents

- From `design-visual-storyteller.md`: narrative arc, emotional journey, visual pacing, data storytelling, progressive disclosure.
- From `design-brand-guardian.md`: brand foundation, visual identity system, voice rules, consistency audit.
- From `design-ux-architect.md` and `design-ui-designer.md`: tokens, spacing, typography hierarchy, reusable components, developer-ready specs.
- From `design-image-prompt-engineer.md`: subject/context/lighting/camera/style/negative-prompt structure for generated imagery.
- From `design-inclusive-visuals-specialist.md`: explicit anti-bias and authenticity checks for people/culture/place imagery.
- From `testing-evidence-collector.md` and `testing-reality-checker.md`: screenshots as proof, default skepticism, no fantasy approvals.
- From NEXUS coordination docs: phase gates, handoff templates, retry loops, and evidence-based progression.
