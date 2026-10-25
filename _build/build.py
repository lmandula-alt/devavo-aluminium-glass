"""Builds the Devavo website pages from the content below and photo-manifest.json.

Run from the repo root:  python _build/build.py          (final pages)
                         python _build/build.py --demo   (adds a "demo for review" banner)
"""
import hashlib, html, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEMO = "--demo" in sys.argv
SITE_URL = "https://devavo.co.za"
PHONE, PHONE_INTL = "079 034 0115", "+27790340115"  # one number for calls, WhatsApp and the catalogue
WHATSAPP = "27790340115"
EMAIL = "luthando@devavo.co.za"
ADDRESS = ("5 Diesel Street, North End", "Gqeberha", "6001")
HOURS = [("Mon – Fri", "08:00 – 16:00"), ("Weekends", "On WhatsApp")]
# open_status in assets/site.js uses the same hours: Mon–Fri 08:00–16:00, South African time
FACEBOOK = "https://www.facebook.com/share/16CC9W"
WA_CATALOGUE = "https://wa.me/c/27790340115"
# Visitor tracking. Paste the IDs in and rebuild; nothing loads until a visitor accepts cookies.
GA4_ID = "G-V5W44GBSJN"  # Google Analytics 4 Measurement ID
META_PIXEL_ID = ""   # Meta (Facebook) Pixel ID, e.g. "123456789012345"
AREAS = ["Gqeberha (Port Elizabeth)", "Kariega (Uitenhage)", "Despatch", "Jeffreys Bay", "Kouga",
         "Makhanda", "Graaff-Reinet", "Sundays River Valley", "Eastern Cape-wide for commercial work"]

PHOTOS = json.load(open(os.path.join(ROOT, "photo-manifest.json"), encoding="utf-8"))
BY_SLUG = {p["slug"]: p for p in PHOTOS}
e = html.escape

