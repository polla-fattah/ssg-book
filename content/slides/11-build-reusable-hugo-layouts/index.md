---
title: "Build Reusable Hugo Layouts"
description: "Chapter 11: a base template, partials, and a section template, with the site looking the same."
book_number: "11"
weight: 12
---

# Build Reusable Hugo Layouts

Static Site Generators in the Age of AI

**Chapter 11**

Polla Fattah

---

## Today's goal

One layout now does everything. It works, but every change needs care.

- A **base template** for the shared document
- Small **partials** for reusable pieces
- A **section template** for Projects

> Reorganising working code should **preserve** its behaviour. Check that first.

---

## By the end of today you can

- **Move** a component into a partial and pass it the context it needs
- **Connect** a base template's named block with its definition
- **Give** Projects its own layout, sharing the rest
- **Check** that content, links, and metadata survived the move

Start from Chapter 10, with status in the project list, and a **clean** tree (companion branch `chapter-10`).

---

## Before you change anything

Run the preview and visit **Home**, **Projects**, and the **notebook project**. Note the title, navigation, footer, metadata, and list entries: these are your **comparison points**.

We use the template paths from Hugo **0.146.0** onwards:

- `layouts/baseof.html`
- `layouts/_partials/`

Older tutorials show `_default` or `partials`. **Do not mix** the two arrangements.

---

## Move the footer into a partial

Stop the preview. Create `layouts/_partials/footer.html`, and **move** the whole footer into it:

```html
<footer>
  <p>Learn, review &amp; share.</p>
  <p class="footer-note">
    Read <a href="{{ "about/" | relURL }}">about this notebook</a>.
  </p>
</footer>
```

---

## What a partial call means

In the footer's old place in `layouts/all.html`, put:

```html
{{ partial "footer.html" . }}
```

- A **partial** renders one piece of a page
- The name is relative to `layouts/_partials/`: no full path
- The final **dot** passes the current context to the partial

Build, then check the three pages: **one** footer on each, with a working About link. Two footers? You copied instead of moving.

---

## Six files, six jobs

- `layouts/baseof.html`: the document, with head, navigation, `main`, and footer call
- `layouts/all.html`: general page content
- `layouts/projects/section.html`: the Projects landing page
- `layouts/_partials/footer.html`: the footer
- `layouts/_partials/page-meta.html`: description, status, and tools
- `layouts/_partials/project-list.html`: the generated project list

---

## Refactoring

**Refactoring** changes how code is organised while keeping what it does.

- More files, but each has a **named purpose**
- The next change to the project list has an obvious starting point
- A new layout shares the document without copying navigation and footer
- Not every element needs its own file: header and navigation stay together

Content files do not move, and URLs do not change.

---

## Page metadata in one partial

Create `layouts/_partials/page-meta.html` with Chapter 10's three blocks: description, status, and tools.

In `layouts/all.html`, replace those three blocks, between the `h1` and `.Content`, with:

```html
{{ partial "page-meta.html" . }}
```

This partial expects a **page**, so `.Description` and `.Params` still work inside it.

---

## The project list in its own partial

`layouts/_partials/project-list.html` holds the heading and the `range`:

```html
<h2>Current work</h2>
<ul>
  {{ range .RegularPages.ByTitle }}
    <li>...link, description, and status...</li>
  {{ end }}
</ul>
```

The chapter gives the complete file, with its `else` message. **Keep** each entry's status.

---

## The condition stays behind

In `all.html`, the Projects block becomes:

```html
{{ if and .IsSection (eq .Section "projects") }}
  {{ partial "project-list.html" . }}
{{ end }}
```

- The **condition** decides whether to show the list
- The **partial** decides how the list looks
- Pass the **section page**: the partial reads its `.RegularPages`

---

## Context crosses the call explicitly

| Where the call is | What the final dot passes |
| --- | --- |
| At the outer level of a layout | The page being rendered |
| Inside a `range` over projects | One project page |
| Inside `with .Description` | The description text |

The dot inside a partial starts as **whatever you pass**. It does not recover the outer page by itself.

Call `page-meta.html` only where the dot is a **page**.

---

## A base template

Copy `layouts/all.html` to `layouts/baseof.html`. In the copy, replace the whole `article` with a named **block**:

```html
<main id="main" tabindex="-1">
  {{ block "main" . }}{{ end }}
</main>
{{ partial "footer.html" . }}
```

