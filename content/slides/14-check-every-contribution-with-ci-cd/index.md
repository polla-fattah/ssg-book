---
title: "Check Every Contribution with CI/CD"
description: "Chapter 14: a checks workflow, branches, and pull requests, so a change is tested before it is merged."
book_number: "14"
weight: 15
---

# Check Every Contribution with CI/CD

Static Site Generators in the Age of AI

**Chapter 14**

Polla Fattah

---

## Today's goal

Every change so far went straight onto `main`, and **every push to `main` publishes**.

- A second workflow that **examines** a proposal before it goes live
- A **branch** and a **pull request**
- A rule broken **on purpose**, and stopped

> Machines check what can be a rule; you check the rest.

---

## By the end of today you can

- **Work** on a branch and propose a change through a pull request
- **Read** a workflow's triggers, jobs, steps, and permissions
- **Run** the same checks locally before pushing
- **Explain** what a passing check does, and does not, establish

Start from Chapter 13 (branch `chapter-13`): clean, pushed, and publishing through Chapter 7's workflow.

---

## Three rules the book already set

| Rule | Where it came from |
| --- | --- |
| Directory flags are real **Booleans** | Chapter 12's quoted `"false"` |
| Internal links stay **relative** | Chapter 8's `/articles/` mistake |
| Articles and projects have a **description** | Chapters 9 and 13's content models |

Plus a build with warnings treated as failures.

---

## A workflow that only reports

Create `.github/workflows/checks.yaml`. It begins:

```yaml
name: Check proposed changes
on:
  pull_request:
    branches: [main]
permissions:
  contents: read
```

Then one job, `checks`, on `ubuntu-24.04`: check out, install Hugo **exactly as in Chapter 7**, and build.

---

## The Boolean and link checks

```yaml
- name: Check that directory flags are Booleans
  shell: bash
  run: |
    if grep -n '"start_here": *"' assets/data/resource_links.json; then
      echo "start_here must be an unquoted Boolean: true or false."
      exit 1
    fi
```

The link check is the same shape, searching `content/` for `](/`.

---

## The description check

```yaml
- name: Check that articles and projects have a description
  shell: bash
  run: |
    status=0
    for page in content/articles/*/index.md content/projects/*/index.md; do
      if ! grep -q '^description:' "$page"; then
        echo "Missing description: $page"
        status=1
      fi
    done
    exit "$status"
```

---

## Commit it to main

```text
git add .github/workflows/checks.yaml
git diff --cached
git commit -m "Add checks for proposed changes"
git push
```

- The publishing workflow runs as usual: it still watches `main`
- No page changes
- The new workflow does **nothing yet**: no pull request exists

The chapter gives the complete file.

---

## The parts you rely on

| Part | Its job |
| --- | --- |
| `on: pull_request` | Runs when a change is **proposed** against `main` |
| `permissions: contents: read` | Read the source, **nothing else** |
| `runs-on: ubuntu-24.04` | A fresh **runner** machine for the job |
| `uses:` | Runs a published action, such as checkout |
| `run:` | Runs shell commands on the runner |

---

## Two deliberate differences

- **Trigger**: `pull_request` examines a **proposal**; Chapter 7's `push` to `main` publishes what is **accepted**
- **Permissions**: publishing needs `pages: write` and `id-token: write`; checking needs only `contents: read`

A job fails when any step exits **non-zero**. `grep` succeeding means it **found** the forbidden thing, so `exit 1`.

**CI**: changes checked as they are proposed. **CD**: delivery, our Chapter 7 workflow.

---

## Run the checks locally first

```text
hugo --minify --panicOnWarning
grep -n '"start_here": *"' assets/data/resource_links.json
grep -rn '](/' content/
grep -c '^description:' content/articles/*/index.md content/projects/*/index.md
```

- The first two `grep` commands should print **nothing**
- The last prints a count per page, and one says **`0`**: the first learning note

A check you can only run on GitHub is a slow way to find a typing mistake.

---

## Raise the content, not the rule

The first learning note predates the article model. The check is **correct**; the page is **out of date**. Add to its front matter:

```yaml
description: "Editing a page in my notebook, checking the result, and recording what changed."
```

Rerun: every page reports `1`. Commit and push the repair on `main`.

A wrong rule? Change it **deliberately**, and say why. Never quietly exempt one file.

---

## Propose a change on a branch

```text
git switch -c add-actions-resource
git status
```

