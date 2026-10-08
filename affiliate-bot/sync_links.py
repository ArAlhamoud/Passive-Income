"""Sync products.csv to the click tracker (Supabase) and the landing page (site/picks.json).

A row is "live" when active=yes and affiliate_url is a real https:// link.
- Live rows are upserted into the tracker's `links` table.
- Rows that are no longer live are switched off in the tracker.
- site/picks.json lists only live rows, with tracked /go/<slug> URLs.

Usage:
    python sync_links.py              # writes picks.json; syncs tracker if keys are set
Env:
    SUPABASE_URL                  e.g. https://xbnqrryetgbqhkfpubzb.supabase.co
    SUPABASE_SECRET_KEY           secret / service_role key (GitHub secret, never commit it)
"""

import csv
import json
import os
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT.parent / "site"
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://xbnqrryetgbqhkfpubzb.supabase.co").rstrip("/")
TRACKER_BASE = f"{SUPABASE_URL}/functions/v1/go"


def is_live(row: dict) -> bool:
    return row["active"].strip().lower() == "yes" and row["affiliate_url"].startswith("https://")


def tracked_url(slug: str, src: str) -> str:
    return f"{TRACKER_BASE}/{slug}?src={src}"


def rest(method: str, path: str, key: str, body=None, prefer: str = "") -> None:
    headers = {"apikey": key, "Content-Type": "application/json"}
    if key.startswith("eyJ"):  # legacy JWT service_role key also goes in Authorization
        headers["Authorization"] = f"Bearer {key}"
    if prefer:
        headers["Prefer"] = prefer
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/{path}", data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        resp.read()


def main() -> int:
    with (ROOT / "products.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    live = [r for r in rows if is_live(r)]
    dead = [r["slug"] for r in rows if not is_live(r)]

    SITE.mkdir(exist_ok=True)
    picks = [
        {"slug": r["slug"], "name": r["name"], "category": r["category"], "kind": r["kind"],
         "blurb": r["why_it_sells"], "url": tracked_url(r["slug"], "site")}
        for r in live
    ]
    (SITE / "picks.json").write_text(json.dumps(picks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"site/picks.json: {len(picks)} live links")

    key = os.environ.get("SUPABASE_SECRET_KEY")
    if not key:
        print("SUPABASE_SECRET_KEY not set: skipped tracker sync")
        return 0
    if live:
        rest("POST", "links?on_conflict=slug", key,
             [{"slug": r["slug"], "name": r["name"], "target_url": r["affiliate_url"],
               "kind": r["kind"], "active": True} for r in live],
             prefer="resolution=merge-duplicates,return=minimal")
    if dead:
        rest("PATCH", f"links?slug=in.({','.join(dead)})", key, {"active": False}, prefer="return=minimal")
    print(f"tracker: {len(live)} upserted, {len(dead)} switched off")
    return 0


if __name__ == "__main__":
    sys.exit(main())
