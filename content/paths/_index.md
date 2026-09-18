---
title: "Learning paths"
description: "Four ways through the book, depending on where you start."
type: docs
---

The book is written to be read in order. One website grows from chapter to
chapter, and each chapter starts from the result of the one before. These four
paths suggest where to put your time, depending on what you already know.

If you skim a chapter, still do its exercises quickly: later chapters edit the
files it creates. Downloadable chapter checkpoints, so you can start midway
without repeating earlier steps, are planned.

## The complete path {#new}

**For you if** you can manage files and install software, but you have not
built a website, used a terminal, or used Git.

Read all nineteen chapters in order and do every exercise. Along the way:

| By the end of | You will have |
| --- | --- |
| [Chapter 3](../book/chapter_03_organise_a_useful_website/) | A small, organised website running on your computer |
| [Chapter 7](../book/chapter_07_publish_your_hugo_site_with_github_pages/) | That website published at a public address |
| [Chapter 8](../book/chapter_08_work_with_an_ai_agent_on_your_hugo_site/) | Your first agent change, checked by you before it was kept |
| [Chapter 14](../book/chapter_14_check_every_contribution_with_ci_cd/) | Automatic checks on every proposed change |
| [Chapter 19](../book/chapter_19_build_your_own_publishing_project/) | A plan for a website of your own |

## Web-literate {#some-experience}

**For you if** you can write HTML and CSS and have met formats such as JSON or
YAML, but you have not used a static site generator, Git, or an AI agent on a
project.

| Chapters | How to read them |
| --- | --- |
| [1](../book/chapter_01_your_first_hugo_website/)–[3](../book/chapter_03_organise_a_useful_website/) | Closely. Hugo's project layout, page bundles, sections, and stable addresses are new. |
| [4](../book/chapter_04_understand_the_html_behind_your_pages/)–[5](../book/chapter_05_practical_css_for_your_hugo_site/) | Skim the explanations, but do the exercises: later chapters edit the same footer and stylesheet. |
| [6](../book/chapter_06_track_and_recover_your_hugo_site_with_git/)–[8](../book/chapter_08_work_with_an_ai_agent_on_your_hugo_site/) | Closely. Git, publishing, and your first agent task. |
| [9](../book/chapter_09_give_your_hugo_content_a_consistent_structure/) and [12](../book/chapter_12_build_a_resource_directory_with_json/) | Skim the YAML and JSON syntax; read the content-model and directory parts closely. |
| [10](../book/chapter_10_use_hugo_templates_to_display_your_content/)–[11](../book/chapter_11_build_reusable_hugo_layouts/) | Closely. Hugo templates are the heart of the generator. |
| 13–19 | In order. |

## Software engineers {#developers}

**For you if** Git, a terminal, data formats, and continuous integration are
everyday tools, and you want Hugo and a reviewed publishing pipeline.

| Chapters | How to read them |
| --- | --- |
| [1](../book/chapter_01_your_first_hugo_website/)–[3](../book/chapter_03_organise_a_useful_website/) | Briskly, for the project setup and Hugo's content organisation: page bundles, `_index.md`, and sections. |
| [4](../book/chapter_04_understand_the_html_behind_your_pages/)–[6](../book/chapter_06_track_and_recover_your_hugo_site_with_git/) | Skim, but apply their edits so your project matches the later chapters. |
| [7](../book/chapter_07_publish_your_hugo_site_with_github_pages/) | The GitHub Pages workflow and how it passes the published address to Hugo. |
| [9](../book/chapter_09_give_your_hugo_content_a_consistent_structure/)–[12](../book/chapter_12_build_a_resource_directory_with_json/) | Closely: content models, archetypes, templates, context, partials, and data files. |
| [14](../book/chapter_14_check_every_contribution_with_ci_cd/) | Checks on pull requests and requiring them before a merge. |
| [15](../book/chapter_15_help_readers_find_and_use_your_content/)–[16](../book/chapter_16_publish_in_multiple_languages/) | Page metadata, sitemap, feed, search, and multilingual configuration. |
| [18](../book/chapter_18_maintain_migrate_and_recover/) | Pinned versions, redirects, and reverting a published change. |
| [8](../book/chapter_08_work_with_an_ai_agent_on_your_hugo_site/), [13](../book/chapter_13_create_and_maintain_content_with_ai_agents/), [17](../book/chapter_17_add_interactive_features_responsibly/) | As your interest takes you: working with agents, and what a static site cannot do by itself. |

## Maintainers and teams {#teams}

**For you if** you already run a website, with Hugo or another static site
generator, and want AI agents to contribute to it without losing control of
what gets published.

These chapters use the book's example website, but their methods apply to your
own repository. Where a chapter names a file such as `content/articles/`,
substitute the equivalent in your project.

| Chapter | What you take to your own site |
| --- | --- |
| [8](../book/chapter_08_work_with_an_ai_agent_on_your_hugo_site/) | An `AGENTS.md` instruction file, bounded tasks, and reviewing what an agent changed. |
| [13](../book/chapter_13_create_and_maintain_content_with_ai_agents/) | Content drafted only from supplied sources, and every claim checked before publishing. |
| [14](../book/chapter_14_check_every_contribution_with_ci_cd/) | Checks on every proposed change, required before anything is merged. |
| [18](../book/chapter_18_maintain_migrate_and_recover/) | A maintenance routine, backups, credentials, and undoing a change that is already live. |
| [19](../book/chapter_19_build_your_own_publishing_project/) | A written brief with named authors, reviewers, and maintainers. |
| [16](../book/chapter_16_publish_in_multiple_languages/) | If your site has a second language: translations reviewed by a speaker and kept up to date. |

## Teaching this book

[Lecture slides](../slides/) for teaching the book in a classroom are being
added chapter by chapter, starting with the course introduction. The complete
path is the order the chapters were written to be taught in.