- `-c` creates the branch and moves onto it
- A branch is a **name for a line of commits**, not a second folder
- Nothing reaches the live site until the branch is **merged**

---

## A fifth record, at the end of the array

```json
{
  "title": "GitHub: Actions documentation",
  "url": "https://docs.github.com/en/actions",
  "description": "...",
  "topics": ["GitHub Actions", "Automation"],
  "start_here": false
}
```

Add a comma before it. Its description: *The official reference for automating builds, checks, and deployments on GitHub.*

---

## Push the branch

Preview Resources, then:

```text
hugo --minify --panicOnWarning
git add assets/data/resource_links.json
git diff --cached
git commit -m "Add the GitHub Actions documentation to the resource directory"
git push -u origin add-actions-resource
```

`-u` connects the branch to GitHub for later pushes.

This push publishes **nothing**: you are not on `main`.

---

## Open a pull request

A **pull request** proposes merging one branch into another. On GitHub, or:

```text
gh pr create --base main --head add-actions-resource --fill
gh pr checks
```

| Read | It tells you |
| --- | --- |
| Files changed | The actual diff |
| Checks | Passed, running, or failed |

---

## Read a passing log first

Open the check run and expand its steps:

- Checkout
- The Hugo install
- A successful build
- Three rule checks, reporting **nothing**

Reading a passing log now makes a failing one far easier to read later.

Leave the pull request **open**: the next step gives it something to catch.

---

## Break a rule on purpose

On the branch, quote the new record's flag:

```json
"start_here": "false"
```

```text
git add assets/data/resource_links.json
git commit -m "Temporarily quote the start_here flag to test the checks"
git push
```

The checks run again, and the pull request turns **red**.

---

## Read the failure from the top

- **Build the website** succeeded: this is valid JSON
- **Check that directory flags are Booleans** failed, printing the line and the message
- The **first** failing step is the one to act on; later steps may not have run

Restore `"start_here": false`, check **locally**, commit, and push: the checks pass.

> A machine caught a broken rule before publication.

---

## Require the check

In **Settings**, create a **ruleset** for `main` that requires the `checks` status to pass.

- The check must have **run once** before GitHub can offer it
- As the owner, you can usually still **bypass** your own rule
- For a solo author it is a reliable **reminder**: bypassing becomes deliberate, not an oversight

GitHub will not let you approve your **own** pull request: review means reading Files changed yourself.

---

## What a green check means

| The checks establish | Only you can establish |
| --- | --- |
| The site builds, warnings as failures | The writing is accurate |
| Directory flags are Booleans | The resource is worth listing |
| Internal links are relative | They go where a reader expects |
| Pages have a description | It describes the page honestly |

A green check is **permission to look properly**, not a verdict. Chapter 13's unsupported sentence passes all four.

---

## Merge and verify

Read Files changed once more: **one** added record. Merge it.

Merging **is** a push to `main`, so the publishing workflow runs:

- Both workflows in the Actions history, with distinct names
- The live Resources page: five records, one Start here label
- The first learning note, Projects, navigation, and footer: unchanged

---

## Back on main

```text
git switch main
git pull
git log --oneline -5
git status
git branch -d add-actions-resource
```

The branch's work now lives on `main`. Delete the remote branch from the pull request page.

The pull request keeps the mistake and its correction: an **honest** history.

---

## Try it yourself

Make one proposal of your own, on a new branch:

- Give the reading-list project a more specific **description**, or
- Add one **topic** label to a directory record

Push it, open a pull request, read the checks, **review your own diff**, and merge when both you and the checks are satisfied.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| The checks do not run | It triggers on `pull_request` only |
| A page you did not touch fails | Expected at first: raise it to the rule |
| The build fails; rules do not run | Steps stop at the first failure |
| Pushing the branch published the site | Were you on `main`? |
| The check is not selectable | It must have run once |

---

## Completion check

- I can explain the checks workflow's trigger and narrow permissions
- I ran the three rule checks locally
- I raised an older page to the rule instead of weakening it
- I opened a pull request without publishing anything
- I broke a rule, found the failing step, and repaired it
- I required the check, and know what my bypass means
- I can name something true that no check here could establish
- I merged, watched it deploy, and verified the live result

---

# Next: Help Readers Find and Use Your Content

Chapter 15: search, navigation, titles, descriptions, sitemaps, and feeds.

**polla.dev/ssg-book**
