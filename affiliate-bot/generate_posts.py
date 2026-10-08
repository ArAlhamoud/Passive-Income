"""Draft affiliate social posts (X + Instagram) from products.csv using Claude.

Usage:
    export ANTHROPIC_API_KEY=...
    python generate_posts.py                # drafts for every active product
    python generate_posts.py --limit 3      # only the first 3 active products
    python generate_posts.py --dry-run      # no API calls, writes placeholder drafts

Output: one Markdown file per run in ../queue/, ready to review and paste into
a scheduler (Buffer, Later, Meta Business Suite, X's native scheduler).
Drafts are never posted automatically: you review every one before it goes out.
"""

import argparse
import csv
import datetime as dt
import json
import os
import pathlib
import sys

from sync_links import is_live, tracked_url

ROOT = pathlib.Path(__file__).resolve().parent
QUEUE_DIR = ROOT.parent / "queue"
MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-5-5")
DISCLOSURE = os.environ.get(
    "AFFILIATE_DISCLOSURE", "#إعلان #ad — قد أحصل على عمولة عند الشراء عبر الرابط | I may earn a commission."
)
OWN_PRODUCT_NOTE = "منتجنا | Our product"

SYSTEM = """You write short, honest social media posts for the brand
"اذكى الأعمال الفائقة | Business Super Intelligence": AI and productivity tools for small business
owners and freelancers in Saudi Arabia and the Gulf.
Rules:
- Write in Arabic (clear Modern Standard Arabic, light Saudi flavour is fine) AND English, as asked below.
- Focus on a concrete business use (e.g. "write your Salla product descriptions in 5 minutes"), not hype.
- Never invent specs, prices, discounts, reviews, ratings or scarcity ("only 3 left") — you don't know them.
- No fake personal experience ("I've used this for months"). Speak about the product, not about yourself.
- Hook in the first line, plain language, at most 2 emojis.
- X post: max 230 characters EXCLUDING the link and disclosure (those get appended later).
- Instagram caption: 2-4 short lines plus 5-8 relevant hashtags. Mention "link in bio".
- x_posts: exactly 2 posts, the first in Arabic, the second in English.
- instagram_captions: exactly 2 captions, the first in Arabic, the second in English.
- image_idea: one line in English describing a simple visual (screenshot, before/after, short reel idea)."""

SCHEMA = {
    "type": "object",
    "properties": {
        "x_posts": {"type": "array", "items": {"type": "string"}},
        "instagram_captions": {"type": "array", "items": {"type": "string"}},
        "image_idea": {"type": "string"},
    },
    "required": ["x_posts", "instagram_captions", "image_idea"],
    "additionalProperties": False,
}


def load_products(path: pathlib.Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if is_live(r)]


def draft_for(client, product: dict) -> dict:
    prompt = (
        f"Product: {product['name']}\n"
        f"Type: {'our own product' if product['kind'] == 'own-product' else 'affiliate partner'}\n"
        f"Category: {product['category']}\n"
        f"Why it sells (my notes): {product['why_it_sells']}"
    )
    response = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
        output_config={
            "effort": "low",
            "format": {"type": "json_schema", "schema": SCHEMA},
        },
    )
    if response.stop_reason == "refusal":
        raise RuntimeError(f"model declined product {product['slug']}")
    text = next(b.text for b in response.content if b.type == "text")
    return json.loads(text)


def placeholder(product: dict) -> dict:
    return {
        "x_posts": [f"[dry run] X post about {product['name']}"],
        "instagram_captions": [f"[dry run] IG caption about {product['name']}"],
        "image_idea": "[dry run]",
    }


def render(product: dict, draft: dict) -> str:
    today = dt.date.today().isoformat()
    note = OWN_PRODUCT_NOTE if product["kind"] == "own-product" else DISCLOSURE
    lines = [f"## {product['name']} (`{product['slug']}`)", "", "### X"]
    for i, post in enumerate(draft["x_posts"], 1):
        link = tracked_url(product["slug"], f"x-{today}-{i}")
        lines += [f"**Variant {i}**", "", f"{post}\n{link}\n{note}", ""]
    lines.append(f"### Instagram (bio link → site; story link: {tracked_url(product['slug'], 'ig-' + today)})")
    for i, cap in enumerate(draft["instagram_captions"], 1):
        lines += [f"**Variant {i}**", "", f"{cap}\n\n{note}", ""]
    lines += [f"_Image idea:_ {draft['image_idea']}", "", "---", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--products", default=str(ROOT / "products.csv"))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    products = load_products(pathlib.Path(args.products))
    if args.limit:
        products = products[: args.limit]
    if not products:
        print("No live products (active=yes with a real https link) in products.csv", file=sys.stderr)
        return 1

    client = None
    if not args.dry_run:
        import anthropic

        client = anthropic.Anthropic()

    sections = []
    for p in products:
        try:
            draft = placeholder(p) if args.dry_run else draft_for(client, p)
        except Exception as e:  # keep going; one bad product shouldn't kill the batch
            print(f"skip {p['slug']}: {e}", file=sys.stderr)
            continue
        sections.append(render(p, draft))

    QUEUE_DIR.mkdir(exist_ok=True)
    out = QUEUE_DIR / f"{dt.date.today().isoformat()}.md"
    header = f"# Post drafts — {dt.date.today().isoformat()}\n\nReview before posting. Delete anything that isn't true.\n\n"
    out.write_text(header + "\n".join(sections), encoding="utf-8")
    print(f"wrote {out} ({len(sections)} products)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
