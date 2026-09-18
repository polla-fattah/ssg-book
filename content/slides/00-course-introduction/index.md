---
title: "Course introduction"
description: "What the course is, what you will build, and how to prepare for Chapter 1."
book_number: "0"
weight: 1
---

# Static Site Generators in the Age of AI

Building and Maintaining Content with AI Agents

**Chapter 0: Course introduction**

Polla Fattah

---

## What you will build

One small website that grows from chapter to chapter.

- A working site on your own computer in **Chapter 1**
- Published at a public address by **Chapter 7**
- Improved by an AI agent, with every change **reviewed by you**
- A plan for a website of **your own** in Chapter 19

---

## Why a static website?

- Your content is **plain text** in folders you control
- The build produces **ordinary files** any browser can read
- Hosting can be **free**: GitHub Pages serves public projects at no charge
- Every change is **recorded** in Git and can be undone

---

## What "static" means

A **static site generator** combines your writing, a layout, and settings into finished web pages **before** anyone visits.

"Static" describes how the result is served. It does **not** mean the site never changes: you edit, rebuild, and publish again.

---

## How a static site generator works

```text
content/     the Markdown you write
layouts/     templates that shape each page
hugo.toml    the site's settings
     |
     v
   hugo       one command builds the site
     |
     v
public/      HTML, CSS, and images: the finished site
```

---

## Where AI fits

An AI agent can **draft, rearrange, and check** your work.

It cannot know what happened to you, confirm that a claim is true, or decide what should be published.

> Machines check rules. People judge meaning.

---

## The working method

1. **Supply** the material the agent works from
2. **Bound** the task: one clear job, named files
3. **Review** every changed line, not the agent's summary
4. **Check** with a build and automatic tests
5. **Decide** yourself what goes live

---

## Your tools

| Tool | Its job |
| --- | --- |
| Hugo | Builds the website |
| Markdown | The format you write in |
| VS Code | The editor we use |
| Git | Records every change so you can undo it |
| GitHub | Hosts, checks, and publishes the project |
| Codex CLI | The AI agent in the exercises |

---

## What you need

- A laptop or desktop where you can **install software**
- An internet connection
- A free **GitHub** account, from Chapter 7
- Access to an **AI agent**, from Chapter 8: check your account's usage limits first

No programming, Git, or command-line experience is assumed.

---

## The course in five parts

| Chapters | Part |
| --- | --- |
| 1 to 5 | Build and understand a first site |
| 6 to 7 | Record it and publish it |
| 8 to 12 | Bring in an agent and give content a structure |
| 13 to 17 | Contribute, check, and reach readers |
| 18 to 19 | Keep it running, then make your own |

---

## How every chapter works

1. **See the result first**: what you will have at the end
2. **Make one small change** early
3. **Break something on purpose**, then recover from it
4. **Try it your way**, then save a checkpoint

---

## Four learning paths

| Path | For you if |
| --- | --- |
| The complete path | You are new to building websites |
| Web-literate | You know HTML, CSS, JSON, or YAML |
| Software engineers | Git and CI are daily tools; you need Hugo |
| Maintainers and teams | You already run a website |

Every path builds the same website.

---

## Habits for this course

- Keep a short **learning note**: versions, errors, what you tried
- **Read error messages** before changing anything
- **Save a checkpoint** before each experiment
- Never paste **passwords or tokens** into project files or prompts
- **Review** every change an agent makes before you keep it

---

## Before the next session

1. Install **VS Code** from its official download page
2. Install **Hugo**
    - Windows: `winget install Hugo.Hugo.Extended`
    - macOS: `brew install hugo`
    - Linux: follow the official Linux guide
3. Open a terminal and check: `hugo version`
4. Create a folder named `my-knowledge-site`

---

# Next: Your First Hugo Website

Chapter 1: a local preview, your first edit, and one deliberate mistake you will know how to repair.

**polla.dev/ssg-book**
