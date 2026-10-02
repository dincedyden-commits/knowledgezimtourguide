# -*- coding: utf-8 -*-
from build_common import page, breadcrumb, write, WHATSAPP_LINK
from icons import icon, scene_svg

canonical = "/gallery.html"

GALLERY_ITEMS = [
    ("dusk", "falls", "Victoria Falls", "The rainforest viewpoint", "Spray can reach you even from the official viewpoints during high-water months — worth the soaking."),
    ("gold", "savanna", "Hwange National Park", "Dusk at a waterhole", "Elephant herds often arrive in the last light, when the heat has finally broken."),
    ("terracotta", "ruins", "Great Zimbabwe", "The Great Enclosure wall", "Built without mortar roughly 700 years ago, and still standing exactly as it was laid."),
    ("forest", "mountains", "Nyanga", "Mount Nyangani at sunrise", "Zimbabwe's highest peak, usually clearest in the very early morning before mist rolls in."),
    ("slate", "trek", "Chimanimani", "The high mountain trail", "Quartzite peaks and a trail that sees more wildlife than people most days."),
    ("green", "city", "Harare", "Jacaranda season streets", "Late September into October, when the avenues briefly turn entirely purple."),
    ("green", "hills", "Eastern Highlands", "Tea estate hills near Nyanga", "Rolling, terraced hillsides that feel closer to the Cape Winelands than typical safari country."),
    ("dusk", "river", "Zambezi River", "Sunset cruise stretch", "The same stretch of river that feeds the Falls a few kilometres downstream."),
    ("gold", "hills", "Hwange Plains", "Open grassland at dawn", "The first game drive of the day often starts before the sun is properly up."),
]

cards = []
for palette, motif, label, title, caption in GALLERY_ITEMS:
    svg = scene_svg(palette, motif)
    cards.append(f'''<div class="gallery-item reveal">
      <div class="gallery-media">{svg}</div>
      <div class="gallery-caption">
        <span class="g-label">{label}</span>
        <h4>{title}</h4>
        <p>{caption}</p>
      </div>
    </div>''')

body = f'''
{breadcrumb([("Home","index.html"),("Gallery", None)], canonical)}

<section class="page-hero">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">A sense of place before you arrive</span>
    <h1>Gallery</h1>
    <p>A few scenes from the destinations we plan trips around — with notes on what each place actually feels like, not just what it looks like.</p>
  </div>
</section>

<section class="bg-cream">
  <div class="wrap">
    <div class="gallery-grid">
      {"".join(cards)}
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Want to see these places for yourself?</h2>
    <p>Tell us which scenes caught your eye and we'll build a trip around them.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Start Planning My Trip</a>
      <a href="{WHATSAPP_LINK}" class="btn btn-whatsapp">{icon('whatsapp')} Chat on WhatsApp</a>
    </div>
  </div>
</section>
'''

html = page(
    title="Gallery | Zimbabwe Tour Guide — Scenes from the Destinations We Cover",
    description="Browse scenes from Victoria Falls, Hwange, Great Zimbabwe, Nyanga, Chimanimani and Harare, with short notes on what each destination actually feels like.",
    canonical_path=canonical,
    body=body,
    keywords="Zimbabwe travel photos, Zimbabwe gallery, Victoria Falls photos, Hwange photos",
)
write("gallery.html", html)


