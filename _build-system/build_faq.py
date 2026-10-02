# -*- coding: utf-8 -*-
from build_common import page, breadcrumb, write, WHATSAPP_LINK
from icons import icon

canonical = "/faq.html"

FAQ_GROUPS = [
    ("Booking & Planning", [
        ("Can I book a custom Zimbabwe tour?", "Yes — in fact, most of our best trips are custom. Tell us your dates, interests, and budget, and we'll build an itinerary from scratch rather than fitting you into a fixed package. See our <a href='tours/custom-zimbabwe-tour.html' style='color:var(--green-deep);font-weight:700;'>Custom Tour page</a> for how this works."),
        ("How far in advance should I book?", "For peak season (July–October), we recommend 4–6 months ahead, since the best lodges in Hwange and other parks fill early. For the quieter green season (November–April), 6–8 weeks is usually enough. If you're inside that window already, still ask — availability sometimes opens up."),
        ("Can solo travelers book a trip?", "Yes. Solo travelers are welcome on every tour we offer, and single-occupancy accommodation rates are included clearly in your quote rather than hidden in a per-person group rate."),
        ("Do you help with hotels and lodges, or just guiding?", "Both. We can arrange your full accommodation alongside guiding and transport, or simply advise if you've already booked lodges and want a guide layered on top. Tell us what you need."),
    ]),
    ("Costs & Payment", [
        ("Are park fees included in tour prices?", "This depends on the specific tour — our tour pages each break down exactly what's included and what's not. As a general rule, national park entry fees are listed separately unless explicitly stated as included, so you always know the real total before booking."),
        ("Is fuel included in the daily rate for transport?", "Yes, when we quote a vehicle and driver-guide for transfers or multi-day touring, fuel is built into that rate. The only fuel costs you'd cover separately are for a self-drive rental, which is a different arrangement from our guided transport."),
        ("Can I pay in USD?", "Yes — USD is the most commonly used currency for tourism transactions in Zimbabwe, and all our quotes are given in USD. Cash and card payment options will be confirmed with you during booking."),
        ("Do you charge a separate planning fee?", "No. Our planning work is built into the overall cost of your trip, and there's no obligation to pay anything just for receiving a draft itinerary and quote."),
    ]),
    ("Logistics & Transport", [
        ("Do you offer airport pickup?", "Yes — airport pickup and drop-off is a standard part of most itineraries we arrange, particularly at Victoria Falls Airport and Harare International. Let us know your flight details once your trip is confirmed."),
        ("Can you arrange transport between destinations?", "Yes. Depending on the route, we arrange road transfers, domestic flights, or a mix of both, and we'll tell you honestly which option makes more sense for your specific itinerary and budget."),
        ("What kind of vehicles do you use?", "Safari and road transfers typically use air-conditioned 4x4 vehicles suited to the terrain involved, with open-sided safari vehicles used specifically for game drives inside national parks."),
    ]),
    ("Trip Experience", [
        ("Can you accommodate dietary requirements or mobility needs?", "Yes — tell us about any dietary restrictions, allergies, or mobility considerations when you enquire, and we'll factor them into lodge selection, vehicle choice, and activity pacing."),
        ("Is travel insurance required?", "We strongly recommend it for every trip, and consider it essential for safari and trekking-focused itineraries (Hwange, Mana Pools-adjacent activities, Chimanimani). Make sure your policy covers the specific activities in your itinerary."),
        ("What happens if weather affects my planned activities?", "Your guide will assess conditions each day and suggest realistic alternatives if something like a hike or activity isn't safe to attempt as planned — we'd rather adjust than push ahead into unsafe conditions."),
    ]),
]


def render_faq_group(title, items):
    rows = []
    for i, (q, a) in enumerate(items):
        rows.append(f'''<div class="faq-item">
      <button class="faq-q" aria-expanded="false">{q} {icon('plus')}</button>
      <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
    </div>''')
    return f'''<div class="section-head" style="margin-bottom:18px;"><h3 style="font-size:21px;">{title}</h3></div><div class="faq-list" data-exclusive="false">{"".join(rows)}</div>'''


def faq_jsonld():
    import json
    all_items = [item for _, items in FAQ_GROUPS for item in items]
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("<a href='tours/custom-zimbabwe-tour.html' style='color:var(--green-deep);font-weight:700;'>", "").replace("</a>", "")}}
            for q, a in all_items
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


groups_html = "".join(
    f'<div style="margin-bottom:44px;">{render_faq_group(title, items)}</div>'
    for title, items in FAQ_GROUPS
)

body = f'''
{breadcrumb([("Home","index.html"),("FAQ", None)], canonical)}

<section class="page-hero">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">Booking &amp; travel questions, answered plainly</span>
    <h1>Frequently Asked Questions</h1>
    <p>Practical answers to the questions we hear most — grouped so you can jump to what's relevant to your trip.</p>
  </div>
</section>

<section class="bg-white">
  <div class="wrap-narrow">
    {groups_html}
  </div>
</section>

<section class="cta-section">
  <div class="wrap">
    <h2>Didn't find your answer here?</h2>
    <p>Ask us directly — most questions get a real reply within a day.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Ask a Question</a>
      <a href="{WHATSAPP_LINK}" class="btn btn-whatsapp">{icon('whatsapp')} Chat on WhatsApp</a>
    </div>
    <div class="cta-trustline">Usually replying within 24 hours, Mon–Sat (CAT, UTC+2)</div>
  </div>
</section>
'''

html = page(
    title="FAQ | Zimbabwe Tour Guide — Booking, Costs & Travel Questions",
    description="Answers to common questions about booking a Zimbabwe tour, including pricing, transport, park fees, payment, and trip logistics.",
    canonical_path=canonical,
    body=body,
    extra_jsonld=faq_jsonld(),
    keywords="Zimbabwe tour FAQ, Zimbabwe travel questions, Zimbabwe booking questions",
)
write("faq.html", html)


