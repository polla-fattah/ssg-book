---
title: "Publish Your Hugo Site with GitHub Pages"
description: "Chapter 7: send this history to GitHub and let a workflow build and publish the site."
book_number: "7"
weight: 8
---

# Publish Your Hugo Site with GitHub Pages

Static Site Generators in the Age of AI

**Chapter 7**

Polla Fattah

---

## Today's goal

Give your website an address **other people can visit**.

- Put the repository on **GitHub**
- Let **GitHub Actions** build it with Hugo
- Publish the result through **GitHub Pages**
- Follow one small update from your editor to the live page

A supplied workflow, explained: no need to master Actions or YAML first.

---

## By the end of today you can

- **Connect** your local repository to GitHub and push your commits
- **Configure** the public address and use a supplied publishing workflow
- **Find** a deployment's status and verify the published pages
- **Publish** a reviewed update, and know where to look when it fails

Start from Chapter 6: on `main`, everything committed, the preview working.

---

## Before you upload

You need internet access and a GitHub account. We use a **public** repository, which is free for Pages.

- Everything you committed becomes **visible**: source, history, and author details
- A page with `draft: true` is not on the website, but its **Markdown is public**
- Review your Chapter 6 history before pushing it

---

## Create an empty repository

| Setting | Choice |
| --- | --- |
| Repository name | `my-knowledge-site` |
| Visibility | Public |
| README, `.gitignore`, licence | **All off**: the remote must be empty |

Copy its HTTPS address; use your **account name**, not your display name:

```text
https://github.com/YOUR-USERNAME/my-knowledge-site.git
```

---

## Sign in from the terminal

Install **GitHub CLI** from cli.github.com, then:

```text
gh --version
gh auth login --hostname github.com --git-protocol https --web --scopes workflow
gh auth setup-git
gh auth status
```

- Sign in in the browser; the `workflow` scope lets you push the workflow file
- No password or token goes into your project files
- Your commit email is author information, **not** a login

---

## Connect and push

```text
git status
git branch --show-current
git remote -v
```

Clean, on `main`, no remote yet? Then:

```text
git remote add origin https://github.com/YOUR-USERNAME/my-knowledge-site.git
git push -u origin main
```

`origin` names the connection. Only **committed** work travels.

---

## Three addresses

| Address | Purpose |
| --- | --- |
| `github.com/YOUR-USERNAME/my-knowledge-site` | Source and history |
| `YOUR-USERNAME.github.io/my-knowledge-site/` | The published website |
| The one `hugo server` prints | Your local preview |

A **project site** has the repository name in its path.

Your source is on GitHub now, but **nothing is published yet**.

---

## Four services, four jobs

| Service | Its job |
| --- | --- |
| **Git** | Stores versions |
| **GitHub** | Hosts the shared repository |
| **GitHub Actions** | Runs the build instructions |
| **GitHub Pages** | Serves the generated website |

In the repository, open **Settings, Pages** and set **Source** to **GitHub Actions**.

A successful push is **not** proof of a deployment.

---

## Set the public address

In `hugo.toml`, change only `baseURL`, keeping the final slash:

```toml
baseURL = 'https://YOUR-USERNAME.github.io/my-knowledge-site/'
```

1. Run `hugo server`, open the **full** address it prints, and check the article and its image
2. Stop it, and build as the workflow will:

```text
hugo --minify --panicOnWarning
```

---

## Why the path matters

- A site under `/my-knowledge-site/` needs that prefix in its links
- The layout's `relURL` already adds it to navigation and the stylesheet
- The article's relative links were designed for this from the start

`--minify` shrinks the output; `--panicOnWarning` turns warnings into **failures**. The result goes to `public/`, which Git ignores.

---

## Add the workflow

Create `.github/workflows/hugo.yaml` and paste the **complete** workflow from the chapter, indented with spaces. It begins:

```yaml
name: Publish Hugo site

on:
  push:
    branches: [main]
  workflow_dispatch:
```

---

## What the workflow does

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

