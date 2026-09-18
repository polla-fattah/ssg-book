---
title: "Understand the HTML Behind Your Pages"
weight: 4
book_number: 4
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1, 17 September 2026**  
*Checked with Hugo 0.150.0 on Linux. No beginner trial; the developer-tools and keyboard exercises are not browser-tested yet.*

You have written articles, created sections, and changed the navigation of your website. Now we will look at what the browser receives when it displays those pages.

The title on the screen is not simply large text. The navigation is not merely a row of coloured words. They have a structure that the browser can interpret. Understanding that structure will help you make deliberate changes, diagnose mistakes, and assess code suggested by an AI agent.

You will begin by inspecting your existing article. Then you will make a temporary browser-only change, update the site's footer in its source file, and investigate how a link can look correct while pointing to the wrong place.

## What you will be able to do

By the end, you should be able to:

- Inspect a rendered page and recognise its main HTML elements and attributes.
- Distinguish Markdown, Hugo templates, generated HTML, and the browser's live document.
- Make and verify a small persistent change to the shared layout.
- Check headings, links, images, and the skip-link target for basic structural correctness.

You do not need to memorise an HTML reference or learn JavaScript in this chapter. We will work mostly with structures already present in your site.

## 4.1 Inspect the article and change it in the browser only

Start from the Chapter 3 project, with its seven authored pages and five navigation links. Keep your Chapter 3 backup outside the active project.

In the project terminal, run:

```text
hugo server
```

Open the address reported by Hugo. Use Articles to reach your first learning note, normally at:

```text
http://localhost:1313/articles/first-learning-note/
```

In a desktop browser, right-click the article's main heading and choose **Inspect** or **Inspect Element**. If you are using a trackpad, use its context-menu gesture. Browser developer tools should open beside or below the page.

Look for the **Elements** panel in Chromium-based browsers such as Chrome or Edge, or the **Inspector** in Firefox. The exact interface varies. You can also open developer tools through the browser's menu and use its element-picker tool to select the heading. [MDN: browser developer tools](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools)

You should find something like:

```html
<h1>My first learning note</h1>
```

If you personalised the title, your words will differ. The important part is the surrounding `h1` element.

Now inspect the first paragraph. You should find a `p` element containing its text. Inspect a section heading such as What I tried and look for `h2`.

You are already reading HTML by matching visible page content to the structure that displays it.

### Make a change that does not touch your files

In the Elements or Inspector panel, find the text inside the article's `h1`. Double-click the text, if your browser supports that, and change it to:

```text
This is a temporary browser edit
```

Press Enter. If direct text editing is unavailable, right-click the element in the panel, choose **Edit as HTML**, and change only its text. Preserve the opening `<h1>` and closing `</h1>` tags.

The visible heading should change. Now reload the page without editing or saving any project file.

The original heading should return. In an ordinary developer-tools session, this edit changes the browser's current document only. It does not update your Markdown file or Hugo template. This exercise assumes you have not configured developer-tool workspaces or persistent local overrides.

> **First checkpoint:** you can inspect the heading, change it temporarily, and explain why a reload restores the source-based result.

This is a useful way to try an idea, but a persistent correction belongs in the appropriate project file. Keep this distinction in mind when someone demonstrates a change using only browser tools.

## 4.2 Read the pieces of an HTML element

HTML stands for **HyperText Markup Language**. Its elements describe the structure and meaning of a document.

Consider an ordinary link:

```html
<a href="https://gohugo.io/documentation/">Hugo documentation</a>
```

| Piece | What it means |
| --- | --- |
| `<a ...>` | Opening tag for a link element |
| `href="..."` | An attribute specifying its destination |
| `Hugo documentation` | The visible link text |
| `</a>` | Closing tag |

Elements can be nested. Close inner elements before their enclosing elements:

```html
<p>Please <strong>check the link</strong> before publishing.</p>
```

Use straight quotation marks around attribute values. Keep spaces between attributes. Indentation makes relationships easier to read but does not create those relationships; the markup does.

Some elements, such as `img`, `meta`, and `link`, are **void elements** and have no closing tag in HTML. Do not add `</img>` after an image. [MDN: basic HTML syntax](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax)

A link's text should help readers predict its destination. A working address paired with a misleading label is still a poor link. [MDN: anchor element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)

