---
title: "Build Reusable Hugo Layouts"
weight: 11
book_number: 11
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

Your shared layout now does several jobs. It creates the HTML document, displays navigation and a footer, presents page metadata, and generates the Projects list. It works, but finding the right place for the next change takes more care.

We will give those jobs clearer homes. A base template will hold the common document structure. Small partial templates will hold reusable pieces. A Projects section template will decide where the project list belongs.

Most of the website should look exactly as it did before. That is the first result to check: reorganising working code should preserve its behaviour. At the end, you will make one small change that belongs only to the Projects landing page.

## What you will be able to do

By the end, you should be able to:

- Move a working page component into a partial and pass it the context it needs.
- Connect a base template's named block with a matching definition.
- Give the Projects section its own layout while retaining shared page structure.
- Check that reorganising templates has preserved content, links, and metadata.

Start from the completed Chapter 10 checkpoint, including status labels in the automatic project list. (If you are following along in the companion repository `ssg-playground`, make sure you are on branch `chapter-10` or check out the completed chapter on branch `chapter-11`.) Both projects should have `draft: false`, and Git should report a clean working tree. Use the same Hugo installation and stylesheet.

This chapter uses the template paths introduced in Hugo 0.146.0, including `layouts/baseof.html` and `layouts/_partials/`. The examples are checked with Hugo 0.150.0. Older tutorials may show `_default` or an unprefixed `partials` directory; follow this book's paths consistently rather than combining arrangements. [Hugo: template-system changes](https://gohugo.io/templates/new-templatesystem-overview/)

## 11.1 Move one familiar component first

Before editing, run the normal preview and visit Home, Projects, and the notebook project. Notice the title, navigation, footer, project metadata, and list entries. These are your comparison points.

Stop the preview with **Ctrl+C**. Inside `layouts`, create a folder named `_partials`, including the leading underscore. Create `layouts/_partials/footer.html`.

Move the complete footer element from `layouts/all.html` into the new file. For the supplied project, it is:

```html
<footer>
  <p>Learn, review &amp; share.</p>
  <p class="footer-note">
    Read <a href="{{ "about/" | relURL }}">about this notebook</a>.
  </p>
</footer>
```

Retain your own accurate footer wording if you personalised it. The new file should contain the footer element, without a second HTML document around it.

In the old footer's position in `layouts/all.html`, put:

```html
{{ partial "footer.html" . }}
```

Save both files, then run:

```text
hugo --minify --panicOnWarning
hugo server
```

Visit the same three pages. The footer should still appear once on each page, with a working About link and the same styling. If you see two footers, the original element was copied but not removed from `all.html`.

