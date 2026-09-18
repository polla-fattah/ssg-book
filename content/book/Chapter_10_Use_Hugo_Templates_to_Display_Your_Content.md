---
title: "Use Hugo Templates to Display Your Content"
weight: 10
book_number: 10
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1, 17 September 2026**  
*Checked with Hugo 0.150.0 on Linux in a focused fixture. No beginner trial, browser review, or deployment yet.*

Your two project pages now contain useful information in their front matter. The description, status, and tools are organised, but visitors cannot see them yet. You also maintain a separate list of project links by hand.

A template can use those existing values to produce the page. Change a project's description once, and Hugo can use it both on the project page and in the Projects list.

We will make that happen in small steps. First, display a description. Next, show status and tools when they are available. Finally, let Hugo generate the Projects list from the pages in that section.

## What you will be able to do

By the end, you should be able to:

- Read simple template expressions and connect their values to content files.
- Use `if` and `with` to display information conditionally.
- Use `range` to display a list, while tracking what the dot represents.
- Build an automatic Projects list and diagnose a common template error.

Start from the completed Chapter 9 checkpoint. Both project pages should be ready for normal builds, with `draft: false`, and the Git working tree should be clean. If you deliberately retained the reading-list page as a draft, finish reviewing it before following the two-project examples below.

Use the same Hugo installation. These exercises continue the `layouts/all.html` convention used since Chapter 1 and tested with Hugo 0.150.0. We will edit that existing layout and the Projects section introduction. No new package, theme, or programming-language installation is required.

## 10.1 Display one value before learning more syntax

Open `layouts/all.html`. Inside its `article` element, find:

```html
<h1>{{ .Title }}</h1>
{{ .Content }}
```

Insert the following block between those two lines:

```html
{{ if .Description }}
  <p>{{ .Description }}</p>
{{ end }}
```

The article should now begin:

```html
<article>
  <h1>{{ .Title }}</h1>
  {{ if .Description }}
    <p>{{ .Description }}</p>
  {{ end }}
  {{ .Content }}
</article>
```

Save and run `hugo server`. Open the notebook project through Projects. Its one-sentence description should appear between the title and Purpose heading. Open the reading-list project and check its description too.

Then visit About. If you have followed the supplied examples, that page has no description field, so the new paragraph should be absent. The title and ordinary Markdown content should still appear.

The three added lines mean: if this page has a non-empty description, put that description inside a paragraph. `end` closes the conditional block. The HTML opening and closing paragraph tags belong inside it, so a missing description does not leave an empty paragraph behind.

We have made the first useful template change. The same instruction serves both project pages because Hugo evaluates it separately for each page.

> **First checkpoint:** descriptions appear where they are provided, and pages without descriptions still render normally.

## 10.2 Understand the HTML and template instructions together

Hugo templates use Go's template language. You do not need to learn the Go programming language or install its compiler for these exercises. Hugo already contains the template-processing machinery. [Hugo: introduction to templating](https://gohugo.io/templates/introduction/)

Consider the line you have used since Chapter 1:

```html
<h1>{{ .Title }}</h1>
```

The `h1` tags describe an HTML heading. The action between `{{` and `}}` asks Hugo for a value. When rendering the reading-list page, Hugo produces a heading such as:

```html
<h1>My website reading list</h1>
```

The browser receives the completed HTML. It does not execute `.Title`, and this feature does not require JavaScript. Editing a template changes what Hugo generates during the next build.

### Read the values already in our layout

| Expression | Meaning at the outer level of this page layout |
| --- | --- |
| `.Title` | The current page's title |
| `.Description` | Its description from front matter |
| `.Content` | Its body rendered from Markdown into HTML |
| `.Params.status` | Its custom `status` parameter |
| `.Site.Title` | The site's title from configuration |

The opening dot means **the current context**: the value or object the template is currently working with. At the outer level of this layout, that is the page Hugo is rendering.

Keep the spelling and capitalisation shown in the examples. Hugo's page methods use names such as `Title` and `Description`; our custom parameter key remains lowercase `status`.

