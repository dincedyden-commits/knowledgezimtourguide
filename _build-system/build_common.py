"""
Zimbabwe Tour Guide — static site generator.
Generates every HTML page from shared layout components + structured content
so design and navigation stay consistent across the whole site.
"""
import os

ROOT = "/home/claude/ztg"

# ---------------------------------------------------------------------------
# SITE-WIDE NAVIGATION DATA (single source of truth for menus + internal links)
# ---------------------------------------------------------------------------

DESTINATIONS = [
    {"slug": "victoria-falls", "name": "Victoria Falls", "tag": "Icon & Adventure Hub"},
    {"slug": "hwange", "name": "Hwange National Park", "tag": "Big Game Safari"},
    {"slug": "great-zimbabwe", "name": "Great Zimbabwe", "tag": "Heritage & History"},
    {"slug": "nyanga", "name": "Nyanga", "tag": "Highlands & Hiking"},
    {"slug": "chimanimani", "name": "Chimanimani", "tag": "Mountains & Trekking"},
    {"slug": "harare", "name": "Harare", "tag": "Capital & Culture"},
]

TOURS = [
    {"slug": "victoria-falls-day-tour", "name": "Victoria Falls Day Tour", "duration": "1 Day", "type": "Day Trip"},
    {"slug": "hwange-safari-experience", "name": "Hwange Safari Experience", "duration": "4 Days", "type": "Safari"},
    {"slug": "great-zimbabwe-historical-tour", "name": "Great Zimbabwe Historical Tour", "duration": "2 Days", "type": "Heritage"},
    {"slug": "nyanga-highlands-escape", "name": "Nyanga Highlands Escape", "duration": "3 Days", "type": "Nature & Hiking"},
    {"slug": "chimanimani-adventure", "name": "Chimanimani Adventure", "duration": "4 Days", "type": "Trekking"},
    {"slug": "custom-zimbabwe-tour", "name": "Custom Zimbabwe Tour", "duration": "Flexible", "type": "Tailor-Made"},
]

