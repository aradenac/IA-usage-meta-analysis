# Cloudflare Pages deployment

The website in `site/` is a standalone static site. No build step is required.

Deployment is handled by GitHub Actions using Cloudflare's official Wrangler action:

- pushes to `main` deploy the production site;
- pushes to other branches deploy Cloudflare Pages previews;
- the workflow only runs when `site/**` or the deployment workflow changes;
- it can also be launched manually with **Run workflow**.

## One-time Cloudflare setup

### 1. Create an API token

In Cloudflare, create a custom API token with:

- **Account > Cloudflare Pages > Edit**
- scope it to the Cloudflare account that will host the site.

Keep the token value: it will be stored in GitHub as a repository secret.

### 2. Get the Cloudflare account ID

Copy the account ID from the Cloudflare dashboard.

### 3. Create the Pages project

Create the Pages project once, with `main` as its production branch:

```bash
export CLOUDFLARE_ACCOUNT_ID="<account-id>"
export CLOUDFLARE_API_TOKEN="<api-token>"

npx wrangler@latest pages project create ia-usage-meta-analysis \
  --production-branch=main
```

The project name must stay aligned with `CLOUDFLARE_PAGES_PROJECT` in
`.github/workflows/deploy-cloudflare-pages.yml`.

## GitHub repository secrets

In **Settings > Secrets and variables > Actions**, create these repository secrets:

| Secret | Value |
| --- | --- |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare account ID |
| `CLOUDFLARE_API_TOKEN` | API token created above |

GitHub provides `GITHUB_TOKEN` automatically; nothing needs to be created for it.

## Deployment behavior

The workflow publishes the existing `site/` directory directly:

```text
site/
└── index.html
```

No Node.js application build, bundler, or generated output directory is involved.

Cloudflare Pages determines the deployment environment from the Git branch:

- `main` → production;
- any other branch → preview deployment.

The workflow writes the resulting deployment URL, and when available the
branch alias URL, into the GitHub Actions job summary.

## Custom domain

A custom domain can be attached later in Cloudflare under the Pages project's
**Custom domains** settings. This does not require any repository change.

## Manual test

After the Cloudflare project and GitHub secrets exist, run:

**GitHub > Actions > Deploy website to Cloudflare Pages > Run workflow**

or push a change to `site/index.html`.
