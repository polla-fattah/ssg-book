---
title: "Publish in Multiple Languages"
description: "Chapter 16: a second language, right-to-left layout, translated navigation, and translations kept honest."
book_number: "16"
weight: 17
---

# Publish in Multiple Languages

Static Site Generators in the Age of AI

**Chapter 16**

Polla Fattah

---

## Today's goal

Add **Kurdish Sorani** as a second language: a Kurdish home page and About page at `/ckb/`.

- Translated **navigation** and a language switcher
- The right **language** and **text direction** for every page
- The layout working **right to left**
- The English site **unchanged** at its existing addresses

Arabic, or any other language, works the same way.

---

## By the end of today you can

- **Add** a second language without changing any English address
- **Set** each page's language and direction, and translate interface labels
- **Recognise** a layout rule that assumes one direction, and replace it
- **Say** what must be true before you publish a translation you cannot read

Start from Chapter 15 (branch `chapter-15`), on a **branch**. If you do not read the language, find **someone who does** first.

---

## Protect your addresses

In `hugo.toml`, replace the `languageCode` line and add:

```toml
defaultContentLanguage = 'en'
defaultContentLanguageInSubdir = false
```

- English stays the default, **where it is**: `/about/` stays `/about/`
- Kurdish pages appear under `/ckb/about/`
- `true` would move every English page to `/en/...` and **break every published link**

---

## Two languages, in hugo.toml

```toml
[languages]
  [languages.en]
    ...languageCode 'en', languageName, title, weight = 1...
  [languages.ckb]
    languageCode = 'ckb'
    languageName = 'کوردی'
    languageDirection = 'rtl'
    title = 'تێبینییەکانی من'
    weight = 2
```

---

## Check nothing moved

```text
hugo --minify --panicOnWarning
hugo server
```

- `ckb` is Kurdish Sorani; `weight` orders the languages; `rtl` is right to left
- Each language has its own **site title**

Visit Home, About, Articles, both projects, Resources, and Search: **all where they were**.

---

## Language and direction per page

`layouts/baseof.html` still says `<html lang="en">`: now **false** for Kurdish pages. Replace it with:

```html
<html lang="{{ .Site.Language.LanguageCode }}"
      dir="{{ .Site.Language.LanguageDirection | default "ltr" }}">
```

- `lang` guides **pronunciation** in screen readers, font choice, hyphenation, and search
- `dir` turns the page around: text, punctuation, and the start of each line
- `default "ltr"`: English has no `languageDirection`, so it gets one

---

## Interface strings

Create `i18n/en.toml` and `i18n/ckb.toml`, **with the same keys**:

```toml
nav_home = 'ماڵەوە'
nav_about = 'دەربارە'
nav_articles = 'وتارەکان'
nav_projects = 'پڕۆژەکان'
nav_resources = 'سەرچاوەکان'
nav_search = 'گەڕان'
```

Plus `nav_label` and `languages_label`. These are the words your **templates** say. A missing key gives an **empty label**, not an error.

---

## Language-aware navigation

Replace the navigation in `baseof.html`:

```html
<nav aria-label="{{ i18n "nav_label" }}">
  <a href="{{ "" | relLangURL }}">{{ i18n "nav_home" }}</a>
  <a href="{{ "about/" | relLangURL }}">{{ i18n "nav_about" }}</a>
  ...the same for articles, projects, resources, and search...
</nav>
{{ partial "language-links.html" . }}
```

- `i18n` reads the **current language's** file; `relLangURL` adds its **prefix**: `/about/` or `/ckb/about/`

---

## The link you might miss

`layouts/_partials/footer.html` has its own About link:

```html
Read <a href="{{ "about/" | relLangURL }}">about this notebook</a>.
```

Left as `relURL`, every Kurdish page would send readers to the **English** About page: a link that works, points somewhere real, and is still **wrong**.

When you change how links are built, **search the whole `layouts` folder**.

---

## A language switcher

`layouts/_partials/language-links.html`:

```html
{{ with .Translations }}
  <nav aria-label="{{ i18n "languages_label" }}" class="language-links">
    {{ range . }}
      <a href="{{ .RelPermalink }}" lang="{{ .Language.LanguageCode }}"
         hreflang="{{ .Language.LanguageCode }}">{{ .Language.LanguageName }}</a>
    {{ end }}
  </nav>
{{ end }}
```

`.Translations`: this page in other languages. None? **No switcher**.

---

## A left-to-right assumption

```css
.skip-link { position: absolute; top: -10rem; left: 1rem; }
```

On a right-to-left page, the skip link lands in the **wrong corner**.

| Physical: a side of the screen | Logical: relative to the text |
| --- | --- |
| `left`, `right` | `inset-inline-start`, `inset-inline-end` |
| `margin-left` | `margin-inline-start` |
| `text-align: left` | `text-align: start` |

---

## Replace it with a logical property

```css
.skip-link { position: absolute; top: -10rem; inset-inline-start: 1rem; }

:lang(ckb) {
  line-height: 1.9;
}
```

- `inset-inline-start`: the left in English, the **right** in Kurdish. One rule, both directions
- The rest of the stylesheet already uses `margin-inline` or vertical values
- `:lang(ckb)` works because each page now has a **real** `lang`

---

## Fonts: do not overpromise

