---
title: "Chapter 13 — Create and Maintain Content with AI Agents"
weight: 13
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*Not yet validated: no Hugo build check, agent session, browser review, or beginner trial has been performed for this chapter.*

In Chapter 8, you gave an agent a small, self-contained job: three bullets in one file. You could read the whole result in a minute. Real content work is larger than that, and its mistakes are harder to see.

In this chapter, you will produce a complete article from source material you supply, then connect it to the rest of the site. The work is divided into three requests: a plan, a draft, and a coordinated update across several files. You will review the claims in the draft against the source before publishing anything.

The visible result is one new article at `/articles/publishing-with-github-pages/`, reachable from the Articles landing page and the home page, with a matching record in the resource directory. The harder result is a working method: supply the material, bound the task, check every claim, and decide publication yourself.

## What you will be able to do

By the end, you should be able to:

- Separate work you can delegate from decisions that must remain yours.
- Supply source material and require an agent to work only from it.
- Break a content contribution into steps that can each be reviewed.
- Check a draft's claims against its source and reject an unsupported sentence.

Start from the completed Chapter 12 checkpoint with a clean Git working tree. You need the Codex CLI installation and account access from Chapter 8, the article and project pages from Chapters 2, 3, and 9, and the JSON directory from Chapter 12. Nothing new is installed in this chapter.

If your account cannot currently reach an agent, you can still complete the exercise by applying the comparison article near the end of the chapter yourself. That practises the Hugo work and the review, but not the delegation.

## 13.1 Decide what an agent may and may not contribute

An agent can arrange, condense, and format material it has been given. It cannot know what happened to you. The notes you are about to supply record events from Chapters 6 and 7; you are the only available authority on whether the finished article describes them correctly.

| Work you can delegate | Decisions that stay with you |
| --- | --- |
| Turning rough notes into ordered prose | Whether an event actually happened |
| Applying an agreed article structure | Whether a claim is supported by the source |
| Writing a one-sentence description | Whether the page is ready for readers |
| Adding a link in an agreed format | Which destinations belong on the site |
| Preparing a record for the directory | Whether a resource deserves inclusion |

The rule behind that table is worth stating plainly: automated checks assess technical requirements, while human review assesses meaning, sources, and suitability for publication. A successful build tells you Hugo could render the page. It says nothing about whether the page is true.

Two habits follow. New pages stay at `draft: true` until you have read them, so publication remains a deliberate decision as it was in Chapter 9. And the source material is committed alongside the article, so the basis for a published claim stays recoverable.

## 13.2 Put the source material where it can be read

At the project root, create a folder named `sources`. Inside it, create `publishing-notes.md` with this content:

```markdown
# Raw notes: publishing the notebook

Not for publication as written. Working notes from Chapters 6 and 7.

Reference consulted: GitHub's documentation on configuring a publishing source,
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

- A Pages site has to be told where its content comes from. We chose the
  GitHub Actions route rather than publishing from a branch.
- The supplied workflow builds with Hugo and deploys the built output.
  We never committed the public/ folder.
- baseURL had to include the repository path. Before that, the live site
  loaded without its stylesheet and the internal links went to the wrong place.
- The first deployment failed. Cause: I pushed before setting the Pages
  source. Fixed by setting it, then running the workflow again.
- The Actions log was where the failure was legible. The browser only
  showed a missing or stale page.
- hugo --minify --panicOnWarning passed locally before that push. Passing
  locally did not mean the deployment had worked.
- Not measured: how long a deployment usually takes.
- Not attempted: a custom domain.
```

Save it as plain text. The `sources` folder sits beside `content`, so Hugo will not turn these notes into a page, just as `AGENTS.md` produced no page in Chapter 8.

Read the notes yourself first. They hold three kinds of material, and the difference matters for the review later:

| In the notes | What it is | How it may be used |
| --- | --- | --- |
| The baseURL problem, the failed first deployment, the Actions log | Events recorded by the author | May become statements about what happened |
| The GitHub documentation reference | An external source | May be credited and paraphrased |
| The two Not lines | Explicit gaps | May be reported as unknown; may not be filled in |

The last row carries this chapter's main risk. Notes usually stop short of what a finished page would like to say, and an agent asked for readable prose has an obvious way to smooth over a gap. A plausible sentence is much harder to notice than a broken link.

Record the source material before it is used:

```text
git add sources/publishing-notes.md
git diff --cached
git commit -m "Add the publishing notes used as source material"
git status
```

## 13.3 Agree what an article must contain, and record it

Chapter 9 gave projects a content model and deliberately left articles alone. The first learning note has only a title and a draft flag. A second article arriving from outside your own typing needs the same kind of agreement.

| Location | Field or heading | Our rule |
| --- | --- | --- |
| Front matter | `title` | A readable article title |
| Front matter | `description` | One sentence explaining what the reader will learn |
| Front matter | `draft` | `true` until you have reviewed the page |
| Body | What this is about | Why the article exists, in two or three sentences |
| Body | What happened | The sequence of events, drawn from the source |
| Body | What I would do differently | A specific change, or an honest statement that it is unclear |
| Body | Sources | Every external reference used, as a link with a short explanation |

Sources is ordinary Markdown in the body, not front matter. Chapter 9 showed that storing a value in front matter does not teach a layout to display it, and Chapter 12 showed the same about data. Attribution no visitor can see is not attribution, and the body makes it visible without a template change.

Prefer a short paraphrase with a credited link over a long quotation: it is easier to keep accurate and avoids reproducing someone else's wording on your site.

An `archetypes/articles.md` starter would suit this model, on the pattern of Chapter 9's project archetype. Add one if you later write articles by hand regularly.

### Record the agreement in the project guidance

Chapter 8's instruction file says nothing about sourcing, because nothing had needed it yet. Add these entries under Files in `AGENTS.md`:

```markdown
- Source material for content work is in sources/.
- Articles are page bundles under content/articles/, each with its own index.md.
- The Articles landing page and its manual list are in content/articles/_index.md.
- The home page and its Latest writing list are in content/_index.md.
```

Add these working agreements alongside the existing rules:

```markdown
- For content tasks, use only the source files named in the task. Do not search the web or add material from memory.
- Do not state anything the named source does not support. Where the source records a gap, say that it is unknown rather than estimating.
- Credit every external reference in a Sources section in the page body, with a link and a short explanation.
- New articles use title, description, and draft in front matter, and the headings What this is about, What happened, What I would do differently, and Sources.
- Leave new pages at draft: true. Publication is the reader's decision.
```

Read the file after editing, then commit it:

```text
git add AGENTS.md
git diff --cached
git commit -m "Add content sourcing and attribution agreements for agent work"
```

Persistent guidance saves repetition and gives you something concrete to point at when a result is wrong. It is not enforcement, so the requests below still state their own boundaries.

## 13.4 Ask for a plan before a draft

Asking straight away for a finished article produces a page that is expensive to check: structure, prose, and claims arrive together, and a fault in the structure has already shaped every paragraph. Ask for a plan instead.

Start a read-only session from the project root:

```text
codex --sandbox read-only --ask-for-approval on-request
```

Check `/status`, then paste:

```text
Read AGENTS.md and sources/publishing-notes.md. Do not edit any file.

I want to publish one article based only on those notes.

Produce, as your reply in this session:
1. A proposed title and a one-sentence description.
2. Under each of the four agreed article headings, the points you would make.
3. A table with one row per factual statement you propose: the statement,
   and the exact line of the notes that supports it.
4. A list of anything an article on this topic would normally mention
   that these notes do not support.

Do not write the article yet. Do not add material from any other source.
```

Read the reply against the notes. A useful plan is recognisable by what it refuses to claim: item 4 should name the deployment duration and custom domains, because the notes record both as unmeasured or untried. Item 3 should map every proposed statement onto a line you can find.

Ask again if it compares hosting providers, quotes the documentation at length, describes your motivation, or offers a statement whose supporting line you cannot locate. Correcting a plan costs one short request; correcting a draft built on that plan costs far more.

Use `/exit`, then confirm that nothing changed:

```text
git status
```

> **First checkpoint:** you have a plan whose every claim is traceable to a line of your notes, and an explicit list of what the notes cannot support.

## 13.5 Draft the article from the source only

Restart with permission to edit the project:

```text
codex --sandbox workspace-write --ask-for-approval on-request
```

A new session does not carry the previous conversation, so the task is stated in full again. Check `/status`, then paste:

```text
Read AGENTS.md and sources/publishing-notes.md before editing.

Task: Write one article from those notes, using the agreed article model.

Create exactly one new file:
content/articles/publishing-with-github-pages/index.md

Front matter: title, a one-sentence description, and draft: true.
Body headings, in this order:
## What this is about
## What happened
## What I would do differently
## Sources

Use no more than 400 words in the body. Plain paragraphs and short lists only.
Every factual statement must be supported by a line in the notes.
Where the notes record something as not measured or not attempted, either
omit it or state plainly that it is unknown. Do not estimate.
Paraphrase the GitHub reference; do not quote it at length. Credit it under
Sources with its URL and one sentence explaining what it covers.

Change no other file. Do not edit layouts, CSS, configuration, the workflow,
the JSON directory, or any existing page.
Do not stage, commit, push, or deploy.

Run hugo --minify --panicOnWarning if permissions allow, and report the result.
Finish by listing the file you created and any statement you were unsure about.
```

When it finishes, use `/exit` and inspect the result yourself:

```text
git status
git diff --stat
git diff --cached
```

The new bundle is untracked, so it appears under status rather than in an ordinary diff. The staged diff should be empty, and no existing file should be modified yet.

Open `content/articles/publishing-with-github-pages/index.md` and read every line against the notes, finding the line that supports each sentence. Check that the front matter has all three fields, that `draft` is still `true`, and that Sources credits the GitHub reference with a working URL.

Build and preview. The article is a draft, so draft rendering has to be enabled, as in Chapter 2:

```text
hugo --minify --panicOnWarning
hugo server -D
```

Open `/articles/publishing-with-github-pages/`. Check the heading order, read the page as a visitor, and follow the link in Sources. The Articles landing page will not list the new article yet; its list has been manual since Chapter 3.

> **Second checkpoint:** one new article exists, reads accurately against your notes, and renders in a draft preview without affecting any other page.

## 13.6 Make the coordinated update across several files

An article nobody can reach is not published work. Three existing files need to know about it, and none updates itself: the Articles list, the home page's Latest writing list, and the resource directory that now holds the reference you cited.

Stop the preview, start a session as before, and paste:

```text
Read AGENTS.md, content/articles/_index.md, content/_index.md, and
assets/data/resource_links.json before editing.

Task: Connect the new article to the rest of the site.
Edit exactly these three files.

1. content/articles/_index.md — add one bullet to the existing Start reading
   list, in the same format as the existing bullet, linking to
   publishing-with-github-pages/ with a short explanation.

2. content/_index.md — add one bullet to the existing Latest writing list,
   in the same format as the existing bullet.

3. assets/data/resource_links.json — add one record at the end of the array
   for the GitHub publishing-source page cited in the new article. Use the
   five agreed keys: title, url, description, topics (an array of strings),
   and start_here (the Boolean false). The url is the complete HTTPS address.

Preserve all existing bullets, records, sections, and front matter.
Match the relative-link style already used in each file.
Change nothing else. Do not stage, commit, push, or deploy.

Run hugo --minify --panicOnWarning and report the result.
```

Three files in one request is a larger surface than anything in Chapter 8, so review them one at a time:

```text
git diff --stat
git diff -- content/articles/_index.md
git diff -- content/_index.md
git diff -- assets/data/resource_links.json
```

Check each change against what the file already did. The bullet in `content/articles/_index.md` is relative to the Articles section and needs no `articles/` prefix; the one in `content/_index.md` is relative to the site root and does. Chapter 8 showed how a link can be well formed and still point to the wrong place, and Chapter 12 set the rule that directory records hold complete external addresses. A record with a relative URL, or with a quoted `"false"` instead of the Boolean, is a mistake the build will not report.

Restart the preview as an ordinary visitor would see it:

```text
hugo server
```

The article is still a draft, so it should be absent, and the two new bullets should lead to a page that is not there yet. That is the expected intermediate state, not a fault. Check the new entry on Resources, follow its external link, and confirm the three original records are unchanged.

If one of the three edits is wrong, correct it with a named follow-up, or restore that single path:

```text
git restore -- content/_index.md
```

Restoring one path leaves the other two edits and the untracked article in place. Inspect status before and after, rather than reaching for a broad cleanup.

## 13.7 Test your review on an unsupported claim

Your notes say the deployment time was never measured. An article about publishing has an obvious gap where that sentence would go.

In the new article, under What happened, add this sentence:

```text
Deployments usually finish in under a minute.
```

Save and build:

```text
hugo --minify --panicOnWarning
```

