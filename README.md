# اذكى الأعمال الفائقة | Business Super Intelligence

AI and productivity tools for small business owners and freelancers in **Saudi Arabia and the Gulf**, published in Arabic and English.

**Goal:** earn enough to pay for the tools that run this project, in steps:

| Milestone | Covers | Monthly target |
|---|---|---|
| 1 | Claude Pro ($20) + ChatGPT Plus ($20); GitHub, Supabase and Cloudflare on free plans | **~$40** |
| 2 | + Supabase Pro ($25) + Vercel Pro ($20), only once a project actually needs them | **~$85** |
| 3 | Upgrade Claude Pro → Max ($200) | **~$270** |

Prices are approximate list prices; check the current pricing pages. Upgrade only after a milestone's income has held for 2 months in a row.

## How the money comes in
1. **Our own digital products** (best margin). Product #1: the bilingual *AI Prompt Kit for Saudi Business Owners* (`products/01-prompt-kit/`).
2. **Software affiliate programs** (often recurring commissions): Canva, Notion, ElevenLabs, Descript, beehiiv, Hostinger, Make.com. Check each program's current terms.
3. **Local affiliate programs:** Amazon.sa Associates and Noon. These are supporting income only, because commissions per sale are small.

## How it's automated

```
products.csv ─push─► [GitHub Action: sync-links] ─► Supabase `links` table + site/picks.json ─► landing page
     │
     └─weekly─► [GitHub Action: weekly-drafts] ─► Claude drafts AR+EN posts ─► queue/DATE.md ─► you review ─► Buffer/Meta scheduler

every click: yoursite / post ─► https://xbnqrryetgbqhkfpubzb.supabase.co/functions/v1/go/<slug>?src=<post> ─► logged ─► 302 to partner
```

| Piece | Where | Status |
|---|---|---|
| Click tracker (`links`, `clicks`, `click_stats`) | Supabase project `bsi-links` (free plan), `supabase/` | Live and tested |
| Product list | `affiliate-bot/products.csv` | Waiting for your affiliate links |
| Link sync | `affiliate-bot/sync_links.py` + `.github/workflows/sync-links.yml` | Needs `SUPABASE_SECRET_KEY` secret |
| Weekly bilingual post drafts | `affiliate-bot/generate_posts.py` + `.github/workflows/weekly-drafts.yml` | Needs `ANTHROPIC_API_KEY` secret |
| Landing page (bio link) | `site/` | Needs hosting on Cloudflare Pages |
| Digital product #1 | `products/01-prompt-kit/` (PDF, cover, Gumroad listing; rebuild with `src/`) | Ready to upload |

## Your setup checklist
1. **GitHub secrets** (repo → Settings → Secrets and variables → Actions):
   - `ANTHROPIC_API_KEY`: from console.anthropic.com. Set a monthly spend limit there, e.g. $5.
   - `SUPABASE_SECRET_KEY`: from Supabase → project `bsi-links` → Project Settings → API keys → secret key.
2. **Gumroad** (or Lemon Squeezy / Payhip): upload `products/01-prompt-kit/prompt-kit.pdf` and `cover.png`, and paste the copy from `listing.md`. First check that the platform can pay out to you in Saudi Arabia (PayPal or bank).
3. **Affiliate programs:** apply, then paste each link into `products.csv` (column `affiliate_url`). Paste the Gumroad product link into the `prompt-kit` row. Each push syncs automatically.
4. **Cloudflare Pages:** dash.cloudflare.com → Workers & Pages → Create → Pages → connect this GitHub repo. Leave the build command empty and set the output directory to `site`. Then put that URL in your Instagram and X bios.
5. **Instagram (Creator account) and X** under the brand name. Schedule the weekly drafts with Buffer or Meta Business Suite.

## Saudi Arabia: check these before you post ads
These are not legal advice. Rules change, so confirm on the official sites.
- **Mawthooq licence (رخصة موثوق):** the General Commission for Audiovisual Media (GCAM) requires a licence for people who publish advertising on social media in KSA. Affiliate posts on your accounts may count as advertising. Check gcam.gov.sa before posting affiliate content publicly. Until you do, focus on **your own product** and the **landing page**.
- **Freelance document (وثيقة العمل الحر)** from freelance.sa: the simple legal basis for earning self-employed income as an individual.
- **Label ads clearly.** The drafts include `#إعلان #ad` and a commission note on every affiliate post.

## Weekly routine (~1 hour)
- Monday: review `queue/` drafts, delete anything untrue, schedule them (15 min).
- Daily: reply to comments and DMs (5–10 min).
- Monthly: ask Claude to "review click_stats and sales, drop the weakest products, suggest the next digital product".

## Next products (ask Claude to build)
- Notion template: "Small shop operating system" (orders, customers, content calendar), sold together with the Notion affiliate link.
- Bundle: Prompt Kit + Ramadan campaign pack, released before Ramadan.
- A free mini-guide (5 prompts) as a lead magnet for a beehiiv newsletter.