ARTICLES = [
    # ---- PHASE 1 ----
    {"slug": "best-time-to-visit-zimbabwe", "title": "Best Time to Visit Zimbabwe: A Month-by-Month Guide", "cat": "Trip Planning", "read": "9 min read", "phase": 1},
    {"slug": "is-zimbabwe-safe-to-visit", "title": "Is Zimbabwe Safe for Tourists? An Honest Local Answer", "cat": "Safety & Practical Tips", "read": "8 min read", "phase": 1},
    {"slug": "zimbabwe-trip-cost-breakdown", "title": "How Much Does a Zimbabwe Trip Cost?", "cat": "Costs & Budget", "read": "8 min read", "phase": 1},
    {"slug": "zimbabwe-visa-entry-requirements", "title": "Zimbabwe Visa Guide for Tourists", "cat": "Safety & Practical Tips", "read": "6 min read", "phase": 1},
    {"slug": "zimbabwe-currency-guide", "title": "What Currency Should Tourists Use in Zimbabwe?", "cat": "Costs & Budget", "read": "6 min read", "phase": 1},
    {"slug": "what-to-pack-for-a-zimbabwe-safari", "title": "What to Pack for a Zimbabwe Safari or Victoria Falls Trip", "cat": "Trip Planning", "read": "7 min read", "phase": 1},
    {"slug": "victoria-falls-first-time-visitors-guide", "title": "Victoria Falls Travel Guide for First-Time Visitors", "cat": "Destination Guides", "read": "10 min read", "phase": 1},
    {"slug": "hwange-national-park-safari-guide", "title": "Hwange National Park Safari Guide", "cat": "Safari Guides", "read": "10 min read", "phase": 1},
    {"slug": "great-zimbabwe-ruins-travel-guide", "title": "Great Zimbabwe Ruins Travel Guide", "cat": "Destination Guides", "read": "9 min read", "phase": 1},
    {"slug": "5-day-zimbabwe-itinerary", "title": "5-Day Zimbabwe Itinerary for First-Time Visitors", "cat": "Itineraries", "read": "9 min read", "phase": 1},

    # ---- PHASE 2 ----
    {"slug": "nyanga-travel-guide", "title": "Nyanga Travel Guide", "cat": "Destination Guides", "read": "8 min read", "phase": 2},
    {"slug": "chimanimani-travel-guide", "title": "Chimanimani Travel Guide", "cat": "Destination Guides", "read": "8 min read", "phase": 2},
    {"slug": "harare-travel-guide", "title": "Harare Travel Guide", "cat": "Destination Guides", "read": "7 min read", "phase": 2},
    {"slug": "bulawayo-travel-guide", "title": "Bulawayo Travel Guide", "cat": "Destination Guides", "read": "7 min read", "phase": 2},
    {"slug": "harare-to-victoria-falls-travel", "title": "How to Travel from Harare to Victoria Falls", "cat": "Trip Planning", "read": "6 min read", "phase": 2},
    {"slug": "how-many-days-do-you-need-in-zimbabwe", "title": "How Many Days Do You Need in Zimbabwe?", "cat": "Trip Planning", "read": "7 min read", "phase": 2},

    # ---- PHASE 3 ----
    {"slug": "zimbabwe-safari-budget-guide", "title": "Zimbabwe Safari Budget Guide", "cat": "Costs & Budget", "read": "9 min read", "phase": 3},
    {"slug": "victoria-falls-vs-hwange", "title": "Victoria Falls vs Hwange: Which Should You Prioritize?", "cat": "Destination Guides", "read": "8 min read", "phase": 3},
    {"slug": "private-tour-vs-self-drive", "title": "Private Zimbabwe Tour vs Self-Drive: Which Is Right for You?", "cat": "Trip Planning", "read": "8 min read", "phase": 3},
    {"slug": "best-zimbabwe-destinations-for-couples", "title": "Best Zimbabwe Destinations for Couples and Honeymoons", "cat": "Travel Inspiration", "read": "7 min read", "phase": 3},
    {"slug": "family-friendly-places-in-zimbabwe", "title": "Best Family-Friendly Places to Visit in Zimbabwe", "cat": "Travel Inspiration", "read": "7 min read", "phase": 3},
    {"slug": "what-to-expect-on-a-zimbabwe-road-trip", "title": "What to Expect on a Zimbabwe Road Trip", "cat": "Safety & Practical Tips", "read": "8 min read", "phase": 3},

    # ---- PHASE 4 ----
    {"slug": "best-lodges-near-victoria-falls", "title": "Best Lodges Near Victoria Falls", "cat": "Destination Guides", "read": "8 min read", "phase": 4},
    {"slug": "best-safari-lodges-near-hwange", "title": "Best Safari Lodges Near Hwange", "cat": "Safari Guides", "read": "8 min read", "phase": 4},
    {"slug": "7-day-zimbabwe-itinerary", "title": "7-Day Zimbabwe Safari Itinerary", "cat": "Itineraries", "read": "11 min read", "phase": 4},
    {"slug": "3-day-victoria-falls-itinerary", "title": "3-Day Victoria Falls Itinerary", "cat": "Itineraries", "read": "7 min read", "phase": 4},
    {"slug": "things-to-do-in-victoria-falls-besides-the-falls", "title": "Best Things to Do in Victoria Falls Besides the Main Falls", "cat": "Destination Guides", "read": "8 min read", "phase": 4},
    {"slug": "how-to-plan-a-custom-zimbabwe-tour", "title": "How to Plan a Custom Zimbabwe Tour", "cat": "Trip Planning", "read": "7 min read", "phase": 4},
    {"slug": "zimbabwe-travel-mistakes-to-avoid", "title": "Zimbabwe Travel Mistakes to Avoid", "cat": "Safety & Practical Tips", "read": "9 min read", "phase": 4},
    {"slug": "visit-zimbabwe-without-a-tour-guide", "title": "Can You Visit Zimbabwe Without a Tour Guide?", "cat": "Trip Planning", "read": "7 min read", "phase": 4},
]

