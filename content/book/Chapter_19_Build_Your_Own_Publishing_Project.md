# Chapter 19 — Build Your Own Publishing Project

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*A planning chapter with no new software steps. The worked brief and the feature table are authored; no project has been built from them and no beginner trial has been run.*

Eighteen chapters ago you did not have a website. You now have one that is published, checked before every change, searchable, partly bilingual, able to receive a message, and covered by a maintenance routine you wrote yourself. More importantly, you have done each of those things once, deliberately, and can explain why.

This chapter turns that into something of your own. You will choose a project, write a brief that says what you are not building, pick features by what they cost to keep rather than by what is possible, and test that brief before writing a single page. Then you will build it from a checkpoint, agree who reviews and who maintains it, and decide what "delivered" means.

The notebook was a teaching project and every decision in it was made for you. From here the decisions are yours, which is the point. The result should be a site a stranger can use, that you can still maintain in a year, and whose quality you can account for.

## What you will be able to do

By the end, you should be able to:

- Write a project brief that states its audience, purpose, and exclusions.
- Choose features by their maintenance cost and justify what you left out.
- Test a brief for scope, checkability, and ownership before building.
- Say what has to be true before you call a website delivered.

Start from any completed checkpoint in this book, or from an empty folder if you would rather. You need the tools installed in Chapters 1, 6, 7, and 8, and nothing new.

This chapter has no single correct answer, so it works differently from the others: the guided exercise is a planning sequence, and the comparison at the end is a worked brief rather than a file to match.

## 19.1 Choose a project you can finish

The commonest failure of an independent project is not technical. It is choosing something whose first useful version is too far away to reach, and abandoning it half-built.

Five kinds of project suit this toolset well, because their content is mostly writing and their structure is mostly stable:

| Project | Its first useful version |
| --- | --- |
| A portfolio | Three pieces of work, each with an honest description |
| A course website | The syllabus, a schedule, and how to get help |
| A manual or handbook | The five procedures people ask about most |
| A research group site | Who is in it, what it works on, and recent publications |
| A business information site | What you do, who for, and how to make contact |

Notice what each first version excludes. A portfolio does not need every project you have ever done; a course site does not need every lecture before the term starts. Choose the smallest version that would be genuinely useful to somebody, and treat everything else as later work.

Apply three tests to your candidate before committing:

1. **Could you publish something useful within a week of part-time work?** If not, the first version is too big.
2. **Do you already have most of the content, or can you write it?** A site waiting on material you do not have is a content problem wearing a technical costume.
3. **Will you still care about it in six months?** Chapter 18's routine only works if somebody runs it.

A static site is a good answer for content that is mostly read. It is a poor answer for anything needing accounts, private data, live transactions, or content that changes hourly. If your idea needs those, the honest conclusion is that this toolset is the wrong one, and recognising that now is worth more than discovering it in Chapter 17's position.

## 19.2 Write a brief that says what you are not building

A brief is a page. Its job is to let you, and anyone helping you, tell whether a proposed change belongs.

Write these six things, in this order, about your own project:

| Part | The question it answers |
| --- | --- |
| Audience | Who is this for, specifically enough to exclude someone |
| Purpose | What should they be able to do after visiting |
| Success | What observable thing would show it is working |
| Content | What material exists, and who writes what does not |
| Out of scope | What this site will deliberately not do |
| Review and maintenance | Who checks it, who keeps it, and how often |

The fifth part is the one people skip and the one that does the most work. Without it, every plausible suggestion sounds like an improvement, and a site accumulates features nobody maintains. With it, you can decline something in one sentence without re-arguing the whole project.

Be specific about the audience. "Anyone interested in my work" excludes nobody and therefore guides nothing. "Students taking this module in their second year, and colleagues who may teach it next year" tells you what to explain and what to assume.

Make success observable where you can. "Students stop emailing me to ask when the assignment is due" is a better success statement than "clear communication", because you will know whether it happened.

Keep the brief in the repository, as `BRIEF.md` beside `MAINTENANCE.md`. It is a project document, not a page on the site, so it sits outside `content/` for the reason Chapter 13's source notes did.

## 19.3 Choose features by what they cost to keep

You have built fourteen capabilities. Every one has an ongoing cost, and the cost is usually higher than the setup.

