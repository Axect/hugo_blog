# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based personal blog (Axect's Blog) deployed to GitHub Pages at https://axect.github.io. The site features bilingual content (Korean and English) and uses a customized fork of the hello-friend-ng theme.

## Common Commands

```bash
# Initialize project (clone theme)
./init.sh

# Create new post
hugo new posts/my_post.md

# Serve locally with live reload
hugo serve -t hello-friend-ng

# Build for production
hugo -t hello-friend-ng

# Build and deploy to GitHub Pages (copies to ../axect.github.io/)
./build_local.sh
```

## Architecture

### Directory Structure
- `content/` - Blog content with bilingual support (`file.md` for Korean, `file.en.md` for English)
- `layouts/shortcodes/` - Custom shortcodes (center, emph, img, animated, note)
- `themes/hello-friend-ng/` - Customized theme fork from https://github.com/Axect/hello-friend-ng
- `hugo.toml` - Main configuration (languages, menus, params, analytics)

### Content Conventions
- Posts live in `content/posts/` with naming pattern `NNN_topic.md`
- Frontmatter uses YAML format with: title, date, draft, toc, tags
- Set `draft: false` when ready to publish

### Theme Customization Points
- MathJax font sizing: `themes/hello-friend-ng/layouts/partials/mathjax_support.html`
- Font family: `themes/hello-friend-ng/assets/scss/_main.scss`
- New shortcodes: add HTML files to `layouts/shortcodes/`

## Custom Shortcodes

| Shortcode | Usage |
|-----------|-------|
| `center` | Center-aligned content with markdown |
| `emph` | Yellow highlight emphasis |
| `img` | Enhanced images with caption, sizing, linking |
| `animated` | Animated border quote effect |
| `note` | Quote paper styling with curly quotes |

## Deployment

The site deploys to a sibling `axect.github.io` repository. The `build_local.sh` script handles building and copying files. After running it, commit and push changes in that repository.