# ---------------------------------------------------------------------------
# VIRAL / SHAREABLE CONTENT LAYER — image-heavy, inspiration-led, still credible
# ---------------------------------------------------------------------------
VIRAL_ARTICLES = [
    {"slug": "beautiful-places-to-visit-in-zimbabwe", "title": "10 Beautiful Places to Visit in Zimbabwe", "cat": "Travel Inspiration", "read": "6 min read"},
    {"slug": "zimbabwe-views-that-dont-look-real", "title": "7 Zimbabwe Views That Don't Look Real", "cat": "Travel Inspiration", "read": "5 min read"},
    {"slug": "victoria-falls-high-water-season", "title": "Victoria Falls in High Water Season: What It Actually Looks Like", "cat": "Travel Inspiration", "read": "5 min read"},
    {"slug": "zimbabwe-road-trip-bucket-list", "title": "The Zimbabwe Road Trip Bucket List", "cat": "Travel Inspiration", "read": "7 min read"},
    {"slug": "hidden-gems-in-zimbabwe", "title": "5 Hidden Gems in Zimbabwe Most Tourists Miss", "cat": "Travel Inspiration", "read": "6 min read"},
    {"slug": "best-zimbabwe-honeymoon-spots", "title": "Best Zimbabwe Honeymoon Spots", "cat": "Travel Inspiration", "read": "6 min read"},
    {"slug": "most-underrated-places-in-zimbabwe", "title": "The Most Underrated Places to Visit in Zimbabwe", "cat": "Travel Inspiration", "read": "6 min read"},
    {"slug": "safari-vs-victoria-falls-which-to-prioritize", "title": "Zimbabwe Safari vs Victoria Falls: Which Should You Prioritize?", "cat": "Travel Inspiration", "read": "6 min read"},
    {"slug": "first-time-zimbabwe-traveler-mistakes", "title": "9 Mistakes First-Time Zimbabwe Travelers Make", "cat": "Travel Inspiration", "read": "7 min read"},
    {"slug": "photos-that-will-make-you-want-to-visit-zimbabwe", "title": "12 Photos That Will Make You Want to Visit Zimbabwe", "cat": "Travel Inspiration", "read": "5 min read"},
]

CATEGORIES = ["Trip Planning", "Destination Guides", "Safari Guides", "Costs & Budget", "Itineraries", "Safety & Practical Tips", "Travel Inspiration"]

# Two extra articles from the original 9, kept as bonus supporting content (not part of the official 30 or the 10 viral pieces)
EXTRA_ARTICLES = [
    {"slug": "victoria-falls-zambia-vs-zimbabwe-side", "title": "Victoria Falls: Zimbabwe Side or Zambia Side?", "cat": "Destination Guides", "read": "7 min read"},
    {"slug": "great-zimbabwe-history-explained", "title": "The History of Great Zimbabwe, Explained Simply", "cat": "Destination Guides", "read": "9 min read"},
    {"slug": "hwange-vs-mana-pools", "title": "Hwange vs. Mana Pools: Which Safari Fits You?", "cat": "Safari Guides", "read": "10 min read"},
]

WHATSAPP_NUMBER = "263770000000"


def whatsapp_link(message="Hi Knowledge, I'd like to plan a Zimbabwe trip"):
    """Build a wa.me link from a plain-text message, URL-encoding it properly."""
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


WHATSAPP_LINK = whatsapp_link()

