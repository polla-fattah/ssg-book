---
title: "Help Readers Find and Use Your Content"
description: "Chapter 15: document titles, descriptions, sitemap and feed, and a search page built from your own content."
book_number: "15"
weight: 16
---

# Help Readers Find and Use Your Content

Static Site Generators in the Age of AI

**Chapter 15**

Polla Fattah

---

## Today's goal

A visitor has the navigation, and nothing else. They cannot **search**, and every tab title looks alike.

- A distinct **title** and a **description** for every page
- The **sitemap** and **feed** Hugo has generated all along
- A **Search** page that filters as the reader types

And a page that still lists every destination when **JavaScript does not run**.

---

## By the end of today you can

- **Give** each page a distinct title and description, with a site-wide fallback
- **Recognise** the sitemap and feed as XML, and say what each is for
- **Build** a search page from your own content, filtered in the browser
- **Test** by keyboard and without JavaScript, and say what a score cannot show

Start from Chapter 14, and work on a **branch**.

---

## The title in every tab

```html
<title>{{ .Title }} | {{ .Site.Title }}</title>
```

On the home page that gives `Welcome to my knowledge notebook | My Knowledge Notebook`: the name twice, and a tab shows only the start.

The document title labels the **tab**, the **bookmark**, the **shared link**, and the **search result**.

---

## A site-wide description

At the end of `hugo.toml`, keeping the existing settings:

```toml
[params]
description = '...'
```

The chapter's value: *Learning notes, small projects, and useful references, published as a static website.*

`[params]` is a TOML table; templates read it as `.Site.Params`.

---

## A better head

In `layouts/baseof.html`, replace the `title` line with:

```html
<title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}
  {{ .Title }} | {{ .Site.Title }}{{ end }}</title>
<meta name="description"
  content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
<link rel="canonical" href="{{ .Permalink }}">
```

- `if .IsHome`: home uses the site name **alone** (`title` is one line in the file)
- `with .Description ... else`: the page's own description, or the **fallback**
- **Canonical**: which address counts as the original

---

## Check the result

| Page | Tab title | Description |
| --- | --- | --- |
| Home | `My Knowledge Notebook` | Its own |
| First learning note | `My first learning note \| ...` | From Chapter 14 |
| About, Resources | `About \| ...` | The **site fallback** |

A quotation mark in a description is **escaped** for the attribute. Check the generated source; do not assume.

---

## The sitemap and the feed

Open these under your preview's base address:

```text
/sitemap.xml
/index.xml
```

| File | For | Read by |
| --- | --- | --- |
| `/sitemap.xml` | A list of your page addresses | Search engines |
| `/index.xml` | A feed of recent content | Feed readers, for subscribers |

Both are **generated**: change content or templates, never these files.

---

## Let readers discover the feed

After the description and canonical lines:

```html
{{ with .OutputFormats.Get "rss" }}
  <link rel="{{ .Rel }}" type="{{ .MediaType.Type }}"
        href="{{ .Permalink }}" title="{{ $.Site.Title }}">
{{ end }}
```

- Home and section pages have a feed; an article **does not**, so `with` skips it
- Inside `with`, the dot is the **output format**; `$` is the context the template **started** with: the page

---

## A Search page

Create `content/search/index.md`:

```markdown
---
title: "Search"
description: "Find a page in this notebook by its title or description."
draft: false
---

Type a word to narrow the list below. Clearing the box shows every page
again. This searches page titles and descriptions, not the full text.
```

---

## layouts/search/page.html

```html
{{ define "main" }}
  <article>
    <h1>{{ .Title }}</h1>
    {{ partial "page-meta.html" . }}
    {{ .Content }}
    <form class="search-form" role="search">
      <label for="search-query">Search titles and descriptions</label>
      <input type="search" id="search-query" name="q" autocomplete="off">
    </form>
    <p id="search-status" role="status"></p>
```

---

## The list of pages

```html
    <ul id="search-index">
      {{ range .Site.RegularPages }}
        {{ if ne .RelPermalink $.RelPermalink }}
          <li class="search-item">
            <a href="{{ .RelPermalink }}">{{ .Title }}</a>
            {{ with .Description }}<p>{{ . }}</p>{{ end }}
          </li>
        {{ end }}
      {{ end }}
    </ul>
```

---

## Read the layout

- A **regular page** like Resources, so `page.html`
- `.Site.RegularPages`: every individual page, **not** section landing pages
- `if ne .RelPermalink $.RelPermalink`: leave out the **Search page itself**; `$` because the dot is now the listed page
- `role="search"` marks the region; `role="status"` marks text whose changes should be **announced**
- A `search.js` script tag follows, with `defer`: it runs after the page exists

Build and open `/search/`: six pages, all linked. Typing does nothing **yet**.

---

## The filtering script

The heart of `static/js/search.js` (full script in the chapter):