# ----------------------------------------------------------------- content
DIVISIONS = [
  {
    "key": "01 Aluminium & Glass", "slug": "aluminium-glass", "name": "Aluminium & Glass", "num": "01",
    "title": "Aluminium Doors, Windows & Shopfronts in Gqeberha",
    "meta": "Custom aluminium doors, windows, sliding and folding doors, shopfronts and glass partitions, made in our Gqeberha workshop and fitted by our own team since 2010.",
    "hero": "ag-french-door-wall", "card": "ag-door-sunburst-pivot-black",
    "h1": "Aluminium and glass, made to measure in Gqeberha",
    "lead": "Doors, windows, shopfronts and sliding systems cut, assembled and glazed in our own workshop, then fitted by the same team that built them. Aluminium is where Devavo started in 2010.",
    "card_text": "Pivot and entrance doors, windows, sliding and folding doors, shopfronts and glass partitions.",
    "tags": ["Doors", "Windows", "Sliding & folding", "Shopfronts", "Partitions", "Glass & mirrors"],
    "services": [
      ("Pivot & entrance doors", "Statement front doors in sunburst, diamond, slatted or plain designs, built to the opening and hung on heavy-duty pivots or hinges."),
      ("Windows", "Top-hung, side-hung, sliding and fixed windows in standard or custom sizes, including replacing old steel and timber frames with aluminium."),
      ("Sliding, folding & stacking doors", "Patio sliders, bi-folds and stacking doors that open a living room to the garden, sized and hung to run smoothly."),
      ("Shopfronts & commercial glazing", "Shopfronts, entrance doors, curtain walling and office partitions for shops, banks, offices, campuses and public buildings."),
      ("Enclosures & sunrooms", "Patio enclosures, garden rooms and sunrooms that turn a stoep into usable space all year."),
      ("Glass, mirrors & bathrooms", "Glass and mirror cutting, safety glass, shower and bathroom doors, and replacement glazing."),
    ],
    "why_img": "ag-shopfront-sanparks",
    "why_title": "One workshop, one team, from measure to handover",
    "why_text": "Every opening is measured on site before anything is cut. Frames are assembled and glazed in our North End workshop and installed by our own fitters, so the people who quote are the people who answer for the finish.",
    "why_points": ["Site measure before fabrication", "Powder-coated and anodised finishes chosen for coastal air",
                   "Safety glass specified for doors and low-level glazing", "Residential, commercial and public-sector work"],
    "videos": [],
    "faqs": [
      ("Do you measure on site before quoting?", "Yes. We measure every opening ourselves before fabrication, so the frame is made for your wall and not a standard size that needs packing out."),
      ("Can you replace my old wooden or steel windows with aluminium?", "Yes. Swapping timber and steel frames for aluminium is a large part of our residential work. We remove the old frames, fit the new ones and make good around the opening."),
      ("Which colours and finishes are available?", "Most of our work is in bronze, charcoal, black, white and natural silver, in powder-coated or anodised finishes that suit the Eastern Cape's salt air. Ask us if you need a specific colour."),
      ("Do you do commercial shopfronts and tenders?", "Yes. We have installed shopfronts, partitions and replacement glazing for SANParks, South Point, Nelson Mandela University, hospitals and municipal buildings."),
    ],
  },
  {
    "key": "02 Automation - Garage Doors & Gates", "slug": "automation", "name": "Automation", "num": "02",
    "title": "Garage Doors, Driveway Gates & Gate Motors in Gqeberha",
    "meta": "Aluminium garage doors, sliding and swing driveway gates, and gate and garage door motors, made, installed and automated by one team in Gqeberha.",
    "hero": "au-garage-double-2", "card": "au-garage-full-view-glass",
    "h1": "Garage doors and gates, built and automated by one team",
    "lead": "We make the garage door or gate in our own workshop, install it, and fit the motor, so there is one contractor responsible for how it looks and how it runs.",
    "card_text": "Garage doors and driveway gates with the motors, remotes and safety beams that run them.",
    "tags": ["Garage doors", "Garage motors", "Driveway gates", "Gate motors", "Pedestrian gates"],
    "services": [
      ("Garage doors", "Sectional and full-view aluminium garage doors made to your opening: slatted, glazed, frosted or patterned, in colours to match the house."),
      ("Garage door motors", "Supply and installation of garage door motors and remotes, so the door opens from the car at the press of a button."),
      ("Driveway gates", "Sliding and swing driveway gates in aluminium and steel: slatted, solid, glazed or timber-look, built to the width of your entrance."),
      ("Gate motors & automation", "Sliding and swing gate motors installed and set up, from homes to heavy-duty motors on public-sector sites."),
      ("Pedestrian gates & boundary infill", "Matching pedestrian gates and slatted infill panels for boundary walls, so the whole frontage reads as one design."),
      ("Remotes, beams & servicing", "Remote programming, safety beams and servicing to keep an existing gate or garage door running reliably."),
    ],
    "why_img": "au-gate-slatted-pair",
    "why_title": "The door, the gate and the motor from one place",
    "why_text": "When the gate is built by one company and automated by another, problems fall between the two. We fabricate the gate or garage door to suit the motor it will carry, then install and set up both.",
    "why_points": ["Gates and doors made in our own workshop", "Motor sized to the weight and width of the gate",
                   "Matching gates, garage doors and boundary infill", "Heavy-duty installs for public-sector sites"],
    "videos": [("garage-door-opening", "Full-view garage door opening"), ("sliding-gate-closing", "Sliding driveway gate in operation"),
               ("boundary-gate-install", "Boundary gates and infill going in")],
    "faqs": [
      ("Can you automate the gate or garage door I already have?", "Usually, yes. We check the gate or door, its track and its weight, and recommend a motor that suits it. If the gate needs repairs first, we will tell you."),
      ("Do you make the gate and fit the motor yourselves?", "Yes. Our workshop builds the gate or garage door, and our team installs it and sets up the motor, remotes and safety beams."),
      ("Which gate motors do you install?", "We install established South African gate motor brands, and choose the model for the gate's weight, length and daily use. The quote names the motor so you can compare."),
      ("Do you do commercial and public-sector gates?", "Yes. We have installed heavy-duty gate motors for EC Public Works in Graaff-Reinet and gate automation for EC Social Development."),
    ],
  },
  {
    "key": "03 Construction & Renovations", "slug": "construction", "name": "Construction & Renovations", "num": "03",
    "title": "Building, Renovations & Maintenance Contractor in Gqeberha",
    "meta": "General building, renovations and extensions, hotel and accommodation refurbishment, ceilings, carports and building maintenance across Gqeberha and the Eastern Cape.",
    "hero": "co-brick-extension", "card": "co-interior-skylight",
    "h1": "Building, renovations and maintenance",
    "lead": "Since 2015 Devavo has built, renovated and maintained homes, accommodation, offices and public buildings. Because we also make our own doors, windows and gates, a renovation can be handled by one contractor from foundation to final fitting.",
    "card_text": "Renovations and extensions, hotel and accommodation refurbishment, general building, ceilings and maintenance.",
    "tags": ["Renovations", "Hotel refurbishment", "General building", "Ceilings", "Carports", "Maintenance"],
    "services": [
      ("Renovations & extensions", "Home and office renovations, room additions and open-plan conversions, from brickwork and roofing to the final coat of paint."),
      ("Hotel & accommodation refurbishment", "Room, corridor and common-area refurbishments for hotels, guest houses and student accommodation, planned around occupancy."),
      ("General building", "New builds, brickwork and masonry packages for main contractors and private clients."),
      ("Ceilings, bulkheads & plastering", "Suspended ceilings, bulkheads, skylights, plastering and painting."),
      ("Carports, roofing & structures", "Steel carports, roof repairs, timber structures and platforms."),
      ("Maintenance & remedial works", "Planned and reactive maintenance for property managers, schools and public buildings, and repair of fire- or storm-damaged homes."),
    ],
    "why_img": "co-interior-bulkhead",
    "why_title": "A builder that also makes the doors and windows",
    "why_text": "On most renovations the aluminium is subcontracted, and the programme waits on someone else's workshop. We build the walls and make the frames that go into them, so openings are sized right and the job keeps moving.",
    "why_points": ["Brickwork, plastering, ceilings and painting in-house", "Aluminium, glazing and gates from our own workshop",
                   "Experience with main contractors such as WBHO", "Public-sector, commercial and residential projects"],
    "videos": [("site-build-scaffolding", "Commercial site, 2020")],
    "faqs": [
      ("Do you take on small renovations as well as large projects?", "Yes. We do everything from a single bathroom or room addition to full refurbishments and masonry packages for main contractors."),
      ("Can you refurbish rooms in a hotel or guest house while it stays open?", "Yes. We plan the work in phases around occupancy, so rooms come out of service in batches rather than all at once."),
      ("Do you work for municipalities and government departments?", "Yes. Recent work includes community halls for Nelson Mandela Bay Municipality, building repairs for EC Public Works and remedial works for NHFC."),
      ("Are you registered with the CIDB?", "Yes. Devavo Trading Enterprise CC is registered with the Construction Industry Development Board. Ask us for our current grading and documents."),
    ],
  },
  {
    "key": "04 Balustrades & Security", "slug": "balustrades-security", "name": "Balustrades & Security", "num": "04",
    "title": "Glass Balustrades, Handrails & Security Gates in Gqeberha",
    "meta": "Frameless glass and aluminium balustrades, handrails, trellis security gates and burglar bars, made and installed in Gqeberha and the Eastern Cape.",
    "hero": "bs-glass-stair", "card": "bs-glass-stair-handrail",
    "h1": "Balustrades, handrails and security gates",
    "lead": "Clear glass balustrades for stairs and balconies, aluminium railings for coastal homes, and trellis gates and burglar bars that secure a building without making it look like a cage.",
    "card_text": "Frameless glass and aluminium balustrades, handrails, trellis gates and burglar bars.",
    "tags": ["Glass balustrades", "Aluminium balustrades", "Handrails", "Trellis gates", "Burglar bars"],
    "services": [
      ("Frameless glass balustrades", "Clear toughened-glass balustrades for staircases, landings and balconies, with or without a top handrail."),
      ("Aluminium & glass balustrades", "Framed aluminium balustrades with glass infill for balconies, decks and stoeps: low-maintenance in salt air."),
      ("Handrails & railings", "Aluminium and steel handrails for stairs, ramps and public buildings."),
      ("Trellis & security gates", "Retractable trellis gates and fixed security gates for doors, shopfronts and windows."),
      ("Burglar bars", "Aluminium and steel burglar bars made to fit and match your windows."),
      ("Custom steel & aluminium fabrication", "Frames, cabinets, enclosures and one-off pieces cut and welded to your drawing."),
    ],
    "why_img": "bs-glass-stair-install",
    "why_title": "Safety you can see through",
    "why_text": "A balustrade has to hold a load and still look light. We specify toughened glass and fixings for the height and use of each stair or balcony, and fit them with the same care as our doors and windows.",
    "why_points": ["Toughened safety glass for every balustrade", "Stainless, black or aluminium handrails",
                   "Security gates keyed to match existing doors", "Made and installed by our own team"],
    "videos": [],
    "faqs": [
      ("Is a frameless glass balustrade safe for a home with children?", "Yes, when it uses toughened safety glass of the right thickness and is fixed properly. We specify the glass and fixings for the height and use of each staircase or balcony."),
      ("Can you add a glass balustrade to an existing staircase?", "Usually, yes. We check the stair structure and choose a fixing method, side-fixed or channel, that suits it."),
      ("Do you make trellis gates to fit odd-sized openings?", "Yes. Our trellis and security gates are made to measure for each door, window or shopfront."),
    ],
  },
]
DIV_BY_KEY = {d["key"]: d for d in DIVISIONS}
DIV_BY_KEY["05 Custom Fabrication"] = DIVISIONS[3]  # fabrication photos sit with Balustrades & Security

