---
title: "Build Your Own Publishing Project"
description: "Chapter 19: choose a project, write a brief that says what you will not build, test it, and deliver."
book_number: "19"
weight: 20
---

# Build Your Own Publishing Project

Static Site Generators in the Age of AI

**Chapter 19**

Polla Fattah

---

## Today's goal

You have done every step once, deliberately. Now the decisions are **yours**.

- Choose a project you can **finish**
- Write a brief that says what you are **not** building
- Pick features by what they cost to **keep**
- Test the brief **before** building, then deliver

A site a stranger can use, you can maintain in a year, and whose quality you can **account for**.

---

## By the end of today you can

- **Write** a brief that states its audience, purpose, and exclusions
- **Choose** features by their maintenance cost, and justify what you left out
- **Test** a brief for scope, checkability, and ownership before building
- **Say** what must be true before you call a website delivered

No new software. The exercise is a **planning sequence**, with no single right answer.

---

## Choose a project you can finish

| Project | Its first useful version |
| --- | --- |
| A portfolio | Three pieces of work, honestly described |
| A course website | Syllabus, schedule, how to get help |
| A manual or handbook | The five procedures people ask about most |
| A research group site | People, topics, recent publications |
| A business information site | What you do, for whom, how to contact you |

Choose the **smallest version** that is genuinely useful to somebody.

---

## Three tests before you commit

1. Could you publish something useful **within a week** of part-time work?
2. Do you **already have** most of the content, or can you write it?
3. Will you still care about it in **six months**?

A static site suits content that is mostly **read**. Accounts, private data, live transactions, or hourly changes? This is the **wrong toolset**, and knowing that now is worth a lot.

---

## Write a brief, in BRIEF.md

| Part | The question it answers |
| --- | --- |
| Audience | Who, specifically enough to **exclude** someone |
| Purpose | What they can do after visiting |
| Success | What **observable** thing shows it works |
| Content | What exists, and who writes the rest |
| Out of scope | What the site will **not** do |
| Review and maintenance | Who checks it, who keeps it, how often |

---

## The parts that do the work

Keep `BRIEF.md` beside `MAINTENANCE.md`, outside `content/`: a project document, not a page.

- **Out of scope** is the part people skip, and the one that lets you decline a suggestion in **one sentence**
- "Anyone interested in my work" excludes nobody, so it **guides nothing**
- "Second-year students on this module, and colleagues who may teach it next year" tells you what to explain
- "Students stop emailing me to ask when it is due" beats "clear communication": you will **know** if it happened

---

## What capabilities cost to keep, 1

| Capability | Chapters | Ongoing cost |
| --- | --- | --- |
| Pages and sections | 2, 3 | Re-reading for stale claims |
| Layout and stylesheet | 1, 4, 5 | CSS work when the design changes |
| Git history | 6 | Almost nothing |
| Publishing | 7 | Watching deployments; a pinned version |
| An agent agreement | 8, 13 | Keeping `AGENTS.md` true |

---

## What capabilities cost to keep, 2

| Capability | Chapters | Ongoing cost |
| --- | --- | --- |
| Content model | 9 | Holding new pages to it |
| Templates and partials | 10, 11 | Knowing which file a change belongs in |
| A JSON directory | 12 | Every record accurate |
| Checks on proposals | 14 | Rules drift as the site changes |
| Titles, sitemap, feed | 15 | A real description per page |

---

## What capabilities cost to keep, 3

| Capability | Chapters | Ongoing cost |
| --- | --- | --- |
| Search | 15 | It grows with the site |
| A second language | 16 | Every edit becomes two decisions |
| A contact form | 17 | A public address, and spam |
| A maintenance routine | 18 | Actually running it |

Every capability's cost to **keep** is usually higher than its setup.

---

## Yes, later, or no

Write one word per capability in your brief.

- Most first versions need the **first seven** and few of the rest
- A course site: the content model and checks; probably **not** a JSON directory or search for twelve pages
- A research group with sixty publications: the JSON directory, **badly**
- A bilingual department: Chapter 16 **from the start**

Add a capability when you can **name the reader difficulty** it removes. Unsure? Prefer **later**.

---

## Test the brief: scope

Give it to a stranger, or read it yourself tomorrow, and ask them to name **two things the site will not do**.

Cannot? The out-of-scope section is decoration. Rewrite it with specifics:

- Not a blog; not a discussion forum
- Not a place to submit work
- Not translated; no accounts

**Expect the first draft to fail**: that is the exercise working.

---

## Test the brief: checkability

| How it gets verified | Example |
| --- | --- |
| A rule a machine applies | Every page has a description; links are relative |
| A named person reading it | The syllabus is accurate; the tone suits students |
| **Nothing** | "Looks professional"; "easy to use" |

The third row is a **wish**, not a requirement: turn it into one of the first two, or remove it.

Chapter 14's division, moved **before** the work exists.

---

## Test the brief: ownership

For every **yes**, name who maintains it, and how often.

- "Me, eventually" is a plan to **accumulate obligations**
- Cut it to **later**, or put its review in `MAINTENANCE.md` with a cadence you will keep

A brief that survives the three tests is short, specific, and **slightly disappointing**: what a useful one looks like.