```javascript
function filter() {
  var query = input.value.trim().toLowerCase();
  var shown = 0;
  items.forEach(function (item) {
    var match = query === "" || item.textContent.toLowerCase().includes(query);
    item.hidden = !match;
    if (match) { shown += 1; }
  });
}
```

---

## Read it as six decisions

| Part | What it does |
| --- | --- |
| Four `document` lookups | Find the form, box, list, and status by their names |
| `if (!form ...)` guard | Stop **quietly** if one is missing |
| `filter()` | Hide items that do not contain the query |
| `item.hidden = !match` | Use the standard `hidden` attribute |
| The `submit` listener | Stop Enter from reloading the page |
| `filter()` at the end | Fill in the status once on load |

---

## Styles, and three queries

Add to `static/css/site.css` the form rules from the chapter, and this one:

```css
.search-item[hidden] { display: none; }
```

| Type | Result |
| --- | --- |
| `notebook` | Several pages match |
| `reading` | Only the reading-list project |
| `hugo` | **Nothing**: Hugo is in page bodies, not in titles or descriptions |

---

## Add Search to the navigation

In `layouts/baseof.html`, after Resources:

```html
<a href="{{ "search/" | relURL }}">Search</a>
```

- Six items now: check a **phone width**; the navigation should wrap
- Hugo's **menu system** could produce these links, but six explicit links are easier to read
- Use menus when navigation differs between **languages**: Chapter 16

---

## A search that fails silently

Change one attribute only:

```html
<ul id="search-list">
```

The page looks **completely normal**. Every link works. Typing does nothing, the status line stays empty, and the console shows **no error**.

The script's guard did not find `search-index`, and **returned quietly**.

---

## Diagnose from the symptom

The status paragraph is empty, and setting it is the script's **last** step, so the script never got there.

1. Inspect the list element and read its `id`
2. Read the four names at the top of `search.js`
3. Find the one that differs

Chapter 5's selector mistake again: one name, **two files**. Restore `id="search-index"`.

A broken script still leaves a **complete, usable index**: the list is real HTML.

---

## Test like a reader

- **Keyboard**: Tab reaches the skip link, the navigation, the box, then **only the visible** results, with a clear focus outline
- **No JavaScript**: disable it and reload: the **full list**, and a box that does nothing
- **Small widths and zoom**: the form stays in the column, nothing is cut off

`role="status"` is **intended** to be announced. How screen readers do it varies, and it is **not yet tested**: do not claim more.

---

## Automated tools, not scores

Run **Lighthouse** or **axe DevTools** on `/search/` and on an article.

- Read the **individual findings**: missing alt text, skipped headings, low contrast
- Several could become **Chapter 14 rules**
- Ignore the overall number

A tool cannot tell whether descriptions are **accurate**, results are **useful**, or an article is **true**. Chapter 13's unsupported sentence would score perfectly.

---

## Give About and Resources descriptions

Add to each page's front matter, in your own accurate words:

```yaml
description: "Why I keep this notebook, and what you can expect to find in it."
```

```yaml
description: "References that support the work recorded in this notebook."
```

Both pages now have their own head description, and **become searchable** by it. Add the Search template and script to `AGENTS.md`.

---

## Propose it as a pull request

```text
git switch -c find-and-search
git add hugo.toml layouts/baseof.html layouts/search/page.html
git add content/search/index.md static/js/search.js static/css/site.css
git add content/about/index.md content/resources/index.md AGENTS.md
git commit -m "Add a search page, document titles, descriptions, and feed discovery"
git push -u origin find-and-search
```

Let the three Chapter 14 checks pass, read Files changed yourself, merge, and verify the live site.

---

## When to replace this search

- The Search page's HTML **grows** with the site
- It only sees **titles and descriptions**

Somewhere between tens and a few hundred pages, or when readers expect **full-text** results, move to a generated index or a search service.

Change the approach when you can describe the reader's **unmet need**, not at a page count.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| The home tab repeats the name | The `if .IsHome` branch replaced the old line |
| Every page shows the site description | The fallback: add page descriptions |
| `.Site.Title` empty in the feed block | Use `$.Site.Title` |
| Typing does nothing, no console error | The four names in `search.js` |
| A page is missing from Search | Is it a draft? |

---

## Completion check

- Each page has a distinct title; home does not repeat the name
- Every page has a head description, with a fallback
- I can say what `/sitemap.xml` and `/index.xml` are for
- I can explain why `$` is needed inside `with` and `range`
- Search filters as I type and reports how many matched
- I diagnosed the silent failure from the empty status line
- The page lists every destination without JavaScript
- I can name something no audit could establish

---

# Next: Publish in Multiple Languages

Chapter 16: a second language, and navigation, metadata, and structure that differ between versions of one site.

**polla.dev/ssg-book**
