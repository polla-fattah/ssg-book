# Chapter 15 — Help Readers Find and Use Your Content

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*The browser script was checked in isolation. No Hugo build, template lookup, browser review, automated audit, or beginner trial yet.*

Your notebook now has nine pages, a resource directory, a publishing workflow, and checks on every proposal. A visitor arriving at it has the navigation, and nothing else. They cannot search it, and a browser tab showing every page as part of the same long name does not help them keep their place.

In this chapter you will improve how the site describes itself and add a way to search it. You will give every page a useful document title and a description, inspect the sitemap and feed Hugo has been generating all along, and build a search page that filters a list of your pages as the reader types.

The visible result is a working Search page in the navigation. The more important results are quieter: distinct browser-tab titles, a description for each page that both search engines and your own search box can use, and a page that still lists every destination when JavaScript does not run.

## What you will be able to do

By the end, you should be able to:

- Give each page a distinct document title and a description, with a site-wide fallback.
- Recognise Hugo's generated sitemap and feed as XML, and explain what each is for.
- Build a search page from your own content and filter it in the browser.
- Test a page by keyboard and without JavaScript, and say what an automated score does not establish.

Start from the completed Chapter 14 checkpoint, with a clean working tree on `main` and the checks workflow in place. Work on a branch and propose the result through a pull request, as you did in Chapter 14; the commands in Section 15.8 assume you did.

This chapter adds a small amount of JavaScript. You are not expected to learn the language here, and the script is supplied and explained. No package, build tool, or external search service is installed.

## 15.1 Give every page a useful title and description

Open your preview and look at the browser tab for the home page, then for the first learning note. Then view the page source and find the `title` element in the head.

Your base template currently builds it like this:

```html
<title>{{ .Title }} | {{ .Site.Title }}</title>
```

On the home page, that produces `Welcome to my knowledge notebook | My Knowledge Notebook`. The notebook's name appears twice in slightly different words, and a browser tab shows only the first part. The document title is the main label used by a tab, a bookmark, a shared link, and a search result, so it is worth getting right.

Add a site-wide description first. In `hugo.toml`, keep the existing three settings and add a named table at the end:

```toml
[params]
description = 'Learning notes, small projects, and useful references, published as a static website.'
```

`[params]` is a TOML table, as introduced in Chapter 12. Values inside it are available to templates as `.Site.Params`.

Now open `layouts/baseof.html` and replace the single `title` line with these three lines:

```html
<title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} | {{ .Site.Title }}{{ end }}</title>
<meta name="description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
<link rel="canonical" href="{{ .Permalink }}">
```

Keep the character set, viewport, and stylesheet lines exactly as they are.

Three template ideas from Chapter 10 are doing the work. `if .IsHome` asks which page this is, so the home page uses the site name alone. `with .Description` uses the page's own description when it has one, and its `else` branch falls back to the site description. `.Permalink` is the page's full address. A **canonical** link tells search engines which address to treat as the original when a page is reachable by more than one route; our site has one route per page, so this is a precaution rather than a repair.

Rebuild and check the source of three pages. The home page tab should read `My Knowledge Notebook`. The first learning note should read `My first learning note | My Knowledge Notebook`, with the description you added in Chapter 14. About and Resources have no description of their own yet, so both fall back to the site description. You will fix that in Section 15.8.

If a description contains a quotation mark, Hugo escapes it for the attribute rather than breaking the tag, as Chapter 4 explained for `&amp;`. Check the generated source rather than assuming.

> **First checkpoint:** every page has a distinct tab title and a description in its head, with a sensible fallback where a page has none.

## 15.2 Inspect the sitemap and feed Hugo already generates

Two XML files have existed since Chapter 1. With the preview running, open these addresses, adding them to the base address Hugo reports:

```text
/sitemap.xml
/index.xml
```

You should see XML rather than a designed page. Chapter 12 introduced its shape: nested named elements, opening and closing tags, a declaration at the top. Browsers display XML as a tree or as plain source, depending on the browser.