- **build** job: check out the source, read the Pages settings, install Hugo `0.150.0`, build with GitHub's address as `baseURL`, and upload `public/`
- **deploy** job: runs only if the build succeeds (`needs: build`)

---

## The parts you rely on

| Part | Its job |
| --- | --- |
| `on: push` for `main` | Runs on every push to `main` |
| `workflow_dispatch` | Lets you start it by hand |
| `permissions` | Read the source; deploy to Pages |
| `concurrency` | One Pages deployment at a time |
| `PAGES_BASE_URL` | Passes GitHub's address to Hugo |

---

## Worth knowing

- An **artifact** is the packaged build result, passed from build to deploy
- `${{ ... }}` belongs to **GitHub Actions**, not Hugo
- GitHub supplies the credentials: **never** paste your own into the YAML
- Plain CSS, no theme: so no Node.js, Go modules, or Sass. A new theme may need them

> From now on, **every push to `main` publishes**.

---

## Publish

```text
git status
git add hugo.toml .github/workflows/hugo.yaml
git diff --cached
git commit -m "Configure GitHub Pages publishing"
git push
```

In the staged diff, confirm the real `baseURL`, the exact workflow path, and the `main` trigger. **Nothing unrelated.**

---

## Watch the run

1. Open the **Actions** tab, then **Publish Hugo site**
2. Pick the run for **your** commit
3. Wait for **build**, then **deploy**, to succeed
4. A failure? Open the **first failed step** and read it before changing anything
5. Open the URL the deployment reports; do not guess it

The first publication can take a little while.

---

## Verify the real website

- Home and every navigation destination
- The first article, with its screenshot and checklist
- The project page and its link back to the article
- The footer's About link, from a nested page

Open a nested page in a new tab and reload: no `localhost`, the right path. Then try a **private window**, signed out.

---

## Publish one small improvement

Add to the article's publishing checklist:

```markdown
- Check the published page after deployment.
```

```text
git diff -- content/articles/first-learning-note/index.md
git add content/articles/first-learning-note/index.md
git diff --cached
git commit -m "Add a live-site check to the publishing checklist"
git push
```

---

## The whole loop

1. **Edit** the source
2. **Preview** it locally
3. **Review** the diff
4. **Commit**
5. **Push**
6. **Watch** the deployment
7. **Verify** the live page

Edit **locally**, not in GitHub's browser editor, until we learn to combine the two.

---

## Break the build on purpose

From a clean tree, delete the closing quote from `baseURL` in `hugo.toml`:

```text
hugo --minify --panicOnWarning
```

Hugo **fails** reading the configuration. Read the error and find the line. **Do not stage or push it.**

```text
git diff -- hugo.toml
git restore -- hugo.toml
hugo --minify --panicOnWarning
```

---

## If it had reached GitHub

- The **build** fails, so the **deploy** never runs
- The previous successful website **stays online**
- Fix it locally, build, commit, and push again

> A successful deployment can still contain wrong facts or a broken link. The live check is your job.

---

## Try it yourself

Improve one sentence on the About page, and take it through the whole loop:

1. Preview, review, commit, push
2. Watch the run for **that** commit
3. Find the change at the **public address**

Record the public URL in your notes. Your latest pushed commit **is** the Chapter 7 checkpoint.

---

## When something goes wrong

| What you see | What to check |
| --- | --- |
| Push rejected: `workflow` scope | `gh auth refresh --scopes workflow` |
| Push rejected: other commits | A README made online? Never force-push |
| No workflow appears | The file path, and that it was pushed to `main` |
| Builds locally, fails remotely | Hugo version, uncommitted files, filename **case** |

---

## Completion check

- My branch is connected to the intended GitHub repository
- The repository holds source and history, not `public/`
- I can tell the repository, preview, and public addresses apart
- Pages uses GitHub Actions, and both jobs succeeded
- I checked live pages, nested links, the stylesheet, and the image
- My checklist and About edits reached the live site
- I repaired the configuration error before committing anything else

---

# Next: Work with an AI Agent on Your Hugo Site

Chapter 8: give an agent a small task, and review its changes before they reach your website.

**polla.dev/ssg-book**
