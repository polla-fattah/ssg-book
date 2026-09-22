---
title: "Build a Resource Directory with JSON"
description: "Chapter 12: structured data, rendered by these shorter templates."
book_number: "12"
weight: 13
---

# Build a Resource Directory with JSON

Static Site Generators in the Age of AI

**Chapter 12**

Polla Fattah

---

## Today's goal

As the Resources list grows, every entry should carry the **same information**: a title, an address, a short explanation, and a few topics.

- Store the repeated details in **JSON**
- Let a Hugo **partial** display them
- Keep the introduction and notebook links in **Markdown**

Add a resource by editing **data**; the template supplies the HTML.

---

## By the end of today you can

- **Read and edit** a small JSON array of consistent records
- **Connect** a local JSON file to a Hugo template, and inspect the output
- **Distinguish** a parsing error from wrong or missing information
- **Choose** a format for writing, configuration, records, or spreadsheets

Start from Chapter 11 with a **clean** tree (companion branch `chapter-11`). No database, package, or data service.

---

## Two resources as JSON

Create `assets/data/resource_links.json`, an array of two records:

```json
[
  {
    "title": "Hugo documentation",
    "url": "https://gohugo.io/documentation/",
    "description": "The official reference for Hugo configuration, content, and templates.",
    "topics": ["Hugo", "Reference"],
    "start_here": true
  },
```

The second, for page bundles, follows; the chapter gives the complete file.

---

## Arrays, objects, and one flag

- `[ ]` encloses an **array**: an ordered list
- `{ }` encloses an **object**: the named values of one resource record
- `start_here` is **our** editorial flag, not a rating from Hugo
- Plain UTF-8 text ending in `.json`: no code fences, no front matter

`assets/` holds sources Hugo **processes** during the build; `static/` files are copied as they are.

---

## The directory partial, part 1

`layouts/_partials/resource-directory.html` begins:

```html
<h2 id="website-publishing">Website publishing</h2>
{{ with resources.Get "data/resource_links.json" }}
  <ul>
    {{ range . | transform.Unmarshal }}
      <li>...one record...</li>
    {{ end }}
  </ul>
```

---

## The directory partial, part 2

```html
<li>
  <a href="{{ .url }}">{{ .title }}</a>
  {{ if .start_here }}<strong>Start here</strong>{{ end }}
  <p>{{ .description }}</p>
  {{ with .topics }}
    <p><strong>Topics:</strong> {{ delimit . ", " }}</p>
  {{ end }}
</li>
```

An empty array shows an `else` message; a missing file stops the build with `errorf`.

---

## A layout for Resources

Resources is a **regular page**, so create `layouts/resources/page.html`:

```html
{{ define "main" }}
  <article>
    <h1>{{ .Title }}</h1>
    {{ partial "page-meta.html" . }}
    {{ .Content }}
    {{ partial "resource-directory.html" . }}
  </article>
{{ end }}
```

---

## Remove the old list, keep the rest

Build and preview: the generated list appears **below** the old manual one. Compare them first.

In `content/resources/index.md`, delete **only** the old `## Website publishing` heading and its two bullets. Keep:

- The front matter and opening paragraph
- How to use these resources, from Chapter 8
- Examples from this notebook, with its internal links

Check `#website-publishing` still reaches the right section.

---

## Our record model

| Key | Expected value |
| --- | --- |
| `title` | A non-empty string |
| `url` | A complete HTTPS address |
| `description` | One accurate sentence |
| `topics` | An array of strings, maybe empty |
| `start_here` | A Boolean |

An **editorial agreement**: nothing enforces it yet.

---

## JSON syntax

```json
"title": "Hugo documentation",
"topics": ["Hugo", "Reference"],
"description": "An explanation of Hugo's \"page bundles\" feature."
```

- Quoted key, colon, value; **double** quotes only
- **Commas** between members and between records, never after the last
- Indentation is for reading: braces, brackets, commas, and colons carry the structure
- Escape a quote inside a string as `\"`; no comments allowed

---

## Types matter

- `["Hugo", "Reference"]` is two labels; `"Hugo, Reference"` is one string
- `[]` is an empty array: the Topics line disappears
- The **array order** is the display order

```json
"start_here": false
```

`false` is a Boolean; `"false"` is a non-empty **string**, which `if` treats as **true**. Valid JSON, wrong meaning.

---

## From file to HTML

- `resources.Get "data/resource_links.json"` looks inside `assets/`
- `transform.Unmarshal` **parses** the file into values the template can use
- `range` visits each record
- `.title` and `.url` are **keys in the data**, not page methods like `.Title`
- `delimit . ", "` joins the topics into `Hugo, Reference`