A **partial** is a template you call to render a piece of a page. The filename in this call is relative to `layouts/_partials/`; do not write the full filesystem path there. The final dot passes the current context to the partial. [Hugo: partial inclusion](https://gohugo.io/functions/partials/include/)

Our footer currently uses fixed wording and `relURL`, so it does not need page-specific values. Passing the page explicitly keeps the calling pattern clear and allows later changes to use it.

> **First checkpoint:** the footer has its own source file, and the rendered pages still show the same single footer.

## 11.2 Give the remaining jobs clear locations

We will finish with these six template files:

| File | Responsibility |
| --- | --- |
| `layouts/baseof.html` | HTML document, head, navigation, main region, and footer call |
| `layouts/all.html` | General page content when no more specific layout applies |
| `layouts/projects/section.html` | Projects landing-page content and project-list call |
| `layouts/_partials/footer.html` | The complete footer element |
| `layouts/_partials/page-meta.html` | Optional description, status, and tools |
| `layouts/_partials/project-list.html` | The Current work heading and generated project list |

There are more files, but each has a named purpose. A future change to the project list will have an obvious starting point. A new page layout can share the document structure without copying the navigation and footer.

This is often called **refactoring**: changing code organisation while preserving intended behaviour. It does not mean that every paragraph or HTML element needs its own file. We will keep the header and navigation together in the base template for now.

The content files remain the source of titles, descriptions, project facts, and Markdown writing. Moving the templates does not require moving that content or changing its URLs.

## 11.3 Extract metadata and the project list

Stop the preview before this group of edits. We will save each connected set of changes before building again.

### Put page metadata in one partial

Create `layouts/_partials/page-meta.html` with the three blocks introduced in Chapter 10:

```html
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
```

In `layouts/all.html`, replace those three blocks between the `h1` and `.Content` with:

```html
{{ partial "page-meta.html" . }}
```

Leave the heading and `.Content` in place. This partial expects to receive a page, so its opening expressions can read `.Description` and `.Params`.

### Put the generated list in its own partial

Create `layouts/_partials/project-list.html`:

```html
<h2>Current work</h2>
<ul>
  {{ range .RegularPages.ByTitle }}
    <li>
      <a href="{{ .RelPermalink }}">{{ .Title }}</a>
      {{ with .Description }}
        <p>{{ . }}</p>
      {{ end }}
      {{ with .Params.status }}
        <p><strong>Status:</strong> {{ . }}</p>
      {{ end }}
    </li>
  {{ else }}
    <li>No projects to display yet.</li>
  {{ end }}
</ul>
```

This preserves the list-entry status from Chapter 10's independent exercise. It also keeps the title order, page-generated links, optional descriptions, and empty-list message.

In `all.html`, replace the existing Projects conditional and everything inside it with:

```html
{{ if and .IsSection (eq .Section "projects") }}
  {{ partial "project-list.html" . }}
{{ end }}
```

The condition still decides whether to show the list. The partial now handles how the list is rendered. Pass the **section page**, because the partial obtains its collection from `.RegularPages`.

Build and preview again. Check the project pages' metadata and the Projects list. The visible result should match Chapter 10.

### Context crosses the call explicitly

The dot inside a partial starts as the value passed to it. It does not automatically recover the outer page if the caller is currently inside a `with` or `range` block.

| Call location | Value passed by the final dot |
| --- | --- |
| At the outer level of a page layout | The page being rendered |
| Inside a range over project pages | One project page |
| Inside `with .Description` | Description text |

Call `page-meta.html` where the dot is a page. Passing description text would give it the wrong kind of input. This is the same context rule you practised in Chapter 10, now applied across files.

## 11.4 Separate the document from its main content

A **base template** contains the shared document structure. It provides a named place where the selected page layout supplies content.

Stop the preview. Copy your current `layouts/all.html` to a new file named `layouts/baseof.html`. In the new file, replace the entire `article` element inside `main` with:

```html
{{ block "main" . }}{{ end }}
```

Keep the surrounding `<main id="main" tabindex="-1">` element. The skip link still needs that target.

With the supplied header and footer call, the complete base template is:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ .Title }} | {{ .Site.Title }}</title>
  <link rel="stylesheet" href="{{ "css/site.css" | relURL }}">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header>
    <p class="site-name">{{ .Site.Title }}</p>
    <nav aria-label="Main navigation">
      <a href="{{ "" | relURL }}">Home</a>
      <a href="{{ "about/" | relURL }}">About</a>
      <a href="{{ "articles/" | relURL }}">Articles</a>
      <a href="{{ "projects/" | relURL }}">Projects</a>
      <a href="{{ "resources/" | relURL }}">Resources</a>
    </nav>
  </header>
  <main id="main" tabindex="-1">
    {{ block "main" . }}{{ end }}
  </main>
  {{ partial "footer.html" . }}
