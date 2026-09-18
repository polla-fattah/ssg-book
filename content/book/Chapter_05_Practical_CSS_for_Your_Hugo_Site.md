---
title: "Practical CSS for Your Hugo Site"
weight: 5
book_number: 5
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1, 17 September 2026**  
*Checked with Hugo 0.150.0 on Linux. No beginner trial; responsive, zoom, and focus behaviour are not browser-tested yet.*

Your notebook already has a readable layout. In Chapter 4, you inspected its HTML and added a footer note. Now you will give that note a style and make two small adjustments to the reading experience.

The visible result is small but deliberate: the footer note sits below a thin rule in quieter text, body text reads a little larger, and your article's section headings have clearer space above them. Everything else should look as it did at the end of Chapter 4.

Our aim is modest: understand enough CSS to customise this Hugo website and check an agent's proposed changes. You do not need to learn every property, build a design system, or become a professional web designer. Work through the three edits, learn how to inspect their effects, and keep the reference material for when you need it.

## What you will be able to do

By the end, you should be able to:

- Find the stylesheet used by this Hugo project and explain how pages load it.
- Read a simple CSS rule and change text size, spacing, or a border deliberately.
- Recognise the existing rules that help the site fit smaller screens.
- Diagnose a selector mistake and check the result across pages and screen widths.

Start with the working Chapter 4 project. Its footer should contain the paragraph with `class="footer-note"`, and its skip link should be repaired. Keep your Chapter 4 backup outside the active project.

The only source file we will change is `static/css/site.css`. No new software or account is required.

## 5.1 Give the footer note a style

Run the preview from your project terminal:

```text
hugo server
```

Open the address Hugo reports and scroll to the footer. In your editor, open `static/css/site.css`. Add this rule at the end of the file, after the final closing brace:

```css
.footer-note {
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px solid #c5ccce;
  color: #46545b;
}
```

Save and return to the browser. Reload if necessary. You should see a fine line above the About note, space around that line, and a slightly softer colour for its ordinary text. The link keeps its existing link colour and underline.

Check the footer on Home and your first article. The same change should appear on both, because both pages use the same stylesheet and footer markup.

You have made your first targeted CSS change. Before adding anything else, understand how it found the right paragraph.

### Read the rule you just added

CSS stands for **Cascading Style Sheets**. It describes the presentation of HTML elements.

In this rule, `.footer-note` is the **selector**: it selects elements whose class list includes `footer-note`. The dot belongs to the CSS selector; it is not part of the HTML class name.

The declarations inside the braces follow the pattern `property: value;`. For example, `color: #46545b;` sets a text colour. Use a colon between the property and value, and a semicolon to end each declaration. [MDN: getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Getting_started)

Compare the two files without changing the HTML:

```html
<p class="footer-note">
```

```css
.footer-note {
  color: #46545b;
}
```

The second snippet illustrates the connection; do not add a second rule just to copy it.

> **First checkpoint:** the footer changed on more than one page, and you can explain how its HTML class connects to its CSS rule.

## 5.2 Know where CSS belongs in this Hugo project

Our starter uses a deliberately simple arrangement:

| Place | Role |
| --- | --- |
| `content/` | The Markdown writing and page metadata |
| `layouts/all.html` | The shared HTML structure and stylesheet link |
| `static/css/site.css` | The stylesheet you edit |
| `public/css/site.css` | The published copy after an ordinary build |

