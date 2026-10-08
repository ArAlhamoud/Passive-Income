// GET /functions/v1/go/<slug>?src=<post-id>  ->  log click, 302 to the link's target.
import { createClient } from "jsr:@supabase/supabase-js@2";

const supabase = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
);
const FALLBACK = Deno.env.get("SITE_URL") ?? "https://github.com/ArAlhamoud/Passive-Income";
const BOT_RE = /bot|crawl|spider|preview|facebookexternalhit|slurp|curl|wget|python|headless/i;

const redirect = (url: string) =>
  new Response(null, { status: 302, headers: { Location: url, "Cache-Control": "no-store" } });

Deno.serve(async (req) => {
  const url = new URL(req.url);
  const slug = url.pathname.split("/").filter(Boolean).pop() ?? "";
  if (!/^[a-z0-9-]{1,64}$/.test(slug) || slug === "go") return redirect(FALLBACK);

  const { data: link } = await supabase
    .from("links").select("target_url").eq("slug", slug).eq("active", true).maybeSingle();
  if (!link) return redirect(FALLBACK);

  const log = supabase.from("clicks").insert({
    slug,
    src: url.searchParams.get("src")?.slice(0, 64) ?? null,
    referrer: req.headers.get("referer")?.slice(0, 256) ?? null,
    is_bot: BOT_RE.test(req.headers.get("user-agent") ?? ""),
  }).then(({ error }) => { if (error) console.error("click insert failed", error.message); });

  // Don't make the visitor wait for the insert.
  // deno-lint-ignore no-explicit-any
  const rt = (globalThis as any).EdgeRuntime;
  if (rt?.waitUntil) rt.waitUntil(log); else await log;

  return redirect(link.target_url);
});
