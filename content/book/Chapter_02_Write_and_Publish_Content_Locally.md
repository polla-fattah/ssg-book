---
title: "Chapter 2 — Write and Publish Content Locally"
weight: 2
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*Checked with Hugo 0.150.0 (standard edition) on Linux. No beginner trial, browser review, or screenshot capture yet.*

In Chapter 1, you changed a home page. Now you will give your website something more substantial to read: its first article.

The article will describe a small thing you have learned. You will give it sections, add links and a screenshot, and make it reachable from the home page. Along the way, you will learn the Markdown needed to make a piece of writing understandable both as a text file and as a web page.

Here, **publish locally** means making the article appear in the site you preview on your computer. You will not upload it to a public host in this chapter.

## What you will be able to do

By the end, you should be able to:

- Create an article in its own folder and control whether it is a draft.
- Structure its text with headings, paragraphs, lists, emphasis, and code formatting.
- Add working links and an image with meaningful alternative text.
- Check the rendered article, repair a broken image reference, and make the article available in a normal local preview.

## 2.1 Start from your working website

Open the original `my-knowledge-site` project from Chapter 1. Keep your personalised introduction. Its relevant files are:

| Existing file | Role |
| --- | --- |
| `hugo.toml` | Site settings |
| `content/_index.md` | Home-page content |
| `layouts/all.html` | The supplied general layout |
| `static/css/site.css` | The supplied styling |

If you need to rebuild that starting point, Chapter 1 includes all four starter files. No new software, theme, or account is required here. This draft's exercises were checked with the same Hugo 0.150.0 Linux baseline used for Chapter 1.

Open a terminal in the folder containing `hugo.toml`. If a preview server is still running, stop it with **Ctrl+C**. Then start it with one additional option:

```text
hugo server -D
```

The `-D` option includes pages marked as drafts. Leave this terminal running and open the address it reports, normally `http://localhost:1313/`.

You should see the home page you already know. We will keep using the same editor, project, and browser while adding one article.

## 2.2 Make an article before studying the syntax

Inside `content`, create a folder named `articles`. Inside it, create another folder named `first-learning-note`. In that folder, create a file named `index.md`.

Its complete path, relative to the project, is:

```text
content/articles/first-learning-note/index.md
```

Copy this small article into that file and save it:

```markdown
---
title: "My first learning note"
draft: true
---

Today I learned how to change a page in my knowledge notebook.

## What I tried

I edited my introduction, saved the file, and checked the local preview.

## What I learned

The words on the page come from a content file that I can edit.
```

Open the article directly in your browser:

```text
http://localhost:1313/articles/first-learning-note/
```

Use your server's actual port if it differs from 1313. Include the final slash.

You should see the article title and two sections, inside the same styled layout as your home page. The title is supplied by the front matter; the body comes from the writing below it.

Your home page does not yet link to this article. That is expected. The Chapter 1 starter displays page content but does not automatically create an article directory. We will add an explicit link shortly and develop wider navigation in Chapter 3.

> **First checkpoint:** you have created a second page without copying the HTML layout or stylesheet. Hugo has used the existing layout to display the new content.

## 2.3 Understand the file you just created

The top of the file contains two pieces of metadata:

| Field | Meaning in this exercise |
| --- | --- |
| `title` | The title displayed by our layout |
| `draft: true` | Exclude the article from a normal build; include it when draft rendering is explicitly enabled |

Keep `true` and `false` unquoted. They represent yes/no values rather than ordinary text. The quotation marks around the title enclose a text value.

