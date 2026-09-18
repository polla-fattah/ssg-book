---
title: "Organise a Useful Website"
description: "Chapter 3: an About page, sections, navigation, and addresses chosen around what a visitor needs."
book_number: "3"
weight: 4
---

# Organise a Useful Website

Static Site Generators in the Age of AI

**Chapter 3**

Polla Fattah

---

## Today's goal

You know where your files are. **A new visitor does not.**

Give them clear routes through the site:

- An **About** page
- Landing pages for **Articles** and **Projects**
- A short **Resources** page
- Navigation that works on every page

Every destination must contain something useful.

---

## By the end of today you can

- **Choose** pages and section names around a visitor's needs
- **Distinguish** a single page from a section landing page, and pick the right index filename
- **Connect** home, sections, and items with working links and shared navigation
- **Check** a visitor's route, and recover when a change breaks an address

---

## Start from Chapter 2

Continue in `my-knowledge-site`. Your article should be `draft: false`, with its screenshot beside it, and linked from the home page.

Keep `my-knowledge-site-ch02-backup` outside the project, then start the **ordinary** preview:

```text
hugo server
```

Follow the Latest writing link and check the article still works.

---

## Add an About page

Create `content/about/index.md`, in your own words:

```markdown
---
title: "About this notebook"
draft: false
---

This notebook collects what I learn and what I build.

Read [my first learning note](../articles/first-learning-note/).
```

---

## Decide what belongs where

Who is the site for, and what should they find? For our fellow learner:

| Visitor's question | Destination |
| --- | --- |
| What is this site, and where do I begin? | Home |
| Who is writing, and why? | About |
| What can I learn here? | Articles |
| What is the author working on? | Projects |
| Where can I read more? | Resources |

---

## No empty destinations

> A smaller site with useful destinations beats a large collection of empty pages.

- This planning is called **information architecture**
- Choose words your visitors **recognise**: a course might use Lessons; a research group, Publications
- Do not add a menu item for something you **might** write later

---

## Make Articles a landing page

Create `content/articles/_index.md`, with an **underscore**:

```markdown
---
title: "Articles"
draft: false
---

- [My first learning note](first-learning-note/)
```

Open `/articles/`. The list is **manual**: a new article will not add itself.

---

## Two index filenames

| File | Meaning |
| --- | --- |
| `content/_index.md` | The home page |
| `content/articles/_index.md` | The Articles section's introduction |
| `content/articles/first-learning-note/index.md` | One article with its image |
| `content/about/index.md` | One standalone page |

`_index.md` is a **section** that contains pages; `index.md` is **one page**. They are **not interchangeable**.

---

## Add a Projects section

Create `content/projects/_index.md` with a manual list, like Articles. Then the project page, `content/projects/learning-notebook/index.md`:

```markdown
## Current status

This is a work in progress.

[Back to Projects](../)
```

Describe only what you have **actually done**.

---

## Link, do not copy

- The article explains **an experience**
- The project page describes **the wider work** and links to that experience

```markdown
Read [my first learning note](../../articles/first-learning-note/).
```

One article, one copy: nothing to keep in sync.

---

## A small Resources page

`content/resources/index.md` is a single page, not a section:

```markdown
- [Hugo documentation](https://gohugo.io/documentation/):
  The official reference for Hugo.
- [My first learning note](../articles/first-learning-note/):
  A practical record of editing and checking content.
```

- The sentence after each link says **why it is there**
- External links leave your site; internal ones stay within it
- Keep only links you have **checked**

---

## Replace the navigation

In `layouts/all.html`, replace **only** the `<nav>...</nav>` block:

```html
<nav aria-label="Main navigation">
  <a href="{{ "" | relURL }}">Home</a>
  <a href="{{ "about/" | relURL }}">About</a>
  <a href="{{ "articles/" | relURL }}">Articles</a>
  <a href="{{ "projects/" | relURL }}">Projects</a>
  <a href="{{ "resources/" | relURL }}">Resources</a>
</nav>
```

Keep everything else in the layout exactly as it is.

---

## What to notice in that block

- The words between the tags are the **visible labels**
- The quoted paths are the **destinations**, with no leading slash
- `relURL` keeps links working when the site lives in a subfolder

One edit, **every page** changes: they all share the layout.

HTML comes in Chapter 4, templates later.

---

## Three things that work together

| Thing | What it does | What it does not do |
| --- | --- | --- |
| Content files | Supply pages and their organisation | Choose the navigation |
| A navigation link | Offers a route to a destination | Create the page |
| A shared layout | Repeats the page structure | Decide what visitors need |

