---
title: "Maintain, Migrate, and Recover"
description: "Chapter 18: a maintenance pass, dependency updates, archiving without breaking addresses, and undoing a published mistake."
book_number: "18"
weight: 19
---

# Maintain, Migrate, and Recover

Static Site Generators in the Age of AI

**Chapter 18**

Polla Fattah

---

## Today's goal

A site nobody maintains does not stay still: it goes quietly out of date while **appearing to work**.

- A **maintenance pass** over the site you have
- **Update** what you depend on; **archive** superseded work
- Publish a mistake **on purpose**, and recover from it live
- Credentials, licensing, privacy, cost, and ownership

---

## By the end of today you can

- **Run** a repeatable maintenance pass and act on what it finds
- **Update** a pinned dependency in every place it is pinned
- **Retire** a page without breaking a published address
- **Undo** a live change without rewriting published history

Start from Chapter 17 (branch `chapter-17`): clean, pushed, and deployed.

---

## A maintenance pass

| Question | Where to look |
| --- | --- |
| Does any page claim something untrue? | Every body, especially progress |
| Are translations level with their sources? | The `source_checked` dates |
| Does every published address resolve? | The live site |
| Is Hugo pinned the same everywhere? | Both workflows, and `hugo version` |
| Does `AGENTS.md` match the project? | Its file map against the folders |

**Write down** what you find before changing anything.

---

## Two findings to expect

**A stale claim.** The reading-list project still says the reading has not begun and the next step is to choose three resources. The resource directory has done that job since Chapter 12.

Nothing broke, no check failed, and the page has been **quietly wrong for nine chapters**.

**Housekeeping.** The `my-knowledge-site-ch01-backup` folders and their siblings are stale copies, easy to confuse with the live project. **Decide** what to keep.

---

## Hugo is pinned twice

`HUGO_VERSION: "0.150.0"` is in both `hugo.yaml` and `checks.yaml`.

Update one and forget the other, and your checks test with one Hugo while the deployment builds with another. **Both pass**, and what you tested is not what you published.

Add a fifth check to `checks.yaml`: it reads both values and **fails if they differ**.

---

## The version check

```yaml
- name: Check that both workflows pin the same Hugo version
  shell: bash
  run: |
    deploy=$(grep 'HUGO_VERSION:' .github/workflows/hugo.yaml | tr -d ' "' | cut -d: -f2)
    checks=$(grep 'HUGO_VERSION:' .github/workflows/checks.yaml | tr -d ' "' | cut -d: -f2)
    echo "deploy=$deploy checks=$checks"
    if [ "$deploy" != "$checks" ]; then
      echo "The two workflows pin different Hugo versions."
      exit 1
    fi
```

---

## Updating Hugo deliberately

The **third** place the version matters is your computer, and no check reaches it: compare `hugo version`.

1. Read the release notes in between
2. Install locally; build with `--panicOnWarning`
3. Check Projects, Resources, Search, Contact, and both languages
4. Change `HUGO_VERSION` in **both** files, on a branch
5. Let the pull request's checks build the site; then merge

Update action versions **one at a time**, so a failure names its cause.

---

## Archive, do not delete

Superseded, not failed, and its address is published. Add a fourth status:

```yaml
params:
  status: "archived"
```

Say so at the top of the body:

```markdown
**Archived.** The resource directory on the [Resources page](../../resources/)
now does this job, with a shared set of fields for every entry. This page is
kept for its history.
```

---

## A retirement that costs no addresses

- Leave `draft: false`: the page and its address **stay**
- The Chapter 11 status label now tells the **truth**
- The generated Projects list shows it as archived, with **no template change**

That was possible because of the naming decisions in **Chapter 3**, not luck.

---

## When an address must change

Hugo's `aliases` field generates a small page at the old address that **redirects** to the new one. Test the mechanism, temporarily, on Resources:

```yaml
aliases:
  - /projects/reading-notes/
```

Build, find `public/projects/reading-notes/index.html`, and visit the address in the preview. Then **remove** the alias: that address never existed.

An address you published **belongs to everyone who saved it**.

---

## Publish the archive on its own

```text
git switch -c archive-reading-list
git add content/projects/reading-list/index.md
git diff --cached
git commit -m "Archive the superseded reading-list project"
git push -u origin archive-reading-list
```

Merge, then check live: three projects, one **archived**, and `/projects/reading-list/` still resolves. Then `git switch main` and `git pull`.

---

## Publish a mistake on purpose

Archiving **feels** like unpublishing. So, on a new branch, change only `draft: true` in the reading-list page:

```text
git switch -c unpublish-archived-project
git add content/projects/reading-list/index.md
git commit -m "Set the archived project to draft"
git push -u origin unpublish-archived-project
```

The checks **pass**. Merge it.

---

## Invisible damage

