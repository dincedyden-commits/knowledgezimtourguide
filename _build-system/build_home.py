# -*- coding: utf-8 -*-
from build_common import page, write, WHATSAPP_LINK, DESTINATIONS, TOURS
from data_destinations import DESTINATION_CONTENT
from data_tours import TOUR_CONTENT
from icons import icon, scene_svg, DEST_SCENES, TOUR_SCENES

canonical = "/index.html"

HORIZON_SVG = '''<svg class="page-hero-art" viewBox="0 0 1440 560" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute;bottom:0;left:0;width:100%;height:auto;z-index:1;opacity:0.95;">
  <circle cx="1160" cy="120" r="86" fill="#D4A017" opacity="0.85"/>
  <path d="M0 320 Q 220 260, 440 310 T 880 290 T 1440 330 V 560 H 0 Z" fill="#2A6B4F" opacity="0.55"/>
  <path d="M0 380 Q 260 330, 520 370 T 1020 360 T 1440 390 V 560 H 0 Z" fill="#1F4D3A" opacity="0.75"/>
  <path d="M0 430 Q 300 400, 600 425 T 1100 415 T 1440 435 V 560 H 0 Z" fill="#143226"/>
  <g transform="translate(150,250)" opacity="0.85">
    <path d="M0 160 L4 60" stroke="#0F2A1F" stroke-width="5" stroke-linecap="round"/>
    <ellipse cx="0" cy="40" rx="62" ry="16" fill="#0F2A1F"/>
    <ellipse cx="-30" cy="55" rx="34" ry="10" fill="#0F2A1F"/>
    <ellipse cx="32" cy="58" rx="30" ry="9" fill="#0F2A1F"/>
  </g>
  <g transform="translate(1250,300) scale(0.7)" opacity="0.7">
    <path d="M0 160 L4 60" stroke="#0F2A1F" stroke-width="5" stroke-linecap="round"/>
    <ellipse cx="0" cy="40" rx="62" ry="16" fill="#0F2A1F"/>
    <ellipse cx="-30" cy="55" rx="34" ry="10" fill="#0F2A1F"/>
  </g>
</svg>'''


def dest_cards():
    cards = []
    for d in DESTINATIONS[:4]:
        slug = d['slug']
        content = DESTINATION_CONTENT[slug]
        palette, motif = DEST_SCENES.get(slug, ("green", "hills"))
        svg = scene_svg(palette, motif)
        cards.append(f'''<a href="destinations/{slug}.html" class="dest-card reveal">
      <div class="dest-media">{svg}<span class="dest-tag">{d['tag']}</span></div>
      <div class="dest-body">
        <h3>{d['name']}</h3>
        <p>{content['intro'][:110]}&hellip;</p>
        <span class="dest-link">Explore {d['name']} {icon('arrow')}</span>
      </div>
    </a>''')
    return "".join(cards)


def tour_cards():
    cards = []
    for i, t in enumerate(TOURS[:4]):
        slug = t['slug']
        content = TOUR_CONTENT[slug]
        palette, motif = TOUR_SCENES.get(slug, ("green", "hills"))
        svg = scene_svg(palette, motif)
        cards.append(f'''<a href="tours/{slug}.html" class="tour-card reveal">
      <div class="tour-media">{svg}<div class="tour-stop-marker" style="position:absolute;top:14px;left:14px;width:30px;height:30px;border-radius:50%;background:var(--gold);color:var(--green-deeper);display:flex;align-items:center;justify-content:center;font-family:var(--serif);font-weight:700;font-size:13px;box-shadow:0 3px 8px rgba(0,0,0,0.25);">{i+1}</div><span class="tour-duration">{t['duration']}</span></div>
      <div class="tour-body">
        <h3>{t['name']}</h3>
        <p>{content['overview'][:105]}&hellip;</p>
        <div class="tour-foot">
          <span class="tour-link">Enquire {icon('arrow')}</span>
        </div>
      </div>
    </a>''')
    return "".join(cards)


jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TravelAgency",
  "name": "Zimbabwe Tour Guide",
  "description": "Private tour planning and local trip design across Zimbabwe, including Victoria Falls, Hwange National Park, Mana Pools, Great Zimbabwe, Nyanga, Chimanimani and Harare.",
  "areaServed": "Zimbabwe",
  "priceRange": "$$",
  "telephone": "+263-77-000-0000",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Victoria Falls",
    "addressCountry": "ZW"
  }
}
</script>'''

body = f'''
<section class="hero" style="position:relative;background:linear-gradient(180deg,#173B2C 0%, var(--green-deep) 55%, #2A6B4F 100%);color:#fff;overflow:hidden;padding-top:0;">
  {HORIZON_SVG}
  <div class="wrap" style="position:relative;z-index:2;padding:48px 0 60px;">
    <div class="hero-eyebrow" style="display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);padding:7px 14px;border-radius:30px;font-size:12.5px;font-weight:600;letter-spacing:0.04em;color:var(--gold-soft);margin-bottom:22px;">
      <span style="width:7px;height:7px;border-radius:50%;background:var(--gold);box-shadow:0 0 0 3px rgba(212,160,23,0.25);display:inline-block;"></span>
      Planned by Zimbabweans who live here, not a call center
    </div>
    <h1 style="color:#fff;font-size:clamp(34px,7vw,62px);font-weight:600;line-height:1.06;letter-spacing:-0.01em;max-width:780px;">Zimbabwe, planned properly &mdash; <em style="font-style:italic;color:var(--gold-soft);font-weight:500;">by people who actually know it.</em></h1>
    <p style="font-size:clamp(16px,2.2vw,19px);color:rgba(255,255,255,0.82);max-width:520px;margin-top:20px;">Private tours and personal trip planning across Victoria Falls, Hwange, Great Zimbabwe, Nyanga, Chimanimani and Harare — built around your dates, your pace, and your budget, with a real local guide on the other end of the message.</p>
    <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:32px;">
      <a href="contact.html" class="btn btn-primary">Start Planning My Trip</a>
      <a href="tours/index.html" class="btn btn-outline">See Popular Tours</a>
    </div>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-top:48px;padding-top:28px;border-top:1px solid rgba(255,255,255,0.15);max-width:560px;" class="hero-stats-grid">
      <div><b style="display:block;font-family:var(--serif);font-size:clamp(22px,4vw,30px);color:var(--gold-soft);font-weight:600;">11+ yrs</b><span style="font-size:13px;color:rgba(255,255,255,0.7);">Guiding across Zimbabwe</span></div>
      <div><b style="display:block;font-family:var(--serif);font-size:clamp(22px,4vw,30px);color:var(--gold-soft);font-weight:600;">600+</b><span style="font-size:13px;color:rgba(255,255,255,0.7);">Private trips planned</span></div>
      <div><b style="display:block;font-family:var(--serif);font-size:clamp(22px,4vw,30px);color:var(--gold-soft);font-weight:600;">4.9 / 5</b><span style="font-size:13px;color:rgba(255,255,255,0.7);">Average traveler rating</span></div>
      <div><b style="display:block;font-family:var(--serif);font-size:clamp(22px,4vw,30px);color:var(--gold-soft);font-weight:600;">&lt; 24 hrs</b><span style="font-size:13px;color:rgba(255,255,255,0.7);">Typical reply time</span></div>
    </div>
  </div>
</section>

<div class="wrap" style="position:relative;">
  <div class="enquiry-card" style="max-width:560px;margin:-30px auto 0;">
    <h3>Tell us about your trip</h3>
    <p>One message, real answers from a local planner — no booking-bot replies.</p>
    <form id="enquiryForm" onsubmit="return handleFormSubmit(event, 'Sent — we\\'ll reply within 24 hours')">
      <div class="field-row">
        <div class="field"><label for="fname">Full name</label><input id="fname" type="text" placeholder="Jane Carter" required></div>
        <div class="field"><label for="femail">Email</label><input id="femail" type="email" placeholder="jane@email.com" required></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="fdates">Travel dates</label><input id="fdates" type="text" placeholder="e.g. Sept 2026"></div>
        <div class="field"><label for="fsize">Group size</label>
          <select id="fsize"><option>Solo traveler</option><option>Couple</option><option>Family</option><option>Small group (5+)</option></select>
        </div>
      </div>
      <div class="field"><label for="fmsg">What do you want to see or do?</label><textarea id="fmsg" rows="3" placeholder="e.g. Victoria Falls + a 3-day Hwange safari, mid-range budget"></textarea></div>
      <button type="submit" class="btn btn-primary btn-block">Send My Trip Request</button>
    </form>
    <div class="enquiry-note">{icon('shield')} No payment required to enquire. We reply with a real itinerary, not a price list.</div>
  </div>
