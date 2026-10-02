# -*- coding: utf-8 -*-
from build_common import page, breadcrumb, write
from icons import icon

LEGAL_PAGES = {

"privacy-policy": {
    "title": "Privacy Policy",
    "meta_title": "Privacy Policy | Zimbabwe Tour Guide",
    "meta_description": "How Zimbabwe Tour Guide collects, uses, and protects the personal information you share when enquiring about or booking a trip.",
    "sections": [
        ("Introduction", ["This Privacy Policy explains how Zimbabwe Tour Guide (\"we\", \"us\", \"our\") collects, uses, and protects personal information when you use this website, submit an enquiry, or book a tour with us. By using this site, you agree to the practices described here."]),
        ("Information We Collect", [
            "When you submit an enquiry or booking form, we collect the information you provide directly, which may include your name, email address, WhatsApp or phone number, travel dates, number of travelers, destinations of interest, and any details you share about your trip preferences.",
            "We do not collect payment card information through this website. Any payment processing for confirmed bookings is handled through separate, secure channels communicated directly with you."
        ]),
        ("How We Use Your Information", [
            "We use the information you provide to respond to your enquiry, prepare and send trip itineraries and quotes, communicate with you about a confirmed booking, and improve the trips and information we offer. We do not sell or rent your personal information to third parties.",
            "We may share necessary details (such as your name and travel dates) with accommodation providers, transport operators, or other tour partners directly involved in delivering your booked trip."
        ]),
        ("Cookies and Analytics", ["This website may use standard analytics tools to understand how visitors use the site, which helps us improve content and navigation. These tools typically collect anonymized or aggregated data such as page views and general location, rather than personally identifying information."]),
        ("Data Retention", ["We retain enquiry and booking information for as long as reasonably necessary to respond to your request, deliver a booked trip, and comply with any applicable record-keeping obligations."]),
        ("Your Rights", ["You may ask us at any time to confirm what personal information we hold about you, to correct inaccurate information, or to request that we delete information that is no longer needed for the purposes described above. Contact us using the details on our Contact page to make such a request."]),
        ("Changes to This Policy", ["We may update this Privacy Policy from time to time to reflect changes in our practices. The \"last updated\" date at the top of this page will reflect the most recent revision."]),
    ],
},

"terms-and-conditions": {
    "title": "Terms & Conditions",
    "meta_title": "Terms & Conditions | Zimbabwe Tour Guide",
    "meta_description": "The terms and conditions that apply when you enquire about, book, or travel on a tour arranged through Zimbabwe Tour Guide.",
    "sections": [
        ("Introduction", ["These Terms &amp; Conditions govern your use of this website and any tour, trip planning service, or itinerary booked through Zimbabwe Tour Guide. By submitting an enquiry or confirming a booking, you agree to these terms."]),
        ("Enquiries and Quotes", ["Submitting an enquiry through this website does not constitute a booking. Itineraries and quotes provided in response to an enquiry are estimates based on the information you provide and are subject to change based on availability, exchange rates, and final trip details, until a booking is formally confirmed."]),
        ("Booking Confirmation", ["A booking is considered confirmed once we have received written confirmation from you and any required deposit has been received, as communicated directly with you for your specific trip. Confirmed bookings will include a final itinerary and total cost breakdown."]),
        ("Traveler Responsibilities", [
            "Travelers are responsible for ensuring they hold valid travel documents, including passports and any required visas, and for arranging adequate travel insurance covering their planned activities.",
            "Travelers participating in safari, hiking, or adventure activities are expected to follow the instructions of their guide at all times, including instructions related to wildlife safety and activity-specific precautions."
        ]),
        ("Changes and Availability", ["Accommodation, activities, and transport arrangements are subject to availability and may occasionally need to be substituted with a comparable alternative due to circumstances beyond our control, such as weather, park closures, or operator availability. We will communicate any such changes as soon as reasonably possible."]),
        ("Limitation of Liability", ["Zimbabwe Tour Guide acts as a planner and coordinator of services provided by third parties, including lodges, transport operators, and activity providers. While we carefully select the partners we work with, we are not liable for circumstances beyond our reasonable control, including but not limited to weather events, wildlife encounters, political developments, or third-party service failures."]),
        ("Governing Law", ["These terms are governed by the laws of Zimbabwe. Any disputes arising from a booking will first be addressed through direct communication between the parties before pursuing other resolution avenues."]),
    ],
},

"refund-cancellation-policy": {
    "title": "Refund & Cancellation Policy",
    "meta_title": "Refund & Cancellation Policy | Zimbabwe Tour Guide",
    "meta_description": "Our policy on deposits, cancellations, and refunds for tours booked through Zimbabwe Tour Guide.",
    "sections": [
        ("Overview", ["This policy outlines how deposits, cancellations, and refunds are handled for trips booked through Zimbabwe Tour Guide. Specific terms for your booking will always be confirmed in writing as part of your final itinerary and quote, since some accommodation and activity providers apply their own, separate cancellation terms."]),
        ("Deposits", ["A deposit is typically required to confirm a booking, with the amount depending on the specific lodges, activities, and season involved in your itinerary. No deposit is required simply to receive a draft itinerary or quote."]),
        ("Cancellations by the Traveler", [
            "Cancellations made well in advance of travel dates are generally eligible for a partial refund of the deposit, minus any non-refundable costs already committed to third-party providers (such as lodge deposits or activity bookings) on your behalf.",
            "Cancellations made close to the travel date are less likely to be refundable, as most lodges and operators in Zimbabwe apply strict cancellation windows of their own, particularly during peak season. We will always disclose the specific cancellation terms tied to your itinerary before you confirm a booking."
        ]),
        ("Cancellations or Changes by Us", ["In the rare event that we need to cancel or substantially change a confirmed booking due to circumstances beyond our control, we will offer either a comparable alternative itinerary or a refund of amounts not already committed to third-party providers."]),
        ("Force Majeure", ["Neither party is liable for failure to perform obligations due to circumstances beyond reasonable control, including natural disasters, government action, park or border closures, or other similar events. In such cases, we will work with you in good faith on rescheduling or partial refunds where recoverable from our partners."]),
        ("How to Request a Cancellation", ["To cancel or amend a booking, contact us directly through the details on our Contact page as early as possible. Earlier notice generally allows for a more favorable outcome given third-party provider deadlines."]),
    ],
},

"disclaimer": {
    "title": "Disclaimer",
    "meta_title": "Disclaimer | Zimbabwe Tour Guide",
    "meta_description": "Important disclaimers regarding travel risk, third-party services, and the information provided on the Zimbabwe Tour Guide website.",
    "sections": [
        ("General Information", ["The content on this website, including destination guides, itineraries, and travel guide articles, is provided for general informational purposes to help travelers plan a trip to Zimbabwe. While we make every effort to keep this information accurate and current, travel conditions, prices, regulations, and availability can change without notice."]),
        ("Travel and Activity Risk", ["Travel to Zimbabwe, including safari activities, wildlife viewing, hiking, and adventure activities such as white-water rafting or bungee jumping, carries inherent risks. Travelers participate in such activities at their own risk and are strongly encouraged to hold travel insurance that covers their specific planned activities."]),
        ("Wildlife Encounters", ["Wildlife sightings, behavior, and proximity cannot be guaranteed or controlled, and all wildlife should be treated as potentially dangerous. Travelers must follow guide instructions at all times during game drives, walking safaris, and any wildlife-adjacent activity."]),
        ("Third-Party Services", ["Zimbabwe Tour Guide coordinates services provided by independent third parties, including lodges, transport operators, and activity providers. We carefully select the partners we work with, but we do not control their day-to-day operations and are not responsible for circumstances arising from their independent actions."]),
        ("External Links", ["This website may reference or link to external resources for additional context. We are not responsible for the content or accuracy of external websites."]),
        ("No Professional Advice", ["Information provided on this website, including visa, health, and safety guidance, is general in nature and should not be treated as a substitute for official government, medical, or insurance advice specific to your circumstances and nationality."]),
    ],
},

}