Hugo supports several front-matter formats. We are using YAML between `---` markers. For now, learn these two fields; you do not need a complete configuration-language lesson. [Hugo front-matter documentation](https://gohugo.io/content-management/front-matter/)

Below the closing marker is the article body, written in Markdown. Markdown uses visible characters such as `##` and `-` to describe structure. Hugo turns that structure into HTML for the browser.

### Why this file is called `index.md`

The article has a folder of its own so its text and image can stay together. Hugo calls a folder containing `index.md` and associated resources a **leaf page bundle**. The home page uses `_index.md`, with an underscore, because it is a different kind of page. Preserve both filenames as shown. [Hugo page bundles](https://gohugo.io/content-management/page-bundles/)

| Source location | Address in this project's local preview |
| --- | --- |
| `content/_index.md` | `/` |
| `content/articles/first-learning-note/index.md` | `/articles/first-learning-note/` |

The article's folder name supplies the last part of its address in this setup. Changing its displayed title does not change that folder name. Later configuration can alter URL behaviour; this is the default arrangement used by our starter.

## 2.4 Give the writing a clear structure

Continue editing the same article. Add one small feature at a time, save, and check the browser.

### Paragraphs and headings

A blank line separates paragraphs:

```markdown
I started with a short introduction.

Then I changed the words and checked the preview.
```

Pressing Enter once inside a paragraph usually does not create a new paragraph in the rendered page. Use a blank line when you mean to start a new thought.

In our layout, the front-matter title already becomes the main page heading. Start body sections with `##`, and use `###` for a subsection:

```markdown
## What I tried

I changed the introduction on my home page.

### How I checked it

I saved the file and read the updated text in the browser.
```

Use heading levels to express the relationship between ideas. Do not choose `###` just because you prefer a smaller font. Styling comes later.

### Emphasis and short code references

Use a pair of double asterisks for a short piece of important text, and a pair of single asterisks for emphasis:

```markdown
My rule is **change one thing at a time** and check it *before continuing*.
```

Use backticks around a filename or short command:

```markdown
I edited `content/_index.md` and used `hugo server -D` to preview drafts.
```

The backticks make technical text easier to distinguish from the surrounding sentence. Displaying a command in an article does not execute it.

### Lists

Use a bulleted list for related items:

```markdown
- A content file contains my writing.
- A layout supplies the page structure.
- A stylesheet controls the appearance.
```

Use a numbered list when the order matters:

```markdown
1. Change a sentence.
2. Save the file.
3. Inspect the preview.
```

Keep blank lines before and after these blocks. That makes the source easier to read and helps avoid accidental formatting interactions.

Hugo's Markdown support includes features beyond basic Markdown. Different publishing tools can support different extensions, so check rendered output when moving content between systems. [Hugo content formats](https://gohugo.io/content-management/formats/)

## 2.5 Add a useful link

A Markdown link has readable text in square brackets and a destination in parentheses:

```markdown
I can consult the [Hugo documentation](https://gohugo.io/documentation/) when I need help.
```

Add this sentence to your article, save, and click the rendered link. The text tells the reader what the destination contains. “Click here” would provide less context.

For a link back to this site's home page, add:

```markdown
[Return to my home page](../../)
```

From `/articles/first-learning-note/`, the first `../` goes up to `/articles/`, and the second reaches the site's home location. These are **web-address relationships**, not instructions to browse folders on your computer.

This link is deliberately relative to the article's address. It also remains inside the site when the same folder structure is hosted under a prefix such as `/my-knowledge-site/`. Moving the article to a different depth would require reviewing the link. Later we will introduce Hugo's tools for managing links as sites grow.

### Link to a section on the same page

Append this section to your article:

```markdown
## My next step

I will write another short note about something I can explain clearly.
```

Near the article's opening paragraph, add:

```markdown
[Jump to my next step](#my-next-step)
```

With this starter, Hugo gives that heading the identifier `my-next-step`. Click the link and look at the browser address: it should end in `#my-next-step`. On a short page, the visual movement may be slight.

This also explains Chapter 1's navigation. Its My interests and Next steps links target specific home-page headings. Changing a heading can change its generated identifier, so check links that point to it.

## 2.6 Illustrate the article with your own screenshot

Open your site's home page. Use your operating system's screen-capture tool to capture just the relevant page area. Save the image as a **PNG file** named `notebook-preview.png`.

If the capture tool puts the image on the clipboard, paste it into a basic image editor and save or export it as PNG. Renaming a JPEG extension to `.png` does not convert its format. Use the tool's actual Save or Export option.

Place the file next to the article:

```text
content/articles/first-learning-note/notebook-preview.png
```

The screenshot is a reader-created asset, so this single chapter file needs no separate image download. Capture your own example site and avoid including unrelated tabs, notifications, or private material in the image.

Add the following to the article after the section explaining what you learned:

```markdown
## My notebook in the browser

![The notebook home page showing its introduction, interests, and next steps](notebook-preview.png)

*My home page after editing the introduction. Screenshot by the author.*
```

Save and inspect the article. The exclamation mark makes this an image rather than a text link. The path names a file in the same page bundle. Do not write `content/articles/...` inside these parentheses: that is a source-file location, not the image's browser address.

The words inside the square brackets are **alternative text**. They describe the useful information in the image for someone who cannot see it. Adjust the wording if your screenshot shows something different. The italic sentence is a visible caption; it serves a different purpose from alternative text.

If you use another person's image in future, establish permission or an appropriate licence and retain the required attribution. Finding an image online does not by itself grant permission to republish it.

### Keep the image within the page

Chapter 1's small stylesheet did not include image sizing. Open `static/css/site.css` and add these rules at the end, outside its existing braces:

```css
article img {
  display: block;
  max-width: 100%;
  height: auto;
}

article pre {
  max-width: 100%;
  overflow-x: auto;
}
```

Save and refresh the preview. The first rule lets large images shrink to the available width while preserving their proportions. The second lets long code samples scroll within their own area. Resize the browser to check the result. These are supplied styling adjustments; Chapter 5 will explain CSS properly.

## 2.7 Display a command without running it

Sometimes a learning note needs to show several lines exactly. A **fenced code block** begins and ends with three backticks. The word after the opening backticks identifies the content type.

Copy the following three-line sample into the body of your article:

````markdown
```text
hugo server -D
```
````

Copy the inner three-backtick opening line, the command, and the closing line; the outer frame is only how this book displays the example. The article will show the command as a code sample. It will not start another server.

If all the writing after a code block appears as code, look for a missing closing fence. You can close a server terminal with Ctrl+C; closing a Markdown code block requires the matching backticks in the file. They solve different problems.

### Optional: a small comparison table

If your note needs a simple comparison, try:

```markdown
| Action | What I check |
| --- | --- |
| Edit a paragraph | The meaning is still correct. |
| Add a link | The intended page opens. |
| Add an image | It loads and has useful alternative text. |
```

The separator row is part of the syntax. Your current CSS may display the table with minimal styling. That is acceptable for this exercise: the goal is to recognise a structured comparison. Tables are optional here and are not required for the completed article.

## 2.8 Test and repair a broken image reference

Before changing anything, confirm that your image currently loads. Then temporarily change only the image filename in the Markdown:

```markdown
![The notebook home page showing its introduction, interests, and next steps](notebook-preview-missing.png)
```

Save and refresh the article. The image should fail to load. Depending on your browser, you may see its alternative text or a broken-image indicator. Hugo may still report a successful build: the ordinary Markdown image reference in this starter does not guarantee that the destination exists.

Repair the reference:

1. Look inside the article folder and read the actual filename.
2. Restore `notebook-preview.png` in the Markdown, matching spelling and letter case.
3. Save and refresh the article.
4. Confirm that the image appears again.

You have practised checking the source against the output. Keep that habit when an AI agent proposes filenames or links. A plausible-looking reference is not evidence that its destination exists.

## 2.9 Make the article ready and link it from the home page

Read the article as a visitor would. Check its meaning, heading order, links, image, and alternative text. Replace the sample sentences with accurate statements about your own work where appropriate.

When it is ready, change this front-matter line:

```yaml
draft: false
```

Save the file. In the terminal, stop the current server with **Ctrl+C**, then restart without the draft option:

```text
hugo server
```

Open the article's address again. It should still appear. You have confirmed that the article no longer depends on a draft-inclusive preview.

If it disappears, check whether `draft` is still `true` in the correct file. Do not immediately add `-D` back and assume the issue is solved; that would hide the distinction you are trying to verify.

The draft field is a publishing control, not an access-control mechanism. The source remains readable to anyone with access to the project, and a draft-inclusive deployment would include the draft. Never use this flag to protect confidential writing.

### Link the article from the home page

Open `content/_index.md`. Leave your introduction, interests, and Next steps section intact. Add this new section at the end of the body:

```markdown
## Latest writing

- [My first learning note](articles/first-learning-note/)
```

Save, visit the home page, and click the new link. From the home page, `articles/first-learning-note/` points to the article's published path. There is no `content/` prefix and no `index.md` in the destination.

Now click the article's **Return to my home page** link. Also try the shared navigation at the top: Home opens the home page, while My interests and Next steps return to the corresponding home-page sections. They do not point to sections inside the article.

This modest manual link is enough for two pages. Do not worry if visiting `/articles/` itself shows a heading without an article list; our starter has no automatic listing loop yet. We will improve organisation next and build reusable listings in the template chapters.

> **Second checkpoint:** a visitor can now open the home page, follow a link to a reviewed article, see its image, and return home.

## 2.10 Try an independent variation and save your checkpoint

Make one more improvement to this article:

1. Add a subsection describing one difficulty you encountered and how you resolved it.
2. Include either a numbered procedure or a short code sample where it helps the explanation.
3. Check the article in the normal preview without `-D`.
4. Follow the home-page link and both article links again.

The new writing should report what actually happened. Do not turn an illustrative example into an invented personal experience.

If you already use a browser chatbot, an optional writing-only exercise is to ask it to suggest clearer headings for a paragraph you supply. Compare its suggestions with the original meaning before changing your file. An account or agent setup is not required for this chapter; direct project access comes later.

### Explain the result to yourself

- Why does this article use `index.md` while the home page uses `_index.md`?
- What changes when you remove `-D` from the server command?
- Why does the image reference contain only its filename?
- Which link would need review if you moved the article deeper into the URL structure?

You should be able to answer using this project. Memorising every Markdown feature is unnecessary.

### Save your Chapter 2 checkpoint

Stop the preview with Ctrl+C and save all edited files. Copy the project folder to a sibling folder named `my-knowledge-site-ch02-backup`, outside the active project. Continue working in the original folder in Chapter 3.

Your changes should be limited to:

| File | Change |
| --- | --- |
| `content/articles/first-learning-note/index.md` | New article, ending with `draft: false` |
| `content/articles/first-learning-note/notebook-preview.png` | Your screenshot |
| `content/_index.md` | Added Latest writing section |
| `static/css/site.css` | Added image and code-block sizing rules |

The configuration and layout from Chapter 1 remain sufficient for this exercise. Generated files may also change when Hugo runs; they are output, not additional authoring tasks.

## Completion check

- [ ] My article opens in the ordinary `hugo server` preview.
- [ ] Its front-matter title supplies the main heading, and body sections use appropriate heading levels.
- [ ] Its links open the intended destinations.
- [ ] The screenshot is beside `index.md` and displays correctly.
- [ ] Its alternative text describes what the screenshot actually shows.
- [ ] I repaired the intentionally broken image reference.
- [ ] The home page links to the article without replacing my earlier content.
- [ ] I have saved a working Chapter 2 checkpoint.

Chapter 3 will develop this two-page beginning into a clearer website structure, with pages, sections, and navigation chosen around the visitor's needs.

## Troubleshooting when you need it

| Problem | Likely cause and next check |
| --- | --- |
| The new article returns a 404. | Check the exact path, that the file is named `index.md`, that it is saved, and whether a draft-inclusive preview is needed. |
| The home page works but `/articles/` shows no list. | The minimal layout does not generate an automatic list. Open the article's full address or use the manual home-page link. |
| The article disappears after restarting the preview. | You may have removed `-D` while `draft` remains `true`. Review the article and change the flag when ready. |
| The page title appears twice. | Remove an extra `#` title from the body; this layout already renders the front-matter title. |
| The image does not load. | Check the actual filename, extension, letter case, and placement beside `index.md`. Ensure the saved file really is a PNG. |
| The image extends beyond the article. | Confirm the added CSS rules are outside existing braces, save the stylesheet, and refresh. |
| A link opens a path containing `content/`. | You used a source path in place of a website address. Compare with the chapter's working link examples. |
| A section link does not jump to the intended heading. | Check whether the heading changed and whether the fragment still matches its generated identifier. |
| A heading displays its hash characters. | Use a space after `##` and make sure the line is not inside a code block or accidentally indented. |
| Much of the article appears as code. | Look for an unclosed three-backtick fence earlier in the file. |
| A pasted table shows pipe characters. | Check its separator row and blank lines, and verify the result in Hugo rather than assuming every Markdown viewer behaves identically. |

## Completed article for comparison

The following is a complete reference version of `content/articles/first-learning-note/index.md`. It assumes your screenshot is saved beside it. Preserve your own accurate wording if you have personalised the exercise. Copy the content inside the outer four-backtick display block; retain the inner three-backtick code block as part of the article.

````markdown
---
title: "My first learning note"
draft: false
---

Today I learned how to change a page in my knowledge notebook.

[Jump to my next step](#my-next-step)

## What I tried

I edited my introduction, saved the file, and checked the local preview.

### How I checked it

1. Change a sentence.
2. Save the file.
3. Inspect the preview.

## What I learned

The words on the page come from a content file that I can edit.

My rule is **change one thing at a time** and check it *before continuing*.

- A content file contains my writing.
- A layout supplies the page structure.
- A stylesheet controls the appearance.

I edited `content/_index.md`. To include drafts in the local preview, I used:

```text
hugo server -D
```

I can consult the [Hugo documentation](https://gohugo.io/documentation/) when I need help.

## My notebook in the browser

![The notebook home page showing its introduction, interests, and next steps](notebook-preview.png)

*My home page after editing the introduction. Screenshot by the author.*

## My next step

I will write another short note about something I can explain clearly.

[Return to my home page](../../)
````

---

## Editorial note for the author — remove before publication

This draft continues the exact four-file starter embedded in Chapter 1. It does not assume a third-party theme, an automated article listing, a content-generation archetype, a Git repository, or an installed AI agent. The shared layout already renders individual pages. The added CSS supports screenshots and code blocks without requiring a separate styling lesson.

The screenshot is deliberately created by the reader, allowing this deliverable to remain one Markdown file. A companion package should eventually provide a reusable example image and matching screenshots of the finished page. The complete reference article provides a recovery point; a packaged Chapter 1 checkpoint is still desirable for readers who need to restart the project.

The chapter teaches links relative to the rendered URL under the starter's existing configuration. Template helpers and content-aware link resolution should be introduced later without retroactively claiming that ordinary relative links automatically survive arbitrary moves. Repeat the subdirectory checks when the actual publishing workflow is introduced.

Validation on 17 September 2026 reconstructed the starter from the current saved Chapter 1 and extracted the article examples and CSS directly from this chapter. Hugo 0.150.0, standard edition, on Linux amd64 built the completed project with warnings treated as failures. Both domain-root and `/my-knowledge-site/` base URLs passed checks for local links, heading targets, stylesheet paths, and the image resource. Checks also confirmed one main heading, rendered emphasis, and the image's alternative text.

Separate builds confirmed draft exclusion without `-D` and inclusion with it. A running local server served the draft article and image, returned 404 for the intentionally broken image path, and served the repaired image. Restarting without `-D` after setting `draft: false` retained the article. A small generated PNG was used only as a path-resolution test fixture; it was not a screenshot and is not part of the deliverable. Actual screenshot capture, visual browser review, cross-platform walkthroughs, and a representative beginner trial remain unverified and are required before publication.
