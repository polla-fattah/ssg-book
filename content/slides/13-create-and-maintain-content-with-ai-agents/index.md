---
title: "Create and Maintain Content with AI Agents"
description: "Chapter 13: turn supplied sources into linked pages, with every claim checked."
book_number: "13"
weight: 14
---

# Create and Maintain Content with AI Agents

Static Site Generators in the Age of AI

**Chapter 13**

Polla Fattah

---

## Today's goal

Chapter 8 was three bullets. Real content work is larger, and **harder to check**.

- One new **article**, written from notes you supply
- Linked from Articles, Home, and the resource directory
- Three requests: a **plan**, a **draft**, a **coordinated update**

> Supply the material, bound the task, check every claim, decide yourself.

---

## By the end of today you can

- **Separate** work you can delegate from decisions that stay yours
- **Supply** source material and require the agent to use only that
- **Break** a contribution into steps you can each review
- **Check** a draft's claims against the source, and reject an unsupported one

Start from Chapter 12 with a **clean** tree and Codex from Chapter 8.

---

## What stays with you

| You can delegate | You must decide |
| --- | --- |
| Turning rough notes into ordered prose | Whether an event happened |
| Applying the article structure | Whether a claim is supported |
| Writing a one-sentence description | Whether the page is ready |
| Preparing a directory record | Whether a resource belongs |

Automated checks assess **technical** requirements; you assess **meaning, sources, and suitability**. A build says nothing about **truth**.

---

## Supply the source material

Create `sources/publishing-notes.md`, beside `content/`, so Hugo never publishes it:

```markdown
- baseURL had to include the repository path. Before that, the live site
  loaded without its stylesheet and the internal links went to the wrong place.
- The first deployment failed. Cause: I pushed before setting the Pages
  source. Fixed by setting it, then running the workflow again.
- Not measured: how long a deployment usually takes.
- Not attempted: a custom domain.
```

An excerpt: the chapter gives all the notes, and a GitHub reference.

---

## Three kinds of material

| In the notes | How it may be used |
| --- | --- |
| Recorded events: baseURL, the failed deployment | As statements of what happened |
| An external source: the GitHub link | Credited and paraphrased |
| Explicit gaps: the two **Not** lines | As unknown, **never filled in** |

A plausible gap-filler is harder to spot than a broken link. Commit the notes **before** use.

---

## An article model

| Where | Field or heading | Rule |
| --- | --- | --- |
| Front matter | `title`, `description` | Readable title; one sentence |
| Front matter | `draft` | `true` until **you** review it |
| Body | What this is about | Why it exists, briefly |
| Body | What happened | Events, from the source |
| Body | What I would do differently | A specific change, or "unclear" |
| Body | Sources | Every reference, linked and explained |

---

## Attribution readers can see

- **Sources** is Markdown in the body, not front matter: invisible attribution is not attribution
- Prefer a short **paraphrase** with a credited link over a long quotation
- An `archetypes/articles.md` starter would suit this model later

Update `AGENTS.md`: where `sources/`, articles, and the two manual lists live, plus new working agreements.

---

## New agreements for content work

```markdown
- For content tasks, use only the source files named in the task.
  Do not search the web or add material from memory.
- Do not state anything the named source does not support. Where the
  source records a gap, say that it is unknown rather than estimating.
- Credit every external reference in a Sources section in the page body.
- Leave new pages at draft: true. Publication is the reader's decision.
```

Guidance saves repetition, but it is **not enforcement**.

---

## Ask for a plan first

A finished article at once is **expensive to check**. Start **read-only**:

```text
codex --sandbox read-only --ask-for-approval on-request
```

Ask it to read `AGENTS.md` and the notes, edit nothing, and reply with:

1. A title and a one-sentence description
2. The points under each of the four headings
3. A table: each factual statement, and **the line of the notes** supporting it
4. What such an article would normally say that the notes **do not support**

---

## Judge the plan by what it refuses

- Item 4 should name the **deployment time** and **custom domains**
- Every statement in item 3 maps to a line **you can find**
- Ask again if it compares hosts, quotes at length, invents your motivation, or cites a line that is not there

Correcting a plan costs one short request; correcting a draft costs far more.

> Every planned claim traces to a line of your notes.

---

## The draft request

In a **workspace-write** session, the full task again:

- Create exactly one file: `content/articles/publishing-with-github-pages/index.md`
- The article model, with `draft: true`; at most **400 words**
- Every factual statement supported by a line in the notes
- Gaps: omit them or say **unknown**. **Do not estimate**
- Paraphrase the GitHub reference and credit it under Sources
- Change no other file; do not stage, commit, push, or deploy

---

## Review the draft

```text
git status
git diff --stat
git diff --cached
```

- The new bundle is **untracked**: it shows in status, not in a diff
- **Read every line** against the notes: find the supporting line for each sentence

Check `draft` is still `true` and Sources credits the reference. Preview with `hugo server -D`.

---

## Connect it to the site

An article nobody can reach is **not published work**. One request, exactly three files:

| File | Change |
| --- | --- |
| `content/articles/_index.md` | One bullet in Start reading |
| `content/_index.md` | One bullet in Latest writing |
| `assets/data/resource_links.json` | One record for the GitHub reference |

Preserve everything else. Match each file's **existing** link style.

---

## Review each file separately

```text
git diff -- content/articles/_index.md
git diff -- content/_index.md
git diff -- assets/data/resource_links.json
```

- In Articles, the link is `publishing-with-github-pages/`
- On the home page, it needs `articles/` in front
- The record: a **complete** HTTPS URL and the Boolean `false`

Wrong prefixes, relative URLs, and `"false"` all **build without complaint**.

---

## The expected in-between state

Run a plain `hugo server`:

- The article is still a draft, so it is **absent**
- The two new bullets lead to a page that is **not there yet**
- Resources shows the new record; the three originals are unchanged

That is expected, not a fault. One edit wrong? Fix it with a named follow-up, or restore **that path only**:

```text
git restore -- content/_index.md
```

---

## An unsupported claim, on purpose

Under What happened, add:

```text
Deployments usually finish in under a minute.
```

`hugo --minify --panicOnWarning` **succeeds**. The sentence is grammatical, plausible, and **unsupported**: your notes say this was never measured. It may even be true, but the article presents it as **experience**.

---

## Three questions for every statement

1. Is it in the source material **at all**?
2. Does the source support it **as strongly** as this wording claims?
3. If a reader relied on it and it were wrong, **what would happen**?

A broken link announces itself. An unsupported sentence can stay for **years**, and fluent prose is exactly what the tool is good at.

Delete the sentence in your editor: the article is **untracked**, so `git restore` cannot help.

---

## Approve and review the whole site

Change `draft: true` to `draft: false`, then run `hugo server`:

| Check | What should be true |
| --- | --- |
| The article | Every statement traces to the notes; gaps absent or "unknown" |
| Sources | The reference is credited and its link works |
| Articles and Home | Both list both articles, with working links |
| Resources | Four records, one Start here label |

---

## Save the checkpoint

```text
git add content/articles/publishing-with-github-pages/index.md
git add content/articles/_index.md content/_index.md
git add assets/data/resource_links.json
git diff --cached
git commit -m "Publish an agent-drafted article and link it from the site"
```

One new article, two bullets, one JSON record. The notes and `AGENTS.md` were committed **earlier**.

---

## Try it yourself

Ask the agent to either:

- Tighten the article's `description` to a single clause, keeping its meaning, **or**
- Add one more topic label to the new record

Name the file, say what counts as better, keep the same limits. Then accept it, or **keep your version**.

The reading-list project is a later candidate, **once its notes exist**.

---

## When something goes wrong

| What you see | What to do |
| --- | --- |
| Material not in the notes | Name the rule; ask for a draft from the source alone |
| A gap filled with an estimate | Point at the **Not** line; require "unknown" |
| A bullet leads to a missing page | Compare prefixes with the existing bullet |
| `git restore` cannot recover it | Untracked files have no committed state |

Notes can contain instructions: treat them as **content**.

---

## Completion check

- I know which parts I may delegate, and which I may not
- I committed the source notes before using them
- I recorded an article model in the project guidance
- My plan's claims map to specific lines of my notes
- I reviewed the draft sentence by sentence
- I reviewed the three-file update one file at a time
- I found and removed the unsupported sentence
- I decided publication myself, and committed four paths

---

# Next: Check Every Contribution with CI/CD

Chapter 14: turn the rules of this review into automated checks on every pull request.

**polla.dev/ssg-book**