| File | What it is for | Who reads it |
| --- | --- | --- |
| `/sitemap.xml` | A list of your page addresses | Search engines discovering what exists |
| `/index.xml` | A feed of recent content | Feed readers, so people can subscribe |

Read the sitemap and check that the addresses match the pages you expect, including the article added in Chapter 13. Read the feed and check that its items have titles and links. If either lists a page you have withdrawn, remember Chapter 9's warning: generated output from an earlier build can persist until a new build and deployment replace it.

Neither file is something to edit. They are generated, like everything in `public/`. To change what appears in them, change the content or the templates, exactly as Chapter 12 said about hand-editing generated XML.

A feed that nobody can discover is not much use. Add this line to the head in `layouts/baseof.html`, after the description and canonical lines:

```html
{{ with .OutputFormats.Get "rss" }}
  <link rel="{{ .Rel }}" type="{{ .MediaType.Type }}" href="{{ .Permalink }}" title="{{ $.Site.Title }}">
{{ end }}
```

This asks whether the current page has a feed. The home page and section landing pages do; an individual article does not, so `with` skips the whole block there.

Note `$.Site.Title` rather than `.Site.Title`. Inside the `with` block the dot has become the output format, not the page. **`$`** always refers to the context the template started with, which is the page. It is the escape hatch for exactly this situation, and you will use it again in the next section.

Rebuild and view the source of the home page and of an article. The home page should carry the feed link; the article should not.

## 15.3 Generate a search page from your own content

Our search will list every page and filter that list as the reader types. The list is produced by Hugo at build time from the pages themselves, so it cannot fall out of date, and it is ordinary HTML, so it remains useful if the filtering never runs.

Create `content/search/index.md`:

```markdown
---
title: "Search"
description: "Find a page in this notebook by its title or description."
draft: false
---

Type a word to narrow the list below. Clearing the box shows every page again. This searches page titles and descriptions, not the full text of each page.
```

Now create `layouts/search/page.html`. Resources uses `layouts/resources/page.html` for the same reason: Search is a regular page at `content/search/index.md`, not a section landing page.

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

    <ul id="search-index">
      {{ range .Site.RegularPages }}
        {{ if ne .RelPermalink $.RelPermalink }}
          <li class="search-item">
            <a href="{{ .RelPermalink }}">{{ .Title }}</a>
            {{ with .Description }}
              <p>{{ . }}</p>
            {{ end }}
          </li>
        {{ end }}
      {{ end }}
    </ul>

    <script src="{{ "js/search.js" | relURL }}" defer></script>
  </article>
{{ end }}
```

The `range` and `with` blocks are the ones from Chapters 10 and 11. `.Site.RegularPages` is the site's individual pages; as in Chapter 11's project list, it excludes section landing pages such as Articles and Projects, which the navigation already covers. The `if ne .RelPermalink $.RelPermalink` line keeps the Search page from listing itself, and it needs `$` because the dot inside `range` is now the page being listed.

The `role="search"` attribute marks this region as the site's search, and `role="status"` marks the paragraph as one whose changes should be announced. The `defer` attribute tells the browser to run the script after the page structure exists.

Build and preview:

```text
hugo --minify --panicOnWarning
hugo server
```

Open `/search/`. You should see the form and a list of six pages: About, both articles, both projects, and Resources. Every link should work. Typing does nothing yet, and the status paragraph is empty, because the script does not exist.

Notice that About and Resources appear with a title and no description. Their titles are searchable; nothing else about them is.

## 15.4 Add the script that filters the list

Create `static/js/search.js`. Files under `static` are copied to the site root, so this is served at `/js/search.js`, in the same way as the stylesheet from Chapter 5.

```javascript
(function () {
  var form = document.querySelector(".search-form");
  var input = document.getElementById("search-query");
  var list = document.getElementById("search-index");
  var status = document.getElementById("search-status");

  if (!form || !input || !list || !status) {
    return;
  }

  var items = list.querySelectorAll(".search-item");

  function filter() {
    var query = input.value.trim().toLowerCase();
    var shown = 0;

    items.forEach(function (item) {
      var match = query === "" || item.textContent.toLowerCase().includes(query);
      item.hidden = !match;
      if (match) {
        shown += 1;
      }
    });

    if (query === "") {
      status.textContent = "Showing all " + items.length + " pages.";
    } else if (shown === 0) {
      status.textContent = "No pages match that word.";
    } else {
      status.textContent = shown + " of " + items.length + " pages match.";
    }
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
  });

  input.addEventListener("input", filter);
  filter();
})();
```

You are not expected to write this from memory. Read it as six decisions:

| Part | What it does |
| --- | --- |
| The four `document` lookups | Find the form, box, list, and status paragraph by the names used in the template |
| The `if (!form || ...)` guard | Stop quietly if any of them is missing, so other pages are unaffected |
| `filter()` | Compare the lowercased query with each item's text and hide the ones that do not contain it |
| `item.hidden = !match` | Use the standard HTML hidden attribute rather than inventing a class |
| The `submit` listener | Prevent the form from reloading the page when Enter is pressed |
| `filter()` at the end | Fill in the status message once when the page loads |

The comparison is a plain case-insensitive substring match on the text already visible in each item. It does not rank results, handle misspellings, match word stems, or search page bodies. For a notebook of this size that is sufficient; Section 15.8 says when it stops being.

The list needs one styling rule so hidden items really disappear, plus a little room for the form. Add this to the end of `static/css/site.css`:

```css
.search-form label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.search-form input {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
}

