# -*- coding: utf-8 -*-
import re
from build_common import page, breadcrumb, write, WHATSAPP_LINK, whatsapp_link, ARTICLES, EXTRA_ARTICLES, VIRAL_ARTICLES, CATEGORIES, DESTINATIONS, TOURS
from data_articles import ARTICLE_BODIES
from data_article_links import ARTICLE_LINKS
from icons import icon, scene_svg, ARTICLE_SCENES, DEST_SCENES, TOUR_SCENES

DEST_BY_SLUG = {d["slug"]: d for d in DESTINATIONS}
TOUR_BY_SLUG = {t["slug"]: t for t in TOURS}
ALL_CORE_ARTICLES = ARTICLES + EXTRA_ARTICLES
ALL_ARTICLES = ALL_CORE_ARTICLES + VIRAL_ARTICLES
ARTICLES_BY_SLUG = {a["slug"]: a for a in ALL_ARTICLES}


def category_slug(cat):
    return cat.lower().replace(" & ", "-").replace(" / ", "-").replace(" ", "-")


def slugify_heading(h):
    return re.sub(r"[^a-z0-9-]", "", re.sub(r"\s+", "-", h.lower()))


def render_toc(sections):
    items = "".join(f'<li><a href="#{slugify_heading(h)}">{h}</a></li>' for h, _ in sections)
    return f'<div class="toc-box"><h4>{icon("compass")} In This Guide</h4><ol>{items}</ol></div>'


def render_sections(sections):
    out = []
    for heading, paras in sections:
        out.append(f'<h2 id="{slugify_heading(heading)}">{heading}</h2>')
        for p in paras:
            out.append(f'<p>{p}</p>')
    return "".join(out)


def render_quick_info(slug, a):
    links = ARTICLE_LINKS.get(slug, {})
    dest_names = ", ".join(DEST_BY_SLUG[d]["name"] for d in links.get("dest", []) if d in DEST_BY_SLUG)
    return f'''<div class="quick-info-box">
      <h4>{icon('compass')} Quick Info</h4>
      <ul>
        <li><b>Category</b> {a['cat']}</li>
        <li><b>Read time</b> {a['read']}</li>
        <li><b>Covers</b> {dest_names or "Zimbabwe-wide"}</li>
      </ul>
    </div>'''


def render_related_pills(slugs, lookup, base_path, label):
    pills = "".join(
        f'<a href="{base_path}{s}.html" class="related-pill">{icon("arrow")} {lookup[s]["name"] if "name" in lookup.get(s, {}) else lookup[s].get("title", s)}</a>'
        for s in slugs if s in lookup
    )
    return f'<div style="margin-bottom:18px;"><span class="eyebrow">{label}</span><div class="related-pills">{pills}</div></div>'


def render_article_cta(article_title):
    wa = whatsapp_link(f"Hi Knowledge, I read your guide on {article_title} and I'd like help planning my trip")
    return f'''<div class="article-cta-block">
      <h4>Need help planning this Zimbabwe trip?</h4>
      <p>Contact Knowledge for a private tour or custom itinerary built around what you just read.</p>
      <div class="cta-row">
        <a href="../contact.html" class="btn btn-primary">Start Planning</a>
        <a href="{wa}" class="btn btn-whatsapp">{icon('whatsapp')} Chat on WhatsApp</a>
      </div>
    </div>'''


def faq_jsonld(items):
    import json
    data = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


ARTICLE_FAQS = {
    "best-time-to-visit-zimbabwe": [
        ("What's the single best month to visit?", "September is often cited as the best all-round month — dry-season wildlife viewing is excellent and Victoria Falls still has reasonable flow before its lowest point in late season."),
        ("Is the rainy season worth avoiding entirely?", "No — it's simply a different trip, with lush scenery, fuller Falls, and lower prices, trading some wildlife predictability for those benefits."),
    ],
    "is-zimbabwe-safe-to-visit": [
        ("Do I need to worry about political instability as a tourist?", "Tourist areas operate normally day to day regardless of national political news cycles — we'll flag anything genuinely relevant to your specific travel dates if it arises."),
    ],
    "zimbabwe-trip-cost-breakdown": [
        ("Is Zimbabwe cheaper or more expensive than Zambia/Botswana for safari?", "Roughly comparable at equivalent accommodation tiers, though Zimbabwe's Hwange often offers better value than Botswana's more famous (and pricier) reserves at a similar standard."),
    ],
    "5-day-zimbabwe-itinerary": [
        ("Can this itinerary work in reverse (Hwange first)?", "Yes — flight and logistics work equally well either direction; it comes down to whether you'd rather start or end with the Falls."),
    ],
    "victoria-falls-vs-hwange": [
        ("Can I do both in under 5 days if I really try?", "It's possible but tight — expect to feel rushed at one or both. We can build a compressed version if your dates are genuinely fixed."),
    ],
}