The build succeeds. Nothing in the project examines that sentence. It is grammatical, plausible, and in keeping with the paragraph around it, and nothing you recorded supports it. It may even be true; you have no evidence either way, and the article presents it as experience.

Ask three questions of any statement in a page you did not write yourself:

1. Is it in the source material at all?
2. If it is, does the source support it as strongly as this wording claims?
3. If a reader relied on it and it were wrong, what would happen?

A broken link announces itself the moment someone activates it. An unsupported sentence can stay on a site for years, and it is the mistake agent-assisted content produces most readily, because fluent prose is exactly what the tool is good at.

Remove the experiment:

```text
git status
```

The article is still untracked, so `git restore` cannot recover it from history. Delete the sentence in your editor, save, and build again. Git protects what it has been given: until the bundle is committed, your editor holds the only earlier state.

> **Third checkpoint:** you found an unsupported claim that the build accepted, and you can explain why review has to read for meaning as well as for errors.

## 13.8 Approve, save, and make one request of your own

Publication is your decision, taken once and deliberately. In `content/articles/publishing-with-github-pages/index.md`, change:

```yaml
draft: true
```

to:

```yaml
draft: false
```

Restart a normal preview with `hugo server` and review the whole result:

| Check | What should be true |
| --- | --- |
| The new article | Every statement traces to your notes; the two gaps are absent or marked unknown |
| Its Sources section | The GitHub reference is credited, and its link works |
| Articles | Both articles are listed, and both links work |
| Home | Latest writing lists both articles, and both links work |
| Resources | Four directory records, correct topics, one Start here label |
| The first learning note | Its body, image, and links are unchanged |
| Projects | Its generated list and section sentence are unchanged |

Then build, inspect, and stage the intended paths:

```text
hugo --minify --panicOnWarning
git status
git add content/articles/publishing-with-github-pages/index.md
git add content/articles/_index.md content/_index.md assets/data/resource_links.json
git diff --cached
```

Read the staged diff in full. It should contain one new article, two added bullets, and one added JSON record. `sources/publishing-notes.md` and `AGENTS.md` were committed earlier in the chapter and should not reappear here.

```text
git commit -m "Publish an agent-drafted article and link it from the site"
git status
```

Now make one request of your own. Ask the agent to tighten the article's `description` to a single clause without changing its meaning, or to add one further topic label to the new record. Name the file, say what counts as an improvement, and keep the same limits on other files and on Git actions.

Review the diff and the page, then accept it or keep your version. The reading-list project from Chapter 9 is an honest candidate for a later contribution: its notes do not exist yet, and an article cannot be written from material you have not gathered.

The local checkpoint is enough to continue. When you decide to publish, use Chapter 7's push, deployment check, and live-page verification yourself.

## Completion check

- [ ] I can say which parts of a content task I may delegate and which I may not.
- [ ] I supplied source material in `sources/` and committed it before it was used.
- [ ] I agreed an article model and recorded it in the project guidance.
- [ ] I obtained a plan whose claims map to specific lines of my notes.
- [ ] I reviewed the draft sentence by sentence against the source.
- [ ] The article credits its external reference visibly in the page body.
- [ ] I made a coordinated update to three files and reviewed each one separately.
- [ ] I found the unsupported sentence that the build accepted, and removed it.
- [ ] I decided publication myself and committed the four intended paths.

This is enough agent-assisted content work for our next steps. Bulk generation, translation, retrieval over your own material, automated fact-checking, and unattended contributions are outside this chapter's scope. The method matters more than the volume: supply the material, bound the request, review the claims, decide publication.

Chapter 14 turns the parts of this review that can be stated as rules into automated checks on a pull request, so that a contribution is tested before anyone decides to merge it.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| The agent adds material that is not in the notes. | Name the rule it broke, ask for a corrected draft from the source alone, and reread the result rather than the summary. |
| It fills a gap with an estimate. | Point at the relevant Not line in the notes. Require an explicit statement that the figure is unknown, or its omission. |
| It quotes the GitHub page at length. | Ask for a paraphrase and a credited link. Long quotations are unnecessary here and harder to maintain. |
| The new article does not appear in the preview. | It is a draft. Use `hugo server -D`, or set `draft: false` when you have decided to publish. |
| The article appears but the two lists do not mention it. | Both lists are manual. Section 13.6 is the step that adds them. |
| A new bullet leads to a missing page. | Compare its relative form with the existing bullet in the same file; the Articles list and the home page need different prefixes. |
| Start here appears on the new record. | Set `start_here` to the unquoted Boolean `false`, as agreed in Chapter 12. |
| The directory record uses a relative address. | Directory records hold complete external HTTPS addresses. Internal notebook links stay in Markdown. |
| The build passes but a sentence looks doubtful. | The build does not read for meaning. Trace the statement to its source line, or remove it. |
| `git restore` will not recover the new article. | An untracked file has no committed state. Edit it in your editor, and commit once you have accepted it. |
| The staged diff contains files from earlier sections. | `sources/publishing-notes.md` and `AGENTS.md` were committed separately. Unstage anything unrelated before committing. |