Hugo copies files from `static/` into the published site. In our default configuration, `static/css/site.css` becomes `css/site.css` within the output. The word `static` does not appear in its public URL. Hugo also supports an `assets/` directory for resources used through its asset-processing features; we do not need that workflow here. [Hugo: directory structure](https://gohugo.io/getting-started/directory-structure/)

Our layout already includes:

```html
<link rel="stylesheet" href="{{ "css/site.css" | relURL }}">
```

Keep that line intact. On the local preview at the site root, it normally produces a link to `/css/site.css`. All seven authored pages load the same CSS file. Hugo supplies the files and resolved address; the browser applies the CSS.

To see what the browser receives, open `/css/site.css` on the same preview address, for example `http://localhost:1313/css/site.css` when Hugo is using that address. You should see the stylesheet text, including your new rule. Return to the page afterwards.

Edit the source under `static/`, not the generated copy under `public/`. A build can replace the latter. Putting CSS into the article's Markdown body will not update the shared stylesheet.

Other Hugo themes may provide a custom-CSS setting or use an asset pipeline. Follow that theme's documented extension mechanism if you later adopt one. The filename and directory arrangement in this chapter belong to our starter; they are not a universal theme customisation recipe.

## 5.3 Learn only the selectors you meet here

You can understand most of our stylesheet with these examples:

| Selector | What it selects in this site |
| --- | --- |
| `body` | The document body |
| `h2` | All second-level headings |
| `.footer-note` | Elements carrying the `footer-note` class |
| `article img` | Images inside an article, including nested descendants |
| `header, main, footer` | Each of these three element types |
| `a:focus-visible` | Links when the browser determines focus should be visibly indicated |

The space in `article img` describes a relationship. The commas in `header, main, footer` group separate selectors. Keep that distinction when reading an agent's suggestion.

### Why the link did not take the footer's colour

Many text properties, including colour and font family, are inherited from a parent when the element has no applicable value of its own. The footer paragraph gets our new colour. Its link already has a colour from the starter's `a` rule, so it does not simply inherit the paragraph's colour.

When declarations compete on the same element and property, CSS uses the **cascade**. In our plain stylesheet, a class selector normally outweighs an element selector for otherwise comparable normal declarations. Between equally specific, otherwise comparable rules, the later declaration wins. “The last rule always wins” is therefore an unreliable shortcut. [MDN: handling CSS conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)

For now, inspect the relevant element and look for the property in the Styles or Rules panel. Overridden declarations are commonly crossed out. The Computed panel shows the resolved value. You do not need to calculate every possible specificity case.

Keep edits in the existing rule where practical. Adding repeated overrides or `!important` without understanding the competing rule makes a small stylesheet harder to maintain.

## 5.4 Make article text comfortable to read

Find the existing `body` rule. Add one declaration immediately after `font-family`:

```css
font-size: 1.125rem;
```

The complete rule should now be:

```css
body {
  margin: 0;
  background: #f5f3ed;
  color: #263238;
  font-family: system-ui, sans-serif;
  font-size: 1.125rem;
  line-height: 1.7;
}
```

Replace or edit the original rule; do not append this entire block as a second `body` rule.

Save and read a paragraph in your first article. With a root font size of 16 CSS pixels, `1.125rem` is 18 CSS pixels. Browser settings may give a different result: `rem` refers to the root element's font size, not to a guaranteed physical size. Text that has its own font-size rule, such as our main heading, will retain that separate sizing. [MDN: font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)

Our existing `system-ui, sans-serif` font stack asks for a system interface font and provides a generic fallback. It avoids needing a font download for this exercise. The existing unitless `line-height: 1.7` makes line spacing respond to the text size.

Try reading several sentences, not just the title. Is the text comfortable? Are navigation labels still usable? This value is a starting choice for our notebook, not a rule that all websites must use.

### Three units worth recognising

| Unit | Useful interpretation here |
| --- | --- |
| `rem` | Relative to the root font size; used for text and spacing |
| `px` | CSS pixels; used here for a thin border and focus outline |
| `%` | Relative to a reference size determined by the property; our image rule uses it to fit the containing area |

Keep the existing `clamp(...)` expressions for now. They already limit our heading size and content padding while allowing them to vary with the viewport. You need to recognise their purpose before you need to write them from memory.

## 5.5 Adjust spacing without changing the content

Find the existing `h2` rule and change `margin-top` from `2rem` to `2.5rem`:

```css
h2 {
  margin-top: 2.5rem;
  line-height: 1.3;
}
```

Save and compare two sections of the first article. The extra separation should help reveal where a new section begins. You did not add blank paragraphs or change the heading level.

Inspect a heading and look for the browser's box-model display. Its labels help distinguish three ideas:

| Property group | Where the space or line belongs |
| --- | --- |
| Margin | Outside the element's border |
| Border | Around the element's padding and content |
| Padding | Between the content and its border |

The footer exercise uses all three: its margin separates it from nearby content, its border provides a dividing line, and its padding separates that line from its text. Vertical margins between ordinary blocks can collapse rather than simply add together, so use the inspector when measured gaps surprise you.

Our starter begins with `* { box-sizing: border-box; }`. This makes specified box widths include padding and borders, which helps avoid accidentally making a box wider than intended. You can retain it without studying alternative box models now. [MDN: the box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)

> **Second checkpoint:** you have adjusted text and spacing through their existing rules, while retaining the article's headings and Markdown structure.

## 5.6 Understand the responsive behaviour already supplied

A content website needs to remain readable when the available width changes. Our starter already includes several useful rules. Leave them in place and observe what they do.

### A reading area with a maximum width

```css
header, main, footer {
  width: min(100% - 2rem, 48rem);
  margin-inline: auto;
}
```

In this page, the width is the smaller of the available width minus `2rem` and `48rem`. This provides side space on narrow screens and prevents the reading area expanding indefinitely on wide ones. `margin-inline: auto` centres these blocks in our current layout.

Avoid replacing this with a large fixed width simply to match one screenshot. Resize the preview and watch the content width change.

### Navigation that can wrap

```css
nav {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
```

The starter uses Flexbox to arrange the links. `flex-wrap: wrap` allows them to continue onto another line when there is not enough room. `gap` separates the items and wrapped lines. This small use of Flexbox is sufficient for our navigation; a full Flexbox course is unnecessary here. [MDN: flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)

### Images and code that fit the article

Chapter 2 supplied:

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

Keep these rules. The image can shrink to fit the article while retaining its proportions. Long preformatted code can scroll within its own area instead of forcing the whole page wider. These rules do not reduce the image file's download size.

A **media query** applies rules when a condition, such as viewport width, is met. You may encounter one in a theme, but our current changes do not need a new breakpoint. Flexible sizing and wrapping already address this chapter's layout needs. [MDN: responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)

### Check the result at more than one size

Check Home, your first article, and Resources. Narrow the browser window or use its responsive preview at about 360 CSS pixels wide, then try a wider view. Also increase browser zoom to 200% and check that you can still reach and read the content; return to your usual zoom afterwards.

Look for clipped words, links that overlap, distorted images, and page-wide sideways scrolling. Navigation wrapping is expected. A long code block scrolling within its own box is different from the entire page requiring horizontal scrolling.

A responsive preview is a useful check, but it does not reproduce every physical device. When available, inspect the site on an actual phone as well.

## 5.7 Diagnose one small mistake

Temporarily change the selector of your new rule from `.footer-note` to `.footer_note`, using an underscore. Leave its declarations and the HTML unchanged. Save and reload.

The line and new paragraph colour should disappear. The rule is valid CSS, but it no longer selects the paragraph. Hugo may report no error: it copies this stylesheet without checking whether its selectors match your intended HTML.

Inspect the paragraph and compare its class with the stylesheet selector character by character. The expected rule will not appear among its matching rules. Restore `.footer-note`, save, and confirm that the styling returns.

Use this short sequence when a change seems to do nothing:

1. **Check the file.** Did you save `static/css/site.css` in the project being previewed? Does the served CSS contain the edit?
2. **Check the match.** Does the selector describe the intended element? Is the class spelling exact?
3. **Check the declaration.** Are the property, colon, value, semicolon, and braces correct? Is another rule overriding it?

Temporary developer-tools edits are useful experiments, but normally disappear on reload. Save the intended correction in your source stylesheet.

| Symptom | Useful next check |
| --- | --- |
| The whole site suddenly looks unstyled. | Inspect the stylesheet link and whether its URL loads successfully. |
| Only one new declaration has no effect. | Check spelling and the property's accepted values; browsers commonly ignore invalid declarations. |
| The footer text changes but its link does not. | Inspect the existing `a` colour rule; this is expected in our example. |
| Styling changes on every page. | They share the stylesheet. Check the selector's scope before making it broader. |
| A saved change is absent from the served CSS. | Verify the active project and file, then try a reload that bypasses the browser cache. |

## 5.8 Finish with a small independent decision

Choose a heading gap that suits your article. Change only `h2`'s `margin-top` to `2rem`, `2.25rem`, or `2.5rem`. Keep the value you find easiest to read, and explain why in one sentence.

Check the footer, headings, and navigation on the three pages used above. Then use Tab to move through links. Keep the existing visible focus outline and the working Skip to content link. The `a:focus-visible` rule helps keyboard users locate their current link; removing it for a cleaner screenshot would make the site harder to use. [MDN: :focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)

For this exercise, retain our text and background colours, and retain link underlines. Future palette changes should include a contrast check; visual preference alone does not establish readability.

When reviewing an agent's styling proposal, ask three questions: which selector changes, which pages it affects, and how the result behaves at a narrow width. For example, “Add space above article section headings by editing the existing `h2` rule in `static/css/site.css`; preserve heading levels and check the article on a narrow screen” is a bounded task you can assess.

### Save your Chapter 5 checkpoint

Save your files, stop the preview, and copy the project to a sibling folder named `my-knowledge-site-ch05-backup`. Continue working in the original project.

## Completion check

- [ ] I can find the editable stylesheet and its served URL.
- [ ] I can read a selector and a `property: value;` declaration.
- [ ] My footer note has its intended border, spacing, and text colour.
- [ ] I adjusted body text and heading spacing in the existing rules.
- [ ] I repaired the deliberate selector mistake.
- [ ] I checked several pages at narrow and wide widths and with increased zoom.
- [ ] Links remain recognisable and keyboard focus remains visible.
- [ ] I saved a working Chapter 5 checkpoint.

This is enough CSS for our next steps. Grid layouts, animation, complex selectors, preprocessors, utility frameworks, and comprehensive theme design are outside this chapter's scope. Look up additional features when a concrete site requirement calls for them.

Chapter 6 introduces Git so that you can record changes, compare versions, and recover work more reliably than by copying whole project folders.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| Hugo cannot find `static/css/site.css`. | Check the path from the project folder: `static`, then `css`, then the file. Files under `static` are served from the site root. |
| An edit keeps disappearing. | Check whether you opened a copy under `public/`. That folder holds generated output; edit the source stylesheet under `static/`. |
| All styling vanishes after a rename. | The filename must match the stylesheet link in `layouts/all.html`. Changing one requires changing the other. |
| A declaration is ignored and nothing reports an error. | Hugo copies this file without checking it. Check the property name and its unit; browsers silently discard declarations they cannot parse. |
| One mistake affects rules below it. | A missing semicolon or brace lets the parser run on to the next one. Restore it and reload before making further edits. |
| Text size changes everywhere, not only in the article. | Check whether you edited the `body` rule. A narrower selector limits how far the change reaches. |
| Increased zoom breaks the layout. | Compare it with a narrow window; both should reflow. A fixed pixel width is the usual cause. |
| The keyboard focus outline has gone. | Restore the `a:focus-visible` rule. Keyboard users need it even when it is not part of your visual preference. |
| A comment appears on the page. | CSS comments use `/* ... */`. Markdown and HTML comment syntax do not apply in this file. |
| The colour differs from the value you typed. | Check that the value is a valid colour, then check whether a later rule of equal or greater specificity overrides it. |

## Completed stylesheet for comparison

This is a recovery reference for `static/css/site.css`, including the earlier starter rules. It reflects the guided values; retain your chosen heading gap if you completed the independent exercise. You do not need to memorise or retype this entire file.

```css
* { box-sizing: border-box; }

body {
  margin: 0;
  background: #f5f3ed;
  color: #263238;
  font-family: system-ui, sans-serif;
  font-size: 1.125rem;
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
h2 { margin-top: 2.5rem; line-height: 1.3; }
footer { padding-block: 1.5rem; }

a:focus-visible { outline: 3px solid #005b66; outline-offset: 4px; }
.skip-link { position: absolute; top: -10rem; left: 1rem; }
.skip-link:focus {
  top: 0.5rem;
  padding: 0.5rem 1rem;
  background: #ffffff;
}

article img {
  display: block;
  max-width: 100%;
  height: auto;
}

article pre {
  max-width: 100%;
  overflow-x: auto;
}

.footer-note {
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px solid #c5ccce;
  color: #46545b;
}
```

---

## Editorial note for the author (remove before publication)

The scope is intentionally limited to practical CSS literacy for the continuing Hugo website. Readers make three guided changes in one file: add the footer-note rule, set the body font size, and adjust heading spacing. Existing responsive and accessibility-related rules are explained at recognition level and retained. Do not expand this into a survey of CSS features or add a framework installation exercise.

The final stylesheet assumes the supplied starter and Chapter 2's image/code rules, plus Chapter 4's footer markup. Other themes need their own documented customisation path. Documentation was consulted on 17 September 2026.

Validation: the Chapter 4 project was copied for testing and updated with the completed stylesheet. Hugo 0.150.0 on Linux built successfully with warnings treated as errors at both a domain root and a `/my-knowledge-site/` base path. The stylesheet references and footer class were checked on all seven authored pages, and the published CSS was verified against its source. The completed stylesheet was also compared with the earlier version to confirm that it contains only the three intended changes, apart from formatting.

These checks establish build and file-path continuity, not visual correctness. A browser could not be provisioned in this environment, so responsive rendering, zoom, focus behaviour, and the visible effects of the exercises still require browser review. A representative beginner trial remains necessary before publication.