def build_article_page(a, links):
    slug = a['slug']
    canonical = f"/travel-guide/{slug}.html"
    content = ARTICLE_BODIES[slug]
    palette, motif = ARTICLE_SCENES.get(slug, ("green", "hills"))
    hero_art = scene_svg(palette, motif)

    jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{a['title']}","articleSection":"{a['cat']}","author":{{"@type":"Organization","name":"Zimbabwe Tour Guide"}}}}
</script>'''
    extra_faq_jsonld = ""
    faq_block = ""
    if slug in ARTICLE_FAQS:
        faq_items = ARTICLE_FAQS[slug]
        extra_faq_jsonld = faq_jsonld(faq_items)
        rows = "".join(
            f'''<div class="faq-item{' open' if i==0 else ''}"><button class="faq-q" aria-expanded="{'true' if i==0 else 'false'}">{q} {icon('plus')}</button><div class="faq-a"><div class="faq-a-inner">{ans}</div></div></div>'''
            for i, (q, ans) in enumerate(faq_items)
        )
        faq_block = f'''<h2 id="faq">FAQ</h2><div class="faq-list" data-exclusive="false">{rows}</div>'''

    dest_pills = render_related_pills(links['dest'], DEST_BY_SLUG, "../destinations/", "Related destinations")
    tour_pills = render_related_pills(links['tours'], TOUR_BY_SLUG, "../tours/", "Related tours")
    related_pills = render_related_pills(links['related'], ARTICLES_BY_SLUG, "", "Related guides")

    body = f'''
{breadcrumb([("Home","index.html"),("Travel Guide","travel-guide/index.html"),(a['title'], None)], canonical)}

<section class="page-hero" style="padding-bottom:48px;">
  <div class="hero-art" style="position:absolute;bottom:0;left:0;width:100%;z-index:1;opacity:0.4;">{hero_art}</div>
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">{a['cat']}</span>
    <h1>{a['title']}</h1>
    <div class="page-hero-meta">
      <span class="pill">{icon('clock')} {a['read']}</span>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap-narrow legal-content">
    <p style="font-size:17px;color:var(--ink);font-weight:500;">{content['intro']}</p>

    {render_quick_info(slug, a)}
    {render_toc(content['sections'])}

    {render_sections(content['sections'])}
    {faq_block}

    <div class="guide-quote" style="margin-top:32px;">{content['closer']}</div>

    {render_article_cta(a['title'])}

    <div class="divider"></div>
    {dest_pills}
    {tour_pills}
    {related_pills}
  </div>
</section>
'''
    html = page(
        title=f"{a['title']} | Zimbabwe Tour Guide",
        description=content['intro'][:155],
        canonical_path=canonical,
        body=body,
        extra_jsonld=jsonld + extra_faq_jsonld,
        keywords=f"{a['cat']}, Zimbabwe travel guide, {a['title']}",
    )
    write(f"travel-guide/{slug}.html", html)


def article_card(a, viral=False):
    slug = a['slug']
    intro = ARTICLE_BODIES[slug]['intro']
    if viral:
        palette, motif = ARTICLE_SCENES.get(slug, ("gold", "hills"))
        svg = scene_svg(palette, motif)
        return f'''<a href="{slug}.html" class="viral-card reveal" data-category="{category_slug(a['cat'])}">
      <div class="viral-media">{svg}<span class="viral-share-tag">{icon('arrow')} Shareable</span>
        <div class="viral-title-overlay"><h4>{a['title']}</h4></div>
      </div>
      <div class="viral-card-body"><p>{intro[:90]}&hellip;</p></div>
    </a>'''
    palette, motif = ARTICLE_SCENES.get(slug, ("green", "hills"))
    svg = scene_svg(palette, motif)
    return f'''<a href="{slug}.html" class="article-card reveal" data-category="{category_slug(a['cat'])}">
      <div class="article-media">{svg}<span class="article-cat">{a['cat']}</span></div>
      <div class="article-body">
        <h3>{a['title']}</h3>
        <p>{intro[:100]}&hellip;</p>
        <div class="article-meta">{icon('clock')} {a['read']}</div>
      </div>
    </a>'''


def build_travel_guide_hub():
    canonical = "/travel-guide/index.html"

    featured = next(a for a in ALL_CORE_ARTICLES if a['slug'] == "best-time-to-visit-zimbabwe")
    f_palette, f_motif = ARTICLE_SCENES.get(featured['slug'], ("green", "hills"))
    featured_svg = scene_svg(f_palette, f_motif)
    featured_intro = ARTICLE_BODIES[featured['slug']]['intro']

    by_cat = {}
    for a in ALL_CORE_ARTICLES:
        by_cat.setdefault(a['cat'], []).append(a)

    def section_for(cat):
        items = by_cat.get(cat, [])[:3]
        cards = "".join(article_card(a) for a in items)
        return f'''<div style="margin-bottom:56px;">
      <div class="guide-section-row">
        <h3>{cat}</h3>
        <a href="#all-guides">View all {icon('arrow')}</a>
      </div>
      <div class="guide-row-scroll">{cards}</div>
    </div>'''

    popular_slugs = ["best-time-to-visit-zimbabwe", "is-zimbabwe-safe-to-visit", "zimbabwe-trip-cost-breakdown", "5-day-zimbabwe-itinerary", "hwange-national-park-safari-guide"]
    popular_items = "".join(
        f'''<a href="{s}.html" class="popular-item reveal"><span class="popular-rank">{i+1:02d}</span><div class="popular-item-body"><h4>{ARTICLES_BY_SLUG[s]['title']}</h4><span>{ARTICLES_BY_SLUG[s]['cat']} &middot; {ARTICLES_BY_SLUG[s]['read']}</span></div></a>'''
        for i, s in enumerate(popular_slugs)
    )

    viral_cards = "".join(article_card(a, viral=True) for a in VIRAL_ARTICLES)

    pills = ['<button class="category-pill active" data-cat="all" onclick="filterArticles(\'all\', this)">All Guides</button>']
    for cat in CATEGORIES:
        pills.append(f'<button class="category-pill" data-cat="{category_slug(cat)}" onclick="filterArticles(\'{category_slug(cat)}\', this)">{cat}</button>')

    all_cards = "".join(article_card(a) for a in ALL_CORE_ARTICLES)

    body = f'''
{breadcrumb([("Home","index.html"),("Travel Guide", None)], canonical)}

