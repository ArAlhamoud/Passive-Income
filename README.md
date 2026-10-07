# Passive Income Plan

**Goal:** earn enough small, mostly automated income to pay for a Claude subscription. That's about **$20/month for Pro** and **$100–200/month for Max**.

**The honest version:** no income is fully passive. Claude can do most of the *production* work: writing, drafting, coding, research, scheduling scripts. You still have to do the *human* parts:

- sign up for accounts and verify your identity
- own the social accounts
- check posts before they go live
- receive the payouts

Plan on about 2–3 hours a week for the first 2 months, then about 1 hour a week.

---

## 1. Ideas, ranked for this goal

| # | Idea | Startup cost | Time to first $ | How much Claude can automate | Realistic monthly range* |
|---|------|--------------|-----------------|------------------------------|-----------------------|
| 1 | **Digital products** (Notion/Sheets templates, prompt packs, checklists, mini-guides) on Gumroad / Etsy / Payhip | $0–20 | 2–6 weeks | Very high: Claude writes and builds the product | $0–300 |
| 2 | **Affiliate niche "picks" page + social posts** (your idea) | $0–15 (domain) | 1–3 months | High: drafts posts and builds the site | $0–200 |
| 3 | **Small web tools / micro-SaaS** (calculators, converters, generators) with ads or a $3–5 tip/upgrade | $0–20 | 1–3 months | Very high: Claude writes the code; deploy free on Vercel | $0–500, high variance |
| 4 | **Niche newsletter** (e.g. weekly deals in one category) with affiliate links + sponsors | $0 (Beehiiv/Substack free) | 3–6 months | High: drafting | $0–300 |
| 5 | **Print-on-demand** (Redbubble, Merch by Amazon, Etsy + Printify) | $0 | 1–3 months | Medium: designs and listings | $0–100 |

\*These are ranges for a one-person side project in its first 6 months. The bottom of every range is **$0**, and most first attempts land there. That's why the plan below runs **two** channels at once.

### Recommendation
Run **#1 (digital products)** and **#2 (affiliate)** together:
- Digital products pay 90%+ margins and keep paying with no extra work.
- Affiliate content brings traffic that can also point to your own products.
- Each Instagram/X post can promote both.

---

## 2. Affiliate playbook (your idea, made workable)

### Pick programs
| Program | Commission | Notes |
|---|---|---|
| Amazon Associates | ~1–10% by category | Easiest to start. **You need 3 qualifying sales in the first 180 days or the account closes.** Don't show prices or star ratings unless they come from Amazon's API. |
| AliExpress / Temu / Shein affiliate | ~3–20% | Cheap impulse products, high volume on Instagram. |
| Etsy / eBay Partner Network | ~1–4% | Good for unique or gift items. |
| Impact / ShareASale / CJ / Awin | varies (often 5–30%) | Brand programs (tech accessories, software, courses). Higher payouts, but approval takes longer. |
| **Software/SaaS programs** (Notion, Canva, hosting, VPNs, AI tools) | 20–50% recurring | **Usually the best payout per click.** They also fit an "AI productivity" niche. |

### Pick ONE niche
Broad "trending products" accounts rarely grow. Choose one niche where products are visual and impulse-priced (under $40). For example:
- desk setup / home office gadgets
- kitchen gadgets
- travel accessories
- AI and productivity tools (also fits digital products and SaaS affiliates)

### The automated loop (code in this repo)
```
products.csv  ──►  generate_posts.py (Claude)  ──►  queue/YYYY-MM-DD.md  ──►  you review  ──►  scheduler (Buffer/Later/Meta)
     ▲                                                                                              │
     └──────────────────────── keep the products that get clicks, drop the ones that don't ◄───────┘
```
- `affiliate-bot/products.csv`: you paste in the affiliate links (each program generates them from your account).
- `affiliate-bot/generate_posts.py`: Claude drafts 2 X variants, 2 Instagram captions and an image idea per product. It adds your link and an `#ad` disclosure.
- `.github/workflows/weekly-drafts.yml`: runs every Monday and commits a fresh batch of drafts to `queue/`.
- **Posting:** paste the drafts into Buffer's free plan, Meta Business Suite (free Instagram scheduling) or X's built-in scheduler. Automatic posting through the X API is possible later, but the X API's paid tiers can cost more than the subscription you're trying to fund. Manual scheduling of one weekly batch takes about 15 minutes.

### Rules that keep accounts alive
1. **Always disclose** (`#ad` / "I earn a commission"). The FTC and most programs require it, and the script adds it automatically.
2. **Don't make up claims.** The prompt tells Claude not to invent prices, reviews or "I use this daily" stories.
3. **Don't spam** with mass identical posts, follow/unfollow bots or link-only replies. X and Instagram ban accounts for this, and an affiliate program can close your account over it.
4. Put links in your bio (use a free Linktree / Beacons page or your own site), because Instagram captions can't have clickable links.

---

## 3. 30-day starter plan

| Week | You do (human-only steps) | Claude does |
|---|---|---|
| 1 | Choose a niche. Create a dedicated Instagram account (Creator account) and an X account. Apply to Amazon Associates and one other program. Create a Gumroad account. Add `ANTHROPIC_API_KEY` as a GitHub secret. | Research 20 candidate products. Draft your bio. Build digital product #1 (e.g. a "desk setup planner" template that matches the niche). |
| 2 | Add 10 products with links to `products.csv`. Publish product #1 on Gumroad. | Generate the first batch of drafts. Write the Gumroad listing. Build a free "picks" landing page (deploy to Vercel) for the bio link. |
| 3 | Schedule 1 post a day. Spend about 10 minutes a day replying to comments. | Draft the next batch. Build digital product #2. |
| 4 | Check stats: clicks per product and Gumroad views. | Analyse what worked. Replace the weakest products. Adjust the prompts. |

**Decision point at day 60:** keep the channel that has produced any money or clear click traction. Double down on it and drop the other.

---

## 4. Costs to watch
- **Claude API** (for the script): roughly 1 cent or less per product draft at low effort, so a weekly batch of 7 products costs pennies. This is billed separately from a Claude.ai Pro/Max subscription.
- **GitHub Actions**: free for this usage.
- **Domain** (optional): about $10–15 a year.

## 5. What to tell Claude next
- "Build digital product #1 for niche X": I'll create the template or guide plus the listing copy.
- "Build the picks landing page and deploy it": a static site on Vercel with your links.
- "Find 20 products in niche X that fit these rules": research for `products.csv`.
- "Add auto-posting to X": only worth it once posting by hand becomes the bottleneck.
