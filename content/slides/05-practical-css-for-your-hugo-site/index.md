---
title: "Practical CSS for Your Hugo Site"
description: "Chapter 5: changing appearance deliberately, starting with the footer-note class."
book_number: "5"
weight: 6
---

# Practical CSS for Your Hugo Site

Static Site Generators in the Age of AI

**Chapter 5**

Polla Fattah

---

## Today's goal

Three small, deliberate changes:

- The footer note sits below a **thin rule**, in quieter text
- Body text reads a little **larger**
- Article section headings get **more space** above them

Everything else should look as it did after Chapter 4.

Enough CSS to customise this site and **check an agent's changes**; not a design course.

---

## By the end of today you can

- **Find** the stylesheet and explain how pages load it
- **Read** a CSS rule and change size, spacing, or a border on purpose
- **Recognise** the rules that help the site fit small screens
- **Diagnose** a selector mistake, and check across pages and widths

The only file you change today is `static/css/site.css`.

---

## Style the footer note

Start `hugo server` (or checkout companion branch `chapter-04` in `ssg-playground`), open `static/css/site.css`, and add at the **end**:

```css
.footer-note {
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px solid #c5ccce;
  color: #46545b;
}
```

A fine line, space around it, softer text. Check Home **and** your article.

---

## Read the rule

- `.footer-note` is the **selector**: elements whose class includes `footer-note`
- The dot belongs to CSS, not to the class name
- Each **declaration** is `property: value;`

```html
<p class="footer-note">
```

```css
.footer-note { color: #46545b; }
```

---

## Where CSS lives in this project

| Place | Role |
| --- | --- |
| `content/` | Your writing and page metadata |
| `layouts/all.html` | Shared structure, with the stylesheet link |
| `static/css/site.css` | **The stylesheet you edit** |
| `public/css/site.css` | The generated copy: never edit it |

Files in `static/` are copied to the site root: the public address is `/css/site.css`, with no `static`.

---

## How every page gets it

```html
<link rel="stylesheet" href="{{ "css/site.css" | relURL }}">
```

- Keep that line in the layout **intact**
- All seven pages load the **same** file
- Hugo supplies the file; the **browser** applies the CSS

Open `http://localhost:1313/css/site.css` to see what the browser receives, including your new rule.

---

## Selectors you meet here

| Selector | Selects |
| --- | --- |
| `body` | The document body |
| `h2` | Every second-level heading |
| `.footer-note` | Elements with the `footer-note` class |
| `article img` | Images **inside** an article |
| `header, main, footer` | **Each** of these three elements |

A **space** describes a relationship; a **comma** groups separate selectors.

---

## Why the link kept its colour

- Colour and font are **inherited** from the parent, unless the element has its own value
- The footer link already has a colour from the `a` rule

When rules compete, the **cascade** decides: a class usually beats an element selector; among equals, the later rule wins.

Inspect the element: crossed-out declarations lost. Avoid `!important`.

---

## Make text comfortable to read

Add `font-size` to the **existing** `body` rule; do not add a second one:

```css
body {
  /* margin, background, and color stay as they are */
  font-family: system-ui, sans-serif;
  font-size: 1.125rem;
  line-height: 1.7;
}
```

Usually 18 CSS pixels. Read whole paragraphs, not just the title.

---

## Three units worth recognising

| Unit | Here it means |
| --- | --- |
| `rem` | Relative to the root font size: text and spacing |
| `px` | CSS pixels: a thin border, the focus outline |
| `%` | Relative to a reference size: fitting an image to the article |

- `rem` follows the reader's browser settings, not a fixed physical size
- A unitless `line-height: 1.7` scales with the text
- Leave the existing `clamp(...)` values alone for now

---

## Adjust spacing

In the existing `h2` rule, change `margin-top` from `2rem` to `2.5rem`:

```css
h2 {
  margin-top: 2.5rem;
  line-height: 1.3;
}
```

New sections are easier to spot, and you added **no blank paragraphs** and changed **no heading levels**.

---

## Margin, border, padding

