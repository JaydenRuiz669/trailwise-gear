# Trailwise Gear

Static, budget-first outdoor publication for the existing Cloudflare Worker `trailwise-gear`.

## Edit and validate

Requires Python 3, no third-party build dependencies.

```sh
python3 scripts/build.py
python3 scripts/check.py
```

Edit articles in `content/guides.json`; edit layout/policies in `scripts/build.py` and styles in `public/style.css`. Commit generated `public/` files with each source change. Cloudflare Workers Builds deploys the committed assets with `npx wrangler deploy` (no build command). Configuration: `wrangler.jsonc`.

See `docs/deployment.md` for connecting the existing Worker without changing its URL, `docs/content-plan.md` for 32 topics and the production process, and `docs/affiliate-operations.md` for monetization preparation. Original homepage preserved in `archive/`.

Cloudflare Web Analytics is included. No affiliate tracking, forms, or secrets are included. Source and generated assets are public. Do not commit credentials or personal application details.
