---
title: "Chapter 18 — Maintain, Migrate, and Recover"
weight: 18
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*The added version check was verified against a fixture. No Hugo build, GitHub Actions run, deployment, revert against a live site, or beginner trial yet.*

Your notebook works. It is published, checked on every proposal, searchable, bilingual in part, and able to receive a message. Nothing about it is finished, because a website that nobody maintains does not stay still; it goes quietly out of date while appearing to work perfectly.

In this chapter you will make a maintenance pass over the site you actually have. You will find a page that now says something untrue, update what you depend on, archive work that has been superseded, and publish a mistake on purpose so that you can practise recovering from it after it has gone live. Then you will settle the questions that outlast any single change: credentials, licensing, privacy, cost, and who owns what.

The visible result is a tidier, more honest site and a written routine you can repeat. The most valuable part is the recovery: knowing what to do about a bad change you have already published is a different skill from avoiding one.

## What you will be able to do

By the end, you should be able to:

- Run a repeatable maintenance pass and act on what it finds.
- Update a pinned dependency in every place it is pinned.
- Retire a page without breaking an address you have published.
- Undo a change that is already live, without rewriting published history.

Start from the completed Chapter 17 checkpoint with a clean working tree on `main`, pushed and deployed. Work on a branch and propose changes through a pull request, except where Section 18.4 deliberately does otherwise.

Nothing new is installed. This chapter is about the site, the repository, and the arrangements around them.

## 18.1 Run a maintenance pass on the site you actually have

A maintenance pass is a list of questions, asked on a schedule, about things that decay silently. Here is the list for this project. Work through it now against your own site, writing down what you find before changing anything.

| Question | Where to look |
| --- | --- |
| Does any page claim something that is no longer true? | Every page body, especially statements about progress |
| Are the translations still level with their sources? | `grep -r 'source_checked' content/` and the English pages they translate |
| Does every published address still resolve? | The live site, and any address you have shared |
| Is the pinned Hugo version the same everywhere? | Both workflow files, and your local `hugo version` |
| Does `AGENTS.md` still describe the real project? | Its file map against the actual folders |
| Is anything left over from an earlier exercise? | The project folder's siblings, and any temporary file |

Two findings are worth expecting, because this book created them.

The first is a stale claim. Open `content/projects/reading-list/index.md`. It was written in Chapter 9 and still says the reading work has not begun, that the resources have not been selected or reviewed, and that the next step is to choose three of them. Since then, Chapter 12 built a resource directory with a field agreement, and Chapters 13 and 16 added to it. The work that page proposes has effectively been done elsewhere, and the page has not noticed. Nothing was broken, no check failed, and the page has been quietly wrong for nine chapters.

The second is housekeeping. Chapters 1 to 5 asked you to copy the project to sibling folders named `my-knowledge-site-ch01-backup` and so on. Those are probably still there: stale copies of a site that has moved on, and easy to confuse with the live project. Decide deliberately whether to keep one and remove the rest, or move them somewhere clearly marked as historical.

Write down what your own pass found. The rest of this chapter acts on the first finding and leaves the others to you.

## 18.2 Update what you depend on

Your project pins Hugo's version, and it pins it in two places:

```text
.github/workflows/hugo.yaml
.github/workflows/checks.yaml
```

Both contain `HUGO_VERSION: "0.150.0"`. That duplication is a small trap. If you update one and forget the other, your checks will examine a proposal with one version of Hugo while your deployment builds it with another. Both jobs will pass, and the thing you tested is not the thing you published.

Add a step to `.github/workflows/checks.yaml` that refuses to let them drift, after the existing checks:

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

This is the same crude, readable kind of check as the others, and it has the same honest limit: it confirms the two files agree, not that the version they agree on is a good one.

There is a third place the version matters, and no check can reach it: the Hugo on your own computer. Run `hugo version` and compare. A local version ahead of the pinned one can build something your deployment cannot, and a local version behind it can hide a problem until CI finds it.

To update Hugo deliberately, do it as a proposal rather than in place:

1. Read the release notes for the versions between yours and the new one.
2. Install the new version locally and run `hugo --minify --panicOnWarning`.
3. Check the pages this book has built: Projects, Resources, Search, Contact, and both languages.
4. Change `HUGO_VERSION` in **both** workflow files on a branch.
5. Open a pull request and let the checks build the whole site with the new version.
6. Merge only when both you and the checks are satisfied.