TRACK_RECORD = [
  ("2026", "Nelson Mandela Bay Municipality", "Building works at Daleview Community Hall and KwaMagxaki Hall (Ward 30)", "construction"),
  ("2026", "Nelson Mandela Bay Municipality", "Building works, Jeff Masemola, KwaNobuhle", "construction"),
  ("2025", "NHFC", "Remedial works to a fire-damaged house, Jeffreys Bay", "construction"),
  ("2024", "Nelson Mandela University", "Aluminium windows, Solomon Mahlangu building", "aluminium-glass"),
  ("2024", "EC Social Development", "Gate motors and nylon gear rack, Ernest Malgas Treatment Centre", "automation"),
  ("2024", "EC Public Works & Infrastructure", "Minor building repairs to houses, Makhanda", "construction"),
  ("2024", "Sundays River Valley Municipality", "Entry doors for community halls", "aluminium-glass"),
  ("2021", "EC Public Works & Infrastructure", "Heavy-duty gate motor installation, Graaff-Reinet", "automation"),
  ("2021", "South Point, Gqeberha", "Shopfront installations", "aluminium-glass"),
  ("2020", "WBHO", "Brickwork for the APLI cold storage facility, Coega IDZ", "construction"),
  ("2020", "SANParks, Tsitsikamma", "Glass supply and installation for the restaurant", "aluminium-glass"),
  ("2020", "South Point, Gqeberha", "Suspended ceilings", "construction"),
  ("2019", "South Point, Gqeberha", "Annual building painting maintenance", "construction"),
  ("2014", "FM Solutions (EC Health maintenance)", "Replacement sliding aluminium sashes, Dora Nginza Hospital", "aluminium-glass"),
]
CLIENTS = ["WBHO", "SANParks", "Nelson Mandela Bay Municipality", "Nelson Mandela University", "EC Public Works & Infrastructure",
           "EC Social Development", "EC Department of Education", "NHFC", "Sundays River Valley Municipality",
           "South Point", "Builders Warehouse Walmer", "C&K Construction"]
REFERENCE = ("They have performed well and would recommend them for contracts of similar value.",
             "Zusakhe Mahonono, SMME Manager, WBHO (completion letter, APLI cold storage facility, Coega)")

# ----------------------------------------------------------------- helpers
ICON = {
  "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
  "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
  "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
  "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
  "quote": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>',
  "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.39-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35z"/><path d="M12 2a10 10 0 0 0-8.2 15.7L2.5 22l4.43-1.26A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.17-1.14l-.3-.18-3.01.86.83-2.94-.19-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>',
  "catalogue": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>',
  "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
}

