---
title: "Track and Recover Your Hugo Site with Git"
weight: 6
book_number: 6
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

In the previous chapters, you kept copies of the project before continuing. Those copies helped you recover, but comparing them becomes awkward. Which one contains the footer improvement? What changed in the stylesheet? Can you recover a file without replacing the whole site?

Git gives your project a history of recorded checkpoints. In this chapter, you will record your working Hugo site, save one useful content change, and recover from a deliberately poor styling change.

We will learn a small local workflow. You do not need a GitHub account yet. Branching strategies, merge conflicts, and advanced history editing can wait until there is a practical reason to use them.

## What you will be able to do

By the end, you should be able to:

- Record the site's source files in a local Git repository while excluding generated output.
- Inspect changes, select them for a commit, and record a meaningful checkpoint.
- Distinguish removing a change from the next commit from discarding a file edit.
- Find recent checkpoints and restore a deliberately changed file.

Start with the working Chapter 5 project and keep its existing backup (or switch to companion branch `chapter-05` in `ssg-playground`). Save all open files. Stop the Hugo preview for the initial setup so that the terminal is available for the commands below.

## 6.1 Prepare Git in the right folder

Open a terminal in the project folder that contains `hugo.toml`, `content`, `layouts`, and `static`. In an editor with an integrated terminal, opening the project folder first usually makes this straightforward. Check the terminal's location; opening a file in the editor does not necessarily change it. (If you are following along in the `ssg-playground` companion repository, it is already a Git repository—you can simply switch between chapter branches without re-running `git init`).

Run:

```text
git --version
```