That is what the arrangement from Chapter 14 is for. A dependency update is exactly the kind of change that looks harmless and occasionally is not.

The action versions in both workflows — `actions/checkout@v7`, `actions/configure-pages@v6`, and the rest — are pinned the same way and need the same treatment. Update them one at a time rather than together, so that a failure tells you which one caused it.

## 18.3 Retire a page without breaking its address

The reading-list project is not wrong because it failed. It is wrong because it has been superseded: the resource directory now does its job, with a field agreement. Deleting the page would be the easy answer and the worst one, because its address has been published and its history is real.

Archive it instead. Chapter 9 agreed that a project's `status` is one of `planned`, `in-progress`, or `complete`, and noted that those values were our editorial choice rather than anything Hugo enforces. We now need a fourth, so add it deliberately: `archived`. Open `content/projects/reading-list/index.md` and change the status, keeping everything else:

```yaml
params:
  status: "archived"
```

Then say so on the page itself, at the top of the body, above the existing `## Purpose` heading:

```markdown
**Archived.** The resource directory on the [Resources page](../../resources/) now does this job, with a shared set of fields for every entry. This page is kept for its history.
```

Leave `draft: false`. The page stays published, its address keeps working, and the status label the Chapter 11 partial already displays now tells the truth. The generated Projects list will show it as archived without any template change.

That is the outcome to aim for: a retirement that costs no addresses. It was available because of the naming decisions in Chapter 3, not by luck.

### When an address has to change

Sometimes it cannot be avoided. Hugo's tool for that is the `aliases` front-matter field, which generates a small page at the old address that sends visitors to the new one.

Our site has no address that must change, so verify the mechanism rather than invent a migration. Temporarily add this to the front matter of `content/resources/index.md`:

```yaml
aliases:
  - /projects/reading-notes/
```

Build with `hugo --minify --panicOnWarning` and look for a generated file at `public/projects/reading-notes/index.html`. Open it: a tiny HTML page whose only job is to redirect, and generated output rather than something you maintain. Start the preview and visit that address to watch it happen.

