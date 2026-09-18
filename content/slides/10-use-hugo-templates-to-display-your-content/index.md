---
title: "Use Hugo Templates to Display Your Content"
description: "Chapter 10: expressions, conditions, and a loop that turns pages into a useful list."
book_number: "10"
weight: 11
---

# Use Hugo Templates to Display Your Content

Static Site Generators in the Age of AI

**Chapter 10**

Polla Fattah

---

## Today's goal

Your projects store a description, a status, and tools, but visitors **cannot see them**. And you still keep the Projects list **by hand**.

1. Display a **description**
2. Show **status** and **tools** when they exist
3. Let Hugo **generate** the Projects list

Change a description once; it updates everywhere Hugo uses it.

---

## By the end of today you can

- **Read** simple template expressions and trace them to content files
- **Use** `if` and `with` to show information only when it exists
- **Use** `range` to display a list, while tracking what the dot means
- **Build** an automatic Projects list, and diagnose a template error

Start from Chapter 9: both projects `draft: false`, a **clean** tree.

---

## Display one value first

In `layouts/all.html`, inside `article`, insert the middle three lines:

```html
<article>
  <h1>{{ .Title }}</h1>
  {{ if .Description }}
    <p>{{ .Description }}</p>
  {{ end }}
  {{ .Content }}
</article>
```

Both projects now show it; About has none, so **no empty paragraph**.

---

## Read what you just wrote

- **If** this page has a non-empty description, put it in a paragraph
- `end` closes the block
- The `<p>` tags sit **inside** it, so nothing is left behind when it is missing
- One instruction serves every page: Hugo evaluates it **per page**

> Descriptions appear where they exist, and pages without them still render normally.

---

## Templates and HTML together

```html
<h1>{{ .Title }}</h1>
```

becomes, for the reading list:

```html
<h1>My website reading list</h1>
```

- Hugo uses **Go's template language**; no Go installation needed
- The browser receives finished HTML: no JavaScript involved
- A template change affects the **next build**

---

## Values in our layout

| Expression | At the page level, it means |
| --- | --- |
| `.Title` | The page's title |
| `.Description` | Its `description` from front matter |
| `.Content` | Its Markdown body, rendered as HTML |
| `.Params.status` | Its custom `status` parameter |

The dot is **the current context**: here, the page. Mind the capitals: `Title`, but `status`.

---

## Conditions and pipes

- `if .Description` **checks**; `{{ .Description }}` **prints**
- Empty text, an empty list, and `false` all count as **false**

```html
<a href="{{ "about/" | relURL }}">about this notebook</a>
```

- `"about/"` is a value, `relURL` a **function**
- The **pipe** `|` passes the left value to the right function
- The result includes `/my-knowledge-site/about/`: keep the input without a leading slash

---

## Use with for optional values

Replace the `if` block with:

```html
{{ with .Description }}
  <p>{{ . }}</p>
{{ end }}
```

- `with` enters the block only when the value is non-empty
- Inside, **the dot becomes the description text**, so print it with `{{ . }}`
- After `end`, the dot is the **page** again

---

## Show the status

After the description block, before `.Content`:

```html
{{ with .Params.status }}
  <p><strong>Status:</strong> {{ . }}</p>
{{ end }}
```

Before the block, the dot is the **page**; inside, the **status text**; after `end`, the page again.

---

## Present is not correct

- The notebook shows `Status: in-progress`; the reading list `Status: planned`
- Pages without a status show **nothing**, not an empty label
- The status block starts **after** the description's `end`, where the dot is the page

The condition proves a value **exists**. It does not prove it is one of our agreed values, or that it is **true**.

---

## Repeat markup with range

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

`range` repeats its block for each element; inside, the dot is **one element**. Try `tools: []`: the whole block vanishes. Restore it.

---

## Follow the dot

| Position | What `.` means |
| --- | --- |
| Before `with .Params.tools` | The page |
| Inside `with`, before `range` | The tools list |
| Inside `range` | One tool name |
| After the inner `end` | The tools list again |
| After the outer `end` | The page again |

---

## Generate the Projects list

```html
{{ if and .IsSection (eq .Section "projects") }}
  <h2>Current work</h2>
  <ul>
    {{ range .RegularPages.ByTitle }}
      <li>...one project...</li>
    {{ else }}
      <li>No projects to display yet.</li>
    {{ end }}
  </ul>
{{ end }}
```

