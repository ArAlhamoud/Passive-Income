# -*- coding: utf-8 -*-
import html, re, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from content import SECTIONS, TOTAL

OUT = str(__import__("pathlib").Path(__file__).resolve().parent.parent / "prompt-kit.html")
BRAND_AR = "اذكى الأعمال الفائقة"
BRAND_EN = "Business Super Intelligence"

AR_NUM = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

def esc(t):
    return html.escape(t, quote=False)

def ph(t):
    """Escape and highlight [PLACEHOLDERS]."""
    return re.sub(r"\[([^\[\]]+)\]", r'<span class="ph">[\1]</span>', esc(t))

CSS = r"""
:root{
  --navy:#0B1F3A; --navy-2:#13325C; --gold:#C9A24B; --gold-soft:#F6EEDB;
  --ink:#1B2430; --muted:#5B6675; --line:#E3E7EE; --paper:#FFFFFF; --tint:#F5F7FA;
  --teal:#0F766E; --teal-soft:#E6F4F2; --ph:#FFF3C4; --ph-ink:#7A5200;
}
@page{ size:A4; margin:16mm 15mm 18mm 15mm;
  @bottom-center{ content:counter(page); font-family:"IBM Plex Sans Arabic","Noto Sans Arabic",sans-serif; font-size:9pt; color:#8A94A3; }
  @bottom-right{ content:"BSI"; font-family:"IBM Plex Sans Arabic",sans-serif; font-size:8pt; color:#B0B8C4; letter-spacing:.15em; }
}
@page cover{ margin:0; @bottom-center{content:none} @bottom-right{content:none} }
*{ box-sizing:border-box; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{ margin:0; background:var(--paper); color:var(--ink);
  font-family:"IBM Plex Sans Arabic","Noto Sans Arabic","Noto Kufi Arabic","Segoe UI","Tahoma","DejaVu Sans",sans-serif;
  font-size:10.5pt; line-height:1.75; }
.en, [lang=en]{ font-family:"IBM Plex Sans","IBM Plex Sans Arabic","Segoe UI",Arial,sans-serif; }
h1,h2,h3{ margin:0; line-height:1.35; }

/* ---------- screen preview ---------- */
@media screen{
  body{ background:#E9EDF2; }
  .page{ width:210mm; min-height:297mm; margin:12px auto; background:#fff; padding:16mm 15mm; box-shadow:0 2px 12px rgba(0,0,0,.08); }
  .cover.page{ padding:0; }
  @media (max-width:820px){ .page{ width:auto; min-height:0; margin:8px; padding:16px; } }
}
@media print{
  .page{ break-before:page; }
  .page:first-child{ break-before:auto; }
}

/* ---------- cover ---------- */
.cover{ page:cover; position:relative; height:297mm; overflow:hidden;
  background:radial-gradient(120% 80% at 85% 10%, #1C4A80 0%, var(--navy) 55%, #071427 100%); color:#fff; }
.cover .frame{ position:absolute; inset:14mm; border:1px solid rgba(201,162,75,.55); border-radius:6mm; }
.cover .pattern{ position:absolute; inset:0; opacity:.10;
  background-image:repeating-linear-gradient(45deg, #C9A24B 0 1px, transparent 1px 22px), repeating-linear-gradient(-45deg, #C9A24B 0 1px, transparent 1px 22px); }
.cover .inner{ position:absolute; inset:30mm 26mm; display:flex; flex-direction:column; }
.cover .brand{ display:flex; align-items:center; gap:12px; }
.cover .mark{ width:46px; height:46px; border-radius:12px; background:var(--gold); color:var(--navy); display:grid; place-items:center; font-weight:700; font-size:15pt; letter-spacing:.04em; font-family:"IBM Plex Sans",sans-serif; }
.cover .brand-ar{ font-size:13pt; font-weight:600; }
.cover .brand-en{ font-size:9.5pt; letter-spacing:.12em; text-transform:uppercase; color:#C8D3E3; }
.cover .titles{ margin-top:auto; margin-bottom:auto; }
.cover .kicker{ display:inline-block; background:rgba(201,162,75,.18); color:#F1DDAE; border:1px solid rgba(201,162,75,.5); padding:4px 14px; border-radius:99px; font-size:10pt; margin-bottom:18px; }
.cover h1{ font-size:34pt; font-weight:700; line-height:1.3; }
.cover h1 .accent{ color:var(--gold); }
.cover .title-en{ direction:ltr; text-align:left; margin-top:18px; font-size:19pt; font-weight:500; color:#DCE4EF; line-height:1.3; }
.cover .rule{ width:90px; height:4px; background:var(--gold); border-radius:4px; margin:26px 0; }
.cover .stats{ display:flex; gap:12px; flex-wrap:wrap; }
.cover .stat{ border:1px solid rgba(255,255,255,.22); border-radius:10px; padding:8px 14px; font-size:10pt; color:#E7EDF5; }
.cover .stat b{ color:var(--gold); font-size:14pt; margin-inline-end:6px; }
.cover .tools{ margin-top:18px; font-size:9.5pt; color:#AFC0D6; }
.cover .foot{ display:flex; justify-content:space-between; align-items:flex-end; font-size:9pt; color:#AFC0D6; }

/* ---------- generic headings ---------- */
.eyebrow{ color:var(--gold); font-weight:600; font-size:9.5pt; letter-spacing:.06em; }
.page-title{ font-size:20pt; color:var(--navy); font-weight:700; }
.page-title-en{ direction:ltr; text-align:left; color:var(--muted); font-size:12pt; font-weight:500; margin-top:2px; }
.divider{ height:3px; width:64px; background:var(--gold); border-radius:3px; margin:12px 0 18px; }
p{ margin:0 0 8px; }

/* ---------- intro ---------- */
.two-col{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.box{ border:1px solid var(--line); border-radius:10px; padding:10px 13px; font-size:9.6pt; line-height:1.6; background:var(--tint); break-inside:avoid; }
.box h3{ font-size:11.5pt; color:var(--navy); margin-bottom:6px; }
.box ol, .box ul{ margin:0; padding-inline-start:20px; }
.box li{ margin-bottom:3px; }
.box.en{ direction:ltr; text-align:left; background:#fff; }
.warn{ border:1px solid #F0D9A8; background:#FFF9EC; border-radius:10px; padding:10px 13px; margin-top:12px; font-size:9.6pt; line-height:1.65; break-inside:avoid; }
.warn h3{ color:#8A5A00; font-size:11.5pt; margin-bottom:4px; }
.warn .en{ direction:ltr; text-align:left; color:#6B5A3A; font-size:8.8pt; line-height:1.5; margin-top:6px; border-top:1px dashed #EBD3A0; padding-top:6px; }
.legend{ display:flex; gap:8px; flex-wrap:wrap; margin-top:10px; font-size:8.8pt; line-height:1.5; }
.legend span.item{ border:1px solid var(--line); border-radius:10px; padding:4px 10px; background:#fff; }
.example{ margin-top:10px; font-size:9.8pt; }

/* ---------- TOC ---------- */
.toc{ list-style:none; margin:0; padding:0; }
.toc li{ display:grid; grid-template-columns:34px 1fr auto; align-items:center; gap:10px; padding:9px 0; border-bottom:1px solid var(--line); }
.toc .n{ width:30px; height:30px; border-radius:8px; background:var(--navy); color:#fff; display:grid; place-items:center; font-weight:600; font-size:10pt; }
.toc .t{ font-weight:600; color:var(--navy); }
.toc .t small{ display:block; direction:ltr; text-align:right; font-weight:400; color:var(--muted); font-size:9pt; }
.toc .c{ color:var(--muted); font-size:9.5pt; white-space:nowrap; }

/* ---------- section header ---------- */
.sec-head{ background:linear-gradient(135deg,var(--navy),var(--navy-2)); color:#fff; border-radius:12px; padding:13px 18px; margin-bottom:11px; position:relative; overflow:hidden; }
.sec-head::after{ content:""; position:absolute; inset-inline-start:-30px; top:-30px; width:120px; height:120px; border-radius:50%; border:16px solid rgba(201,162,75,.18); }
.sec-head .num{ color:var(--gold); font-size:9.5pt; font-weight:600; letter-spacing:.06em; }
.sec-head h2{ font-size:17pt; font-weight:700; }
.sec-head .en-title{ direction:ltr; text-align:left; color:#C8D3E3; font-size:11pt; }
.sec-head .intro{ margin-top:8px; font-size:9.8pt; color:#E3EAF3; }
.sec-head .intro .en{ direction:ltr; text-align:left; color:#AFC0D6; font-size:9pt; margin-top:2px; }

/* ---------- prompt card ---------- */
.card{ border:1px solid var(--line); border-radius:10px; padding:9px 12px 10px; margin-bottom:9px; break-inside:avoid; background:#fff; }
.card-head{ display:flex; gap:10px; align-items:flex-start; }
.card-head .id{ flex:0 0 auto; min-width:30px; height:30px; border-radius:9px; background:var(--gold-soft); color:#8A6A1F; display:grid; place-items:center; font-weight:700; font-size:10.5pt; font-family:"IBM Plex Sans",sans-serif; }
.card-head h3{ font-size:12pt; color:var(--navy); }
.card-head .t-en{ direction:ltr; text-align:right; color:var(--muted); font-size:9.5pt; font-weight:500; }
.card-head .titles{ flex:1; }
.badge{ display:inline-block; font-size:8pt; font-weight:600; background:var(--teal-soft); color:var(--teal); border:1px solid #BFE3DE; border-radius:99px; padding:1px 9px; margin-inline-start:6px; vertical-align:middle; }
.when{ display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:5px 0 6px; font-size:8.8pt; line-height:1.55; color:var(--muted); }
.when .lab{ font-weight:600; color:var(--ink); }
.when .en{ direction:ltr; text-align:left; }
.prompt{ border-radius:8px; padding:7px 11px; font-size:9.6pt; line-height:1.72; position:relative; }
.prompt .lab{ display:block; font-size:8pt; font-weight:600; letter-spacing:.06em; color:var(--muted); margin-bottom:2px; }
.prompt.ar{ background:var(--tint); border-inline-start:3px solid var(--navy); }
.prompt.en{ direction:ltr; text-align:left; background:#FBFCFD; border-left:3px solid var(--gold); margin-top:6px; font-size:8.9pt; line-height:1.55; }
.ph{ background:var(--ph); color:var(--ph-ink); border-radius:4px; padding:0 3px; font-weight:600; box-decoration-break:clone; -webkit-box-decoration-break:clone; }
.tip{ display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:6px; font-size:8.7pt; line-height:1.55; background:var(--teal-soft); border-radius:8px; padding:7px 10px; }
.tip .lab{ font-weight:700; color:var(--teal); }
.tip .en{ direction:ltr; text-align:left; color:#2F4F4B; }

/* ---------- closing ---------- */
.closing{ display:flex; flex-direction:column; justify-content:center; min-height:250mm; text-align:center; }
.closing .mark{ width:64px; height:64px; margin:0 auto 16px; border-radius:16px; background:var(--navy); color:var(--gold); display:grid; place-items:center; font-weight:700; font-size:19pt; font-family:"IBM Plex Sans",sans-serif; }
.closing h2{ font-size:22pt; color:var(--navy); }
.closing .en-h{ direction:ltr; color:var(--muted); font-size:13pt; margin-top:4px; }
.closing .link{ display:inline-block; margin:22px auto 6px; padding:10px 22px; border-radius:99px; background:var(--navy); color:#fff; text-decoration:none; font-weight:600; direction:ltr; }
.closing .sub{ color:var(--muted); font-size:10pt; max-width:140mm; margin:14px auto 0; }
.closing .sub .en{ direction:ltr; margin-top:6px; }
.closing .legal{ margin-top:30px; font-size:8.5pt; color:#8A94A3; }
"""