def img(slug, alt=None, cls="", sizes="100vw", eager=False, attrs="", thumb=False):
    """thumb=True serves the 640px version and keeps the full photo for the lightbox."""
    p = BY_SLUG[slug]
    alt = p["desc"] if alt is None else alt
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    src = f"images/work/thumb/{slug}.webp" if thumb else f"images/work/{slug}.webp"
    full = f' data-full="images/work/{slug}.webp"' if thumb else ""
    return (f'<img src="{src}"{full} alt="{e(alt)}" width="{p["w"]}" height="{p["h"]}" '
            f'{load}{c} {attrs}>').replace(" >", ">")

def tracking_config():
    if not (GA4_ID or META_PIXEL_ID):
        return ""
    return f'<script>window.DEVAVO_TRACKING={json.dumps({"ga4": GA4_ID, "pixel": META_PIXEL_ID})};</script>'

def consent_banner():
    if not (GA4_ID or META_PIXEL_ID):
        return ""
    uses = " and ".join(x for x in ("count visitors" if GA4_ID else "",
                                     "show our adverts on Facebook and Instagram" if META_PIXEL_ID else "") if x)
    return f"""<div class="consent" id="consent" role="dialog" aria-live="polite" aria-label="Cookie choice" hidden>
  <p>We use cookies to {uses}. <a href="privacy.html">Read more</a></p>
  <div><button type="button" class="btn btn-outline" data-consent="no">Decline</button><button type="button" class="btn btn-primary" data-consent="yes">Accept</button></div>
</div>"""

def asset_version(name):
    """Short content hash so browsers fetch the new file whenever it changes."""
    return hashlib.md5(open(os.path.join(ROOT, "assets", name), "rb").read()).hexdigest()[:8]

def url(path):
    return (SITE_URL + "/" + path) if SITE_URL else path

def wa_link(text="Hi Devavo, I'd like a quote for "):
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP}?text={quote(text)}"

NAV = [("index.html", "Home"), ("aluminium-glass.html", "Aluminium & Glass"), ("automation.html", "Automation"),
       ("construction.html", "Construction"), ("balustrades-security.html", "Balustrades & Security"),
       ("projects.html", "Projects")]

def header(current):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{e(t)}</a>' for h, t in NAV)
    banner = ('<div class="demo-banner">Demo for review. This version is not published; links and form are for testing only.</div>'
              if DEMO else "")
    return f"""{banner}<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <span class="tb-left"><span class="open-status" data-open-status><i></i><span>Call or WhatsApp {PHONE}</span></span></span>
  <span class="tb-right"><a href="{WA_CATALOGUE}" target="_blank" rel="noopener">View<span class="tb-long"> our</span> catalogue</a><a href="tel:{PHONE_INTL}"><span class="tb-long">Call / WhatsApp </span>{PHONE}</a></span>
</div></div>
<header class="site-nav">
  <div class="nav-row">
    <a href="index.html" class="brand" aria-label="Devavo home">
      <span class="wordmark" aria-hidden="true"><img src="images/logo/devavo-logo-160.png" alt="" width="160" height="103"><span class="name">evavo</span></span>
      <span class="sub">Own your reality</span></a>
    <nav class="primary" id="primaryNav" aria-label="Main">{links}<a href="contact.html" class="nav-cta"{" aria-current=\"page\"" if current == "contact.html" else ""}>Get a quote</a></nav>
    <button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false" aria-controls="primaryNav">{ICON["menu"]}</button>
  </div>
</header>"""

def footer():
    divs = "".join(f'<li><a href="{d["slug"]}.html">{e(d["name"])}</a></li>' for d in DIVISIONS)
    hours = "".join(f"<li>{e(a)}: {e(b)}</li>" for a, b in HOURS)
    return f"""<footer class="site"><div class="container">
  <div class="cols">
    <div><img class="footer-logo" src="images/logo/devavo-logo-160.png" alt="Devavo" width="160" height="103" loading="lazy"><p class="footer-tag">Own your reality</p><p>Devavo Trading Enterprise CC. Aluminium and glass, automation, construction and balustrades, from our workshop in North End, Gqeberha. Established 2010.</p></div>
    <div><h4>Divisions</h4><ul>{divs}<li><a href="projects.html">Projects</a></li></ul></div>
    <div><h4>Contact</h4><ul><li><a href="tel:{PHONE_INTL}">{PHONE}</a></li><li><a href="{wa_link()}" target="_blank" rel="noopener">WhatsApp {PHONE}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{e(ADDRESS[0])}, {e(ADDRESS[1])}</li></ul></div>
    <div><h4>Hours</h4><ul>{hours}<li>After hours: call or WhatsApp, we will get back to you</li><li><a href="{WA_CATALOGUE}" target="_blank" rel="noopener">WhatsApp catalogue</a></li>
      <li><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
  </div>
  <div class="legal"><span>© <span id="year">2026</span> Devavo Trading Enterprise CC · Reg. 2010/087431/23</span><span><a href="privacy.html">Privacy &amp; cookies</a> · Gqeberha, Eastern Cape</span></div>
</div></footer>
<nav class="action-bar" aria-label="Quick contact">
  <a href="tel:{PHONE_INTL}">{ICON["phone"]}Call</a>
  <a class="wa" href="{wa_link()}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp</a>
  <a class="q" href="contact.html">{ICON["quote"]}Free quote</a>
</nav>
<a class="wa-float" href="{wa_link()}" target="_blank" rel="noopener" aria-label="Get a quote on WhatsApp">{ICON["wa"]}<span>Quote on WhatsApp</span></a>
{consent_banner()}
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
  <img alt=""><p class="cap"></p>
  <button class="x" aria-label="Close">×</button><button class="prev" aria-label="Previous photo">‹</button><button class="next" aria-label="Next photo">›</button>
</div>
<script src="assets/site.js?v={asset_version('site.js')}" defer></script>"""

