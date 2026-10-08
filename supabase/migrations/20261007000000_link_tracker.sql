-- Affiliate link tracker: /go/<slug> logs a click, then redirects to target_url.
create table public.links (
  slug        text primary key check (slug ~ '^[a-z0-9-]{1,64}$'),
  name        text not null,
  target_url  text not null check (target_url ~ '^https://'),
  kind        text not null default 'affiliate' check (kind in ('affiliate', 'own-product', 'other')),
  active      boolean not null default true,
  created_at  timestamptz not null default now()
);

create table public.clicks (
  id          bigint generated always as identity primary key,
  slug        text not null references public.links (slug) on update cascade on delete cascade,
  src         text,            -- which post/channel, e.g. ?src=ig-2026-10-07
  referrer    text,
  is_bot      boolean not null default false,
  created_at  timestamptz not null default now()
);
create index clicks_slug_created_at_idx on public.clicks (slug, created_at);

-- Only the edge function (service role) touches these tables; no public access.
alter table public.links  enable row level security;
alter table public.clicks enable row level security;

-- Weekly report helper: human clicks per link and source over the last N days.
create view public.click_stats with (security_invoker = true) as
select l.slug, l.name, l.kind, c.src,
       count(*) filter (where c.created_at > now() - interval '7 days')  as clicks_7d,
       count(*) filter (where c.created_at > now() - interval '30 days') as clicks_30d,
       count(*) as clicks_all
from public.links l
join public.clicks c on c.slug = l.slug and not c.is_bot
group by l.slug, l.name, l.kind, c.src;
