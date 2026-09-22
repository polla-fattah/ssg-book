---
title: "Static Site Generator Landscape: A Reference Guide"
description: "A broad catalog of static site generators organized by language, ecosystem, and publishing focus."
date: 2026-09-15
---

Static site generators span a wide range of languages, runtimes, and publishing models. Some are general-purpose build tools, while others specialize in documentation, scientific publishing, blogs, books, or framework-based applications.

This reference organizes the landscape by ecosystem and highlights the architectural focus of each generator.

## JavaScript and TypeScript

### General Purpose and Content-First

- **[Eleventy (11ty)](https://www.11ty.dev/):** Node.js-based generator supporting Liquid, Nunjucks, Markdown, WebC, and multiple other templating languages, with zero client JavaScript by default.
- **[Astro](https://astro.build/):** Component-islands architecture supporting React, Preact, Svelte, Vue, SolidJS, and plain Markdown or MDX with partial hydration.
- **[Hexo](https://hexo.io/):** Fast Node.js blogging engine with extensive plugin and theme ecosystems.
- **[Lume](https://lume.land/):** Deno-native static site generator supporting Nunjucks, Vento, JSX, Markdown, and TypeScript.
- **[Metalsmith](https://metalsmith.io/):** Functional, plugin-driven file manipulation pipeline for Node.js.
- **[Assemble](https://assemble.io/):** Classic Grunt and Gulp-era generator powered by Handlebars.
- **[Harp](https://harpjs.com/):** Zero-configuration web server and static engine supporting Jade/Pug, Markdown, and EJS.
- **[Phenomic](https://phenomic.io/):** Modular static site compiler for React and Webpack ecosystems.
- **[Wintersmith](https://wintersmith.io/):** Flexible, multi-format Node.js site generator.
- **[DocPad](https://docpad.org/):** Early extensible Node.js document management and site builder.
- **[Punch](https://laktek.github.io/punch/):** Conventions-based site generator using Mustache.
- **[Blacksmith](https://github.com/flatiron/blacksmith):** Logic-less template engine driven by Director and Plates.
- **[Capri](https://github.com/capri-js/capri):** Vite-based static compiler supporting partial hydration across diverse frontend libraries.
- **[Elder.js](https://elderguide.com/tech/elderjs/):** Opinionated, SEO-optimized static site generator designed for Svelte.
- **[iles](https://iles.pages.dev/):** Vite-driven static generator featuring islands of interactivity for Vue, Preact, and Svelte.
- **[Abell](https://abelljs.org/):** Low-level, lightweight static generator using custom `.abell` component syntax.

### React Frameworks and Static Export

- **[Next.js](https://nextjs.org/) (`output: 'export'`):** Full static HTML export from React server and client components.
- **[Gatsby](https://www.gatsbyjs.com/):** React and GraphQL-based static generator with an extensive plugin ecosystem.
- **[React Static](https://github.com/react-static/react-static):** Minimalist, progressive React-first static site framework.
- **[Cuttlebelle](https://cuttlebelle.com/):** React-driven generator that decouples data and editing from code components.

### Vue.js Ecosystem

- **[Nuxt](https://nuxt.com/) (`nuxi generate`):** Prerenders Vue.js applications into crawlable static HTML.
- **[VitePress](https://vitepress.dev/):** High-speed Vue 3 and Vite documentation generator and successor to VuePress.
- **[VuePress](https://vuepress.vuejs.org/):** Classic Vue-powered static site generator using Markdown and Webpack.
- **[Gridsome](https://gridsome.org/):** Vue 2 alternative to Gatsby powered by a local GraphQL data layer.
- **[Saber](https://saber.land/):** Extensible Vue-based static site generator with automatic routing.

## Documentation and Technical Publishing

- **[Docusaurus](https://docusaurus.io/):** Meta-maintained documentation framework built on React and MDX.
- **[Starlight](https://starlight.astro.build/):** Documentation platform built directly on top of Astro.
- **[Slate](https://github.com/slatedocs/slate):** Markdown-based API documentation generator.
- **[Docsify](https://docsify.js.org/):** Runtime Markdown compiler that renders documentation on the fly without a build step.
- **[Docute](https://docute.org/):** Lightweight alternative to Docsify for single-page documentation.
- **[GitBook Legacy CLI](https://github.com/GitbookIO/gitbook):** Original Node.js command-line tool for publishing Markdown books.

## Angular and Svelte

- **[Scully](https://scully.io/):** Static site generator for Angular applications.
- **[SvelteKit](https://svelte.dev/docs/kit/adapter-static) with `adapter-static`:** Pre-renders static HTML pages for Svelte applications.
- **[Sapper](https://sapper.svelte.dev/):** Legacy predecessor to SvelteKit with built-in static page exports.

## Go

- **[Hugo](https://gohugo.io/):** Extremely fast build engine written in Go, featuring built-in asset pipelines and zero runtime dependencies.
- **[Goldsmith](https://github.com/metal3d/goldsmith):** Pipeline-based static generator inspired by Metalsmith and compiled to native Go.
- **[Statically](https://github.com/StaticGen/Statically):** Go-based static engine built around Markdown and Go standard templates.
- **[Ponzu](https://github.com/ponzu-cms/ponzu):** Headless CMS and server written in Go that supports static JSON and HTML generation.
- **[GoPublish](https://github.com/markbates/gopublish):** Minimalist publishing tool for transforming Markdown structures into HTML.

## Rust

- **[Zola](https://www.getzola.org/):** Fast, all-in-one generator using Tera templates, Sass compilation, and CommonMark.
- **[mdBook](https://rust-lang.github.io/mdBook/):** Official command-line tool used by the Rust team for creating programming and technical books.
- **[Cobalt](https://github.com/cobalt-org/cobalt.rs):** Minimalist, opinionated static blog engine.
- **[Seite](https://seite.dev/):** Modern static site generator featuring native Model Context Protocol (MCP) tool integration.
- **[Crowbook](https://github.com/lise-henry/crowbook):** Converts Markdown books into HTML, EPUB, and PDF formats.

## Python

- **[Pelican](https://getpelican.com/):** Veteran Python SSG supporting Markdown and reStructuredText with Jinja2 templating.
- **[MkDocs](https://www.mkdocs.org/):** Markdown-driven generator focused on project documentation, widely paired with the Material theme.
- **[Sphinx](https://www.sphinx-doc.org/):** Standard documentation tool across the scientific Python community, supporting reStructuredText and MyST Markdown.
- **[Lektor](https://www.getlektor.com/):** Flexible, desktop GUI-friendly flat-file content management system and static builder.
- **[Nikola](https://getnikola.com/):** Feature-rich engine supporting Markdown, reStructuredText, and Jupyter Notebooks.
- **[Frozen-Flask](https://frozen-flask.readthedocs.io/):** Freezes dynamic Flask applications into completely static file trees.
- **[Cactus](https://github.com/koenbok/Cactus):** Static site generator designed to deploy directly to Amazon S3 using Django templates.
- **[Hyde](https://github.com/hyde/hyde):** Early Python alternative to Jekyll built on Jinja2.
- **[MyST Markdown / Curvenote](https://mystmd.org/):** Scientific publishing engine converting technical Python code and notebooks into websites.
- **[Bengal](https://bengal-docs.github.io/):** Python generator designed for documentation and product sites.
- **[Blurry](https://github.com/stephenleo/blurry):** Schema-first, SEO-focused Markdown generator producing Schema.org metadata.
- **[Dewar](https://github.com/clehner/dewar):** Flask-like, lightweight static publishing pipeline.
- **[Pagegen](https://github.com/mitchellkrogza/Pagegen):** Simple, syntax-flexible page generator.

## Ruby

- **[Jekyll](https://jekyllrb.com/):** Foundation of modern static publishing, deeply integrated as the default builder for GitHub Pages.
- **[Bridgetown](https://www.bridgetownrb.com/):** Modern Ruby static and progressive framework that modernizes Jekyll with Vite and esbuild.
- **[Middleman](https://middlemanapp.com/):** Sinatra-inspired modular site generator specialized in marketing and campaign sites.
- **[Nanoc](https://nanoc.app/):** Flexible, data-driven transformation pipeline supporting heterogeneous data sources.
- **[Ruhoh](https://github.com/ruhoh/ruhoh.rb):** Universal static blog engine designed as a decoupled version of Jekyll.
- **[Scruffy](https://github.com/damieng/scruffy):** Minimalist static builder focused on text-only and lightweight styling.

## PHP

- **[PHPJigsaw](https://jigsaw.tighten.com/):** Built on Laravel's Blade templating engine, Mix/Vite, and Tailwind CSS.
- **[Sculpin](https://sculpin.io/):** Composer-based static generator powered by Symfony components and Twig templates.
- **[Spress](https://spress.yosymfony.com/):** Extensible static site generator built on Symfony micro-components.
- **[Couscous](https://couscous.io/):** Generates developer documentation websites directly from Markdown files in GitHub repositories.
- **[Capro](https://github.com/locomotivemtl/capro):** Lightweight PHP 8 static generator using Laravel Blade templates.
- **[flatMark](https://github.com/flatmark/flatmark):** Flat-file Markdown website generator requiring no database dependencies.
- **[Phrozn](https://phrozn.info/):** Component-based static site generator written in PHP.

## C#, .NET, and F#

- **[Statiq](https://statiq.dev/):** Highly modular, extensible pipeline-driven document generator for .NET developers.
- **[Wyam](https://wyam.io/):** Predecessor to Statiq using Razor templates and Roslyn-powered configuration.
- **[AspNetStatic](https://github.com/MarvinJWendt/AspNetStatic):** Static generation engine that prerenders pages from existing ASP.NET Core pipelines.
- **[DocFX](https://dotnet.github.io/docfx/):** Microsoft's technical documentation generator for .NET API references and Markdown.
- **[Fornax](https://sergeytihon.github.io/Fornax/):** Static site generator written in F# using type-safe F# DSLs for page layouts.

## C, C++, and Minimalist Tools

- **[Soupault](https://www.kainjow.com/soupault/):** C and OCaml DOM-based generator that manipulates raw HTML elements through HTML parsers rather than text template tags.
- **[Tup](https://gittup.org/tup/):** High-speed build system frequently adapted for low-latency static site pipelines.
- **[Treehouse](https://github.com/saulpw/Treehouse):** Minimalist C-based Markdown processor generating lightweight static trees.
- **[Smu](https://github.com/tiagokokada/smu):** Small Markdown engine designed for fast shell-based static builds.

## Haskell and Functional Languages

- **[Hakyll](https://jaspervdj.be/hakyll/):** Haskell static site compiler powered by Pandoc with an xmonad-like DSL.
- **[Franklin.jl](https://franklinjl.org/):** Julia static engine focused on mathematics and LaTeX-rich scientific writing.
- **[Pollen](https://docs.racket-lang.org/pollen/):** Lisp and Racket-powered digital book publishing environment created by Matthew Butterick.
- **[Frog](https://github.com/greghendershott/frog):** Racket static blog generator using Markdown and Pygments.
- **[Obelisk](https://obelisk.build/):** Elixir static site framework leveraging Elixir concurrency and EEx templates.
- **[Coil](https://github.com/utdemir/coil):** Minimalist Elixir-based static site engine.
- **[LambdaPad](https://github.com/joewing/lamdba-pad):** Erlang-based static website compiler.
- **[Cryogen](https://cryogenweb.org/):** Clojure compiler built with Selmer and Markdown.
- **[Perun](https://github.com/hashobject/perun):** Clojure build pipeline targeting the Boot and Clojure ecosystem.

## JVM Languages

- **[JBake](https://jbake.org/):** Java generator supporting AsciiDoc, Markdown, FreeMarker, and Thymeleaf.
- **[Orchid](https://orchid.run/):** Java and Kotlin documentation and site generator supporting multi-module builds.
- **[Laika](https://typelevel.org/Laika/):** Scala text-to-HTML, EPUB, and PDF compiler.
- **[Gaiden](https://github.com/kobo/gaiden):** Groovy documentation engine for turning Markdown into clean reference sites.
- **[Grain](https://github.com/gaoxingliang/grain):** Groovy static generator using metaprogramming capabilities.

## Swift

- **[SwiftPublish](https://github.com/JohnSundell/SwiftPublish):** Swift-native generator allowing entire websites to be declared in pure Swift code.
- **[Saga](https://github.com/robb/SwiftSaga):** Code-first static generator in Swift with no configuration files or implicit build magic.
- **[Ignite](https://github.com/twostraws/Ignite):** Declarative, pure-Swift static site builder adopting SwiftUI-like syntax.

## Perl

- **[Blosxom](https://blosxom.sourceforge.net/):** Historic flat-file blogging engine originally written as a single Perl script.
- **[Statocles](https://metacpan.org/dist/Statocles):** Comprehensive CMS and static publishing platform for Perl developers.
- **[Dotiac DTL](https://metacpan.org/dist/Dotiac-DTL):** Django Template Language compiler ported to Perl for static page rendering.

## R and Literate Data Science

- **[Quarto](https://quarto.org/):** Multilingual technical publishing system for R, Python, Julia, and Observable JavaScript, powered by Pandoc.
- **[Blogdown](https://pkgs.rstudio.com/blogdown/):** R package integrating Hugo, Markdown, and R Markdown for data-driven websites.
- **[Bookdown](https://bookdown.org/):** Authoring framework built on R Markdown for multi-chapter technical books.

## Shell, Awk, Make, and Minimal Utilities

- **[BashBlog](https://github.com/mtgrosser/bashblog):** Self-contained Bash script that generates a complete RSS-capable blog.
- **[Site44](https://site44.com/):** Web service that compiles Dropbox folders into static hosting.
- **[saait](https://git.codemadness.org/saait/file/README.html):** HTML site generator written in C and Awk for simple, lightweight pages.
- **[m4-bakery](https://github.com/stevenharradine/m4-bakery):** Static generator using GNU m4 macro processing and Make pipelines.
- **[gen_site](https://github.com/andrewrk/gen_site):** Ultra-minimalist Lua generator for developers working directly in HTML and Lua.
- **[Hwaro](https://github.com/bixuanzju/hwaro):** High-speed static generator compiled to native code using Crystal.

## Choosing from the Landscape

The right generator depends less on the total number of features than on the shape of the project:

- Choose **[Hugo](https://gohugo.io/)** or **[Zola](https://www.getzola.org/)** when build speed, low operational overhead, and large content collections are the priority.
- Choose **[Astro](https://astro.build/)**, **[Eleventy](https://www.11ty.dev/)**, or **[Lume](https://lume.land/)** when a JavaScript or TypeScript ecosystem and flexible component authoring are important.
- Choose **[VitePress](https://vitepress.dev/)**, **[Docusaurus](https://docusaurus.io/)**, **[MkDocs](https://www.mkdocs.org/)**, **[Sphinx](https://www.sphinx-doc.org/)**, **[Starlight](https://starlight.astro.build/)**, or **[DocFX](https://dotnet.github.io/docfx/)** for documentation and developer portals.
- Choose **[Quarto](https://quarto.org/)**, **[Bookdown](https://bookdown.org/)**, **[Hakyll](https://jaspervdj.be/hakyll/)**, or **[Laika](https://typelevel.org/Laika/)** for scientific, academic, or multi-format publishing.
- Choose **[Next.js](https://nextjs.org/)**, **[Nuxt](https://nuxt.com/)**, **[Gatsby](https://www.gatsbyjs.com/)**, or **[SvelteKit](https://kit.svelte.dev/)** when a static site is closely connected to a frontend application ecosystem.
- Choose **[Jekyll](https://jekyllrb.com/)**, **[Pelican](https://getpelican.com/)**, or **[Middleman](https://middlemanapp.com/)** when an established language ecosystem or hosting platform is the deciding factor.
- Choose a minimalist tool such as **[saait](https://git.codemadness.org/saait/file/README.html)**, **[Smu](https://github.com/tiagokokada/smu)**, **[BashBlog](https://github.com/mtgrosser/bashblog)**, or **[gen_site](https://github.com/andrewrk/gen_site)** when the goal is maximum control and the smallest possible build system.

The static site generator landscape is therefore not a single race toward one universal tool. It is a collection of specialized publishing systems. The most durable choice is the one whose build model, content format, runtime assumptions, and maintenance cost fit the project being built.
