---
title: "Chapter 7 — Publish Your Hugo Site with GitHub Pages"
weight: 7
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

**Draft 0.1 — 17 September 2026**  
*Local checks only, with Hugo 0.150.0 on Linux. No live GitHub deployment, browser verification, or beginner trial yet.*

Your website now has content, a readable layout, and a local Git history. This chapter gives it an address other people can visit.

You will put the existing repository on GitHub, let GitHub Actions build it with Hugo, and publish the result through GitHub Pages. Then you will make one small update and follow it from your editor to the live page.

This is our first publishing workflow. We will use a supplied configuration and explain its important parts. You do not need to learn all of GitHub Actions, YAML, or website hosting before your site can go online.

## What you will be able to do

By the end, you should be able to:

- Connect your local Git repository to an empty GitHub repository and push your commits.
- Configure the site's public address and use a supplied Hugo publishing workflow.
- Find a deployment's status and verify the published pages, links, and image.
- Publish a reviewed content update and recognise where to investigate a failure.

Start with the completed Chapter 6 project. Its current branch should be `main`, its changes should be committed, and its local preview should work. The deliberate CSS mistake must already be repaired.

You need internet access, a GitHub account, and permission to create a repository in that account. We will also install GitHub CLI for browser-based sign-in from the terminal. The route below uses a **public repository**, GitHub-hosted standard runners, and the supplied `github.io` address. GitHub Pages is available for public repositories on GitHub Free; service limits still apply. No paid domain is needed for this exercise. [GitHub: about Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

A public repository exposes its committed source and history, including commit author details. Review what you recorded in Chapter 6 before uploading it. A Hugo page marked `draft: true` can be absent from the rendered site while its Markdown remains visible in a public repository.

## 7.1 Give the project a home on GitHub

Sign in to GitHub in your browser, or create an account and complete the required account setup. Create a **new repository** with these choices:

| Setting | Choice for this exercise |
| --- | --- |
| Owner | Your personal account |
| Repository name | `my-knowledge-site` |
| Visibility | Public |
| Initialise with a README | Leave off |
| Add a `.gitignore` template | Leave off; we already have one |
| Choose a licence during creation | Leave unset for this exercise |

We need an empty remote repository because your local project already has its own commits. A licence is a separate publishing decision you can make deliberately later; a public repository does not by itself grant a general licence to reuse all its contents.

After creation, GitHub should show setup instructions for the empty repository. Keep that page open. Copy its **HTTPS repository URL**, which should have this shape:

```text
https://github.com/YOUR-USERNAME/my-knowledge-site.git
```

`YOUR-USERNAME` is a placeholder. Use the account name from the repository URL, not your profile's display name. If that repository name is already in use, choose an unused name and substitute it consistently throughout the chapter.

### Sign in from the terminal

Install GitHub CLI using the instructions for your operating system on the [official GitHub CLI site](https://cli.github.com/). Reopen your terminal if necessary, then check:

```text
gh --version
```

`gh` is GitHub CLI. It supplements the `git` commands you learned earlier.

Run:

```text
gh auth login --hostname github.com --git-protocol https --web --scopes workflow
```

Follow the displayed instructions to open the browser, enter the device code if requested, and authorise GitHub CLI for your account. The additional `workflow` scope allows uploading the Actions workflow file we will add below. Complete any account verification there. Then run:

```text
gh auth setup-git
gh auth status
```

These commands connect Git's authentication to your GitHub CLI sign-in and let you check which account is active. Your Chapter 6 commit email is author metadata; it is not a login credential. This route does not require putting a password or token into your project files. [GitHub CLI: login](https://cli.github.com/manual/gh_auth_login), [GitHub CLI: configure Git authentication](https://cli.github.com/manual/gh_auth_setup-git)

### Connect and push the existing repository

In the terminal at your Hugo project root, run:

```text
git status
git branch --show-current
git remote -v
```

The book project should be clean, on `main`, with no remote listed yet. If `origin` already exists, inspect its address before proceeding; do not replace an existing connection just to match the example. The workflow below assumes the `main` branch created in Chapter 6.

Replace the placeholder URL with the one copied from your empty repository:

```text
git remote add origin https://github.com/YOUR-USERNAME/my-knowledge-site.git
git push -u origin main
```

A **remote** is a named connection to another repository. `origin` is our name for this one. The push transfers your committed history; `-u` sets the upstream relationship so later `git push` commands know where to send this branch. Unsaved or uncommitted edits are not included. [Git: push](https://git-scm.com/docs/git-push)

Refresh the repository page. You should see `hugo.toml`, the source folders, and your earlier commits. You should not need to upload `public/` or drag individual files into GitHub's browser editor.

> **First checkpoint:** your source and Git history are now on GitHub. The website itself has not yet been deployed.

## 7.2 Distinguish the source address from the website address

For the project repository we just created, the addresses normally have these forms:

| Address | Purpose |
| --- | --- |
| `https://github.com/YOUR-USERNAME/my-knowledge-site` | Browse source files and project history |
| `https://YOUR-USERNAME.github.io/my-knowledge-site/` | Visit the published website |
| The address printed by `hugo server` | Preview on your computer |

This chapter uses a **project site**, so the repository name appears in the website's path. A repository named exactly `YOUR-USERNAME.github.io` follows a different convention; do not rename our project to that special name for this exercise.

Git stores versions. GitHub hosts the shared repository. GitHub Actions runs the build instructions. GitHub Pages serves the generated website. These services work together, but pushing source files is not itself proof of a successful deployment.

In your repository's browser interface, open **Settings → Pages**. Under **Build and deployment**, set **Source** to **GitHub Actions**. Interface labels may move over time; the important choice is a custom Actions workflow rather than publishing directly from a branch folder. [GitHub: custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

## 7.3 Set the public address in Hugo

Open `hugo.toml`. Replace only its `baseURL` value, using your actual username and repository name:

```toml
baseURL = 'https://YOUR-USERNAME.github.io/my-knowledge-site/'
```

Keep the final slash. Preserve the existing language code and site title.

The repository path matters. A site published below `/my-knowledge-site/` needs navigation and stylesheet addresses that include that prefix where appropriate. Our shared layout already uses Hugo's `relURL` function for those links. The article's relative image and content links were also designed for the existing folder structure.

Preview with:

```text
hugo server
```

Open the **full address reported by Hugo**. With the configured project path, the preview may now be under `/my-knowledge-site/` rather than at the local server's root. Check Home, Articles, the first article, and its image. Stop the preview with Ctrl+C when finished.

Then run an ordinary build:

```text
hugo --minify --panicOnWarning
```

`--minify` reduces generated output where supported. `--panicOnWarning` makes warnings fail this build, so they receive attention before publication. Hugo writes the result to `public/`, which stays excluded from Git by the earlier ignore rule.

The workflow will obtain the actual Pages base address from GitHub and pass it to Hugo at build time. Keeping `hugo.toml` accurate also makes local builds useful. If you later rename the repository or add a domain, revisit the configuration and links together.

## 7.4 Add the supplied publishing workflow

Using your editor, create a folder named `.github` at the project root, a `workflows` folder inside it, and a file named `hugo.yaml` inside that:

```text
.github/workflows/hugo.yaml
```

Paste the following complete file. Use spaces for indentation, and do not include the Markdown fence markers. You do not need to replace anything inside this workflow for the personal project repository described here.

```yaml
name: Publish Hugo site

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-24.04
    env:
      HUGO_VERSION: "0.150.0"
    steps:
      - name: Check out the source
        uses: actions/checkout@v7

      - name: Read the Pages configuration
        id: pages
        uses: actions/configure-pages@v6

      - name: Install Hugo
        shell: bash
        run: |
          curl --fail --location --retry 3 \
            --output "$RUNNER_TEMP/hugo.tar.gz" \
            "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-amd64.tar.gz"
          mkdir -p "$RUNNER_TEMP/hugo-bin"
          tar -xzf "$RUNNER_TEMP/hugo.tar.gz" -C "$RUNNER_TEMP/hugo-bin" hugo
          echo "$RUNNER_TEMP/hugo-bin" >> "$GITHUB_PATH"

      - name: Build the website
        env:
          PAGES_BASE_URL: ${{ steps.pages.outputs.base_url }}
        run: hugo --minify --panicOnWarning --baseURL "${PAGES_BASE_URL}/"

      - name: Upload the generated website
        uses: actions/upload-pages-artifact@v5
        with:
          path: public

  deploy:
    needs: build
    runs-on: ubuntu-24.04
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Publish to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v5
```

The workflow uses GitHub's checkout and Pages actions, following the build-and-deploy arrangement documented by Hugo and GitHub. It retains the Hugo version used for the earlier chapter examples. Action versions are explicit too; they should be reviewed when maintaining the book. [Hugo: hosting on GitHub Pages](https://gohugo.io/host-and-deploy/host-on-github-pages/), [Checkout action](https://github.com/actions/checkout), [Configure Pages action](https://github.com/actions/configure-pages), [Upload Pages artifact action](https://github.com/actions/upload-pages-artifact), [Deploy Pages action](https://github.com/actions/deploy-pages)

### Understand the parts you are relying on

| Part | Its job |
| --- | --- |
| `on: push` for `main` | Starts the workflow when commits are pushed to this branch |
| `workflow_dispatch` | Allows a manual run from GitHub's Actions interface |
| `permissions` | Allows source reading and the authenticated Pages deployment |
| `concurrency` | Groups Pages runs so deployments do not run simultaneously |
| `build` | Gets the source, installs Hugo, and produces the site |
| `PAGES_BASE_URL` | Passes GitHub's Pages address to the build |
| Upload step | Packages `public/` as a deployment artifact |
| `deploy` with `needs: build` | Publishes after the build job succeeds |

An **artifact** here is a packaged build result passed between jobs. It is not another source commit. The `github-pages` **environment** records the deployment target and its URL. GitHub supplies the workflow's authentication; do not paste your own account credentials into this YAML file.

The `${{ ... }}` expressions belong to GitHub Actions. They are not Hugo template expressions, even though both use braces. The shell script in the install step runs on GitHub's Linux runner, including when your own computer runs Windows.

Our starter uses plain CSS and no external theme, so this workflow does not install Node.js, Go modules, or a Sass toolchain. A future theme with extra build requirements would need corresponding changes. Copying a workflow does not automatically satisfy every theme's dependencies.

This is a small automated build-and-deploy pipeline. Chapter 14 will add the fuller CI/CD workflow: checks on proposed changes, clearer quality gates, and controlled deployment. For now, every push to `main` is a publishing action once this workflow is installed.

## 7.5 Publish and inspect the first deployment

Review the configuration and new workflow before recording them:

```text
git status
git add hugo.toml .github/workflows/hugo.yaml
git diff --cached
git commit -m "Configure GitHub Pages publishing"
git push
```

Review the entire staged diff. In particular, confirm the real `baseURL`, the exact workflow file path, and the `main` trigger. There should be no unrelated edits in this commit.

Open the repository's **Actions** tab. Select **Publish Hugo site** and open the run associated with the commit you just pushed. The run should show a build job followed by a deployment job.

Wait for both jobs to finish successfully. If a job fails, open its first failed step and read the message before changing files. A successful push means the source reached GitHub; it does not mean Hugo built or Pages deployed successfully.

Open the website URL shown by the deployment or by **Settings → Pages**. Use that reported URL rather than guessing. The first deployment may take a little time to become available. [GitHub: configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

### Verify the actual website

Visit these on the published site:

- Home and every main navigation destination.
- The first article, including its screenshot and publishing checklist.
- The project detail page and its link back to the article.
- The footer's About link from a nested page.

Check that the stylesheet loaded and that the content is readable at a narrow width. Open a nested page directly in a new tab and reload it. Its address should remain on the published site's domain and project path, with no `localhost` address involved.

Finally, try the public URL in a private browser window while signed out of GitHub. For this public project site, visitors should not need your account or the Hugo server running on your computer.

> **Second checkpoint:** both workflow jobs succeeded, and you verified the rendered site at its public address.

## 7.6 Publish one small improvement

Open the first article's Markdown file. Add this item to the publishing checklist created in Chapter 6:

```markdown
- Check the published page after deployment.
```

Save, preview locally, and check the diff. Then use the familiar cycle with one new final step:

```text
git diff -- content/articles/first-learning-note/index.md
git add content/articles/first-learning-note/index.md
git diff --cached
git commit -m "Add a live-site check to the publishing checklist"
git push
```

Open the new Actions run, confirm that it corresponds to this commit, and wait for deployment to finish. Reload the published article and find the new checklist item. If it is not visible yet, check the deployment status before blaming the browser cache.

You have now completed the whole loop: edit, preview, review, commit, push, watch the deployment, and verify the live page. Repeat this loop for future small updates.

For this exercise, make edits in your local project. Editing independently in GitHub's browser interface would create remote commits that your local branch must first incorporate. We will introduce that collaboration workflow deliberately later.

## 7.7 Recognise a failed build without publishing a mistake

Start from a clean working tree after the successful update. We will create a temporary local configuration error.

In `hugo.toml`, remove the final closing quote from the `baseURL` line. Save and run:

```text
hugo --minify --panicOnWarning
```

Hugo should fail while reading the TOML configuration. Read the error and locate the damaged line. Do not stage or push this experiment.

Review the isolated change and restore it:

```text
git diff -- hugo.toml
git restore -- hugo.toml
hugo --minify --panicOnWarning
git status
```

The second build should succeed and status should be clean. As in Chapter 6, restoring the file is appropriate here because the only unstaged change in it was our deliberate mistake.

If a similar error reached GitHub, the failed build would prevent the dependent deploy job from publishing that run. Fix the source locally, check the build, commit the correction, and push again. A previously successful Pages deployment normally remains available when a later build fails.

A technically successful deployment can still contain inaccurate writing or a broken link. The workflow we have supplied does not verify facts, every destination, or accessibility. The live checks remain part of your publishing responsibility.

## 7.8 Your independent publishing task

Improve one sentence on the About page. Use the same cycle to preview, commit, push, and verify it at the public address. Choose a change you can recognise clearly on the live page.

Record the public URL somewhere useful, such as your project notes. Your latest committed and pushed version is the Chapter 7 checkpoint.

## Completion check

- [ ] My local branch is connected to the intended GitHub repository.
- [ ] The repository contains source and history, while generated `public/` output remains ignored.
- [ ] I can distinguish the repository URL, local preview, and public website URL.
- [ ] Pages uses GitHub Actions as its publishing source.
- [ ] Both build and deployment jobs completed successfully.
- [ ] I checked the live pages, nested links, stylesheet, and article image.
- [ ] My checklist update and independent About-page edit reached the live site.
- [ ] I repaired the temporary local configuration error before committing anything else.
- [ ] I understand that future pushes to `main` trigger publication.

Chapter 8 introduces the primary AI agent environment. With local preview, Git history, and publishing in place, you will be able to give an agent a small task and review its changes before they reach your website.

## Troubleshooting when you need it

| Symptom | First useful check |
| --- | --- |
| GitHub CLI is not found. | Complete its installation and reopen the terminal. |
| Authentication fails. | Use `gh auth status` to check the active account and complete the browser login. A Git author email is not authentication. |
| Pushing the YAML file is rejected for a missing `workflow` scope. | For the GitHub CLI browser-login route used here, run `gh auth refresh --hostname github.com --scopes workflow`, complete its authorisation, then retry the push. See [GitHub CLI: refresh authentication](https://cli.github.com/manual/gh_auth_refresh). |
| Git says `origin` already exists. | Inspect `git remote -v`; determine whether it points to the intended repository before changing it. |
| A push is rejected because the remote has different commits. | Check whether you initialised the GitHub repository with a README or edited it online. Do not force-push over unexplained work; reconcile the histories before continuing. |
| No workflow appears. | Check that `.github/workflows/hugo.yaml` was committed and pushed to `main`, and that Actions is enabled for the repository. |
| GitHub reports invalid workflow syntax. | Check the file extension, spaces, indentation, and copied `${{ ... }}` expressions. Do not include Markdown backticks. |
| Configure Pages or deployment fails. | Confirm Settings → Pages uses GitHub Actions, then read the failed step. Account, repository, or environment restrictions may need attention. |
| The workflow waits for approval. | Check whether the `github-pages` environment has deployment protection rules and who may approve the run. |
| Installing Hugo fails. | Inspect the download step and version string. A network/download failure is different from a content or template error. |
| Hugo builds locally but fails remotely. | Compare Hugo versions and confirm that all required source files are committed. Also check exact filename case: the runner uses Linux. |
| The first public URL returns 404. | Check that deployment finished, use its reported URL, and confirm the project-name path. Allow initial publication time before retrying. |
| The page appears without styling or navigation goes to the wrong place. | Check the project path and generated stylesheet/link addresses. Preserve the layout's `relURL` expressions. |
| A new local edit is absent online. | Confirm it was saved, committed, pushed, and successfully deployed. Identify the commit attached to the run. |
| A draft is visible as source on GitHub. | Hugo's draft setting controls rendering, not access to files in a public repository. |

Custom domains, DNS, alternative hosts, detailed workflow security, and collaboration policies are beyond this first publishing exercise. Keep the working setup small and introduce those topics when the project needs them.

---

## Editorial note for the author — remove before publication

The core route is one personal public project repository, HTTPS authentication through GitHub CLI, the existing `main` branch, and a GitHub Actions deployment to Pages. It does not create a remote repository or publish anything on the author's behalf. Readers perform those account-specific actions themselves.

The workflow intentionally matches the plain-CSS starter and Hugo 0.150.0 used for the earlier chapter validation. Action major versions were checked against their official repositories on 17 September 2026. Major-version tags can move; dependency pinning and update review should receive fuller treatment in Chapter 14. Recheck versions, account limits, interface labels, and the complete hosted workflow before publication.

Local validation used a project reconstructed from the earlier chapters and Hugo 0.150.0 on Linux. The workflow YAML was parsed, its trigger, job dependency, permissions, and artifact path checked, and its install script checked for shell syntax. The official Hugo archive was downloaded and its extraction and executable-path setup verified. A production-style build passed checks for all seven authored pages and 71 local links, resources, and fragment targets beneath `/my-knowledge-site/`. A small image fixture represented the reader's screenshot for path checks.

Initial and subsequent pushes were exercised against a temporary local bare Git repository, not GitHub. The publishing-checklist update appeared in the generated article. The deliberately malformed TOML failed to build; restoring the committed configuration repaired the build and left the working tree clean. All four action-version tags were confirmed against their official remote repositories.

A real authenticated GitHub Actions/Pages deployment, browser verification of the hosted site, and a beginner trial remain publication gates. These local checks cannot verify account authentication, repository permissions, service behaviour, or the full hosted workflow. No public repository or website was created during drafting.
