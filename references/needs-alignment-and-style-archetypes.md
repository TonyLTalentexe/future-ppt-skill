# Needs Alignment And Style Archetypes

Use this reference at the start of every serious PPT task, before slide design or SVG generation.

The deck's design language should be selected from audience, purpose, decision context, and content risk. Do not start by choosing colors or decoration.

## Alignment Gate

Create `needs_alignment_brief.md` before `slide_brief_matrix.md`.

If the user has not provided enough context, ask up to three concise questions before producing the deck, unless they explicitly ask to proceed immediately. Do not ask for information that can be inferred from the source document, file path, meeting title, or prior context.

If the task is urgent or the user says "直接做", proceed with explicit assumptions in `needs_alignment_brief.md` and mention the assumptions in the final handoff.

## Required Brief

```markdown
# Needs Alignment Brief

## Situation
- source_files:
- meeting/context:
- audience:
- audience_knowledge_level:
- presenter:
- decision_or_action_needed:
- time_budget:

## Deck Job
- primary_goal:
- secondary_goal:
- what_success_looks_like:
- final_deliverable:
- expected_length:
- reading_mode: live presentation / leave-behind / both

## Content Contract
- must_include:
- nice_to_have:
- must_not_include:
- sensitive_or_uncertain_content:
- required_evidence:
- expected_appendix:

## Style Direction
- selected_archetype:
- reason_for_archetype:
- reference_sources_or_templates:
- density_level:
- visual_posture:
- chart_table_posture:
- image_generation_posture:
- tone_words:
- forbidden_style_moves:

## Assumptions And Open Questions
- assumptions:
- blocking_questions:
- nonblocking_questions:
```

## Three-Question Intake

When context is missing, prefer questions that resolve multiple choices:

1. Audience and decision: "这份 PPT 主要给谁看？希望对方看完做出什么判断或动作？"
2. Content boundary: "哪些内容必须出现？哪些内容不希望出现或需要弱化？"
3. Style archetype: "更像咨询公司汇报、投委会/董事会材料、小米发布会、学术答辩、政府汇报，还是其他参考？"

Ask fewer questions when the answer is already implied. For example, a fund internal talent report can usually infer `audience = investment/research leadership` and `goal = make sourcing/judgment/action easier`, but still may need style and exclusion boundaries.

## Style Archetype Menu

Use archetypes as design logic, not as copied templates. Learn their composition, hierarchy, table logic, chart density, and pacing. Do not claim the output is an official McKinsey/BCG/Xiaomi template unless the user provides such a template and usage rights. After selecting an archetype, load `style-archetype-playbooks.md` for production rules.

| Archetype | Best For | Composition Logic | Visual Language | Avoid |
|---|---|---|---|---|
| McKinsey-style consulting | CEO/strategy/board problem solving | assertion headline, exhibit-first pages, clean charts, MECE sections, strong takeaway boxes | white or very restrained background, crisp grids, waterfall/bar/2x2, compact footnotes | cinematic decoration, vague icons, unsupported claims |
| BCG-style strategic narrative | market maps, portfolio choices, transformation | big strategic frame, opportunity maps, matrices, journey, bold section pages | slightly warmer/editorial, geometric blocks, strong charts and scenario pages | over-dense tables without implication |
| Bain/operator style | action plan, GTM, operations, sales | recommendation first, workstreams, owners, impact/effort, roadmap | pragmatic tables, dashboards, status colors, simple decision boards | overly abstract thesis pages |
| Xiaomi/launch style | product/technology launch, inspiring internal pitch | one claim per page, huge type, dramatic object, rhythm of breath/density | pure dark or stage-like background, strong contrast, hero visuals, minimal prose | tiny charts, many equal cards, long paragraphs |
| Investor/IC memo deck | investment committee, financing, fund decision | thesis, market, team, traction, risks, ask, evidence appendix | restrained premium, strong numbers, proof cards, risk boxes | hiding risks, overly promotional language |
| Government/official report | policy, public institution, formal leadership | formal hierarchy, context-policy-action, stable tables | red/blue or restrained official palette, sober typography, clear captions | edgy neon, speculative visuals |
| Academic/technical defense | experts, scientists, technical review | problem-method-result-contribution, diagrams, citations | clear mechanisms, source figures, equations/tables where needed | marketing language, fake science imagery |
| Design/brand pitch | brand, product, experience proposal | moodboard, principles, options, before/after, concept routes | large images, typographic polish, material/color systems | unexplained business logic |
| Internal operating review | weekly/monthly management, execution | KPI first, variance, root cause, decision/action | dashboard, traffic lights, trend charts, owner/action tables | decorative covers and weak action items |
| Talent/research map |人才挖掘, expert landscape, candidate strategy | landscape map, funnel, tiering, archetype comparison, next actions | network maps, evidence cards, source-backed ranking, restrained highlights | treating candidates as decorative portraits |

## Matching Rules

Choose by purpose:

- If the deck must persuade a senior executive to choose a path, use consulting or strategic narrative.
- If the deck must trigger an investment or resource decision, use investor/IC.
- If the deck must excite or launch, use Xiaomi/launch.
- If the deck must withstand expert scrutiny, use academic/technical.
- If the deck must manage execution, use operating review.
- If the deck must source or compare people, use talent/research map.

Choose by reading mode:

- Live presentation: fewer words, larger claims, stronger pacing, more speaker notes.
- Leave-behind: more evidence, tables, captions, appendices, and source notes.
- Both: main deck stays presentation-readable; appendix carries detail.

## Content Boundary Rules

Define what not to include before writing pages:

- uncertain claims without evidence
- sensitive people/company details
- unsupported rankings
- fake logos, fake screenshots, fake citations, or fake charts
- overly promotional language when the audience expects judgment
- technical details that belong in appendix
- decorative images that do not support the decision

## Template Learning Rules

When using mature templates or references:

- extract page archetypes: cover, agenda, executive summary, exhibit, comparison, roadmap, appendix
- extract grid and margin system
- extract table density and chart grammar
- extract headline style and implication placement
- extract image posture: hero, proof screenshot, object, portrait, none
- extract pacing: dense pages vs breathing pages

Do not copy:

- proprietary slide masters, exact layouts, icons, watermarks, or brand marks without permission
- irrelevant decorative motifs
- template text placeholders

The final deck should feel like it understands the reference's operating logic, not like a pasted template skin.

After template learning, update `design_contract.md` with the selected archetype, page grammar, component families, chart/table posture, and forbidden moves.
