---
title: "Add Interactive Features Responsibly"
weight: 17
book_number: 17
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1, 17 September 2026**  
*The browser script was checked in isolation. No Hugo build, browser review, mail-client handoff test, or beginner trial yet.*

Readers who find something useful on your site may want to reply to it. A contact form is the obvious way to invite that, and it is also the point where a static site meets its actual limit.

Your site is a set of files. It has no program running on a server, so there is nothing on your side to receive a submitted message. In this chapter you will build a proper contact form, watch it fail to send, and then make it work in the one way a site like yours can without collecting anyone's data: by handing the message to the visitor's own mail program.

The visible result is a Contact page with a form that validates what the visitor types and opens a pre-filled message in their mail client. The lasting result is a clear map of where work can happen (during your build, in the visitor's browser, or on somebody else's server) and an honest account of what each choice costs.

## What you will be able to do

By the end, you should be able to:

- Say which of three places any given feature's work happens in.
- Write accessible form markup with labels, types, and required fields.
- Explain why a static site cannot receive a form submission, and what the options are.
- Explain why a secret cannot be kept in a static site.

Start from the completed Chapter 16 checkpoint with a clean working tree on `main`. Work on a branch and propose the result through a pull request.

Nothing in this chapter requires an account, a payment, or a third-party service. Section 17.6 explains what services do and what you would be agreeing to, but the built feature deliberately sends no visitor data anywhere.

## 17.1 Decide where the work happens

Every feature on a website runs somewhere, and there are only three somewheres available to you. Being able to name the right one is most of what this chapter teaches.

| Where | When it runs | What you have already built there |
| --- | --- | --- |
| Your build | Once, before publication | Every page Hugo generates; the resource directory from Chapter 12; the search list from Chapter 15 |
| The visitor's browser | Each time someone opens a page | The search filtering from Chapter 15 |
| Someone else's server | When something asks it to | Nothing yet |

Build-time work is the cheapest and safest: it happens on your computer or on a GitHub runner, it cannot fail in front of a visitor, and it produces plain files. Browser work can respond to a person, but it only has what the page already contains. Server work can do things neither of the others can (store a message, send an email, charge a card), and it is the only one that introduces an account, a cost, a privacy obligation, and something that can be unavailable.

A form is interesting precisely because it straddles the boundary. Collecting what someone types is browser work. *Receiving* it is server work, and you do not have a server.

## 17.2 Build the form properly

Create `content/contact/index.md`:

```markdown
---
title: "Contact"
description: "How to send me a message about anything in this notebook."
draft: false
---

If something here was useful, wrong, or unclear, I would like to hear about it.

The form below prepares a message in your own email program. Nothing you type is sent anywhere until you send it yourself.
```

Now create `layouts/contact/page.html`. Search and Resources use the same pattern, because Contact is a regular page at `content/contact/index.md`:

```html
{{ define "main" }}
  <article>
    <h1>{{ .Title }}</h1>
    {{ partial "page-meta.html" . }}
    {{ .Content }}

    <form class="contact-form" id="contact-form" novalidate>
      <p>
        <label for="contact-name">Your name</label>
        <input type="text" id="contact-name" name="name" required autocomplete="name">
      </p>
      <p>
        <label for="contact-subject">Subject</label>
        <input type="text" id="contact-subject" name="subject" required>
      </p>
      <p>
        <label for="contact-message">Message</label>
        <textarea id="contact-message" name="message" rows="6" required></textarea>
      </p>
      <p>
        <button type="submit">Prepare this message</button>
      </p>
      <p id="contact-status" role="status"></p>
    </form>

    <script src="{{ "js/contact.js" | relURL }}" defer></script>
  </article>
{{ end }}
```

Read the markup rather than only pasting it, because three details do real work.

Every control has a `<label>` whose `for` matches the control's `id`. That connection is what lets a screen reader announce the right name, and it is why clicking the label focuses the field. A placeholder is not a label: it disappears as soon as someone types.

