# Canva Integration Reference

Use this reference when the user provides a Canva URL/design ID, asks to use Canva, wants stronger template/brand/moodboard help, or needs a separate Canva design deliverable.

## Boundary

- Default final deliverable remains native editable PPTX via `ppt-master`.
- Use Canva as a brand/template/moodboard/reference-design layer.
- Do not silently convert a requested PPTX into a Canva-only deliverable.
- Do not paste Canva pages as whole-slide bitmap images into the final PPTX unless the user explicitly wants a visual mockup rather than editable PowerPoint.
- Local files cannot be imported into Canva through the connector unless they are available via a public HTTPS URL. Keep local-file workflows in `ppt-master` unless the user uploads/shares a public URL.

## What Canva Adds

- Existing design search and reading: find user-owned/shared Canva presentations, read page content, page thumbnails, and presenter notes.
- Brand consistency: inspect/use brand kits and brand templates when available.
- Template acceleration: search brand templates; use autofill only when a template has a non-empty dataset and the user confirms the template.
- Creative ideation: generate Canva presentation candidates through the required outline-review flow.
- Repurposing: import public HTTPS PDFs/PPTX/DOCX/URLs into Canva when the user provides a public URL.
- Editing: update text/media/layout in existing Canva designs through an editing transaction, then commit only after explicit user approval.

## Mode 1: Canva Reference Extraction

Use when the user provides a Canva design URL or design ID.

1. Extract the design ID from `https://www.canva.com/design/{design_id}`. Resolve shortlinks first when needed.
2. Use Canva design metadata, pages/thumbnails, content, and presenter notes to inspect:
   - page count and page rhythm
   - title, body, caption hierarchy
   - dominant visual objects and image posture
   - color palette and repeated components
   - logo/brand placement
   - chart/table/diagram language
3. Write `<project_path>/canva_style_extract.md`.
4. Translate findings into:
   - `visual_evidence_plan.md`
   - `design_contract.md`
   - `spec_lock.md`

Do not copy every Canva element. Extract the system: hierarchy, grid, rhythm, palette, and image strategy.

## Mode 2: Brand Kit / Brand Template Alignment

Use when the user says the deck must be on-brand or asks to use a Canva template.

1. If the user asks for an on-brand design, list brand kits and let the user choose.
2. If the user asks for a template, search brand templates, not existing designs.
3. For generation from template, use only templates with non-empty datasets and confirm the selected template with the user.
4. Inspect dataset fields before autofill.
5. Translate brand/template rules into native PPT constraints:
   - colors → HEX roles in `spec_lock.md`
   - typography → PPT-safe font family and exact sizes
   - logos → project `images/`
   - locked/repeated elements → master-like slide constants
   - page types → deck archetypes

## Mode 3: Canva Creative Candidate / Moodboard

Use only after `slide_brief_matrix.md` and `visual_evidence_plan.md` exist.

For Canva presentation generation:

- Start with Canva outline review. Do not bypass it.
- Keep generated candidate decks short unless the user explicitly wants a full Canva version.
- Treat the candidate as visual R&D unless Canva is the requested deliverable.
- Extract what works: cover composition, image posture, title scale, section rhythm, color pairings, and slide archetypes.
- Rebuild final PPTX natively through `ppt-master`.

## Mode 4: Import / Export Reality Check

- Canva can import public HTTPS files through the connector; it cannot access local `/Users/...` paths.
- Canva Connect APIs support exporting Canva designs to formats including PDF, PNG/JPG, MP4, and PPTX for eligible presentation designs, but the current Codex plugin session may not expose a direct local export tool. Check available tools before promising an export.
- When the final deliverable is a local PPTX, do not depend on Canva export. Use Canva for ideation/reference, then export through `ppt-master`.
- If the user explicitly wants a Canva editable design, deliver the Canva design URL and clearly label it separately from the native PPTX.

## Mode 5: Canva-Assisted QA

Add a Canva section to `qa_report.md` when used:

- Canva source/design/template/brand kit used
- extracted visual rules
- pages that adopted Canva-inspired archetypes
- pages intentionally diverging from Canva and why
- whether final PPTX remained native-editable

Canva design polish does not replace SVG/PPTX QA. Always still render previews, inspect the montage, and run native editability checks.