def card(num, p):
    badge = '<span class="badge">المخرَج باللهجة السعودية · Saudi-dialect output</span>' if p["dialect"] else ""
    return f"""
<article class="card">
  <div class="card-head">
    <div class="id">{num:02d}</div>
    <div class="titles">
      <h3>{esc(p['t_ar'])}{badge}</h3>
      <div class="t-en" lang="en">{esc(p['t_en'])}</div>
    </div>
  </div>
  <div class="when">
    <div><span class="lab">متى تستخدمه: </span>{esc(p['w_ar'])}</div>
    <div class="en" lang="en" dir="ltr"><span class="lab">When to use: </span>{esc(p['w_en'])}</div>
  </div>
  <div class="prompt ar"><span class="lab">الأمر بالعربية</span>{ph(p['p_ar'])}</div>
  <div class="prompt en" lang="en" dir="ltr"><span class="lab">PROMPT · ENGLISH</span>{ph(p['p_en'])}</div>
  <div class="tip">
    <div><span class="lab">نصيحة: </span>{esc(p['tip_ar'])}</div>
    <div class="en" lang="en" dir="ltr"><span class="lab">Tip: </span>{esc(p['tip_en'])}</div>
  </div>
</article>"""

parts = []
# Cover
parts.append(f"""
<section class="page cover">
  <div class="pattern"></div>
  <div class="frame"></div>
  <div class="inner">
    <div class="brand">
      <div class="mark">BSI</div>
      <div><div class="brand-ar">{BRAND_AR}</div><div class="brand-en" lang="en">{BRAND_EN}</div></div>
    </div>
    <div class="titles">
      <div class="kicker">إصدار ثنائي اللغة · Bilingual Edition</div>
      <h1>حقيبة أوامر <span class="accent">الذكاء الاصطناعي</span><br>لأصحاب المشاريع</h1>
      <div class="title-en" lang="en">AI Prompt Kit for<br>Saudi Business Owners</div>
      <div class="rule"></div>
      <div class="stats">
        <div class="stat"><b>{TOTAL}</b>أمرًا جاهزًا للنسخ</div>
        <div class="stat"><b>{len(SECTIONS)}</b>أقسام عملية</div>
        <div class="stat"><b>2</b>لغتان: عربي · English</div>
      </div>
      <div class="tools" lang="en" dir="ltr">Works with Claude · ChatGPT · Gemini · Canva AI</div>
    </div>
    <div class="foot">
      <div>للتسويق، المتاجر، خدمة العملاء، المواسم، التوظيف، والتخطيط</div>
      <div lang="en" dir="ltr">bsi · [WEBSITE_URL]</div>
    </div>
  </div>
</section>""")

