# -*- coding: utf-8 -*-
from build_common import page, breadcrumb, write, WHATSAPP_LINK, whatsapp_link, DESTINATIONS, TOURS, ARTICLES, EXTRA_ARTICLES
from data_destinations import DESTINATION_CONTENT
from icons import icon, scene_svg, DEST_SCENES, TOUR_SCENES, ARTICLE_SCENES

ARTICLES_BY_SLUG = {a["slug"]: a for a in ARTICLES + EXTRA_ARTICLES}
TOURS_BY_SLUG = {t["slug"]: t for t in TOURS}


def render_quick_facts(facts):
    items = "".join(
        f'<div class="qf-item">{icon(ic)}<div><b>{label}</b><span>{val}</span></div></div>'
        for ic, label, val in facts
    )
    return f'<div class="quick-facts">{items}</div>'


def render_why_visit(items):
    cards = "".join(
        f'''<div class="why-card reveal"><div class="why-icon">{icon("check")}</div><h4>{title}</h4><p>{body}</p></div>'''
        for title, body in items
    )
    return f'<div class="why-grid">{cards}</div>'


def render_things_to_do(items):
    rows = "".join(
        f'''<div class="numbered-item reveal"><div class="num">{i+1}</div><div><h4>{title}</h4><p>{body}</p></div></div>'''
        for i, (title, body) in enumerate(items)
    )
    return f'<div class="numbered-list">{rows}</div>'


def render_where_to_stay(items):
    cards = "".join(
        f'''<div class="why-card reveal"><div class="why-icon">{icon("map-pin")}</div><h4>{title}</h4><p>{body}</p></div>'''
        for title, body in items
    )
    return f'<div class="why-grid" style="grid-template-columns:1fr;">{"".join(f"""<div class=\"why-card reveal\"><div class=\"why-icon\">{icon("map-pin")}</div><h4>{t}</h4><p>{b}</p></div>""" for t, b in items)}</div>'.replace(
        'style="grid-template-columns:1fr;"', ''
    )


def render_what_to_pack(items):
    lis = "".join(f'<li>{icon("check")}{item}</li>' for item in items)
    return f'<div class="inc-box yes"><h4>{icon("check")} Packing checklist</h4><ul>{lis}</ul></div>'


def render_itinerary(days):
    rows = "".join(
        f'''<div class="itin-day reveal"><span class="day-label">{day}</span><h4>{title}</h4><p>{body}</p></div>'''
        for day, title, body in days
    )
    return f'<div class="itinerary">{rows}</div>'


def render_faq(items, exclusive="false"):
    rows = []
    for i, (q, a) in enumerate(items):
        open_cls = " open" if i == 0 else ""
        aria = "true" if i == 0 else "false"
        rows.append(f'''<div class="faq-item{open_cls}">
      <button class="faq-q" aria-expanded="{aria}">{q} {icon("plus")}</button>
      <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
    </div>''')
    return f'<div class="faq-list" data-exclusive="{exclusive}">{"".join(rows)}</div>'


def faq_jsonld(items):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


def render_related_tours(slugs):
    pills = "".join(
        f'<a href="../tours/{s}.html" class="related-pill">{icon("arrow")} {TOURS_BY_SLUG[s]["name"]}</a>'
        for s in slugs if s in TOURS_BY_SLUG
    )
    return pills


def render_related_articles(slugs):
    pills = "".join(
        f'<a href="../travel-guide/{s}.html" class="related-pill">{icon("arrow")} {ARTICLES_BY_SLUG[s]["title"]}</a>'
        for s in slugs if s in ARTICLES_BY_SLUG
    )
    return pills


def build_destination_page(slug, d):
    canonical = f"/destinations/{slug}.html"
    palette, motif = DEST_SCENES.get(slug, ("green", "hills"))
    hero_art = scene_svg(palette, motif)

    jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"TouristAttraction","name":"{d['name']}","description":"{d['intro'][:200].replace(chr(34), chr(39))}","address":{{"@type":"PostalAddress","addressRegion":"{d['region']}","addressCountry":"ZW"}}}}