---

## Each project in the list

The block goes after `{{ .Content }}`. Inside its `range`, each project gets:

```html
<li>
  <a href="{{ .RelPermalink }}">{{ .Title }}</a>
  {{ with .Description }}
    <p>{{ . }}</p>
  {{ end }}
</li>
```

Inside `range`, the dot is **one project page**: so `.Title` is that project, not "Projects".

---

## Only on the Projects page

```html
{{ if and .IsSection (eq .Section "projects") }}
```

- `.IsSection`: is this a section page?
- `eq .Section "projects"`: is its section `projects`?
- `and`: both must be true; the parentheses group the `eq` check

A project page is not a section; Articles is a section with another name. Nested project sections later? **Revisit** this condition.

---

## Choose, order, and link

- `.RegularPages`: the pages **directly** in this section, not deeper
- `.ByTitle`: sorted by title, not by folder order
- `else`: what to show when the collection is **empty**
- `.RelPermalink`: the page's own address, **with** the project prefix

```text
/my-knowledge-site/projects/reading-list/
```

Never assemble a URL from the title or add the repository name by hand.

---

## Remove the duplicate list

Projects may now show **two** lists. In `content/projects/_index.md`, keep only:

```markdown
---
title: "Projects"
draft: false
---

Small projects I am developing, with notes about their purpose and progress.
```

One heading, one list, descriptions from the project pages. Check the list is **not** on About, Articles, or Resources.

---

## Make sure the list responds

1. Change the reading list's `description`: the page **and** the list change. Restore it
2. Set both projects to `draft: true`, run plain `hugo server`, and open **Projects**: "No projects to display yet." Restore both

Check the **landing page**, not old project URLs: old output can remain.

> Projects now draws its titles, descriptions, and links from the project pages.

---

## A context mistake, on purpose

Inside the description block, temporarily change `{{ . }}` to:

```html
{{ with .Description }}
  <p>{{ .Title }}</p>
{{ end }}
```

```text
hugo --minify --panicOnWarning
```

The build **fails**: `Title` cannot be read from **text**. The project has a title; you asked for it in the wrong place. Restore `{{ . }}`.

---

## Reading a template error

1. Which **file** and **expression** does Hugo name?
2. What does the **dot** represent there?
3. Does the requested value **belong** to that context?

- Unmatched block? Pair every `if`, `with`, and `range` with its own `end`
- The reported line can come **after** the real mistake
- Never add `safeHTML` as a general repair

---

## Try it yourself

Add each project's **status** to its entry in the automatic list:

- Start from the status block you wrote earlier
- Place it inside the `range`, after the description's `end`
- **Predict** what the dot means there before you type

Expect `in-progress` and `planned`. A repeated "Projects" or a context error? Check the **placement**, not the content.

---

## Optional: ask an agent to explain

Read-only, as in Chapter 8. Ask it to explain:

- The condition that selects the landing page
- The collection and its sort order
- The source of each link
- What the dot means inside `range` and `with`

It should **trace the values**, not just say the template looks correct. It must not claim builds or browser checks it did not run.

---

## Save the checkpoint

```text
hugo --minify --panicOnWarning
git status
git diff
git add layouts/all.html content/projects/_index.md
git diff --cached
git commit -m "Display project metadata and generate the Projects list"
```

Only these **two** files. The description, tools, and draft experiments must leave **no** change in the project pages.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| A field prints nothing | The key, its spelling, and the context |
| An error mentions a string | A `with` or `range` changed the dot to text |
| Unexpected end of template | Match every block with its `end` |
| The list appears twice | Remove the manual list from the Markdown |
| A list link lacks the prefix | Use `.RelPermalink` |

---

## Completion check

- I can trace description, status, and tools to their source values
- Missing values leave no empty labels or lists
- I can explain how `if`, `with`, and `range` differ
- I know what the dot means inside each nested block
- Projects has one automatic list with working links
- I tested the empty list and restored both projects
- I repaired the context error and added status to the list
- I committed only the two intended files

---

# Next: Build Reusable Hugo Layouts

Chapter 11: the same expressions, arranged into reusable pieces that are easier to maintain.

**polla.dev/ssg-book**
