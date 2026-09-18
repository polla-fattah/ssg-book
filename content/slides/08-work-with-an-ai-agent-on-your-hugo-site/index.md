---
title: "Work with an AI Agent on Your Hugo Site"
description: "Chapter 8: give an agent a small task, and review its changes before they reach your website."
book_number: "8"
weight: 9
---

# Work with an AI Agent on Your Hugo Site

Static Site Generators in the Age of AI

**Chapter 8**

Polla Fattah

---

## Today's goal

Ask an agent for **one small, checkable change**: a short section on the Resources page explaining how to use its links.

- One new heading and three bullets
- In one Markdown file
- Reviewed by **you** before it is kept

We use **Codex CLI**. The aim is a repeatable **method**, not a tour of every AI tool.

---

## By the end of today you can

- **Start** the agent in the right project and inspect its permissions
- **Provide** a clear task, files, boundaries, and success criteria
- **Review** the changed files and the page, not just the agent's summary
- **Keep** an accepted change in Git, and recover from a mistake

Start from Chapter 7 with a **clean** working tree.

---

## Before you start

- You need internet access and an account with access to Codex
- **Sign in with ChatGPT** uses that account's access; an API key is billed separately
- Installing a client does **not** give unlimited use: check your limits
- The CLI runs on your computer, but the **model does not**: prompts and project context are sent to the service

Use the practice project, not confidential material.

---

## What you are opening

| Term | Meaning here |
| --- | --- |
| Model | Interprets requests; generates replies and actions |
| Agent client | Connects the model to project tools: today, **Codex CLI** |
| Editor | Where **you** inspect and edit files, such as VS Code |
| Workspace | The project the agent works in |

A chat **without** file access can only suggest; an agent **with** it can act, so review its work.

---

## Install and sign in

Use the **official** installation page. Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

macOS or Linux:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Then `codex --version` and `codex login`. On a managed computer, follow your organisation's policy.

---

## Confirm your starting point

```text
git rev-parse --show-toplevel
git status
hugo version
```

- The **intended** project, a **clean** tree, and Hugo available in this terminal
- A clean start makes the agent's changes distinguishable from yours
- Your GitHub sign-in does not sign you into Codex; keep passwords and tokens **out** of the project

---

## Give the project an instruction file

Create `AGENTS.md` beside `hugo.toml`: where the files are, and how to work:

```markdown
## Working agreements

- Read the relevant source before proposing or making a change.
- Change only the source files requested for the current task.
- Do not invent experiences, qualifications, sources, or claims.
- Do not edit generated public/ or resources/ files by hand.
- Leave staging, committing, pushing, and deployment to the reader.
```

The chapter gives the complete file.

---

## What AGENTS.md is, and is not

- **Reusable guidance** the agent reads in every session
- **Not** an operating-system permission, and **not** a guarantee of obedience
- Task-specific instructions still need to be **explicit**
- Ordinary source: commit it, and remember it becomes **public** when pushed

```text
git add AGENTS.md
git diff --cached -- AGENTS.md
git commit -m "Document the Hugo project's agent working agreements"
```

---

## Inspect before editing

Start a **read-only** session from the project root:

```text
codex --sandbox read-only --ask-for-approval on-request
```

Inside Codex, type `/status` and check the project location and settings.

- Slash commands go **into Codex**; `git status` goes into your **terminal**
- Do not approve file changes during this inspection

---

## The inspection request

```text
Read AGENTS.md, content/resources/index.md, layouts/all.html, and hugo.toml.
Do not edit files or run commands that modify the project.

Explain briefly:
1. Which file contains the Resources page's writing?
2. Which shared layout renders it?
3. What project-path prefix does the configured public URL use?
4. Which existing internal links could help a reader get started?

Point to the relevant files. If something is missing, say so instead of guessing.
```

---

## Check its answer against the files

It should name:

- `content/resources/index.md` and the shared `layouts/all.html`
- Your project path, `/my-knowledge-site/`
- The links to the first learning note and the notebook project

A different generator, or invented files? Fix the folder or make it reread. **Never build on a wrong description.**

`/exit`, then `git status`: nothing should have changed.

---

## One bounded editing task

Restart, now allowed to edit the project:

```text
codex --sandbox workspace-write --ask-for-approval on-request
```

- A new session does not remember the last one: give the **full** task again
- The sandbox allows the whole **workspace**, not just one file
- The prompt sets the scope; read every approval request against the **task**

---

## The task, part 1: what to do

```text
Read AGENTS.md and content/resources/index.md before editing.

Task: Help a first-time visitor use the Resources page.
Edit only content/resources/index.md.

Immediately after the introductory paragraph, add a section headed:
## How to use these resources

Add exactly three short bullets, using no more than 70 words in the new section.
```