</script>
{faq_jsonld(d['faq'])}'''

    body = f'''
{breadcrumb([("Home","index.html"),("Destinations","destinations/index.html"),(d['name'], None)], canonical)}

<section class="page-hero">
  <div class="hero-art" style="position:absolute;bottom:0;left:0;width:100%;z-index:1;opacity:0.5;">{hero_art}</div>
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">{d['hero_kicker']}</span>
    <h1>{d['h1']}</h1>
    <p>{d['intro']}</p>
    <div class="page-hero-actions">
      <a href="../contact.html" class="btn btn-primary">Plan a Trip to {d['name']}</a>
      <a href="{whatsapp_link(f"Hi Knowledge, I'd like to plan a trip to {d['name']}")}" class="btn btn-outline">Ask on WhatsApp</a>
    </div>
  </div>
</section>

<section class="bg-white tight">
  <div class="wrap">
    {render_quick_facts(d['facts'])}
  </div>
</section>

<section id="why">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why visit</span>
      <h2 class="section-title">Why visit {d['name']}</h2>
    </div>
    {render_why_visit(d['why_visit'])}
  </div>
</section>

<section class="bg-white" id="things-to-do">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">On the ground</span>
      <h2 class="section-title">Best things to do in {d['name']}</h2>
    </div>
    {render_things_to_do(d['things_to_do'])}
  </div>
</section>

<section id="planning">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Timing it right</span>
      <h2 class="section-title">Best time to visit &amp; how long to stay</h2>
    </div>
    <div class="inc-grid">
      <div class="inc-box yes">
        <h4>{icon('calendar')} Best time to visit</h4>
        <p style="font-size:14.5px;color:var(--slate);">{d['best_time']}</p>
      </div>
      <div class="inc-box yes">
        <h4>{icon('clock')} How many days you need</h4>
        <p style="font-size:14.5px;color:var(--slate);">{d['days_needed']}</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-white" id="stay">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Basing yourself here</span>
      <h2 class="section-title">Where to stay in {d['name']}</h2>
    </div>
    <div class="why-grid">
      {"".join(f'''<div class="why-card reveal"><div class="why-icon">{icon("map-pin")}</div><h4>{t}</h4><p>{b}</p></div>''' for t, b in d['where_to_stay'])}
    </div>
  </div>
</section>

<section id="getting-there">
  <div class="wrap">
    <div class="inc-grid">
      <div class="inc-box yes">
        <h4>{icon('plane')} How to get there</h4>
        <p style="font-size:14.5px;color:var(--slate);">{d['how_to_get_there']}</p>
      </div>
      {render_what_to_pack(d['what_to_pack'])}
    </div>
  </div>
</section>

<section class="bg-white" id="itinerary">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">A starting point</span>
      <h2 class="section-title">Sample {d['name']} itinerary</h2>
      <p class="section-sub">A realistic outline — every trip we plan adjusts this to your dates and pace.</p>
    </div>
    {render_itinerary(d['sample_itinerary'])}
  </div>
</section>

<section class="related-strip tight" id="related-tours">
  <div class="wrap">
    <span class="eyebrow">Tours that cover {d['name']}</span>
    <div class="related-pills">
      {render_related_tours(d['related_tours'])}
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap-narrow">
    <div class="section-head">
      <span class="eyebrow">Common questions</span>
      <h2 class="section-title">FAQ: {d['name']}</h2>
    </div>
    {render_faq(d['faq'])}
  </div>
</section>

