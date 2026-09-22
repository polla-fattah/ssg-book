---
title: "Track and Recover Your Hugo Site with Git"
description: "Chapter 6: record changes, compare versions, and recover work without copying whole folders."
book_number: "6"
weight: 7
---

# Track and Recover Your Hugo Site with Git

Static Site Generators in the Age of AI

**Chapter 6**

Polla Fattah

---

## Today's goal

Backup folders helped, but they are awkward to compare.

- Which copy has the footer improvement?
- What changed in the stylesheet?
- Can I recover **one file** without replacing the whole site?

**Git** gives the project a history of recorded checkpoints. Today it stays **local**: no GitHub account yet.

---

## By the end of today you can

- **Record** the site's source in a local Git repository, leaving generated output out
- **Inspect** changes, select them, and commit a meaningful checkpoint
- **Distinguish** unstaging a change from discarding an edit
- **Find** recent checkpoints and restore a changed file

Save all files and **stop** the Hugo preview before you start.

---

## Check Git, in the right folder

Open a terminal in the folder with `hugo.toml` (or checkout companion branch `chapter-05` in `ssg-playground`), then:

```text
git --version
git rev-parse --show-toplevel
```

- No version? Install Git from **git-scm.com**, then reopen the terminal
- `not a git repository` is **expected** here: nothing manages this folder yet (playground users are already inside git)
- A path instead? Git already manages it or a parent. **Do not** nest a new repository blindly

---

## Create the repository

```text
git init -b main
```

- Creates the hidden `.git` folder, where the history lives: leave it alone
- `main` is the name of the branch, one line of development

Then set **who** you are, for this repository only:

```text
git config user.name "Your Chosen Author Name"
git config user.email "you@example.com"
```

---

## Your identity is public

- The name and email become part of the history, which may later be **shared**
- They identify the author; they do **not** sign you in anywhere
- Using GitHub? Copy its exact private `noreply` address from your settings. **Never invent one.**
- Changing it later does not rewrite old commits

Check with `git config user.name` and `git config user.email`.

---

## Leave generated files out

Create `.gitignore` beside `hugo.toml`, with no `.txt` ending:

```gitignore
/public/
/resources/
/.hugo_build.lock
/hugo_stats.json
.DS_Store
Thumbs.db
```

`/resources/` means the root folder only, **not** your `content/resources/` page.

---

## Select the source files

```text
git status
git add .gitignore hugo.toml content layouts static
```

- Before the first commit, files are **untracked**: on disk, not yet recorded
- `git add` puts their current contents in the **staging area**
- Staging chooses what the next commit contains. It is **not** saving

---

## Review before you record

```text
git status
git diff --cached --stat
git diff --cached
```

- Are `content/resources/index.md` and the article image there?
- Are `public/` and backup folders **absent**?
- No API key or private note in the list?

A long diff opens a viewer: **Space** moves on, **q** quits.

---

## Record the first checkpoint

```text
git commit -m "Save Hugo site after Chapter 5"
git status
```

A **commit** records the staged state, with an identifier, the author, and a message. Status then reports a **clean working tree**.

> Clean means Git has recorded everything. It does not mean the website is correct.

---

## Three places an edit can be

| Place | Meaning | Ask yourself |
| --- | --- | --- |
| Working tree | The files you edit on disk | What have I changed? |
| Staging area | Prepared for the next commit | What am I about to record? |
| Commit history | Recorded project states | What did I save earlier? |

**Save** updates the file. `git add` stages it. `git commit` records what is staged.

Edit a file **after** staging it, and the new edit is not included until you stage again.

---

## Make a content change

At the end of your first article, after a blank line:

```markdown
## My publishing checklist

- Read the page in the local preview.
- Check its links and image description.
- Review the changed files before recording a checkpoint.
```

Check it in `hugo server`: a diff shows the **text**, the preview shows how it **renders**.

---

## Read the diff

```text
git status
git diff -- content/articles/first-learning-note/index.md
```

`+` marks added lines and `-` removed ones. They belong to the display, not your Markdown.

