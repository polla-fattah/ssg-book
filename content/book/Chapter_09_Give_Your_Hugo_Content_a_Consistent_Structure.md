---
title: "Give Your Hugo Content a Consistent Structure"
weight: 9
book_number: 9
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

Your website has one project page. Adding a second is easy: create another Markdown file and begin writing. After several projects, however, you might notice that one page explains its purpose, another lists tools, and a third never says whether the work has started.

A small shared structure makes those pages easier to write, compare, and maintain. It also gives an AI agent concrete requirements to follow. The structure should answer useful questions without making every page look like a long form.

In this chapter, you will improve the existing notebook project, create a reusable starter, and add a short page describing a planned reading list. Both project pages will carry consistent metadata and useful headings. They will continue to use the layout you already have.

## What you will be able to do

By the end, you should be able to:

- Choose a few useful fields and headings for a repeatable kind of content.
- Read and edit the basic YAML values used in Hugo front matter.
- Create a project page from an archetype and distinguish its source path from its title.
- Preview a draft, review its information, and make it reachable from the Projects page.

Start from the completed Chapter 8 project with a clean Git working tree. (If you are following along in the companion repository `ssg-playground`, make sure you are on branch `chapter-08` or check out the completed chapter on branch `chapter-09`.) You need the same Hugo installation and editor; no new service or account is required. The agent review near the end is optional.

## 9.1 Improve the project you already have

Open `content/projects/learning-notebook/index.md`. Its front matter currently provides a title and a draft setting. Replace just that opening block with:

```yaml
---
title: "My knowledge notebook"
description: "A personal website for learning notes, small projects, and useful references."
draft: false
params:
  status: "in-progress"
  tools:
    - "Hugo"
    - "Markdown"
---
```

Keep your existing body text and links. If you have personalised the title, retain your own title. The example describes the book project; adjust any statement that does not describe your actual work.

Next, update the paragraph under `## Current status` to reflect your progress. For example:

```markdown
This is a work in progress. The site has organised content, a shared layout, and a Git history. I am making its project descriptions more consistent.
```

Before the final Back to Projects link, add:

```markdown
## Next step

Use the same small set of fields and headings when describing another project.
```

Save, run `hugo server`, and open the notebook project through Projects. You should see the revised paragraph and new heading. Its title, navigation, and existing links should still work.

You will **not** see an automatic status label or tools list. The shared layout currently displays the page title and Markdown body. Storing another value in front matter does not automatically teach that layout to display it. The description is also not automatically added to the HTML head by our minimal starter.

That distinction matters: the source now contains information that later templates can use, while the visible improvement comes from the body text you just edited.

> **First checkpoint:** the existing project has useful metadata and an updated description, and you can explain which changes are visible on the page.

## 9.2 Decide what every project should explain

A **content model** is an agreement about the information a kind of content should contain. For this site, a project needs a name, a short description, a state of progress, and enough writing to explain the work.

We will use this small agreement:

| Location | Field or heading | Our rule |
| --- | --- | --- |
| Front matter | `title` | A readable project name |
| Front matter | `description` | One sentence explaining the project's purpose |
| Front matter | `draft` | Whether this page is still being prepared for publication |
| Under `params` | `status` | One of `planned`, `in-progress`, or `complete` |
| Under `params` | `tools` | A list of relevant tools; an empty list is acceptable |
| Body | Purpose | What the project is intended to achieve |
| Body | Current status | What has actually happened so far |
| Body | What I have learned | Specific learning, or an honest statement that work has not begun |
| Body | Next step | One concrete action, or a clear completion statement |

The three status values are **our editorial choices**, not a built-in Hugo workflow. Hugo will not reject a fourth value merely because this table excludes it. We must review the values ourselves until we deliberately add validation later.

The table is also a scope limit. We do not need an owner field when every project belongs to the same author, a budget for a reading list, or a percentage complete that nobody can measure reliably.

### Keep publication state separate from project progress

`draft` describes the **page**. `status` describes the **project**.

A page can be ready to publish even when its project is only planned. Conversely, a completed project can have an unfinished page that still needs editing. For example:

```yaml
draft: false
params:
  status: "planned"
```

This combination is reasonable: readers can see an honest description of a plan. It does not claim that the planned work is finished.

### Separate quick facts from explanation

The status value gives a short answer that a future layout can display or use for grouping. The Current status paragraph explains the evidence behind it. They serve different purposes, but must agree.

Avoid putting several sentences into `status`, or hiding the project's entire story in metadata. Keep the explanation in Markdown, where headings, links, and paragraphs are convenient to read and edit.