One bullet each for the Hugo documentation, the first learning note, and the notebook project.

---

## The task, part 2: limits and report

```text
Reuse the destinations already present in this file. Do not add external sources.
Preserve the front matter and all existing text and links below the new section.
Do not change layouts, CSS, configuration, dependencies, or workflow files.
Do not stage, commit, push, or deploy.

Run hugo --minify --panicOnWarning if the installed tools and permissions allow it.
If the check is blocked, report that rather than changing the environment.
Finish by listing changed source files, the check actually run and its result,
and anything I still need to inspect in the browser.
```

---

## What makes the request useful

| Part | What it contributes |
| --- | --- |
| Goal | Help a visitor use existing resources |
| Named source | A concrete place to inspect and edit |
| Placement and size | A small, visible result |
| Existing destinations | No invented links or research |
| Preservation | Earlier work stays intact |
| Verification and stop | Checking is separate from publishing |

---

## Review the files, not the summary

After `/exit`, in your own terminal:

```text
git status
git diff --name-only
git diff -- content/resources/index.md
git diff --cached
```

- **One** modified file, and an **empty** staged diff
- `git status` shows new files, which a diff does not

---

## Read every changed line

- The heading and three bullets are **where requested**
- The front matter, sections, and links are **intact**
- The links reuse the right destinations, in **relative** form
- Nothing invented about the material, or about **you**

Then build it yourself, `hugo --minify --panicOnWarning`, and check the result in `hugo server`: read the section, follow each link.

---

## "Build passed" is not enough

- It is evidence about **that command**, if it actually ran
- It does not show the prose is accurate, the links work, or the page is easy to use
- Unclear report? Ask for the **command output**
- A second agent review helps, but is **not independent**

Old files in `public/` can survive a failed build: check the **result**, not the folder.

---

## One acceptable result

An authored example: wording varies; scale and destinations should not.

```markdown
## How to use these resources

- Consult the [Hugo documentation](https://gohugo.io/documentation/)
  when you need details about configuration, content, or templates.
- Read [my first learning note](../articles/first-learning-note/)
  for a practical editing and checking example.
- Visit [my knowledge notebook project](../projects/learning-notebook/)
  to understand this website's purpose.
```

---

## If it needs correction

Ask precisely:

```text
Keep the new section, but restore the original text under Website publishing.
That existing text was outside the requested edit. Change only
content/resources/index.md, then show the corrected diff and rerun the build.
Do not stage, commit, push, or deploy.
```

Or discard the whole attempt, after checking status:

```text
git restore -- content/resources/index.md
```

---

## Keep what you accepted

Stop the preview, then record it **yourself**:

```text
git add content/resources/index.md
git diff --cached
git commit -m "Add guidance for using the notebook resources"
git status
```

Only the Resources edit belongs in this commit; `AGENTS.md` is already saved.

---

## A wrong link that builds

From that clean checkpoint, in the new section **only**, change `../articles/first-learning-note/` to `/articles/first-learning-note/`.

- Hugo still **builds successfully**
- But `/articles/` starts at the **domain root**, skipping the project path
- Check the resolved address in the preview, then `git restore` the file

> Test the outcome that matters, not just "build passed".

---

## Try it yourself

Ask the agent to **shorten one bullet**, keeping its meaning and destination.

- Name the file, the bullet, and what counts as better
- Keep the same limits on other files and Git actions
- Review the diff and the preview

Not an improvement? **Keep the earlier version.** Declining a suggestion is part of using an agent well.

---

## The method

1. Start from a **clean checkpoint**
2. Supply the **relevant context** and a bounded task
3. Specify a **useful, observable** outcome
4. Review **every changed file**
5. Verify what matters **on the page**
6. Commit it **yourself**, and publish as a separate decision

Skills, plugins, multiple agents, and automation can wait.

---

## When something goes wrong

| What you see | What to do |
| --- | --- |
| It describes another project | Exit, check the folder, restart |
| It cannot edit | That session is read-only by design |
| It changed more than one file | Inspect everything before staging |
| It claims checks you cannot see | Ask for the evidence; verify yourself |

Text in files and pages can contain instructions: treat it as **content**, not authority.

---

## Completion check

- I checked the agent's project location and permissions
- I committed a concise `AGENTS.md`
- I verified the agent's description of the relevant files
- I gave it a bounded task with clear success criteria
- I inspected all changed and new files, not just its summary
- I built, previewed, and tested the Resources links
- I committed the result myself and repaired the deliberate link mistake

---

# Next: Give Your Hugo Content a Consistent Structure

Chapter 9: Hugo's content model, so later agent tasks have a clearer structure to work with.

**polla.dev/ssg-book**