`required` marks the fields that must be filled. `type="text"` and `<textarea>` choose the kind of control; `rows="6"` gives the message room. `autocomplete="name"` lets a browser offer a value the visitor has already stored, which is a convenience you provide rather than data you collect.

`novalidate` on the form switches off the browser's own validation messages. We are doing the checking in our script so that the message appears in one predictable place; without it you would get two different kinds of warning. If you prefer the browser's built-in messages, remove `novalidate` and the script will still work.

Add a link to the new page from the footer, so it is reachable from everywhere without adding a seventh navigation item. Chapter 15 noted that the navigation was already close to the point where one row stops being comfortable. Open `layouts/_partials/footer.html` and extend its note:

```html
<p class="footer-note">
  Read <a href="{{ "about/" | relLangURL }}">about this notebook</a>
  or <a href="{{ "contact/" | relLangURL }}">send a message</a>.
</p>
```

Note `relLangURL`, following Chapter 16. Add the styling to `static/css/site.css`:

```css
.contact-form label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 0.5rem;
  font-family: inherit;
  font-size: 1rem;
}

.contact-form button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
}

.contact-error {
  color: #8c2f16;
  font-weight: 600;
}
```

`font-family: inherit` matters more than it looks. Form controls do not inherit the page font by default, so without that line the message box would use the browser's own font while everything around it used yours.

Build and preview `/contact/`. You should see a labelled form. Click each label and confirm the matching field takes focus.

## 17.3 Watch it fail to send

Fill the form in and press **Prepare this message**.

Nothing useful happens. Depending on the browser, the page reloads, the fields empty, and what you typed is gone. Look at the address bar: you may see your text appended to the URL as `?name=...&subject=...`.

That is the whole lesson of this chapter, and it is worth sitting with. A `<form>` with no `action` submits to the current address. Your site answers that request the only way it can: by serving the same page file again. There is no program on your side to read the fields, store them, or email them. Hugo ran once, on your computer, and produced files.

Worse, the failure is not silent. If those values appeared in the address bar, they are now in the browser's history, and they would be in a server's access log. A form that appears to work and quietly leaks its contents into a URL is more dangerous than one that visibly does nothing.

This is why the three places in Section 17.1 matter. Receiving a submission is server work. Your options are exactly three:

| Option | What it needs | What it costs |
| --- | --- | --- |
| Hand off to the visitor's mail program | Nothing | The visitor needs a configured mail client; your address becomes public |
| A third-party form service | An account, and a privacy notice | Their terms, their data handling, possibly money |
| Your own serverless function | A hosting account and code you maintain | Setup, upkeep, and a second thing that can break |

We will build the first, because it is the only one that collects nothing, and then explain the others precisely enough that you could choose one deliberately.

> **First checkpoint:** you have seen a form fail to submit on a static site, and can explain why in terms of where work happens.

## 17.4 Validate in the browser and hand off to a mail client

Create `static/js/contact.js`:

```javascript
(function () {
  var form = document.getElementById("contact-form");
  var status = document.getElementById("contact-status");

  if (!form || !status) {
    return;
  }

  var address = form.dataset.address;

  function valueOf(id) {
    var field = document.getElementById(id);
    return field ? field.value.trim() : "";
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    var name = valueOf("contact-name");
    var subject = valueOf("contact-subject");
    var message = valueOf("contact-message");

    if (name === "" || subject === "" || message === "") {
      status.textContent = "Please fill in your name, a subject, and a message.";
      status.className = "contact-error";
      return;
    }

    if (!address) {
      status.textContent = "This form is not configured with an address yet.";
      status.className = "contact-error";
      return;
    }

    var body = message + "\n\n-- \n" + name;
    var href =
      "mailto:" + address +
      "?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(body);

    status.textContent = "Opening your email program. Nothing has been sent yet.";
    status.className = "";
    window.location.href = href;
  });
})();
```

The script needs to know where to write to, and that address should live in your content rather than in the script. Add it to the form tag in `layouts/contact/page.html`:

```html
<form class="contact-form" id="contact-form" novalidate
      data-address="{{ .Params.contact_address }}">
```

Then add the value to the front matter of `content/contact/index.md`:

```yaml
params:
  contact_address: "you@example.org"
```

Use an address you are willing to publish. Section 17.5 discusses that choice.

Four things in the script are worth understanding rather than trusting.

`event.preventDefault()` stops the submission you saw fail in Section 17.3. Everything after it replaces the browser's default behaviour, which is why nothing reaches the address bar any more.

The empty-field check is our own validation, which is why `novalidate` was on the form. Note that it trims whitespace first, so a field containing only spaces counts as empty.

`encodeURIComponent` is the important one. A `mailto:` link is a URL, and characters such as `&`, `#`, `?`, and a line break have meaning inside URLs. Without encoding, a message containing an ampersand would be cut short at that character. This is the same class of problem as Chapter 4's `&amp;`: text has to be escaped for the context it is placed into.

Notice which parts are encoded and which is not. The subject and message are text a visitor typed, so they are encoded. The address is a value you wrote in your own front matter, and it is passed through unchanged, because encoding it would turn the `@` into `%40` and not every mail program accepts that form.

`window.location.href = href` hands the whole thing to the operating system, which opens the default mail program with the fields filled in. Your site has finished. It never held the message, never transmitted it, and has no copy of it.

Rebuild and try it. Submit with an empty message and check that the error appears in the status paragraph. Then fill everything in and submit: your mail program should open with the subject and body already present, and the message should still be unsent until you send it.

> **Second checkpoint:** the form validates in the browser and hands a composed message to the visitor's mail client without transmitting anything.

## 17.5 Be honest with the visitor about what happens

An interactive feature makes a promise. The visitor cannot see your templates, so whatever they believe about their message comes from what the page says.

Our form deserves a plain statement, and it already has one in `content/contact/index.md`: the message is prepared in their own email program and nothing is sent until they send it. Keep that sentence accurate. If you later switch to a form service, it becomes false, and changing it is part of making that switch rather than a tidying task afterwards.

Two honest drawbacks of this approach belong on your own list rather than the visitor's.

Your address becomes public, in the page source and in the front matter you commit. Automated collectors do read published pages for addresses. Obscuring it with a script is a small obstacle and not protection; if that is unacceptable, use an address you can abandon, or choose a form service instead. Do not pretend an obfuscated address is private.

The handoff needs a configured mail program. A visitor using webmail in a browser without a registered mail handler will press the button and see nothing happen. That is a real failure for a real group of people, which is why the Contact page should also state the address as plain readable text, so anyone can copy it. Add that to the page body:

```markdown
You can also write to me directly at `you@example.org`.
```

A feature that works for most people plus a plain alternative for everyone else is a better design than a clever feature that silently excludes some readers.

Finally, note what this form does not collect. There is no analytics script, no cookie, no stored draft, and no third party involved. That is worth knowing because it means you owe your visitors no consent banner or data notice for this page. The moment you add a service that receives their message, you acquire obligations that vary by jurisdiction, and Chapter 18 returns to that.

## 17.6 What a service or a function would change

Suppose the mail handoff is not good enough: you want messages to arrive without depending on the visitor's setup. Both remaining options mean something runs on a server.

A **third-party form service** gives you an address to point your form's `action` at. The visitor's browser posts the fields to that company, which stores them and usually emails you. In exchange, you accept that their servers hold your visitors' messages, you agree to their terms and pricing, you depend on their availability, and you take on the duty of telling visitors where their data goes. The form markup barely changes; the responsibilities change completely.

A **serverless function** is a small program your hosting provider runs on request. You write it, so nothing is hidden from you, and you can validate and forward a message however you like. You also maintain it, keep its dependencies current, and handle its failures. GitHub Pages does not run functions, so this route means either moving your hosting or adding a second provider alongside it.

| Question to ask | Mail handoff | Form service | Your own function |
| --- | --- | --- | --- |
| Who receives the message first? | The visitor's mail program | The service | Your function |
| What must you tell visitors? | That nothing is sent until they send it | Who holds their data and why | The same, plus what you retain |
| What can break? | Their mail client | The service, or your account with it | Your code and your provider |
| Ongoing cost? | None | Possibly | Usually usage-based |
| Is your address public? | Yes | Not necessarily | Not necessarily |

