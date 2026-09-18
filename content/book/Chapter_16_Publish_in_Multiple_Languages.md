---
title: "Chapter 16 — Publish in Multiple Languages"
weight: 16
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*The added CI check was verified against a fixture. No Hugo build, browser review, right-to-left rendering check, native-speaker review of the Kurdish strings, or beginner trial yet.*

Your notebook is in English. If some of your readers would rather read Kurdish, or if your work belongs to a place where two languages are normal, the site should be able to say the same things twice.

In this chapter you will add Kurdish Sorani as a second language, translate the navigation and two pages, and give the document the language and text direction a browser needs. Kurdish Sorani is written in a Perso-Arabic script and runs right to left, so this is also the first time your layout has to work in the other direction. You will find and repair the one stylesheet rule that assumes left to right.

The visible result is a Kurdish home page and About page at `/ckb/`, reachable from a language link, with the English site unchanged at its existing addresses. If you would rather use Arabic, or any other second language, every step works the same way; only the language code and the strings change.

## What you will be able to do

By the end, you should be able to:

- Add a second language without changing any existing English address.
- Set each page's language and text direction, and translate interface labels.
- Recognise a layout rule that assumes one text direction, and replace it.
- Say what must be true before you publish a translation you cannot read.

Start from the completed Chapter 15 checkpoint with a clean working tree on `main`. Work on a branch and propose the result through a pull request, as in Chapters 14 and 15.

One requirement is not technical. If you do not read the second language, you need someone who does, and Section 16.6 explains why that is not optional. Choose a language you can have reviewed before you begin.

## 16.1 Add a second language without changing your existing addresses

Your English pages are published and linked. Chapter 3 established that addresses should be stable, so the first decision is the one that protects them.

Open `hugo.toml`. Replace the `languageCode` line, keep everything else, and add the language settings:

```toml
baseURL = 'https://YOUR-USERNAME.github.io/my-knowledge-site/'
title = 'My Knowledge Notebook'
defaultContentLanguage = 'en'
defaultContentLanguageInSubdir = false

[params]
description = 'Learning notes, small projects, and useful references, published as a static website.'

[languages]
  [languages.en]
    languageCode = 'en'
    languageName = 'English'
    title = 'My Knowledge Notebook'
    weight = 1
  [languages.ckb]
    languageCode = 'ckb'
    languageName = 'کوردی'
    languageDirection = 'rtl'
    title = 'تێبینییەکانی من'
    weight = 2
```

Two settings carry the whole decision. `defaultContentLanguage = 'en'` says English is the default, and `defaultContentLanguageInSubdir = false` says the default language stays where it is. English pages keep `/about/`; Kurdish pages will appear under `/ckb/about/`. Setting that second value to `true` would move every English page to `/en/...` and break every address you have published and every link anyone has saved.

