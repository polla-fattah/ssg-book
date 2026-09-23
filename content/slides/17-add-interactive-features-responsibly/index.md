---
title: "Add Interactive Features Responsibly"
description: "Chapter 17: a contact form, where a static site's work happens, and why it cannot keep a secret."
book_number: "17"
weight: 18
---

# Add Interactive Features Responsibly

Static Site Generators in the Age of AI

**Chapter 17**

Polla Fattah

---

## Today's goal

A contact form is where a static site meets its **actual limit**.

- Build a proper, accessible form
- Watch it **fail to send**
- Make it work the one way that **collects nothing**: the visitor's own mail program

> Where does the work happen, and at what cost?

---

## By the end of today you can

- **Say** which of three places a feature's work happens in
- **Write** accessible form markup: labels, types, required fields
- **Explain** why a static site cannot receive a submission, and the options
- **Explain** why a secret cannot be kept in a static site

No account, payment, or third-party service. Start from Chapter 16 (branch `chapter-16`), on a **branch**.

---

## Three places work can happen

| Where | When it runs | Built there so far |
| --- | --- | --- |
| Your build | Once, before publication | Every page; the directory; the search list |
| The visitor's browser | Each time a page opens | The search filtering |
| Someone else's server | When asked | Nothing yet |

Only a server can **receive**: store, send, or charge. Only it brings an account, a cost, a privacy duty, and downtime.

---

## The Contact page

`content/contact/index.md`:

```markdown
---
title: "Contact"
description: "How to send me a message about anything in this notebook."
draft: false
---

If something here was useful, wrong, or unclear, I would like to hear about it.
```

Plus a sentence saying the form prepares a message in **your own** email program.

---

## The form

`layouts/contact/page.html`, a regular page like Search. One field of three:

```html
<form class="contact-form" id="contact-form" novalidate>
  <p>
    <label for="contact-name">Your name</label>
    <input type="text" id="contact-name" name="name" required autocomplete="name">
  </p>
  ...subject, and a textarea for the message...
  <p><button type="submit">Prepare this message</button></p>
  <p id="contact-status" role="status"></p>
</form>
```

---

## Three details that do real work

- A `<label>` whose `for` matches the control's `id`: announced by screen readers; clicking it **focuses** the field
- A **placeholder is not a label**: it vanishes when someone types
- `required` marks what must be filled; `autocomplete="name"` is a convenience, not **data you collect**
- `novalidate` switches off the browser's messages, so ours appear in **one** place

---

## Reach it from the footer

A seventh navigation item would crowd the row, so extend the footer note:

```html
<p class="footer-note">
  Read <a href="{{ "about/" | relLangURL }}">about this notebook</a>
  or <a href="{{ "contact/" | relLangURL }}">send a message</a>.
</p>
```

- `relLangURL`, as Chapter 16 taught
- Add the form styles from the chapter, including `font-family: inherit`: form controls do **not** inherit the page font

---

## Watch it fail to send

Fill in the form and press **Prepare this message**.

- The page reloads, the fields empty, your text is **gone**
- The address bar may show `?name=...&subject=...`

A form with no `action` submits to the **same address**. Your site answers by serving the same file again. Nothing on your side can read, store, or email it.

Values in the URL end up in **history and server logs**: worse than doing nothing.

---

## Three ways to receive a message

| Option | Needs | Costs |
| --- | --- | --- |
| Visitor's mail program | Nothing | A mail client; a public address |
| A form service | An account, a privacy notice | Their terms and data handling |
| Your own function | Hosting and code | Upkeep; a second thing to break |

We build the first: the only one that **collects nothing**.

---

## Validate and hand off

`static/js/contact.js`, at its heart:

```javascript
form.addEventListener("submit", function (event) {
  event.preventDefault();
  var body = message + "\n\n-- \n" + name;
  var href =
    "mailto:" + address +
    "?subject=" + encodeURIComponent(subject) +
    "&body=" + encodeURIComponent(body);
  status.textContent = "Opening your email program. Nothing has been sent yet.";
  window.location.href = href;
});
```

---

## Where the address lives

In your **content**, not the script. On the form tag:

```html
<form class="contact-form" id="contact-form" novalidate
      data-address="{{ .Params.contact_address }}">
```

And in the page's front matter:

```yaml
params:
  contact_address: "you@example.org"
```

Use an address you are **willing to publish**.