If Git is available, you will see a version number. If the command is not recognised, use the [official Git installation page](https://git-scm.com/install/) and follow the instructions for your operating system. Reopen the terminal afterwards and repeat the check. Installing Git and creating a GitHub account are separate tasks.

The examples in this draft were tested with Git 2.51.1. Use a recent supported installation rather than trying to match that exact version. Commands below are entered one line at a time and work in a normal PowerShell, macOS, or Linux terminal with Git installed.

Before creating a repository, run:

```text
git rev-parse --show-toplevel
```

For the plain project created in this book, an error containing `not a git repository` is expected at this point. It means no enclosing repository was found.

If a path appears instead, Git already manages this folder or a parent folder. Do not create a nested repository blindly. If the path is this project, use its existing history and skip `git init`. If it is an unrelated parent, put the standalone Hugo project outside that repository before following this beginner setup.

### Create the local repository

For our project without an existing repository, run:

```text
git init -b main
```

This creates the repository's metadata and names the initial branch `main`. A branch names a line of development; we will use just this one for now. Git stores its local history in the project's `.git` directory. Leave that directory under Git's management. [Git: init](https://git-scm.com/docs/git-init)

No checkpoint has been recorded yet, and nothing has been uploaded.

### Choose the author identity for your commits

Replace both placeholders before running:

```text
git config user.name "Your Chosen Author Name"
git config user.email "you@example.com"
```

These settings apply to this repository because we have not used `--global`. They identify the author of future commits; they do not sign you into a service. Check them with:

```text
git config user.name
git config user.email
```

The chosen name and email become part of commit history, which may later be shared. Use an identity you intend to share. If you already use GitHub and prefer its private commit address, copy the exact `noreply` address from your account settings. Do not invent one. Changing your setting later does not rewrite old commits. [Git: first-time setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup), [GitHub: commit email addresses](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)

## 6.2 Save the working site as your first checkpoint

### Tell Git which generated files to leave out

Create a plain-text file named `.gitignore` beside `hugo.toml`. Include the initial dot and ensure your editor does not add `.txt` to its name. If the file already exists, retain its contents and add any missing rules below.

```gitignore
# Hugo output and generated files
/public/
/resources/
/.hugo_build.lock
/hugo_stats.json

# Local operating-system metadata
.DS_Store
Thumbs.db
```

For our starter, these Hugo outputs can be recreated. We want the source content, layouts, CSS, configuration, and article image in history. The `/resources/` entry refers to the generated directory at the repository root; it does not exclude our `content/resources/` page.

Ignore rules normally keep matching untracked files out of staging. They do not erase files or stop tracking something already committed. This list is tailored to the book's project, not every possible Hugo build arrangement. [Git: gitignore](https://git-scm.com/docs/gitignore)

### Select and inspect the initial files

Run:

```text
git status
```

Before the first commit, the source files appear as **untracked**: present on disk but not yet recorded by Git. Generated directories covered by `.gitignore` should not appear in the ordinary list.

Select the book's source files:

```text
git add .gitignore hugo.toml content layouts static
```

This prepares their current contents in Git's **staging area**, also called the index. Staging chooses what the next commit will contain. It is separate from saving a file in your editor. [Git: add](https://git-scm.com/docs/git-add)

Review that selection:

```text
git status
git diff --cached --stat
git diff --cached
```

The status should now describe changes to be committed. The short summary lists files and change counts; the full diff shows text being added. An image normally appears as a binary change rather than readable lines. If Git opens a scrolling viewer, use Space to move forward and `q` to return to the prompt.

Check that the expected source files are present, including `content/resources/index.md`, and that generated `public/` files and backup folders are absent. Review the content too: an API key or private note should not enter history just because it sits inside an otherwise useful directory.

If the selection contains something unexpected, correct it before committing. The remainder of this chapter assumes the ordinary book project shown above.

### Record the checkpoint

Run:

```text
git commit -m "Save Hugo site after Chapter 5"
git status
```

A **commit** records the staged project state with an identifier, author information, and a message. The `-m` option supplies that message directly. The command should report a new commit, and status should report a clean working tree when no other changes remain. [Git: commit](https://git-scm.com/docs/git-commit)

A clean working tree describes Git's tracked state; it does not certify that the website is correct. Ignored files can still exist, and the browser checks from Chapter 5 still matter.

> **First checkpoint:** your working Hugo source now has a recorded local version. You have not published the site.

## 6.3 Understand the three places an edit can be

Before the next exercise, distinguish these:

| Place | Meaning | Useful question |
| --- | --- | --- |
| Working tree | The project files you edit on disk | What have I changed? |
| Staging area | The prepared contents for the next commit | What am I about to record? |
| Commit history | Previously recorded project states | What did I save earlier? |

Saving in the editor updates the working file. `git add` stages its current contents. `git commit` records the staged state.

If you stage a file and then edit it again, the additional edit is not automatically included. Stage it again if it belongs in the same commit, then review the staged diff. This is why a file can appear in both the staged and unstaged sections of `git status`.

For this chapter, make one small change at a time. That makes the distinction easier to see and the resulting history easier to read.

## 6.4 Record a useful content change

Open `content/articles/first-learning-note/index.md`. Add this section at the end, with a blank line before the heading:

```markdown
## My publishing checklist

- Read the page in the local preview.
- Check its links and image description.
- Review the changed files before recording a checkpoint.
```

Save. Start `hugo server` in another terminal if convenient, or run it in the same terminal and stop it after inspecting the article. Check that the section appears correctly. A Git diff will help review the writing, but the preview reveals how it renders.

Back at an available terminal in the project root, run:

```text
git status
git diff -- content/articles/first-learning-note/index.md
```

The file should be modified but not staged. The diff should show the new section with `+` prefixes. Removed text uses `-`; unchanged context helps locate the edit. The prefixes are part of the comparison display, not extra Markdown to copy.

Without `--cached`, this diff compares the working file with its staged version. With `--cached`, it compares the staged version with the last commit. The `--` separates options from the file path. [Git: diff](https://git-scm.com/docs/git-diff)

Stage and review:

```text
git add content/articles/first-learning-note/index.md
git diff --cached -- content/articles/first-learning-note/index.md
```

Now run the unstaged comparison again:

```text
git diff -- content/articles/first-learning-note/index.md
```

It should print nothing if you made no further edits after staging. Your change has not vanished: it is in the staged comparison.

### Practise taking a file out of the next commit

Before committing, run:

```text
git restore --staged -- content/articles/first-learning-note/index.md
git status
```

Open the Markdown file. Your publishing checklist should still be there. The command removed the change from the staging area while preserving the working file. Status should show it as an unstaged modification.

Stage it again and record it:

```text
git add content/articles/first-learning-note/index.md
git diff --cached -- content/articles/first-learning-note/index.md
git commit -m "Add a publishing checklist to the first learning note"
git status
```

Use messages that explain the purpose of a change. “Add a publishing checklist” is more useful when browsing history than “update” or “stuff”. A single commit should represent a change you can describe coherently.

> **Second checkpoint:** you reviewed a content change, staged it, unstaged it without losing it, and then committed it deliberately.

## 6.5 Recover from a deliberately poor CSS edit

First run `git status`. Begin this exercise only when your working tree is clean. This keeps unrelated work out of the recovery example.

Open `static/css/site.css`. In the `body` rule, temporarily replace:

```css
font-size: 1.125rem;
```

with:

```css
font-size: 6rem;
```

Save and inspect the article in Hugo's preview. Much of the inherited text should become impractically large. The page may still build successfully; the problem is the styling decision.

**Do not stage or commit this deliberate mistake.** Inspect it:

```text
git diff -- static/css/site.css
```

Confirm that the only edit to this file is the font-size experiment. Then discard that working-file edit:

```text
git restore -- static/css/site.css
```

This command overwrites that file's unstaged changes with its staged version. Because we began clean and never staged the experiment, that version is also the last committed one. It discards *all* unstaged changes in the named file, not just the font-size line. [Git: restore](https://git-scm.com/docs/git-restore)

Check the file, reload the preview if needed, and run:

```text
git status
```

The text size should be restored and the working tree clean. The committed publishing checklist remains in the article.

### Two similar commands with different effects

| Command used in this chapter | What happens |
| --- | --- |
| `git restore --staged -- path/to/file` | Removes staged changes relative to the last commit; keeps the working file |
| `git restore -- path/to/file` | Replaces the working file with its staged version; discards its unstaged edits |

These examples concern a file already in the first commit. If you accidentally staged the CSS mistake, plain `git restore` will not undo that staged version. In this exercise, unstage the stylesheet first using the first form, review its remaining diff, and then use the second form to discard the experiment.

For a file containing both useful work and a mistake, correct the unwanted line in your editor instead of restoring the whole file. The path-specific recovery above is appropriate because we deliberately isolated one unwanted edit.

## 6.6 Read the history you have created

Run:

```text
git log --oneline -5
```

For a new repository following this chapter, you should see two commits, newest first: the publishing checklist and the Chapter 5 baseline. Each begins with an abbreviated identifier. Your identifiers will differ from anyone else's. [Git: log](https://git-scm.com/docs/git-log)

You can inspect the latest committed change to the article with:

```text
git diff HEAD~1 HEAD -- content/articles/first-learning-note/index.md
```

Here, `HEAD` identifies the current commit and `HEAD~1` its first parent, the preceding checkpoint in our simple history. This comparison should show the checklist addition. It requires the two commits we have just made.

Your record starts when you begin committing. Git has not reconstructed the individual steps from Chapters 1–5; they are represented together by the baseline commit. It also cannot reliably recover arbitrary edits that were never recorded.

Keep ordinary device backups. Local Git history lives on the same computer as the files and does not protect against losing that computer. If you copy the repository as a backup, include its `.git` directory so the history travels with it. Chapter 7 will add a remote copy on GitHub and the first publishing workflow.

## 6.7 Make your own small commit

Improve one sentence in `content/about/index.md`. Preserve its front matter and links. Then complete this cycle without copying a whole project folder:

1. Save and inspect the About page in the local preview.
2. Use `git status` and a file-specific `git diff` to review your change.
3. Stage the About file and inspect its staged diff.
4. Commit with a message explaining the improvement.
5. Check that status is clean and the new commit appears in the recent log.

If you forget the syntax, use the command card below. Understanding which state you are inspecting matters more than memorising options.

This is also the foundation for later agent work. Start from a known checkpoint, give the agent a bounded task, inspect every changed file, and decide what to record. A commit documents a change; it does not establish that AI-generated text is accurate or that the website behaves correctly.

## Completion check

- [ ] Git manages the Hugo project folder I intended.
- [ ] The initial commit contains the site's source and required image, with generated output excluded.
- [ ] I can distinguish saving, staging, and committing.
- [ ] I reviewed and committed the article's publishing checklist.
- [ ] I unstaged a change without deleting the working edit.
- [ ] I discarded the isolated CSS experiment and checked the restored result.
- [ ] I made an independent About-page commit and can find it in the log.
- [ ] My working tree is clean, and I understand that the site is still local.

Your latest commit is the Chapter 6 checkpoint. Keep the earlier backup, but you no longer need a new sibling folder for every small revision.

This is enough Git for our next steps. Branching, merge conflicts, remote collaboration, and history editing are outside this chapter's scope. Learn each one when a concrete need appears rather than in advance.

Chapter 7 gives the project a public address. You will send this history to GitHub and let a supplied workflow build and publish the site from it.

## Troubleshooting when you need it

| Symptom | What to check |
| --- | --- |
| `git` is not recognised. | Install Git for your operating system and reopen the terminal. |
| `not a git repository` appears after setup. | Check the terminal's folder. Run commands in the project where you initialised Git. |
| Git asks who you are when committing. | Set the repository's author name and email, then retry the commit. |
| A path does not match any files. | Check the project root and exact spelling. Use quotes around a path containing spaces. |
| `git diff` is empty, but you know you changed something. | Check status and `git diff --cached`; the edit may be staged. An untracked file also does not appear in an ordinary unstaged diff. |
| A file has both staged and unstaged changes. | You edited it again after staging. Review both comparisons before deciding what to include. |
| A generated file is still tracked despite `.gitignore`. | Ignore rules do not remove existing tracked files. Diagnose how it entered the repository before committing more output. |
| Git warns about LF and CRLF line endings. | These are different newline conventions. Check whether the command completed and inspect the diff; do not rewrite every file merely to silence a warning. |
| `nothing to commit` appears. | Check status: the edit may already be committed, unsaved in the editor, ignored, or not staged. |
| A restore command did not undo the mistake. | Check whether the mistake is staged. Apply the two-state explanation in Section 6.5. |

Branching, collaboration, and undoing changes already shared with others require additional decisions. We will introduce them where needed. For now, the useful habit is to preview, review, stage, and commit a small understandable change.

## Command card: the local workflow

Run commands from the repository root. Replace example paths where necessary.

| Purpose | Command |
| --- | --- |
| See what is staged, unstaged, or untracked | `git status` |
| Review an unstaged file edit | `git diff -- path/to/file` |
| Stage the current contents of a file | `git add path/to/file` |
| Review everything selected for the next commit | `git diff --cached` |
| Record the staged changes | `git commit -m "Describe the change"` |
| Review recent checkpoints | `git log --oneline -5` |
| Unstage a tracked file while keeping its edit | `git restore --staged -- path/to/file` |
| Discard a tracked file's unstaged edits | `git restore -- path/to/file` |

