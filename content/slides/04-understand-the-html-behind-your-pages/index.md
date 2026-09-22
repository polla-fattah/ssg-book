---
title: "Understand the HTML Behind Your Pages"
description: "Chapter 4: what the browser actually receives, and how it connects to what you wrote."
book_number: "4"
weight: 5
---

# Understand the HTML Behind Your Pages

Static Site Generators in the Age of AI

**Chapter 4**

Polla Fattah

---

## Today's goal

See what the browser **receives** when it shows your pages.

- The title is not just large text; the navigation is not just coloured words
- Both have a **structure** the browser interprets

That lets you make deliberate changes, diagnose mistakes, and judge code an **AI agent** suggests.

---

## By the end of today you can

- **Inspect** a page and recognise its main elements and attributes
- **Distinguish** Markdown, templates, generated HTML, and the live document
- **Make and verify** a small lasting change to the shared layout
- **Check** headings, links, images, and the skip link

No HTML reference to memorise, and no JavaScript.

---

## Inspect the article

Start `hugo server` in your Chapter 3 project (or checkout companion branch `chapter-03` in `ssg-playground`) and open:

```text
http://localhost:1313/articles/first-learning-note/
```

Right-click the main heading and choose **Inspect** or press **F12** (**Ctrl + Shift + I** / **Cmd + Option + I**). Look for **Elements** (Chrome, Edge) or **Inspector** (Firefox):

```html
<h1>My first learning note</h1>
```

Then find the first paragraph's `p`, and What I tried's `h2`.

---

## Change it in the browser only

1. In the panel, double-click the `h1` text
2. Type `A temporary browser edit` and press Enter
3. **Reload** without saving any file: the original returns

The inspector edits the browser's **current document**, not your files.

> Try ideas in the browser; make lasting changes in the source.

---

## The pieces of an element

```html
<a href="https://gohugo.io/documentation/">Hugo documentation</a>
```

| Piece | What it means |
| --- | --- |
| `<a ...>` | The opening tag of a link |
| `href="..."` | An **attribute**: the destination |
| `Hugo documentation` | The visible link text |
| `</a>` | The closing tag |

---

## Nesting and void elements

Close inner elements **before** the ones around them:

```html
<p>Please <strong>check the link</strong> before publishing.</p>
```

- Straight quotes around attribute values, spaces between attributes
- Indentation helps reading; **the markup** creates the structure
- `img`, `meta`, and `link` are **void elements**: never write `</img>`

A working address with a misleading label is still a poor link.

---

## Make one lasting change

In `layouts/all.html`, replace **only** the footer element:

```html
<footer>
  <p>Learn, review &amp; share.</p>
  <p class="footer-note">
    Read <a href="{{ "about/" | relURL }}">about this notebook</a>.
  </p>
</footer>
```

Save, check the home page and the article, then **reload**: the change stays.

---

## What is in that footer

- **Nesting**: the link sits in a paragraph, inside `footer`
- `&amp;` shows an `&`; `&lt;` and `&gt;` show `<` and `>`
- `footer-note` is a **class**: a label with no style yet, used in Chapter 5
- `{{ ... }}` is processed by **Hugo**, before the browser sees it

```html
<a href="/about/">about this notebook</a>
```

That is what the browser actually receives.

---

## From content to browser

| Form | Where you see it |
| --- | --- |
| Content source | `content/articles/first-learning-note/index.md` |
| Layout source | `layouts/all.html`, with `{{ .Title }}` and `{{ .Content }}` |
| Generated HTML | **View Page Source**, or files made by a build |
| Live document | **Elements** or **Inspector**, including your edits |

The live document is the **DOM**: Document Object Model.

---

## Edit the source, not the output

- Never edit a generated `public/.../index.html`: the next build overwrites it
- View Page Source shows the **response**; the inspector shows the **live** tree
- You may see extra code Hugo adds for live reload

If the page literally shows `{{ .Title }}`, you opened the layout file itself. Open the **Hugo preview address** instead.

---

## The document's head

| Part | Its job |
| --- | --- |
| `<!doctype html>` | Modern HTML parsing |
| `<html lang="en">` | The document, in English |
| `<meta charset="utf-8">` | The character encoding |
| `<title>` | The text in the browser tab |
| Stylesheet `<link>` | Which CSS file to load |

`head` holds information **about** the page; `header` is visible content **inside** it.

---

## Semantic elements in the body

| Element | Meaning here |
| --- | --- |
| `header` | Site name and navigation |
| `nav` | Major navigation links |
| `main` | This page's primary content |
| `article` | The self-contained piece of writing |
| `footer` | Closing site information |

Their names say their **purpose**, not their look.

---

## Markdown becomes HTML

| Markdown | HTML |
| --- | --- |
| Front matter `title` | `h1`, from the layout |
| `## What I tried` | `h2` |
| `**important**` and `*emphasis*` | `strong` and `em` |
| Bulleted and numbered lists | `ul` or `ol`, with `li` items |
| A link and an image | `a` with `href`; `img` with `src` and `alt` |

