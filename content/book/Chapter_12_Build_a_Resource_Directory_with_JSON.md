# Chapter 12 — Build a Resource Directory with JSON

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*Checked with Hugo 0.150.0 on Linux in a focused fixture. No beginner trial, browser review, or deployment yet.*

Your Resources page contains a small collection of links. Markdown handles that well. As the collection grows, however, you may want every entry to have the same information: a title, an address, a short explanation, and a few topics.

We will store those repeated details in JSON and let a Hugo partial display them. The surrounding introduction and links to your own notebook pages will remain ordinary Markdown.

By the end, you will be able to add a resource by editing a data file. The template will supply its HTML. You will also recognise where YAML, TOML, CSV, and XML fit, without trying to master every format in one chapter.

## What you will be able to do

By the end, you should be able to:

- Read and edit a small JSON array containing consistently structured records.
- Connect a local JSON resource to a Hugo template and inspect its rendered output.
- Distinguish a parsing error from incorrect or incomplete information.
- Choose a suitable format for page writing, configuration, records, or spreadsheet exchange.

Start from the completed Chapter 11 checkpoint with a clean Git working tree. Keep the same Hugo installation and shared templates. No database, JavaScript package, or external data service is required. Internet access is useful for checking the linked documentation, but the directory itself is built from a local file.

## 12.1 Put two existing resources into JSON

We will begin with the two links already under Website publishing. Their titles, destinations, and descriptions are known, so this first step is a change of representation rather than a research task.

At the project root, create an `assets` folder. Inside it, create a `data` folder and then `resource_links.json`. The complete path is:

```text
assets/data/resource_links.json
```

Use this content:

```json
[
  {
    "title": "Hugo documentation",
    "url": "https://gohugo.io/documentation/",
    "description": "The official reference for Hugo configuration, content, and templates.",
    "topics": ["Hugo", "Reference"],
    "start_here": true
  },
  {
    "title": "Hugo page bundles",
    "url": "https://gohugo.io/content-management/page-bundles/",
    "description": "An explanation of grouping a page with related resources.",
    "topics": ["Hugo", "Content organisation"],
    "start_here": false
  }
]
```

The outside square brackets enclose an **array**, an ordered list. Each pair of curly braces encloses an **object**, which groups the named values for one resource. We will call each object a resource record.

Save the file as UTF-8 plain text in your editor. Make sure its name ends in `.json`, rather than `.json.txt`. Do not place Markdown code fences or front matter delimiters inside it.

`start_here` is our own editorial flag. Here, it marks the general documentation as a suggested starting point. It does not claim that Hugo itself assigned a rating to the resource.

