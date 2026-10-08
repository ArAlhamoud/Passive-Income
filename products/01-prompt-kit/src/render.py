import glob, asyncio, os
from playwright.sync_api import sync_playwright

D = str(__import__("pathlib").Path(__file__).resolve().parent.parent)
S = os.path.dirname(os.path.abspath(__file__))
exe = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))[-1]

FONT_CHECK = """async () => { await document.fonts.ready;
  return { ar: document.fonts.check('700 16px "IBM Plex Sans Arabic"', 'حقيبة'),
           ar4: document.fonts.check('400 16px "IBM Plex Sans Arabic"', 'حقيبة'),
           en: document.fonts.check('500 16px "IBM Plex Sans"', 'Kit'),
           loaded: [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight).slice(0,30) } }"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe)
    pg = b.new_page()
    pg.goto("file://" + D + "/prompt-kit.html", wait_until="networkidle")
    pg.emulate_media(media="print")
    # force-load all weights used
    pg.evaluate("""async()=>{ for (const w of [400,500,600,700]) { await document.fonts.load(w+' 16px "IBM Plex Sans Arabic"','عربي'); await document.fonts.load(w+' 16px "IBM Plex Sans"','Latin'); } }""")
    print("fonts:", pg.evaluate(FONT_CHECK))
    pg.pdf(path=D + "/prompt-kit.pdf", format="A4", print_background=True, prefer_css_page_size=True)

    cp = b.new_page(viewport={"width": 1280, "height": 720})
    cp.goto("file://" + D + "/cover.html", wait_until="networkidle")
    print("cover fonts:", cp.evaluate(FONT_CHECK))
    cp.screenshot(path=D + "/cover.png")
    b.close()