## 4.3 Make one persistent HTML change

We will improve the footer so it includes a route to the About page. Because the footer belongs to the shared layout, the change should appear across the site.

Open `layouts/all.html` in your editor. Near the end, find:

```html
<footer>A place to learn, explain, and share.</footer>
```

Replace that entire footer element, and only that element, with:

```html
<footer>
  <p>Learn, review &amp; share.</p>
  <p class="footer-note">
    Read <a href="{{ "about/" | relURL }}">about this notebook</a>.
  </p>
</footer>
```

Save, then check the home page and the first article. Scroll to the bottom. Both should display the new footer. Its About link should open `/about/` in this local setup. Reload the page: the change should remain because you saved it in the source layout.

The paragraphs sit inside `footer`; the link sits inside the second paragraph. That is nesting in a real project change.

The character reference `&amp;` produces a visible ampersand, `&`. For literal angle brackets in ordinary HTML text, `&lt;` and `&gt;` represent `<` and `>`. When writing code examples in Markdown, continue using code fences rather than manually converting all their characters.

The `footer-note` class does not introduce a new visual style by itself. We will use it as a convenient styling target in Chapter 5.

### Why there are braces inside the link

The source contains:

```html
<a href="{{ "about/" | relURL }}">about this notebook</a>
```

The browser should receive a completed link, normally:

```html
<a href="/about/">about this notebook</a>
```

The expression inside `{{ ... }}` is processed by Hugo before the browser receives the page. It adjusts the URL for the site's configured base. It is not browser-side HTML syntax. Keep this supplied expression intact; its full explanation belongs in the templating chapters. [Hugo relative-URL function](https://gohugo.io/functions/urls/relurl/)

> **Second checkpoint:** you made a small source change, predicted which pages it would affect, and verified that the change survives a reload.

## 4.4 Follow the journey from content to browser

The same article appears in several forms. Each has a different role:

| Form | Where you see it | Example |
| --- | --- | --- |
| Content source | `content/articles/first-learning-note/index.md` | A front-matter title and Markdown body |
| Layout source | `layouts/all.html` | `<h1>{{ .Title }}</h1>` and `{{ .Content }}` |
| Generated HTML | The response served by Hugo or files created by a build | `<h1>My first learning note</h1>` followed by paragraphs and sections |
| Live browser document | Elements or Inspector | The browser's current tree of elements, including temporary changes |

The browser's live document is called the **Document Object Model**, or **DOM**. The browser constructs it by parsing HTML. Scripts or developer tools can subsequently change it.

If your browser offers **View Page Source**, open it for the local article and search for its title. This view exposes the HTML response rather than your Hugo template. The Elements panel shows the browser's parsed, live document; it can differ after edits or browser corrections. You may also see development-only code added for Hugo's live reload.

For everyday authoring, make persistent changes in your content or layout source. Editing a generated `public/.../index.html` file is unreliable because another build can overwrite it.

If the screen literally displays `{{ .Title }}`, check that you opened the Hugo preview address rather than double-clicking `layouts/all.html` in the file manager. A browser cannot execute Hugo template expressions.

### Recognise the structure already in your layout

Read `layouts/all.html` from top to bottom. You do not need to change it again yet.

| Part | Job in our starter |
| --- | --- |
| `<!doctype html>` | Selects modern HTML parsing behaviour |
| `<html lang="en">` | Contains the document and declares English as its main language |
| `<head>` | Holds information about the document and linked resources |
| `<meta charset="utf-8">` | Declares the character encoding |
| Viewport `meta` element | Helps the layout use the device's viewport appropriately |
| `<title>` | Supplies the document title normally shown in the browser tab |
| Stylesheet `<link>` | Tells the browser which CSS resource to load |
| `<body>` | Contains the page's displayed structure and content |

The `head` element is different from `header`. The former holds document information; the latter can provide introductory content within the body. Likewise, a document's `title` and its visible `h1` serve different roles even when their wording overlaps.

Within this site's body, you will find:

| Element | Meaning here |
| --- | --- |
| `header` | Site name and introductory navigation |
| `nav` | Major navigation links |
| `main` | This page's primary content |
| `article` | The page's self-contained piece of writing |
| `footer` | Closing site information and the new About link |