</body>
</html>
```

Retain any earlier deliberate header customisation in your copied file. The example shows the expected structure, not a reason to discard your own wording.

Now replace `layouts/all.html` with this smaller template:

```html
{{ define "main" }}
  <article>
    <h1>{{ .Title }}</h1>
    {{ partial "page-meta.html" . }}
    {{ .Content }}
    {{ if and .IsSection (eq .Section "projects") }}
      {{ partial "project-list.html" . }}
    {{ end }}
  </article>
{{ end }}
```

Save both files before building. The base contains the document; `all.html` supplies the main content. Do not leave another `html`, `head`, or `body` element in `all.html`.

### Match `block` with `define`

`block "main" .` marks the place in the base where the main content will be rendered and passes the page context. `define "main"` supplies the corresponding content in the selected layout. The names must match exactly. [Hugo: block](https://gohugo.io/functions/go-template/block/), [Hugo: define](https://gohugo.io/functions/go-template/define/)

The block name `"main"` and the HTML element `<main>` happen to share a word, but they have different roles. One is a template name; the other gives the browser a document landmark. We retain both.

For Hugo to apply the base, the selected content template must contain definitions without ordinary output outside them. Keep the complete `article` inside `define`. An HTML comment or stray element outside the definition can prevent the base from being applied. [Hugo: base templates](https://gohugo.io/templates/types/#base)

Build and preview Home, Projects, and the notebook project again. Confirm that the navigation, metadata, list, stylesheet, and footer remain present. You have now separated the document structure from the content area without changing what the visitor needs to see.

## 11.5 Give Projects its own section template

The general content layout still contains a Projects-specific condition. We can now move that decision into Hugo's template selection.

Create a `projects` folder inside `layouts`, then create `layouts/projects/section.html`:

```html
{{ define "main" }}
  <article>
    <h1>{{ .Title }}</h1>
    {{ partial "page-meta.html" . }}
    {{ .Content }}
    {{ partial "project-list.html" . }}
  </article>
{{ end }}
```

Then remove the entire Projects conditional from `layouts/all.html`. Its complete final content becomes:

```html
{{ define "main" }}
  <article>
    <h1>{{ .Title }}</h1>
    {{ partial "page-meta.html" . }}
    {{ .Content }}
  </article>
{{ end }}
```

Save both before rebuilding. The general layout no longer needs to ask whether it is rendering Projects. The specialised section layout makes the list call.

For our current project, the important selections are:

| Page being rendered | Content template selected |
| --- | --- |
| Projects landing page | `layouts/projects/section.html` |
| Notebook project | `layouts/all.html` |
| Reading-list project | `layouts/all.html` |
| Home, About, Articles, and Resources | `layouts/all.html` |

Both content templates use the same `baseof.html`. A project detail page does not become a section page merely because it lives under Projects. Likewise, the name `section.html` is a template filename; it does not replace the content file `content/projects/_index.md`.

Hugo's template selection considers page kind and location among other factors. We only need the matching Projects section template and the general `all.html` fallback here. Additional languages, output formats, custom layout names, and nested sections can introduce more candidates. [Hugo: template paths and selection](https://gohugo.io/templates/new-templatesystem-overview/)

There is a little shared article markup in the two content templates. That is acceptable at this scale. The document, metadata, footer, and list logic each have a clear home; we do not need another layer solely to avoid repeating a few simple lines.

### Follow one rendered page through the files

For Projects, Hugo selects `projects/section.html` and combines its `main` definition with the base. That definition calls the metadata and project-list partials. The base also calls the footer partial.

For the notebook project, Hugo selects `all.html`. It uses the same base and metadata partial, but makes no project-list call. The notebook's Markdown body supplies its own headings and links as before.

Build and preview those two pages side by side. Projects should have one generated list; the notebook should have its own metadata and body without a second list of all projects.

> **Second checkpoint:** Projects has a dedicated layout, while its navigation, document structure, and footer remain shared with the rest of the site.

## 11.6 Check a failure that a successful build can miss

Stop the preview. In `layouts/all.html` only, temporarily change the first line to:

```html
{{ define "body-content" }}
```

Leave the matching `end` in place. Build:

```text
hugo --minify --panicOnWarning
```

The build can succeed. The definition is valid template syntax, but its name no longer matches the base's `main` block.

Start the preview and open About or the notebook project. You should see the shared navigation and footer, but the main article is missing. Projects should still work because its separate template continues to define `main` correctly.

This is a useful diagnostic distinction. When shared navigation appears but page content disappears, inspect the base's block name and the selected content template's definition before changing Markdown files.

Stop the server and restore:

```html
{{ define "main" }}
```

Build and preview the affected pages again. Verify that their title and content return.

A missing partial file causes a different kind of problem: Hugo normally reports that it cannot find the named partial. Compare the call's filename with the file under `_partials`. Use exact spelling and capitalisation, because a mismatch that goes unnoticed on one filesystem can fail on another.

Keep the scope of a repair small. The deliberately changed definition needs one corrected name, not replacement of the entire template set.

## 11.7 Make one change in the right place

Add a brief sentence immediately before the project list on the Projects landing page. For example:

```html
<p>Choose a project to see its purpose, progress, and next step.</p>
```

Decide where it belongs before editing. It is introductory text for this landing-page layout, so put it in `layouts/projects/section.html`, after `.Content` and before the project-list partial call.

Preview Projects, then the notebook project and About. The sentence should appear only on Projects. If it appears everywhere, you probably added it to the base or a shared component.

For longer editorial introductions, continue using `content/projects/_index.md`. This short exercise demonstrates layout scope; it does not mean that normal page writing should migrate into templates.

### Keep the agent's file map accurate

Chapter 8's `AGENTS.md` says the shared layout is `layouts/all.html`. That description is now incomplete. Replace that one entry under Files with:

```markdown
- Shared HTML structure is in layouts/baseof.html.
- General page content is in layouts/all.html.
- The Projects landing-page template is layouts/projects/section.html.
- Reusable components are in layouts/_partials/.
```

Retain the other file entries and working agreements. An instruction file is useful only when it describes the current project accurately.

If you ask an agent for a later edit, name the intended layer. “Change the introduction on Projects” is clearer when you also say whether you mean the Markdown introduction or the small layout-specific sentence. Require it to inspect the current files before proposing a move.

## 11.8 Review the whole result and save

A shared-template edit can affect many pages, so review representative pages from both selected layouts. Use a normal preview without draft inclusion.

| Check | What should remain true |
| --- | --- |
| Home and About | Their title, content, navigation, and footer remain present |
| Articles and the first learning note | The existing manual article link and body still work |
| Notebook and reading-list projects | Description, status, tools, and Markdown body remain correct |
| Projects | One generated list retains its order, descriptions, statuses, and links |
| Resources | Its earlier writing and links remain available |
| Skip link | It still targets the single `main` element with `id="main"` |
| Stylesheet and footer link | Their URLs retain the configured project prefix |

The new Projects sentence is the one intentional visible addition. The rest of this chapter has mainly changed where the rendering instructions live.

Stop the preview, build, and inspect Git:

```text
hugo --minify --panicOnWarning
git status
git diff
```

Expect one modified existing template, five new template files, and the updated `AGENTS.md`. Content and CSS should have no changes from this chapter's required steps. Use status to notice the new files; they are not shown by the ordinary unstaged diff until tracked.

Stage the intended paths with these commands:

```text
git add layouts/all.html layouts/baseof.html layouts/projects/section.html
git add layouts/_partials/footer.html layouts/_partials/page-meta.html layouts/_partials/project-list.html
git add AGENTS.md
git diff --cached
```

Read the staged changes. Much of the new-file text should be familiar code moved from `all.html`. Confirm that the status block in each project-list entry survived the move, and that no temporary incorrect block name remains.

When the result matches your review, commit:

```text
git commit -m "Organise Hugo layouts into a base, section template, and partials"
git status
```

A clean local checkpoint is enough to continue. Publish through Chapter 7's workflow when you are ready to push the reviewed result.

## Completion check

- [ ] I can locate the base, general content template, Projects template, and three partials.
- [ ] Each partial is called with the kind of context it expects.
- [ ] Both selected content templates define the base's `main` block.
- [ ] Projects uses its own template while project detail pages use the general fallback.
- [ ] The metadata, project-list statuses, navigation, and footer survived the moves.
- [ ] I diagnosed and repaired the deliberately mismatched definition.
- [ ] My independent sentence appears only on Projects.
- [ ] I updated the agent file map and committed the seven intended files.

Chapter 12 will use structured data to build a small resource directory. These shorter templates will give us a clear place to render that data without adding every new responsibility to one large file.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| Hugo cannot find a partial. | Check the filename, its location under `layouts/_partials/`, and the name used in the call. |
| A partial reports a field error. | Check what context its caller passes; page metadata needs a page, and the project list needs its section page. |
| The footer appears twice. | Keep one footer element inside the partial and one call from the base. |
| Navigation or styling disappears after the split. | Check whether the content template has ordinary output outside `define`, preventing the base from being applied. |
| The shared frame appears but the article is missing. | Match the `block` and `define` names exactly. |
| Projects loses its list. | Check the path `layouts/projects/section.html` and its project-list call. |
| Every project page shows the project list. | Keep the call in the section template, not the general content template. |
| A layout edit seems to have no effect. | Identify which template the affected page actually selects; Projects now has a specific one. |
| An agent edits the old location. | Check the updated file map and name the intended file in the task. |

