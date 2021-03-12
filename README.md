# Blog with Hugo

## Deploy process

1. Add new post: `hugo new posts/test.md`
2. Write & fix meta data: `draft: false`
3. Build with theme: `hugo -t hello-friend-ng`
4. Publish public: `cd public && gitu`

## Tips

### Mathjax font size

Fix scale of `themes/hello-friend-ng/layouts/partials/mathjax_support.html`

### Font family

Change font in `themes/hello-friend-ng/assets/scss/_main.scss`

### Write short code

Add `SOME_CODE.html` to `layouts/shortcodes/`