| Capability | Built in | What it costs to keep |
| --- | --- | --- |
| Markdown pages and sections | 2, 3 | Re-reading them for claims that went stale |
| A layout and stylesheet | 1, 4, 5 | CSS work whenever the design changes |
| Git history | 6 | Almost nothing |
| Publishing through GitHub Pages | 7 | Watching deployments; one pinned version |
| An agent working agreement | 8, 13 | Keeping `AGENTS.md` true as files move |
| A content model and archetype | 9 | Holding new pages to it |
| Templates and partials | 10, 11 | Knowing which file a change belongs in |
| A JSON data directory | 12 | Keeping every record accurate |
| Checks on every proposal | 14 | Rules drift as the site changes |
| Titles, descriptions, sitemap, feed | 15 | A real description for every page |
| Site search | 15 | It grows with the site |
| A second language | 16 | Every edit becomes two decisions |
| A contact form | 17 | A public address, and the spam it attracts |
| A maintenance routine | 18 | Actually running it |

Now choose. For each capability, write one of three words in your brief: **yes**, **later**, or **no**.

Most first versions need the first seven rows and very few of the rest. A course website probably wants the content model and the checks, and almost certainly does not want a JSON directory or search for twelve pages. A research group site with sixty publications wants the JSON directory badly. A bilingual department site needs Chapter 16 from the start, because retrofitting a second language is more work than beginning with one.

Two rules make this choice easier to live with.

Add a capability when you can name the reader difficulty it removes. "Search, because visitors cannot find anything in forty articles" is a reason. "Search, because the book showed me how" is not.

And prefer **later** to **yes** when you are unsure. A site that does five things well and says it will do a sixth is in better condition than one that does six things adequately. Chapter 18's archive step exists because retiring a feature is harder than postponing it.

## 19.4 Test the brief, and expect it to fail

Before you build anything, test the brief you have just written. Most first drafts fail at least one of these, so finding a failure here is the exercise working rather than going wrong.

**The scope test.** Give the brief to someone who does not know the project — or leave it a day and read it as a stranger. Ask them to name two things the site will *not* do. If they cannot, your out-of-scope section is decoration. Rewrite it with specifics: not a blog, not a discussion forum, not a place to submit work, not translated, no accounts.

**The checkability test.** Take each requirement in turn and ask which of three things will verify it:

| How it gets verified | Example |
| --- | --- |
| A rule a machine can apply | Every page has a description; internal links are relative |
| A named person reading it | The syllabus is accurate; the tone suits students |
| Nothing | "Looks professional"; "easy to use" |

Anything in the third row is a wish, not a requirement. Either turn it into one of the first two rows or remove it. This is the same division Chapter 14 drew between what a check establishes and what a human must, applied one step earlier, before the work exists.

**The ownership test.** For every capability you marked **yes**, name who maintains it and how often. If the answer to both is "me, eventually", you have written a plan to accumulate obligations. Either cut the capability to **later**, or put its review in `MAINTENANCE.md` with a cadence you would actually keep.

Rewrite the brief in response to what these tests found. A brief that survives them is short, specific, and slightly disappointing, which is what a useful one looks like.

> **First checkpoint:** you have a brief whose exclusions a stranger can name, whose requirements are each verifiable by a rule or a person, and whose commitments have owners.

## 19.5 Start from a checkpoint rather than from nothing

You do not need to rebuild the notebook's foundations. Choose the checkpoint that matches the capabilities you marked **yes**, copy it to a new folder, and remove what belongs to the notebook.

| Start from | When it fits |
| --- | --- |
| Chapter 7 | You want pages, a layout, Git, and publishing, and will add the rest as needed |
| Chapter 11 | You know you need templates, partials, and a section layout |
| Chapter 14 | You want checks on proposals from the first commit |
| An empty folder | You want to prove to yourself that you can |

Starting from Chapter 14 is the most common sensible answer, because retrofitting checks onto a site with existing problems means fixing the problems first, as Section 14.3 showed.

Whichever you choose, do this before writing content:

1. Remove the notebook's `content/` pages and its `sources/` notes. Keep the structure, not the material.
2. Replace `hugo.toml`'s `title`, `baseURL`, and site description with your own.
3. Rewrite `AGENTS.md` so its file map and agreements describe *this* project. An inherited instruction file that describes another site is worse than none.
4. Replace `MAINTENANCE.md` with the routine your brief committed to, and add `BRIEF.md`.
5. Adjust the Chapter 14 rules to your own content model. The description rule names `content/articles/` and `content/projects/`; your sections are different.
6. Delete the capabilities you marked **no**, rather than leaving them switched off. Unused templates and scripts are things a future reader must understand before changing anything.

Then create your own first page, publish it, and confirm the whole chain works — build, checks, deployment, live address — before there is enough content for a problem to hide in.

## 19.6 Agree who reviews and who maintains

If you are working alone, this section is still not optional; it is just quicker.

