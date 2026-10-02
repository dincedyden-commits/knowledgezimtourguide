# -*- coding: utf-8 -*-
"""
Internal linking rules for every article: each must link to
>=1 destination, >=1 tour, and 2-3 related articles (plus contact CTA, always present in template).
"""

ARTICLE_LINKS = {
    # ---- Phase 1 ----
    "best-time-to-visit-zimbabwe": {"dest": ["victoria-falls", "hwange"], "tours": ["victoria-falls-day-tour", "hwange-safari-experience"], "related": ["is-zimbabwe-safe-to-visit", "5-day-zimbabwe-itinerary", "victoria-falls-high-water-season"]},
    "is-zimbabwe-safe-to-visit": {"dest": ["harare", "hwange"], "tours": ["custom-zimbabwe-tour"], "related": ["zimbabwe-travel-mistakes-to-avoid", "what-to-expect-on-a-zimbabwe-road-trip", "zimbabwe-visa-entry-requirements"]},
    "zimbabwe-trip-cost-breakdown": {"dest": ["victoria-falls", "hwange"], "tours": ["custom-zimbabwe-tour"], "related": ["zimbabwe-safari-budget-guide", "zimbabwe-currency-guide", "private-tour-vs-self-drive"]},
    "zimbabwe-visa-entry-requirements": {"dest": ["victoria-falls", "harare"], "tours": ["victoria-falls-day-tour"], "related": ["zimbabwe-currency-guide", "is-zimbabwe-safe-to-visit", "what-to-pack-for-a-zimbabwe-safari"]},
    "zimbabwe-currency-guide": {"dest": ["victoria-falls", "harare"], "tours": ["custom-zimbabwe-tour"], "related": ["zimbabwe-trip-cost-breakdown", "zimbabwe-visa-entry-requirements", "zimbabwe-safari-budget-guide"]},
    "what-to-pack-for-a-zimbabwe-safari": {"dest": ["hwange", "victoria-falls"], "tours": ["hwange-safari-experience", "victoria-falls-day-tour"], "related": ["best-time-to-visit-zimbabwe", "zimbabwe-travel-mistakes-to-avoid", "hwange-national-park-safari-guide"]},
    "victoria-falls-first-time-visitors-guide": {"dest": ["victoria-falls"], "tours": ["victoria-falls-day-tour"], "related": ["victoria-falls-zambia-vs-zimbabwe-side", "things-to-do-in-victoria-falls-besides-the-falls", "3-day-victoria-falls-itinerary"]},
    "hwange-national-park-safari-guide": {"dest": ["hwange"], "tours": ["hwange-safari-experience"], "related": ["hwange-vs-mana-pools", "zimbabwe-safari-budget-guide", "best-safari-lodges-near-hwange"]},
    "great-zimbabwe-ruins-travel-guide": {"dest": ["great-zimbabwe"], "tours": ["great-zimbabwe-historical-tour"], "related": ["great-zimbabwe-history-explained", "how-many-days-do-you-need-in-zimbabwe", "zimbabwe-road-trip-bucket-list"]},
    "5-day-zimbabwe-itinerary": {"dest": ["victoria-falls", "hwange"], "tours": ["custom-zimbabwe-tour", "hwange-safari-experience"], "related": ["how-many-days-do-you-need-in-zimbabwe", "best-time-to-visit-zimbabwe", "7-day-zimbabwe-itinerary"]},

    # ---- Phase 2 ----
    "nyanga-travel-guide": {"dest": ["nyanga"], "tours": ["nyanga-highlands-escape"], "related": ["chimanimani-travel-guide", "what-to-pack-for-a-zimbabwe-safari", "hidden-gems-in-zimbabwe"]},
    "chimanimani-travel-guide": {"dest": ["chimanimani"], "tours": ["chimanimani-adventure"], "related": ["nyanga-travel-guide", "hidden-gems-in-zimbabwe", "what-to-expect-on-a-zimbabwe-road-trip"]},
    "harare-travel-guide": {"dest": ["harare"], "tours": ["custom-zimbabwe-tour"], "related": ["harare-to-victoria-falls-travel", "bulawayo-travel-guide", "zimbabwe-currency-guide"]},
    "bulawayo-travel-guide": {"dest": ["great-zimbabwe"], "tours": ["great-zimbabwe-historical-tour", "custom-zimbabwe-tour"], "related": ["harare-travel-guide", "zimbabwe-road-trip-bucket-list", "most-underrated-places-in-zimbabwe"]},
    "harare-to-victoria-falls-travel": {"dest": ["harare", "victoria-falls"], "tours": ["custom-zimbabwe-tour"], "related": ["how-many-days-do-you-need-in-zimbabwe", "what-to-expect-on-a-zimbabwe-road-trip", "harare-travel-guide"]},
    "how-many-days-do-you-need-in-zimbabwe": {"dest": ["victoria-falls", "hwange"], "tours": ["custom-zimbabwe-tour"], "related": ["5-day-zimbabwe-itinerary", "7-day-zimbabwe-itinerary", "how-to-plan-a-custom-zimbabwe-tour"]},

    # ---- Phase 3 ----
    "zimbabwe-safari-budget-guide": {"dest": ["hwange"], "tours": ["hwange-safari-experience"], "related": ["zimbabwe-trip-cost-breakdown", "best-safari-lodges-near-hwange", "victoria-falls-vs-hwange"]},
    "victoria-falls-vs-hwange": {"dest": ["victoria-falls", "hwange"], "tours": ["victoria-falls-day-tour", "hwange-safari-experience"], "related": ["safari-vs-victoria-falls-which-to-prioritize", "5-day-zimbabwe-itinerary", "how-many-days-do-you-need-in-zimbabwe"]},
    "private-tour-vs-self-drive": {"dest": ["hwange"], "tours": ["custom-zimbabwe-tour"], "related": ["visit-zimbabwe-without-a-tour-guide", "what-to-expect-on-a-zimbabwe-road-trip", "zimbabwe-travel-mistakes-to-avoid"]},
    "best-zimbabwe-destinations-for-couples": {"dest": ["victoria-falls", "nyanga"], "tours": ["custom-zimbabwe-tour"], "related": ["best-zimbabwe-honeymoon-spots", "nyanga-travel-guide", "best-lodges-near-victoria-falls"]},
    "family-friendly-places-in-zimbabwe": {"dest": ["victoria-falls", "hwange"], "tours": ["victoria-falls-day-tour", "hwange-safari-experience"], "related": ["what-to-pack-for-a-zimbabwe-safari", "is-zimbabwe-safe-to-visit", "how-many-days-do-you-need-in-zimbabwe"]},
    "what-to-expect-on-a-zimbabwe-road-trip": {"dest": ["chimanimani", "nyanga"], "tours": ["custom-zimbabwe-tour"], "related": ["zimbabwe-road-trip-bucket-list", "private-tour-vs-self-drive", "harare-to-victoria-falls-travel"]},

    # ---- Phase 4 ----
    "best-lodges-near-victoria-falls": {"dest": ["victoria-falls"], "tours": ["victoria-falls-day-tour"], "related": ["victoria-falls-first-time-visitors-guide", "3-day-victoria-falls-itinerary", "best-zimbabwe-destinations-for-couples"]},
    "best-safari-lodges-near-hwange": {"dest": ["hwange"], "tours": ["hwange-safari-experience"], "related": ["hwange-national-park-safari-guide", "zimbabwe-safari-budget-guide", "hwange-vs-mana-pools"]},
    "7-day-zimbabwe-itinerary": {"dest": ["victoria-falls", "hwange"], "tours": ["hwange-safari-experience", "victoria-falls-day-tour"], "related": ["5-day-zimbabwe-itinerary", "how-many-days-do-you-need-in-zimbabwe", "zimbabwe-safari-budget-guide"]},
    "3-day-victoria-falls-itinerary": {"dest": ["victoria-falls"], "tours": ["victoria-falls-day-tour"], "related": ["victoria-falls-first-time-visitors-guide", "things-to-do-in-victoria-falls-besides-the-falls", "best-lodges-near-victoria-falls"]},
    "things-to-do-in-victoria-falls-besides-the-falls": {"dest": ["victoria-falls"], "tours": ["victoria-falls-day-tour"], "related": ["victoria-falls-first-time-visitors-guide", "3-day-victoria-falls-itinerary", "victoria-falls-high-water-season"]},
    "how-to-plan-a-custom-zimbabwe-tour": {"dest": ["victoria-falls", "hwange", "great-zimbabwe", "nyanga", "chimanimani", "harare"], "tours": ["custom-zimbabwe-tour"], "related": ["how-many-days-do-you-need-in-zimbabwe", "zimbabwe-safari-budget-guide", "private-tour-vs-self-drive"]},
    "zimbabwe-travel-mistakes-to-avoid": {"dest": ["hwange"], "tours": ["custom-zimbabwe-tour"], "related": ["first-time-zimbabwe-traveler-mistakes", "zimbabwe-currency-guide", "what-to-expect-on-a-zimbabwe-road-trip"]},
    "visit-zimbabwe-without-a-tour-guide": {"dest": ["victoria-falls", "hwange"], "tours": ["custom-zimbabwe-tour"], "related": ["private-tour-vs-self-drive", "what-to-expect-on-a-zimbabwe-road-trip", "zimbabwe-travel-mistakes-to-avoid"]},

    # ---- Extras ----
    "victoria-falls-zambia-vs-zimbabwe-side": {"dest": ["victoria-falls"], "tours": ["victoria-falls-day-tour"], "related": ["victoria-falls-first-time-visitors-guide", "victoria-falls-high-water-season", "zimbabwe-visa-entry-requirements"]},
    "great-zimbabwe-history-explained": {"dest": ["great-zimbabwe"], "tours": ["great-zimbabwe-historical-tour"], "related": ["great-zimbabwe-ruins-travel-guide", "bulawayo-travel-guide", "zimbabwe-road-trip-bucket-list"]},
    "hwange-vs-mana-pools": {"dest": ["hwange"], "tours": ["hwange-safari-experience"], "related": ["hwange-national-park-safari-guide", "best-safari-lodges-near-hwange", "victoria-falls-vs-hwange"]},

    # ---- Viral ----
    "beautiful-places-to-visit-in-zimbabwe": {"dest": ["victoria-falls", "hwange", "great-zimbabwe"], "tours": ["custom-zimbabwe-tour"], "related": ["zimbabwe-views-that-dont-look-real", "hidden-gems-in-zimbabwe", "zimbabwe-road-trip-bucket-list"]},
    "zimbabwe-views-that-dont-look-real": {"dest": ["victoria-falls", "chimanimani"], "tours": ["custom-zimbabwe-tour"], "related": ["beautiful-places-to-visit-in-zimbabwe", "photos-that-will-make-you-want-to-visit-zimbabwe", "victoria-falls-high-water-season"]},
    "victoria-falls-high-water-season": {"dest": ["victoria-falls"], "tours": ["victoria-falls-day-tour"], "related": ["best-time-to-visit-zimbabwe", "victoria-falls-zambia-vs-zimbabwe-side", "victoria-falls-first-time-visitors-guide"]},
    "zimbabwe-road-trip-bucket-list": {"dest": ["nyanga", "chimanimani", "great-zimbabwe"], "tours": ["custom-zimbabwe-tour"], "related": ["what-to-expect-on-a-zimbabwe-road-trip", "hidden-gems-in-zimbabwe", "harare-to-victoria-falls-travel"]},
    "hidden-gems-in-zimbabwe": {"dest": ["nyanga", "chimanimani"], "tours": ["custom-zimbabwe-tour"], "related": ["most-underrated-places-in-zimbabwe", "nyanga-travel-guide", "chimanimani-travel-guide"]},
    "best-zimbabwe-honeymoon-spots": {"dest": ["victoria-falls", "nyanga"], "tours": ["custom-zimbabwe-tour"], "related": ["best-zimbabwe-destinations-for-couples", "best-lodges-near-victoria-falls", "nyanga-travel-guide"]},
    "most-underrated-places-in-zimbabwe": {"dest": ["nyanga", "chimanimani", "harare"], "tours": ["custom-zimbabwe-tour"], "related": ["hidden-gems-in-zimbabwe", "bulawayo-travel-guide", "zimbabwe-road-trip-bucket-list"]},
    "safari-vs-victoria-falls-which-to-prioritize": {"dest": ["victoria-falls", "hwange"], "tours": ["victoria-falls-day-tour", "hwange-safari-experience"], "related": ["victoria-falls-vs-hwange", "how-many-days-do-you-need-in-zimbabwe", "5-day-zimbabwe-itinerary"]},
    "first-time-zimbabwe-traveler-mistakes": {"dest": ["victoria-falls", "hwange"], "tours": ["custom-zimbabwe-tour"], "related": ["zimbabwe-travel-mistakes-to-avoid", "zimbabwe-currency-guide", "zimbabwe-visa-entry-requirements"]},
    "photos-that-will-make-you-want-to-visit-zimbabwe": {"dest": ["victoria-falls", "hwange", "great-zimbabwe"], "tours": ["custom-zimbabwe-tour"], "related": ["beautiful-places-to-visit-in-zimbabwe", "zimbabwe-views-that-dont-look-real", "zimbabwe-road-trip-bucket-list"]},
}


