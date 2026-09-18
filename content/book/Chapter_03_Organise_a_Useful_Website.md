---
title: "Chapter 3 — Organise a Useful Website"
weight: 3
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*Checked with Hugo 0.150.0 (standard edition) on Linux. No beginner trial or browser review yet.*

Your website now has a home page and an article. You know how to edit both, but a new visitor does not know where your files are. They need clear routes through the information you have published.

In this chapter, you will add an About page, give Articles a useful landing page, introduce a Projects section, and collect a few resources. Then you will replace the small home-page navigation with links that work across the website.

The aim is a site whose organisation makes sense to someone who has never seen your project folder. Every destination we add will contain something useful, even if it is only a short explanation and one carefully chosen link.

## What you will be able to do

By the end, you should be able to:

- Choose pages and section names around a visitor's needs.
- Distinguish an individual page from a section landing page and use the appropriate index filename.
- Connect the home page, sections, and individual items with working links and shared navigation.
- Check a visitor's route through the site and recover from a change that breaks an address.

## 3.1 Start with the website you already have

Continue in the original `my-knowledge-site` folder. Your Chapter 2 article should be marked `draft: false`, have its screenshot beside it, and be linked from the home page.

The files we depend on are:

| File | Existing purpose |
| --- | --- |
| `content/_index.md` | Personal introduction and Latest writing link |
| `content/articles/first-learning-note/index.md` | First article |
| `content/articles/first-learning-note/notebook-preview.png` | Article screenshot |
| `layouts/all.html` | Shared page structure and navigation |
| `static/css/site.css` | Styling, including Chapter 2's image sizing |
| `hugo.toml` | Basic site settings |

Keep the Chapter 2 backup outside your active project. If you have not made it, stop the preview, save your files, and copy the project to a sibling folder named `my-knowledge-site-ch02-backup` before continuing.

Start the ordinary preview from the folder containing `hugo.toml`:

```text
hugo server
```

Open the address reported in the terminal, normally `http://localhost:1313/`. Follow the Latest writing link and confirm the article still works. Return to the home page.

We will use normal, non-draft pages for the short examples in this chapter. They are local practice content and must be reviewed before any later public deployment. No new installation is needed. The examples were checked with Hugo 0.150.0 on Linux, matching the preceding chapters' test baseline.

## 3.2 Add an About page first

A new visitor may want to know what your notebook is for. Give them a short answer.

Inside `content`, create an `about` folder and a file named `index.md` inside it. Its path is `content/about/index.md`.

Copy this complete file, then replace the introduction with accurate wording about yourself or your work:

```markdown
---
title: "About this notebook"
draft: false
---

This notebook collects things I am learning and projects I am developing.

## What you can find here

I write short explanations, describe small projects, and collect resources that help me learn.

## Where to begin

Read [my first learning note](../articles/first-learning-note/) for an example of how I record what I have tried.
```

Save and open:

```text
http://localhost:1313/about/
```

Use your actual server port if it is different. Check the title, read the text, and follow the link to the article.

You have added a new destination using skills from Chapter 2. It does not need a new stylesheet or a new HTML layout.

> **First checkpoint:** a visitor who opens the About page can understand the site's purpose and reach an example of its writing.

## 3.3 Decide what belongs where

Before adding more folders, write a short answer to these questions in a learning note outside the project:

1. Who is this website primarily for?
2. What should that person be able to find or do?
3. Which existing content answers those needs?

For our example, the primary visitor is a fellow learner who wants to understand an idea, inspect a small project, or find a useful reference. That gives us a manageable structure:

| Visitor's question | Destination | What belongs there |
| --- | --- | --- |
| What is this website, and where should I begin? | Home | A brief introduction and selected starting points |
| Who is writing, and what is the purpose? | About | Relevant background and the notebook's scope |
| What can I learn here? | Articles | Explanations and learning notes |
| What has the author been working on? | Projects | Descriptions of work, its status, and related evidence |
| Where can I read more? | Resources | A small collection of links with explanations |

These names are a starting point, not a universal formula. A course website might use Lessons and Exercises; a research group might use Research and Publications. Choose words your intended visitors recognise.

Avoid adding a menu item simply because you might write something for it later. A smaller site with useful destinations is easier to understand than a large collection of empty pages.

The organisation of information and the routes connecting it are often called **information architecture**. At this scale, the table above is enough planning. You do not need a complex diagram to begin.