Three roles matter, and one person can hold all three as long as the distinction survives:

**The author** writes or commissions the content. **The reviewer** decides whether it is accurate and fit to publish, which Chapters 13 and 16 established cannot be delegated to a machine. **The maintainer** runs Chapter 18's routine and owns the dependencies.

Write the names in `BRIEF.md`. Then settle the three questions that cause trouble later:

- **Who may merge?** Working alone, you do, after reading the diff. With collaborators, require an approval in the Chapter 14 ruleset and stop approving your own work.
- **What needs a second reader?** At minimum: anything stating a fact about a person, anything in a language the author does not read, and anything an agent drafted from supplied material.
- **When does review happen?** On the pull request, before the merge. Review after publication is damage control, and Chapter 18 showed what that costs.

If your project belongs to an institution, find out early who is accountable for what it says. A course site may need departmental sign-off; a business site may have legal requirements about contact details or accessibility. That is a constraint for the brief, not a surprise for later.

## 19.7 Give an agent a project it has never seen

Chapters 8 and 13 built a working method with an agent, on a project it could inspect. A new project changes one thing: at the start, there is far less for it to read.

That matters because it determines what you can usefully ask for. An agent cannot write your syllabus, your portfolio descriptions, or your group's research summary, because those are facts about you and it has none of them. What it can do is take material you supply and shape it, exactly as in Chapter 13.

So the order is:

1. Write `AGENTS.md` for this project first, describing its real files and your own agreements.
2. Gather your material into `sources/` before asking for any content work.
3. Ask for a plan before a draft, and require each proposed claim to point at a line of your source.
4. Review the changed files, not the summary.
5. Keep the rule from Chapter 16: do not publish what you cannot review, in any language.

Two tasks suit an agent well on a new project, and both are structural rather than factual. Setting up a repetitive section — twelve week pages from a schedule you supply — is work with a clear right answer you can check at a glance. So is adjusting the Chapter 14 rules to your content model, since you can read the result and run it locally.

One task suits it badly: deciding what the site should contain. That is your brief, and delegating it produces a plausible site for a project nobody has.

## 19.8 Deliver, review, and decide what happens next

A website is never finished, so "delivered" has to mean something narrower and checkable. Use this:

| Delivered means | How you know |
| --- | --- |
| The brief's purpose is met | A stranger can do the thing the purpose names |
| Every requirement is verified | By a rule, or by the named person, with nothing left in the third row |
| It is published at a stable address | You visited it, not just the preview |
| The checks run on every proposal | You have seen one fail and one pass |
| Someone can maintain it | `MAINTENANCE.md` has a routine, an owner, and a next date |
| Nothing claims more than it can | No unsourced facts, no untranslated promises, no form that loses messages |

Then do the last review yourself, as a visitor rather than an author. Open the live site on a phone. Use only the navigation. Try to do the thing your purpose statement names. Tab through a page. Read the three pages you wrote first, which are always the ones that aged while you were building the rest.

Record what you decided in `BRIEF.md`: what you built, what you marked **later**, and the date of the next review. Then put that date somewhere you will actually see it, because a maintenance routine in a repository is a document, and a date in your calendar is a commitment.

### What this method was for

The case this book has been making is narrow and practical. Your content is plain text in folders you control. Its history is recorded and recoverable. Its build is a single command that anyone can run. Its checks state their rules in files you can read. An agent can help with it because the material is inspectable, and its contributions can be reviewed because the changes are visible in a diff.

None of that makes the writing true, the design good, or the site worth visiting. Those remain yours. What it does is keep them yours: nothing here depends on a platform that might change its terms, a format you cannot read, or a process you cannot inspect. When you next choose a tool, that is the question worth asking of it.

Build the thing you actually need, at the smallest size that helps somebody, and keep it honest.

## Completion check

- [ ] I chose a project whose first useful version I can reach.
- [ ] `BRIEF.md` states the audience, purpose, success, content, exclusions, and owners.
- [ ] A stranger reading my brief can name two things the site will not do.
- [ ] Every requirement is verified by a rule or by a named person.
- [ ] I marked each of the book's capabilities yes, later, or no, and can justify one **no**.
- [ ] I started from a checkpoint and removed what belonged to the notebook.
- [ ] `AGENTS.md` and the Chapter 14 rules describe this project, not the notebook.
- [ ] The first page is published at its real address, with checks running on proposals.
- [ ] Author, reviewer, and maintainer are named, and I know what needs a second reader.
- [ ] I reviewed the live site as a visitor, on a phone, using only the navigation.
- [ ] `MAINTENANCE.md` has a next review date, and that date is in my calendar.