Read that table as a set of trades rather than a ranking. For a personal notebook that receives occasional messages, the first column is often the right answer. For a form people rely on, it is usually not.

Choose deliberately, and write the choice down somewhere, such as a note in the repository or a line in `AGENTS.md`, so that a future contribution, from you or an agent, does not quietly replace one with another.

## 17.7 Why you cannot keep a secret in a static site

One more limit deserves its own section, because it catches people who have otherwise understood everything above.

Suppose you want to show live data: the weather, a repository's star count, a reading list from an external service. Many such services give you an **API**, a documented address your code can request data from, and many require an **API key** to identify you.

You cannot use a key like that in your published site. Everything the browser needs, the visitor has: the HTML, the CSS, the JavaScript, and any value inside them. Putting a key in `static/js/anything.js` publishes it. So does putting it in a template that renders into a page, or in a data file you commit. The reader of your site can read it too, and so can anyone who finds your repository.

There are two honest ways around it, and both come back to Section 17.1.

Fetch the data **at build time**. Hugo can request a remote address while generating the site, so the key lives in your build environment (a GitHub Actions secret rather than a file in the repository), and only the *result* is published. The data is as fresh as your last build, which for a notebook is usually fine.

Or put the key **on a server you control**, in a function that holds it and passes on only what the page needs. That is the serverless option from Section 17.6, with the same costs.

What you must not do is commit the key and rely on the repository being obscure, or on the key being short. If you ever do commit one by accident, treat it as public immediately: revoke it at the service and issue a new one. Removing it in a later commit does not help, because the old commit still contains it, and Chapter 6's whole point was that Git keeps history. Chapter 18 returns to credentials as a maintenance matter.

## 17.8 Test it, propose it, and save

Test the feature the way Chapter 15 taught, because a form has more failure modes than a page of text.

| Check | What should be true |
| --- | --- |
| Labels | Clicking each label focuses its field |
| Keyboard | Tab reaches every field and the button, with a visible focus outline |
| Empty submission | The status paragraph reports what is missing, in the error colour |
| Whitespace only | A field containing only spaces is treated as empty |
| Awkward characters | A message containing `&`, `?`, and a line break survives into the mail program intact |
| Without JavaScript | Disable it and reload; see below |
| Narrow width and zoom | Fields stay inside the reading column |
| Both languages | The footer's new link goes to `/contact/` in English and `/ckb/contact/` in Kurdish |

The no-JavaScript case needs a decision rather than a check. With the script disabled, the form reverts to the Section 17.3 behaviour: it appears to submit and loses the message, possibly into the address bar. That is worse than no form at all, so the honest fix is the plain address you added in Section 17.5. Confirm it is readable with JavaScript off.

The Kurdish check will show you something: `/ckb/contact/` does not exist, because you have not translated the page. The footer link will lead nowhere from a Kurdish page. Fix it as your independent improvement for this chapter, in one of two ways. Either translate the page, following Chapter 16 and including a `source_checked` date, or make the footer link appear only where the page exists. The first is more work and better for readers; the second is one template condition. Decide which you can actually maintain.

Then update `AGENTS.md`, under Files:

```markdown
- The Contact page template is layouts/contact/page.html.
- The contact script is static/js/contact.js.
```

And one working agreement, which is the decision from Section 17.6 written down:

```markdown
- The contact form prepares a message in the visitor's own mail client and sends nothing to any server. Do not replace it with a form service, an analytics script, or any request to a third party without being asked.
```

Build, review, and propose:

```text
hugo --minify --panicOnWarning
git switch -c contact-form
git status
git add content/contact/index.md layouts/contact/page.html
git add static/js/contact.js static/css/site.css
git add layouts/_partials/footer.html AGENTS.md
git diff --cached
git commit -m "Add a contact form that composes a message in the visitor's mail client"
git push -u origin contact-form
```