</div>

<div class="strip">
  <div class="wrap">
    <div class="strip-item">{icon('star-shield')} Zimbabwe Tourism Authority registered</div>
    <div class="strip-item">{icon('shield')} Licensed local guides only</div>
    <div class="strip-item">{icon('clock')} Secured trip deposits, no hidden fees</div>
    <div class="strip-item">{icon('users')} Genuinely loved by past travelers</div>
  </div>
</div>

<section id="why">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Why travel with us</span>
      <h2 class="section-title">A real person plans your trip — not a template</h2>
      <p class="section-sub">Most "Zimbabwe tour" sites are resellers. We're guides and planners on the ground, and that changes what we can tell you.</p>
    </div>
    <div class="why-grid">
      <div class="why-card reveal"><div class="why-icon">{icon('map-pin')}</div><h4>Local, on-the-ground knowledge</h4><p>We know which Hwange waterholes are active this week, not just what's printed in a brochure from five years ago.</p></div>
      <div class="why-card reveal"><div class="why-icon">{icon('users')}</div><h4>Private, not bus-tour group trips</h4><p>Every itinerary is built for you and your group — your pace, your interests, your budget — never a fixed package.</p></div>
      <div class="why-card reveal"><div class="why-icon">{icon('compass')}</div><h4>Straight talk on cost and safety</h4><p>We tell you honestly what something costs and what it doesn't include — and flag safety basics most sites skip.</p></div>
      <div class="why-card reveal"><div class="why-icon">{icon('whatsapp')}</div><h4>You message a guide, not a queue</h4><p>Questions get answered by someone who has actually driven the route — usually within a day.</p></div>
    </div>
  </div>
</section>

<section class="bg-white" id="destinations">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Where to go</span>
      <h2 class="section-title">Popular Zimbabwe destinations</h2>
      <p class="section-sub">Six places that make up almost every trip we plan — explore each one before you decide on a route.</p>
    </div>
    <div class="card-grid cols-4">
      {dest_cards()}
    </div>
    <div style="text-align:center;margin-top:36px;">
      <a href="destinations/index.html" class="btn btn-ghost">See All Destinations</a>
    </div>
  </div>
</section>

<section id="tours">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The route most travelers take</span>
      <h2 class="section-title">Popular private tours across Zimbabwe</h2>
      <p class="section-sub">Each trip below can be shortened, combined, or rebuilt entirely — these are starting points, not fixed packages.</p>
    </div>
    <div class="card-grid">
      {tour_cards()}
    </div>
    <div style="text-align:center;margin-top:36px;">
      <a href="tours/custom-zimbabwe-tour.html" class="btn btn-ghost">Combine These Into One Private Itinerary</a>
    </div>
  </div>
</section>

<section class="bg-green how-section" style="position:relative;overflow:hidden;" id="how">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow on-dark">From message to Zambezi sunset</span>
      <h2 class="section-title">How a trip with us actually comes together</h2>
      <p class="section-sub">No deposit until you have a real itinerary in hand and you're happy with it.</p>
    </div>
    <div class="how-grid" style="display:grid;grid-template-columns:1fr;gap:0;margin-top:48px;">
      <div class="how-step reveal" style="padding:0 22px 36px 0;"><div class="step-num" style="font-family:var(--serif);font-size:15px;color:var(--gold-soft);font-weight:700;width:34px;height:34px;border:1.5px solid rgba(212,160,23,0.5);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:18px;">1</div><h4 style="color:#fff;font-size:18px;margin-bottom:10px;">You tell us the shape of your trip</h4><p style="color:rgba(255,255,255,0.72);font-size:14.5px;">Dates, interests, and budget — rough is fine. We ask the follow-up questions that actually matter.</p></div>
      <div class="how-step reveal" style="padding:0 22px 36px 0;"><div class="step-num" style="font-family:var(--serif);font-size:15px;color:var(--gold-soft);font-weight:700;width:34px;height:34px;border:1.5px solid rgba(212,160,23,0.5);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:18px;">2</div><h4 style="color:#fff;font-size:18px;margin-bottom:10px;">We build a draft itinerary</h4><p style="color:rgba(255,255,255,0.72);font-size:14.5px;">Day-by-day, with real lodges, realistic drive times, and honest pricing — usually within 24–48 hours.</p></div>
      <div class="how-step reveal" style="padding:0 22px 36px 0;"><div class="step-num" style="font-family:var(--serif);font-size:15px;color:var(--gold-soft);font-weight:700;width:34px;height:34px;border:1.5px solid rgba(212,160,23,0.5);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:18px;">3</div><h4 style="color:#fff;font-size:18px;margin-bottom:10px;">We refine it together</h4><p style="color:rgba(255,255,255,0.72);font-size:14.5px;">Swap a lodge, add a day in Hwange, drop an activity — the plan adjusts until it's actually yours.</p></div>
      <div class="how-step reveal" style="padding:0;"><div class="step-num" style="font-family:var(--serif);font-size:15px;color:var(--gold-soft);font-weight:700;width:34px;height:34px;border:1.5px solid rgba(212,160,23,0.5);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:18px;">4</div><h4 style="color:#fff;font-size:18px;margin-bottom:10px;">You travel, we stay reachable</h4><p style="color:rgba(255,255,255,0.72);font-size:14.5px;">A direct contact number for your guide throughout the trip — not a head office on another continent.</p></div>
    </div>
  </div>