def business_ld():
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness",
        "name": "Devavo", "legalName": "Devavo Trading Enterprise CC", "foundingDate": "2010",
        "description": "Aluminium and glass, garage doors and gate automation, construction and renovations, and balustrades in Gqeberha and the Eastern Cape.",
        "email": EMAIL, "telephone": PHONE_INTL,
        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS[0], "addressLocality": ADDRESS[1],
                    "addressRegion": "Eastern Cape", "postalCode": ADDRESS[2], "addressCountry": "ZA"},
        "areaServed": "Eastern Cape, South Africa",
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "16:00"}],
        "sameAs": [FACEBOOK, WA_CATALOGUE],
        "logo": url("images/logo/devavo-logo.png"), "image": url("images/logo/devavo-logo.png"),
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
            {"@type": "OfferCatalog", "name": d["name"], "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[0]}} for s in d["services"]]}
            for d in DIVISIONS]},
    }

def page(filename, title, meta, body, current, ld=None, og_img="ag-shopfront-sanparks"):
    lds = [business_ld()] + ([ld] if ld else [])
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    doc = f"""<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(meta)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(meta)}">
<meta property="og:image" content="{url('images/work/' + og_img + '.webp')}">
<meta name="theme-color" content="#ec1a23">
<link rel="icon" type="image/png" sizes="32x32" href="images/logo/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="images/logo/icon-192.png">
<link rel="apple-touch-icon" href="images/logo/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Arimo:wght@400;700&family=Tinos:wght@400;700&family=Work+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={asset_version('site.css')}">
{tracking_config()}
{ld_html}
</head>
<body>
{header(current)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
"""
    open(os.path.join(ROOT, filename), "w", encoding="utf-8", newline="\n").write(doc)

def quote_section(division=None, heading="Tell us what you need built"):
    opts = "".join(f'<option{" selected" if division == d["name"] else ""}>{e(d["name"])}</option>' for d in DIVISIONS)
    hours = "<br>".join(f"{e(a)}: {e(b)}" for a, b in HOURS)
    return f"""<section class="dark" id="quote"><div class="container quote-wrap">
  <div class="quote-info">
    <span class="eyebrow">Free quote</span>
    <h2>{e(heading)}</h2>
    <p>Send a few details and photos of the job on WhatsApp, or fill in the form, and we will come back to you with a quote. Site visits are arranged by appointment.</p>
    <ul class="contact-list">
      <li>{ICON["phone"]}<div><small>Call or WhatsApp, any time</small><a href="tel:{PHONE_INTL}">{PHONE}</a><span class="after-hours">Outside trading hours? Still call or WhatsApp. If we can’t pick up, we’ll get back to you.</span></div></li>
      <li>{ICON["wa"]}<div><small>Catalogue</small><a href="{WA_CATALOGUE}" target="_blank" rel="noopener">Browse our products on WhatsApp</a></div></li>
      <li>{ICON["mail"]}<div><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
      <li>{ICON["pin"]}<div><small>Workshop</small>{e(ADDRESS[0])}, {e(ADDRESS[1])}, {e(ADDRESS[2])}</div></li>
      <li>{ICON["clock"]}<div><small>Trading hours</small>{hours}<span class="open-status on-dark" data-open-status><i></i><span></span></span></div></li>
    </ul>
  </div>
  <form class="quote" name="quote" method="POST" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="quote">
    <p hidden><label>Leave this empty: <input name="bot-field"></label></p>
    <div class="form-row">
      <div class="field"><label for="q-name">Full name</label><input id="q-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="q-phone">Phone</label><input id="q-phone" name="phone" type="tel" autocomplete="tel" placeholder="e.g. 082 000 0000" required></div>
    </div>
    <div class="form-row">
      <div class="field"><label for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email"></div>
      <div class="field"><label for="q-area">Suburb or town</label><input id="q-area" name="area" placeholder="e.g. Walmer, Kariega"></div>
    </div>
    <div class="form-row">
      <div class="field full"><label for="q-division">What do you need?</label>
        <select id="q-division" name="division">{opts}<option>Not sure / more than one</option></select></div>
    </div>
    <div class="form-row">
      <div class="field full"><label for="q-msg">Project details</label><textarea id="q-msg" name="message" placeholder="What needs doing, rough sizes, and when you would like it done."></textarea></div>
    </div>
    <button type="submit" class="btn btn-primary">Send quote request</button>
    <p class="form-note">Prefer WhatsApp? <a href="{wa_link()}" target="_blank" rel="noopener">Message us on {PHONE}</a> and attach photos of the opening or site.</p>
    <div class="form-success" role="status" aria-live="polite"></div>
  </form>
</div></section>"""