Inspect three of these in your own article.

---

## Heading levels are structure

- One `h1` per page, from the layout; `h2` for sections, `h3` inside them
- A bold paragraph **looks** like a heading but **is not** one
- An `h2` used just for big text gives a **misleading** outline

Screen-reader users jump between headings, so the difference matters.

Two big titles? You probably wrote `# My first learning note` in the body as well. **Remove it**; do not hide it with CSS.

---

## Images: src and alt

```html
<img src="notebook-preview.png"
     alt="The notebook home page showing its introduction">
```

- `src` is the resource; `alt` is its **text alternative**
- The italic caption from Chapter 2 is separate from `alt`
- A purely decorative image can have `alt=""`
- A **missing** `alt` is not the same as an empty one

---

## id and class

| | `id` | `class` |
| --- | --- | --- |
| How many per page | **One** element | Many elements |
| What uses it | Fragments such as `#main` | CSS and scripts |
| Example here | `id="main"` | `site-name`, `footer-note` |

Neither creates styling by itself.

Keep `aria-label="Main navigation"` and `tabindex="-1"` on `main`: the skip link relies on them.

---

## The skip link

```html
<a class="skip-link" href="#main">Skip to content</a>

<main id="main" tabindex="-1">
```

A route **past** the repeated navigation, straight to the content.

Reload the home page and press **Tab** until Skip to content appears, then **Enter**. The address gains `#main`.

---

## Break the skip link on purpose

1. In `layouts/all.html`, change only `href="#main"` to `href="#missing-main"`
2. Save and reload: it **still looks like a link**, and Hugo builds
3. Search the inspector for `id="missing-main"`: nothing
4. Restore `href="#main"` and repeat the keyboard check

> Matching words in the address bar are not enough: check that the target exists.

---

## Which file do I edit?

| What is wrong | Look first at |
| --- | --- |
| The article's title | Its front matter `title` |
| A heading or sentence in the body | The page's Markdown |
| A menu label or the footer, everywhere | `layouts/all.html` |
| The site name, everywhere | `title` in `hugo.toml` |
| Font, colour, or spacing | `static/css/site.css`, after the HTML |

Page writing stays in Markdown; shared structure stays in the layout.

---

## Recognise: a data table

```html
<table>
  <caption>Notebook content</caption>
  <tr><th scope="col">Section</th><th scope="col">Purpose</th></tr>
  <tr><td>Articles</td><td>Learning notes</td></tr>
</table>
```

- `tr` a row, `th` a header cell, `td` a data cell
- The `caption` names the table; `scope="col"` ties a header to its column

Tables are for **tabular data**, not page layout. Do not add this to your site.

---

## Recognise: a labelled input

```html
<label for="contact-email">Email address</label>
<input id="contact-email" name="email" type="email">
```

- The label's `for` matches the input's `id`
- `name` identifies the value when it is sent
- A placeholder is **not** a label

This HTML alone sends nothing and stores nothing. Real forms come in the interaction chapter.

---

## Judge an agent's proposal

| Proposal | What to examine |
| --- | --- |
| "Make the `h1` a paragraph so it is smaller" | It removes the main heading. Change size with CSS. |
| "Make every link say Read more" | Can visitors still tell the destinations apart? |

Ask which **files and elements** it will change, and why.

A confident explanation does not replace **inspecting the result**.

---

## Try it yourself

Change only the footer's **first paragraph** to a sentence that fits your notebook. Keep the About link and `footer-note`.

1. Check the footer on Home, About, and your article
2. Follow its About link from the article
3. Reload: the change persists
4. The skip link still targets `main`

---

## Save your checkpoint

Stop the preview and copy the folder to `my-knowledge-site-ch04-backup`.

| File | Today's change |
| --- | --- |
| `layouts/all.html` | New footer; skip link repaired |

- The temporary inspector edit belongs in **no** file
- `#missing-main` must be back to `#main` **before** you copy

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| The footer change vanishes on reload | You edited only the DOM: save it in the layout |
| Hugo reports a template error | Restore the `relURL` link exactly |
| The page shows `{{ ... }}` | Open the Hugo address, not the file |
| `&amp;` shows literally | You wrote `&amp;amp;`, or used a code block |

Browsers **recover** from bad markup: inspect, do not trust appearance.

---

## Completion check

- I can find the `h1`, a body heading, a link, and the image in the inspector
- I can explain why a browser-only edit vanishes on reload
- I recognise elements, attributes, nesting, and void elements
- I can tell Markdown, layout, generated HTML, and the DOM apart
- My new footer appears on every page, and its link works
- The skip link and `main` match again
- I saved a Chapter 4 checkpoint

---

# Next: Practical CSS for Your Hugo Site

Chapter 5: changing appearance deliberately, starting with the `footer-note` class.

**polla.dev/ssg-book**