---

## Four things to understand

- `event.preventDefault()` stops the failing submission: nothing reaches the address bar
- Our own check **trims** first, so spaces alone count as empty
- `encodeURIComponent`: `&`, `#`, `?`, and line breaks mean something in URLs; unencoded, a message is **cut short**
- The **address** is not encoded: `@` would become `%40`

Your site never holds, sends, or keeps the message.

---

## Try it

- Submit with an empty message: the error appears in the status line
- Fill everything in: your mail program opens with subject and body filled
- The message is **still unsent** until you send it

> The form validates in the browser and hands off without transmitting anything.

---

## Be honest with the visitor

The page's promise, "nothing is sent until you send it", must stay **true**. Change it as part of any switch to a service.

- Your address becomes **public**: obscuring it is not protection
- Some visitors have **no mail handler**: the button does nothing for them

So also show it as plain text:

```markdown
You can also write to me directly at `you@example.org`.
```

No analytics, cookie, or third party: **no consent banner owed** for this page.

---

## A service or a function

| Question | Mail handoff | Form service | Your function |
| --- | --- | --- | --- |
| Who gets it first? | The visitor's mail program | The service | Your function |
| What can break? | Their mail client | The service, or your account | Your code and provider |
| Address public? | Yes | Not necessarily | Not necessarily |

Trades, not a ranking. Pages runs **no** functions. **Write down** your choice.

---

## You cannot keep a secret here

An **API** is an address your code requests data from; an **API key** identifies you to it.

Everything the browser needs, the visitor **has**. A key in `static/js/`, a template, or a committed data file is **published**.

- Fetch **at build time**, with the key as a GitHub Actions secret: only the **result** is published
- Or keep the key on a **server you control**

---

## A committed key is a public key

- Do not rely on the repository being obscure, or the key being short
- Committed one by accident? **Revoke it at the service** and issue a new one, immediately
- Deleting it in a later commit does **not** help: the old commit still has it

Git keeps history: that was Chapter 6's whole point.

---

## Test the form

| Check | What should be true |
| --- | --- |
| Labels and keyboard | Clicking focuses; Tab reaches all, with a visible outline |
| Empty or spaces only | The status line reports what is missing |
| `&`, `?`, a line break | They arrive **intact** in the mail program |
| Without JavaScript | The form fails again: the **plain address** is the fix |
| Both languages | The footer link goes to `/contact/` or `/ckb/contact/` |

---

## Your decision: the Kurdish link

`/ckb/contact/` does not exist, so the Kurdish footer link leads **nowhere**. Choose one:

- **Translate** the page, following Chapter 16, with a `source_checked` date
- **Show the link** only where the page exists: one template condition

The first is better for readers; the second is less work. Choose what you can **maintain**.

---

## Record the decision, and propose

Add to `AGENTS.md` the template, the script, and this agreement:

```markdown
- The contact form prepares a message in the visitor's own mail client
  and sends nothing to any server. Do not replace it with a form service,
  an analytics script, or any third-party request without being asked.
```

```text
git switch -c contact-form
git add content/contact/index.md layouts/contact/page.html static/js/contact.js
git add static/css/site.css layouts/_partials/footer.html AGENTS.md
git commit -m "Add a contact form that composes a message in the visitor's mail client"
```

---

## Before you merge

- Read the diff, especially the **address you publish**: it cannot be taken back
- The four Chapter 14 checks should pass
- Merge, and try the form from the **live** site, not only the preview

> A form that collects nothing still makes a **promise**.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| Values appear in the URL | The script did not load: its path and ids |
| The mail program does not open | No mail handler: the plain address is for this |
| Cut off at an `&` | A missing `encodeURIComponent` |
| "Not configured with an address" | `contact_address` and `data-address` |
| A different font in the box | `font-family: inherit` |

---

## Completion check

- I can place each feature in the build, the browser, or a server
- Every control has a matching label
- I can explain in one sentence why the form failed to send
- Empty and whitespace-only fields are caught
- `&` and line breaks arrive intact, and I know why encoding matters
- The page says truthfully what happens, with a plain address
- I can explain why an API key cannot live in a static site
- I decided what to do about the Kurdish Contact link

---

# Next: Maintain, Migrate, and Recover

Chapter 18: reviewing content, updating dependencies, handling credentials, and recovering when something goes wrong.

**polla.dev/ssg-book**