You do not have to memorise every available method. For each new expression, ask which source value it should read and which visible result it should produce.

### Conditions do not need a value to be printed

In the description block, `if .Description` checks whether the value is non-empty. The separate `{{ .Description }}` prints it. `if` itself does not change the current context.

Empty text, an empty list, and `false` all count as false in these conditions. A non-empty description counts as true. This is sufficient for the fields we are using. [Hugo: if](https://gohugo.io/functions/go-template/if/)

### Recognise a function and a pipe

The footer and navigation already contain this pattern:

```html
<a href="{{ "about/" | relURL }}">about this notebook</a>
```

`"about/"` is a text value. `relURL` is a function. The pipe character, `|`, passes the value on its left to the function on its right. Here, Hugo forms a URL using the site's configured base path.

For the book's GitHub project site, the result includes `/my-knowledge-site/about/`. Keep the input as `"about/"`; a leading slash would request a root-relative path and change the result. [Hugo: relURL](https://gohugo.io/functions/urls/relurl/)

Later in this chapter, we will obtain URLs directly from page objects. Use the value appropriate to the task: a known site path for the existing navigation, or a page's own URL when listing pages.

## 10.3 Use `with` when a value is optional

The description block checks `.Description` and then names it again. `with` provides a convenient alternative. Replace that entire `if` block with:

```html
{{ with .Description }}
  <p>{{ . }}</p>
{{ end }}
```

Save and confirm that the visible result is unchanged.

For a non-empty description, `with` enters its block and makes the description the current context. Inside that block, the dot is the description text. After `end`, the previous page context is restored. [Hugo: with](https://gohugo.io/functions/go-template/with/)

This is why the inner expression is `{{ . }}`. Writing `.Description` there would try to ask the description text for another description. We will deliberately test that kind of mistake later.

Now add a separate block immediately after the description block and before `.Content`:

```html
{{ with .Params.status }}
  <p><strong>Status:</strong> {{ . }}</p>
{{ end }}
```

The notebook project should show `Status: in-progress`; the reading-list project should show `Status: planned`. Other pages without that parameter should show neither the label nor an empty paragraph.

We are displaying the stored status value directly. Turning `in-progress` into a more polished label is a possible later improvement. Keep the stored values consistent with Chapter 9's agreement.

### Follow the dot through one block

| Position | What `.` represents |
| --- | --- |
| Before `with .Params.status` | The page being rendered |
| Inside that `with` block | Its status text, such as `planned` |
| After the matching `end` | The page again |

Keep the description and status blocks beside one another. The status block must start **after** the description block's `end`, so it can read `.Params` from the page.

The condition only establishes that a value is present. It does not verify that the status is one of our agreed values or that the project's reported progress is true. The content review from Chapter 9 still matters.

## 10.4 Repeat markup for the tools list

A status is one value; tools are a list. The notebook currently records Hugo and Markdown. We want one list item for each tool, without writing a fixed number of HTML elements.

Add this block after the status block and before `.Content`:

```html
{{ with .Params.tools }}
  <p><strong>Tools:</strong></p>
  <ul>
    {{ range . }}
      <li>{{ . }}</li>
    {{ end }}
  </ul>
{{ end }}
```

Save and preview both project pages. The notebook should list Hugo and Markdown. The reading-list project should show whatever truthful list you retained in Chapter 9.

`range` repeats its block for the elements of a collection. Inside each repetition, the dot refers to that element. Here, the elements are tool names, so `{{ . }}` prints one name. [Hugo: range](https://gohugo.io/functions/go-template/range/)

There are two nested blocks to keep track of:

| Position | What `.` represents |
| --- | --- |
| Before `with .Params.tools` | The page |
| Inside `with`, before `range` | The tools list |
| Inside `range` | One tool name |
| After the inner `end` | The tools list again |
| After the outer `end` | The page again |

The outer `with` also prevents an empty Tools label and list when `tools: []` is stored. Indentation makes the two closing `end` actions easier to match with their opening blocks.

For a quick check, temporarily change the reading-list project's tools value to `tools: []`, preserving the rest of its front matter. The Tools label and list should disappear. Restore the original list afterwards, so this experiment leaves no content change.

These blocks also work on any other page that deliberately supplies the same parameters. We are using them for projects because that is the content family with this agreed model.

## 10.5 Generate the Projects list from its pages

We can use `range` for a collection of pages as well as a collection of tool names. Each element will then provide a title, description, and URL.

In `layouts/all.html`, insert the following block **after** `{{ .Content }}` and **before** `</article>`:

```html
{{ if and .IsSection (eq .Section "projects") }}
  <h2>Current work</h2>
  <ul>
    {{ range .RegularPages.ByTitle }}
      <li>
        <a href="{{ .RelPermalink }}">{{ .Title }}</a>
        {{ with .Description }}
          <p>{{ . }}</p>
        {{ end }}
      </li>
    {{ else }}
      <li>No projects to display yet.</li>
    {{ end }}
  </ul>
{{ end }}
```

For the moment, Projects may display both the old manual list and the new automatic one. That is an expected intermediate result. We will remove the old list after checking the new one.

### Limit the change to the intended section

The first line combines two checks:

- `.IsSection` asks whether this is a section page.
- `eq .Section "projects"` asks whether its top-level section is `projects`.

`eq` means equal, and `and` requires both checks to be true. The parentheses group the equality check. This is template syntax, so we do not replace these words with operators from another language.

In our shallow structure, the condition selects the Projects landing page. The notebook page belongs to Projects but is not itself a section page, so it does not receive the automatic project list. Articles is a section page, but its section name differs. [Hugo: IsSection](https://gohugo.io/methods/page/issection/), [Hugo: Section](https://gohugo.io/methods/page/section/)

If you later introduce nested project sections, revisit this condition: those sections can satisfy it too. We are solving the structure currently in the book.

### Choose and order the collection

On this section page, `.RegularPages` supplies the regular pages directly in the section. It does not recursively collect pages inside further subsections. `.ByTitle` sorts the resulting collection by title in ascending order. [Hugo: RegularPages](https://gohugo.io/methods/page/regularpages/), [Hugo: ByTitle](https://gohugo.io/methods/pages/bytitle/)

With the supplied titles, the notebook comes before the reading list. The filesystem's folder order does not control this list.

Inside `range`, the dot is now one project page. That is why `.Title` names the project rather than repeating the landing page's title, Projects.

The inner `with .Description` temporarily changes the dot to that project's description text. When its `end` is reached, the project page becomes current again. The outer `range` then moves on to the next project.

`else` handles an empty collection. In that case, it produces the explanatory list item instead of project entries. We will test this briefly before the final checkpoint.

### Let Hugo supply the page URL

`.RelPermalink` provides the current project's relative permalink, including the configured base path. For the reading-list project, our published site uses a path like:

```text
/my-knowledge-site/projects/reading-list/
```

We do not assemble that URL from the title or manually prepend the repository name. Use the returned value directly in `href`; it already represents the page's location. [Hugo: RelPermalink](https://gohugo.io/methods/page/relpermalink/)

## 10.6 Remove the duplicate list and verify the result

Open `content/projects/_index.md`. Keep the front matter and introduction. Remove the old `## Current work` heading and its two manually written project bullets. For the supplied example, the complete file becomes:

```markdown
---
title: "Projects"
draft: false
---

Small projects I am developing, with notes about their purpose and progress.
```

Retain your personalised introduction if you wrote one. Do not remove the Markdown file: its title and introductory content still belong to the section page.

Save and refresh Projects. You should now see one Current work heading and one list. Its descriptions come from the project pages' front matter, so the notebook's wording may differ from the former hand-written bullet.

Follow both links and return through Back to Projects. Check About, Articles, and Resources as well. The new list should not appear there, and their existing content should remain intact.

### Check that the list responds to content

Temporarily change the reading-list project's description by adding a short phrase. Save and inspect both the project page and the Projects list. Both should reflect the edit. Restore the original description afterwards.

Next, stop the preview and temporarily set both projects to `draft: true`. Start a normal `hugo server` without `-D`, and refresh the **Projects landing page**. The generated list should show its empty message. Stop the server, restore both draft values to `false`, and restart normally. Both entries should return.

Check the newly rendered landing-page list during this experiment. As Chapter 9 explained, old generated project files can remain, so directly opening an old project URL is not a reliable draft-exclusion test.

Use an ordinary preview for the final review. A preview started with `-D` intentionally includes draft projects in the generated list.

> **Second checkpoint:** Projects draws its titles, descriptions, and links from the project pages, and its list changes when the included content changes.

## 10.7 Diagnose a context mistake

Stop the server. In the first description block, near the top of the article, temporarily change:

```html
{{ with .Description }}
  <p>{{ . }}</p>
{{ end }}
```

to:

```html
{{ with .Description }}
  <p>{{ .Title }}</p>
{{ end }}
```

Run:

```text
hugo --minify --panicOnWarning
```

The build should fail when rendering a page with a description. The error should point into the template and indicate that `Title` cannot be evaluated on the current text value. Exact wording and the page reported first may vary.

The project still has a title. The problem is where we asked for it. Inside `with .Description`, the dot is description text, not the project page.

Restore `{{ . }}` in that paragraph and build again. This is a small source repair; replacing the whole layout would discard working changes unnecessarily.

When reading a template error, ask three questions:

1. Which file and expression does Hugo identify?
2. What does the dot represent at that location?
3. Does the requested value belong to that context?

For an unmatched-block error, also pair each `if`, `with`, and `range` with its own `end`. The reported location can be after the original mistake, especially when a closing action is missing.

Hugo normally escapes ordinary text values appropriately when inserting them into HTML. Do not add `safeHTML` as a general repair for an error or unexpected output. Our descriptions are plain text; the existing `.Content` value is the rendered Markdown body. These are different kinds of input.

## 10.8 Make one small template change yourself

Add a status paragraph to each project entry in the automatic list, after its description. It should display that project's recorded status and omit the entire paragraph when the value is absent.

Use the status block from Section 10.3 as a starting point. Place it inside the page `range`, after the description's `end`. Before typing, predict what the dot represents there and why `.Params.status` should work.

Build and preview. Confirm that the notebook entry reports `in-progress` and the reading-list entry reports `planned`. A repeated Projects title, a missing label, or a context error means you should inspect placement before changing the content files.

This variation leaves the content model unchanged. You are choosing another place to display information already stored once in each project page.

### Optional: ask an agent to explain your result

Use Chapter 8's read-only approach and ask:

```text
Read AGENTS.md, layouts/all.html, content/projects/_index.md,
and the two project index.md files beneath content/projects/.
Do not edit files or run commands that modify the project.

Explain how the automatic Projects list works. Identify the condition
that selects its landing page, the collection and sort order, the source
of each link, and what the dot represents inside range and with.

Check for duplicate manual links and context mistakes. Cite the relevant
expressions. Do not claim that browser checks or a build were performed
unless you actually performed them with permission.
```

Compare the explanation with your own reading. The agent should be able to trace the values, rather than merely say that the template looks correct.

### Save the checkpoint

Run:

```text
hugo --minify --panicOnWarning
git status
git diff
```

The intended persistent changes are `layouts/all.html` and `content/projects/_index.md`. The temporary description, tools, and draft experiments should leave no changes in the individual project files.

Inspect the diff, then stage and review those two paths:

```text
git add layouts/all.html content/projects/_index.md
git diff --cached
```

When the staged changes match the reviewed result, commit:

```text
git commit -m "Display project metadata and generate the Projects list"
git status
```

Keep this checkpoint locally or publish it through Chapter 7's reviewed push-and-check workflow.

## Completion check

- [ ] I can connect the displayed description, status, and tools to their source values.
- [ ] Missing optional values do not leave empty labels or lists.
- [ ] I can explain how `if`, `with`, and `range` differ.
- [ ] I can identify the current context inside each nested block.
- [ ] Projects has one automatic list with working links and the intended order.
- [ ] I checked the empty collection and restored both projects to normal builds.
- [ ] I repaired the deliberate context error and added status to the list entries.
- [ ] I committed only the two intended source files.

Chapter 11 will organise this growing layout into reusable pieces. The expressions and context rules will remain the same; we will change how the templates are arranged so shared page structure is easier to maintain.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| A field prints nothing. | Check the source key, spelling, and current context. |
| A field error mentions a string. | Look for a surrounding `with` or `range` that changed the dot to text. |
| Hugo reports an unexpected end of the template. | Match every opening block with an `end`; use indentation to reveal nesting. |
| The Projects heading or links appear twice. | Remove the old heading and manual bullets from the section's Markdown body. |
| The list appears on individual projects. | Restore the `.IsSection` check around the list. |
| The list is empty unexpectedly. | Check project draft values, their `index.md` paths, and whether they are directly in this section. |
| A list link omits the project prefix. | Use `.RelPermalink` from the project page instead of building the URL manually. |
| Changing a Markdown description has no effect. | Edit the front matter `description` field used by the template, save, and check the build output. |
| An experiment has left unexpected Git changes. | Inspect those exact files and restore the temporary values before staging. |

## Article block for comparison

This is the core result before the independent status-in-the-list variation. Use it to compare the `article` element inside `layouts/all.html`. Keep the rest of your layout, including the navigation, skip link, stylesheet reference, and footer.

```html
<article>
  <h1>{{ .Title }}</h1>

  {{ with .Description }}
    <p>{{ . }}</p>
  {{ end }}

  {{ with .Params.status }}
    <p><strong>Status:</strong> {{ . }}</p>
  {{ end }}

  {{ with .Params.tools }}
    <p><strong>Tools:</strong></p>
    <ul>
      {{ range . }}
        <li>{{ . }}</li>
      {{ end }}
    </ul>
  {{ end }}

  {{ .Content }}

  {{ if and .IsSection (eq .Section "projects") }}
    <h2>Current work</h2>
    <ul>
      {{ range .RegularPages.ByTitle }}
        <li>
          <a href="{{ .RelPermalink }}">{{ .Title }}</a>
          {{ with .Description }}
            <p>{{ . }}</p>
          {{ end }}
        </li>
      {{ else }}
        <li>No projects to display yet.</li>
      {{ end }}
    </ul>
  {{ end }}
</article>
```

---

## Editorial note for the author (remove before publication)

This chapter introduces a small working subset of Go templates: value output, conditions, `with`, `range`, context, one existing pipe, page collections, and page URLs. Keep variables, partials, base templates, more elaborate lookups, and data transformations out of this exercise. Chapter 11 should start from the two-file checkpoint and retain the independent addition of status to each list entry.

The Projects condition is deliberately tied to the current shallow content structure. The list is based on direct regular children rather than a recursive or site-wide collection. Description output is a visible paragraph; this chapter does not add an HTML meta description. The existing shared layout continues to serve all authored pages.

Official Hugo documentation was consulted on 17 September 2026. Examples were checked with Hugo 0.150.0 on Linux in a focused fixture containing the two Chapter 9 projects and the complete Chapter 4 shared layout. Unrelated destination pages retained placeholder bodies; this was not a full replay of the earlier chapters.

The successive edits produced the supplied comparison block. Checks covered optional descriptions and parameters, an empty tools list, project ordering, links at both a domain root and the GitHub project prefix, list placement, propagation of description edits, HTML escaping of description text, empty and draft-inclusive collections, the deliberate context error and its repair, and the independent status addition. The completed exercise produced a clean Git checkpoint with only the two intended files changed.

These were command-line build and generated-HTML checks. Visual browser review, a representative beginner trial, and an external deployment were not performed. The optional agent request is an authored exercise, not a recorded transcript.