1. **Projects** lists two entries instead of three; nothing looks broken
2. `/projects/reading-list/` returns **404**: a published address is gone
3. **No broken link** anywhere: the generated list quietly dropped it

From inside, the site looks **consistent**. Only people holding the old address see the damage.

A draft flag is not a way to **withdraw** a published page, and not a way to archive one.

---

## Undo it with a new commit

```text
git switch main
git pull
git log --oneline -5
```

**Not** `git reset` and a forced push: the change is published. Rewriting history removes the **record**, not what happened.

```text
git revert <commit>
git revert -m 1 <merge-commit>
```

---

## Merge commits and -m 1

- GitHub's default merge button makes a **merge commit**: `Merge pull request #4`
- It joins two histories, so Git cannot tell which to undo: `-m 1` means **what the branch brought in**
- Squash and merge? One ordinary commit: plain `git revert`
- GitHub's **Revert** button opens the undo as a new pull request, through the checks

Then `git show --stat HEAD`, build, and `git push`. Check live: three projects, the address resolves, still archived.

---

## Three ways to undo

| Command | What it does | Right when |
| --- | --- | --- |
| `git restore` | Discards an uncommitted change | Before you commit |
| `git revert` | Adds a commit undoing an earlier one | After it is **published** |
| `git reset --hard` | Moves the branch, discarding commits | Only on work **never shared** |

History now holds the mistake **and** its correction: the honest record.

---

## GitHub is not your backup

A **remote** is for collaborating; a **backup** survives the failure you fear.

| Copy | Protects against |
| --- | --- |
| Your working folder | Nothing on its own |
| GitHub | Losing the computer |
| A clone elsewhere | Losing the **account** |

```text
git clone --mirror https://github.com/YOUR-USERNAME/my-knowledge-site.git
```

---

## What cloning does not restore

- Your GitHub **account** and its recovery methods
- The Pages settings and the Chapter 14 **ruleset**
- A custom **domain** and its registration
- Your **agent** account from Chapter 8

Write down where each lives and how you would regain it.

**A restore you have never thought through is a plan, not a backup.**

---

## Questions with no build step

- **Credentials**: a committed token stays in history: **revoke** it. Prefer tokens that can only read
- **Licensing**: no licence means **no reuse**. License only what you hold; not quotes or borrowed images
- **Privacy**: your site collects **nothing**; GitHub keeps its own logs. Add a third party and the answer changes
- **Cost**: nothing today; check again if anything goes private or grows

---

## What is genuinely yours

- The repository is yours; a domain is **rented**; the platform can change its terms
- The **content** is yours: Markdown, CSS, and templates in a folder you can copy
- Moving hosts means pointing a different build at **the same files**

That portability is the case this book has made. The maintenance pass keeps it **real**.

---

## Write the routine down

Create `MAINTENANCE.md`, with sections for:

- **Every few months**: stale claims, translation dates, addresses, open questions
- **When a dependency changes**: release notes, both workflows, a branch
- **After a live mistake**: `git revert`, not `git reset`; verify the live result
- **Decisions to keep**: the contact form, the four status values, aliases for moved addresses

Keep it a list of **questions**; add one when surprised.

---

## Teach the agent the lesson

Add to `AGENTS.md`:

```markdown
- The maintenance routine is in MAINTENANCE.md.
- Archiving a page means changing its status and saying so in the body.
  It does not mean setting draft: true, which withdraws a published address.
```

A mistake you had to learn becomes a **rule** you no longer need to remember.

Beyond this book: **content reuse** of the JSON directory, and **retrieval** over your own archive.

---

## Propose the rest

```text
git switch -c maintenance-pass
git add .github/workflows/checks.yaml MAINTENANCE.md AGENTS.md
git diff --cached
git commit -m "Add a version check and record the maintenance routine"
git push -u origin maintenance-pass
```

- No leftover **alias** on Resources, no stray edit to the archived page
- The five checks pass; merge and verify the live site

Then act on one finding of **your own**, and record the decision.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| The version check fails | You changed one workflow file |
| The archived page left Projects | `draft: true`: archiving is a status |
| `git revert` reports a conflict | Resolve the file, then complete it |
| `git reset --hard` on published work | Recover from a copy, then revert |
| A token appears in a commit | Revoke it at the service **now** |

---

## Completion check

- I ran the pass and found a page that had been quietly wrong
- Both workflows pin one Hugo version, and a check enforces it
- I archived a page without changing its address
- I tested an alias and removed the one I did not need
- I published a mistake, saw a 404, and undid it with `git revert`
- I have a third copy, and know what cloning does not restore
- I can state my licensing position and what my site collects
- `MAINTENANCE.md` records the routine and its decisions

---

# Next: Build Your Own Publishing Project

Chapter 19: your own project, planned, built, checked, published, and maintained.

**polla.dev/ssg-book**