## 3.4 Make Articles a useful landing page

Your article already exists under `content/articles/`. In Chapter 2, visiting `/articles/` did not show an article list because our minimal layout has no listing loop.

We can make that address useful with ordinary Markdown. Create `content/articles/_index.md`. Notice the underscore: this file describes the section that contains articles, rather than a single article at the end of the structure.

Use this complete content:

```markdown
---
title: "Articles"
draft: false
---

Short notes about ideas I have tried and things I am learning.

## Start reading

- [My first learning note](first-learning-note/) — Editing a page, checking the result, and recording what changed.
```

Save and open:

```text
http://localhost:1313/articles/
```

The page now explains what the section contains and provides a link to the article. Click it.

Hugo recognises top-level content directories as sections. Adding `_index.md` gives this section its own title and introductory content. Hugo also supports nested sections, but we will keep our structure shallow. [Hugo sections](https://gohugo.io/content-management/sections/)

The list you just wrote is **manual**. Adding another article file will not automatically add a bullet here. For now, maintain the list yourself. The template chapters will show how to generate such lists from content.

### Keep the two index filenames distinct

| File | Meaning in this project |
| --- | --- |
| `content/_index.md` | Home-page content |
| `content/articles/_index.md` | Articles section introduction and manual list |
| `content/articles/first-learning-note/index.md` | One article and its associated image bundle |
| `content/about/index.md` | One standalone About page |

Do not rename the section's `_index.md` to `index.md`. A leaf bundle built around `index.md` has different rules for the files beneath it; the two names are not interchangeable. [Hugo page-bundle documentation](https://gohugo.io/content-management/page-bundles/)

## 3.5 Add Projects and a Resources page

The website itself is a small project you are developing. You can describe its purpose and current state without claiming that it is finished.

Create a `projects` folder inside `content`. Then create the two files below.

### Section page: `content/projects/_index.md`

```markdown
---
title: "Projects"
draft: false
---

Small projects I am developing, with notes about their purpose and progress.

## Current work

- [My knowledge notebook](learning-notebook/) — A website for organising explanations, project notes, and useful resources.
```

### Project page: `content/projects/learning-notebook/index.md`

```markdown
---
title: "My knowledge notebook"
draft: false
---

## Purpose

I am building a small website where readers can find my learning notes and follow my projects.

## Current status

This is a work in progress. I have a home page and an article, and I am improving the site's organisation.

## What I have learned

I can edit Markdown, preview a page, and check links and images.

Read [my first learning note](../../articles/first-learning-note/) for an example.

[Back to Projects](../)
```

Create the `learning-notebook` folder before saving its `index.md`. Save both files, open `/projects/`, follow its project link, and use Back to Projects to return.

The project description is intentionally short. Change any sentence that does not match what you have actually done. A statement such as “work in progress” helps readers interpret the page accurately.

Avoid making a copy of the first article inside Projects. The article explains an experience; the project page describes the wider work and links to that experience. Keeping one article avoids maintaining two copies of the same text.

### A small Resources page

For the moment, Resources can be one page containing a few references. It does not need a section full of individual resource pages.

Create `content/resources/index.md`:

```markdown
---
title: "Resources"
draft: false
---

References that support the work recorded in this notebook.

## Website publishing

- [Hugo documentation](https://gohugo.io/documentation/) — The official reference for Hugo configuration, content, and templates.
- [Hugo page bundles](https://gohugo.io/content-management/page-bundles/) — An explanation of grouping a page with related resources.

## Examples from this notebook

- [My first learning note](../articles/first-learning-note/) — A practical record of editing and checking content.
- [My knowledge notebook project](../projects/learning-notebook/) — The purpose and current state of this website.
```

Save and open `/resources/`. Follow each link. The external links leave your site; the internal examples stay within it.

The explanation after each link tells the visitor why it is included. That is more useful than collecting many unexplained URLs. When maintaining a resource list, keep links you have checked and can describe accurately.

## 3.6 Add navigation and clear starting points

The navigation supplied in Chapter 1 links to Home and two headings on the home page. Our site now needs routes to its main destinations.

Open `layouts/all.html`. Find the existing block beginning with `<nav aria-label="Main navigation">` and ending with `</nav>`.

Replace **that block only** with:

```html
<nav aria-label="Main navigation">
  <a href="{{ "" | relURL }}">Home</a>
  <a href="{{ "about/" | relURL }}">About</a>
  <a href="{{ "articles/" | relURL }}">Articles</a>
  <a href="{{ "projects/" | relURL }}">Projects</a>
  <a href="{{ "resources/" | relURL }}">Resources</a>
</nav>
```

Save the file and refresh the preview. The new navigation should appear on the home page, article, and new pages because they all use the shared layout.

Do not replace the whole layout with this fragment. Keep the surrounding document, the stylesheet link, the Skip to content link, the main content area, and the footer.

You need only recognise two things today: the words between the link tags are the visible labels, and the quoted paths inside the template expressions identify the destinations. `relURL` makes those links relative to the configured site base, including a hosting subdirectory. The paths supplied to it here deliberately have no leading slash. [Hugo relative-URL function](https://gohugo.io/functions/urls/relurl/)

We will explain the HTML in Chapter 4 and the template expressions in the later templating chapters. This supplied replacement is a small, controlled change rather than a requirement to learn the full template language now.

### Three distinct things that work together

| Thing | What it does | What it does not do by itself |
| --- | --- | --- |
| Content files and folders | Supply pages and their organisation | Decide which destinations appear in the navigation |
| A navigation link | Offers a route to a destination | Create the destination page |
| A shared layout | Renders repeated page structure | Automatically infer the best navigation for visitors |

Hugo has a menu system that can separate navigation data from its rendering. We will use more structured approaches when we have enough template knowledge. For this exercise, the five explicit links make the relationship visible and easy to inspect. [Hugo menus](https://gohugo.io/content-management/menus/)

The My interests and Next steps sections can stay on your home page. We are removing their top-navigation entries, not deleting the content or changing its existing heading identifiers.

### Give the home page clear starting points

A visitor may scan the body of the home page before noticing its navigation. Help them choose a useful next step.

In `content/_index.md`, preserve your existing introduction, My interests, Next steps, and Latest writing. Add this section at the end:

```markdown
## Explore the notebook

- [About](about/) — What this notebook is for.
- [Articles](articles/) — Explanations and learning notes.
- [Projects](projects/) — Work in progress and what I have learned from it.
- [Resources](resources/) — References and useful examples.
```

Save and inspect the home page. These links repeat some navigation destinations, but add context. They do not copy the destination pages' full content.

A home page should help people begin. As the site grows, you can shorten the introduction or select a smaller set of featured items if the page becomes crowded. You do not need to show every future article on the home page.

> **Second checkpoint:** the site now has consistent navigation and useful landing pages, and its original article remains reachable at its existing address.

## 3.7 Choose stable names, addresses, and organising tools

Use short, descriptive folder names. The examples use lowercase letters and hyphens: `first-learning-note` and `learning-notebook`. This is a practical convention for our English-language project, not a rule that all websites must use English URLs.

Avoid names such as `page2`, `new-final`, or `test-copy` for destinations you intend to keep. They say little to a visitor and become confusing as the site grows.

Here is the completed map. Preview paths are relative to the local site address.

| Content source | Preview path | Purpose |
| --- | --- | --- |
| `content/_index.md` | `/` | Home |
| `content/about/index.md` | `/about/` | About |
| `content/articles/_index.md` | `/articles/` | Article landing page |
| `content/articles/first-learning-note/index.md` | `/articles/first-learning-note/` | First article |
| `content/projects/_index.md` | `/projects/` | Project landing page |
| `content/projects/learning-notebook/index.md` | `/projects/learning-notebook/` | Project description |
| `content/resources/index.md` | `/resources/` | Resource collection |

Our Markdown links are relative to the page where they appear. For example, `learning-notebook/` works from the Projects landing page, while `../projects/learning-notebook/` works from Resources. Copying a relative link to a page at another location can change what it points to.

### A displayed title and a URL can change independently

In `content/about/index.md`, change the title from “About this notebook” to “Why I keep this notebook”. Save and reopen `/about/`.

The page heading changes, but the address remains `/about/` in our current configuration. The navigation still says About because its label was written separately in the layout. Restore the original title or keep the new one if it suits your writing.

Renaming a content folder is different: in this project it changes the corresponding URL. Once a site has public readers, existing bookmarks and inbound links matter. Later chapters will cover redirects and planned migrations.

### Sections, tags, and categories: different organising tools

Sections answer “where does this item belong in the site?” Tags and categories can describe subjects shared by content in different locations.

For our growing notebook:

| Organising choice | Example | Use |
| --- | --- | --- |
| Section | Articles | Groups a kind of content and gives it a landing page |
| Category | Web publishing | A broad subject grouping, if we choose to use one |
| Tag | Markdown | A narrower topic that could connect an article and a project |

Hugo calls such subject groupings **taxonomies**. Categories and tags are conventional names; Hugo does not force categories to be broad or tags to be narrow. That distinction is an editorial convention we would adopt and document. [Hugo taxonomies](https://gohugo.io/content-management/taxonomies/)

We will configure and display these labels in later content-modelling and template exercises. Simply adding a `tags` field does not make our current minimal layout display tag badges or useful linked lists. For this chapter, sections and explicit links are sufficient.

Resist creating a label for every word in an article. Before introducing a grouping, decide how it will help a visitor find related material and who will keep its names consistent.

## 3.8 Find and repair a broken route

This exercise is for your local practice copy. Do not perform unplanned moves on a public site.

First open `/projects/` and confirm that My knowledge notebook opens the correct project page. Then:

1. Stop the preview server with Ctrl+C.
2. In the editor, rename the folder `content/projects/learning-notebook` to `content/projects/learning-notebook-test`. Keep its `index.md` inside it.
3. Leave the links in the Projects and Resources pages unchanged.
4. Restart `hugo server`, open `/projects/`, and click its project link.

The link still points to the old address, so a freshly generated preview should no longer find the project there. Open `/projects/learning-notebook-test/` directly to confirm that the page exists at its new address.

The content has not been deleted. Its destination has moved while the links have stayed the same. Hugo can build successfully even when a manually written link no longer reaches a page.

If the old page remains visible because of cached or previously generated output, do not treat that as proof the route is correct. Use a fresh browser request and restart the preview with in-memory rendering for this check:

```text
hugo server --renderToMemory
```

Stop any already running server before issuing that command. It serves newly generated pages from memory, avoiding an old generated file as the explanation for an apparent success.

For this exercise, recover by restoring the original destination:

1. Stop the server.
2. Rename the folder back to `learning-notebook`.
3. Restart the normal `hugo server` preview.
4. Test the project links from both Projects and Resources.

We deliberately keep the original address. If a real move were needed, we would identify all affected links and consider redirects as part of the change.

## 3.9 Test the site as a visitor

Open a new browser tab at the home page. Follow each route below using links rather than typing every destination:

| Visitor task | Route to try | What success looks like |
| --- | --- | --- |
| Understand the purpose | Home → About | A clear explanation and a useful example link |
| Read something | Home → Articles → first learning note | The right article, including its screenshot |
| Inspect a project | Home → Projects → My knowledge notebook | An accurate purpose and status, plus related reading |
| Find a reference | Home → Resources → Hugo documentation | The intended external reference opens |
| Recover orientation | Open the article directly, then use navigation | Main site destinations are available without starting at Home |

Use the keyboard for one route as well. Press Tab to move through links, observe the visible focus indicator supplied by the stylesheet, and press Enter on the link you want. The first link should offer Skip to content. It remains useful even though we changed the main navigation.

Resize the browser to a narrow window. The existing navigation styling should let its links wrap rather than forcing a single long row. Check this in your actual browser; an automated build cannot establish that the site is comfortable to use.

If a route is confusing, change its label or explanation before adding more content. An accessible destination is not necessarily an understandable one.

## 3.10 Try an independent improvement and preserve the result

Choose one of these small tasks:

- Add a second resource you have read, explain its relevance, and test its link.
- Improve the About page so it names a specific audience and explains what they can expect.
- Add one accurate sentence to the project page describing its next planned improvement, clearly distinguishing planned work from completed work.

Do not create new sections for this exercise. Practise making the existing structure more useful.

An optional AI-assisted planning task is to supply the visitor questions and current navigation labels to a chatbot and ask it to identify one confusing label. Ask for reasons, not a redesigned website. Decide whether the suggestion matches your intended audience before editing anything. Agent installation and direct file access still come later.

Explain in a learning note:

1. Why does Articles have `_index.md` while About has `index.md`?
2. Why did one navigation edit affect several pages?
3. Why does creating a new page not automatically add a link to our manual lists?
4. Why is changing a title usually a smaller routing change than renaming a folder in this setup?

### Preserve the completed structure

Save your files and stop the preview. Copy the active project to a sibling folder named `my-knowledge-site-ch03-backup`. Keep it outside the project and continue using the original folder for Chapter 4.

The required changes are:

| File | Change |
| --- | --- |
| `content/about/index.md` | New About page |
| `content/articles/_index.md` | New section introduction and manual article link |
| `content/projects/_index.md` | New section introduction and manual project link |
| `content/projects/learning-notebook/index.md` | New project description |
| `content/resources/index.md` | New resource collection |
| `content/_index.md` | Added Explore the notebook section |
| `layouts/all.html` | Replaced only the main navigation block |

Your existing article, screenshot, configuration, and stylesheet remain in place. If you chose an independent improvement, its content may differ from the examples; its links should still work.

## Completion check

- [ ] Every main navigation item opens a useful page in the normal preview.
- [ ] Articles and Projects have working landing pages.
- [ ] The original article still uses its Chapter 2 address and displays its image.
- [ ] My manual lists link to the correct items.
- [ ] I have distinguished site structure, navigation, and subject labels.
- [ ] I restored the original project folder name after the recovery exercise.
- [ ] I followed the visitor routes, including one with the keyboard.
- [ ] I saved a working Chapter 3 checkpoint.

Chapter 4 will inspect the HTML generated by these pages. We will connect the content you write, the navigation fragment you replaced, and the structure the browser actually receives.

## Troubleshooting when you need it

| Symptom | Check |
| --- | --- |
| Articles has a heading but no links. | Confirm you saved the supplied body in `content/articles/_index.md`. This starter does not generate a list automatically. |
| An article becomes unavailable after creating the section page. | Confirm the section file is `_index.md`, not `index.md`, and that the article is still in its original folder. |
| An item exists but is not shown in the navigation. | Navigation entries are explicit in `layouts/all.html`; adding a content file does not edit that block. |
| An item appears in navigation but returns a 404. | Check its destination file, spelling, draft status, and the path inside the navigation expression. |
| Only the navigation appears and the rest of the page is gone. | You may have replaced the whole layout with the fragment. Restore `layouts/all.html` from the Chapter 2 backup, then replace only its `<nav>...</nav>` block. |
| A changed navigation label still opens the old destination. | Labels and destinations are separate. Inspect the link's path as well as its visible wording. |
| A link contains the right words but opens the wrong relative path. | Check the page from which it is followed. `../` moves up from that page's URL, not from the project root. |
| The old project page appears during the rename exercise. | Check the URL, make a fresh request, and use the in-memory preview described in the exercise to rule out stale generated output. |
| A new section appears twice on the home page. | Add the Explore section once. Remove only an accidental duplicate, preserving your earlier personalised content. |
| The article screenshot no longer matches the site's navigation. | It records the Chapter 2 state. That is acceptable as a historical screenshot; capture a new one only if you intend the article to describe the current appearance. |

---

## Editorial note for the author — remove before publication

This chapter continues the saved Chapter 1 starter and Chapter 2 article rather than assuming features supplied by an external theme. Section lists are written in Markdown. The navigation change is one supplied block; Hugo's menu configuration, template iteration, active-menu state, and taxonomy rendering are deliberately deferred until their prerequisites have been introduced.

The five new content files and all required edits appear inline. No extra asset download is necessary. Preserve reader customisations and the existing article URL when producing companion checkpoints. A packaged Chapter 2 baseline would make restarting easier; it is not an assumed download in these instructions.

Official documentation was consulted on 17 September 2026. Validation reconstructed the project from the current saved Chapters 1 and 2 and extracted this chapter's five new Markdown files, navigation fragment, and home-page addition directly from the draft. Hugo 0.150.0, standard edition, on Linux amd64 built the result with warnings treated as failures.

Checks passed for all seven authored pages, one main heading per page, identical five-link main navigation, internal link destinations, fragment targets, stylesheet paths, and the existing article image. Those checks covered both a domain-root base URL and a `/my-knowledge-site/` base URL. The image was represented by a small generated PNG for path verification, not an actual screenshot or an additional deliverable.

A separate build confirmed that changing the About title retained its address. A running in-memory preview served all seven routes. Renaming the project folder made the old address return 404 and the new address return 200; restoring the folder restored the original route. Checks used server responses and generated HTML. Visual browser inspection, actual keyboard interaction, operating-system walkthroughs, and a representative beginner trial have not been performed and remain necessary before publication.