You have finished the book. What is outside it is larger than what is in it: themes and design systems, full-text search, taxonomies, image pipelines, staged environments, analytics, databases, and retrieval over your own archive. Each is worth learning when a project makes the need concrete, and each is easier to learn now, because you can tell what a tool is doing to your files.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| You cannot decide what to build. | Choose the one with content you already have. The material, not the idea, is the constraint. |
| The brief keeps growing. | Move additions to **later** by default. An addition should name the reader difficulty it removes. |
| Every requirement feels unverifiable. | You are describing qualities rather than outcomes. Ask what you would observe if it were true. |
| The site is built but nothing is on it. | The content was the project all along. Write three pages before adding a ninth capability. |
| A capability you copied is unused. | Delete it. An unused template is something a future reader must understand first. |
| The inherited checks fail on your content. | They name the notebook's sections. Adjust the rules to your model, as Section 19.5 step 5 says. |
| An agent produced a plausible page about you that is wrong. | It had no source. Supply material to `sources/` and ask for a plan before a draft. |
| You are the only reviewer and you keep approving yourself. | Name what requires a second reader, and find one for that list only. |
| Nobody visits it. | Check that the purpose names something a real person wanted. Publication is not distribution. |
| It worked, then went stale. | Run the Chapter 18 pass. If it has not been run, the cadence was unrealistic rather than the routine wrong. |
| You have lost interest. | Archive it honestly, as Section 18.3 did, rather than leaving a site that claims to be current. |

A project's hardest problems are rarely in its build. They are in deciding what it is for and keeping that decision written down.

## A worked brief for comparison

This is fictional and deliberately reusable. It shows the shape and the level of specificity, not a template to fill in unchanged.

```markdown
# Brief: Introduction to Data Analysis, module website

## Audience
Second-year students taking this module, and colleagues who may teach it
next year. Not prospective students, and not the general public.

## Purpose
A student should be able to find the syllabus, the week's reading, the
assignment deadlines, and how to get help, without emailing anyone.

## Success
Routine "when is it due" and "what should I read" emails stop arriving.
A colleague can teach the module from this site plus the slides.

## Content
Exists: syllabus, twelve-week schedule, assessment brief, reading list.
To write: a short "how to get help" page, and one page per week.
Written by me. Reviewed by the module convenor before term.

## Out of scope
Not a place to submit work; submission stays in the university system.
No student accounts, no grades, no discussion forum, no blog.
Not translated. No analytics. No contact form; my office hours and
university address are enough.

## Capabilities
Yes: Markdown pages and sections, layout and stylesheet, Git, publishing,
content model for week pages, templates and partials, checks on proposals,
titles and descriptions.
Later: search, if the site passes forty pages.
No: JSON directory, second language, contact form.

## Review and maintenance
Author and maintainer: me. Reviewer: the module convenor, for the syllabus
and assessment pages only.
Routine: full pass in the week before term starts; week pages checked each
Friday during term; dependency update once a year in the summer.
Next review: the first Monday of next term.
```

Read what that brief refuses. No forum, no accounts, no translation, no analytics, no contact form, and search only at a stated threshold. Each refusal is a maintenance obligation the author will not carry, and each one is easier to defend written down than argued case by case.

---

## Editorial note for the author — remove before publication

This chapter deliberately teaches no new software. Everything it asks for exists by Chapter 18, and the work is deciding rather than building. That makes it structurally unlike the other eighteen, and two consequences need to be accepted rather than smoothed away: the guided exercise is a planning sequence whose output differs for every reader, and the comparison appendix is a worked brief rather than a file to match.

It is also the only chapter with no forward pointer, because there is no Chapter 20. The closing prose in Section 19.8 replaces it, and the completion check's closing paragraph names what lies outside the book instead of what comes next. Any automated consistency check over the chapters should expect that exception rather than flagging it.

Section 19.4 is the designed failure, and the only one in the book that is not technical. A first brief usually fails the scope or checkability test, and the chapter says so in advance so a reader treats the failure as the exercise working. The three-row verification table is Chapter 14's automated-versus-human distinction moved one step earlier, before the work exists, which is where it saves the most effort. The third row — "nothing" — is the load-bearing part.

The capability table in Section 19.3 is the chapter's most useful artifact and the most likely to rot. It must be re-derived if chapters are renumbered or a capability moves. The yes/later/no instruction matters more than the table: the book's arc has been additive, and this is the one place that teaches subtraction.

A course website is the worked example because it is the likeliest real use for this book's reader, and its exclusions are unusually clear. The brief is fictional. Validation here means a trial rather than a build; see the validation record.