Likewise, an article and a project do not need identical models. A learning note might need a question and an explanation rather than a project status. We will improve one content family at a time.

## 9.3 Read only the YAML you need

Our pages already use YAML front matter between two `---` lines. This section explains the few shapes introduced by the project model. We will keep using YAML for these pages and TOML for `hugo.toml`; the formats do not need to match. Hugo supports several front matter formats. [Hugo: front matter](https://gohugo.io/content-management/front-matter/)

### A named value

```yaml
title: "My knowledge notebook"
```

`title` is the key; the quoted text is its value. Keep the colon and the space after it. The quotation marks are straight quotes, not typographic opening and closing quotes copied from a word processor.

Use quotes for the text fields in this chapter. They make the boundaries clear, especially when a title contains a colon:

```yaml
title: "Reading list: website publishing"
```

If text contains a double quotation mark, you can put the whole value in single quotes instead, provided the text does not itself require handling an apostrophe:

```yaml
title: 'Notes on "static" websites'
```

You do not need every YAML quoting rule to complete this project. Follow the simple examples and use your editor's error messages when a value becomes more complicated.

### A true-or-false value

```yaml
draft: false
```

`false` is a Boolean value. Keep `true` and `false` lowercase and unquoted. Writing `"false"` gives the YAML reader text instead of a Boolean; relying on later conversion makes the source less clear.

The distinction is useful beyond this one field. A name is text, a yes-or-no setting is a Boolean, and several tools form a list.

### Related values under one key

```yaml
params:
  status: "in-progress"
  tools:
    - "Hugo"
    - "Markdown"
```

Indentation describes the relationships. `status` and `tools` belong under `params`; the two list entries belong under `tools`. Use spaces, with two spaces for each level shown here. Do not use tabs for indentation.

`params` is a mapping: it groups named values. The dash-prefixed entries form a list. To add another relevant tool later, add another entry at the same indentation. To record that no tools have been chosen, use:

```yaml
params:
  status: "planned"
  tools: []
```

An empty list is clearer than inserting a tool merely to fill a space. It also preserves the expected value shape for later template code.

Hugo provides recognised fields such as `title`, `description`, and `draft`. Put our custom project information under `params`, following Hugo's documented convention. Do not add a second `params` block if one already exists; add the new values within the existing block. [Hugo: custom page parameters](https://gohugo.io/content-management/front-matter/#parameters)

### A short source-reading check

Before continuing, point to the value that answers each question in your notebook project:

1. What should the page be called?
2. Is the page ready for an ordinary build?
3. Is the project finished?
4. Which tools does the page record?

If you can answer by reading the front matter, you know enough YAML for the exercise. More formats and larger data collections belong in Chapter 12.

## 9.4 Keep the page structure and address predictable

Chapter 3 introduced two filenames that look almost the same. They still have different jobs:

| Source | Job in our site |
| --- | --- |
| `content/projects/_index.md` | Introduces the Projects section and contains its manual links |
| `content/projects/learning-notebook/index.md` | Describes one project |
| `content/projects/reading-list/index.md` | Will describe our second project |

The folder containing an `index.md` is a **leaf bundle**. It groups one page with any resources that belong to it. A bundle can start with only its Markdown file; an image is not required. The section uses `_index.md` because it can contain project pages beneath it. [Hugo: page bundles](https://gohugo.io/content-management/page-bundles/)

Do not rename `content/projects/_index.md` to `index.md` to make the names look consistent. Their different names express a useful structural difference.

Under our current configuration, the new folder will give the second project an address ending in:

```text
/projects/reading-list/
```

On the GitHub project site, that follows `/my-knowledge-site/`. The page title can be “My website reading list” while its folder remains `reading-list`. Changing the title alone will not change this folder-derived address in our starter.

Keep folder names short, lowercase, and separated with hyphens. Avoid changing an established folder name just because you improve a title; existing links may rely on its address. Hugo supports explicit URL overrides, but we do not need them for this exercise.

If a project later needs a screenshot, place it beside that project's `index.md` and use the relative image-link technique from Chapter 2. Keep site-wide assets such as the shared stylesheet in their existing location.

## 9.5 Make a reusable starter with an archetype

Copying an old project page can also copy its facts, links, and completion claims. A starter can provide the useful structure without carrying over another project's story.

Hugo calls a new-content starter an **archetype**. Create a folder named `archetypes` beside `content`, then create `archetypes/projects.md`. If that file already exists in your project, inspect it and adapt it instead of replacing unrelated work.

Use this complete starter:

```markdown
---
title: "Replace with a project name"
description: "Replace with one sentence about the project's purpose."
draft: true
params:
  status: "planned"
  tools: []
---

## Purpose

Explain what this project is intended to achieve.

## Current status

Describe what has actually happened so far.

## What I have learned

Record a specific lesson, or explain that work has not begun.

## Next step

Name one concrete action.

[Back to Projects](../)
```

This starter is deliberately plain. It supplies text and headings without generating dates, guessing titles, or introducing template expressions. You will replace its prompts before publishing.

Archetypes can supply both front matter and body content. They are used when new content is created; editing an archetype does not rewrite pages you already created from it. That is why we updated the notebook project separately. [Hugo: archetypes](https://gohugo.io/content-management/archetypes/)

### Create the second project

Stop the preview with **Ctrl+C**. From the project root, run:

```text
hugo new content --kind projects projects/reading-list/index.md
```

The command asks Hugo to use the `projects` archetype and create a file beneath `content/`. Do not add a second `content/` prefix to the path shown. The `--kind` option selects the archetype for this creation step; it is not our project's progress status. [Hugo: new content command](https://gohugo.io/commands/hugo_new_content/)

Open `content/projects/reading-list/index.md`. Confirm that it contains the starter's fields and headings. You should see `draft: true`, an empty tools list, and prompts to replace.

If the destination already exists, inspect the existing file. Do not use an overwrite option to force the command through. This exercise assumes that the second project has not yet been created.

### Turn the prompts into useful content

Replace the generated file with this complete example, or equivalent truthful wording about your own planned reading list:

```markdown
---
title: "My website reading list"
description: "A planned collection of resources for learning website publishing."
draft: true
params:
  status: "planned"
  tools:
    - "Markdown"
---

## Purpose

I plan to collect a small set of resources that help me learn website publishing.

## Current status

This is a proposal. I have not yet selected or reviewed the resources.

## What I have learned

The reading work has not begun. I will record useful findings as I review each resource.

## Next step

Choose three resources and write one sentence explaining why each belongs in the list.

I will begin with the references on the [Resources page](../../resources/).

[Back to Projects](../)
```

Here, `Markdown` is a planned tool. For our model, the tools list records intended tools while a project is planned, and actual tools once work begins. Update it as the project changes.

Notice that the example does not claim to have read anything. Creating a page about a plan is not evidence that the plan has been carried out.

## 9.6 Preview the draft, then connect it to Projects

Start a preview that includes drafts:

```text
hugo server -D
```

Use the address Hugo reports. Open the new project's route by adding `projects/reading-list/` to that base address. With the earlier project-site configuration and the usual port, this will normally be:

```text
http://localhost:1313/my-knowledge-site/projects/reading-list/
```

Use your actual base path and port. The page is not yet linked from Projects, so opening the route directly is expected.

Read the whole page. Follow Resources and Back to Projects. Confirm that both stay within the configured site path. The relative destinations are written for a page two levels below the site's root, just like the existing notebook project.

The `-D` option includes draft pages in this preview. It does not edit the front matter or mark the page ready. Ordinary builds exclude drafts unless configured otherwise. [Hugo: draft field](https://gohugo.io/content-management/front-matter/#fields)

### Make a deliberate publication decision

When the writing is ready, change only:

```yaml
draft: false
```

Leave `status: "planned"` as it is. The page is ready; the reading project is still a plan.

Stop the server, then restart with the normal command:

```text
hugo server
```

Reopen the page and check that it is available without draft inclusion. Restarting makes it clear which preview settings you are using.

Now open `content/projects/_index.md`. Preserve its introduction and existing project link. Under `## Current work`, add:

```markdown
- [My website reading list](reading-list/): A planned collection of resources for learning website publishing.
```

Visit Projects through the navigation. Both project links should work, and each project should link back to Projects. The list is still manual: creating a page or adding metadata does not insert a link into it. Chapter 10 will introduce the template tools needed to automate a list.

If you prefer to keep your page as a draft, keep `draft: true` and postpone adding this public-facing link. A manually written link can point to a page that an ordinary build excludes.

A build can leave output from an earlier run in place. Changing a previously generated page back to a draft is therefore not a reliable way to withdraw an already published copy; removal needs a separate output and deployment check.

A draft setting also does not make source private. If you push a draft Markdown file to a public GitHub repository, its text remains readable in that repository even when the website omits the page.

> **Second checkpoint:** a second project uses the agreed structure, appears in the normal preview, and is reachable through Projects without claiming that its planned work is complete.

## 9.7 Find and repair a front matter mistake

Stop the server. In the new reading-list page, temporarily remove the closing quote from the title line:

```yaml
title: "My website reading list
```

Leave the rest of the file untouched. Run:

```text
hugo --minify --panicOnWarning
```

The build should fail because the quoted value is unfinished. Read the error and identify the named source file. Its reported line may be where parsing became impossible rather than the exact place where you removed the quote.

Restore the correct line:

```yaml
title: "My website reading list"
```

Build again. The successful build tells you that Hugo can process the repaired source. It does not establish that the project description is accurate or that its status follows our editorial agreement.

For example, `status: "planed"` is valid quoted text but misspells our chosen value. Likewise, a tools list can contain an invented claim without causing a build error. There are two different checks: whether the file can be processed, and whether its contents meet the model and describe reality.

Before saving the checkpoint, compare both project pages with the table in Section 9.2. Check that the status values use the agreed spelling and that the paragraphs support them. Read the new page for leftover starter prompts.

Do not judge a failed build by looking for an HTML file left in `public/`. Output from an earlier successful build may remain. Read the current command result and repair the source.

## 9.8 Review, make one choice, and save

For a small independent variation, choose one real next action for your reading-list project and rewrite its Next step paragraph in your own words. Make the action specific enough that you can later tell whether you did it.

Then examine the tools list. Keep Markdown if it is relevant, choose a different actual plan, or use an empty list if undecided. Do not add fields simply to make the page look more sophisticated.

This is a modest exercise in modelling: decide what belongs in an existing field, retain its expected shape, and keep the explanatory writing consistent with it.

### Optional: ask the agent to check the agreement

Using Chapter 8's read-only inspection approach, give the agent this request:

```text
Read AGENTS.md and these files:
- content/projects/learning-notebook/index.md
- content/projects/reading-list/index.md
- archetypes/projects.md

Do not edit files or run commands that modify the project.

Our project model requires title, description, draft, params.status,
and params.tools. Status must be planned, in-progress, or complete.
Tools must be a list, which can be empty.
The body should contain Purpose, Current status, What I have learned,
and Next step.

Check both project pages against that agreement. Identify missing fields,
wrong value shapes, leftover starter prompts, and contradictions between
status and body text. Treat the archetype's prompts as intentional.
Report file-specific findings. Do not invent facts or claim to verify
real-world progress from these files alone.
```

Read the cited lines yourself. If the agent suggests a correction, decide whether it is supported before editing. It can compare the files with an explicit agreement; it cannot establish that you performed work outside those files.

### Save the completed chapter

Run the ordinary build and inspect status:

```text
hugo --minify --panicOnWarning
git status
git diff
```

The intended changes are the existing notebook project, the Projects section, the new archetype, and the new reading-list page. Remember that `git diff` alone does not display untracked files. Open both new files before staging them.

Stage only the chapter's four paths:

```text
git add content/projects/learning-notebook/index.md content/projects/_index.md archetypes/projects.md content/projects/reading-list/index.md
git diff --cached
```

Check the complete staged result, including the new files. When it matches what you reviewed, commit:

```text
git commit -m "Define a consistent project model and add a reading-list project"
git status
```

The working tree should be clean. Publishing remains the separate push-and-check process from Chapter 7; the local checkpoint is sufficient for continuing the book.

## Completion check

- [ ] Both projects use the agreed fields and body headings.
- [ ] I can distinguish page readiness from project progress.
- [ ] I can read a text value, a Boolean, a mapping, and a list in the front matter.
- [ ] I created the second project from the projects archetype and replaced its prompts.
- [ ] I understand why changing an archetype does not update existing pages.
- [ ] I checked the second page in the normal preview and tested its links.
- [ ] I repaired the deliberate YAML mistake and reviewed the actual information.
- [ ] I inspected and committed the four intended source files.

Chapter 10 will use these consistent fields in Hugo templates. We will begin with small expressions and conditions, then use a loop to turn a collection of pages into a useful list.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| Status, tools, or description do not appear on the page. | Our current layout does not display them. Check the source; template use comes next. |
| Hugo reports a YAML parsing error. | Check quotes, colons, indentation, and the two front matter delimiters in the named file. |
| The new command produces a different starter. | Check `archetypes/projects.md`, the project root, and the `--kind projects` option. |
| The command says the destination exists. | Inspect that file rather than overwriting it. You may already have completed the creation step. |
| The new page is absent from a normal preview. | Check `draft`, the filename, and the address. Use `-D` only when intentionally previewing drafts. |
| The page opens directly but is missing from Projects. | The section list is manual. Add its link after the page is ready. |
| A link leaves the GitHub project path. | Compare its relative destination with the examples and inspect the resolved address. |
| Editing the archetype does not change an old page. | That is expected; update existing content separately. |
| A build passes despite an incorrect project status. | Review the values against our model. No custom status validator has been installed. |

