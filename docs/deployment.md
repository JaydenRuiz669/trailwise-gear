# Existing Cloudflare Worker integration

Do not create or delete a Worker. Preserve `trailwise-gear` and its existing workers.dev URL.

1. Sign in to the existing Cloudflare account.
2. Workers & Pages → `trailwise-gear` → Settings → Builds → Connect.
3. Authorize GitHub for **only** `JaydenRuiz669/trailwise-gear` where selectable.
4. Select repository and production branch `main`; root directory is repository root.
5. Build command: leave empty. This repository commits the generated static `public/` directory and has no deployment build dependency.
6. Deploy command: `npx wrangler deploy`.
7. Verify the dashboard Worker name is exactly `trailwise-gear`, matching `wrangler.jsonc`. Check existing bindings/routes before the first deployment; do not remove unrelated configuration.
8. Trigger a build using the dashboard or a new main commit, then verify deployment logs, homepage, one article, policies, robots.txt, sitemap.xml, and a deliberately missing URL (must return 404).

Locally, run `python3 scripts/build.py` then `python3 scripts/check.py` after content edits. Commit the regenerated public files with the source edit. Cloudflare deploys those exact assets on main pushes. No Cloudflare credential belongs in GitHub files.

The previous live homepage is archived under `archive/` and is not served as a public asset. The existing repository history is preserved. A normal revert of the site commit can restore the baseline; check live deployment status before making rollback claims.

Primary documentation checked October 26, 2026:
- https://developers.cloudflare.com/workers/ci-cd/builds/
- https://developers.cloudflare.com/workers/ci-cd/builds/configuration/
- https://developers.cloudflare.com/workers/static-assets/binding/

## Search Console (after deployment)

Use a URL-prefix property for `https://trailwise-gear.jaydenisraelruiz.workers.dev/`. This workers.dev subdomain is not a purchased domain; do not assume control of the parent domain’s DNS. The owner must sign in to Google and provide the actual verification file or meta tag. Add that exact token to the site, deploy, verify ownership, then submit `/sitemap.xml`. Do not invent a verification code. Use URL Inspection for sample pages; submission does not guarantee indexing. No analytics script is required for Search Console.