The `assets` directory holds source resources that Hugo can process. This is different from `static`, whose files are copied into the output directly. We will ask Hugo to read this JSON while generating the page. [Hugo: resources.Get](https://gohugo.io/functions/resources/get/)

## 12.2 Display the records on Resources

We can reuse the base template from Chapter 11 and add one small content layout. Create `layouts/_partials/resource-directory.html`:

```html
<h2 id="website-publishing">Website publishing</h2>
{{ with resources.Get "data/resource_links.json" }}
  <ul>
    {{ range . | transform.Unmarshal }}
      <li>
        <a href="{{ .url }}">{{ .title }}</a>
        {{ if .start_here }}
          <strong>Start here</strong>
        {{ end }}
        <p>{{ .description }}</p>
        {{ with .topics }}
          <p><strong>Topics:</strong> {{ delimit . ", " }}</p>
        {{ end }}
      </li>
    {{ else }}
      <li>No resources to display yet.</li>
    {{ end }}
  </ul>
{{ else }}
  {{ errorf "Missing resource directory data: assets/data/resource_links.json" }}
{{ end }}
```

The `with`, `range`, and `if` blocks follow the patterns from Chapter 10. The new functions read the file, interpret its JSON, and join the topic names. We will examine those lines after seeing the result.

Now create `layouts/resources/page.html`:

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

Use `page.html` here because Resources is the regular page at `content/resources/index.md`. Projects used `section.html` for its section landing page. Keep the existing Resources content filename and front matter unchanged.

Build and preview:

```text
hugo --minify --panicOnWarning
hugo server
```

Open Resources through the navigation. Below its existing Markdown content, you should see the generated Website publishing list. It should contain two records, topic labels, and one Start here label.

For this brief intermediate stage, the old manually written Website publishing list is still present. Compare its two destinations and descriptions with the generated entries before removing it.

### Remove the old list without losing the introduction

In `content/resources/index.md`, delete only the old `## Website publishing` heading and the two bullets immediately beneath it. Retain:

- The front matter and opening paragraph.
- The How to use these resources section created in Chapter 8.
- The Examples from this notebook heading and its internal links.

Save and refresh. There should now be one Website publishing heading, after the Markdown sections. The general documentation link also remains in the explanatory How to use section; that repetition is intentional.

The explicit `id="website-publishing"` preserves the heading's existing fragment destination. Open the page with `#website-publishing` at the end of its address and check that the fragment still identifies the correct section.

> **First checkpoint:** Resources displays two JSON records through the shared page structure, and its earlier introduction and internal links still work.

## 12.3 Learn the JSON shapes used by the directory

JSON stands for **JavaScript Object Notation**, but it is a data format used by many languages. Writing this file does not add JavaScript behaviour to the website. [JSON: format overview](https://www.json.org/json-en.html)

Our records use a small agreement:

| Key | Expected value | Purpose |
| --- | --- | --- |
| `title` | Non-empty string | Text readers will activate as a link |
| `url` | String containing a complete HTTPS address | Destination of this external resource |
| `description` | Non-empty string | One accurate sentence about the resource |
| `topics` | Array of strings, possibly empty | A few useful subject labels |
| `start_here` | Boolean | Whether this entry gets our starting-point label |

Use these keys consistently in every record. This table is an editorial agreement; we have not installed a validator that enforces every requirement.

### Objects contain named values

A JSON member has a quoted key, a colon, and a value:

```json
"title": "Hugo documentation"
```

The title is a **string**, or text value. Both JSON keys and string values use straight double quotation marks. The single-quote option shown for YAML in Chapter 9 does not apply here.

Within an object, commas separate members. A comma also separates adjacent objects in the outside array. There is no comma after the final member or final array element.

Formatting across lines makes the records easier to review, but indentation does not define their structure as it does in YAML. Braces, brackets, commas, and colons do that job.

### Arrays can appear inside objects

The whole directory is an array of records. Each record's topics value is another array:

```json
["Hugo", "Reference"]
```

This preserves two separate labels. `"Hugo, Reference"` would instead be one string. If no labels are useful, use `[]`, an empty array.

The outer array also gives us a deliberate display order. Moving a complete record earlier in that array moves it earlier in our rendered list. Rearranging the members inside an individual object does not change the template's field order.

### Boolean values are not quoted text

```json
"start_here": false
```

`false` is a Boolean value. `"false"` is a non-empty string. Both can occur in syntactically valid JSON, but only the unquoted Boolean matches our model.

This difference matters to the supplied template. Its `if .start_here` condition treats a non-empty string as true, so the text `"false"` can produce a Start here label. A successful parse does not guarantee the intended meaning.

JSON also supports numbers and `null`, as well as strings, Booleans, objects, and arrays. We do not need numeric ratings or null values for this directory, so we will not add fields merely to demonstrate them.

### Keep text inside its quotes

A quotation mark inside a string must be escaped with a backslash:

```json
"description": "An explanation of Hugo's \"page bundles\" feature."
```

The rendered sentence contains quotation marks without the escape backslashes. An apostrophe, as in `Hugo's`, does not need escaping inside these double quotes.

Keep descriptions as plain text. The template does not render Markdown within them. Ordinary JSON does not allow comments either; put authoring guidance in `AGENTS.md` or a separate note instead of adding `//` lines to this file.

## 12.4 Trace the data from file to HTML

The partial starts with:

```html
{{ with resources.Get "data/resource_links.json" }}
```

`resources.Get` looks beneath `assets`, so its argument leaves off the leading `assets/`. The current context inside this `with` block is the resource it found.

Next:

```html
{{ range . | transform.Unmarshal }}
```

The pipe passes that resource to `transform.Unmarshal`, which parses its structured contents. Here, the result is the JSON array. `range` then visits each record. *Unmarshal* means converting a stored representation into values the template can use. Hugo supports this operation for several data formats. [Hugo: transform.Unmarshal](https://gohugo.io/functions/transform/unmarshal/)

Inside the loop, `.title`, `.url`, and `.description` refer to keys in one JSON object. They are not the page methods `.Title`, `.RelPermalink`, and `.Description` used in Chapter 10. These records are data; they do not automatically become Hugo pages.

The inner topics block changes context again:

```html
{{ with .topics }}
  <p><strong>Topics:</strong> {{ delimit . ", " }}</p>
{{ end }}
```

Inside it, the dot is the topics array. `delimit` joins its values using the supplied separator, producing text such as `Hugo, Reference`. An empty array skips the whole paragraph. [Hugo: delimit](https://gohugo.io/functions/collections/delimit/)

The final `else` belongs to the outer file lookup. If the JSON file cannot be found, `errorf` reports our message and fails the build. A deliberately empty array is different: it reaches the loop's `else` and displays No resources to display yet. [Hugo: errorf](https://gohugo.io/functions/fmt/errorf/)

### Keep the three source roles distinct

| Source | What you edit there |
| --- | --- |
| `content/resources/index.md` | Introduction, explanatory writing, and notebook links |
| `assets/data/resource_links.json` | Repeated external-resource records |
| `layouts/_partials/resource-directory.html` | How each record is presented |

The Resources page layout connects these pieces to the shared base. Changing a description in JSON does not require editing the HTML template.

This happens during the Hugo build. Visitors receive the resulting HTML list; their browser does not fetch the JSON for this exercise. Parsing this asset alone does not publish a separate downloadable JSON file. Its source will still be visible if you push it to your public GitHub repository.

## 12.5 Add a resource without changing the template

Stop the preview and open `assets/data/resource_links.json`. Add a comma after the second object's closing brace, then add this third object before the array's closing square bracket:

```json
{
  "title": "Hugo template introduction",
  "url": "https://gohugo.io/templates/introduction/",
  "description": "An introduction to template expressions, functions, and context in Hugo.",
  "topics": ["Hugo", "Templates"],
  "start_here": false
}
```

This object belongs inside the existing array. Do not paste it after the final `]`, wrap it in another array, or replace the first two records.

The linked page introduces the template concepts used in the preceding chapters. Open it and compare its content with our description before retaining the entry. [Hugo: template introduction](https://gohugo.io/templates/introduction/)

Build and preview Resources. You should see three entries, with the new one last. Follow its link. The shared header, footer, and internal notebook links should remain unchanged.

For this exercise, `url` stores complete external HTTPS addresses. Pass them directly to `href`; do not prepend the GitHub repository path. Keep the existing relative notebook links in Markdown. A mixed directory of internal and external destinations would need an explicit convention for handling both.

### Choose an order yourself

Move the template-introduction record before the page-bundles record while leaving the general documentation first. Move the complete object and check the commas between its neighbours.

Build and preview again. The list should now follow your chosen order without a template edit. This is a small independent variation: you control the content sequence while preserving the record structure.

If you edit a description as well, keep it factual and brief. Do not add a claim that you have completed a tutorial simply because its link is now on the website.

> **Second checkpoint:** you added and reordered records through JSON alone, and verified the displayed information and destinations.

## 12.6 Repair broken syntax, then check meaning

Stop the preview. In the first record, temporarily remove the comma after its title line:

```text
"title": "Hugo documentation"
"url": "https://gohugo.io/documentation/",
```

This excerpt is deliberately invalid JSON. Run:

```text
hugo --minify --panicOnWarning
```

The build should fail while parsing the resource. Read the error and identify the data file or the partial's parsing expression. The reported position may be where parsing became impossible rather than exactly where the comma was removed.

Restore the comma and build again. Do not change a working template to compensate for malformed input.

Then review the directory against the table in Section 12.3. In particular, check that every record has all five keys, topics are arrays, and the starting-point flags are actual Booleans.

There are three separate questions:

1. Can Hugo parse the JSON and render the template?
2. Do the records follow our agreed field names and value types?
3. Are their descriptions accurate and their destinations useful?

The supplied build catches syntax errors and missing files. It does not fully enforce our record model, verify remote links, or establish the truth of descriptions. A misspelled key may leave output blank; an incorrect but well-formed URL may still be rendered as a link.

Use the editor's JSON highlighting and formatting to make mistakes easier to spot. Formatting is not a factual review, and old files in `public/` are not evidence that the latest build succeeded.

## 12.7 Recognise the other formats without rewriting the project

JSON is our working format for the directory. The following examples are for comparison only; do not create extra copies of the directory in the project.

| Format | Useful role in this book | What to recognise |
| --- | --- | --- |
| Markdown | Page writing | Headings, paragraphs, links, and lists |
| JSON | Repeated resource records | Objects, arrays, quoted keys, explicit value types |
| YAML (`.yaml` or `.yml`) | Front matter and the GitHub workflow | Named values and indentation-based structure |
| TOML | `hugo.toml` configuration | `key = value` entries and named tables |
| CSV | Rows exchanged with spreadsheet tools | A header row, records, delimiters, and quoted cells |
| XML | Formats such as sitemaps and feeds | Nested named elements and attributes |

### YAML and TOML: familiar information, different notation

Here is a small part of one resource represented in YAML:

```yaml
title: "Hugo documentation"
start_here: true
topics:
  - "Hugo"
  - "Reference"
```

The same information can be expressed in TOML:

```toml
title = "Hugo documentation"
start_here = true
topics = ["Hugo", "Reference"]
```

These standalone examples have no front matter delimiters. In a Markdown page, Hugo uses delimiters to identify where metadata begins and ends. Keep the existing YAML page front matter and TOML site configuration; converting them adds no benefit to this exercise. [YAML specification](https://yaml.org/spec/1.2.2/), [TOML specification](https://toml.io/en/v1.0.0)

### CSV: useful rows, but conversion needs decisions

A small spreadsheet export might look like this:

```csv
title,url,description
Hugo documentation,https://gohugo.io/documentation/,"Reference for configuration, content, and templates."
Hugo page bundles,https://gohugo.io/content-management/page-bundles/,Explains grouping a page with related resources.
```

The quotation marks keep the commas inside the first description from becoming column separators. CSV dialects vary, so check the delimiter and encoding used by an export. CSV is plain tabular text; it does not preserve a spreadsheet's full formatting or workbook structure. [RFC 4180: CSV format](https://www.rfc-editor.org/info/rfc4180/)

To turn those rows into our JSON records, map each column to its matching key, then deliberately supply `topics` and `start_here`. The CSV shown does not contain those values. A converter or agent should not invent them without an instruction.

For a small import, compare the number of data rows with the number of JSON objects, inspect the first and last records, and check descriptions containing commas or quotation marks. Treat arrays and Booleans explicitly rather than carrying every cell across as a string.

Hugo can parse CSV with `transform.Unmarshal`, but the CSV-to-directory workflow is optional future work. Our current template expects the JSON array shown earlier. Merely renaming a CSV file to `.json` does not convert it.

### XML: recognise the wrapper and preserve meaning

A simplified XML record could be:

```xml
<resource>
  <title>Hugo documentation</title>
  <url>https://gohugo.io/documentation/</url>
</resource>
```

The opening and closing tags describe a hierarchy. Real XML formats define which elements and attributes belong where; similar-looking tags do not make this fragment a valid sitemap or feed. [W3C: XML specification](https://www.w3.org/TR/xml/)

When you encounter Hugo's generated sitemap or RSS output, recognise XML as the representation. Change the source or relevant template to maintain generated output, rather than hand-editing the generated file.

## 12.8 Keep the directory manageable and save

A directory helps when records share stable fields and presentation. It is less useful for a long explanation, a learning narrative, or a page whose information has no repeated shape. Continue writing those in Markdown.

Before adding a field, ask what a reader or a template will do with it. An unused rating, review date, or author field creates more information to maintain. Our five fields are enough for the current result.

### Update the project guidance

Add these entries under Files in `AGENTS.md`:

```markdown
- Resource-directory records are in assets/data/resource_links.json.
- The Resources page template is layouts/resources/page.html.
- Resource-directory rendering is in layouts/_partials/resource-directory.html.
```

Add this working agreement alongside the existing rules:

```markdown
- Resource records use title, url, description, topics (an array of strings), and start_here (a Boolean). Preserve these types and do not invent descriptions or destinations.
```

An agent can help prepare a record or convert supplied rows, but it needs source information and a field agreement. Chapter 13 will practise that editorial workflow in more detail.

### Review the completed page

Check that Resources shows three directory entries in your chosen order, with the expected topics and starting-point label. Follow each external link, then verify the retained notebook links. Check Projects too, so the new Resources layout has not displaced the section layout from Chapter 11.

Stop the preview and run:

```text
hugo --minify --panicOnWarning
git status
git diff
```

The intended changes are three new files, the edited Resources Markdown, and the updated guidance. Read the new files as well as the ordinary diff before staging:

```text
git add assets/data/resource_links.json layouts/resources/page.html layouts/_partials/resource-directory.html
git add content/resources/index.md AGENTS.md
git diff --cached
```

Confirm that only the old manual Website publishing section was removed from Markdown. Retain the earlier agent-assisted How to use section and its links.

When the result matches your review, commit:

```text
git commit -m "Build the Resources directory from local JSON records"
git status
```

The working tree should be clean. The local checkpoint is sufficient for the next chapter; publishing remains the reviewed workflow from Chapter 7.

## Completion check

- [ ] I can distinguish an object, an array, a string, and a Boolean in the directory.
- [ ] All records follow the five-field agreement and contain accurate descriptions.
- [ ] I know which file holds the records, the page writing, and the rendering instructions.
- [ ] I added and reordered a resource without changing the template.
- [ ] I repaired the missing comma and checked more than build success.
- [ ] I can explain when CSV conversion needs decisions about missing fields and types.
- [ ] Resources retains its earlier Markdown sections and working links.
- [ ] I updated the guidance and committed the five intended files.

This is enough structured data for our next steps. A database, an API request, a browser-side loader, and automated format conversion are outside this chapter's scope. A JSON file and a template cover a great deal before any of those becomes necessary.

Chapter 13 turns supplied source material into linked pages. The field agreement you have just written becomes the standard an agent's contribution has to meet.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| The missing-data message appears. | Check the exact path `assets/data/resource_links.json`; the resource lookup omits the initial `assets/`. |
| Hugo reports a JSON parsing error. | Check commas, double quotes, matching brackets, and whether a comment or trailing comma was added. |
| An entry has blank text. | Compare its keys with the model and the lowercase keys used in the template. |
| Start here appears for `"false"`. | Replace the string with the Boolean `false`. |
| Topics are displayed incorrectly. | Store separate topic strings inside an array, not one combined string. |
| The old list still appears. | Remove only the manual Website publishing heading and its two original bullets. |
| The generated directory is absent. | Check `layouts/resources/page.html` and its partial call; Resources is a regular page. |
| A record uses an internal-looking URL. | This model uses complete external HTTPS addresses; keep notebook links in the Markdown section. |
| A build passes but a destination fails. | Verify the URL itself. This template does not perform remote-link checks. |

---

## Editorial note for the author — remove before publication

JSON is the hands-on focus. YAML and TOML are recognition comparisons building on earlier chapters; CSV introduces conversion decisions, and XML is brief orientation. The chapter does not add a database, API retrieval, a browser-side loader, a complete schema validator, or automated format conversion.

The canonical checkpoint uses a JSON asset with `resources.Get` and `transform.Unmarshal`. This works with the book's Hugo 0.150.0 baseline without relying on the later `hugo.Data` API or deprecated `.Site.Data` access. Hugo also has a root `data` directory, but it is not the source location used by this exercise. Keep the complete `assets/data/` path consistent in future chapters.

The generated Website publishing section follows the retained Markdown sections and keeps its fragment identifier. Its external links are complete URLs; internal notebook links remain in Markdown. Chapter 13 should retain the three records and use supplied source material for any proposed additions.

Official documentation was consulted on 17 September 2026. The exact JSON and templates were checked with Hugo 0.150.0 on Linux against the Chapter 11 validation fixture. Seven other authored routes retained their generated structure and meaningful text. As in earlier checks, some unrelated page bodies were placeholders; this was not a complete replay of the book.

Checks covered two-record rendering, addition and reordering of the third record, preservation of the Resources Markdown sections, the heading fragment, external and internal destinations at root and project-prefix configurations, malformed and missing input, empty arrays and topics, the quoted-Boolean pitfall, HTML escaping, and the five-file Git checkpoint. The JSON asset was not separately published by this rendering path. The supplied TOML, CSV, and XML examples were also parsed locally; no automated conversion pipeline was created.

External documentation pages were consulted, but visual browser review, a beginner trial, and a live deployment were not performed. The template is intentionally not a complete record-schema or remote-link validator; later CI work should distinguish these checks from parsing and rendering.