def gallery(photos, filters=True, limit=None, show_division=False):
    cats = []
    for p in photos:
        c = DIV_BY_KEY[p["division"]]["name"] if show_division else p["sub"]
        if c not in cats:
            cats.append(c)
    figs = []
    for p in photos[:limit] if limit else photos:
        c = DIV_BY_KEY[p["division"]]["name"] if show_division else p["sub"]
        figs.append(f'<figure data-cat="{e(c)}">{img(p["slug"], thumb=True)}<figcaption>{e(p["desc"])}</figcaption></figure>')
    btns = ""
    if filters and len(cats) > 1:
        btns = '<div class="filters" role="group" aria-label="Filter photos"><button type="button" data-filter="all" aria-pressed="true">All</button>' + \
               "".join(f'<button type="button" data-filter="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in cats) + "</div>"
    return f'<div data-gallery>{btns}<div class="gallery">{"".join(figs)}</div></div>'

def catalogue_band(division=None):
    what = f"{division.lower()} designs" if division else "door, window, gate and garage door designs"
    return f"""<section class="catalogue"><div class="container cat-row">
  <div class="cat-copy"><span class="eyebrow">WhatsApp catalogue</span>
    <h2>Browse our {e(what)}</h2>
    <p>Our WhatsApp catalogue on {PHONE} shows our designs and finishes. Pick one you like, send it to us in the same chat, and we will quote it to your size.</p></div>
  <div class="cat-actions">
    <a class="btn btn-wa" href="{WA_CATALOGUE}" target="_blank" rel="noopener">{ICON["catalogue"]}Open the catalogue</a>
    <a class="btn btn-outline" href="{wa_link()}" target="_blank" rel="noopener">{ICON["wa"]}Chat on {PHONE}</a>
  </div>
</div></section>"""

def process():
    steps = [("Enquiry", "Call, WhatsApp or send the form with a few details and photos."),
             ("Site measure", "We visit, measure every opening or area, and talk through options."),
             ("Quote", "A written quote with materials, finishes and a programme."),
             ("Build", "Frames, gates and doors made in our workshop; building work on site."),
             ("Install & handover", "Our own team fits, tests and walks you through the finished job.")]
    s = "".join(f'<div class="step"><span class="n">0{i+1}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(steps))
    return f"""<section><div class="container">
  <div class="section-head"><span class="eyebrow">How it works</span><h2>From first call to handover</h2></div>
  <div class="steps">{s}</div>
</div></section>"""

def track_rows(filter_slug=None):
    rows = [r for r in TRACK_RECORD if not filter_slug or r[3] == filter_slug]
    div_name = {d["slug"]: d["name"] for d in DIVISIONS}
    return "".join(
        f'<div class="proj"><div class="body"><span class="meta">{e(y)} · {e(div_name[s])}</span><h3>{e(c)}</h3><p>{e(t)}</p></div></div>'
        for y, c, t, s in rows)

# ----------------------------------------------------------------- pages
def build_home():
    mosaic = "".join(
        f'<a href="{d["slug"]}.html">{img(d["card"], d["name"], eager=i < 2, thumb=True)}<span>{e(d["name"])}</span></a>'
        for i, d in enumerate(DIVISIONS))
    cards = "".join(f"""<a class="div-card" href="{d['slug']}.html">{img(d['hero'], '', thumb=True)}
  <div class="body"><span class="num">{d['num']}</span><h3>{e(d['name'])}</h3><p>{e(d['card_text'])}</p>
  <ul>{''.join(f'<li>{e(t)}</li>' for t in d['tags'])}</ul><span class="more">Explore {e(d['name'])} →</span></div></a>""" for d in DIVISIONS)
    why = [("2010", "Established", "Started in aluminium in a single garage; now a full manufacturing workshop in North End."),
           ("4", "Divisions, one contractor", "Aluminium, automation, building and balustrades, so one team handles the whole job."),
           ("CIDB", "Registered contractor", "Registered with the Construction Industry Development Board and on public-sector supplier databases."),
           ("EC", "Eastern Cape-wide", "From homes in Gqeberha to public buildings in Graaff-Reinet, Makhanda and Tsitsikamma.")]
    why_html = "".join(f'<div class="why"><span class="n">{e(n)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for n, t, d in why)
    featured = [p for p in PHOTOS if p["slug"] in (
        "ag-shopfront-sanparks", "au-garage-full-view-glass", "bs-glass-stair-handrail", "co-interior-curved-bulkhead",
        "ag-door-double-entrance-slats", "au-gate-boundary-infill", "ag-shopfront-absa", "co-carport-roofing",
        "ag-bifold-pergola", "au-gate-slatted-pair", "ag-door-sunburst-pivot-black", "bs-glass-balcony")]
    clients = "".join(f"<span>{e(c)}</span>" for c in CLIENTS)
    body = f"""<section class="home-hero"><div class="container grid">
  <div>
    <span class="eyebrow">Gqeberha · Eastern Cape · Since 2010</span>
    <h1>Aluminium, automation and building, from one team</h1>
    <p class="sub">Devavo makes doors, windows, shopfronts, garage doors and gates in our own workshop, automates them, and builds and renovates the spaces they go into. One contractor, one point of contact, one standard.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="contact.html">{ICON["quote"]}Get a free quote</a>
      <a class="btn btn-wa" href="{wa_link()}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp us</a>
      <a class="btn btn-ghost" href="{WA_CATALOGUE}" target="_blank" rel="noopener">{ICON["catalogue"]}View catalogue</a>
    </div>
    <div class="hero-facts"><span><b>Own workshop</b> in North End</span><span><b>CIDB</b> registered</span><span><b>Public &amp; private</b> clients</span></div>
  </div>
  <div class="mosaic">{mosaic}</div>
</div></section>

<section><div class="container">
  <div class="section-head"><span class="eyebrow">What we do</span><h2>Four divisions, one contractor</h2>
    <p class="lede">Choose the work you need. Each division has its own specialists, and they share one workshop and one site team, so jobs that cross trades don't fall between contractors.</p></div>
  <div class="div-grid">{cards}</div>
</div></section>

{catalogue_band()}

<section class="dark"><div class="container">
  <div class="section-head"><span class="eyebrow">Why Devavo</span><h2>Built in-house, answered for in-house</h2></div>
  <div class="why-grid">{why_html}</div>
</div></section>

<section><div class="container">
  <div class="section-head row"><div><span class="eyebrow">Recent work</span><h2>From the workshop and the site</h2></div>
    <a class="btn btn-outline" href="projects.html">See all projects</a></div>
  {gallery(featured, filters=False)}
</div></section>

<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Track record</span><h2>Trusted by contractors, government and property owners</h2>
    <p class="lede">A selection of clients we have worked for, directly or as a subcontractor.</p></div>
  <div class="clients">{clients}</div>
  <blockquote class="ref"><p>“{e(REFERENCE[0])}”</p><cite>{e(REFERENCE[1])}</cite></blockquote>
</div></section>

{process()}

<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Where we work</span><h2>Gqeberha and the Eastern Cape</h2></div>
  <div class="areas">{''.join(f'<span><b>·</b> {e(a)}</span>' for a in AREAS)}</div>
</div></section>

{quote_section()}"""
    page("index.html", "Devavo | Aluminium & Glass, Garage Doors & Gates, Construction | Gqeberha",
         "Devavo makes aluminium doors, windows and shopfronts, garage doors and automated gates, glass balustrades, and does building and renovations in Gqeberha and the Eastern Cape. Est. 2010.",
         body, "index.html")

def build_division(d):
    photos = [p for p in PHOTOS if p["division"] == d["key"]]
    if d["slug"] == "balustrades-security":
        photos += [p for p in PHOTOS if p["division"] == "05 Custom Fabrication"]
    svcs = "".join(f'<div class="svc"><span class="n">{d["num"]}.{i+1}</span><h3>{e(t)}</h3><p>{e(x)}</p></div>'
                   for i, (t, x) in enumerate(d["services"]))
    vids = ""
    if d["videos"]:
        cards = "".join(f"""<div class="video-card"><video src="images/video/{v}.mp4" poster="images/video/{v}.jpg" controls controlslist="nodownload noplaybackrate" disablepictureinpicture muted playsinline preload="none"></video><p>{e(c)}</p></div>"""
                        for v, c in d["videos"])
        vids = f"""<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">On video</span><h2>See it working</h2></div>
  <div class="video-row{' two' if len(d['videos']) == 1 else ''}">{cards}</div></div></section>"""
    track = track_rows(d["slug"])
    track_html = f"""<section><div class="container">
  <div class="section-head"><span class="eyebrow">Selected projects</span><h2>Recent {e(d['name'].lower())} work</h2></div>
  <div class="proj-grid">{track}</div></div></section>""" if track else ""
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faqs"])
    others = "".join(f'<a class="btn btn-outline" href="{o["slug"]}.html">{e(o["name"])}</a>' for o in DIVISIONS if o is not d)
    body = f"""<section class="page-hero">{img(d['hero'], '', eager=True)}<div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / {e(d['name'])}</p>
  <span class="eyebrow">Division {d['num']} · {e(d['name'])}</span>
  <h1>{e(d['h1'])}</h1><p>{e(d['lead'])}</p>
  <div class="hero-ctas"><a class="btn btn-primary" href="#quote">{ICON["quote"]}Get a quote</a>
    <a class="btn btn-wa" href="{wa_link('Hi Devavo, I would like a quote for ' + d['name'].lower() + ': ')}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp us</a>
    <a class="btn btn-ghost" href="{WA_CATALOGUE}" target="_blank" rel="noopener">{ICON["catalogue"]}View catalogue</a></div>
</div></section>

<section><div class="container">
  <div class="section-head"><span class="eyebrow">Services</span><h2>What our {e(d['name'].lower())} team does</h2></div>
  <div class="svc-grid">{svcs}</div>
</div></section>

<section class="alt"><div class="container split">
  {img(d['why_img'])}
  <div class="copy"><span class="eyebrow">Why Devavo</span><h2>{e(d['why_title'])}</h2><p>{e(d['why_text'])}</p>
    <ul class="ticks">{''.join(f'<li>{e(x)}</li>' for x in d['why_points'])}</ul></div>
</div></section>

<section><div class="container">
  <div class="section-head"><span class="eyebrow">Gallery</span><h2>{e(d['name'])} by Devavo</h2>
    <p class="lede">Photos from our own jobs. Tap any photo to view it larger.</p></div>
  {gallery(photos)}
</div></section>

{catalogue_band(d['name']) if d['slug'] in ('aluminium-glass','automation','balustrades-security') else ''}
{vids}
{track_html}

<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Questions</span><h2>Frequently asked</h2></div>
  <div class="faq">{faqs}</div>
</div></section>

{quote_section(d['name'], 'Get a quote for ' + d['name'].lower())}

<section><div class="container">
  <div class="section-head"><span class="eyebrow">Also from Devavo</span><h2>Our other divisions</h2></div>
  <div class="hero-ctas">{others}</div>
</div></section>"""
    ld = {"@context": "https://schema.org", "@type": "Service", "name": d["name"], "serviceType": d["name"],
          "provider": {"@type": "HomeAndConstructionBusiness", "name": "Devavo"}, "areaServed": "Eastern Cape, South Africa",
          "description": d["meta"]}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faqs"]]}
    page(d["slug"] + ".html", f"{d['title']} | Devavo", d["meta"], body, d["slug"] + ".html", ld, og_img=d["hero"])
    # FAQ structured data appended into the same page head
    path = os.path.join(ROOT, d["slug"] + ".html")
    s = open(path, encoding="utf-8").read().replace(
        "</head>", f'<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>\n</head>', 1)
    open(path, "w", encoding="utf-8", newline="\n").write(s)

def build_projects():
    photos = [p for p in PHOTOS if p["division"] != "06 Team & Company"]
    body = f"""<section class="page-hero">{img('ag-shopfront-absa-install', '', eager=True)}<div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Projects</p>
  <span class="eyebrow">Projects</span><h1>Our work across all four divisions</h1>
  <p>Photos from homes, shops, campuses and public buildings across the Eastern Cape, and a record of recent contracts.</p>
</div></section>

<section><div class="container">
  <div class="section-head"><span class="eyebrow">Gallery</span><h2>Browse by division</h2></div>
  {gallery(photos, show_division=True)}
</div></section>

<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Track record</span><h2>Recent contracts</h2>
    <p class="lede">Selected work for main contractors, government and institutions. References are available on request.</p></div>
  <div class="proj-grid">{track_rows()}</div>
  <blockquote class="ref"><p>“{e(REFERENCE[0])}”</p><cite>{e(REFERENCE[1])}</cite></blockquote>
</div></section>

{quote_section()}"""
    page("projects.html", "Projects & Track Record | Devavo, Gqeberha",
         "Photos and recent contracts from Devavo's aluminium and glass, automation, construction and balustrade divisions in Gqeberha and the Eastern Cape.",
         body, "projects.html", og_img="ag-shopfront-absa-install")

def build_contact():
    body = f"""<section class="page-hero">{img('tm-team-on-site', '', eager=True)}<div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Contact</p>
  <span class="eyebrow">Contact</span><h1>Get a free quote</h1>
  <p>Tell us about the job. The quickest way is WhatsApp with a few photos, but the form and phone work just as well.</p>
</div></section>
{quote_section(heading='Tell us what you need built')}
<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Where we work</span><h2>Gqeberha and the Eastern Cape</h2>
    <p class="lede">Our workshop is at {e(ADDRESS[0])}, {e(ADDRESS[1])}. Call ahead to arrange a visit.</p></div>
  <div class="areas">{''.join(f'<span><b>·</b> {e(a)}</span>' for a in AREAS)}</div>
</div></section>"""
    page("contact.html", "Contact & Free Quote | Devavo, Gqeberha",
         f"Get a free quote from Devavo for aluminium and glass, garage doors and gates, construction and renovations, or balustrades. Call {PHONE} or WhatsApp {PHONE}.",
         body, "contact.html", og_img="tm-team-on-site")

def build_privacy():
    tools = []
    if GA4_ID:
        tools.append("<li><b>Google Analytics</b> counts visits and shows which pages are viewed, so we know what is useful.</li>")
    if META_PIXEL_ID:
        tools.append("<li><b>Meta Pixel</b> (Facebook and Instagram) lets us show our adverts to people who have visited this site and measure whether those adverts work.</li>")
    tool_list = "<ul class=\"ticks\">" + "".join(tools) + "</ul>" if tools else "<p>We do not currently use any analytics or advertising cookies.</p>"
    body = f"""<section class="page-hero">{img('ag-shopfront-sanparks', '', eager=True)}<div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Privacy</p>
  <span class="eyebrow">Privacy &amp; cookies</span><h1>How we handle your information</h1>
</div></section>
<section><div class="container"><div class="faq" style="display:grid;gap:22px">
  <p>Devavo Trading Enterprise CC respects your privacy and processes personal information in line with the Protection of Personal Information Act (POPIA).</p>
  <h2 style="font-size:24px">Quote requests</h2>
  <p>When you send a quote request, we receive your name, phone number, email address, area and project details. We use these only to reply to you, quote and do the work. We do not sell or share them with anyone else. Form messages are delivered through our website host, Netlify.</p>
  <h2 style="font-size:24px">Cookies and visitor statistics</h2>
  <p>With your permission, this site uses the following. They only load if you choose <b>Accept</b> on the cookie notice:</p>
  {tool_list}
  <p>If you choose <b>Decline</b>, none of them load. You can change your choice at any time: <button type="button" class="btn btn-outline" data-consent-reset>Change cookie choice</button></p>
  <h2 style="font-size:24px">Photos and videos</h2>
  <p>All photos and videos on this site show Devavo's own work and are the property of Devavo Trading Enterprise CC. Please do not copy or reuse them without our written permission.</p>
  <h2 style="font-size:24px">Contact</h2>
  <p>To ask what information we hold about you, or to have it corrected or deleted, email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE}.</p>
</div></div></section>"""
    page("privacy.html", "Privacy & Cookies | Devavo", "How Devavo handles personal information, cookies and visitor statistics.",
         body, "privacy.html")

def build_extras():
    pages = ["index.html", "aluminium-glass.html", "automation.html", "construction.html",
             "balustrades-security.html", "projects.html", "contact.html", "privacy.html"]
    if SITE_URL:
        urls = "".join(f"<url><loc>{SITE_URL}/{'' if p == 'index.html' else p}</loc></url>" for p in pages)
        open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
            f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    robots = "User-agent: *\nAllow: /\nDisallow: /_build/\n" + (f"Sitemap: {SITE_URL}/sitemap.xml\n" if SITE_URL else "")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(robots)

build_home()
for d in DIVISIONS:
    build_division(d)
build_projects()
build_contact()
build_privacy()
build_extras()
print("built", "(demo)" if DEMO else "")
