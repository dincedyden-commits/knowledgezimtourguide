# -*- coding: utf-8 -*-
"""
Small icon set (stroke-style, matches homepage) + decorative scene SVGs
used across destination/tour cards, galleries, and quick-facts blocks.
"""

ICONS = {
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l-5 2V6l5-2 6 2 5-2v14l-5 2-6-2z"/><path d="M9 4v14M15 6v14"/></svg>',
    "map-pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "plane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.6 21l2-6.6L3 11l1-1.6 9.7.6L17.3 3l2 .6-2.3 8.4 6 3.4-.5 1.8-6.7-1.4-2 6.6z"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H7a4 4 0 00-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M22 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>',
    "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 17h14M5 17a2 2 0 01-2-2v-2l2-5h14l2 5v2a2 2 0 01-2 2M5 17a2 2 0 002 2h0a2 2 0 002-2M17 17a2 2 0 002 2h0a2 2 0 002-2"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8l-3 6-5 2 3-6z"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12l5 5L20 7"/></svg>',
    "cross": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M18 6L6 18M6 6l12 12"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "chevron-down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M6 9l6 6 6-6"/></svg>',
    "plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M12 5v14M5 12h14"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4.5 8-11V5l-8-3-8 3v6c0 6.5 8 11 8 11z"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6l9 7 9-7M3 6v12h18V6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.13.96.36 1.9.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0122 16.92z"/></svg>',
    "clock-reply": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
    "star-shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9 9 4.03 9 9z"/></svg>',
    "binoculars": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="7" cy="16" r="3"/><circle cx="17" cy="16" r="3"/><path d="M10 16h4M9 9l1.5 4M15 9l-1.5 4M9 9h6l1 -5h-8z"/></svg>',
    "mountain": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 20l6-10 4 6 2-3 6 7z"/></svg>',
    "footprints": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 16c0-3 2-5 2-8s-1-3-2-3-2 1-2 3c0 1 .5 2 .5 2M8 21c1-2-1-4-1-7s2-5 2-8 1-3 2-3 2 1 2 3-1 2-1 3"/></svg>',
}


def icon(name, cls=""):
    svg = ICONS.get(name, ICONS["compass"])
    if cls:
        return svg.replace("<svg ", f'<svg class="{cls}" ', 1)
    return svg


# --- Decorative SVG "scene" cards (no stock photos; consistent hand-built illustration style) ---