My interests and Next steps stay on the home page; only their menu entries go.

---

## Give the home page starting points

At the end of `content/_index.md`, keeping everything else:

```markdown
## Explore the notebook

- [About](about/): What this notebook is for.
- [Articles](articles/): Explanations and learning notes.
- [Projects](projects/): Work in progress and what I learned.
- [Resources](resources/): References and useful examples.
```

These repeat the navigation, but **add context**. A home page helps people begin; it does not list everything.

---

## The completed map

| Source, inside `content/` | Preview path |
| --- | --- |
| `_index.md` | `/` |
| `about/index.md` | `/about/` |
| `articles/_index.md` | `/articles/` |
| `projects/_index.md` | `/projects/` |
| `projects/learning-notebook/index.md` | `/projects/learning-notebook/` |
| `resources/index.md` | `/resources/` |

---

## Titles and addresses change independently

Change the About title to "Why I keep this notebook" and reload.

- The **heading** changes
- The **address** stays `/about/`
- The **menu label** stays About: it lives in the layout

Renaming a **folder** changes the address. Once a site has readers, that breaks their bookmarks and links.

Relative links depend on **where they are followed from**.

---

## Sections, categories, and tags

| Tool | Example | Use |
| --- | --- | --- |
| Section | Articles | A kind of content, with a landing page |
| Category | Web publishing | A broad subject, if we choose one |
| Tag | Markdown | A narrow topic that links an article and a project |

Hugo calls subject groupings **taxonomies**. Broad versus narrow is **our convention**, not Hugo's rule.

Add a label only when it helps a visitor find related material.

---

## Break a route on purpose

1. Stop the server with **Ctrl+C**
2. Rename `content/projects/learning-notebook` to `learning-notebook-test`
3. Leave the links in Projects and Resources unchanged
4. Restart `hugo server` and click the project link

The page **still exists**, at `/projects/learning-notebook-test/`. The links point to where it **used to be**, yet Hugo builds without complaint.

---

## Rule out stale pages, then recover

If the old page still appears, do not trust it. Restart with:

```text
hugo server --renderToMemory
```

Then recover:

1. Stop the server and rename the folder back to `learning-notebook`
2. Restart `hugo server`
3. Test the project links from **both** Projects and Resources

A real move needs every affected link found, and **redirects**.

---

## Test the site as a visitor

| Task | Route |
| --- | --- |
| Understand the purpose | Home, About |
| Read something | Home, Articles, first learning note |
| Inspect a project | Home, Projects, My knowledge notebook |
| Find a reference | Home, Resources, Hugo documentation |
| Recover orientation | Open the article directly, then use the menu |

Try one route with **Tab** and **Enter**, then narrow the window.

---

## Try it yourself

Choose **one**:

- Add a resource you have read, say why it matters, test the link
- Make About name its audience and what they can expect
- Add the project's next step, clearly marked as planned

> An accessible destination is not necessarily an understandable one.

---

## Explain it to yourself

- Why does Articles have `_index.md` while About has `index.md`?
- Why did one navigation edit affect several pages?
- Why does a new page not appear in our manual lists?
- Why is changing a title a smaller change than renaming a folder?

---

## Save your checkpoint

Stop the preview and copy the folder to `my-knowledge-site-ch03-backup`.

| File | Today's change |
| --- | --- |
| `content/about/`, `content/resources/` | New pages |
| `content/articles/_index.md` | New landing page |
| `content/projects/` | Landing page and project page |
| `content/_index.md` | Explore the notebook |
| `layouts/all.html` | Navigation block only |

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| Articles has no links | Its `_index.md` body: nothing is generated |
| The article vanished | The section file is `_index.md`, not `index.md` |
| A new page is not in the menu | The menu is written by hand in the layout |
| A menu item gives a 404 | The file, spelling, draft status, and path |
| Only the menu is left | You replaced the whole layout: use the backup |

---

## Completion check

- Every navigation item opens a useful page
- Articles and Projects have working landing pages
- The first article keeps its Chapter 2 address and image
- My manual lists link to the right items
- I can tell structure, navigation, and subject labels apart
- I restored the project folder after the recovery exercise
- I followed the visitor routes, one with the keyboard
- I saved a Chapter 3 checkpoint

---

# Next: Understand the HTML Behind Your Pages

Chapter 4: what the browser actually receives, and how it connects to what you wrote.

**polla.dev/ssg-book**
