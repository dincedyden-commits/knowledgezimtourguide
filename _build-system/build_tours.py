# -*- coding: utf-8 -*-
from build_common import page, breadcrumb, write, WHATSAPP_LINK, whatsapp_link, TOURS, DESTINATIONS
from data_tours import TOUR_CONTENT
from icons import icon, scene_svg, TOUR_SCENES

DEST_BY_SLUG = {d["slug"]: d for d in DESTINATIONS}


def render_quick_facts(facts):
    items = "".join(
        f'<div class="qf-item">{icon(ic)}<div><b>{label}</b><span>{val}</span></div></div>'
        for ic, label, val in facts
    )
    return f'<div class="quick-facts">{items}</div>'


def render_highlights(items):
    lis = "".join(f'<li>{icon("check")}{item}</li>' for item in items)
    return f'<div class="inc-box yes" style="max-width:760px;"><h4>{icon("check")} Trip highlights</h4><ul>{lis}</ul></div>'


def render_itinerary(days):
    rows = "".join(
        f'''<div class="itin-day reveal"><span class="day-label">{day}</span><h4>{title}</h4><p>{body}</p></div>'''
        for day, title, body in days
    )
    return f'<div class="itinerary">{rows}</div>'


def render_included(included, not_included):
    inc = "".join(f'<li>{icon("check")}{i}</li>' for i in included)
    exc = "".join(f'<li>{icon("cross")}{i}</li>' for i in not_included)
    return f'''<div class="inc-grid">
      <div class="inc-box yes"><h4>{icon('check')} What's included</h4><ul>{inc}</ul></div>
      <div class="inc-box no"><h4>{icon('cross')} What's not included</h4><ul>{exc}</ul></div>
    </div>'''


def render_faq(items):
    rows = []
    for i, (q, a) in enumerate(items):
        open_cls = " open" if i == 0 else ""
        aria = "true" if i == 0 else "false"
        rows.append(f'''<div class="faq-item{open_cls}">
      <button class="faq-q" aria-expanded="{aria}">{q} {icon("plus")}</button>
      <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
    </div>''')
    return f'<div class="faq-list">{"".join(rows)}</div>'


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


def render_related_destinations(slugs):
    pills = "".join(
        f'<a href="../destinations/{s}.html" class="related-pill">{icon("arrow")} {DEST_BY_SLUG[s]["name"]}</a>'
        for s in slugs if s in DEST_BY_SLUG
    )
    return pills


def build_tour_page(slug, t):
    canonical = f"/tours/{slug}.html"
    palette, motif = TOUR_SCENES.get(slug, ("green", "hills"))
    hero_art = scene_svg(palette, motif)

    jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"TouristTrip","name":"{t['name']}","description":"{t['overview'][:200].replace(chr(34), chr(39))}"}}
</script>
{faq_jsonld(t['faq'])}'''

    wa_link = whatsapp_link(f"Hi Knowledge, I'd like to book the {t['name']}")

    body = f'''
{breadcrumb([("Home","index.html"),("Tours","tours/index.html"),(t['name'], None)], canonical)}

<section class="page-hero">
  <div class="hero-art" style="position:absolute;bottom:0;left:0;width:100%;z-index:1;opacity:0.5;">{hero_art}</div>
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">{t['hero_kicker']}</span>
    <h1>{t['name']}</h1>
    <div class="page-hero-meta">
      <span class="pill">{icon('compass')} {t['tag']}</span>
    </div>
    <div class="page-hero-actions">
      <a href="../contact.html" class="btn btn-primary">Enquire About This Tour</a>
      <a href="{wa_link}" class="btn btn-outline">{icon('whatsapp')} Ask on WhatsApp</a>
    </div>
  </div>
</section>

<section class="bg-white tight">
  <div class="wrap">
    {render_quick_facts(t['quick_facts'])}
  </div>
</section>

<section id="overview">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Tour overview</span>
      <h2 class="section-title">What this trip is</h2>
      <p class="section-sub">{t['overview']}</p>
    </div>
    {render_highlights(t['highlights'])}
  </div>
</section>

<section class="bg-white" id="itinerary">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Day by day</span>
      <h2 class="section-title">Sample itinerary</h2>
    </div>
    {render_itinerary(t['itinerary'])}
  </div>
</section>

<section id="included">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The fine print, made clear</span>
      <h2 class="section-title">What's included &amp; what's not</h2>
    </div>
    {render_included(t['included'], t['not_included'])}
    <div class="inc-box yes" style="margin-top:20px;max-width:760px;">
      <h4>{icon('compass')} A note on pricing</h4>
      <p style="font-size:14.5px;color:var(--slate);">{t['pricing_notes']}</p>
    </div>
  </div>