<section class="page-hero">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">A real Zimbabwe travel resource</span>
    <h1>Zimbabwe Travel Guide</h1>
    <p>Trip planning advice, destination breakdowns, safari comparisons, honest cost guides, and the kind of practical detail that only comes from actually guiding here — plus the views and stories that make people fall for this country in the first place.</p>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="featured-article reveal">
      <div class="featured-media">{featured_svg}<span class="featured-badge">Featured Guide</span></div>
      <div class="featured-body">
        <span class="eyebrow">{featured['cat']}</span>
        <h2>{featured['title']}</h2>
        <p>{featured_intro[:180]}&hellip;</p>
        <a href="{featured['slug']}.html" class="btn btn-primary" style="width:fit-content;">Read the Full Guide</a>
      </div>
    </div>
  </div>
</section>

<section class="bg-cream tight">
  <div class="wrap">
    <div class="guide-section-row"><h3>{icon('star-shield')} Most Popular Guides</h3></div>
    <div class="popular-list">
      {popular_items}
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    {section_for("Trip Planning")}
    {section_for("Destination Guides")}
    {section_for("Safari Guides")}
    {section_for("Costs & Budget")}
    {section_for("Itineraries")}
    {section_for("Safety & Practical Tips")}
  </div>
</section>

<section class="bg-green">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow on-dark">Image-led, shareable, still genuinely useful</span>
      <h2 class="section-title">Featured Travel Stories &amp; Inspiration</h2>
      <p class="section-sub">The Zimbabwe scenes worth sharing — pin them, send them, or just use them to convince whoever you're traveling with.</p>
    </div>
    <div class="card-grid">
      {viral_cards}
    </div>
  </div>
</section>

<section class="bg-cream" id="all-guides">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Browse everything</span>
      <h2 class="section-title">All Travel Guides</h2>
    </div>
    <div class="category-pills">
      {"".join(pills)}
    </div>
    <div class="article-grid">
      {all_cards}
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Found what you needed? Let's plan the actual trip.</h2>
    <p>Every guide here connects to a real itinerary we can build for you.</p>
    <div class="cta-actions">
      <a href="../contact.html" class="btn btn-primary">Start Planning My Trip</a>
      <a href="../tours/index.html" class="btn btn-outline">Browse Tours</a>
    </div>
  </div>
</section>
'''
    html = page(
        title="Zimbabwe Travel Guide | Trip Planning, Safari & Practical Tips",
        description="A real Zimbabwe travel resource covering trip planning, destination comparisons, safari advice, costs and budgeting, sample itineraries, safety tips, and travel inspiration.",
        canonical_path=canonical,
        body=body,
        keywords="Zimbabwe travel guide, Zimbabwe trip planning, Zimbabwe blog, Zimbabwe travel tips, Zimbabwe travel magazine",
    )
    write("travel-guide/index.html", html)


if __name__ == "__main__":
    build_travel_guide_hub()
    for a in ALL_ARTICLES:
        links = ARTICLE_LINKS[a['slug']]
        build_article_page(a, links)


