# -*- coding: utf-8 -*-
from build_common import page, breadcrumb, write, WHATSAPP_LINK
from icons import icon

canonical = "/contact.html"

jsonld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ContactPage","name":"Contact Zimbabwe Tour Guide"}
</script>'''

body = f'''
{breadcrumb([("Home","index.html"),("Contact", None)], canonical)}

<section class="page-hero">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">One message, a real reply</span>
    <h1>Plan Your Zimbabwe Trip</h1>
    <p>Tell us about your trip and a local guide will reply directly — usually within 24 hours.</p>
    <div class="page-hero-meta">
      <span class="pill">{icon('clock')} Replies within 24 hrs, Mon–Sat</span>
      <span class="pill">{icon('map-pin')} Based in Victoria Falls, Zimbabwe</span>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap" style="display:grid;grid-template-columns:1fr;gap:40px;">
    <div class="contact-grid" style="display:grid;grid-template-columns:1fr;gap:40px;">

      <div class="enquiry-card reveal" style="max-width:100%;">
        <h3>Tell us about your trip</h3>
        <p>To help us send a useful quote, please include your dates, number of travelers, and the destinations you want to visit.</p>
        <form id="contactForm" onsubmit="return handleFormSubmit(event, 'Thank you — we\\'ll reply within 24 hours')">
          <div class="field-row">
            <div class="field"><label for="cname">Full name</label><input id="cname" type="text" placeholder="Jane Carter" required></div>
            <div class="field"><label for="cemail">Email</label><input id="cemail" type="email" placeholder="jane@email.com" required></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="cwhatsapp">WhatsApp number</label><input id="cwhatsapp" type="tel" placeholder="+1 555 000 0000"></div>
            <div class="field"><label for="ctravelers">Number of travelers</label><input id="ctravelers" type="number" min="1" placeholder="2"></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="cdates">Travel dates</label><input id="cdates" type="text" placeholder="e.g. 12–20 September 2026"></div>
            <div class="field"><label for="cdest">Destinations interested in</label>
              <select id="cdest">
                <option>Victoria Falls</option>
                <option>Hwange National Park</option>
                <option>Great Zimbabwe</option>
                <option>Nyanga</option>
                <option>Chimanimani</option>
                <option>Harare</option>
                <option>Not sure yet / open to suggestions</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label>Need transport arranged?</label>
              <div class="radio-row">
                <label><input type="radio" name="transport" value="yes" checked> Yes</label>
                <label><input type="radio" name="transport" value="no"> No</label>
              </div>
            </div>
            <div class="field">
              <label>Need help with itinerary planning?</label>
              <div class="radio-row">
                <label><input type="radio" name="itinerary" value="yes" checked> Yes</label>
                <label><input type="radio" name="itinerary" value="no"> No</label>
              </div>
            </div>
          </div>
          <div class="field"><label for="cmsg">Tell us more about your trip</label><textarea id="cmsg" rows="4" placeholder="e.g. Celebrating an anniversary, interested in a safari plus some relaxed time at the Falls, mid-range budget"></textarea></div>
          <button type="submit" class="btn btn-primary btn-block">Send My Enquiry</button>
        </form>
        <div class="enquiry-note">{icon('shield')} No payment required to enquire. We reply with a real itinerary, not a price list.</div>
      </div>

      <div class="why-grid" style="grid-template-columns:1fr;gap:18px;">
        <div class="why-card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div class="why-icon" style="margin-bottom:0;flex-shrink:0;">{icon('whatsapp')}</div>
          <div><h4>Prefer WhatsApp?</h4><p>Message us directly for the fastest response, especially if your trip is coming up soon.</p>
          <a href="{WHATSAPP_LINK}" class="btn btn-whatsapp btn-sm" style="margin-top:10px;">Chat on WhatsApp</a></div>
        </div>
        <div class="why-card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div class="why-icon" style="margin-bottom:0;flex-shrink:0;">{icon('mail')}</div>
          <div><h4>Email</h4><p>hello@zimbabwetourguide.com — for longer questions or sending documents.</p></div>
        </div>
        <div class="why-card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div class="why-icon" style="margin-bottom:0;flex-shrink:0;">{icon('map-pin')}</div>
          <div><h4>Based in Victoria Falls, Zimbabwe</h4><p>Our team operates across all destinations covered on this site — Victoria Falls, Hwange, Great Zimbabwe, Nyanga, Chimanimani, and Harare.</p></div>
        </div>
        <div class="why-card reveal" style="display:flex;gap:16px;align-items:flex-start;">
          <div class="why-icon" style="margin-bottom:0;flex-shrink:0;">{icon('clock')}</div>
          <div><h4>Response time</h4><p>Usually within 24 hours, Monday–Saturday (Central Africa Time, UTC+2). Messages sent over the weekend are answered the following Monday.</p></div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="bg-cream tight">
  <div class="wrap-narrow text-center">
    <span class="eyebrow">Service areas</span>
    <h3 style="margin-top:10px;font-size:20px;">We plan trips across Victoria Falls, Hwange National Park, Great Zimbabwe, Nyanga, Chimanimani, and Harare</h3>
    <p style="margin-top:10px;color:var(--slate);font-size:14.5px;">Not sure which of these fits your trip? Mention "not sure yet" in the form above and we'll suggest a route.</p>
  </div>
</section>
'''

html = page(
    title="Contact Us | Zimbabwe Tour Guide — Plan Your Trip",
    description="Get in touch to plan your private Zimbabwe tour. Send your dates, group size, and destinations of interest — we reply within 24 hours with a real itinerary.",
    canonical_path=canonical,
    body=body,
    extra_jsonld=jsonld,
    keywords="contact Zimbabwe Tour Guide, book Zimbabwe tour, Zimbabwe trip enquiry",
)
write("contact.html", html)