def render_sections(sections):
    out = []
    for heading, paras in sections:
        out.append(f'<h2>{heading}</h2>')
        for p in paras:
            out.append(f'<p>{p}</p>')
    return "".join(out)


def build_legal_page(slug, data):
    canonical = f"/legal/{slug}.html"
    body = f'''
{breadcrumb([("Home","index.html"),("Legal", None),(data['title'], None)], canonical)}

<section class="page-hero" style="padding:40px 0 44px;">
  <div class="wrap" style="position:relative;z-index:2;">
    <span class="eyebrow on-dark">Legal</span>
    <h1>{data['title']}</h1>
  </div>
</section>

<section class="bg-white">
  <div class="wrap-narrow legal-content">
    <span class="legal-updated">Last updated: June 2026</span>
    {render_sections(data['sections'])}
    <p style="margin-top:30px;">Questions about this policy? <a href="../contact.html" style="color:var(--green-deep);font-weight:700;">Contact us</a> and we'll clarify anything that isn't clear.</p>
  </div>
</section>
'''
    html = page(
        title=data['meta_title'],
        description=data['meta_description'],
        canonical_path=canonical,
        body=body,
        keywords=f"Zimbabwe Tour Guide {data['title'].lower()}",
    )
    write(f"legal/{slug}.html", html)


if __name__ == "__main__":
    for slug, data in LEGAL_PAGES.items():
        build_legal_page(slug, data)


