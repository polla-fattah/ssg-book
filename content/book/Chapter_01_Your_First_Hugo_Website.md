---
title: "Your First Hugo Website"
weight: 1
book_number: 1
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.2, September 2026**  
*Checked with Hugo 0.150.0 through 0.166.0. Requires Hugo 0.146.0 or later for the template layout convention.*

You have something worth sharing: notes from your work, an explanation you have written, a useful collection of resources, or a project you want others to understand. A website gives those materials a place where people can find and read them.

In this chapter, you will make the first small part of that website. You will open a local preview, change an introduction, and watch the page update. You will also make a deliberate mistake and repair it.

The first result is modest: a readable home page headed **My Knowledge Notebook**, with an introduction and links to two sections on the page. Across the book, this notebook will grow into a site with articles, projects, and resources. Later, you will ask an AI agent to help maintain it, review the agent's changes, and publish approved updates.

For now, success means being able to say: **“I know which file contains these words, I can change them, and I can put them back.”**

## What you will be able to do

By the end of this chapter, you should be able to:

- Start and stop a local Hugo preview.
- Find the file containing the home-page introduction and edit it.
- Explain the roles of the content file, layout, and browser preview.
- Recover from a small editing mistake and preserve a working copy.

No previous HTML, CSS, Git, or programming experience is required. The starter includes a little code for you to copy. You are not expected to understand that code yet.

## 1.1 A quick picture of what we are building

Imagine a notebook whose pages can be displayed as a website. You write the words in ordinary text files. A layout supplies the page structure, and a stylesheet supplies its appearance. Hugo combines them into files a browser can display.

Hugo is a **static site generator**, often shortened to **SSG**. “Generate” means that it produces the website output from your source material. “Static” describes how that output can be served; it does not mean you can never update the site or add interaction.

For this first exercise, remember three roles:

| Role | In our project |
| --- | --- |
| You write and edit the content. | A Markdown file contains the introduction. |
| Hugo builds the page. | It combines that content with the supplied layout. |
| Your browser displays the result. | You view the page through a local preview address. |

Hugo's official [quick-start guide](https://gohugo.io/getting-started/quick-start/) demonstrates the same basic relationship between a project, its content, and its local preview. Our exercise uses a smaller embedded starter so this chapter can stand alone.

## 1.2 Get the tools ready

You need a desktop or laptop computer, a browser, a text editor, and Hugo. You can read the chapter on a phone, but the practical steps assume a computer.