#search-status {
  color: #37474f;
}

.search-item[hidden] {
  display: none;
}
```

The last rule matters. The `hidden` attribute normally hides an element, but a `display` value from another rule can override it, so making the intent explicit avoids a puzzle later. As Chapter 5 said, check contrast before adopting a new colour rather than trusting appearance.

Reload `/search/` and try three queries in turn:

| Type this | Expected result |
| --- | --- |
| `notebook` | Several pages match, because the word appears in their titles and descriptions |
| `reading` | The reading-list project alone matches |
| `hugo` | Nothing matches, even though the site is built with Hugo |

The third result is worth pausing on rather than treating as a fault. Hugo is named in your Resources directory and in your articles' bodies, but not in any page title or description, and those are the only text this search examines. Clear the box and all six pages should return.

> **Second checkpoint:** searching filters a list Hugo generated from your own pages, and the status line reports how many matched.

## 15.5 Connect Search to the navigation

In `layouts/baseof.html`, add one link to the existing navigation block, after Resources:

```html
<a href="{{ "search/" | relURL }}">Search</a>
```

Save, then visit three different pages and use the new link from each. The navigation now has six items. That is close to the point where a single row stops being comfortable on a narrow screen, so check it at a phone width using the technique from Chapter 5; the supplied navigation wraps rather than overflowing.

Chapter 3 noted that Hugo has a menu system that keeps navigation data separate from its rendering, and that we would use it when there was enough template knowledge. There now is. We are still not doing it, because six explicit links are easier to read than a configuration table that produces six links. Reach for the menu system when the navigation differs between sections or languages, which Chapter 16 will begin to make true.

## 15.6 Diagnose a search that fails silently

This failure is deliberately undramatic, which is the point.

In `layouts/search/page.html`, change one attribute only:

```html
<ul id="search-list">
```

Save and reload `/search/`. Look carefully before reading on.

The page appears completely normal. Every page is listed, every link works, the form is there. Typing does nothing, and the status paragraph stays empty. Open the browser console from Chapter 4 and you will find no error at all.

The guard in the script is responsible. It looked for `search-index`, did not find it, and returned without doing anything. That guard is worth having, because it stops the script complaining on every other page of the site. The cost is that a genuine mistake produces silence rather than a message.

Work from the observable symptom instead. The status paragraph is empty, and the script's last action is to set it, so the script cannot have reached the end. Then compare the two names:

1. Inspect the list element and read its `id`.
2. Read the four names near the top of `static/js/search.js`.
3. Find the one that differs.

This is Chapter 5's selector mistake in another costume: a name that must match in two files, changed in only one. Restore `id="search-index"`, save, and confirm that filtering and the status line return.

There is one more thing to notice. Because the list is real HTML produced at build time, a broken script leaves a complete, usable index of your site rather than an empty box and an error. A search built by asking the browser to fetch and assemble an index would have failed visibly and uselessly instead. That is a reason to prefer this arrangement at this size, not merely a happy accident.

## 15.7 Test by keyboard, without JavaScript, and at small widths

Automated tools come next. Do these three checks first, because they are the ones that find real problems.

**By keyboard.** Load `/search/` and press Tab from the top of the page. You should reach the Skip to content link, the six navigation links, then the search box, then the links in the list. Type a word and continue tabbing: you should move through the visible results only, because a hidden item cannot receive focus. Confirm that the focus outline from Chapter 5 is visible at every stop.

**Without JavaScript.** In your browser's developer tools, disable JavaScript and reload the page. The expected result is the full list of pages, with a box that does nothing. Confirm that, then re-enable JavaScript. A visitor in that situation still has every destination and a working navigation; they have lost a convenience, not the page.

**At small widths and increased zoom.** Use Chapter 5's method on the Search page: narrow the window to a phone width and separately increase the browser zoom. The form should stay within the reading column, the navigation should wrap, and no text should be cut off.

On announcements, be careful what you claim. The `role="status"` paragraph is intended to be read out when its text changes, which is why the script writes a count there rather than only hiding items. Whether and how that is announced varies between screen readers and browsers, and this draft has not been tested with any of them. Treat it as a reasonable arrangement that still needs checking, not as a verified result.

## 15.8 Use automated tools without trusting their scores, then improve one thing and save

Chromium browsers include Lighthouse in their developer tools, and accessibility extensions such as axe DevTools report a similar class of finding. Run one against `/search/` and one against an article.

Read the individual findings and ignore the overall number. A report of this kind can tell you that an image lacks alternative text, that a heading level was skipped, that a contrast is too low, or that a page has no description. Those are worth acting on, and several could later become rules in the Chapter 14 workflow.

What it cannot tell you is whether your descriptions are accurate, whether the search results are the ones a reader wanted, whether your headings describe what follows them, or whether the article is true. Chapter 13's unsupported sentence would score perfectly. A high score means a set of mechanical checks passed, which is what a green pull request means, and it carries the same limits.

Now make the improvement the chapter has been pointing at. About and Resources still have no description, so they fall back to the site description and offer only a title to your search box. Add one line to the front matter of each, keeping their existing fields:

```yaml
description: "Why I keep this notebook, and what you can expect to find in it."
```

```yaml
description: "References that support the work recorded in this notebook."
```

Use your own accurate wording. Then check both: the head of each page should now carry its own description, and searching for a word from either description should match that page.

Update the file map in `AGENTS.md`, under Files:

```markdown
- The Search page template is layouts/search/page.html.
- The search script is static/js/search.js.
```

Build, review, and propose the result as a pull request on a branch, as in Chapter 14:

```text
hugo --minify --panicOnWarning
git switch -c find-and-search
git status
git add hugo.toml layouts/baseof.html layouts/search/page.html
git add content/search/index.md static/js/search.js static/css/site.css
git add content/about/index.md content/resources/index.md AGENTS.md
git diff --cached
git commit -m "Add a search page, document titles, descriptions, and feed discovery"
git push -u origin find-and-search
```

Open the pull request and let the checks run. All three Chapter 14 rules should still pass: the directory flags are untouched, no root-relative link was added, and both new descriptions sit on pages the description rule does not even examine. Read Files changed yourself, then merge and verify the live site.

Finally, decide when this search stops being the right one. Every page appears in the Search page's HTML, so that page grows with your site, and the filtering sees only titles and descriptions. Somewhere between tens and a few hundred pages, or as soon as readers expect full-text results, the answer becomes a generated index the browser fetches, or a dedicated search service. Change the approach when you can describe the reader's unmet need, not when the page count reaches a particular number.

## Completion check

- [ ] Each page has a distinct document title, and the home page does not repeat the site name.
- [ ] Every page has a description in its head, with the site description as a fallback.
- [ ] I found `/sitemap.xml` and `/index.xml` and can say what each is for.
- [ ] The home page offers the feed for discovery and an article correctly does not.
- [ ] I can explain why `$` is needed inside the `with` and `range` blocks I added.
- [ ] Search lists my pages, filters as I type, and reports how many matched.
- [ ] I diagnosed the silent failure by noticing the empty status line, not an error message.
- [ ] The page still lists every destination with JavaScript disabled.
- [ ] I read individual audit findings and can name something no audit could establish.
- [ ] About and Resources have their own descriptions, and the change passed the checks.

This is enough discoverability for our next steps. Full-text indexing, result ranking, search analytics, structured data for rich results, image optimisation, and performance budgets are outside this chapter's scope. Each becomes worth adding when a reader's difficulty makes the need concrete.

Chapter 16 adds a second language, which is the first change that will make navigation, metadata, and page structure differ between versions of the same site.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| The home page tab still repeats the site name. | Confirm the `if .IsHome` branch is in `layouts/baseof.html` and that you replaced the old `title` line rather than adding a second one. |
| Every description is the site description. | Those pages have no `description` in their front matter. That is the fallback working; add page descriptions where you want distinct text. |
| The build fails after the head edit. | Check that each `{{ if }}`, `{{ with }}`, and `{{ end }}` is matched, and that the attribute quotation marks survived the paste. |
| `/sitemap.xml` or `/index.xml` is not found. | Use the full base address Hugo reports, including any project prefix, and check the spelling. |
| The feed link appears on every page, or on none. | The `with .OutputFormats.Get "rss"` block decides this. Section pages and the home page have a feed; regular pages do not. |
| `.Site.Title` is empty inside the feed block. | Inside `with`, the dot is the output format. Use `$.Site.Title`. |
| The Search page uses the wrong layout. | Confirm the path `layouts/search/page.html`. Search is a regular page, like Resources. |
| The Search page lists itself. | Restore the `if ne .RelPermalink $.RelPermalink` condition, including the `$`. |
| Articles and Projects are missing from the list. | That is intended. `.Site.RegularPages` excludes section landing pages, which the navigation covers. |
| A page you expect is missing. | Check whether it is still a draft. A normal build excludes drafts, so the generated list excludes them too. |
| Typing does nothing and the console is empty. | The script's guard returned early. Compare the four names in `search.js` with the `id` and class in the template. |
| Items do not disappear when filtered. | Confirm the `.search-item[hidden]` rule is in the stylesheet and that the served CSS contains it. |
| The page reloads when Enter is pressed. | The script did not load or returned early. Check the script tag's address, then the four names. |

An automated report and a passing check both examine stated rules on one version of a page. Neither establishes that a reader can find what they came for.

---

## Editorial note for the author — remove before publication

This chapter pays two debts: Chapter 9's note that the starter omits the description from the head, and Chapter 3's promise of the Hugo menu system. Section 15.5 deliberately declines the second, because a configuration table producing six links is harder to read than six links; Chapter 16's per-language navigation is the real trigger.

The search design departs from the usual Hugo recipe on purpose. Rather than a JSON output format and a browser-side index fetch, the page list is rendered as HTML at build time and filtered in place. That reuses only the `range`, `with`, and context skills from Chapters 10 and 11, avoids output-format lookup rules, makes Section 15.7's no-JavaScript check a genuine success, and leaves the Section 15.6 failure with a page that still works. The cost — titles and descriptions only, on a page that grows with the site — is stated twice in the text. A JSON index belongs after Chapter 16 if a later edition wants one.

Section 15.6 is the quietest designed failure in the book: no console error, no visual defect. The diagnostic route is the empty status paragraph, which is why the script sets that message last. Watch whether beginners find an absent error more unsettling than a crash; if so, make the guard log rather than removing it.

The Section 15.4 script was executed against a stand-in for its page, which corrected one instruction in the draft. Nothing else here is validated, and Section 15.2 is the highest risk in the chapter because it assumes generated output the project has never been checked for. See the validation record.