LOGO_SVG = '''<svg class="logo-mark" viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="23" fill="#1F4D3A"/><path d="M6 30 Q 14 18, 24 24 T 42 18" stroke="#D4A017" stroke-width="2.2" fill="none" stroke-linecap="round"/><circle cx="33" cy="14" r="5.5" fill="#D4A017"/><path d="M6 36 L14 28 L20 33 L28 24 L34 29 L42 22" stroke="#F7F5F0" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

LOGO_SVG_FOOTER = '''<svg class="logo-mark" viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="23" fill="#2A6B4F"/><path d="M6 30 Q 14 18, 24 24 T 42 18" stroke="#D4A017" stroke-width="2.2" fill="none" stroke-linecap="round"/><circle cx="33" cy="14" r="5.5" fill="#D4A017"/></svg>'''


def rel(path_from_root):
    """No-op helper kept for clarity; all internal links are root-relative."""
    return path_from_root


def head(title, description, canonical_path, extra_jsonld="", keywords=""):
    kw = f'\n<meta name="keywords" content="{keywords}">' if keywords else ""
    return f'''<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">{kw}
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.zimbabwetourguide.com{canonical_path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.zimbabwetourguide.com{canonical_path}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
{extra_jsonld}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{path_prefix(canonical_path)}assets/style.css">'''


def path_prefix(canonical_path):
    """Return the relative prefix ('', '../') needed to reach /assets/ from a given page depth."""
    depth = canonical_path.strip("/").count("/")
    return "../" * depth if depth > 0 else ""


def nav_link(label, href, current_path):
    active = " active" if href == current_path else ""
    return f'<a href="{href}" class="{active.strip()}">{label}</a>' if active else f'<a href="{href}">{label}</a>'


def header_html(current_path=""):
    pre = path_prefix(current_path)
    dest_links = "\n".join(f'<a href="{pre}destinations/{d["slug"]}.html">{d["name"]}</a>' for d in DESTINATIONS)
    tour_links = "\n".join(f'<a href="{pre}tours/{t["slug"]}.html">{t["name"]}</a>' for t in TOURS)

    def is_active(href_suffix):
        return " active" if current_path.rstrip("/") == href_suffix.rstrip("/") else ""

    return f'''<div class="trust-bar">
  <div class="wrap">
    <span>🇿🇼 <strong>Locally owned &amp; operated</strong> — based in Victoria Falls, Zimbabwe</span>
  </div>
</div>
<header class="site-header">
  <div class="wrap nav">
    <a href="{pre}index.html" class="logo">
      {LOGO_SVG}
      <div>ZIMBABWE TOUR GUIDE<small>Private Tours &amp; Trip Planning</small></div>
    </a>
    <nav class="nav-links">
      <div class="nav-drop">
        <button type="button">Destinations <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M6 9l6 6 6-6"/></svg></button>
        <div class="nav-drop-panel">
          {dest_links}
        </div>
      </div>
      <div class="nav-drop">
        <button type="button">Tours <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M6 9l6 6 6-6"/></svg></button>
        <div class="nav-drop-panel">
          {tour_links}
        </div>
      </div>
      <a href="{pre}travel-guide/index.html"{is_active('/travel-guide/index.html')}>Travel Guide</a>
      <a href="{pre}about.html"{is_active('/about.html')}>About</a>
      <a href="{pre}gallery.html"{is_active('/gallery.html')}>Gallery</a>
      <a href="{pre}faq.html"{is_active('/faq.html')}>FAQ</a>
    </nav>
    <a href="{pre}contact.html" class="btn btn-ghost nav-cta">Plan My Trip</a>
    <button class="nav-burger" id="burgerBtn" aria-label="Open menu" aria-expanded="false"><span></span></button>
  </div>
</header>

<div class="mobile-menu" id="mobileMenu">
  <div class="mobile-menu-top">
    <span style="color:#fff;font-family:var(--serif);font-weight:700;font-size:18px;">Menu</span>
    <button class="mobile-menu-close" id="closeMenuBtn" aria-label="Close menu">✕</button>
  </div>
  <a href="{pre}index.html" class="mm-link">Home</a>
  <div class="mm-group-label">Destinations</div>
  <div class="mm-sub">
    {"".join(f'<a href="{pre}destinations/{d["slug"]}.html">{d["name"]}</a>' for d in DESTINATIONS)}
  </div>
  <div class="mm-group-label">Tours</div>
  <div class="mm-sub">
    {"".join(f'<a href="{pre}tours/{t["slug"]}.html">{t["name"]}</a>' for t in TOURS)}
  </div>
  <a href="{pre}travel-guide/index.html" class="mm-link">Travel Guide</a>
  <a href="{pre}about.html" class="mm-link">About</a>
  <a href="{pre}gallery.html" class="mm-link">Gallery</a>
  <a href="{pre}faq.html" class="mm-link">FAQ</a>
  <a href="{pre}contact.html" class="btn btn-primary btn-block">Plan My Trip</a>
</div>'''


def footer_html(current_path=""):
    pre = path_prefix(current_path)
    dest_links = "\n          ".join(f'<li><a href="{pre}destinations/{d["slug"]}.html">{d["name"]}</a></li>' for d in DESTINATIONS[:5])
    tour_links = "\n          ".join(f'<li><a href="{pre}tours/{t["slug"]}.html">{t["name"]}</a></li>' for t in TOURS[:5])
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="{pre}index.html" class="logo">{LOGO_SVG_FOOTER} ZIMBABWE TOUR GUIDE</a>
        <p>Private tours and local trip planning across Zimbabwe — run by licensed, Zimbabwe-based guides.</p>
        <div class="footer-social">
          <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg></a>
          <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
          <a href="{WHATSAPP_LINK}" aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Destinations</h5>
        <ul>
          {dest_links}
        </ul>
      </div>
      <div class="footer-col">
        <h5>Tours</h5>
        <ul>
          {tour_links}
        </ul>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <ul>
          <li><a href="{pre}about.html">About Knowledge</a></li>
          <li><a href="{pre}travel-guide/index.html">Travel Guide</a></li>
          <li><a href="{pre}gallery.html">Gallery</a></li>
          <li><a href="{pre}faq.html">FAQ</a></li>
          <li><a href="{pre}contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col footer-contact">
        <h5>Contact</h5>
        <ul>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg> Victoria Falls, Zimbabwe</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.13.96.36 1.9.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0122 16.92z"/></svg> +263 77 000 0000</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6l9 7 9-7M3 6v12h18V6"/></svg> hello@zimbabwetourguide.com</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Zimbabwe Tour Guide. All rights reserved.</span>
      <div class="footer-legal">
        <a href="{pre}legal/privacy-policy.html">Privacy Policy</a>
        <a href="{pre}legal/terms-and-conditions.html">Terms &amp; Conditions</a>
        <a href="{pre}legal/refund-cancellation-policy.html">Refund Policy</a>
        <a href="{pre}legal/disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </div>
</footer>

<div class="mobile-sticky-cta">
  <a href="{WHATSAPP_LINK}" class="btn btn-whatsapp">WhatsApp</a>
  <a href="{pre}contact.html" class="btn btn-primary">Plan My Trip</a>
</div>

<script src="{pre}assets/main.js"></script>'''


def page(title, description, canonical_path, body, extra_jsonld="", keywords=""):
    pre = path_prefix(canonical_path)
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
{head(title, description, canonical_path, extra_jsonld, keywords)}
</head>
<body>
{header_html(canonical_path)}
{body}
{footer_html(canonical_path)}
</body>
</html>'''


def breadcrumb(items, current_path):
    """items: list of (label, href) tuples; last item has no href."""
    pre = path_prefix(current_path)
    lis = []
    for i, (label, href) in enumerate(items):
        if href:
            full_href = href if href.startswith("http") else f"{pre}{href}"
            lis.append(f'<li><a href="{full_href}">{label}</a></li>')
        else:
            lis.append(f'<li>{label}</li>')
    return f'''<div class="breadcrumb"><div class="wrap"><ol>{"".join(lis)}</ol></div></div>'''


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"wrote {path} ({len(content)} bytes)")


