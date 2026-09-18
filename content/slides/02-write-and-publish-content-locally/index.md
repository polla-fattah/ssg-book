---
title: "Write and Publish Content Locally"
description: "Chapter 2: your first article, with headings, links, a screenshot, and a code sample."
book_number: "2"
weight: 3
---

# Write and Publish Content Locally

Static Site Generators in the Age of AI

**Chapter 2**

Polla Fattah

---

## Today's goal

Give your website its **first article**: a short note about something you have learned.

- Sections, a link, a screenshot, and a code sample
- Reachable from the home page

**Publish locally** means it appears in the preview on your computer. Nothing goes online today.

---

## By the end of today you can

- **Create** an article in its own folder and control whether it is a draft
- **Structure** text with headings, paragraphs, lists, emphasis, and code
- **Add** working links and an image with meaningful alternative text
- **Repair** a broken image and publish the article in a normal preview

---

## Start from your working site

Open `my-knowledge-site` from Chapter 1, stop any running preview with **Ctrl+C**, and start it again with one extra option:

```text
hugo server -D
```

`-D` includes pages marked as **drafts**. Keep this terminal running.

---

## Create the article

Make this folder and file inside the project:

```text
content/articles/first-learning-note/index.md
```

Then open it in the browser, including the final slash:

```text
http://localhost:1313/articles/first-learning-note/
```

It uses the same layout and styling as the home page: you copied **no HTML at all**.

---

## The first version

```markdown
---
title: "My first learning note"
draft: true
---

Today I learned how to change a page in my notebook.

## What I tried

I edited my introduction and checked the preview.
```

---

## Front matter: two fields today

| Field | What it does |
| --- | --- |
| `title` | Becomes the page's main heading |
| `draft: true` | Leaves the page out of a normal build; `-D` includes it |

Write `true` and `false` **without quotation marks**: they are yes or no values, not text.

Below the second `---` is the article body, written in **Markdown**.

---

## Why the file is called index.md

The article has its own folder so its **text and image stay together**. Hugo calls this a **page bundle**.

| Source file | Address in the preview |
| --- | --- |
| `content/_index.md` | `/` |
| `content/articles/first-learning-note/index.md` | `/articles/first-learning-note/` |

The home page uses `_index.md`; an article uses `index.md`. Keep both exactly.

---

## Paragraphs and headings

- A **blank line** starts a new paragraph; one Enter does not
- The title is already the main heading, so body sections start with `##`
- Use `###` for a subsection inside a section

```markdown
## What I tried

### How I checked it
```

Choose heading levels for **meaning**, not for a smaller font.

---

## Emphasis and short code

```markdown
My rule is **change one thing at a time**.

I check it *before continuing*.

I edited `content/_index.md` and used `hugo server -D`.
```

- `**double asterisks**` for important words, `*single*` for emphasis
- Backticks around filenames and commands

Showing a command in an article **does not run it**.

---

## Lists

Bullets for related items:

```markdown
- A content file contains my writing.
- A layout supplies the page structure.
```

Numbers when the order matters:

```markdown
1. Change a sentence.
2. Save the file.
3. Inspect the preview.
```

---

## Add a useful link

```markdown
I can consult the
[Hugo documentation](https://gohugo.io/documentation/)
when I need help.

[Return to my home page](../../)
```

- The link text should say **where it goes**, never "click here"
- `../../` is a relationship between **web addresses**: up to `/articles/`, then up to the home page

---

## Link to a section of the page

Add a new section at the end of the article:

```markdown
## My next step
```

Then link to it from near the top:

```markdown
[Jump to my next step](#my-next-step)
```

Hugo gives the heading the identifier `my-next-step`. **Change the heading, and the link can break.**

---

## Add your own screenshot

1. Capture your home page and save it as a real **PNG**: `notebook-preview.png`
2. Put it **next to** `index.md` in the article folder
3. Add it to the article:

```markdown
![The notebook home page showing its introduction,
interests, and next steps](notebook-preview.png)

*My home page after my edits. Screenshot by the author.*
```

---

## Alternative text and captions

- The text in `![...]` is **alternative text**: it describes the image for someone who cannot see it
- The italic line underneath is a **caption**, for everyone
- The image path is just the **filename**, never `content/articles/...`
- Leave private tabs and notifications out of screenshots
- Someone else's image needs **permission** or a suitable licence

---

## Keep the image within the page

Add these rules at the end of `static/css/site.css`:

```css
article img { display: block; max-width: 100%; height: auto; }
article pre { max-width: 100%; overflow-x: auto; }
```

Large images now shrink to fit, and long code scrolls. Chapter 5 explains CSS.

---

## Show a command without running it

A **fenced code block** starts and ends with three backticks:

````markdown
```text
hugo server -D
```
````

If the rest of your article suddenly looks like code, a **closing fence is missing**.

---

## Break something on purpose

1. Change the image filename to `notebook-preview-missing.png` and save
2. The image fails to load, yet Hugo still **builds without complaint**
3. Read the real filename in the article folder
4. Restore `notebook-preview.png`, matching spelling and letter case

> A plausible-looking reference is not evidence that its destination exists.

---

## Make the article ready

1. Read it as a visitor: meaning, headings, links, image, alternative text
2. Change the front matter to `draft: false`
3. Stop the server with **Ctrl+C** and restart it **without** `-D`:

```text
hugo server
```

4. Check the article still appears

`draft` is a publishing switch, **not a lock**: never use it to hide confidential writing.

---

## Link it from the home page

At the end of `content/_index.md`, keep everything else and add:

```markdown
## Latest writing

- [My first learning note](articles/first-learning-note/)
```

The link points to the article's **web address**: no `content/`, no `index.md`.

Then check the article's link back home, and the navigation at the top.

---

## Try it yourself

1. Add a subsection about **one difficulty** you met and how you solved it
2. Include a numbered procedure or a short code sample
3. Check it in the normal preview, without `-D`
4. Follow the home-page link and both article links again

Report what **actually** happened: do not turn an example into an invented experience.

---

## Explain it to yourself

- Why does the article use `index.md` but the home page `_index.md`?
- What changes when you remove `-D` from the server command?
- Why does the image reference contain only its filename?
- Which link needs review if the article moves deeper?

---

## Save your checkpoint

Stop the preview and copy the whole folder to `my-knowledge-site-ch02-backup`, next to the project.

| File | Today's change |
| --- | --- |
| `content/articles/first-learning-note/index.md` | New article, `draft: false` |
| `.../first-learning-note/notebook-preview.png` | Your screenshot |
| `content/_index.md` | Latest writing section |
| `static/css/site.css` | Image and code sizing rules |

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| The article gives a 404 | The exact path, `index.md`, and whether it is still a draft |
| It vanished after a restart | `draft: true` without `-D` |
| The image does not load | Filename, extension, letter case, and folder |
| A link opens a path with `content/` | You used a file path instead of a web address |
| Much of the article looks like code | An unclosed three-backtick fence |

---

## Completion check

- My article opens in the normal `hugo server` preview
- Its title is the main heading; sections use sensible levels
- Its links open the right destinations
- The screenshot sits beside `index.md` and displays
- Its alternative text describes what the screenshot shows
- I repaired the broken image on purpose
- The home page links to the article
- I saved a Chapter 2 checkpoint

---

# Next: Organise a Useful Website

Chapter 3: an About page, sections, navigation, and addresses chosen around what a visitor needs.

**polla.dev/ssg-book**
