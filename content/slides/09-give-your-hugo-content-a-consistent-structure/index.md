---
title: "Give Your Hugo Content a Consistent Structure"
description: "Chapter 9: a content model, YAML front matter, and an archetype for project pages."
book_number: "9"
weight: 10
---

# Give Your Hugo Content a Consistent Structure

Static Site Generators in the Age of AI

**Chapter 9**

Polla Fattah

---

## Today's goal

After a few projects, one page explains its purpose, another lists tools, and a third never says whether the work has started.

- Agree what **every project page** should explain
- Build a reusable **starter** for new projects
- Add a second project: a planned **reading list**

A shared structure is easier to write, compare, maintain, and hand to an **agent**.

---

## By the end of today you can

- **Choose** a few useful fields and headings for a kind of content
- **Read and edit** the basic YAML in Hugo front matter
- **Create** a page from an archetype, and tell its path from its title
- **Preview** a draft, review it, and link it from Projects

Start from Chapter 8 with a **clean** working tree (companion branch `chapter-08`).

---

## Improve the existing project

Replace only the front matter of `content/projects/learning-notebook/index.md`:

```yaml
title: "My knowledge notebook"
description: "A personal website for learning notes, small projects, and useful references."
draft: false
params:
  status: "in-progress"
  tools:
    - "Hugo"
    - "Markdown"
```

Then update its Current status paragraph and add a `## Next step` section.

---

## What you will not see

- **No** status label and **no** tools list on the page
- The layout shows only the title and the body
- Storing a value does **not** teach the layout to display it

The source now holds information **later templates can use**. The visible change came from the body text you edited.

> Metadata is stored today and displayed in Chapter 10.

---

## A content model: front matter

A **content model** is an agreement about what a kind of content contains.

| Field | Our rule |
| --- | --- |
| `title` | A readable project name |
| `description` | One sentence on the project's purpose |
| `draft` | Is the **page** still being prepared? |
| `params.status` | `planned`, `in-progress`, or `complete` |
| `params.tools` | A list of tools; empty is fine |

---

## A content model: the body

| Heading | What goes under it |
| --- | --- |
| Purpose | What the project is meant to achieve |
| Current status | What has **actually** happened |
| What I have learned | Specific learning, or an honest "not begun" |
| Next step | One concrete action, or a clear completion statement |

The three status values are **our** choice: Hugo will not reject a fourth. No owner, budget, or percentage: the model is also a **scope limit**.

---

## Page readiness is not project progress

- `draft` describes the **page**
- `status` describes the **project**

```yaml
draft: false
params:
  status: "planned"
```

An honest plan, published. `status` is the quick answer; the body gives the evidence. **They must agree.**

---

## YAML: text values

```yaml
title: "My knowledge notebook"
title: "Reading list: website publishing"
title: 'Notes on "static" websites'
```

- `title` is the **key**; after the colon and a space comes the **value**
- Quote text values: essential when the text contains a colon
- **Straight** quotes, never curly ones from a word processor
- Text containing `"`? Wrap it in single quotes

---

## YAML: true, false, and lists

```yaml
draft: false
params:
  tools:
    - "Hugo"
    - "Markdown"
```

- `true` and `false` are **Booleans**: lowercase, unquoted
- **Indentation** is structure: two spaces per level, **never tabs**
- `params` groups values; dashes make a **list**; `[]` is an empty one

---

## Read the source

Point to the value that answers each question in your notebook project:

1. What should the page be called?
2. Is the page ready for an ordinary build?
3. Is the project finished?
4. Which tools does the page record?

Can you answer all four? You know enough YAML for today. More formats come in Chapter 12.

Custom values go under **one** `params` block; never add a second.

---

## Predictable pages and addresses

| Source | Job |
| --- | --- |
| `content/projects/_index.md` | The Projects section and its manual links |
| `content/projects/learning-notebook/index.md` | One project |
| `content/projects/reading-list/index.md` | Our second project |

- A folder with an `index.md` is a **leaf bundle**: the page and its own files
- The **folder** sets the address; renaming it breaks links. The **title** can change freely

---

## An archetype: a starter for new pages

Copying an old project copies its claims too. Create `archetypes/projects.md`:

```markdown
---
title: "Replace with a project name"
description: "Replace with one sentence about the project's purpose."
draft: true
params:
  status: "planned"
  tools: []
---
```

---

## The archetype's body

It continues with four headings, each with a prompt:

```markdown
## Purpose

Explain what this project is intended to achieve.

## Current status

Describe what has actually happened so far.
```

Then **What I have learned**, **Next step**, and a Back to Projects link.

---

## Create the second project

Stop the preview, then from the project root:

```text
hugo new content --kind projects projects/reading-list/index.md
```

- `--kind projects` chooses the archetype; it is **not** the project's status
- The path is inside `content/`: do not add `content/` yourself
- It already exists? **Inspect it**; never force an overwrite

Editing an archetype later does **not** change pages already created from it.

---

## Replace the prompts with the truth

```yaml
title: "My website reading list"
draft: true
params:
  status: "planned"
  tools:
    - "Markdown"
```

Add a one-sentence `description`, and a body that says honestly: a proposal, nothing reviewed yet.

**A page about a plan is not evidence that it was carried out.**

---

## Preview the draft

```text
hugo server -D
```

Open the page directly, since Projects does not link to it yet:

```text
http://localhost:1313/my-knowledge-site/projects/reading-list/
```

- Read the whole page; follow **Resources** and **Back to Projects**
- `-D` shows drafts; it does **not** make a page ready

---

## Decide to publish

1. Change only `draft: false`, and keep `status: "planned"`
2. Restart with plain `hugo server` and reopen the page
3. In `content/projects/_index.md`, under `## Current work`, add:

```markdown
- [My website reading list](reading-list/): A planned collection of
  resources for learning website publishing.
```

The list is still **manual**: Chapter 10 automates it.

---

## What draft does not do

- A draft is **not private**: its Markdown is readable in a public repository
- Turning a published page back into a draft does not reliably **withdraw** it: old output can remain
- A manual link can point to a page an ordinary build **excludes**

Keeping it as a draft? Keep `draft: true`, and add the Projects link later.

---

## Break the front matter on purpose

Stop the server, and remove the closing quote from the title:

```yaml
title: "My website reading list
```

```text
hugo --minify --panicOnWarning
```

The build **fails** and names the file. The reported line may be where parsing gave up, not where the quote went missing. Restore the quote and build again.

---

## Two different checks

| Check | Question | Who checks it |
| --- | --- | --- |
| Can the file be processed? | Valid YAML, closed quotes | Hugo |
| Does it meet the model? | `planned`, not `planed` | You |
| Does it describe reality? | No invented tools or progress | You |

Compare both pages with the model, and look for leftover starter prompts.

---

## Try it yourself

- Rewrite the reading list's **Next step** as a real action you could later confirm
- Review its **tools** list: keep Markdown, choose your real plan, or use `[]`
- Do not add fields just to look sophisticated

Optional: ask the agent, **read-only**, to check both pages against the model. It can compare files with an agreement; it cannot confirm work done outside them.

---

## Save the checkpoint

```text
hugo --minify --panicOnWarning
git status
git add archetypes/projects.md content/projects/_index.md
git add content/projects/learning-notebook/index.md
git add content/projects/reading-list/index.md
git diff --cached
git commit -m "Define a consistent project model and add a reading-list project"
```

Open both **new** files before staging: `git diff` does not show untracked files.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| Status or tools are not on the page | Expected: the layout does not show them yet |
| A YAML parsing error | Quotes, colons, indentation, both `---` lines |
| The wrong starter appears | `archetypes/projects.md` and `--kind projects` |
| The new page is not in a normal preview | `draft`, the filename, the address |

---

## Completion check

- Both projects use the agreed fields and headings
- I can tell page readiness from project progress
- I can read text, a Boolean, a mapping, and a list in YAML
- I created the second project from the archetype and replaced its prompts
- I checked it in the normal preview and tested its links
- I repaired the deliberate YAML mistake and reviewed the information
- I committed the four intended files

---

# Next: Use Hugo Templates to Display Your Content

Chapter 10: expressions, conditions, and a loop that turns pages into a useful list.

**polla.dev/ssg-book**