Read the diff with particular care for the address you published, since that is the part you cannot take back. The four Chapter 14 rule checks should pass. Merge, verify the live page, and try the form once from the published site rather than only from your preview.

## Completion check

- [ ] I can name the three places a feature's work can happen and place each of my own features.
- [ ] Every form control has a matching label, and clicking a label focuses its field.
- [ ] I saw the form fail to submit and can explain why in one sentence.
- [ ] I understand why the failure could leak field values into the address bar.
- [ ] The form validates empty and whitespace-only fields before doing anything.
- [ ] A message containing `&` and a line break arrives intact, and I know why encoding is needed.
- [ ] The page states plainly that nothing is sent until the visitor sends it.
- [ ] A plain readable address is available for people whose mail client does not open.
- [ ] I can explain what a form service or a serverless function would change.
- [ ] I can explain why an API key cannot be kept in a published static site.
- [ ] I decided what to do about the untranslated Kurdish Contact link.

This is enough interactivity for our next steps. Comments, accounts, payments, live data, analytics, spam filtering, and anything requiring a database are outside this chapter's scope. Each one adds a server, an obligation, or both, and none should be added because it is possible.

Chapter 18 turns to keeping all of this working: reviewing content, updating what you depend on, handling credentials, and recovering when something goes wrong.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| The page reloads and the fields empty. | The script did not load or returned early. Check the script tag's address and the `contact-form` and `contact-status` names. |
| Your typed values appear in the address bar. | The same cause. The default submission happened because `preventDefault` never ran. |
| The mail program does not open. | The visitor may have no registered mail handler. This is the case the plain readable address exists for. |
| The message is cut off at an `&`. | An encoding step is missing. Every part placed into the `mailto:` URL goes through `encodeURIComponent`. |
| Line breaks are lost in the message. | Check that the body is built with `\n` and encoded; some mail clients also normalise spacing themselves. |
| The status message says no address is configured. | Add `contact_address` under `params` in the page's front matter, and confirm the `data-address` attribute renders. |
| The message box uses a different font. | Add `font-family: inherit` to the form control rules; controls do not inherit it by default. |
| The error text is not visible enough. | Check the contrast of `.contact-error` against the page background, as Chapter 5 advised for any new colour. |
| The footer link is missing on one page. | The footer is a shared partial. If it differs between pages, you edited a copy rather than `layouts/_partials/footer.html`. |
| The Kurdish footer link leads nowhere. | `/ckb/contact/` does not exist yet. Section 17.8 asks you to choose between translating the page and hiding the link. |
| A spam message arrives. | Your address is public, which is the stated cost of this approach. Filter at your mail provider; there is no form to protect. |

A form that collects nothing still makes a promise to the person filling it in. Keep the page's description of what happens true, especially if you change how it works.

---

## Editorial note for the author (remove before publication)

Section 17.3's failure is the chapter's spine: a beginner presses a button, loses their text, and possibly sees it in the address bar. That is a real defect of naive static forms and the most memorable way to teach where processing occurs. Keep the leaked-values observation; it makes the limit feel consequential rather than academic.

Requiring no account was a firm constraint, following the blueprint's rule that account requirements and costs be stated before an exercise. A chapter that made readers sign up for a form service would also have made them accept a third party's terms on their visitors' behalf. Section 17.6 explains the alternatives well enough to choose one, which meets the plan's "external services and APIs" requirement without building one.

Section 17.7 earns its own section: a static site cannot hold a secret. It is the concrete reason build-time fetching exists, it connects to Chapter 6's point that history is permanent, and it forestalls the most likely serious mistake a reader could make with an API. Do not soften the revoke-immediately instruction.

The Kurdish gap in Section 17.8 is intentional and left unresolved. A footer link added here creates a dead destination in the language added in Chapter 16: exactly the maintenance cost Section 16.7 described, arriving one chapter later. Offering the reader two honest repairs rather than supplying one makes the trade explicit.

The Section 17.4 script was executed against a stand-in for its page, which corrected how the address is encoded. No Hugo build, browser, or mail-client handoff has been tested. See the validation record.