It all happens at **build** time: visitors receive HTML, not the JSON file.

---

## Three sources, three roles

| Source | What you edit there |
| --- | --- |
| `content/resources/index.md` | Introduction, writing, notebook links |
| `assets/data/resource_links.json` | The repeated resource records |
| `layouts/_partials/resource-directory.html` | How each record looks |

Change a description in JSON: **no template edit** needed.

Pushed to a public repository, the JSON source is still **visible**.

---

## Add a resource with data alone

After the second record's `}`, add a comma and a third record, **inside** the array:

```json
{
  "title": "Hugo template introduction",
  "url": "https://gohugo.io/templates/introduction/",
  "description": "An introduction to template expressions, functions, and context in Hugo.",
  "topics": ["Hugo", "Templates"],
  "start_here": false
}
```

Open the link and check the description matches it.

---

## Choose the order yourself

Move the template-introduction record **before** the page-bundles record, keeping the general documentation first.

- Move the **whole** object; check the commas on both sides
- Build and preview: a new order, **no template edit**
- `url` holds complete external addresses: never add the repository path

> You added and reordered records through JSON alone.

---

## Break the syntax on purpose

Remove the comma after the first record's title:

```text
"title": "Hugo documentation"
"url": "https://gohugo.io/documentation/",
```

`hugo --minify --panicOnWarning` **fails** while parsing. The reported position may be later than the missing comma.

Restore the comma. **Never** change a working template to compensate for broken data.

---

## Three separate questions

1. Can Hugo **parse** the JSON and render the template?
2. Do the records follow our **field names and types**?
3. Are the descriptions **accurate** and the destinations useful?

The build catches the first. It does **not** enforce the model, check remote links, or judge the truth. A misspelled key leaves a **blank**; a wrong URL still renders as a link.

---

## Formats and their roles

| Format | Its role in this book |
| --- | --- |
| Markdown | Page writing |
| JSON | Repeated resource records |
| YAML | Front matter and the GitHub workflow |
| TOML | `hugo.toml` configuration |
| CSV | Rows from spreadsheet tools |
| XML | Sitemaps and feeds |

---

## The same data, three notations

```yaml
title: "Hugo documentation"
start_here: true
topics:
  - "Hugo"
```

```toml
title = "Hugo documentation"
start_here = true
topics = ["Hugo"]
```

Recognise them; **do not convert** the project's existing files.

---

## CSV needs decisions

```csv
title,url,description
Hugo documentation,https://gohugo.io/documentation/,"Configuration, content, and templates."
```

- Quotes keep a comma **inside** a cell from splitting it
- The rows have no `topics` or `start_here`: those need **decisions**, not invention
- Compare row and record counts; check first and last records
- Renaming `.csv` to `.json` does **not** convert it

---

## XML: recognise it

```xml
<resource>
  <title>Hugo documentation</title>
  <url>https://gohugo.io/documentation/</url>
</resource>
```

- Nested named elements describe a hierarchy
- Real formats define which elements belong where
- Hugo's sitemap and RSS are XML: change the **source or template**, never the output

---

## Keep the directory manageable

- Use data for **repeated shapes**; keep explanations and narratives in Markdown
- Before adding a field, ask **who uses it**
- Update `AGENTS.md` with the three new file locations, and this agreement:

```markdown
- Resource records use title, url, description, topics (an array
  of strings), and start_here (a Boolean). Preserve these types and
  do not invent descriptions or destinations.
```

---

## Save the checkpoint

```text
git add assets/data/resource_links.json layouts/resources/page.html
git add layouts/_partials/resource-directory.html
git add content/resources/index.md AGENTS.md
git diff --cached
git commit -m "Build the Resources directory from local JSON records"
```

Five files. Only the old Website publishing section left the Markdown; check Projects still has its own layout.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| The missing-data message | The path; the lookup omits `assets/` |
| A JSON parsing error | Commas, double quotes, brackets, comments |
| An entry has blank text | Its keys against the model |
| Start here on `"false"` | Use the Boolean `false` |
| No generated directory | `layouts/resources/page.html` and its call |

---

## Completion check

- I can tell an object, an array, a string, and a Boolean apart
- All records follow the five-field agreement, accurately
- I know which file holds records, writing, and presentation
- I added and reordered a resource without a template edit
- I repaired the missing comma and checked more than the build
- I know why CSV conversion needs decisions
- Resources keeps its Markdown sections and links
- I committed the five intended files

---

# Next: Create and Maintain Content with AI Agents

Chapter 13: turn supplied sources into linked pages, with every claim checked.

**polla.dev/ssg-book**