# Intro
parts.append(f"""
<section class="page">
  <div class="eyebrow">ابدأ من هنا · START HERE</div>
  <h1 class="page-title">كيف تستخدم هذه الحقيبة</h1>
  <div class="page-title-en" lang="en">How to use this kit</div>
  <div class="divider"></div>
  <p>هذه الحقيبة تضم {TOTAL} أمرًا (Prompt) مكتوبًا بعناية لأصحاب المشاريع الصغيرة والمستقلين في السعودية والخليج. كل أمر مكتوب بالعربية الفصحى وبالإنجليزية، ويعمل مع أدوات مثل Claude وChatGPT وGemini، وبعضها مصمم لمساعدتك في Canva AI.</p>
  <div class="two-col" style="margin-top:10px">
    <div class="box">
      <h3>خطوات الاستخدام</h3>
      <ol>
        <li>اختر الأمر المناسب من الفهرس.</li>
        <li>انسخه كاملًا بالعربية أو الإنجليزية.</li>
        <li>استبدل كل ما بين القوسين <span class="ph">[هكذا]</span> بمعلوماتك الحقيقية.</li>
        <li>الصقه في أداة الذكاء الاصطناعي وأرسله.</li>
        <li>حسّن النتيجة بطلبات قصيرة: «أقصر»، «أكثر رسمية»، «أعطني خيارات أخرى».</li>
        <li>راجع النتيجة وعدّلها قبل النشر أو الإرسال.</li>
      </ol>
    </div>
    <div class="box en" lang="en" dir="ltr">
      <h3>How to use</h3>
      <ol>
        <li>Pick the right prompt from the contents page.</li>
        <li>Copy it in full, in Arabic or English.</li>
        <li>Replace everything in brackets <span class="ph">[LIKE_THIS]</span> with your real details.</li>
        <li>Paste it into your AI tool and send.</li>
        <li>Refine with short follow-ups: "shorter", "more formal", "give me other options".</li>
        <li>Review and edit the result before publishing or sending.</li>
      </ol>
    </div>
  </div>
  <div class="two-col" style="margin-top:10px">
    <div class="box">
      <h3>كيف تملأ الفراغات بين الأقواس</h3>
      <ul>
        <li>كلما كانت المعلومة أدق، كانت النتيجة أفضل. اكتب «عطور عود للرجال بسعر 250–400 ريال» بدل «عطور».</li>
        <li>احذف الأقواس نفسها بعد الكتابة.</li>
        <li>إذا وجدت خيارات مثل <span class="ph">[رسمي / ودّي]</span> فاختر واحدًا فقط.</li>
        <li>إذا لم تنطبق معلومة على مشروعك، احذف الجملة كلها.</li>
      </ul>
      <div class="example"><b>مثال:</b> «لمشروع <span class="ph">[اسم المشروع]</span>» ← «لمشروع مقهى ريحان»</div>
    </div>
    <div class="box en" lang="en" dir="ltr">
      <h3>Filling in the placeholders</h3>
      <ul>
        <li>Be specific: "men's oud perfumes, SAR 250–400" beats "perfumes".</li>
        <li>Remove the brackets themselves once filled in.</li>
        <li>Where you see options like <span class="ph">[formal / friendly]</span>, keep only one.</li>
        <li>If a detail doesn't apply to you, delete the whole sentence.</li>
      </ul>
      <div class="example"><b>Example:</b> "for <span class="ph">[BUSINESS_NAME]</span>" → "for Rayhan Café"</div>
    </div>
  </div>
  <div class="legend">
    <span class="item"><span class="badge" style="margin:0">المخرَج باللهجة السعودية</span> الأمر مكتوب بالفصحى لكنه يطلب أن تكون النتيجة باللهجة السعودية البيضاء.</span>
    <span class="item" lang="en" dir="ltr">The <b>Saudi-dialect</b> badge means the prompt asks for output in everyday Saudi dialect. Remove that line if you want MSA output.</span>
  </div>
</section>""")