| Command | Compares |
| --- | --- |
| `git diff` | Working file with the staged version |
| `git diff --cached` | Staged version with the last commit |

---

## Stage, and watch it move

```text
git add content/articles/first-learning-note/index.md
git diff --cached -- content/articles/first-learning-note/index.md
git diff -- content/articles/first-learning-note/index.md
```

The last command now prints **nothing**.

The change has not vanished: it moved to the **staged** comparison.

---

## Take it out of the next commit

```text
git restore --staged -- content/articles/first-learning-note/index.md
git status
```

Open the article: your checklist is **still there**. Only the staging was undone.

Stage it again, review, and record it:

```text
git commit -m "Add a publishing checklist to the first learning note"
```

---

## Write useful messages

| Weak message | Useful message |
| --- | --- |
| `update` | `Add a publishing checklist to the first learning note` |
| `stuff` | `Explain the notebook's audience on the About page` |
| `fix` | `Restore the skip link's target` |

One commit, **one change** you can describe in one sentence.

---

## Make a mistake on purpose

Start from a **clean** `git status`. In the `body` rule of `static/css/site.css`:

```css
font-size: 6rem;
```

The site still builds; the text is absurdly large. **Do not stage or commit it.**

```text
git diff -- static/css/site.css
git restore -- static/css/site.css
git status
```

The text returns to normal, and the checklist is still committed.

---

## Two similar commands

| Command | What happens |
| --- | --- |
| `git restore --staged -- file` | Unstages it; **keeps** your edit |
| `git restore -- file` | Replaces the file with its staged version; **discards** unstaged edits |

- The second discards **every** unstaged edit in that file, not just one line
- Staged the mistake by accident? Unstage it first, then restore
- Good work and a mistake in one file? Fix the line in the **editor** instead

---

## Read your history

```text
git log --oneline -5
git diff HEAD~1 HEAD -- content/articles/first-learning-note/index.md
```

- Two commits, newest first: the checklist, then the Chapter 5 baseline
- `HEAD` is the current commit; `HEAD~1` the one before it
- Your identifiers differ from everyone else's

History starts **when you start committing**: Chapters 1 to 5 are one baseline.

---

## Git is not a backup

- Local history lives on the **same computer** as the files
- Keep ordinary device backups
- Copying the project? Include `.git`, so the history travels with it

Chapter 7 adds a remote copy on **GitHub**.

---

## Try it yourself

Improve one sentence in `content/about/index.md`, keeping its front matter and links:

1. Save and check the About page in the preview
2. `git status` and a file-specific `git diff`
3. Stage it and check the staged diff
4. Commit with a message that explains the improvement
5. Status is clean; the commit is in the log

---

## The same habit, with AI agents

1. Start from a known **checkpoint**
2. Give a **bounded** task
3. Inspect **every** changed file
4. Decide what to record

> A commit documents a change; it does not prove the change is right.

---

## Command card

| Purpose | Command |
| --- | --- |
| What is staged or unstaged? | `git status` |
| Review an unstaged edit | `git diff -- path` |
| Stage, then review | `git add path`; `git diff --cached` |
| Record it | `git commit -m "Describe the change"` |
| Recent checkpoints | `git log --oneline -5` |

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| `not a git repository` after setup | The terminal's folder |
| Git asks who you are | Set `user.name` and `user.email` |
| `git diff` is empty after an edit | It may be staged: try `--cached` |
| `nothing to commit` | Unsaved, ignored, unstaged, or already committed |
| LF and CRLF warnings | Newline styles: check the diff |

---

## Completion check

- Git manages the Hugo folder I intended
- The first commit holds the source and image, without generated output
- I can tell saving, staging, and committing apart
- I committed the publishing checklist after reviewing it
- I unstaged a change without losing the edit
- I discarded the CSS experiment and checked the result
- My About-page commit is in the log, and the tree is clean

Your latest commit **is** the Chapter 6 checkpoint: no backup folder needed.

---

# Next: Publish Your Hugo Site with GitHub Pages

Chapter 7: send this history to GitHub and let a workflow build and publish the site.

**polla.dev/ssg-book**