---

## Start from a checkpoint

| Start from | When it fits |
| --- | --- |
| Chapter 7 | Pages, layout, Git, and publishing; the rest later |
| Chapter 11 | You need templates, partials, and a section layout |
| Chapter 14 | Checks on proposals from the **first commit** |
| An empty folder | You want to prove that you can |

Chapter 14 is the common sensible choice: retrofitting checks means fixing old problems first.

---

## Make it yours before writing content

1. Remove the notebook's `content/` pages and `sources/` notes
2. Replace the `title`, `baseURL`, and description in `hugo.toml`
3. Rewrite `AGENTS.md` for **this** project: an inherited one is worse than none
4. Replace `MAINTENANCE.md`, and add `BRIEF.md`
5. Adjust the Chapter 14 rules to **your** sections
6. **Delete** every capability you marked **no**

Then publish one page and confirm the **whole chain**: build, checks, deployment, live address.

---

## Three roles

- **Author**: writes or commissions the content
- **Reviewer**: decides it is accurate and fit to publish; **not** a machine
- **Maintainer**: runs the routine and owns the dependencies

One person can hold all three, as long as the **distinction survives**. Write the names in `BRIEF.md`.

An institution's project? Find out early **who is accountable** for what it says.

---

## Three questions that cause trouble later

- **Who may merge?** Alone: you, after reading the diff. With others: require an approval, and stop approving yourself
- **What needs a second reader?** Facts about people, languages the author does not read, and anything an agent drafted
- **When does review happen?** On the pull request, **before** the merge

Review after publication is **damage control**: Chapter 18 showed the cost.

---

## An agent on a project it has never seen

It cannot write your syllabus or your research summary: those are **facts about you**.

1. Write `AGENTS.md` for this project **first**
2. Gather material into `sources/` before any content work
3. Plan before draft; every claim points at a **source line**
4. Review the changed files, not the summary
5. Do not publish what you **cannot review**, in any language

---

## Good and bad agent tasks

**Good**: structural work with a checkable right answer

- Twelve week pages from a schedule you supply
- Adjusting the Chapter 14 rules to your content model

**Bad**: deciding what the site should **contain**

That is your brief. Delegating it produces a plausible site for **a project nobody has**.

---

## What "delivered" means

| Delivered means | How you know |
| --- | --- |
| The purpose is met | A stranger can do what the purpose names |
| Every requirement is verified | By a rule or a named person |
| Published at a stable address | You visited it, not the preview |
| Checks run on every proposal | You have seen one fail and one pass |
| Someone can maintain it | A routine, an owner, a next date |
| Nothing claims more than it can | No unsourced facts, no lost messages |

---

## The last review is yours

As a **visitor**, not an author:

- Open the live site on a **phone**; use only the navigation
- Try to do the thing your **purpose** names
- **Tab** through a page
- Reread the first three pages you wrote: they aged while you built the rest

Record what you built, what is **later**, and the next review date in `BRIEF.md`. Then put that date in your **calendar**: a date there is a commitment.

---

## A worked brief: who and why

```markdown
# Brief: Introduction to Data Analysis, module website

## Audience
Second-year students taking this module, and colleagues who may teach it
next year. Not prospective students, and not the general public.

## Purpose
A student should be able to find the syllabus, the week's reading, the
assignment deadlines, and how to get help, without emailing anyone.
```

Success: the routine "when is it due" emails **stop arriving**.

---

## A worked brief: what it refuses

```markdown
## Out of scope
Not a place to submit work; submission stays in the university system.
No student accounts, no grades, no discussion forum, no blog.
Not translated. No analytics. No contact form.

## Capabilities
Yes: pages, layout, Git, publishing, content model, templates, checks, titles.
Later: search, if the site passes forty pages.
No: JSON directory, second language, contact form.
```

Each refusal is an obligation the author will **not** carry.

---

## When something goes wrong

| What you see | What to do |
| --- | --- |
| You cannot decide what to build | Choose the one whose **content you already have** |
| The brief keeps growing | Additions go to **later** by default |
| Every requirement feels unverifiable | Ask what you would **observe** if it were true |
| The site is built, but empty | Write three pages before a ninth capability |
| You have lost interest | Archive it honestly, as Chapter 18 did |

---

## What this method was for

- Your content is **plain text** in folders you control
- Its history is **recorded** and recoverable
- Its build is **one command** anyone can run
- Its checks state their rules in **files you can read**
- An agent's work can be **reviewed**, because every change shows in a diff

None of that makes the writing true or the site worth visiting. It keeps those things **yours**.

---

## Completion check

- My project's first useful version is within reach
- `BRIEF.md` states audience, purpose, success, content, exclusions, owners
- A stranger can name two things the site will not do
- Every requirement is verified by a rule or a named person
- Each capability is marked yes, later, or no
- `AGENTS.md` and the checks describe **this** project
- The first page is live, with checks on proposals
- `MAINTENANCE.md` has a next review date, and it is in my calendar

---

# Build the thing you actually need

At the smallest size that helps somebody, and keep it honest.

**Static Site Generators in the Age of AI**

**polla.dev/ssg-book**