`ckb` is the language code for Kurdish Sorani. `weight` sets the order languages are listed in. `languageDirection = 'rtl'` records that this language runs right to left, which Section 16.2 will use. Each language has its own `title`, so the site name itself is translated. [Hugo: multilingual mode](https://gohugo.io/content-management/multilingual/)

Build and preview:

```text
hugo --minify --panicOnWarning
hugo server
```

Check that the English site is exactly as it was. Visit the home page, About, Articles, the two projects, Resources, and Search. Nothing should have moved. There is no Kurdish content yet, so `/ckb/` has nothing to show.

> **First checkpoint:** the site has two configured languages and every English address is unchanged.

## 16.2 Give each page its language and direction

Open `layouts/baseof.html` and look at its first two lines. The language is written into the file:

```html
<html lang="en">
```

That was true when there was one language. Now it is a statement the Kurdish pages would make incorrectly, and it matters more than it looks: the `lang` attribute tells a screen reader which pronunciation to use, helps a browser choose a font, and affects how text is hyphenated and searched.

Replace that line with:

```html
<html lang="{{ .Site.Language.LanguageCode }}" dir="{{ .Site.Language.LanguageDirection | default "ltr" }}">
```

The `dir` attribute is what actually turns the page around. It is not decoration: it tells the browser that text, punctuation, and the natural start of a line all run from the right. `default "ltr"` supplies a value for English, which has no `languageDirection` in the configuration, and is the same `default` idea you could use anywhere a setting might be absent.

Rebuild and view the source of an English page. It should read `lang="en"` and `dir="ltr"`. We cannot check the Kurdish side until there is a Kurdish page, which is Section 16.5.

## 16.3 Translate the navigation with language-aware links

The navigation has two problems in a second language. Its labels are English words, and its destinations are built with `relURL`, which knows about the project path but not about the language.

Fix the labels first. Create a folder named `i18n` at the project root, beside `content` and `layouts`. Inside it, create `i18n/en.toml`:

```toml
nav_home = 'Home'
nav_about = 'About'
nav_articles = 'Articles'
nav_projects = 'Projects'
nav_resources = 'Resources'
nav_search = 'Search'
nav_label = 'Main navigation'
languages_label = 'Languages'
```

Then create `i18n/ckb.toml` with the same keys:

```toml
nav_home = 'ماڵەوە'
nav_about = 'دەربارە'
nav_articles = 'وتارەکان'
nav_projects = 'پڕۆژەکان'
nav_resources = 'سەرچاوەکان'
nav_search = 'گەڕان'
nav_label = 'ڕێنیشاندەری سەرەکی'
languages_label = 'زمانەکان'
```

These files hold **interface strings**: the words your templates say, rather than the words you write as content. Keep the keys identical in both files; a key present in one file and missing from the other produces an empty label rather than an error. [Hugo: multilingual translation of strings](https://gohugo.io/content-management/multilingual/)

Now replace the whole navigation block in `layouts/baseof.html` with this version:

```html
<nav aria-label="{{ i18n "nav_label" }}">
  <a href="{{ "" | relLangURL }}">{{ i18n "nav_home" }}</a>
  <a href="{{ "about/" | relLangURL }}">{{ i18n "nav_about" }}</a>
  <a href="{{ "articles/" | relLangURL }}">{{ i18n "nav_articles" }}</a>
  <a href="{{ "projects/" | relLangURL }}">{{ i18n "nav_projects" }}</a>
  <a href="{{ "resources/" | relLangURL }}">{{ i18n "nav_resources" }}</a>
  <a href="{{ "search/" | relLangURL }}">{{ i18n "nav_search" }}</a>
</nav>
{{ partial "language-links.html" . }}
```

Two functions are doing the work. `i18n` looks a key up in the current language's file. `relLangURL` is `relURL` with the language prefix added, so the same template line produces `/about/` in English and `/ckb/about/` in Kurdish. Leaving `relURL` there would have sent every Kurdish visitor back to the English pages. [Hugo: relLangURL](https://gohugo.io/functions/urls/rellangurl/)

One more link needs the same treatment, and it is not in the file you were just editing. Open `layouts/_partials/footer.html` and change its About link:

```html
Read <a href="{{ "about/" | relLangURL }}">about this notebook</a>.
```

The footer appears on every page in both languages. Left as `relURL`, it would have sent Kurdish readers to the English About page from the bottom of every Kurdish page — a link that works, points somewhere real, and is still wrong. When you change how links are built, search the whole `layouts` folder rather than only the file in front of you.

Its visible wording stays English for now. That is remaining translation work rather than a defect: like the five untranslated pages, it is a known gap, and Section 16.5 is about stating such gaps rather than hiding them.

Create the language switcher as `layouts/_partials/language-links.html`:

```html
{{ with .Translations }}
  <nav aria-label="{{ i18n "languages_label" }}" class="language-links">
    {{ range . }}
      <a href="{{ .RelPermalink }}" lang="{{ .Language.LanguageCode }}" hreflang="{{ .Language.LanguageCode }}">{{ .Language.LanguageName }}</a>
    {{ end }}
  </nav>
{{ end }}
```

`.Translations` gives the other language versions of **this page**, so the link goes to the same page in the other language rather than to a language home page. The `lang` attribute on each link matters here too: the word `کوردی` is Kurdish even when it appears on an English page, and marking it lets a screen reader pronounce it correctly.

Because of `with`, a page with no translation shows no switcher at all. That is the honest behaviour: offering a Kurdish link on a page that has no Kurdish version would promise something that does not exist. The consequence, which Section 16.5 returns to, is that readers switch language from the pages that have both versions.

The stylesheet needs nothing new for the switcher beyond a little separation. Add this to `static/css/site.css`:

```css
.language-links {
  margin-top: 0.5rem;
  font-size: 0.9375rem;
}
```

Rebuild and check the English pages. The labels should be unchanged English words, every navigation link should still work, and no switcher should appear yet.

## 16.4 Find and fix the rule that assumes left to right

Before adding Kurdish content, look at the stylesheet for rules that describe positions as left or right rather than as start and end. There is one:

```css
.skip-link { position: absolute; top: -10rem; left: 1rem; }
```

That rule came from the Chapter 1 starter and has been correct ever since, because English begins on the left. On a right-to-left page it puts the Skip to content link in the far corner from where reading begins, which is precisely the wrong place for the first thing a keyboard user reaches.

CSS has two families of properties for this. **Physical** properties name a side of the screen: `left`, `right`, `margin-left`, `padding-right`, `text-align: left`. **Logical** properties name a position relative to the text direction: `inset-inline-start`, `margin-inline-start`, `text-align: start`. A logical property follows the direction; a physical one does not.

Replace that one rule with:

```css
.skip-link { position: absolute; top: -10rem; inset-inline-start: 1rem; }
```

`inset-inline-start` means the beginning of the line: the left in English, the right in Kurdish. One property, both directions, no duplicated rules and no second stylesheet.

Look through the rest of the file and satisfy yourself that nothing else needs changing. The reading column already uses `margin-inline: auto`, which you met in Chapter 5, and the spacing rules use `padding-block` or symmetric values. The remaining `margin-top` and `border-top` values are vertical, so text direction does not affect them.

Kurdish Sorani also reads more comfortably with a little more space between lines than English. Add this rule:

```css
:lang(ckb) {
  line-height: 1.9;
}
```

The `:lang()` selector matches elements whose language is the one named, which works because Section 16.2 put a real `lang` attribute on the document.

A word about fonts, because it is easy to overpromise here. Our stack is still `system-ui, sans-serif` from Chapter 1. Every current desktop and mobile operating system ships a font that covers Arabic script, so the text should render without downloading anything. What you cannot assume is that it renders *well*: letter shapes, joining, and diacritic placement vary between system fonts, and a font that looks correct on your computer may not on someone else's. Check the Kurdish pages on more than one device before deciding that a downloadable font is necessary. If you do add one later, the cost is a download on every visit, which is a real trade rather than an obvious improvement.

## 16.5 Translate two pages, and be honest about the rest

Hugo identifies a page's language from its filename. A file with no language code belongs to the default language, which is why none of your existing files need renaming.

| File | Language | Address |
| --- | --- | --- |
| `content/about/index.md` | English, by default | `/about/` |
| `content/about/index.ckb.md` | Kurdish | `/ckb/about/` |

Create `content/_index.ckb.md` for the Kurdish home page and `content/about/index.ckb.md` for the Kurdish About page. Give each the same front-matter fields the English version has, with `title` and `description` in Kurdish, and add one new field:

```yaml
---
title: "دەربارە"
description: "..."
draft: false
params:
  source_checked: "2026-09-17"
---
```

`source_checked` records the date on which this translation was last compared with its English source. Section 16.7 explains how it is used. Fill in the description and body in your second language; the comparison files at the end of the chapter show the expected shape.

Write the Kurdish home page to link only to what actually exists in Kurdish. Your English home page has an Explore the notebook list of four sections; the Kurdish one should link to the Kurdish About page, and then say plainly that the rest of the notebook is in English, with a link to the English home page. Do not copy the English list of links across, because five of those destinations have no Kurdish version.

This is the ordinary condition of a bilingual site, not a failure. A site where one language is complete and the other covers an entry point is honest as long as it says so. What misleads a reader is a navigation that promises six Kurdish pages and delivers one.

Build and preview:

```text
hugo --minify --panicOnWarning
hugo server
```

Open `/ckb/`. Check all of the following:

| Check | What should be true |
| --- | --- |
| Text direction | The page reads right to left, and the navigation begins on the right |
| The document | Its source shows `lang="ckb"` and `dir="rtl"` |
| Navigation labels | Kurdish, from `i18n/ckb.toml` |
| Navigation destinations | Each goes to `/ckb/...`, not to the English page |
| The footer link | It also goes to `/ckb/about/`, not to `/about/` |
| The language switcher | It appears on the Kurdish home and About pages, and on their English versions |
| An English-only page | Articles shows no switcher, because it has no translation |
| The skip link | Press Tab; it appears at the right-hand side, where reading begins |
| Line spacing | The Kurdish text is a little more open than the English |

> **Second checkpoint:** two Kurdish pages render right to left with translated navigation, and the English site is untouched.

## 16.6 Use an agent to draft a translation, and require a reviewer

An agent can produce a fluent draft translation quickly. Whether it produced a correct one is a separate question, and it is not one the agent can answer about its own work.

Everything Chapter 13 established applies here, with one addition that is stricter than anything in that chapter. Chapter 13 asked you to check an agent's claims against a source you could read. A translation into a language you cannot read removes that ability entirely. Fluent, confident, and wrong looks exactly like fluent, confident, and right.

So the rule for this chapter is plain. **If you do not read the target language, do not publish the translation until someone who does has reviewed it.** Not a second model, not a back-translation into English, and not your own impression that it looks reasonable. A back-translation can turn an error into something that reads correctly in English, which is worse than no check at all.

If you do read the language, you are the reviewer, and the work is ordinary editing.

A bounded request, following Chapter 13's pattern, looks like this:

```text
Read AGENTS.md and content/about/index.md before editing.

Task: Draft a Kurdish Sorani translation of that page.
Create exactly one new file: content/about/index.ckb.md

Keep the front-matter field names in English and translate only their values.
Keep draft: true. Keep the heading structure and the number of paragraphs.
Translate only what the English page says. Do not add, remove, or improve
any claim, and do not localise examples into different ones.
Where a term has no settled Kurdish equivalent, keep the English term and
list it at the end of your reply with your reasoning.

Change no other file. Do not stage, commit, push, or deploy.
Finish by listing the file you created and every term you were unsure about.
```

Three things in that request matter more than the rest. Keeping the field names in English prevents a translated key that no template reads. Holding the structure fixed makes the two versions comparable line by line. And asking for the uncertain terms produces the list your reviewer should look at first.

When the draft comes back, note that `draft: true` keeps it out of the built site. Send the file, or the rendered draft preview, to your reviewer. Give them the English page alongside it, and ask specifically whether anything has been added, dropped, or softened, not merely whether the language reads well.

Set `draft: false` and `source_checked` to the review date when, and only when, someone has actually read it. The date claims a review happened; do not write one you cannot support. This is the same discipline as Chapter 13's unsupported sentence, in a setting where you have fewer ways to catch the mistake yourself.

## 16.7 Track which translations have gone stale

A translation is correct on the day it is made. The English page then changes, and nothing tells the Kurdish page about it.

This is the maintenance cost of a second language, and it is the part people underestimate. Every edit to an English page that has a translation creates a decision: update the translation, or accept that it now says something slightly different.

The `source_checked` field is the record that makes the question visible. Establish the habit as a rule for yourself:

1. When you change an English page that has a translation, open the translation in the same commit.
2. If you can update it, do so and set `source_checked` to today.
3. If you cannot, leave the date alone. The stale date is the signal.
4. Before a review round, list the translations whose dates are oldest.

You can see the state of things at any time with:

```text
grep -r 'source_checked' content/
```

A date from months ago on a page whose English source you have edited twice since is exactly what you want to be able to find.

Hugo can also report when a file was last changed, through `.Lastmod` and, with configuration, from Git history. Comparing a page's own modification time with its translation's would automate part of this. We are not doing that here, because the comparison needs care about which changes matter: correcting a typo in an English paragraph does not invalidate its translation, and a build-time comparison cannot tell the difference. The date you set by hand records a judgement, which is the thing worth recording.

## 16.8 Check the result, propose it, and save

Add one step to `.github/workflows/checks.yaml`, after the existing description check, so that a translation without a recorded source check cannot be merged:

```yaml
      - name: Check that translations record a source check
        shell: bash
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

This is the same crude, readable kind of check as the three in Chapter 14, and it has the same honest limit: it confirms that a date is present, not that a review happened or that the date is true. Only you can establish that, which is why the rule in Section 16.6 is a rule and not a workflow step. Run it locally first, as Chapter 14 taught:

```text
grep -r 'source_checked' content/
```

Update the file map in `AGENTS.md`, under Files:

```markdown
- Interface strings are in i18n/en.toml and i18n/ckb.toml.
- Kurdish pages are the .ckb.md files beside their English versions.
- The language switcher is layouts/_partials/language-links.html.
```

Add one working agreement:

```markdown
- Never change a translated page's meaning to match a template. Translations keep English front-matter field names and translate only their values.
```

Then build, review, and propose the whole change:

```text
hugo --minify --panicOnWarning
git switch -c add-kurdish
git status
git add hugo.toml layouts/baseof.html layouts/_partials/language-links.html
git add layouts/_partials/footer.html
git add i18n/en.toml i18n/ckb.toml static/css/site.css
git add content/_index.ckb.md content/about/index.ckb.md
git add .github/workflows/checks.yaml AGENTS.md
git diff --cached
git commit -m "Add Kurdish as a second language with translated navigation"
git push -u origin add-kurdish
```

Open the pull request and read the checks. The build and all four rule checks should pass. Note which of them your Kurdish files are not examined by: the description rule looks at `content/articles/*/index.md` and `content/projects/*/index.md`, and a filename such as `index.ckb.md` matches neither. Read Files changed yourself, paying particular attention to `hugo.toml`, then merge and verify the live site in both languages. Check one English address you had published before this chapter and confirm it still works.

Finally, make one improvement of your own. Translate one more page, most usefully the Search page, since its interface labels are already translated and its generated list will simply show the Kurdish pages that exist. Or add a third language, which will show you immediately how much of this arrangement was general and how much was about Kurdish in particular.

## Completion check

- [ ] Every English address published before this chapter still works.
- [ ] I can explain what `defaultContentLanguageInSubdir = false` protects.
- [ ] Each page declares its own `lang` and `dir`.
- [ ] Navigation labels come from the `i18n` files, and its links use `relLangURL`.
- [ ] The footer's About link is language-aware too, not only the navigation's.
- [ ] I replaced the physical `left` with a logical `inset-inline-start` and can say why.
- [ ] Two Kurdish pages render right to left with the skip link in the correct corner.
- [ ] The Kurdish home page links only to pages that exist in Kurdish.
- [ ] The language switcher appears on translated pages and is absent elsewhere.
- [ ] I can state the condition for publishing a translation I cannot read.
- [ ] Every translation records a `source_checked` date, and the new check passes.

This is enough multilingual publishing for our next steps. Per-language taxonomies, translated URL segments, machine-translation pipelines, language detection and redirection, downloadable fonts, and full mixed-direction typography are outside this chapter's scope. Add the second language properly before adding a third.

Chapter 17 adds a modest interactive feature, which will raise the question of where a visitor's information goes and what a static site can and cannot do by itself.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| Every English page moved to `/en/...`. | `defaultContentLanguageInSubdir` is `true`. Set it to `false` and rebuild; the old addresses should return. |
| `/ckb/` is not found. | There is no Kurdish content yet, or the filename lacks the `.ckb` part before `.md`. |
| The Kurdish page reads left to right. | Check `languageDirection = 'rtl'` in the configuration and that `dir` is in the `html` tag in `layouts/baseof.html`. |
| A navigation label is blank. | That key is missing from one `i18n` file. Keep the same keys in both. |
| Kurdish navigation links lead to English pages. | Those links still use `relURL`. They need `relLangURL`. |
| The footer sends Kurdish readers to the English About page. | `layouts/_partials/footer.html` has its own link. Change it to `relLangURL` as well. |
| The site title is in the wrong language. | Give each language its own `title` inside its `[languages.xx]` table. |
| The skip link appears in the far corner. | Replace `left: 1rem` with `inset-inline-start: 1rem` in `.skip-link`. |
| No language switcher appears anywhere. | It only appears on pages that have a translation. Check the Kurdish home or About page. |
| The switcher appears on a page with no translation. | Confirm the `with .Translations` wrapper survived the paste. |
| Kurdish text shows as boxes or disconnected letters. | The operating system lacks a suitable font. Test elsewhere before concluding the site is at fault. |
| The new check fails on a page you translated. | Add `source_checked` to its front matter, and only date it from a review that happened. |
| A translation reads well but says something different. | That is what a reviewer is for. A fluent draft is not evidence of an accurate one. |

An automated check can confirm that a translation exists and records a date. It cannot confirm that the two language versions say the same thing.

## Comparison files

Your own wording will differ, and the Kurdish here should be checked by a speaker before you adopt it. These show the expected shape and scale.

`content/_index.ckb.md`:

```markdown
---
title: "بەخێربێن"
description: "تێبینییەکانی فێربوون و پڕۆژە بچووکەکان."
draft: false
params:
  source_checked: "2026-09-17"
---

ئەمە ماڵپەری تێبینییەکانی منە.

## دەستپێک

- [دەربارە](about/) — دەربارەی ئەم ماڵپەرە.

## زمانی ئینگلیزی

زۆربەی ناوەڕۆکی ئەم ماڵپەرە بە ئینگلیزییە: [ماڵپەری ئینگلیزی](../).
```

The link to the English home page is written as `../`, not `/`. From `/ckb/` that resolves to the site root, and it keeps the project-path prefix when the site is published in a subdirectory. A root-relative `/` would also fail the Chapter 14 link rule, which is the check earning its place.

`content/about/index.ckb.md`:

```markdown
---
title: "دەربارە"
description: "دەربارەی ئەم ماڵپەرە و ئەوەی لێی دەدۆزیتەوە."
draft: false
params:
  source_checked: "2026-09-17"
---

ئەمە ماڵپەرێکی کەسییە بۆ تۆمارکردنی تێبینییەکانی فێربوون.
```

Note what the Kurdish home page does not do: it does not reproduce the four-item Explore the notebook list from the English home page, because only About exists in Kurdish. Its last section says so directly rather than leaving a reader to discover it.

---

## Editorial note for the author — remove before publication

Every Kurdish string here, in the `i18n` file and the comparison pages, must be reviewed by a Sorani speaker before publication. The navigation terms are standard web-interface words and should be low risk; the page bodies are short and deliberately plain, but they remain unreviewed machine-produced Kurdish in a chapter whose own rule forbids exactly that. Treat the chapter as failing its own standard until that review happens. Arabic is offered in the opening for authors without a Sorani reviewer.

Section 16.1 leads because it is the irreversible decision. Translation by filename with `defaultContentLanguageInSubdir = false` preserves every published English address; translation by directory would have moved the whole tree and invalidated Chapter 7's live URLs.

Chapter 15 predicted this chapter would make the Hugo menu system necessary. It does not, and Section 16.3 shows why: both languages offer the same six destinations, so only labels and prefixes differ, which `i18n` and `relLangURL` handle with less machinery. Menus win when the *set* of destinations differs between languages or sections. Consider softening Chapter 15's sentence for readers who remember the promise.

Section 16.4's failure was found by reading rather than invented: `.skip-link` holds the only physical-direction property in the stylesheet, so right-to-left genuinely misplaces it, and a keyboard user meets it first. Section 16.6 is the strictest instruction in the book and should stay strict; the back-translation warning matters most, because it is the workaround a reader will reach for and it launders errors into fluent English.

The added workflow step was executed against a fixture, and review corrected three drafting errors including a footer left on `relURL`. Nothing else is validated. See the validation record.
