# -*- coding: utf-8 -*-
"""
Full body content (HTML-ready paragraphs) for each travel guide article.
Each entry provides intro + a list of (heading, paragraphs[]) sections,
plus a closing CTA framing line.
"""

ARTICLE_BODIES = {

"best-time-to-visit-zimbabwe": {
    "intro": "There's no single \"best\" time to visit Zimbabwe — there's a best time for what you specifically want to see. Water levels at Victoria Falls, wildlife concentration in the parks, and even how much you'll pay all shift dramatically across the year. Here's how the months actually break down.",
    "sections": [
        ("January – March: Green Season, Full Falls", [
            "This is Zimbabwe's wet season, and it shows. Victoria Falls runs at or near its fullest, which is spectacular but can mean heavy spray obscuring some viewpoints, particularly on the Zimbabwean side. The bush turns lush and green across the parks, which is excellent for birding but makes general wildlife harder to spot since animals don't need to cluster at waterholes.",
            "This is also the cheapest and quietest period across most lodges, which suits travelers prioritizing value and solitude over guaranteed wildlife sightings."
        ]),
        ("April – June: The Transition", [
            "Rains taper off, vegetation starts thinning, and temperatures are mild and comfortable almost everywhere. Victoria Falls is still running strong into April and May, often considered close to an ideal viewing window — full enough to be dramatic, with improving visibility.",
            "Wildlife viewing in Hwange starts improving toward the end of this window as natural water sources begin drying up."
        ]),
        ("July – October: Peak Safari Season", [
            "This is the dry season, and it's when Hwange and Zimbabwe's other parks deliver their most reliable wildlife sightings — animals concentrate predictably around the remaining waterholes. It's also when Victoria Falls' water levels drop enough for activities like Devil's Pool to become possible (typically from around August).",
            "This is peak season for a reason, which means it's also the most expensive and the most booked-up. If you're set on these months, book lodges and flights well in advance."
        ]),
        ("November – December: Building Back Up", [
            "The first rains typically arrive in November, refreshing the bush and triggering some dramatic afternoon thunderstorms. Wildlife viewing is still reasonably good early in the month before animals disperse with the new rain-fed water sources.",
            "Victoria Falls is usually at its lowest water level in late October through November, occasionally reducing to a comparative trickle on the Zimbabwean side in particularly dry years — worth checking current levels if the Falls themselves are your main priority for these specific months."
        ]),
    ],
    "closer": "If you're trying to optimize for one thing — guaranteed wildlife, full Falls, or lower prices — tell us which matters most and we'll suggest the months that actually deliver it.",
},

"victoria-falls-zambia-vs-zimbabwe-side": {
    "intro": "Victoria Falls sits on the border between Zimbabwe and Zambia, and both countries offer genuinely different experiences of the same natural wonder. Many travelers visit both — here's an honest comparison if you're deciding where to base yourself.",
    "sections": [
        ("The Zimbabwean Side", [
            "Zimbabwe holds about 75% of the Falls' width and offers the more panoramic, postcard view — this is where most of the classic Victoria Falls photographs come from. The Zimbabwean rainforest walk has 16 distinct viewpoints, giving you the full sweep of the Falls from a respectful, dry-ish distance (depending on season and spray).",
            "Victoria Falls town itself is well-developed with restaurants, curio markets, and most of the region's adventure activities — bungee jumping, the bridge walk, and most rafting operators are based here."
        ]),
        ("The Zambian Side", [
            "Zambia gets you physically closer to the edge, including the Knife-Edge Bridge walkway that puts you right beside the main falls. This side is also home to Devil's Pool and Livingstone Island, the famous (and seasonal) experience of swimming right at the lip of the Falls — only accessible from the Zambian side, and only when water levels are low enough.",
            "Livingstone, the Zambian town near the Falls, is smaller and quieter than Victoria Falls town, with a slightly different, more low-key feel."
        ]),
        ("Can You Visit Both?", [
            "Yes, easily. The KAZA UniVisa (around $50 for most nationalities) covers both Zimbabwe and Zambia and is specifically designed to allow day trips across the border to see both sides. The walk across the Victoria Falls Bridge between the two border posts takes about 15–20 minutes.",
            "Most travelers based in Victoria Falls, Zimbabwe spend a half-day crossing over to see the Zambian side, particularly if Devil's Pool is open for the season."
        ]),
    ],
    "closer": "If you can only choose one, Zimbabwe generally offers the better all-round first visit thanks to the wider views and more developed infrastructure — but if Devil's Pool is on your list, build in time for Zambia too.",
},

"hwange-vs-mana-pools": {
    "intro": "Hwange and Mana Pools are Zimbabwe's two best-known safari destinations, and they offer genuinely different experiences rather than just \"more of the same wildlife, different location.\" Here's how to decide which fits your trip.",
    "sections": [
        ("Hwange: Scale and Predictability", [
            "Hwange is Zimbabwe's largest park, and its dry-season wildlife viewing is built around reliable, pumped waterholes — meaning sightings, particularly of elephants, are close to guaranteed during the July–October peak. It's an excellent choice for first-time safari travelers or anyone who wants strong odds of consistent game viewing across a multi-day stay.",
            "Hwange is also more accessible logistically, with shorter transfer times from Victoria Falls and a wider range of accommodation standards, from budget self-catering to high-end lodges."
        ]),
        ("Mana Pools: Wilderness and Walking", [
            "Mana Pools, set along the Zambezi River floodplain, is known specifically for walking safaris — it's one of the few parks in Africa where unguided walking is even permitted for experienced visitors, though we always recommend a professional guide regardless. The walking experience here is considered among the best in southern Africa.",
            "Mana Pools tends to be more remote and harder to reach, usually requiring a light aircraft transfer, and the experience leans more toward a slower, immersive wilderness feel than Hwange's broader, more vehicle-accessible game-viewing style.",
            "Note: while Mana Pools is one of Zimbabwe's signature safari destinations, it isn't currently one of the destinations we operate guided trips to directly — we can still advise on it and connect you with trusted operators if it's central to your plans."
        ]),
        ("Which Should You Choose?", [
            "If this is your first safari, you want strong odds of big sightings, and convenient logistics matter, Hwange is the more practical choice. If you're an experienced safari traveler specifically chasing a walking-focused, more remote wilderness experience, Mana Pools is worth the extra logistics.",
            "Many longer Zimbabwe itineraries combine both — Hwange for guaranteed game viewing, followed by a Mana Pools extension for the walking experience, if time and budget allow."
        ]),
    ],
    "closer": "Tell us what kind of safari experience you're after — guaranteed sightings or remote walking wilderness — and we'll help you build the right itinerary around it.",
},

"zimbabwe-trip-cost-breakdown": {
    "intro": "\"How much does a Zimbabwe trip cost?\" doesn't have a single answer, but it does have an honest one. Here's a realistic breakdown of where your money actually goes on a typical week-long trip.",
    "sections": [
        ("International Flights", [
            "This is usually the single biggest line item and varies enormously by origin city and season. Flying into Victoria Falls or Harare from Europe or North America commonly runs from the mid-hundreds to over a thousand US dollars round-trip, with significant seasonal swings."
        ]),
        ("Accommodation", [
            "Zimbabwe spans a genuinely wide accommodation range. Budget guesthouses and self-catering camps can run $30–60 per person per night. Mid-range lodges typically sit in the $150–350 range. High-end safari lodges, particularly in Hwange, can exceed $500–800 per person per night, often on an all-inclusive basis covering meals and activities."
        ]),
        ("Park Fees and Activities", [
            "Victoria Falls park entry is a modest, fixed daily fee per nationality. National park fees for Hwange are charged per person per day and are separate from accommodation costs unless your lodge has bundled them. Adventure activities (bungee jumping, white-water rafting, helicopter flights) are priced individually, generally $50–200 each depending on the activity."
        ]),
        ("Transport Between Destinations", [
            "Road transfers between nearby destinations (Victoria Falls to Hwange, for example) are relatively affordable, often $80–150 per vehicle depending on distance and vehicle type. Domestic flights connecting more distant points (Harare to Victoria Falls, for instance) typically run $150–300 per person one-way."
        ]),
        ("A Realistic Example", [
            "A mid-range week combining 2–3 nights at Victoria Falls and 3–4 nights in Hwange, excluding international flights, commonly lands somewhere between $1,800 and $3,500 per person, depending on lodge standard and how many optional activities you add. Budget travelers can do a similar trip for considerably less; luxury travelers can easily double or triple that figure."
        ]),
    ],
    "closer": "These are realistic ranges, not a quote — send us your actual dates, group size, and the standard of comfort you want, and we'll give you real numbers rather than averages.",
},

"7-day-zimbabwe-itinerary": {
    "intro": "A week is a genuinely workable amount of time to see two of Zimbabwe's signature destinations properly, without feeling like you're constantly packing and unpacking. Here's a realistic 7-day route that we actually build for travelers.",
    "sections": [
        ("Days 1–3: Victoria Falls", [
            "Arrive at Victoria Falls Airport and settle in. Day one is a guided walk through the rainforest trail and viewpoints, plus a sunset Zambezi cruise in the evening. Day two is your choice of an adrenaline activity (white-water rafting, bungee jumping) or a more relaxed pace with a helicopter flight and time at leisure in town. Day three is a half-day cross-border visit to see the Zambian side of the Falls, if you have a KAZA UniVisa, followed by a relaxed afternoon before transferring onward."
        ]),
        ("Days 4–7: Hwange National Park", [
            "Transfer to Hwange by road (around 2 hours) or light aircraft. Days four through six follow a safari rhythm: dawn and dusk game drives, rest during the heat of the day, and one guided walking safari mixed in. Day seven is a final early-morning drive before transferring back to Victoria Falls for departure, or onward to your next destination if your trip continues."
        ]),
        ("Why This Combination Works", [
            "Victoria Falls and Hwange are close enough that transfers don't eat into your trip, but different enough in character — adventure-and-sightseeing versus immersive wildlife — that the week doesn't feel repetitive. It's the single most common 7-day combination we plan, for good reason."
        ]),
        ("Alternative: Add the Eastern Highlands", [
            "If wildlife and waterfalls aren't your only interest, some travelers swap a day or two of Hwange for a short Harare stopover plus a 2-day Nyanga add-on, trading some safari time for cooler mountain air and hiking. This requires a domestic flight connection through Harare, so it suits travelers less pressed for time."
        ]),
    ],
    "closer": "This itinerary is a realistic starting point, not a fixed package — every detail adjusts to your actual dates, interests, and pace once you enquire.",
},

"zimbabwe-visa-entry-requirements": {
    "intro": "Visa requirements for Zimbabwe are more straightforward than many travelers expect, but it's worth knowing your options before you arrive. Here's what most nationalities actually need.",
    "sections": [
        ("Visa on Arrival", [
            "Most international visitors, including travelers from the UK, US, EU, Canada, and Australia, can obtain a visa on arrival at Victoria Falls Airport, Harare's Robert Gabriel Mugabe International Airport, or major land border posts. Single-entry visas typically cost around $30–75 depending on nationality, payable in US dollars cash."
        ]),
        ("The KAZA UniVisa", [
            "If your trip includes crossing into Zambia (for example, to see the Zambian side of Victoria Falls) or Botswana via the relevant border post, the KAZA UniVisa is worth getting instead of a standard single-entry visa. Priced around $50 for most nationalities, it covers unlimited entries between Zimbabwe and Zambia for 30 days, including day trips across the border."
        ]),
        ("What to Bring", [
            "A passport valid for at least six months beyond your travel dates, with at least one blank page. Visa fees are most reliably paid in US dollars cash — card payment exists at some entry points but isn't guaranteed to work, so cash remains the safer bet.",
            "It's worth double-checking current requirements for your specific nationality before traveling, since rules and fees are occasionally updated."
        ]),
        ("E-Visa Option", [
            "Zimbabwe also offers an online e-visa application system for travelers who prefer to arrange things before departure rather than on arrival. Processing typically takes a few business days, so apply with some lead time if you choose this route."
        ]),
    ],
    "closer": "If you're unsure which visa option suits your specific itinerary — especially if Zambia or Botswana are part of your plans — tell us your route and we'll point you toward the right one.",
},

"is-zimbabwe-safe-to-visit": {
    "intro": "This is one of the most common questions we get, and it deserves a straight answer rather than either blind reassurance or vague hedging. Here's an honest, practical answer from people who live and work here.",
    "sections": [
        ("The Short Answer", [
            "Yes, Zimbabwe's tourist regions — Victoria Falls, Hwange, Great Zimbabwe, the Eastern Highlands, and Harare's main areas — see millions of international visitors a year with very low rates of traveler-targeted crime. The tourism industry is a major part of the economy, and the areas visitors actually go are correspondingly well looked after."
        ]),
        ("What Actually Matters Day to Day", [
            "Normal city precautions apply in Harare and Bulawayo, the same as any city: avoid displaying valuables carelessly, use arranged transport after dark rather than walking unfamiliar areas, and keep copies of important documents. In safari areas, the relevant safety considerations are wildlife-related, not crime-related — following your guide's instructions around animals matters far more than anything else.",
            "Road safety is worth a specific mention: rural roads can have potholes, occasional wildlife crossings, and limited lighting at night, which is part of why we generally recommend arranged transport or experienced local drivers for longer road transfers rather than self-driving unfamiliar routes after dark."
        ]),
        ("Health and Practical Considerations", [
            "Malaria risk exists in lower-lying areas including Victoria Falls and Hwange, so prophylaxis is worth discussing with a travel doctor before your trip. Tap water in major towns is generally treated, though bottled water is the safer default, particularly in more rural areas. Travel insurance covering medical evacuation is genuinely worth having, especially for safari and trekking-focused trips."
        ]),
        ("Currency and Cash", [
            "Zimbabwe operates largely on US dollars for tourism transactions, which simplifies budgeting for international visitors. Carrying a reasonable amount of small-denomination cash is useful, particularly for markets, tips, and rural areas where card payment isn't always reliable."
        ]),
    ],
    "closer": "If you have specific safety questions about your particular itinerary or personal circumstances, ask us directly — we'd rather give you a real answer than a generic reassurance.",
},

"what-to-pack-for-a-zimbabwe-safari": {
    "intro": "Packing for a Zimbabwe safari is mostly about practicality, not gear obsession. Here's what actually matters, based on what we see travelers wish they'd brought (or left at home).",
    "sections": [
        ("Clothing", [
            "Neutral colours — khaki, olive, brown, grey — are genuinely useful for game drives, since bright colours and stark white can be more visible to wildlife and show dust quickly. Layers matter more than most people expect: dry-season mornings on a game drive can be genuinely cold, even when afternoons are warm.",
            "Long sleeves and trousers in lightweight fabric help with both sun and insect protection during dawn and dusk drives, when mosquitoes are most active."
        ]),
        ("Footwear", [
            "Comfortable closed shoes for game drives and camp walking; proper hiking boots if your trip includes Nyanga or Chimanimani. Avoid packing only sandals — even relaxed safari days involve more walking around camp and lodge grounds than people expect."
        ]),
        ("Practical Extras", [
            "Binoculars, if you have a pair — most camps provide some, but having your own means you're not sharing during a good sighting. A dry bag or waterproof pouch if your trip includes Victoria Falls, where spray reaches the walking trails. A reliable insect repellent, particularly for evenings in lower-lying safari areas.",
            "A basic first-aid kit with anything personal you might need — pharmacies in remote safari areas are limited, even though Harare and Victoria Falls town have reasonable options."
        ]),
        ("What You Probably Don't Need", [
            "Heavy camouflage-pattern clothing isn't necessary for civilian safari travel and is, in some African countries, actually restricted for visitors to wear. A full specialist safari wardrobe also isn't required — comfortable, practical clothing in muted tones covers nearly everything."
        ]),
    ],
    "closer": "We send every traveler a packing list tailored to their specific itinerary once a trip is confirmed, since a Victoria Falls and Hwange trip and a Chimanimani trek genuinely need different gear.",
},

"great-zimbabwe-history-explained": {
    "intro": "Great Zimbabwe is the largest pre-colonial stone structure in sub-Saharan Africa, and it's also the source of the country's name. Here's the history behind the ruins, explained in plain terms.",
    "sections": [
        ("Origins: An 11th-Century Beginning", [
            "Construction at Great Zimbabwe is believed to have begun around the 11th century, built by ancestors of the modern Shona people. The site grew over the following centuries into the political and economic capital of a major trading kingdom."
        ]),
        ("Peak Power: 13th to 15th Centuries", [
            "At its height, Great Zimbabwe was home to an estimated 18,000 people, making it one of the largest urban centres in sub-Saharan Africa at the time. The city sat at the centre of a trading network that reached as far as the East African coast, exchanging gold and ivory for goods including Chinese porcelain and glass beads from as far afield as the Middle East and Persia — artefacts of which have been found on site."
        ]),
        ("The Architecture Itself", [
            "What makes the site remarkable is its construction technique: dry-stone walling, meaning the granite blocks are stacked and shaped to fit without any mortar binding them. The Great Enclosure, the site's most famous structure, stands up to 11 metres high with walls roughly 5 metres thick at points, and has remained structurally intact for some 700 years."
        ]),
        ("Decline and Legacy", [
            "The city was largely abandoned by the 15th century, likely due to a combination of factors including resource depletion and shifting trade routes, with successor states emerging elsewhere in the region. The site remained significant in local oral history and was \"rediscovered\" by European explorers in the 19th century, though local communities had never lost knowledge of its existence or significance.",
            "The country took its modern name from this site at independence in 1980 — \"Zimbabwe\" derives from the Shona phrase generally translated as \"houses of stone.\" The carved soapstone Zimbabwe Birds found at the ruins remain a national symbol, appearing on the country's flag and currency."
        ]),
    ],
    "closer": "Visiting with a guide who can walk you through this history on-site turns the ruins from impressive stonework into a genuinely understood ancient city — it's the difference our Great Zimbabwe tour is built around.",
},

}

# ---------------------------------------------------------------------------
# Merge in all phase batches + viral content into one master ARTICLE_BODIES dict
# ---------------------------------------------------------------------------
from data_articles_phase1 import PHASE1_NEW
from data_articles_phase2 import PHASE2_NEW
from data_articles_phase3 import PHASE3_NEW
from data_articles_phase4 import PHASE4_NEW
from data_viral import VIRAL_BODIES

ARTICLE_BODIES.update(PHASE1_NEW)
ARTICLE_BODIES.update(PHASE2_NEW)
ARTICLE_BODIES.update(PHASE3_NEW)
ARTICLE_BODIES.update(PHASE4_NEW)
ARTICLE_BODIES.update(VIRAL_BODIES)