<section class="bg-white tight" id="read-more">
  <div class="wrap">
    <span class="eyebrow">Read more</span>
    <h3 style="margin-top:8px;font-size:20px;">Related travel guides</h3>
    <div class="related-pills">
      {render_related_articles(d['related_articles'])}
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Ready to start planning your {d['name']} trip?</h2>
    <p>Tell us your dates and what you want to see. We'll reply with a real itinerary, not a sales pitch.</p>
    <div class="cta-actions">
      <a href="../contact.html" class="btn btn-primary">Start Planning</a>
      <a href="{WHATSAPP_LINK}" class="btn btn-whatsapp">{icon('whatsapp')} Chat on WhatsApp</a>
    </div>
    <div class="cta-trustline">Usually replying within 24 hours, Mon–Sat (CAT, UTC+2)</div>
  </div>
</section>
'''
    html = page(
        title=f"{d['meta_title']} | Zimbabwe Tour Guide",
        description=d['meta_description'],
        canonical_path=canonical,
        body=body,
        extra_jsonld=jsonld,
        keywords=f"{d['name']} Zimbabwe, {d['name']} travel guide, {d['name']} tours, visit {d['name']}",
    )
    write(f"destinations/{slug}.html", html)


def build_destinations_hub():
    canonical = "/destinations/index.html"
    cards = []
    for d in DESTINATIONS:
        slug = d['slug']
        content = DESTINATION_CONTENT[slug]
        palette, motif = DEST_SCENES.get(slug, ("green", "hills"))
        svg = scene_svg(palette, motif)
        cards.append(f'''<a href="{slug}.html" class="dest-card reveal">
      <div class="dest-media">{svg}<span class="dest-tag">{d['tag']}</span></div>
      <div class="dest-body">
        <h3>{d['name']}</h3>
        <p>{content['intro'][:120]}&hellip;</p>
        <span class="dest-link">Explore {d['name']} {icon('arrow')}</span>
      </div>
    </a>''')

    jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{
        ",".join(f'{{"@type":"ListItem","position":{i+1},"name":"{d["name"]}","url":"https://www.zimbabwetourguide.com/destinations/{d["slug"]}.html"}}' for i, d in enumerate(DESTINATIONS))
    }]}}
</script>'''

    body = f'''
{breadcrumb([("Home","index.html"),("Destinations", None)], canonical)}

<section class="page-hero">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">Where to go in Zimbabwe</span>
    <h1>Zimbabwe Destinations</h1>
    <p>From the thunder of Victoria Falls to the quiet stone ruins of Great Zimbabwe and the cool mountain air of the Eastern Highlands — explore the places that make up almost every trip we plan.</p>
  </div>
</section>

<section class="bg-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Six places, one country</span>
      <h2 class="section-title">Explore by destination</h2>
      <p class="section-sub">Each destination page covers what to do, when to go, where to stay, and a sample itinerary — built from on-the-ground experience, not guesswork.</p>
    </div>
    <div class="card-grid cols-4">
      {"".join(cards)}
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Not sure which destinations to combine?</h2>
    <p>Most travelers visit two or three of these places in one trip. Tell us what you're drawn to and we'll suggest a route that actually makes sense.</p>
    <div class="cta-actions">
      <a href="../contact.html" class="btn btn-primary">Start Planning My Trip</a>
      <a href="../tours/custom-zimbabwe-tour.html" class="btn btn-outline">See Custom Tour Option</a>
    </div>
  </div>
</section>
'''
    html = page(
        title="Zimbabwe Destinations | Victoria Falls, Hwange, Great Zimbabwe & More",
        description="Explore Zimbabwe's top travel destinations — Victoria Falls, Hwange National Park, Great Zimbabwe, Nyanga, Chimanimani, and Harare — with practical guides for each.",
        canonical_path=canonical,
        body=body,
        extra_jsonld=jsonld,
        keywords="Zimbabwe destinations, places to visit in Zimbabwe, Zimbabwe travel guide",
    )
    write("destinations/index.html", html)


if __name__ == "__main__":
    build_destinations_hub()
    for d in DESTINATIONS:
        build_destination_page(d['slug'], DESTINATION_CONTENT[d['slug']])