Then remove the alias again, because we do not want a redirect from an address that never existed. You now know the tool, and you know how to check that it worked. [Hugo: aliases](https://gohugo.io/content-management/urls/#aliases)

Keep a real alias whenever you genuinely move or rename something. An address you published belongs to everyone who saved it.

### Publish the archive on its own

Propose this change by itself, following Chapter 14. Keeping it separate matters for the next section, which needs something small and isolated to undo:

```text
hugo --minify --panicOnWarning
git switch -c archive-reading-list
git add content/projects/reading-list/index.md
git diff --cached
git commit -m "Archive the superseded reading-list project"
git push -u origin archive-reading-list
```

Open the pull request, let the checks run, read the diff, and merge. Confirm on the live site that Projects lists three entries with one marked archived, and that `/projects/reading-list/` still resolves. Then bring your local copy up to date:

```text
git switch main
git pull
```

## 18.4 Recover from a change you have already published

Everything so far has caught mistakes before publication. This section is about the other case, and to practise it we will publish a mistake on purpose.

The mistake is a realistic one. Archiving a page feels like it should mean unpublishing it, so a reasonable person changes one more line. Make it as a change of its own, so that undoing it later undoes nothing else:

```text
git switch -c unpublish-archived-project
```

In `content/projects/reading-list/index.md`, change only:

```yaml
draft: true
```

Then commit, push, and propose it as usual:

```text
git add content/projects/reading-list/index.md
git commit -m "Set the archived project to draft"
git push -u origin unpublish-archived-project
```

Open the pull request and read the checks. **They pass.** None of the five rules examines a draft flag, the site builds cleanly, and nothing anywhere reports a problem. Merge it and let the deployment run.

Now look at the consequences on the live site, in this order:

1. Visit Projects. The list has two entries instead of three. Nothing is broken; the page simply no longer mentions the project.
2. Visit `/projects/reading-list/` directly. It returns a 404. That address was published, and now it is gone.
3. Look for a broken link anywhere on your site. There is none, because Chapter 10 replaced the hand-written project list with a generated one, so the drafted page removed itself from the only place that linked to it.

That combination is what makes this failure worth practising. From inside the site everything looks consistent, and the only people who can see the damage are the ones who had the old address. Chapter 9 warned that a draft setting is not a reliable way to withdraw a published page; this is the same lesson from the other direction.

### Undo it with a new commit, not by rewriting history

Find the commit you want to undo:

```text
git switch main
git pull
git log --oneline -5
```

You may be tempted by `git reset` and a forced push. Do not use them here. That change is already on GitHub, already deployed, and possibly already pulled elsewhere. Rewriting published history does not remove what happened; it removes the record of it, and breaks every copy holding the old history.

Use `git revert` instead. Which form you need depends on how you merged, and the log tells you which you are looking at:

```text
git revert <commit>
git revert -m 1 <merge-commit>
```

If you merged with GitHub's default button, the newest commit on `main` is a **merge commit**, recognisable in the log by a subject like `Merge pull request #4`. A merge commit joins two histories, so Git cannot know which one you meant to undo, and plain `git revert` refuses. `-m 1` tells it to undo what the branch brought in. If you used Squash and merge, the change arrived as one ordinary commit and the plain form is correct.

GitHub also offers a Revert button on a merged pull request, which opens the undo as a new proposal so it passes through the same checks. That is often the better route; use the command line here so you have done it once without the button.

Either way, Git creates a **new** commit applying the opposite change. Your editor may open for its message; the default is fine. Then check what it did and publish the fix:

```text
git show --stat HEAD
hugo --minify --panicOnWarning
git push
```

The push starts the publishing workflow. When it finishes, check the same three things: the Projects list has three entries again, `/projects/reading-list/` resolves, and the archived status label is still correct.

Your history now contains both the mistake and its correction, which is the honest record.

| Command | What it does | When it is right here |
| --- | --- | --- |
| `git restore` | Discards an uncommitted change | Before you commit, as in Chapter 6 |
| `git revert` | Adds a commit undoing an earlier one | After the change is published |
| `git reset --hard` | Moves the branch, discarding commits | Only on work you have never shared |

> **Checkpoint:** you published a change, saw its effect on real addresses, and undid it without rewriting anything anyone else may have.

## 18.5 Know where your backups actually are

You have your working copy and a copy on GitHub. It is easy to treat the second as a backup, and it is not one.

A **remote** is a copy that exists so you can collaborate and publish. A **backup** is a copy that survives the failure you are worried about. If the failure you are worried about is losing your laptop, GitHub covers it. If it is losing access to your GitHub account — a suspension, a lost recovery method, a change of terms, an organisation you leave — then GitHub is the thing that failed, and it cannot also be the recovery.

Keep three copies, in two places you control differently:

| Copy | Protects against |
| --- | --- |
| Your working folder | Nothing on its own |
| GitHub | Losing the computer |
| A clone on external storage or another service | Losing the account |

Making the third is one command, run wherever you keep it:

```text
git clone --mirror https://github.com/YOUR-USERNAME/my-knowledge-site.git
```

A mirror clone copies the repository's full history rather than a working tree. Chapter 6 made the same point about ordinary copies: a backup that omits the `.git` directory keeps your files and throws away everything that made them recoverable.

Then check what is not in the repository at all, because those things need their own answer:

- Your GitHub account and its recovery methods.
- The Pages configuration and the ruleset from Chapter 14.
- A custom domain, if you ever add one, and its registration.
- Your agent account from Chapter 8.

None of that is restored by cloning your files. Write down where each one lives and how you would regain it. A restore you have never thought through is a plan, not a backup.

## 18.6 Credentials, licensing, privacy, and cost

These are the questions that have no build step, which is why they get skipped.

**Credentials.** Chapter 7 authenticated you to GitHub, Chapter 8 to an agent service, and Chapter 17 published an email address on purpose. Section 17.7 established the rule: a secret committed to Git stays in the history. If you ever commit a token, revoke it at the service immediately rather than removing it in a later commit. Review what each token can do; one that can only read is a smaller problem than one that can publish.

**Licensing.** Your repository is public and your content carries no licence, which by default means nobody may reuse it. That may be what you want. If not, add a `LICENSE` file, or say on the About page what people may do; many notebooks use a Creative Commons licence for writing and a separate one for code. Two cautions: you can only license what you hold, so do not place a licence over quoted material or a borrowed image, and the Chapter 13 article being agent-drafted from your notes changes neither your responsibility for it nor your ability to license it.

**Privacy.** Your site collects nothing: no analytics script, no cookie, no form service, and Chapter 17's form transmits nothing. That is worth keeping, because it means you owe visitors no consent banner and hold no data you could lose. What you should not claim is that nobody observes them: GitHub serves your pages and keeps its own request logs, which is its collection rather than yours. Add anything that loads from another domain and you have changed the answer, so the page describing it must change too.

**Cost.** Today: nothing. A public repository, Pages hosting, and Actions minutes within the free allowance. That changes if the repository becomes private, if the workflows grow, if you add a domain, or if agent usage exceeds your plan. Check the current figures rather than trusting this paragraph.

**Ownership.** The repository is yours; a domain is rented; the platform can change its terms. The part that is genuinely yours is the content, and it is yours because it is Markdown, CSS, and templates in a folder you can copy. Moving this site to another host means pointing a different build at the same files. That portability is the practical case this book has been making, and the maintenance pass in Section 18.1 is what keeps it real.

## 18.7 Record the routine, and what you are deliberately not doing

A routine you keep in your head is not a routine. Create `MAINTENANCE.md` at the project root:

```markdown
# Maintenance routine

## Every few months
- Read each page body for claims that are no longer true.
- Compare each translation's source_checked date with its English source.
- Check that every published address still resolves.
- Review open questions in MAINTENANCE.md and AGENTS.md.

## When a dependency changes
- Read the release notes.
- Update HUGO_VERSION in both workflow files on a branch.
- Build locally, then let the checks build the proposal.
- Update action versions one at a time.

## After any mistake reaches the live site
- Use git revert, not git reset, on published history.
- Verify the live result, not only the build.

## Decisions to keep
- The contact form sends nothing to any server.
- Project status values are planned, in-progress, complete, or archived.
- Addresses that have been published get an alias if they must move.
```

Add one entry to `AGENTS.md` under Files, and one working agreement:

```markdown
- The maintenance routine is in MAINTENANCE.md.
```

```markdown
- Archiving a page means changing its status and saying so in the body. It does not mean setting draft: true, which withdraws a published address.
```

That second agreement is the Section 18.4 mistake, written down so that neither you nor an agent makes it again. This is what the instruction file is for: a decision you had to learn becomes a rule you no longer have to remember.

Two extensions belong here as directions rather than exercises. **Content reuse** is the observation that your resource directory is structured data with an agreement, so it could feed something else — a printed list, another site, a course page — by reading the same JSON rather than copying it. **Retrieval** is the idea of pointing an agent at your own accumulated content to answer questions from it. Both are reasonable next steps and both are outside this book's scope, for the same reason: they need a clear account of what is authoritative and what happens when the source changes, and that is a larger subject than an exercise.

## 18.8 Complete the pass, propose it, and save

Two things are already on `main`: the archive from Section 18.3 and the revert from Section 18.4. What remains uncommitted is the version check, the routine, and the guidance updates.

```text
hugo --minify --panicOnWarning
git switch -c maintenance-pass
git status
git add .github/workflows/checks.yaml MAINTENANCE.md AGENTS.md
git diff --cached
git commit -m "Add a version check and record the maintenance routine"
git push -u origin maintenance-pass
```

Read the diff, then check the working tree for two things that should not be in it: the alias you added to `content/resources/index.md` in Section 18.3, and any leftover edit to the archived page. `git status` should report nothing beyond the three files above. Confirm also that `MAINTENANCE.md` says what you will actually do rather than what sounds thorough.

The checks should pass, including the new version comparison. Merge, then verify the live site once more: Projects shows three entries with one archived, `/projects/reading-list/` resolves after the revert, and both languages still work.

Finally, act on one finding from your own Section 18.1 pass that this chapter did not cover. The old backup folders are the likeliest candidate, and the most useful thing you can do with them is decide, rather than leave them to accumulate. Record what you decided in `MAINTENANCE.md`, because the value of that file is that next time you will not have to work it out again.

## Completion check

- [ ] I ran the maintenance pass and wrote down what it found.
- [ ] I found a page that had been quietly wrong and can say why no check caught it.
- [ ] Both workflows pin the same Hugo version, and a check now enforces that.
- [ ] I know the third place the Hugo version matters and why no check can reach it.
- [ ] I archived a superseded page without changing its address.
- [ ] I verified how an alias behaves and removed the one I did not need.
- [ ] I published a mistake, saw a live address return 404, and can explain why nothing detected it.
- [ ] I undid it with `git revert` and can say why `git reset` was wrong there.
- [ ] I have a third copy of the repository, and I know what cloning does not restore.
- [ ] I can state my site's licensing position and what it collects about visitors.
- [ ] `MAINTENANCE.md` records the routine and the decisions worth keeping.

This is enough maintenance for a site of this size. Scheduled dependency robots, automated link crawling, uptime monitoring, staged environments, content audits at scale, and retrieval over your own archive are outside this chapter's scope. Add each one when the work it saves exceeds the work it becomes.

Chapter 19 hands the whole method to you: a project of your own, planned, built, checked, published, and maintained with the arrangements you have just finished putting in place.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| The version check fails after an update. | You changed one workflow file. Both must pin the same value. |
| The version check passes but the deployment differs from your test. | Compare your local `hugo version` with the pinned value; no check can see your computer. |
| The archived page vanished from Projects. | You set `draft: true`. Archiving is a status change; restore `draft: false`. |
| The archived page still shows no status. | The label comes from the Chapter 11 partial and the `status` value under `params`; check the indentation. |
| The alias produced no file. | Build after adding it, and look under `public/` at the alias path, not in your source folder. |
| The alias page is still served after removal. | Old generated output can persist. Rebuild, and remember that a live deployment needs a new push. |
| `git revert` reports a conflict. | Later commits touched the same lines. Resolve the file, then complete the revert; the change is not lost. |
| You already ran `git reset --hard` on published work. | Recover from the remote or your mirror clone. Then push forward with a revert rather than forcing. |
| The live site still shows the mistake after reverting. | The revert is a commit like any other. Check that you pushed and that the publishing run succeeded. |
| `git clone --mirror` produces no working files. | That is correct. A mirror holds the history; clone it normally to get a working tree back. |
| A token appeared in a commit. | Revoke it at the service now. Removing it in a later commit does not remove it from history. |

A maintenance pass finds what you thought to ask about. Keep `MAINTENANCE.md` as a list of questions rather than a list of answers, and add a question each time something surprises you.

---

## Editorial note for the author — remove before publication

The findings are real rather than invented. The reading-list page genuinely became untrue over Chapters 9 to 16: it claims the reading work has not begun while Chapter 12's resource directory does that job. Verify on replay that the wording still reads as stale; if earlier chapters are revised, re-derive this finding rather than assuming it. The leftover Chapter 1 to 5 backup folders are the second real finding and should stay, because readers will have them.

Section 18.4 is the designed failure and the most carefully constructed thing here. Setting `draft: true` while archiving is the mistake a reasonable person makes, it passes all five CI checks, and its damage is invisible from inside the site: Chapter 10 replaced the hand-written project list with a generated one, so the drafted page removes itself from the only place that linked to it. A published address 404s and nothing on the site reveals it. This is also the chapter that finally needs `git revert`, cashing Chapter 6's deferral of history editing. Publishing a mistake on purpose is deliberate: describing the recovery without performing it would leave readers attempting `git revert` for the first time under real pressure.

Section 18.3 declines to fake a migration. No address must change, so the alias is verified as a mechanism and then removed, with the honest framing that Chapter 3's naming is why no redirect is needed. Do not replace this with an invented rename.

At about 3,830 words of reader-facing prose this is the longest chapter, against a previous maximum of 3,690 — a measured overrun, since this plan row lists eleven topics where most list three or four. Split Section 18.6 if the trial shows it running long: credentials, licensing, privacy, cost, and ownership are a coherent chapter of their own.

The version-match step was executed against a fixture, and working through the sequence corrected two drafting faults. Nothing else is validated. See the validation record.
