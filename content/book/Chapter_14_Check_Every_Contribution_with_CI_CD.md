---
title: "Check Every Contribution with CI/CD"
weight: 14
book_number: 14
---

*Static Site Generators in the Age of AI*  
*Building and Maintaining Content with AI Agents*

Chapter 6 deferred branching until there was a concrete reason to use it. This is that reason. Every change you have made since then went straight onto `main`, and every push to `main` publishes.

In this chapter, you will add a second workflow that examines a proposed change before it can reach the live site. It builds the site and checks three rules this book has already established: directory flags must be real Booleans, internal links must stay relative, and articles and projects must carry a description. Then you will propose a change on a branch, break one of those rules on purpose, and watch the checks stop it.

The visible result is a pull request with a red failing check, then the same pull request with a green passing one, then a deployment you approved. The durable result is a division of labour: the machine checks what can be stated as a rule, and you check what cannot.

## What you will be able to do

By the end, you should be able to:

- Work on a branch and propose a change through a pull request.
- Read a workflow's triggers, jobs, steps, and permissions, and say why its permissions are narrower than the publishing workflow's.
- Run the same checks locally before pushing.
- Explain what a passing check does and does not establish before you merge.

Start from the completed Chapter 13 checkpoint with a clean Git working tree, pushed to GitHub, with the Chapter 7 publishing workflow in place and a working public address. (If you are following along in the companion repository `ssg-playground`, make sure you start from branch `chapter-13` or check out the completed chapter on branch `chapter-14`.) You need the GitHub CLI authentication from Chapter 7 and access to your repository's settings.

Everything here runs on GitHub's free runners for a public repository. Automation minutes are billed differently for private repositories and for larger runners; check your account's current terms before moving this arrangement to other work.

## 14.1 Add a workflow that checks proposed changes

The Chapter 7 workflow deploys. This one only reports. Keeping them in separate files makes the difference visible in the repository itself, and it leaves your working publishing workflow untouched.

Create `.github/workflows/checks.yaml`:

```yaml
name: Check proposed changes

on:
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  checks:
    runs-on: ubuntu-24.04
    env:
      HUGO_VERSION: "0.150.0"
    steps:
      - name: Check out the proposed source
        uses: actions/checkout@v7

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
        run: hugo --minify --panicOnWarning

      - name: Check that directory flags are Booleans
        shell: bash
        run: |
          if grep -n '"start_here": *"' assets/data/resource_links.json; then
            echo "start_here must be an unquoted Boolean: true or false."
            exit 1
          fi

      - name: Check that internal links stay relative
        shell: bash
        run: |
          if grep -rn '](/' content/; then
            echo "Internal links must be relative, not root-relative."
            exit 1
          fi

      - name: Check that articles and projects have a description
        shell: bash
        run: |
          status=0
          for page in content/articles/*/index.md content/projects/*/index.md; do
            if ! grep -q '^description:' "$page"; then
              echo "Missing description: $page"
              status=1
            fi
          done
          exit "$status"
```