- Our stack is still `system-ui, sans-serif`
- Current systems ship a font that **covers** Arabic script
- Covering is not rendering **well**: letter shapes, joining, and marks vary between fonts
- Check on **more than one device** before adding a downloadable font

A web font costs a **download on every visit**: a real trade, not an obvious improvement.

---

## Translate two pages

| File | Address |
| --- | --- |
| `content/about/index.md` | `/about/` |
| `content/about/index.ckb.md` | `/ckb/about/` |

Also `content/_index.ckb.md` for `/ckb/`. Each keeps the English fields, plus:

```yaml
params:
  source_checked: "2026-09-17"
```

---

## Be honest about the rest

The Kurdish home page links to what **exists** in Kurdish: the About page. Then it says plainly that the rest is in English, and links there:

```markdown
زۆربەی ناوەڕۆکی ئەم ماڵپەرە بە ئینگلیزییە: [ماڵپەری ئینگلیزی](../).
```

`../`, not `/`: it keeps the project prefix, and passes the **Chapter 14 link rule**.

A navigation that promises six Kurdish pages and delivers one **misleads**; a site that says what it covers does not.

---

## Check /ckb/

| Check | What should be true |
| --- | --- |
| Direction | Right to left; navigation starts on the right |
| The document | `lang="ckb"` and `dir="rtl"` |
| Links | Navigation **and footer** go to `/ckb/...` |
| Switcher | On the translated pages; **absent** on Articles |
| Skip link | Tab: it appears on the **right** |

---

## Translation you cannot read

Agents draft fluent translations fast; they cannot judge their own **correctness**.

> If you do not read the target language, do not publish the translation until someone who does has reviewed it.

- **Not** a second model
- **Not** a back-translation into English: it can turn an error into something that reads correctly
- **Not** your impression that it looks reasonable

---

## A bounded translation request

```text
Task: Draft a Kurdish Sorani translation of content/about/index.md.
Create exactly one new file: content/about/index.ckb.md

Keep the front-matter field names in English and translate only their values.
Keep draft: true. Keep the heading structure and the number of paragraphs.
Translate only what the English page says. Do not add, remove, or improve
any claim. Where a term has no settled Kurdish equivalent, keep the English
term and list it at the end of your reply with your reasoning.
```

English field names keep templates working; the fixed structure makes versions **comparable**.

---

## Review, then date it

- Give the reviewer the **English page** alongside the draft
- Ask whether anything was **added, dropped, or softened**, not only whether it reads well
- Start with the list of uncertain terms

Set `draft: false` and `source_checked` **only** when someone has actually read it. The date **claims** a review happened.

---

## Translations go stale

The English page changes; nothing tells the Kurdish page.

1. Changed an English page? Open its translation **in the same commit**
2. Can update it? Do, and set `source_checked` to today
3. Cannot? **Leave the date**: a stale date is the signal
4. Before a review round, list the oldest dates

```text
grep -r 'source_checked' content/
```

---

## A fourth check in checks.yaml

```yaml
- name: Check that translations record a source check
  run: |
    status=0
    for page in $(find content -name '*.ckb.md'); do
      if ! grep -q 'source_checked:' "$page"; then
        echo "Missing source_checked: $page"
        status=1
      fi
    done
    exit "$status"
```

---

## What the check can and cannot say

- Added after the description check, it confirms a date is **present**, not that a review happened or the date is **true**
- The description rule does not examine `index.ckb.md` files at all
- That is why the reviewer rule is a **rule**, not a workflow step

Update `AGENTS.md`: the `i18n` files, the `.ckb.md` pages, and the switcher; and one agreement:

```markdown
- Translations keep English front-matter field names and translate only their values.
```

---

## Propose it

```text
git switch -c add-kurdish
git add hugo.toml layouts/baseof.html layouts/_partials/language-links.html
git add layouts/_partials/footer.html i18n/en.toml i18n/ckb.toml
git add static/css/site.css content/_index.ckb.md content/about/index.ckb.md
git add .github/workflows/checks.yaml AGENTS.md
git commit -m "Add Kurdish as a second language with translated navigation"
git push -u origin add-kurdish
```

Read Files changed, especially `hugo.toml`. Merge, then check **both** languages live, and one **old** English address.

---

## Try it yourself

Translate one more page, most usefully **Search**: its labels are already translated, and its list simply shows the Kurdish pages that exist.

Or add a **third** language, and see how much of this was general and how much was about Kurdish.

Either way: a **reviewer** before publication, and a truthful `source_checked`.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| English pages moved to `/en/...` | `defaultContentLanguageInSubdir = false` |
| The Kurdish page reads left to right | `languageDirection` and the `dir` attribute |
| A navigation label is blank | The key is missing from one `i18n` file |
| Kurdish links lead to English pages | `relURL` instead of `relLangURL`, footer too |
| Boxes instead of Kurdish letters | Test on another system before blaming the site |

---

## Completion check

- Every English address from before still works
- Each page declares its own `lang` and `dir`
- Labels come from `i18n`; navigation **and footer** use `relLangURL`
- The skip link uses `inset-inline-start`, and sits correctly in both directions
- The Kurdish home page links only to what exists in Kurdish
- I can state the condition for publishing a translation I cannot read
- Every translation has a `source_checked` date, and the check passes

---

# Next: Add Interactive Features Responsibly

Chapter 17: a modest interactive feature, and where a visitor's information goes.

**polla.dev/ssg-book**
