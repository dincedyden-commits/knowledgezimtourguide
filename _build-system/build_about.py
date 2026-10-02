# -*- coding: utf-8 -*-
from build_common import page, breadcrumb, write, WHATSAPP_LINK
from icons import icon, scene_svg

canonical = "/about.html"

jsonld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Person","name":"Knowledge","jobTitle":"Local Zimbabwe Tour Guide","worksFor":{"@type":"Organization","name":"Zimbabwe Tour Guide"}}
</script>'''

portrait_svg = '''<svg viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice">
  <defs><linearGradient id="gpabout" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#2A6B4F"/><stop offset="100%" stop-color="#0F2A1F"/></linearGradient></defs>
  <rect width="400" height="500" fill="url(#gpabout)"/>
  <circle cx="320" cy="80" r="50" fill="#D4A017" opacity="0.8"/>
  <path d="M0 340 Q120 290 220 330 T400 310 V500 H0Z" fill="#143226"/>
  <path d="M0 390 Q150 360 260 385 T400 370 V500 H0Z" fill="#0A1A13"/>
  <g transform="translate(70,330)" opacity="0.9"><path d="M0 130 L3 50" stroke="#0A1A13" stroke-width="5" stroke-linecap="round"/><ellipse cx="0" cy="35" rx="50" ry="13" fill="#0A1A13"/></g>
  <circle cx="200" cy="180" r="55" fill="#E8BE4F" opacity="0.15"/>
</svg>'''

body = f'''
{breadcrumb([("Home","index.html"),("About", None)], canonical)}

<section class="page-hero">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">The person behind every itinerary</span>
    <h1>Meet Knowledge — Your Local Zimbabwe Tour Guide</h1>
    <p>Every trip on this site is planned by a real person who has driven these roads, guided these parks, and answered these exact questions hundreds of times before.</p>
  </div>
</section>

<section class="about-hero bg-white">
  <div class="wrap" style="display:grid;grid-template-columns:1fr;gap:48px;align-items:center;">
    <div class="portrait-frame reveal">
      {portrait_svg}
      <div class="portrait-badge"><span class="stars">★★★★★</span><div><b style="font-size:13px;">4.9 / 5</b><small>180+ traveler reviews</small></div></div>
    </div>
    <div class="guide-content">
      <span class="eyebrow">Who Knowledge is</span>
      <h2 class="section-title">Born and guiding in Zimbabwe for over a decade</h2>
      <p class="section-sub">Knowledge grew up in Matabeleland North, close enough to Victoria Falls that the sound of the Falls and the rhythm of the tourism season were simply part of everyday life. He trained and was licensed as a professional guide more than eleven years ago, and has spent that time guiding across Victoria Falls, Hwange National Park, Great Zimbabwe, and the Eastern Highlands.</p>
      <ul class="about-list">
        <li>{icon('shield')} <span><strong>Licensed under Zimbabwe's Tourism Act</strong>, with first-aid and wilderness safety certification kept current year to year.</span></li>
        <li>{icon('users')} <span><strong>Direct relationships with park rangers and lodge operators</strong> built over more than a decade of guiding, which means real-time knowledge of what's actually happening on the ground.</span></li>
        <li>{icon('map-pin')} <span><strong>Based in Victoria Falls</strong>, with the small team that helps run Zimbabwe Tour Guide spread across the destinations this site covers.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="bg-cream">
  <div class="wrap-narrow legal-content">
    <h2>Why he started helping travelers in Zimbabwe</h2>
    <p>Knowledge started guiding because he kept noticing the same gap: international travelers were booking trips through agencies and platforms that had never actually been to the places they were selling. Itineraries were built from outdated brochures, not from knowing which waterhole was active that particular week or which lodge had genuinely improved its food in the last year.</p>
    <p>Zimbabwe Tour Guide grew directly out of that frustration — a small operation built around the idea that the person planning your trip should be someone who has actually driven the route, eaten at the lodge, and stood at the viewpoint they're describing to you.</p>

    <h2>What types of trips he helps with</h2>
    <p>Knowledge and the team plan everything from a simple two-day Victoria Falls visit to multi-destination itineraries combining safari time in Hwange with mountain trekking in Chimanimani or a cultural stop at Great Zimbabwe. Solo travelers, couples, families, and small groups are all welcome — pacing and activity choices adjust to who's actually traveling.</p>
    <p>He particularly enjoys helping first-time visitors to Africa who aren't sure what to expect, and returning travelers who want to go beyond the standard Victoria Falls stopover into Zimbabwe's quieter, less-visited corners.</p>

    <h2>Favorite Zimbabwe destinations</h2>
    <p>Ask Knowledge directly and he'll tell you Hwange at dawn during the dry season is hard to beat — the way elephant herds emerge out of the dust as the light comes up never quite gets old, even after a decade of seeing it. For something completely different, he's partial to the cool, quiet mornings in Nyanga, a deliberate contrast to the lowland heat most visitors associate with Zimbabwe.</p>

    <h2>What travelers can expect</h2>
    <p>Direct, honest communication from the first message — including being told plainly if something you're asking for isn't realistic within your dates or budget, rather than being oversold. A real itinerary, with real lodge names and real drive times, usually within 24–48 hours of enquiring. And throughout your actual trip, a direct line to your guide, not a head office on another continent.</p>

    <h2>How to start planning a trip</h2>
    <p>Send a message with your rough dates, group size, and what's drawing you to Zimbabwe — specific (Victoria Falls and a short safari) or vague (somewhere wild, somewhere green) both work. From there, expect a draft itinerary back within a day or two, with as many rounds of adjustment as it takes to get it right.</p>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">A glimpse of the work</span>
      <h2 class="section-title">On the road and in the field</h2>
    </div>
    <div class="mini-media-grid" style="grid-template-columns:repeat(2,1fr);max-width:600px;margin:32px auto 0;">
      <div class="mini-media reveal">{scene_svg('gold','savanna')}</div>
      <div class="mini-media reveal">{scene_svg('dusk','falls')}</div>
      <div class="mini-media reveal">{scene_svg('green','hills')}</div>
      <div class="mini-media reveal">{scene_svg('terracotta','ruins')}</div>
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Ready to start the conversation?</h2>
    <p>Tell Knowledge your dates and what you're hoping to see — you'll hear back from him directly.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Start Planning My Trip</a>
      <a href="{WHATSAPP_LINK}" class="btn btn-whatsapp">{icon('whatsapp')} Chat on WhatsApp</a>
    </div>
    <div class="cta-trustline">Usually replying within 24 hours, Mon–Sat (CAT, UTC+2)</div>
  </div>
</section>
'''

html = page(
    title="About Knowledge | Your Local Zimbabwe Tour Guide",
    description="Meet Knowledge, the licensed local guide behind Zimbabwe Tour Guide — his background, the trips he helps plan, and how to start working with him directly.",
    canonical_path=canonical,
    body=body,
    extra_jsonld=jsonld,
    keywords="Zimbabwe tour guide, Knowledge Zimbabwe guide, local Zimbabwe guide, about Zimbabwe Tour Guide",
)
write("about.html", html)