| Part | Where it sits |
| --- | --- |
| Margin | **Outside** the border |
| Border | Around the padding and content |
| Padding | **Between** the content and its border |

The footer note uses all three. Vertical margins can **collapse**: measure with the inspector's box model.

`* { box-sizing: border-box; }` keeps padding and borders inside a box's width.

---

## A reading area with a maximum width

```css
header, main, footer {
  width: min(100% - 2rem, 48rem);
  margin-inline: auto;
}
```

- The **smaller** of the available width minus `2rem`, or `48rem`
- Side space on phones; no endless lines on wide screens
- `margin-inline: auto` centres the blocks

Never replace it with a fixed width to match one screenshot.

---

## Navigation that wraps

```css
nav { display: flex; flex-wrap: wrap; gap: 1rem; }
```

- **Flexbox** arranges the links in a row
- `flex-wrap: wrap` moves them to a new line when space runs out
- `gap` separates items and lines

Chapter 2's image and code rules also stay: images shrink, long code scrolls in its own box.

---

## Check more than one size

On Home, your article, and Resources:

1. Narrow the window, or toggle responsive preview (**Ctrl + Shift + M** / **Cmd + Shift + M**) near **360 pixels**
2. Try a wide view
3. Zoom to **200%**: can you still read and reach everything?

Look for clipped words, overlapping links, distorted images, and **sideways scrolling of the whole page**. Wrapping navigation is fine.

A real phone beats any simulation.

---

## Break a selector on purpose

1. Change `.footer-note` to `.footer_note`, with an underscore
2. Save and reload: the line and colour **disappear**
3. Hugo reports **nothing**: it copies CSS without checking it
4. Inspect the paragraph: the rule is not among its matches
5. Restore `.footer-note` and confirm the style returns

> Valid CSS that selects nothing still does nothing.

---

## When a change does nothing

1. **Check the file.** Saved, in the project being previewed? Does the served CSS contain it?
2. **Check the match.** Does the selector describe that element? Exact spelling?
3. **Check the declaration.** Property, colon, value, semicolon, braces. Is another rule winning?

Inspector edits vanish on reload: save the fix in the source.

---

## Choose your heading gap

Change only `h2`'s `margin-top`: `2rem`, `2.25rem`, or `2.5rem`.

- Keep the one **you** find easiest to read, and say why in one sentence
- Tab through the links: keep the **focus outline** and the skip link
- Keep the colours and **link underlines**

Any future palette change needs a **contrast check**, not just taste.

---

## Review an agent's styling proposal

Ask three questions:

- Which **selector** changes?
- Which **pages** does it affect?
- How does it behave at a **narrow** width?

```text
Add space above article section headings by editing the
existing h2 rule in static/css/site.css. Preserve heading
levels and check the article on a narrow screen.
```

---

## Save your checkpoint

Stop the preview and copy the folder to `my-knowledge-site-ch05-backup`.

| Rule in `static/css/site.css` | Today's change |
| --- | --- |
| `.footer-note` | New rule: border, spacing, colour |
| `body` | `font-size: 1.125rem` |
| `h2` | `margin-top` of your choice |

Keep working in the original folder.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| All styling vanished | The stylesheet link, and whether `/css/site.css` loads |
| An edit keeps disappearing | You opened the copy under `public/` |
| Rules below a mistake stop working | A missing semicolon or brace |
| The focus outline has gone | Restore the `a:focus-visible` rule |
| A comment appears on the page | CSS comments are `/* ... */` |

---

## Completion check

- I can find the stylesheet and its served address
- I can read a selector and a `property: value;` declaration
- My footer note has its border, spacing, and colour
- I changed body text and heading spacing in the existing rules
- I repaired the deliberate selector mistake
- I checked narrow, wide, and 200% zoom
- Links are recognisable and keyboard focus is visible
- I saved a Chapter 5 checkpoint

---

# Next: Track and Recover Your Hugo Site with Git

Chapter 6: record changes, compare versions, and recover work without copying whole folders.

**polla.dev/ssg-book**
