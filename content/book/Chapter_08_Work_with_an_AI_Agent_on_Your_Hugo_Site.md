---
title: "Chapter 8 — Work with an AI Agent on Your Hugo Site"
weight: 8
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*Checked with Hugo 0.150.0 on Linux in a focused fixture. No beginner trial or browser review; the agent exercise is authored, not a recorded session.*

You can now write a page, recognise its HTML and CSS, save a Git checkpoint, and publish an update. Those skills make an AI agent more useful: you can give it a specific job and judge what it actually changes.

Our first job is small. The Resources page already contains useful links. You will ask an agent to add a short section explaining how a reader might use them. The result should be easy to inspect: one new heading and three bullets in one Markdown file.

We will use **Codex CLI** as the primary agent environment. The aim is to learn a repeatable working method, not to install every available AI tool. Alternative editor setups can use the same task and review criteria.

## What you will be able to do

By the end, you should be able to:

- Start the agent in the intended Hugo project and inspect its working permissions.
- Provide a clear task, relevant files, boundaries, and observable success criteria.
- Review the changed files and rendered page independently of the agent's summary.
- Keep an accepted change in Git and recover from an isolated mistake.

Start from the working Chapter 7 project with a clean Git working tree. The chapter's local exercises also work if you have completed its source configuration but have not yet published. You need internet access and an account with access to Codex.

Check your account's current access and usage limits before starting. Signing in with ChatGPT uses the access available through that account or workspace; API-key sign-in uses separately billed API access. Installing a client does not provide unlimited model usage. We will use **Sign in with ChatGPT** and will not configure an API key in this exercise. [OpenAI: authentication](https://learn.chatgpt.com/docs/auth)

## 8.1 Know what you are opening

An agent combines a model with tools that can inspect files, make edits, and run commands. Its usefulness depends on the tools, context, and permissions available in that session.

| Term | Meaning in this chapter |
| --- | --- |
| Model | The system interpreting the request and generating responses or actions |
| Agent client | The application connecting the model to project tools |
| Codex CLI | The terminal client used for our practical exercises |
| Editor | The application where you inspect and edit files, such as VS Code |
| Workspace | The project location the agent is working with |

An ordinary chat without access to your files can suggest a change, but cannot establish that it changed your local project. An agent with file access can act on the project, so its output needs review as well as reading.