def scene_svg(palette="green", motif="hills"):
    """
    palette: green | gold | terracotta | forest | dusk
    motif:   hills | falls | savanna | ruins | mountains | river | city
    Returns a self-contained SVG string sized for a 300x168 (or similar) card slot.
    """
    palettes = {
        "green":      ("#3A8067", "#143226"),
        "gold":       ("#D4A017", "#7A5410"),
        "forest":     ("#4F8C6E", "#0F2A1F"),
        "terracotta": ("#B45F2E", "#5C2E12"),
        "dusk":       ("#2A6B4F", "#0A1A13"),
        "slate":      ("#6B7280", "#1F2937"),
    }
    top, bottom = palettes.get(palette, palettes["green"])
    uid = f"{palette}{motif}"

    base = f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="{top}"/><stop offset="100%" stop-color="{bottom}"/></linearGradient></defs><rect width="300" height="168" fill="url(#{uid})"/>'

    if motif == "falls":
        body = '''<path d="M0 110 Q70 80 150 105 T300 95 V168 H0Z" fill="#1F4D3A" opacity="0.7"/>
        <rect x="120" y="40" width="8" height="90" fill="#E8F4FF" opacity="0.85"/>
        <rect x="135" y="35" width="6" height="95" fill="#E8F4FF" opacity="0.7"/>
        <rect x="148" y="45" width="7" height="85" fill="#E8F4FF" opacity="0.8"/>
        <ellipse cx="135" cy="135" rx="80" ry="12" fill="#fff" opacity="0.15"/>'''
    elif motif == "savanna":
        body = '''<circle cx="230" cy="40" r="26" fill="#FBE9B0" opacity="0.6"/>
        <path d="M0 120 Q90 95 160 115 T300 105 V168 H0Z" fill="#1F4D3A"/>
        <g transform="translate(60,95)"><ellipse cx="0" cy="20" rx="20" ry="6" fill="#0F2A1F"/><path d="M0 20 L2 -10" stroke="#0F2A1F" stroke-width="3"/></g>
        <g transform="translate(110,105) scale(0.8)"><ellipse cx="0" cy="20" rx="20" ry="6" fill="#0F2A1F"/><path d="M0 20 L2 -10" stroke="#0F2A1F" stroke-width="3"/></g>'''
    elif motif == "river":
        body = '''<path d="M0 100 Q80 130 160 100 T300 115 V168 H0Z" fill="#1F4D3A" opacity="0.65"/>
        <path d="M40 130 Q150 110 280 135" stroke="#9BD7C4" stroke-width="3" fill="none" opacity="0.5"/>'''
    elif motif == "ruins":
        body = '''<rect x="100" y="60" width="100" height="70" fill="#3C2A1A" opacity="0.7"/>
        <rect x="120" y="80" width="60" height="50" fill="#2A1C10" opacity="0.6"/>
        <path d="M0 140 Q100 120 200 140 T300 130 V168 H0Z" fill="#1F4D3A" opacity="0.5"/>'''
    elif motif == "mountains":
        body = '''<path d="M0 130 L60 60 L100 100 L150 40 L200 95 L250 70 L300 110 V168 H0Z" fill="#143226" opacity="0.8"/>
        <path d="M150 40 L160 55 L140 55 Z" fill="#fff" opacity="0.5"/>
        <path d="M0 150 Q100 140 200 150 T300 145 V168 H0Z" fill="#0F2A1F"/>'''
    elif motif == "city":
        body = '''<rect x="40" y="80" width="22" height="60" fill="#0F2A1F" opacity="0.7"/>
        <rect x="70" y="60" width="26" height="80" fill="#0F2A1F" opacity="0.8"/>
        <rect x="105" y="90" width="20" height="50" fill="#0F2A1F" opacity="0.6"/>
        <rect x="200" y="50" width="24" height="90" fill="#0F2A1F" opacity="0.85"/>
        <rect x="232" y="75" width="20" height="65" fill="#0F2A1F" opacity="0.6"/>
        <path d="M0 150 Q150 140 300 150 V168 H0Z" fill="#143226"/>'''
    elif motif == "trek":
        body = '''<path d="M0 140 L50 70 L90 110 L140 50 L190 105 L240 75 L300 120 V168 H0Z" fill="#0A1A13" opacity="0.85"/>
        <circle cx="140" cy="50" r="9" fill="#fff" opacity="0.6"/>'''
    else:  # hills
        body = '''<path d="M0 110 Q70 80 150 105 T300 95 V168 H0Z" fill="#2A6B4F" opacity="0.55"/>
        <path d="M0 130 Q120 110 240 130 T300 120 V168 H0Z" fill="#143226" opacity="0.6"/>
        <g transform="translate(150,80)" opacity="0.85"><path d="M0 80 L2 30" stroke="#0F2A1F" stroke-width="4" stroke-linecap="round"/><ellipse cx="0" cy="20" rx="32" ry="8" fill="#0F2A1F"/></g>'''

    return f'<svg viewBox="0 0 300 168" preserveAspectRatio="xMidYMid slice">{base}{body}</svg>'


# default scene mapping per slug for visual variety but consistency across pages
DEST_SCENES = {
    "victoria-falls": ("dusk", "falls"),
    "hwange": ("gold", "savanna"),
    "great-zimbabwe": ("terracotta", "ruins"),
    "nyanga": ("forest", "mountains"),
    "chimanimani": ("slate", "trek"),
    "harare": ("green", "city"),
}

TOUR_SCENES = {
    "victoria-falls-day-tour": ("dusk", "falls"),
    "hwange-safari-experience": ("gold", "savanna"),
    "great-zimbabwe-historical-tour": ("terracotta", "ruins"),
    "nyanga-highlands-escape": ("forest", "mountains"),
    "chimanimani-adventure": ("slate", "trek"),
    "custom-zimbabwe-tour": ("green", "hills"),
}

ARTICLE_SCENES = {
    "best-time-to-visit-zimbabwe": ("green", "hills"),
    "victoria-falls-zambia-vs-zimbabwe-side": ("dusk", "falls"),
    "hwange-vs-mana-pools": ("gold", "savanna"),
    "zimbabwe-trip-cost-breakdown": ("slate", "hills"),
    "7-day-zimbabwe-itinerary": ("forest", "river"),
    "zimbabwe-visa-entry-requirements": ("green", "city"),
    "is-zimbabwe-safe-to-visit": ("dusk", "hills"),
    "what-to-pack-for-a-zimbabwe-safari": ("gold", "savanna"),
    "great-zimbabwe-history-explained": ("terracotta", "ruins"),
}


