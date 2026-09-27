# Cloudflare Pages deployment

The website in `site/` is a standalone static site. No application build step is required.

Deployment is handled directly by the native Cloudflare Pages GitHub integration.

## Cloudflare Pages configuration

Use the following settings for the project:

| Setting | Value |
| --- | --- |
| Project name | `ia-usage-meta-analysis` |
| Production branch | `main` |
| Framework preset | None |
| Build command | `exit 0` |
| Build output directory | `site` |
| Root directory | repository root |

The repository layout is:

```text
site/
└── index.html
```

Cloudflare publishes the contents of `site/` directly.

## Deployment behavior

With the GitHub integration enabled:

- a push to `main` triggers a production deployment;
- other enabled branches can create preview deployments;
- Cloudflare reports deployment status back to GitHub.

No Cloudflare API token, account ID, Wrangler configuration, or GitHub Actions deployment workflow is required for the website.

## Custom domain

A custom domain can be attached in the Cloudflare Pages project under **Custom domains**. This does not require a repository change.

## References

- [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)
- [Cloudflare Pages — Build configuration](https://developers.cloudflare.com/pages/configuration/build-configuration/)