VS Code is an editor, not itself a particular model. An agent extension adds the relevant capabilities. Codex has an official IDE integration, including a VS Code extension; follow its own setup instructions if you later choose that interface. You do not need both interfaces for this chapter. [OpenAI: Codex IDE extension](https://learn.chatgpt.com/docs/codex/ide)

The CLI runs on your computer, but that does not mean its model runs offline. Relevant prompts and project context can be sent to the model service. Use the book's practice project and the account arrangements appropriate to your material.

## 8.2 Install, sign in, and check the project

Use the [official Codex CLI installation page](https://learn.chatgpt.com/docs/codex/cli). Choose one installation route. The standalone installers below avoid introducing a separate Node.js setup solely for this chapter.

**On Windows, in PowerShell:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

**On macOS or Linux, in a terminal:**

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

These commands download and execute OpenAI's installer. Use the official page as the source for updated instructions. On a managed computer, follow your organisation's software-installation policy rather than changing system restrictions to force an installation.

Reopen the terminal if the installer requests it. Check:

```text
codex --version
```

Keep the reported version in your notes; interface details can change. If Codex was already installed, check its version and continue without installing a second copy.

### Sign in

Run:

```text
codex login
```

Complete the browser sign-in using your intended ChatGPT account. GitHub authentication from Chapter 7 does not sign you into Codex. Do not paste passwords or account tokens into the Hugo project.

On Windows, complete the client's native sandbox setup when prompted. Some setup steps may require administrator approval. Use the current [Windows sandbox instructions](https://learn.chatgpt.com/docs/windows/windows-sandbox) if your device cannot complete them. The native Windows route is sufficient for this plain Hugo project; WSL is a separate environment and is not an additional requirement for the book.

### Confirm your starting point

In the terminal opened at the Hugo project root, run:

```text
git rev-parse --show-toplevel
git status
hugo version
```

Confirm that Git reports your intended project, the working tree is clean, and Hugo is available in this terminal. Save or resolve your own unfinished edits before involving the agent. A clean starting point makes its changes distinguishable from yours.

If a usage limit or account restriction prevents agent access, you can still study the task and apply the comparison example manually. That practises the Hugo change, but it does not complete the hands-on agent exercise.

## 8.3 Give the project a short instruction file

Create `AGENTS.md` beside `hugo.toml`. If one already exists, read it and retain relevant guidance rather than replacing it blindly. For our starter, use:

```markdown
# Project guidance

This is a small Hugo knowledge website using Markdown and plain CSS.

## Files

- Content lives in content/.
- The shared layout is layouts/all.html.
- The stylesheet is static/css/site.css.
- Site configuration is hugo.toml.
- The publishing workflow is .github/workflows/hugo.yaml.

## Working agreements

- Read the relevant source before proposing or making a change.
- Change only the source files requested for the current task.
- Preserve existing front matter, URLs, and authored facts unless the task asks otherwise.
- Do not invent experiences, qualifications, sources, or claims about the author.
- Use the installed Hugo; do not add dependencies or change the publishing workflow unless requested.
- Do not edit generated public/ or resources/ files by hand.
- When asked to check a change, run hugo --minify --panicOnWarning and report the result accurately.
- If a check cannot run, explain what prevented it and what remains unchecked.
- Leave staging, committing, pushing, and deployment to the reader unless explicitly delegated.
```

This file gives Codex reusable project guidance. It does not create operating-system permissions or guarantee compliance. Codex may also load applicable instructions from other locations; task-specific instructions still need to be explicit. [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Read the file yourself, then save a checkpoint:

```text
git add AGENTS.md
git diff --cached -- AGENTS.md
git commit -m "Document the Hugo project's agent working agreements"
git status
```

The instruction file is ordinary project source and can be tracked. It is outside `content/`, so this starter will not turn it into a website page. Remember that pushing it to the public repository will make its text visible as source.

## 8.4 Ask the agent to inspect before it edits

Start a session from the project root:

```text
codex --sandbox read-only --ask-for-approval on-request
```

Inside Codex, enter:

```text
/status
```

Check the displayed project location and active settings. Slash commands go into the Codex interface; commands such as `git status` go into your ordinary terminal.

The read-only mode is useful for this first inspection. Requests to go beyond the configured boundary may trigger approval; do not approve file changes for this inspection task. The later workspace-write mode permits ordinary project edits and commands without asking about every one. Permissions can vary with installation and managed settings, so inspect the active session. [OpenAI: approvals and sandboxing](https://learn.chatgpt.com/docs/agent-approvals-security)

Paste this request into the agent:

```text
Read AGENTS.md, content/resources/index.md, layouts/all.html, and hugo.toml.
Do not edit files or run commands that modify the project.

Explain briefly:
1. Which file contains the Resources page's writing?
2. Which shared layout renders it?
3. What project-path prefix does the configured public URL use?
4. Which existing internal links could help a reader get started?

Point to the relevant files. If something is missing, say so instead of guessing.
```

Compare the response with the files. It should identify the Resources Markdown file, the shared `all.html` layout, and your configured project path. It should recognise the existing links to the first learning note and notebook project.

If the agent describes a different generator or invents files, correct the working directory or ask it to reread the named sources. Do not build the next task on a mistaken description.

Use `/exit` to return to your terminal. Run `git status` again; inspection should have left no source changes. [OpenAI: CLI commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

> **First checkpoint:** the agent inspected the correct project, and you verified its account of the relevant files.

## 8.5 Give it one bounded editing task

Restart from the same project root with permission to make local edits:

```text
codex --sandbox workspace-write --ask-for-approval on-request
```

A new session should not be assumed to remember the previous conversation. We will provide the full task again. Check `/status`, then paste:

```text
Read AGENTS.md and content/resources/index.md before editing.

Task: Help a first-time visitor use the Resources page.
Edit only content/resources/index.md.

Immediately after the introductory paragraph, add a section headed:
## How to use these resources

Add exactly three short bullets, using no more than 70 words in the new section.
- One bullet should explain when to consult the existing Hugo documentation link.
- One should link to the existing first learning note as a practical example.
- One should link to the existing notebook project page for the site's purpose.

Reuse the destinations already present in this file. Do not add external sources.
Preserve the front matter and all existing text and links below the new section.
Do not change layouts, CSS, configuration, dependencies, or workflow files.
Do not stage, commit, push, or deploy.

Run hugo --minify --panicOnWarning if the installed tools and permissions allow it.
If the check is blocked, report that rather than changing the environment.
Finish by listing changed source files, the check actually run and its result,
and anything I still need to inspect in the browser.
```

Watch the activity. The task authorises an edit to one source file and a local build. Generated output from that build is expected; hand-editing generated files is not. A request to install a framework, change your deployment workflow, or publish the result would not be necessary for this task.

A prompt sets the intended scope. The workspace sandbox is broader than this one-file instruction; it is not a per-file guarantee. Read any approval request in relation to the actual task rather than approving it automatically.

### What makes this request useful?

| Part | What it contributes |
| --- | --- |
| Goal | Help a visitor use existing resources |
| Named source | Gives the agent a concrete place to inspect and edit |
| Placement and size | Defines a small, visible result |
| Existing destinations | Avoids inventing links and extra research |
| Preservation requirements | Keeps earlier work intact |
| Verification and stopping point | Separates editing and checking from publication |

You could make this edit yourself. That is a strength of the first exercise: the task is small enough for you to understand its entire result.

## 8.6 Review the files, not just the summary

When the agent finishes, read its report, then use `/exit`. In your normal terminal, run:

```text
git status
git diff --name-only
git diff -- content/resources/index.md
git diff --cached
```

You should see one modified source file: `content/resources/index.md`. The staged diff should be empty because the agent was asked not to stage anything. Use status to notice unexpected new files too; an ordinary diff does not show untracked files.

Read every changed line. Check that:

- The new heading and three bullets appear in the requested place.
- The existing front matter, sections, and links remain intact.
- The new links reuse the correct destinations, including their relative-path form.
- The text describes the material accurately and does not invent claims about you.

Then run the build yourself:

```text
hugo --minify --panicOnWarning
```

Check its exit result, not merely the presence of output in `public/`; old output can remain after a failed build. Next run `hugo server`, open its reported address, and visit Resources. Read the section and activate its links. Check the first learning note and project page, then return to Resources.

The agent's statement that a build passed is evidence about that command if it actually ran. It does not establish that the prose is accurate, every link works, or the page is easy to use. Ask for the command output when the report is unclear. An agent's second review can help, but it is not an independent guarantee.

### One acceptable result for comparison

Your agent may choose different wording. This example shows the intended scale and destinations; it is not a transcript from a recorded agent run:

```markdown
## How to use these resources

- Consult the [Hugo documentation](https://gohugo.io/documentation/) when you need details about configuration, content, or templates.
- Read [my first learning note](../articles/first-learning-note/) for a practical editing and checking example.
- Visit [my knowledge notebook project](../projects/learning-notebook/) to understand this website's purpose.
```

Preserve the existing introduction above this section and the two original sections below it. There is no need to replace the whole page with the example.

### If the result needs correction

Give a precise follow-up such as:

```text
Keep the new section, but restore the original text under Website publishing.
That existing text was outside the requested edit. Change only
content/resources/index.md, then show the corrected diff and rerun the build.
Do not stage, commit, push, or deploy.
```

If the session has been closed, start it again in the project and name the file and current issue explicitly. Do not assume an earlier conversation is automatically present.

If you want to discard the entire attempt, inspect status first. For this one previously tracked file, with no other valuable edits and no staged change, use:

```text
git restore -- content/resources/index.md
```

If it was staged, use Chapter 6's unstage step first. Inspect unexpected changes separately; restoring this one path does not undo other files or remove newly created files. Avoid a broad cleanup command merely to make status look clean.

## 8.7 Keep the accepted result, then test your review habit

When the Resources edit meets the requirements, stop the preview and record it yourself:

```text
git add content/resources/index.md
git diff --cached
git commit -m "Add guidance for using the notebook resources"
git status
```

If the staged diff includes any unrelated changes, resolve them before committing. The expected checkpoint contains only the accepted Resources edit; `AGENTS.md` was already committed separately.

### A link can be wrong even when the build passes

Begin this short experiment from that clean checkpoint. In the **new section only**, change the first-learning-note destination from:

```text
../articles/first-learning-note/
```

to:

```text
/articles/first-learning-note/
```

Save and build again. Hugo can still build successfully. However, on the project site below `/my-knowledge-site/`, a destination starting with `/articles/` goes to the domain root and omits the project prefix.

Inspect the link's resolved address in your local preview using the configured project path. Compare it with the working article address. Do not push this deliberate mistake.

Restore the isolated experiment:

```text
git diff -- content/resources/index.md
git restore -- content/resources/index.md
hugo --minify --panicOnWarning
git status
```

This returns to the accepted section you just committed. Check its link again. You have demonstrated why the review must test a relevant outcome rather than simply accept “build passed”.

> **Second checkpoint:** you accepted an agent-assisted change after checking it yourself, and caught a link problem that building alone did not detect.

## 8.8 Make one request of your own

Ask the agent to shorten one bullet in the new section while preserving its meaning and destination. Name the file, identify the bullet, and say what counts as an improvement. Reuse the same limits on other files and Git actions.

Review the diff and preview. If the change is useful, commit it yourself. If it is already concise enough or the rewrite loses meaning, keep the earlier version. Successful use of an agent includes deciding not to accept a suggestion.

You can keep the Chapter 8 checkpoint local. When you decide to publish the accepted work, use Chapter 7's `git push`, deployment-status check, and live-page verification yourself. Pushing `main` activates the publishing workflow, so it is a separate decision from accepting a local edit.

## Completion check

- [ ] I installed or opened the primary agent client and confirmed my account access.
- [ ] I checked the project location and the session's working permissions.
- [ ] I created and committed concise project guidance in `AGENTS.md`.
- [ ] I verified the agent's initial description of the relevant Hugo files.
- [ ] I gave it a bounded task with clear success criteria.
- [ ] I inspected all changed and newly created files, not just its summary.
- [ ] I built and previewed the Resources change and tested its links.
- [ ] I committed the accepted result myself and repaired the deliberate link mistake.
- [ ] I can make a small follow-up request and decide whether to accept the result.

Keep the method small: supply relevant context, specify a useful outcome, review the changed files, and verify what matters on the page. Skills, plugins, multiple agents, unattended automation, and comparing many models can wait.

Chapter 9 returns to Hugo's content model so that later agent tasks have a clearer structure to work with.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| `codex` is not recognised. | Follow the official installation instructions, reopen the terminal, and check `codex --version`. |
| Sign-in or account access fails. | Check the intended account and its current access. GitHub sign-in and Codex sign-in are separate. |
| The agent describes files from another project. | Exit, check the terminal location, and restart in the Hugo repository. |
| The agent cannot edit during the inspection session. | That session is deliberately read-only. Use the workspace-write session for the editing exercise. |
| A policy prevents using the supplied flags. | Inspect the managed requirements and current official setup guidance. Do not bypass organisational controls. |
| The agent cannot find Hugo. | Check `hugo version` in the same environment. A Windows installation and a WSL installation do not automatically share every tool. |
| The build cannot write its output. | Read the permission error and active writable roots. You can run the build in your normal project terminal and report the result. |
| The agent changes more than the named source file. | Stop and inspect all changes before staging. Ask for a scoped correction or restore only edits you have identified as unwanted. |
| The result claims research or checks that are not shown. | Ask what source or command supports the claim and perform the relevant verification yourself. |
| New files are missing from the diff. | Read `git status`; untracked files require separate inspection. |
| An interrupted session leaves the project uncertain. | Check status and diffs before restarting. Re-state the task, current state, and remaining work. |

Repository text, quoted prompts, and retrieved pages can contain instructions unrelated to your task. Treat such material as content to assess, not as authority to change credentials, publish, or expand the job. The reusable project guidance and the current task should remain explicit.

---

## Editorial note for the author — remove before publication

Codex CLI is the primary environment for this draft. The tool taxonomy and optional IDE link give orientation without turning the chapter into a catalogue of installations. The exercise is intentionally small enough for a beginner to review completely. More substantial content generation and source-verification work belong in Chapter 13.

Official documentation was consulted on 17 September 2026. Installers, account access, model availability, permissions, and interface labels need rechecking before publication. The book does not require a particular model name or claim unlimited access. The standalone installers shown are the documented OS-specific routes; the local validation environment may use a different installation route, which must be identified below.

The comparison example was applied and checked in a focused local Hugo fixture using the earlier starter layout, navigation, original Resources text, and project-path configuration. Destination pages contained placeholder bodies; this was not a full replay of Chapters 1–7. With Hugo 0.150.0 on Linux, the build passed, generated internal link destinations resolved to existing pages under the project prefix, and the root instruction file produced no page. The deliberate root-relative link mistake still allowed a successful build; restoring the committed file repaired it and returned Git to a clean state. The example also met the three-bullet, 70-word limit.

Codex CLI 0.154.0 was installed in a temporary Linux directory through npm for command-help checks. Its version, login command, sandbox modes, and approval flag were checked. No account sign-in, model request, interactive permission flow, or standalone OS installer was tested. The sample is authored, not a recorded agent response. Before publication, run the prompts with a beginner on the supported operating systems and verify the actual agent behaviour, installation, sign-in, and preview experience.

Maintain the book's established teaching rhythm: a short explanation, one useful project change, inspection and recovery where relevant, and a completion checkpoint. Aim for approximately 3,200–4,000 words for chapters of comparable scope, allowing modest variation for supplied files. Introduce only the concepts needed for the exercise and explicitly defer advanced material.