These are **semantic elements**: their names communicate purpose. `section` can group a thematic part of a document, typically with a heading; `aside` can hold related supplementary content. Neither is needed just to make a coloured box. Choose markup for its role, then use CSS for appearance. [MDN: structuring documents](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents)

The English language declaration fits our current example. It is not a rule for all pages in the future bilingual site. We will revisit language and direction together in the multilingual chapter.

## 4.5 Connect Markdown to the HTML it creates

Return to your article's Markdown file and compare it with the browser inspector:

| Markdown or metadata | Typical HTML in our starter |
| --- | --- |
| Front-matter `title` | An `h1` inserted by the layout |
| `## What I tried` | An `h2` section heading |
| A paragraph separated by blank lines | A `p` element |
| `**important words**` | A `strong` element |
| `*emphasised words*` | An `em` element |
| A bulleted list | `ul` containing `li` elements |
| A numbered list | `ol` containing `li` elements |
| Text inside single backticks | A `code` element |
| A fenced code block | A block that normally contains `pre` and `code` |
| A Markdown link | An `a` element with `href` |
| A Markdown image | An `img` element with `src` and `alt` |

Inspect one example from each of three rows. You are not expected to rewrite the article in HTML. The value of this comparison is knowing what your authoring choices produce.

### Heading level is a structural choice

Our layout supplies one main `h1` per page. Body sections use `h2`; their subsections use `h3`. This is our straightforward page structure, not a claim that font size determines importance.

Replacing an `h2` with a bold paragraph may preserve a similar appearance but removes a section heading from the document structure. Screen-reader users can use heading navigation, so that difference matters. Conversely, making text an `h2` only to enlarge it gives the document a misleading structure. [MDN: heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)

If you find two large article titles, inspect them and trace each back to its source. A common cause in our project is adding `# My first learning note` to the Markdown body when the layout already renders the front-matter title. Remove the unnecessary body title rather than hiding it with CSS.

## 4.6 Read attributes without guessing

Attributes add information to elements. Three groups matter immediately in this project.

### Destinations and image descriptions

Inspect the screenshot in your first article. Its HTML should contain an image source and alternative text, similar to:

```html
<img src="notebook-preview.png"
     alt="The notebook home page showing its introduction, interests, and next steps">
```

`src` identifies the resource. `alt` supplies a text alternative appropriate to the image's purpose. The visible italic caption you added in Chapter 2 is separate from `alt`.

An informative image needs useful alternative text; a purely decorative image may appropriately have `alt=""`. Omitting the attribute is different from deliberately giving an empty alternative. Check the meaning in context instead of automatically describing every image the same way. [MDN: image element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)

### Identifiers and classes

An `id` identifies one element within a page. Its value should be unique in that document. The same value can appear on different pages: each page has its own document. A fragment such as `#main` can point to an element with `id="main"`. [MDN: id attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)

A `class` assigns a reusable label. Multiple elements may share the same class, and an element can have more than one class. CSS and scripts can use these labels to select elements. A class name does not itself create styling. [MDN: class attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)

In our site, `class="site-name"` already has a stylesheet rule, while the new `class="footer-note"` has no specific rule yet. Neither needs to be globally unique.

### Existing accessibility-related attributes

The navigation's `aria-label="Main navigation"` supplies an accessible name for that navigation region. Our `main` element has `tabindex="-1"`, which makes it focusable without adding it as an ordinary stop in sequential Tab navigation. This supports the skip-link arrangement in the starter.

Keep these attributes while making unrelated edits. Use native HTML elements appropriately and understand the purpose of any accessibility attribute you add. Adding attributes at random is not an accessibility review.

## 4.7 Trace and repair the skip link

The first link in the layout is:

```html
<a class="skip-link" href="#main">Skip to content</a>
```

Its destination is the existing element:

```html
<main id="main" tabindex="-1">
```

Together, they offer a route past repeated navigation to the page's content. The stylesheet keeps the link out of view until it receives focus.

Reload the home page and place keyboard focus in the page. Press Tab from the beginning of the page's focus order until Skip to content appears. Browser chrome can receive focus first; keep track of where focus is rather than assuming the first keypress always reaches the page. Activate the link with Enter. The address should acquire `#main`, and the browser should move to the main-content target. You may need a longer page to notice much scrolling.