</section>

<section class="bg-cream" id="guide">
  <div class="wrap" style="display:grid;grid-template-columns:1fr;gap:48px;align-items:center;" class="about-hero">
    <div class="portrait-frame reveal">
      <svg viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice">
        <defs><linearGradient id="gphome" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#2A6B4F"/><stop offset="100%" stop-color="#0F2A1F"/></linearGradient></defs>
        <rect width="400" height="500" fill="url(#gphome)"/>
        <circle cx="320" cy="80" r="50" fill="#D4A017" opacity="0.8"/>
        <path d="M0 340 Q120 290 220 330 T400 310 V500 H0Z" fill="#143226"/>
        <path d="M0 390 Q150 360 260 385 T400 370 V500 H0Z" fill="#0A1A13"/>
        <g transform="translate(70,330)" opacity="0.9"><path d="M0 130 L3 50" stroke="#0A1A13" stroke-width="5" stroke-linecap="round"/><ellipse cx="0" cy="35" rx="50" ry="13" fill="#0A1A13"/></g>
      </svg>
      <div class="portrait-badge"><span class="stars">★★★★★</span><div><b style="font-size:13px;">4.9 / 5</b><small>180+ traveler reviews</small></div></div>
    </div>
    <div>
      <span class="eyebrow">Who's actually planning your trip</span>
      <h2 class="section-title">Meet Knowledge, your local guide</h2>
      <p class="section-sub">Zimbabwe Tour Guide is run by Knowledge and a small team of licensed, Zimbabwe-based guides — not a booking platform reselling someone else's itineraries.</p>
      <div class="guide-quote">"We don't sell Zimbabwe as a postcard. We plan it the way we'd plan it for our own family — honestly, and with the boring-but-important details sorted first."</div>
      <div style="margin-top:24px;"><a href="about.html" class="btn btn-ghost">Read Knowledge's Story</a></div>
    </div>
  </div>
</section>

<section class="bg-white" id="testimonials">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">What past travelers say</span>
      <h2 class="section-title">Real trips, real feedback</h2>
    </div>
    <div class="testi-grid">
      <div class="testi-card reveal"><div class="testi-stars">★★★★★</div><p>"They replied to every question personally, and the Hwange itinerary they built was better than anything our agent back home found."</p><div class="testi-person"><div class="testi-avatar">RM</div><div><b>Rachel M.</b><span>United Kingdom</span></div></div></div>
      <div class="testi-card reveal"><div class="testi-stars">★★★★★</div><p>"Felt like we had a friend on the ground the whole trip, not a call center. The Hwange walking safari was the highlight of our year."</p><div class="testi-person"><div class="testi-avatar">DK</div><div><b>David K.</b><span>United States</span></div></div></div>
      <div class="testi-card reveal"><div class="testi-stars">★★★★★</div><p>"Upfront about costs from the first message — no surprise add-ons at the end. We'll book through them again for our next Africa trip."</p><div class="testi-person"><div class="testi-avatar">SN</div><div><b>Sofia N.</b><span>Germany</span></div></div></div>
    </div>
  </div>
</section>