Source notes, repository text, and retrieved pages can contain instructions aimed at whatever reads them. Treat such material as content to assess, not as authority to widen the task, publish, or change credentials.

## One acceptable article for comparison

Your agent will choose different wording. This example shows the intended scale, the heading order, and the level of claim the notes actually support. It is not a transcript of a recorded agent run.

````markdown
---
title: "What I learned publishing with GitHub Pages"
description: "How this notebook reached a public address, and what went wrong the first time."
draft: false
---

## What this is about

This notebook is published from its own repository rather than uploaded by
hand. Setting that up went wrong once, in a way that was easy to misread.

## What happened

A Pages site has to be told where its content comes from. I chose the GitHub
Actions route rather than publishing from a branch, so a workflow builds the
site with Hugo and deploys the built output. The generated `public/` folder is
never committed.

The first deployment failed, because I pushed before setting the publishing
source. Setting it and running the workflow again fixed it. The failure was
only legible in the Actions log; the browser showed a missing page, which told
me nothing about the cause.

One configuration detail mattered more than I expected: `baseURL` has to
include the repository path. Before I corrected it, the live site loaded
without its stylesheet and its internal links went to the wrong place.

I also learned to distrust a passing local build as evidence about the live
site. `hugo --minify --panicOnWarning` succeeded before the push that failed
to deploy.

## What I would do differently

I would set the publishing source before the first push, and read the Actions
log before looking at the site in a browser.

I have not measured how long a deployment usually takes, and I have not tried
a custom domain, so I cannot say anything useful about either.

## Sources

- [GitHub: configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) — Explains how a Pages site is told where to publish from, including the GitHub Actions route used here.
````

The matching directory record, added at the end of the array in `assets/data/resource_links.json`:

```json
{
  "title": "GitHub: configuring a publishing source",
  "url": "https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site",
  "description": "The official explanation of how a GitHub Pages site is told where its content is published from.",
  "topics": ["GitHub Pages", "Publishing"],
  "start_here": false
}
```

And the two added bullets, in their existing lists:

```markdown
- [What I learned publishing with GitHub Pages](publishing-with-github-pages/) — Setting up a publishing source, and the first deployment that failed.
```

```markdown
- [What I learned publishing with GitHub Pages](articles/publishing-with-github-pages/)
```

---

## Editorial note for the author — remove before publication

This is the second half of the agent thread opened in Chapter 8. That chapter taught a bounded single-file edit; this one teaches sourcing, decomposition, attribution, and claim checking on a contribution too large to verify at a glance. The three-request sequence — plan, draft, coordinated update — is the structural point, and the plan request is read-only so a structural objection costs one cheap round trip.

The supplied notes describe the reader's own Chapters 6 and 7 experience, deliberately: the reader is the authority on the source, so checking factual accuracy is genuinely possible rather than a performance. The two gap lines carry the main lesson and must survive editing. Section 13.3's article model completes the content-modelling thread Chapter 9 left open, and attribution sits in the page body because the starter renders no attribution field — reusing Chapter 9's lesson about front matter not being self-displaying.

Section 13.7's unsupported sentence is the designed failure, mirroring Chapter 8's link mistake: both pass `hugo --minify --panicOnWarning`. The recovery differs on purpose — the new bundle is untracked, so `git restore` does not apply, which gives a concrete reason for committing a contribution once accepted. Check in the trial that beginners do not read this as a defect in Git.

This is the longest chapter at roughly 4,830 words, though its reader-facing prose is mid-range; the difference is the three prompts, the supplied notes, and the comparison article, which are reference material and were not cut to reach a total. If the trial shows it running long, move the prompts into a companion command card as Chapter 6 does for Git.

Nothing here has been validated. See the validation record for what a replay must confirm.