# TOC
toc_items = []
n = 1
for i, s in enumerate(SECTIONS, 1):
    a, b = n, n + len(s["prompts"]) - 1
    toc_items.append(f"""<li><div class="n">{i}</div><div class="t">{esc(s['ar'])}<small lang="en">{esc(s['en'])}</small></div><div class="c"><span>{len(s['prompts'])} أوامر</span> · <span dir="ltr" lang="en">#{a}–{b}</span></div></li>""")
    n = b + 1
parts.append(f"""
<section class="page">
  <div class="eyebrow">الفهرس · CONTENTS</div>
  <h1 class="page-title">محتويات الحقيبة</h1>
  <div class="page-title-en" lang="en">What's inside — {TOTAL} prompts in {len(SECTIONS)} sections</div>
  <div class="divider"></div>
  <ul class="toc">{''.join(toc_items)}</ul>
  <div class="warn" style="margin-top:22px">
    <h3>تنبيه مهم: راجع كل ما ينتجه الذكاء الاصطناعي</h3>
    <p style="margin:0">أدوات الذكاء الاصطناعي قد تخطئ في المعلومات أو الحسابات أو التواريخ، وقد تخترع تفاصيل غير صحيحة. تحقق من الأسعار والأرقام ومواعيد المناسبات الهجرية والمعلومات النظامية (مثل نظام العمل وضريبة القيمة المضافة والتجارة الإلكترونية) من مصادرها الرسمية قبل النشر. هذه الحقيبة أداة مساعدة للكتابة والتفكير، وليست استشارة قانونية أو محاسبية. ولا تُدخل بيانات حساسة مثل أرقام الهويات أو الحسابات البنكية أو بيانات العملاء الشخصية في أي أداة.</p>
    <div class="en" lang="en">Important: AI tools can get facts, maths and dates wrong, and can invent details. Verify prices, numbers, Hijri dates and regulatory information (Labor Law, VAT, e-commerce rules) against official sources before publishing. This kit helps you write and think; it is not legal or accounting advice. Never paste sensitive data such as ID numbers, bank details or customers' personal information into an AI tool.</div>
  </div>
</section>""")

