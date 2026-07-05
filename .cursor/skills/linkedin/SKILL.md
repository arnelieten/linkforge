---
name: linkedin
description: Polishes rough LinkedIn post drafts from linkedin-drafts/input/ into five human-sounding post options in linkedin-drafts/output/. Applies Arne Lieten's LinkedIn identity, natural voice rules, and self-check criteria from agent_workforce prompts. Use when the user asks to polish, refine, or batch-process LinkedIn drafts from the input folder.
---

# Polish LinkedIn Drafts

## Folders

| Path | Purpose |
|------|---------|
| `linkedin-drafts/input/` | Rough drafts (`.md` or `.txt`) |
| `linkedin-drafts/output/` | Polished posts (same basename as input) |

Create both folders if they do not exist.

## Workflow

For each file in `linkedin-drafts/input/`:

1. **Read** the rough draft. Preserve the author's topic, angle, examples, and constraints. Do not invent a different subject.
2. **Polish** using [references/style-guide.md](references/style-guide.md).
3. **Write 5 distinct post options.** Each must follow all style rules but vary in hook, angle, or length so the user can pick one.
4. **Self-check** every option against the checklist in the style guide before writing output.
5. **Write** all five options to `linkedin-drafts/output/<same-filename>`.

Process one file at a time. If multiple files exist, process all unless the user names a specific file.

## Output format

Each output file contains **5 post options** the user can choose from. Make each option genuinely different: vary the opening hook, tone (more direct vs more personal), and length (some shorter, some closer to 120 words). Do not produce five near duplicates.

```markdown
# Option 1

[Revised post body: under 120 words, LinkedIn line breaks, 3 to 5 hashtags at end. No dashes.]

# Option 2

[Revised post body]

# Option 3

[Revised post body]

# Option 4

[Revised post body]

# Option 5

[Revised post body]

---

## Visual ideas

1. [One-liner for a visual or meme]
2. [One-liner]
3. [One-liner]
```

Do not wrap posts in code fences in the output file.

## Rewrite rules (summary)

- **No dashes in the post.** Never use em dashes, en dashes, or hyphens as punctuation. They read as AI slop. Use a period, comma, colon, or a new line instead. Rephrase compound words to avoid hyphens where you can ("mid level" not "mid-level").
- Strip AI-giveaway and hype phrases; use plain, concrete language.
- Short lines, clear breaks. No walls of text.
- Strong specific hook; one useful insight; thoughtful takeaway or question.
- Tone: funny, self-aware, informal junior engineer. Not corporate guru.
- Under 120 words including hashtags.

For full identity, voice examples, before/after rewrites, and self-check list, read [references/style-guide.md](references/style-guide.md).

For tone calibration, optionally read 2 or 3 files from `src/agent_workforce/prompt_plugins/example_*.jinja2`.