The install step is the one from Chapter 7, unchanged, so the checks use the same Hugo version as the deployment. [GitHub: Actions documentation](https://docs.github.com/en/actions), [Checkout action](https://github.com/actions/checkout)

Commit this file to `main` and push it:

```text
git add .github/workflows/checks.yaml
git diff --cached
git commit -m "Add checks for proposed changes"
git push
```

That push runs the publishing workflow as usual, because `hugo.yaml` still watches `main`. It will rebuild and republish the same content; adding a checks file does not change any page. The new workflow does nothing yet, because no pull request exists.

## 14.2 Read the parts you are relying on

The vocabulary here is small, and you have seen most of it in Chapter 7.

| Part | Its job in this file |
| --- | --- |
| `on: pull_request` | Starts this workflow when a change is proposed against `main`, not when it is pushed there |
| `permissions: contents: read` | Allows reading the source and nothing else |
| `jobs: checks` | One job; Chapter 7's workflow has two, `build` and `deploy` |
| `runs-on: ubuntu-24.04` | The **runner**: a fresh machine GitHub provides for this job |
| `env: HUGO_VERSION` | One value used by the install step |
| `steps` | Actions and shell commands, run in order on that runner |
| `uses:` | Runs a published action, such as checkout |
| `run:` | Runs shell commands on the runner |

Two differences from the publishing workflow are deliberate, and both are worth being able to explain.

The **trigger** is different. `pull_request` means these checks look at a proposal. Chapter 7's `push` to `main` means that workflow acts on what has already been accepted. A proposal gets examined; an accepted change gets published.

The **permissions** are narrower. Chapter 7's workflow needs `pages: write` and `id-token: write` because it deploys. This one reads the source and reports, so `contents: read` is all it should have. Giving a checking job the ability to publish would remove the distinction the two files exist to create.

A job fails when any step exits with a non-zero status. In our three checks, `exit 1` is how a broken rule reports itself, and a step that finds nothing simply ends successfully. The `if grep ...; then ... exit 1; fi` shape looks inverted at first: `grep` succeeding means it *found* the thing we do not want.

**CI** stands for continuous integration: changes are checked as they are proposed, rather than in one examination before release. **CD** covers continuous delivery or deployment, which for us is the Chapter 7 workflow. Together they describe the arrangement you now have, not a product you install.

## 14.3 Run the same checks locally, and repair what they find

A check you can only run on GitHub is a slow way to find a typing mistake. Run the three rules on your own computer first.

In your project terminal:

```text
hugo --minify --panicOnWarning
grep -n '"start_here": *"' assets/data/resource_links.json
grep -rn '](/' content/
grep -c '^description:' content/articles/*/index.md content/projects/*/index.md
```

The first two `grep` commands should print nothing and report no match. The last one prints a count for each page, and this is where you should find a problem: `content/articles/first-learning-note/index.md` reports `0`.

That article was written in Chapter 2, before this book had given articles a content model. Chapter 13 introduced the model and applied it to the new article only. The check is correct and the content is out of date.

This is the ordinary experience of adopting a check: the first thing it finds is existing work that predates the rule. Bring the older page up to the standard rather than weakening the rule to accommodate it. Open `content/articles/first-learning-note/index.md` and add a description line to its front matter, keeping the existing fields:

```yaml
description: "Editing a page in my notebook, checking the result, and recording what changed."
```

Run the last command again. Every page should now report `1`. Then build, review, and commit the repair on `main`:

```text
hugo --minify --panicOnWarning
git diff -- content/articles/first-learning-note/index.md
git add content/articles/first-learning-note/index.md
git commit -m "Add a description to the first learning note"
git push
```

If a rule turns out to be wrong rather than the content, change the rule deliberately and say why in the commit message. What you should not do is add an exception that quietly exempts one file, because the next reader will not know whether it is a decision or an oversight.

> **First checkpoint:** the three rules pass locally, and `main` satisfies the standard its own checks describe.

## 14.4 Propose a change on a branch

Until now, an edit and its publication were the same act. A branch separates them: you can record work, push it, and show it to a check before anything reaches the live site.

Create a branch and switch to it:

```text
git switch -c add-actions-resource
git status
```

`git switch -c` creates the branch and moves onto it. Status should report the new branch with a clean tree. Nothing has been copied; a branch is a name for a line of commits, not a second folder. [Git: switch](https://git-scm.com/docs/git-switch)

Now make the proposed change. Add a fifth record at the end of the array in `assets/data/resource_links.json`, following the Chapter 12 agreement. Remember the comma after the previous record's closing brace:

```json
{
  "title": "GitHub: Actions documentation",
  "url": "https://docs.github.com/en/actions",
  "description": "The official reference for automating builds, checks, and deployments on GitHub.",
  "topics": ["GitHub Actions", "Automation"],
  "start_here": false
}
```

Preview it, then commit it to the branch and push:

```text
hugo server
```

Check Resources: four records, correct topics, one Start here label. Stop the preview, then:

```text
hugo --minify --panicOnWarning
git add assets/data/resource_links.json
git diff --cached
git commit -m "Add the GitHub Actions documentation to the resource directory"
git push -u origin add-actions-resource
```

The `-u origin add-actions-resource` part sends the branch to GitHub for the first time and remembers the connection, so later pushes on this branch need only `git push`. This push does **not** publish anything: `hugo.yaml` watches `main`, and you are not on `main`.

## 14.5 Open the pull request and read its checks

A **pull request** proposes that one branch be merged into another. It is also where the checks report and where the diff can be read. [GitHub: pull requests](https://docs.github.com/en/pull-requests)

Open your repository on GitHub. It should offer to create a pull request from the branch you just pushed. Choose to compare `add-actions-resource` into `main`, give it a short title such as `Add the GitHub Actions documentation to the resource directory`, and create it.

If you prefer the terminal, the GitHub CLI from Chapter 7 can do the same:

```text
gh pr create --base main --head add-actions-resource --fill
gh pr checks
```

On the pull request page, look at three things in order:

| What to read | What it tells you |
| --- | --- |
| Files changed | The actual diff, which is the same thing you reviewed locally |
| Checks | Whether Check proposed changes passed, is running, or failed |
| The commit list | Which commits this proposal contains |

Open the check run itself and expand its steps. You should see the checkout, the Hugo install, a successful build, and the three rule checks reporting nothing. Reading a passing log now makes a failing one far easier to interpret later.

This proposal should pass. Leave the pull request open; the next section gives it something to catch.

## 14.6 Break a rule on purpose and let the checks stop it

Chapter 12 explained that `"false"` in quotation marks is a string, not a Boolean, and that it makes the Start here label appear on a record that should not have one. Hugo builds it without complaint. We now have a check that does not.

On your branch, edit the new record so its flag is quoted:

```json
"start_here": "false"
```

Commit and push it:

```text
git add assets/data/resource_links.json
git commit -m "Temporarily quote the start_here flag to test the checks"
git push
```

Return to the pull request. The push adds a commit to the same proposal, so the checks run again. This time the job should fail, and the pull request should show a red mark rather than a green one.

Open the failed run and find the step that failed. The Build the website step should have succeeded, because this mistake is valid JSON. The Check that directory flags are Booleans step should have failed, printing the matching line and the message from the workflow.

Read the log from the top, not from the bottom. The first failing step is the one to act on; later steps may not have run at all.

Now repair it. Restore the unquoted Boolean:

```json
"start_here": false
```

Then verify locally before pushing again, which is the habit worth keeping:

```text
grep -n '"start_here": *"' assets/data/resource_links.json
hugo --minify --panicOnWarning
git add assets/data/resource_links.json
git commit -m "Restore start_here as a Boolean"
git push
```

The checks should run once more and pass. The pull request now contains three commits, including the mistake and its correction. That history is honest and useful; it is not something to hide.

> **Second checkpoint:** a rule this book taught was broken, a machine caught it before publication, and you fixed it from the log.

## 14.7 Require the checks, and keep review separate from them

Nothing so far stops you merging a failing pull request. A **ruleset** can require the check to pass first.

In your repository on GitHub, open **Settings**, then the rules or rulesets area, and create a rule targeting the `main` branch. Enable the requirement that status checks must pass, and select `checks` from the list of available checks. Save it.

The check must have run at least once before GitHub can offer it by name, which is why this step comes after Section 14.6 rather than before it. Interface labels in this area change; use GitHub's current documentation if the wording differs from the description above. [GitHub: about rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

Be clear about what you have just built. As the repository's owner, you can usually still merge past your own rule. For a solo author, the ruleset is a reliable reminder rather than a wall, and that is worth having: it makes bypassing a failing check a deliberate act instead of an oversight.

Now separate the two kinds of judgement, which is the point of the whole chapter:

| The checks establish | Only you can establish |
| --- | --- |
| The site builds with warnings treated as failures | The writing is accurate |
| Directory flags are Booleans | The resource is worth listing |
| Internal links are relative | Those links go where a reader expects |
| Articles and projects have a description | The description describes the page honestly |

Every row on the left is something we could state as a rule. Nothing on the right can be, which is why a green check is permission to look properly rather than a verdict. Chapter 13's unsupported sentence would pass all four of these checks.

An approval requirement is the other half of this arrangement, and it needs a second person: GitHub will not let you approve your own pull request. If a collaborator joins the project, add a required approval then. Working alone, your review step is reading Files changed deliberately before you merge, exactly as you read a diff in Chapter 6.

## 14.8 Merge, verify the deployment, and save

Read the pull request's Files changed once more. It should show one added record and nothing else. Confirm the check is green, then merge it on GitHub.

Merging commits the change to `main`, which is a push to `main`, which starts the Chapter 7 publishing workflow. Watch it in the Actions tab, then verify the live site as you did in Chapter 7:

| Check | What should be true |
| --- | --- |
| Actions | Both workflows appear in the history, with distinct names and purposes |
| The publishing run | It built and deployed after the merge |
| The live Resources page | Five records, correct topics, one Start here label |
| The live article | The first learning note still reads correctly after its description was added |
| The rest of the site | Navigation, Projects, and the footer are unchanged |

Bring your local repository back into line. Your branch's work now lives on `main`, so switch back and collect it:

```text
git switch main
git pull
git log --oneline -5
git status
```

The log should show the merged work, and the tree should be clean. The remote branch can be deleted from the pull request page once merged; GitHub usually offers a button for it. Delete your local copy when you no longer need it:

```text
git branch -d add-actions-resource
```

Then make one proposal of your own on a new branch. A small, honest option: give the reading-list project from Chapter 9 a more specific description, or add one topic label to an existing directory record. Push it, open a pull request, read the checks, review your own diff, and merge it when both you and the checks are satisfied.

## Completion check

- [ ] I can explain why the checks workflow uses `pull_request` and narrower permissions than the publishing workflow.
- [ ] I ran all three rule checks locally and interpreted their output.
- [ ] I brought an older page up to a rule rather than weakening the rule.
- [ ] I created a branch, pushed it, and opened a pull request without publishing anything.
- [ ] I read a passing check log before I needed to read a failing one.
- [ ] I broke a rule on purpose, found the failing step in the log, and repaired it.
- [ ] I required the check on `main` and can say what my own bypass ability means.
- [ ] I can name something true about my site that no check here could establish.
- [ ] I merged an approved change, watched it deploy, and verified the live result.

This is enough automation for our next steps. Test frameworks, external link crawling, accessibility and performance scoring, preview deployments for each pull request, scheduled maintenance runs, and multi-environment promotion are outside this chapter's scope. Add a check when you can state the rule it enforces and say what it cannot see.

Chapter 15 turns to the reader's experience of the finished site: search, navigation, and the titles, descriptions, sitemaps, and feeds that help people find your content.

## Troubleshooting when you need it

| Symptom | Useful next step |
| --- | --- |
| The checks workflow does not run. | It triggers on `pull_request` only. Confirm the file is on `main`, and that a pull request against `main` exists. |
| The description check fails on a page you did not touch. | That is expected on first use. Section 14.3 repairs the older article; bring existing content up to the rule. |
| The description check reports a path with an asterisk in it. | No file matched that pattern. Check that the article and project bundles exist at the expected paths. |
| A `grep` check fails and you cannot see why. | The printed line is the match. `grep` succeeding means it found what the rule forbids. |
| The build step fails but the rule checks do not run. | Steps stop at the first failure. Fix the build first, then rerun. |
| The internal-link check fails on an external address. | The pattern matches `](/` only. A complete `https://` address does not contain it; check for a stray leading slash. |
| Pushing the branch published the site. | Confirm you were not on `main`. `hugo.yaml` triggers on pushes to `main`, including a merge. |
| The check cannot be selected in the ruleset. | It must have run at least once. Open a pull request, let the checks run, then add the requirement. |
| GitHub will not let you approve your own pull request. | That is expected. Working alone, read Files changed yourself and require the status check instead. |
| A merge conflict appears in the pull request. | Your branch and `main` changed the same lines. Chapter 18 covers resolving these; for now, update the branch from `main` and re-check the file. |
| The live site does not show the merged change. | Check the publishing run in Actions. A merge starts it, but the deployment still has to succeed. |

A passing check set is evidence about stated rules on one commit. It is not evidence that the writing is true, the sources are real, or the page is suitable to publish.

## Command card: the branch and review cycle

```text
git switch -c my-change          # create a branch and move onto it
git add <paths>                  # stage the intended files
git commit -m "message"          # record the work on the branch
git push -u origin my-change     # send the branch to GitHub the first time
git push                         # later pushes on the same branch
git switch main                  # return to the published line of work
git pull                         # collect the merged result
git branch -d my-change          # delete the local branch once merged
```

Run the local checks from Section 14.3 before each push. Open, read, and merge the pull request on GitHub.