A **text editor** saves the actual characters in a file. Use Visual Studio Code, or another editor you already know that saves plain text. A word processor is not suitable for these project files. VS Code is available from its [official download page](https://code.visualstudio.com/download).

A **terminal** is a place where you enter commands. Each command below tells your computer to perform one action. Type the command and press Enter. Do not type the surrounding code fences or a prompt such as `PS>` or `$`.

For this chapter, you do not need a GitHub account, a domain name, or a paid AI subscription.

### Install Hugo for your operating system

If Hugo is already installed, go directly to the verification command below.

**Windows:** Open PowerShell from the Start menu. If Windows Package Manager (`winget`) is available, the following installation command is listed in Hugo's documentation:

```powershell
winget install Hugo.Hugo.Extended
```

Follow the installer prompts. Then close and reopen PowerShell. If you were using VS Code's terminal, restart VS Code as well so it can find the newly installed program. If `winget` is unavailable, use the prebuilt-binary instructions in the [official Windows installation guide](https://gohugo.io/installation/windows/).

The command installs the extended edition. This chapter uses only core features and also works with the standard edition; there is no need to replace a working standard installation solely for this exercise.

**macOS:** If Homebrew is already installed, open Terminal and run:

```bash
brew install hugo
```

If Homebrew is not installed, follow the prebuilt-binary route or another supported route in the [official macOS installation guide](https://gohugo.io/installation/macos/).

**Linux:** Follow the [official Linux installation guide](https://gohugo.io/installation/linux/) for your distribution. Check the installed version rather than assuming your distribution's package is recent enough for this exercise.

### Check that Hugo can run

In your terminal, enter:

```text
hugo version
```

You should see a line identifying Hugo and its version. Extra information about the edition, operating system, or build is normal. Record the version you installed in a separate learning note; it will help if you need to troubleshoot later.

This starter uses the template conventions introduced in **Hugo 0.146.0**. Its build and live-edit exercises were verified with **Hugo 0.150.0 through 0.166.0**. Use version 0.146.0 or later; older distribution packages (such as legacy packages from Debian/Ubuntu `apt`) do not support `all.html` and will fail to build. In Hugo 0.158.0 and later, site language configuration uses `locale` instead of `languageCode` to avoid deprecation warnings. See the [template-system overview](https://gohugo.io/templates/new-templatesystem-overview/) for the relevant changes.

> **If the command is not recognised:** stop here and fix the installation. Reopen your terminal first. If that does not help, return to the installation guide for your operating system. Your website files are not the cause of an unrecognised `hugo` command.

## 1.3 Create your project folder

Using your normal file manager, create a folder named `my-knowledge-site` somewhere convenient, such as inside Documents.

Open VS Code and choose **File → Open Folder**, then select that folder. If your editor asks whether you trust the folder, remember that this is the new folder you just created for the exercise.

In the editor's file explorer, create these folders and files. Paths in this table are relative to `my-knowledge-site`.

| File | Where it goes | Purpose |
| --- | --- | --- |
| `hugo.toml` | Directly inside the project folder | The site's basic settings |
| `_index.md` | Inside a folder named `content` | The home-page text |
| `all.html` | Inside a folder named `layouts` | The supplied page structure |
| `site.css` | Inside `static`, then a folder named `css` | The supplied appearance |

The resulting paths are `hugo.toml`, `content/_index.md`, `layouts/all.html`, and `static/css/site.css`.

Pay attention to the underscore in `_index.md`. In Hugo, a leading underscore designates a section or branch bundle (such as the home page), whereas `index.md` without an underscore designates an individual standalone leaf article. Also make sure the files are not accidentally named `hugo.toml.txt` or `all.html.txt`. Creating them inside the code editor helps avoid hidden filename-extension problems.

You can either create these four files by hand or obtain them ready-made from the companion starter repository (`ssg-playground`, branch `chapter-01`).

Copy the contents from **Starter files** near the end of this chapter into the four matching files. Copy only what is inside each code block; do not include the backticks. Save every file.

The HTML and CSS are supplied materials. Leave them unchanged for now. We will examine their structure in later chapters. This small starter performs the presentation role that a larger theme would normally provide.

> **Pause and check:** the editor should show the four files at exactly the paths listed above. You do not need to run `hugo new site` or install a separate theme for this embedded starter.

## 1.4 Open your first preview

In VS Code, choose **Terminal → New Terminal**. The integrated terminal normally opens in the project folder. Confirm that you are in the folder containing `hugo.toml`:

- In PowerShell, type `Get-Location` to show the folder and `Get-ChildItem` to list its contents.
- In macOS or Linux terminals, type `pwd` to show the folder and `ls` to list its contents.

If you are in the wrong place, close that terminal, open the correct project folder in the editor, and create a new terminal there.

Now run:

```text
hugo server
```

Leave the terminal running. Read its output and find the local address, normally:

```text
http://localhost:1313/
```

Enter that address in your browser's address bar (or hold **Ctrl** and click the link directly in the VS Code terminal, or **Command** on macOS). If Hugo reports a different address or port, use the one it reports.

You should see:

- The site name, **My Knowledge Notebook**, near the top.
- A navigation row with **Home**, **My interests**, and **Next steps**.
- The heading **Welcome to my knowledge notebook**.
- A short introduction and two sections underneath it.

The navigation links for My interests and Next steps move within this same page. We will add separate pages later.

**This is a local preview.** `localhost` refers to the computer you are using. Opening that address on somebody else's computer will not open your website. We will make the site publicly reachable in the publishing chapter.

Hugo's development server watches project files and normally rebuilds and refreshes the preview after changes. The terminal stays occupied while that server runs; this is expected behaviour. [Hugo server documentation](https://gohugo.io/commands/hugo_server/)

## 1.5 Make the page yours

Open `content/_index.md` in the editor. Find this sentence:

```markdown
Hello! I am Dana. This is where I collect useful ideas, learning notes, and small projects.
```

Dana is a fictional example. Replace the name and introduction with your own wording. For example:

```markdown
Hello! I am Sara. I use this notebook to explain what I am learning and share useful resources.
```

Save the file with **Ctrl+S** on Windows/Linux or **Command+S** on macOS. Look at your browser. The introduction should change, while the colours and page layout remain the same.

If it does not change, refresh the browser once. Then check that you saved the correct file and that the terminal has not reported an error.

You have now completed the central operation you will repeat throughout the book:

**Edit the source, save it, and inspect the result.**

### Change the heading as well

At the top of the same file, find:

```yaml
title: "Welcome to my knowledge notebook"
```

Change only the text inside the quotation marks:

```yaml
title: "Welcome to Sara's learning space"
```

Save and inspect the page again.

The lines between the two `---` markers form the **front matter** in **YAML** format: a small block of structured metadata about the page. Here, its `title` supplies the large page heading. The writing below the second marker forms the page's main content.

You only need to recognise that distinction today. Chapter 2 develops Markdown, and Chapter 9 explains structured metadata and configuration in detail.

## 1.6 Understand what changed

You edited the writing without editing the layout. The starter keeps those responsibilities in separate files:

| File | What you would change there |
| --- | --- |
| `content/_index.md` | The home-page heading and main text |
| `hugo.toml` | The site-wide name and basic settings |
| `layouts/all.html` | The structure used to display pages |
| `static/css/site.css` | Colours, spacing, typography, and other styling |

The name at the top of the site comes from `hugo.toml`. The larger heading inside the article comes from `content/_index.md`. They can be different because they describe different things: the whole site and the current page.

Hugo reads the project and generates the browser-facing output. Continue editing the source files listed above. If you later encounter a generated folder such as `public`, changes made there may be overwritten by another build.

You may notice expressions such as `{{ .Title }}` in the layout. They mark places where Hugo inserts information. You do not need to write template expressions yet; first become comfortable changing content and recognising its effect.

## 1.7 Practise recovering from a mistake

Before experimenting, save your current work. Then copy the introduction paragraph into a separate temporary note outside the project. This gives you a small, clear recovery reference.

In `content/_index.md`, replace the introduction paragraph with:

```markdown
This paragraph was changed by mistake.
```

Save the file and inspect the preview. The website still works, but its content is wrong.

Return to the editor. Use **Undo** until your previous introduction returns, then save again. If the editor's undo history is unavailable, restore the paragraph from your temporary note and save it.

Check the browser to confirm the original introduction is back.

This distinction will matter when we introduce AI agents: **a page can build successfully and still contain the wrong information**. Seeing a successful build is one check; reading the result is another.

For this exercise, undo and a temporary copy are sufficient. The Git chapter will give you a more dependable record of changes and a way to restore earlier versions.

## 1.8 Where AI agents will fit

An AI agent can be given access to project files and asked to propose or perform a change. In later chapters, you will set up an agent and control the scope of its work. Today, consider this illustrative task:

> Read `content/_index.md`. Propose a clearer version of its introduction using only the information already present. Keep the meaning and first-person voice. Do not change the title, section headings, configuration, layout, or stylesheet. Show the proposed replacement before editing the file.

This instruction identifies the file, the intended improvement, and the limits. If an agent invented a qualification or project, you would reject or correct that addition even if its wording sounded polished.

No agent installation is required for this chapter. You have already practised the human actions that make later agent work inspectable: locating the source, reading changes, previewing the page, and restoring earlier text.

## 1.9 Try a small independent change

Without changing the layout or stylesheet:

1. Add one interest under **My interests**, following the existing list format.
2. Rewrite the sentence under **Next steps** to describe something you want to share.
3. Save the file and verify both changes in the browser.

Keep the section headings unchanged for this exercise because the starter's navigation links point to them. We will learn how headings and links relate in the next chapter.

Now explain aloud, or in a learning note:

- Which file did you change?
- Which visible parts of the page changed?
- Why did the appearance remain consistent?

If you can answer those questions, you have begun to understand the workflow rather than merely repeat commands.

## 1.10 Stop, restart, and preserve your work

Click inside the terminal running Hugo and press **Ctrl+C**. This stops the preview server; it does not delete your files. On macOS, the terminal interruption is also Ctrl+C, not Command+C.

The browser may continue to show the last page it loaded. That does not mean the preview server is still running. Refreshing or navigating after stopping the server may show a connection error.

To resume, open the project folder and run:

```text
hugo server
```

Open the reported address again.

For a simple end-of-chapter checkpoint, stop the server, save all files, and use your file manager to copy the entire `my-knowledge-site` folder to a sibling folder named `my-knowledge-site-ch01-backup`. Do not put the backup inside the active project. Continue working in the original folder in Chapter 2.

## Completion check

- [ ] I can run `hugo version` and identify my installed version.
- [ ] I can open the local website preview.
- [ ] I can change the introduction and page title in `content/_index.md`.
- [ ] I can distinguish content, configuration, layout, and styling.
- [ ] I have restored an intentionally incorrect paragraph.
- [ ] I can stop and restart the preview.
- [ ] I have preserved a working copy of the project.

In Chapter 2, we will add a separate article and learn the Markdown needed to structure it, link it, and illustrate it.

## Troubleshooting when you need it

| What you see | What to check or do |
| --- | --- |
| `hugo` is not recognised or not found. | Reopen the terminal or editor after installation. Verify the installation and executable path using the official operating-system guide. |
| Hugo cannot locate the configuration or project. | Check that the terminal is in the folder containing `hugo.toml`, rather than its parent or the `content` folder. |
| A configuration parsing error appears. | Compare `hugo.toml` with the supplied starter. Keep straight quotation marks, matching pairs, and the equals signs. |
| A front-matter parsing error appears. | Check the two `---` markers and the matching quotation marks around the title in `content/_index.md`. |
| The browser shows a connection error. | Check that `hugo server` is still running and that you entered its reported address, including `http://` and the port. |
| The terminal reports that port 1313 is already in use. | Stop an earlier preview with **Ctrl+C**. On Windows, closing a terminal tab without stopping Hugo may leave an orphaned `hugo.exe` running; terminate it in Task Manager or use `hugo server --port 1314`. |
| The home page is missing or Hugo warns about a missing layout. | Check the spelling and placement of `layouts/all.html`, confirm that its code was saved, and check the Hugo version. |
| The page appears without the supplied styling. | Check that `site.css` is inside `static/css`, and compare the stylesheet link in `layouts/all.html` with the starter. |
| Your change does not appear. | Save the file, check for terminal errors, refresh the preview, and confirm that the editor and server are using the same project folder. |
| You see `---` or template expressions as literal text. | Open the address from `hugo server`, rather than double-clicking a source file in the file manager. Check that code was copied into the right files. |

When an error occurs, change one thing at a time and try again. Keep the error message: it provides useful evidence for troubleshooting and for later work with an agent.

## Starter files

These four blocks contain the complete starter for this draft. Copy each into the file named above it. They are provided as project materials; studying HTML, CSS, and template syntax is deferred to later chapters.

### File 1: `hugo.toml`

```toml
baseURL = 'https://example.org/'
locale = 'en'
title = 'My Knowledge Notebook'
```

`https://example.org/` is a placeholder, not your published website. In Hugo v0.158.0+, `locale = 'en'` is the standard language configuration (older Hugo versions used `languageCode = 'en'`). Hugo's local server supplies the preview address. We will configure the real public address when publishing.

### File 2: `content/_index.md`

```markdown
---
title: "Welcome to my knowledge notebook"
---

Hello! I am Dana. This is where I collect useful ideas, learning notes, and small projects.

## My interests

- Learning new things
- Explaining useful ideas
- Sharing small projects

## Next steps

I will use this notebook to publish my first article and organise useful resources.
```

### File 3: `layouts/all.html`

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
      <a href="{{ "" | relURL }}#my-interests">My interests</a>
      <a href="{{ "" | relURL }}#next-steps">Next steps</a>
    </nav>
  </header>
  <main id="main" tabindex="-1">
    <article>
      <h1>{{ .Title }}</h1>
      {{ .Content }}
    </article>
  </main>
  <footer>A place to learn, explain, and share.</footer>
</body>
</html>
```

### File 4: `static/css/site.css`

```css
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f5f3ed;
  color: #263238;
  font-family: system-ui, sans-serif;
  line-height: 1.7;
}
header, main, footer {
  width: min(100% - 2rem, 48rem);
  margin-inline: auto;
}
header { padding-block: 2rem 1rem; }
.site-name { font-size: 1.25rem; font-weight: 700; }
nav { display: flex; flex-wrap: wrap; gap: 1rem; }
a { color: #005b66; text-underline-offset: 0.2em; }
main {
  padding: clamp(1rem, 4vw, 2rem);
  background: #ffffff;
  border: 1px solid #d5d9d8;
  border-radius: 0.75rem;
  overflow-wrap: anywhere;
}
h1 { font-size: clamp(1.7rem, 5vw, 2.5rem); line-height: 1.2; }
h2 { margin-top: 2rem; line-height: 1.3; }
footer { padding-block: 1.5rem; }
a:focus-visible { outline: 3px solid #005b66; outline-offset: 4px; }
.skip-link { position: absolute; top: -10rem; left: 1rem; }
.skip-link:focus {
  top: 0.5rem;
  padding: 0.5rem 1rem;
  background: #ffffff;
}
```

The starter uses `all.html` as a general HTML layout, following Hugo's newer template conventions. It intentionally keeps presentation local and small; no external theme download, Git submodule, JavaScript package, or custom font is required for this exercise. Later chapters will develop the layout into reusable parts.

---

## Editorial note for the author (remove before publication)

This is a self-contained chapter draft for review. To honour the request for one Markdown file, the starter is embedded in the chapter instead of referring to an unavailable companion download. This is a provisional adaptation of the blueprint's packaged starter-theme approach; it does not select a third-party theme for the whole book.

Before publication, choose whether to package this small starter or adapt the exercise to the final theme. A downloadable, versioned starter should make copying four files unnecessary in the main reading path; the embedded source can remain as a fallback. Supply matching screenshots from that final starter.

Documentation was consulted on 17 September 2026. The four starter blocks were extracted directly from this Markdown file and tested with Hugo 0.150.0, standard edition, on Linux amd64. The production build passed with warnings treated as failures. Checks confirmed the home-page content, navigation target IDs, and copied stylesheet. A running local server reflected a changed introduction, an intentional mistaken edit, and restoration of the corrected text. These checks verified server responses; they did not constitute a visual browser audit or a beginner usability trial.

Package-manager commands install the versions available from their respective repositories; they do not pin the final book's software baseline. Before publication, select a supported release baseline and rerun the exercises against it. A representative beginner trial, visual browser inspection, and Windows/macOS installation walkthroughs remain necessary before describing this chapter as publication-ready.
