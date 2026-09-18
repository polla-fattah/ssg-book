---
title: "Your First Hugo Website"
description: "Chapter 1: a local preview, your first edit, and one deliberate mistake repaired."
book_number: "1"
weight: 2
---

# Your First Hugo Website

Static Site Generators in the Age of AI

**Chapter 1**

Polla Fattah

---

## Today's goal

A readable home page headed **My Knowledge Notebook**, running on your own computer.

Success means you can say:

> I know which file contains these words, I can change them, and I can put them back.

---

## By the end of today you can

- **Start and stop** a local Hugo preview
- **Find and edit** the file that holds the home-page introduction
- **Explain** the roles of the content file, the layout, and the browser preview
- **Recover** from a small mistake and keep a working copy

No HTML, CSS, Git, or programming experience is needed.

---

## Three roles

| Who | What happens |
| --- | --- |
| You | Write and edit the content in a Markdown file |
| Hugo | Builds the page from that content and a layout |
| Your browser | Displays the result at a local preview address |

Hugo is a **static site generator** (SSG). "Generate" means it produces the website from your source files.

---

## The tools for today

- **A text editor** that saves plain text: VS Code. A word processor will not do.
- **A terminal**, where you type one command and press Enter. Do not type the prompt, such as `PS>` or `$`.
- **Hugo**, which builds and previews the site

Today you do **not** need a GitHub account, a domain name, or an AI subscription.

---

## Install Hugo, then check it

- Windows: `winget install Hugo.Hugo.Extended`, then reopen PowerShell
- macOS: `brew install hugo`
- Linux: follow the official Linux installation guide

Check that it runs:

```text
hugo version
```

Use version **0.146.0 or later**, and write the version in your learning note. If `hugo` is not recognised, fix the installation before going on.

---

## Create the project

Make a folder `my-knowledge-site`, open it in VS Code, and add four files:

| File | Its job |
| --- | --- |
| `hugo.toml` | The site's basic settings |
| `content/_index.md` | The home-page text |
| `layouts/all.html` | The page structure (supplied) |
| `static/css/site.css` | The appearance (supplied) |

Watch the underscore in `_index.md`, and make sure no file ends in `.txt`.

---

## Open your first preview

1. In VS Code: **Terminal, New Terminal**
2. Check you are in the folder with `hugo.toml`: `Get-Location` on Windows, `pwd` on macOS or Linux
3. Start the preview:

```text
hugo server
```

4. Open the address it reports, normally `http://localhost:1313/`

---

## What you should see

- The site name **My Knowledge Notebook** at the top
- A navigation row: **Home**, **My interests**, **Next steps**
- The heading **Welcome to my knowledge notebook**
- A short introduction and two sections

`localhost` means **this computer**. Nobody else can open your preview; publishing comes in Chapter 7.

---

## Make the page yours

Open `content/_index.md` and replace the introduction with your own words:

```markdown
Hello! I am Sara. I use this notebook to explain
what I am learning and share useful resources.
```

Save with **Ctrl+S** (or **Command+S**) and look at the browser.

> Edit the source, save it, and inspect the result.

---

## Change the heading

At the top of the same file:

```yaml
---
title: "Welcome to Sara's learning space"
---
```

The lines between the two `---` markers are the **front matter**: information about the page. Its `title` becomes the large heading.

Everything below the second marker is the page's **content**.

---

## Which file does what

| File | Change it to adjust |
| --- | --- |
| `content/_index.md` | The home-page heading and text |
| `hugo.toml` | The site name and basic settings |
| `layouts/all.html` | How pages are structured |
| `static/css/site.css` | Colours, spacing, and typography |

You changed the words without touching the layout. Edit the **source files**, never a generated `public` folder.

---

## Break something on purpose

1. Save your work, and copy the introduction into a separate note
2. Replace it with: `This paragraph was changed by mistake.`
3. Save: the site **still works**, but the content is **wrong**
4. Use **Undo** until your text returns, then save again

> A page can build successfully and still contain the wrong information.

---

## Where AI agents will fit

A bounded request names the file, the goal, and the limits:

```text
Read content/_index.md. Propose a clearer version of its
introduction using only the information already present.
Keep the meaning and first-person voice. Do not change the
title, section headings, configuration, layout, or stylesheet.
Show the proposed replacement before editing the file.
```

If an agent invented a qualification, you would **reject** it, however polished it sounded.

---

## Try it yourself

1. Add one interest under **My interests**
2. Rewrite the sentence under **Next steps**
3. Save and check both changes in the browser

Then answer, aloud or in your learning note:

- Which file did you change?
- Which parts of the page changed?
- Why did the appearance stay the same?

---

## Stop, restart, and back up

- **Stop** the preview: click in the terminal and press **Ctrl+C** (also on macOS)
- **Restart** it later with `hugo server`
- **Back up**: stop the server, save everything, and copy the whole folder to `my-knowledge-site-ch01-backup`, next to the project, not inside it

Keep working in the original folder next time.

---

## When something goes wrong

| What you see | What to do |
| --- | --- |
| `hugo` is not recognised | Reopen the terminal; check the installation |
| Hugo cannot find the project | Move the terminal to the folder with `hugo.toml` |
| A connection error | Check `hugo server` is still running |
| Port 1313 is in use | Stop the old preview, or use `--port 1314` |

Change **one thing at a time**, and keep the error message.

---

## Completion check

- I can run `hugo version` and name my version
- I can open the local preview
- I can change the introduction and the page title
- I can tell content, configuration, layout, and styling apart
- I restored a paragraph I broke on purpose
- I can stop and restart the preview
- I have a backup of the project

---

# Next: Write and Publish Content Locally

Chapter 2: your first article, with headings, links, a screenshot, and a code sample.

**polla.dev/ssg-book**