# Sections
n = 1
for i, s in enumerate(SECTIONS, 1):
    cards = []
    for p in s["prompts"]:
        cards.append(card(n, p)); n += 1
    parts.append(f"""
<section class="page" id="sec-{s['key']}">
  <header class="sec-head">
    <div class="num"><span>القسم {i}</span> · <span lang="en" dir="ltr">SECTION {i}</span></div>
    <h2>{esc(s['ar'])}</h2>
    <div class="en-title" lang="en">{esc(s['en'])}</div>
    <div class="intro">{esc(s['intro_ar'])}<div class="en" lang="en">{esc(s['intro_en'])}</div></div>
  </header>
  {''.join(cards)}
</section>""")

# Closing
parts.append(f"""
<section class="page">
  <div class="closing">
    <div class="mark">BSI</div>
    <h2>شكرًا لك، وبالتوفيق في مشروعك</h2>
    <div class="en-h" lang="en">Thank you — and best of luck with your business</div>
    <p class="sub">هذه الحقيبة من <b>{BRAND_AR}</b>. ابدأ بثلاثة أوامر فقط هذا الأسبوع، وجرّبها على مشروعك الحقيقي، ثم أضف غيرها تدريجيًا.
      <span class="en" lang="en" style="display:block">This kit is by <b>{BRAND_EN}</b>. Start with just three prompts this week, try them on your real business, then add more gradually.</span></p>
    <a class="link" href="[WEBSITE_URL]">bsi · [WEBSITE_URL]</a>
    <p class="sub">لمزيد من الأدوات والموارد زر موقعنا. · <span lang="en">For more tools and resources, visit our website.</span></p>
    <p class="legal">© {BRAND_AR} | {BRAND_EN}. للاستخدام الشخصي والتجاري داخل مشروعك. لا يُسمح بإعادة بيع الحقيبة أو توزيعها.<br>
      <span lang="en">For personal and in-business use. Reselling or redistributing this kit is not permitted.</span><br>
      <span lang="en">Claude, ChatGPT, Gemini, Canva, Salla, Zid, Shopify, Google and WhatsApp are trademarks of their respective owners; BSI is not affiliated with them.</span></p>
  </div>
</section>""")

doc = f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>حقيبة أوامر الذكاء الاصطناعي لأصحاب المشاريع — AI Prompt Kit | BSI</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>
"""
open(OUT, "w", encoding="utf-8").write(doc)
print("wrote", OUT, TOTAL)