Keep the `main` element: the skip link targets it. Above it, the head, skip link, header, and navigation stay as they were.

---

## Replace all.html with this

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

---

## Match block with define

- `block "main" .` marks **where** the content goes, and passes the page
- `define "main"` supplies **what** goes there
- The names must match **exactly**
- `"main"` the block and `<main>` the element only share a word

Nothing may sit **outside** `define`, and no `html`, `head`, or `body` remains in `all.html`: even a stray comment can stop the base from being applied.

Build, and check Home, Projects, and the notebook project again.

---

## Give Projects its own template

Create `projects/section.html`; drop the condition from `all.html`:

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

---

## Which template renders which page

| Page | Content template |
| --- | --- |
| Projects landing page | `layouts/projects/section.html` |
| Notebook and reading-list projects | `layouts/all.html` |
| Home, About, Articles, Resources | `layouts/all.html` |

- **Both** use the same `baseof.html`
- A project page is **not** a section page just because it lives under Projects
- `section.html` is a template, not a content file

---

## Follow one page through the files

**Projects**: Hugo selects `projects/section.html`, fills the base's `main` block with it, and calls the metadata and project-list partials. The base calls the footer.

**The notebook project**: Hugo selects `all.html`. Same base, same metadata partial, **no** project list.

> Projects has its own layout; navigation, document, and footer stay shared.

---

## A failure the build misses

In `layouts/all.html` only, change the first line to:

```html
{{ define "body-content" }}
```

- `hugo --minify --panicOnWarning` **succeeds**
- About and the notebook show navigation and footer, but **no article**
- Projects still works: its own template defines `main`

Restore `{{ define "main" }}`, and check the pages again.

---

## Reading this kind of failure

- Frame present, content missing? Compare the base's **block** name with the page's **define**
- A missing partial is different: Hugo reports it **cannot find** the file
- Match filenames **exactly**, including capitals: another system may be stricter

Repair one wrong name; do not replace the whole template set.

---

## One change, in the right place

Add a sentence to the Projects landing page, just before the list:

```html
<p>Choose a project to see its purpose, progress, and next step.</p>
```

It belongs in `layouts/projects/section.html`, after `.Content` and before the list call.

- It should appear **only** on Projects
- Everywhere? You added it to the base or a shared partial
- Longer introductions stay in `content/projects/_index.md`

---

## Keep the agent's map accurate

`AGENTS.md` still says the layout is `layouts/all.html`. Replace that entry:

```markdown
- Shared HTML structure is in layouts/baseof.html.
- General page content is in layouts/all.html.
- The Projects landing-page template is layouts/projects/section.html.
- Reusable components are in layouts/_partials/.
```

An instruction file helps only while it is **true**. When you ask for an edit, name the **layer** you mean.

---

## Review the whole result

| Check | What should remain true |
| --- | --- |
| Home, About, Resources | Title, content, navigation, footer |
| The first learning note | Its body and links |
| Both projects | Description, status, tools, body |
| Projects | One list: order, descriptions, statuses, links |
| Skip link and stylesheet | `#main` target; project prefix in URLs |

The Projects sentence is the **only** intentional visible change.

---

## Save the checkpoint

```text
git add layouts/all.html layouts/baseof.html layouts/projects/section.html
git add layouts/_partials/footer.html layouts/_partials/page-meta.html
git add layouts/_partials/project-list.html AGENTS.md
git diff --cached
git commit -m "Organise Hugo layouts into a base, section template, and partials"
```

Seven files: one modified template, five new ones, and `AGENTS.md`. No content or CSS changes. Check `git status` for the new files first.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| Hugo cannot find a partial | Its name, and that it is in `layouts/_partials/` |
| A partial reports a field error | What context its caller passes |
| The footer appears twice | One footer in the partial, one call in the base |
| Navigation or styling vanished | Output outside `define` |
| Every project shows the list | Keep the call in the section template |

---

## Completion check

- I can find the base, the two content templates, and the three partials
- Each partial receives the context it expects
- Both content templates define the base's `main` block
- Projects uses its own template; project pages use the fallback
- Metadata, statuses, navigation, and footer survived the moves
- I repaired the mismatched definition
- My sentence appears only on Projects
- I updated `AGENTS.md` and committed the seven files

---

# Next: Build a Resource Directory with JSON

Chapter 12: structured data, rendered by these shorter templates.

**polla.dev/ssg-book**