<section class="bg-cream" id="guides-content">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Plan it yourself, with our notes</span>
      <h2 class="section-title">Zimbabwe travel guides</h2>
      <p class="section-sub">40+ practical, on-the-ground guides for travelers who want to understand Zimbabwe before they book anything.</p>
    </div>
    <div class="article-grid">
      <a href="travel-guide/best-time-to-visit-zimbabwe.html" class="article-card reveal">
        <div class="article-media">{scene_svg('green','hills')}<span class="article-cat">Trip Planning</span></div>
        <div class="article-body"><h3>Best Time to Visit Zimbabwe: A Month-by-Month Guide</h3><p>Water levels, weather, and wildlife all swing dramatically by season — here's what to expect.</p><div class="article-meta">9 min read</div></div>
      </a>
      <a href="travel-guide/hwange-vs-mana-pools.html" class="article-card reveal">
        <div class="article-media">{scene_svg('gold','savanna')}<span class="article-cat">Safari Guides</span></div>
        <div class="article-body"><h3>Hwange vs. Mana Pools: Which Safari Fits You?</h3><p>Vehicle game drives or walking safaris — the honest tradeoffs between two flagship parks.</p><div class="article-meta">10 min read</div></div>
      </a>
      <a href="travel-guide/zimbabwe-visa-entry-requirements.html" class="article-card reveal">
        <div class="article-media">{scene_svg('green','city')}<span class="article-cat">Safety &amp; Practical Tips</span></div>
        <div class="article-body"><h3>Zimbabwe Visa &amp; Entry Requirements, Explained Simply</h3><p>What most nationalities actually need at the border, including the KAZA UniVisa option.</p><div class="article-meta">6 min read</div></div>
      </a>
    </div>
    <div style="text-align:center;margin-top:36px;"><a href="travel-guide/index.html" class="btn btn-ghost">Browse All Travel Guides</a></div>
  </div>
</section>

<section class="bg-white" id="faq">
  <div class="wrap-narrow">
    <div class="section-head">
      <span class="eyebrow">Before you ask</span>
      <h2 class="section-title">Frequently asked questions</h2>
    </div>
    <div class="faq-list">
      <div class="faq-item open"><button class="faq-q" aria-expanded="true">Is Zimbabwe safe to travel to right now? {icon('plus')}</button><div class="faq-a"><div class="faq-a-inner">Yes — Zimbabwe's tourist regions (Victoria Falls, Hwange, Great Zimbabwe, the Eastern Highlands) see millions of international visitors with very low rates of traveler crime. As with any destination, normal precautions apply, and we brief every traveler on local specifics before arrival.</div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">How far in advance should I book a private tour? {icon('plus')}</button><div class="faq-a"><div class="faq-a-inner">For peak season (July–October), we recommend 4–6 months ahead, since the best lodges in Hwange fill early. For the green season (November–April), 6–8 weeks is usually enough.</div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">Do you arrange transport between destinations, or just guiding? {icon('plus')}</button><div class="faq-a"><div class="faq-a-inner">Both. Depending on your itinerary, we arrange road transfers, internal flights, or a combination — and we'll always tell you honestly which option suits your route and budget best.</div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">What's not included in the prices shown? {icon('plus')}</button><div class="faq-a"><div class="faq-a-inner">International flights, visa fees, and travel insurance are not included in any quoted price. Every itinerary we send breaks down exactly what is and isn't covered before you pay a deposit.</div></div></div>
    </div>
    <div style="text-align:center;margin-top:28px;"><a href="faq.html" class="btn btn-ghost">See the Full FAQ</a></div>
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Your Zimbabwe trip starts with one honest conversation.</h2>
    <p>Tell us your dates and what you want to see. We'll reply with a real plan — not a sales pitch.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Start Planning My Trip</a>
      <a href="{WHATSAPP_LINK}" class="btn btn-whatsapp">{icon('whatsapp')} Chat on WhatsApp</a>
    </div>
    <div class="cta-trustline">Usually replying within 24 hours, Mon–Sat (CAT, UTC+2)</div>
  </div>
</section>
'''

html = page(
    title="Zimbabwe Tour Guide | Private Tours & Local Trip Planning with Knowledge",
    description="Plan a private Zimbabwe safari with local experts who know the routes, the rangers, and the right season. Victoria Falls, Hwange, Great Zimbabwe, Nyanga, Chimanimani & Harare tours, planned by Zimbabweans, built around you.",
    canonical_path=canonical,
    body=body,
    extra_jsonld=jsonld,
    keywords="Zimbabwe tours, Zimbabwe safari, Victoria Falls tours, Hwange National Park safari, private Zimbabwe tour guide, Zimbabwe trip planning",
)
write("index.html", html)