Now make a deliberate source mistake. In `layouts/all.html`, change only the skip link's destination from `#main` to `#missing-main`. Do not change the `main` element's identifier. Save and reload.

The link still looks like a link. Its activation may add `#missing-main` to the address, but no element with that identifier exists. Hugo may build successfully because a successful template render does not prove that every fragment has a matching target.

Use the inspector's search facility to look for `id="missing-main"`. Compare the result with `id="main"`. Repair the source link by restoring `href="#main"`, save, and repeat the keyboard check.

The lesson is specific: matching words in the address bar are not enough. Verify that the target exists and that the route is useful.

## 4.8 Know which source file to edit

When something looks wrong, first decide where the information came from:

| Observation | Source to inspect first |
| --- | --- |
| The article's title is wrong. | Its front-matter `title` |
| A body heading or sentence is wrong. | The page's Markdown body |
| A main navigation label is wrong on every page. | The navigation block in `layouts/all.html` |
| The About link in the new footer is wrong everywhere. | The footer block in `layouts/all.html` |
| The screenshot's alternative text is wrong. | The image syntax in the article's Markdown |
| The site name is wrong everywhere. | `title` in `hugo.toml` |
| The font, colour, or spacing is wrong. | `static/css/site.css`, after checking the underlying HTML |
| An inspector-only edit disappears. | Make the intended change in its persistent source file. |

Do not put the same paragraph into both the Markdown body and the shared layout. The layout would then repeat it across unrelated pages. Do not move page-specific writing into the layout just because the browser inspector made it look like one continuous HTML file.

Raw HTML embedded in Markdown also depends on the generator's rendering configuration. For this chapter, put the footer HTML in the supplied layout and keep ordinary page writing in Markdown. There is no need to change raw-HTML rendering settings.

## 4.9 Optional recognition: tables and form controls

You will encounter more HTML in later chapters and in agent-generated proposals. Recognise the purpose of these examples; do not add them to the project for this exercise.

### A small data table

```html
<table>
  <caption>Notebook content</caption>
  <thead>
    <tr><th scope="col">Section</th><th scope="col">Purpose</th></tr>
  </thead>
  <tbody>
    <tr><td>Articles</td><td>Learning notes</td></tr>
    <tr><td>Projects</td><td>Descriptions of ongoing work</td></tr>
  </tbody>
</table>
```

`tr` identifies a row; `th` a header cell; `td` a data cell. The caption identifies the table, and `scope="col"` associates each header with its column. Tables are useful for tabular information, not for positioning the page's navigation and content. [MDN: table element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)

### A labelled input

```html
<label for="contact-email">Email address</label>
<input id="contact-email" name="email" type="email">
```

The label's `for` value matches the input's `id`. The `name` can identify the value when form data is submitted; it serves a different purpose from `id`. A placeholder is not a substitute for a persistent label. [MDN: label element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)

This fragment is not a working contact system. An actual form needs a deliberate submission route and processing arrangement. Its HTML alone does not deliver messages, store records, or establish that submitted information is safe. We will build a complete modest integration in the interaction chapter. [MDN: form element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)

## 4.10 Judge an agent's proposed change, then make your own

Consider these two illustrative proposals. No agent account is needed.

| Proposal | What you should examine |
| --- | --- |
| Replace the article's `h1` with a paragraph to reduce its size. | The goal concerns appearance, but the change removes the main heading. Keep the heading and address size through CSS later. |
| Shorten every link label to “Read more”. | Check whether visitors can still distinguish the destinations, especially when encountering links outside their surrounding paragraphs. |

Ask an agent to explain which files and elements it intends to change and why. Compare that explanation with the rendered result. A confident description does not replace inspecting the markup or checking keyboard behaviour.

For an optional writing exercise, describe how you would request the footer change we made: identify the file, the existing block, the required wording, the About destination, and what must remain intact. We will turn instructions like this into practical agent tasks later.

### Make one independent change and preserve it

Change only the first paragraph of your new footer to a short sentence that fits your notebook. Preserve the About link, the `footer-note` class, and the rest of the layout. If you use an ampersand in HTML text, practise writing it as `&amp;`.

Then:

1. Check the footer on Home, About, and your first article.
2. Activate its About link from the article.
3. Reload and confirm the source change persists.
4. Confirm the repaired skip link still targets `main`.

Save all files, stop the preview, and copy the project to a sibling folder named `my-knowledge-site-ch04-backup`. Continue using the original project for Chapter 5.

Only `layouts/all.html` needs a permanent change in this chapter. The temporary inspector edit does not belong in any file. The intentionally broken skip-link destination must be repaired before creating the checkpoint.

## Completion check

- [ ] I can locate the article's `h1`, a body heading, a link, and its image in the inspector.
- [ ] I can explain why a temporary browser edit disappears on reload.
- [ ] I can recognise elements, attributes, nesting, and void elements.
- [ ] I can distinguish the page's Markdown from its shared layout and generated HTML.
- [ ] My updated footer appears across the site and its link works.
- [ ] The skip link and main-content identifier match again.
- [ ] I know which source file to inspect for common content and layout problems.
- [ ] I saved a working Chapter 4 checkpoint.

Chapter 5 will use CSS to change appearance deliberately. The `footer-note` class, browser inspector, and structural distinctions you learned here will give those styling changes a clear foundation.

## Troubleshooting when you need it

| Symptom | Check |
| --- | --- |
| Developer tools select the wrong element. | Use the element picker again or expand the nearby nodes in Elements/Inspector until you find the relevant text. |
| The inspector's heading differs from the source file. | Reload to discard temporary DOM edits; confirm you are previewing the same project and page. |
| The footer changes on every page. | That is expected: all seven authored pages currently use the shared layout. |
| The footer change disappears after a reload. | You may have edited only the browser DOM. Save the change in `layouts/all.html`. |
| Hugo reports a template error near the new link. | Restore the exact `{{ "about/" | relURL }}` expression, keeping both brace pairs and straight quotes. |
| The layout displays template braces literally. | Open the Hugo server address, not the layout file directly. |
| The new class produces no visible change. | No class-specific CSS rule has been added yet. A class is a label, not a style definition. |
| `&amp;` appears literally on the page. | Check whether you double-escaped it as `&amp;amp;` or placed the example inside a code block. |
| The address ends in `#missing-main` but nothing useful happens. | Restore the skip link to `#main`; a fragment needs a corresponding element identifier. |
| The page still looks acceptable after a markup mistake. | Browsers can recover from malformed HTML. Inspect the resulting structure rather than treating appearance as proof of correctness. |

## Completed layout for comparison

Use this as a recovery reference for `layouts/all.html` if an edit went wrong. It preserves Chapter 3's navigation and includes the new footer. Retain your own accurate footer wording if you completed the independent exercise.

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
    <article>
      <h1>{{ .Title }}</h1>
      {{ .Content }}
    </article>
  </main>
  <footer>
    <p>Learn, review &amp; share.</p>
    <p class="footer-note">
      Read <a href="{{ "about/" | relURL }}">about this notebook</a>.
    </p>
  </footer>
</body>
</html>
```

---

## Editorial note for the author (remove before publication)

This chapter continues the seven-page project from Chapter 3. It prioritises inspection and source tracing over adding features. The only required persistent modification is the shared footer; the optional tables and form-control fragments are recognition examples, not project additions. The complete layout is a recovery reference, not a replacement for the earlier content files.

Browser menu names vary, so provide screenshots for the final supported browser while retaining the Elements/Inspector terminology. DOM editing assumes ordinary developer tools without persistent overrides. Keyboard behaviour and accessibility need direct browser checks; a successful Hugo build does not validate them.

Documentation was consulted on 17 September 2026. The project was reconstructed from Chapters 1–3 and built with Hugo 0.150.0 on Linux. All seven authored pages passed checks for local links, image and stylesheet references, fragment targets, unique identifiers, and the expected footer at both a domain root and a `/my-knowledge-site/` base path. The completed layout was checked to preserve the earlier layout outside the footer. The deliberately broken skip-link fragment still allowed a successful build, as described; the correct destination was then restored. A small image fixture stood in for the reader's screenshot during resource checks.

An executable browser was unavailable for automated checks, so the developer-tools editing and keyboard-focus exercises have not been browser-tested in this draft. Those checks, a representative beginner trial, and cross-platform review remain necessary before publication. These structural checks are not a complete accessibility audit.