</section>

<section class="bg-white tight">
  <div class="wrap">
    <div class="inc-box yes" style="max-width:100%;">
      <h4>{icon('users')} Who this trip is best for</h4>
      <p style="font-size:14.5px;color:var(--slate);">{t['best_for']}</p>
    </div>
  </div>
</section>

<section class="related-strip tight" id="related-destinations">
  <div class="wrap">
    <span class="eyebrow">Destinations on this tour</span>
    <div class="related-pills">
      {render_related_destinations(t['related_destinations'])}
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap-narrow">
    <div class="section-head">
      <span class="eyebrow">Common questions</span>
      <h2 class="section-title">FAQ: {t['name']}</h2>
    </div>
    {render_faq(t['faq'])}
    <p style="margin-top:20px;font-size:14px;color:var(--slate);">Have a question that's not here? See our full <a href="../faq.html" style="color:var(--green-deep);font-weight:700;">FAQ page</a> or ask us directly.</p>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Ready to enquire about the {t['name']}?</h2>
    <p>Send your dates and group size — we'll reply with a clear, honest itinerary and quote.</p>
    <div class="cta-actions">
      <a href="../contact.html" class="btn btn-primary">Start Your Enquiry</a>
      <a href="{wa_link}" class="btn btn-whatsapp">{icon('whatsapp')} Chat on WhatsApp</a>
    </div>
    <div class="cta-trustline">Usually replying within 24 hours, Mon–Sat (CAT, UTC+2)</div>
  </div>
</section>
'''
    html = page(
        title=f"{t['meta_title']} | Zimbabwe Tour Guide",
        description=t['meta_description'],
        canonical_path=canonical,
        body=body,
        extra_jsonld=jsonld,
        keywords=f"{t['name']}, Zimbabwe tours, {t['tag']} Zimbabwe",
    )
    write(f"tours/{slug}.html", html)


def build_tours_hub():
    canonical = "/tours/index.html"
    cards = []
    for t in TOURS:
        slug = t['slug']
        content = TOUR_CONTENT[slug]
        palette, motif = TOUR_SCENES.get(slug, ("green", "hills"))
        svg = scene_svg(palette, motif)
        cards.append(f'''<a href="{slug}.html" class="tour-card reveal">
      <div class="tour-media">{svg}<span class="tour-trip-type">{t['type']}</span><span class="tour-duration">{t['duration']}</span></div>
      <div class="tour-body">
        <h3>{t['name']}</h3>
        <p>{content['overview'][:115]}&hellip;</p>
        <div class="tour-foot">
          <span class="tour-link">View Details {icon('arrow')}</span>
        </div>
      </div>
    </a>''')

    body = f'''
{breadcrumb([("Home","index.html"),("Tours", None)], canonical)}

<section class="page-hero">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">Private tours, not group packages</span>
    <h1>Zimbabwe Tours &amp; Custom Itineraries</h1>
    <p>Every tour below is a starting point built from real routes and real lodges — combine them, shorten them, or let us build something entirely custom around your trip.</p>
  </div>
</section>

<section class="bg-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose a starting point</span>
      <h2 class="section-title">Private Zimbabwe tours</h2>
      <p class="section-sub">Each tour page includes a full itinerary, what's included, and honest pricing notes — no surprises after you enquire.</p>
    </div>
    <div class="card-grid">
      {"".join(cards)}
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Want to combine two or three of these into one trip?</h2>
    <p>Most of our best itineraries are a mix — a few days at the Falls, a few in Hwange, maybe a stop in the highlands. Tell us what you're drawn to.</p>
    <div class="cta-actions">
      <a href="custom-zimbabwe-tour.html" class="btn btn-primary">See the Custom Tour Option</a>
      <a href="../contact.html" class="btn btn-outline">Start Planning</a>
    </div>
  </div>
</section>
'''
    html = page(
        title="Zimbabwe Tours | Private Safari & Sightseeing Itineraries",
        description="Browse private Zimbabwe tours — Victoria Falls, Hwange Safari, Great Zimbabwe, Nyanga, Chimanimani, and fully custom itineraries built around your trip.",
        canonical_path=canonical,
        body=body,
        keywords="Zimbabwe tours, private Zimbabwe safari, Zimbabwe tour packages, custom Zimbabwe itinerary",
    )
    write("tours/index.html", html)


if __name__ == "__main__":
    build_tours_hub()
    for t in TOURS:
        build_tour_page(t['slug'], TOUR_CONTENT[t['slug']])


