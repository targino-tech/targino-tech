import os
import html

BASE = os.path.dirname(os.path.abspath(__file__))
BADGES_DIR = os.path.join(BASE, "badges")
os.makedirs(BADGES_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GENERATE BADGE MEDALS (80x80 SVGs matching Credly look & feel)
# -------------------------------------------------------------

def make_badge_svg(title_top, title_bottom, color, icon_svg):
    safe_top = html.escape(title_top)
    safe_bot = html.escape(title_bottom)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80" role="img" aria-label="{safe_top} {safe_bot}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#161B22"/>
      <stop offset="100%" stop-color="#0D1117"/>
    </linearGradient>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{color}"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0.3"/>
    </linearGradient>
  </defs>
  <!-- Outer Ring -->
  <circle cx="40" cy="40" r="37.5" fill="url(#bg)" stroke="url(#ring)" stroke-width="2"/>
  <circle cx="40" cy="40" r="33" fill="none" stroke="#242C37" stroke-width="1" stroke-dasharray="2,2"/>
  <!-- Icon Center -->
  <g transform="translate(24, 18)">
    {icon_svg}
  </g>
  <!-- Badge Texts -->
  <text x="40" y="58" font-family="'Segoe UI',Roboto,Helvetica,sans-serif" font-size="6.5" font-weight="700" text-anchor="middle" fill="{color}" letter-spacing="0.5">{safe_top}</text>
  <text x="40" y="67" font-family="'Segoe UI',Roboto,Helvetica,sans-serif" font-size="5.5" font-weight="600" text-anchor="middle" fill="#8B949E">{safe_bot}</text>
</svg>
"""

# IDsec SOC Analyst Icon (Shield with lock)
idsec_icon = """<path d="M16 2L4 6v8c0 7.5 5.1 14.5 12 16 6.9-1.5 12-8.5 12-16V6l-12-4z" fill="none" stroke="#00E5FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="12" y="14" width="8" height="6" rx="1.5" fill="#00E5FF"/>
<path d="M14 14v-2a2 2 0 0 1 4 0v2" fill="none" stroke="#00E5FF" stroke-width="1.8"/>"""

# Fórum Telecom / Analista de Redes (Network Routers / Switch Nodes)
forum_icon = """<rect x="4" y="10" width="24" height="12" rx="3" fill="none" stroke="#00A4EF" stroke-width="2"/>
<circle cx="9" cy="16" r="1.5" fill="#00A4EF"/>
<circle cx="15" cy="16" r="1.5" fill="#00A4EF"/>
<circle cx="21" cy="16" r="1.5" fill="#00A4EF"/>
<path d="M10 6l6-4 6 4M10 26l6 4 6-4" fill="none" stroke="#00A4EF" stroke-width="1.5" stroke-linecap="round"/>"""

# DIO / Riachuelo Cibersegurança (Security Eye / Radar)
dio_icon = """<circle cx="16" cy="16" r="12" fill="none" stroke="#EA4B71" stroke-width="2"/>
<circle cx="16" cy="16" r="7" fill="none" stroke="#EA4B71" stroke-width="1.5" stroke-dasharray="3,2"/>
<circle cx="16" cy="16" r="3" fill="#EA4B71"/>
<path d="M16 2v4M16 26v4M2 16h4M26 16h4" stroke="#EA4B71" stroke-width="1.8" stroke-linecap="round"/>"""

with open(os.path.join(BADGES_DIR, "idsec-soc.svg"), "w", encoding="utf-8") as f:
    f.write(make_badge_svg("IDSEC", "SOC ANALYST", "#00E5FF", idsec_icon))

with open(os.path.join(BADGES_DIR, "forum-telecom.svg"), "w", encoding="utf-8") as f:
    f.write(make_badge_svg("FÓRUM TEL", "NETWORK SPEC", "#00A4EF", forum_icon))

with open(os.path.join(BADGES_DIR, "dio-cyber.svg"), "w", encoding="utf-8") as f:
    f.write(make_badge_svg("DIO / RIACHUELO", "CYBERSECURITY", "#EA4B71", dio_icon))


# -------------------------------------------------------------
# 2. GENERATE PROJECT CARDS (matching Lucas Marujo build_cards.py)
# -------------------------------------------------------------

FONT = "'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
CARD_BACKGROUND = "#0D1117"
CARD_BORDER = "#242C37"
CARD_WIDTH = 300
CARD_RADIUS = 16
CARD_PADDING = 24
TOP_HEIGHT = 152
HALF_WIDTH = CARD_WIDTH // 2
BOTTOM_HEIGHT = 68
BUTTON_GAP = 8
BUTTON_WIDTH = (CARD_WIDTH - 2 * CARD_PADDING - BUTTON_GAP) // 2
BUTTON_HEIGHT = 34
BUTTON_Y = BOTTOM_HEIGHT - CARD_PADDING - BUTTON_HEIGHT
APP_BUTTON_X = CARD_PADDING
SITE_BUTTON_X = BUTTON_GAP // 2
LABEL_Y = BUTTON_Y + 21.5
LABEL_CHAR_WIDTH = 5.8
LABEL_ICON_GAP = 7
DOWNLOAD_ICON_WIDTH = 10
SITE_ICON_WIDTH = 8

PROJECTS = [
    {
        "slug": "cups",
        "name": "CUPS Root Intel",
        "kind": "SYSADMIN · UX",
        "color": "#00E5FF",
        "icon_path": """<rect x="36" y="36" width="28" height="20" rx="3" fill="none" stroke="#00E5FF" stroke-width="2.2"/>
        <path d="M42 36V30a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v6M42 50v8h16v-8" fill="none" stroke="#00E5FF" stroke-width="2.2"/>
        <line x1="40" y1="42" x2="44" y2="42" stroke="#00E5FF" stroke-width="2.5" stroke-linecap="round"/>""",
        "lines": ["Interface moderna com Dark Theme,", "Command Palette (Ctrl+K) para CUPS."],
        "cta": "Repositório",
        "site_cta": "Ver Projeto",
    },
    {
        "slug": "orkai",
        "name": "Orkai CLI",
        "kind": "CONTRIBUTOR",
        "color": "#FF5F87",
        "icon_path": """<rect x="35" y="35" width="30" height="30" rx="6" fill="none" stroke="#FF5F87" stroke-width="2.2"/>
        <path d="M41 45l5 5-5 5M49 55h8" fill="none" stroke="#FF5F87" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>""",
        "lines": ["Orquestrador de agentes de IA.", "Contribuição: Modo Português (pt-BR)."],
        "cta": "Ver PR",
        "site_cta": "Orkai Repo",
    },
    {
        "slug": "infralab",
        "name": "Infra & SOC Lab",
        "kind": "NETWORKING · LAB",
        "color": "#F38020",
        "icon_path": """<path d="M50 32l-14 6v9c0 9 6 17.5 14 20 8-2.5 14-11 14-20v-9l-14-6z" fill="none" stroke="#F38020" stroke-width="2.2" stroke-linejoin="round"/>
        <path d="M46 47l3 3 6-6" fill="none" stroke="#F38020" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>""",
        "lines": ["Topologias MikroTik, FortiGate,", "Proxmox e automação com n8n."],
        "cta": "Ver Stack",
        "site_cta": "Detalhes",
    },
]

def top_shape():
    edge = CARD_WIDTH - 0.75
    return (
        f"M0.75 {TOP_HEIGHT + 1}V{0.75 + CARD_RADIUS:g}"
        f"A{CARD_RADIUS} {CARD_RADIUS} 0 0 1 {0.75 + CARD_RADIUS:g} 0.75H{edge - CARD_RADIUS:g}"
        f"A{CARD_RADIUS} {CARD_RADIUS} 0 0 1 {edge:g} {0.75 + CARD_RADIUS:g}V{TOP_HEIGHT + 1}"
    )

def app_half_shapes():
    bottom = BOTTOM_HEIGHT - 0.75
    corner = (
        f"V{bottom - CARD_RADIUS:g}"
        f"A{CARD_RADIUS} {CARD_RADIUS} 0 0 0 {0.75 + CARD_RADIUS:g} {bottom:g}H{HALF_WIDTH + 1}"
    )
    return f"M{HALF_WIDTH + 1} -1H0.75{corner}Z", f"M0.75 -1{corner}"

def site_half_shapes():
    bottom = BOTTOM_HEIGHT - 0.75
    edge = HALF_WIDTH - 0.75
    corner = (
        f"V{bottom - CARD_RADIUS:g}"
        f"A{CARD_RADIUS} {CARD_RADIUS} 0 0 1 {edge - CARD_RADIUS:g} {bottom:g}H-1"
    )
    return f"M-1 -1H{edge:g}{corner}Z", f"M{edge:g} -1{corner}"

def layout_label(label, button_x, icon_width):
    text_width = LABEL_CHAR_WIDTH * len(label)
    center = button_x + BUTTON_WIDTH / 2
    text_end = center - (text_width + LABEL_ICON_GAP + icon_width) / 2 + text_width
    return text_end, text_end + LABEL_ICON_GAP + icon_width / 2

def render_piece(width, height, label, body):
    safe_label = html.escape(label)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{safe_label}">
  {body}
</svg>
"""

def render_half(shapes, button):
    fill, border = shapes
    return (
        f'<path d="{fill}" fill="{CARD_BACKGROUND}"/>'
        f'<path d="{border}" fill="none" stroke="{CARD_BORDER}"/>'
        f"{button}"
    )

def render_cta(project):
    label = project["cta"]
    color = project["color"]
    tx, ix = layout_label(label, APP_BUTTON_X, DOWNLOAD_ICON_WIDTH)
    arrow_top = BUTTON_Y + 9.5
    safe_label = html.escape(label)
    button = (
        f'<rect x="{APP_BUTTON_X}" y="{BUTTON_Y}" width="{BUTTON_WIDTH}" height="{BUTTON_HEIGHT}"'
        f' rx="{BUTTON_HEIGHT / 2:g}" fill="{color}"/>'
        f'<text x="{tx:g}" y="{LABEL_Y:g}" text-anchor="end" font-family="{FONT}" font-size="12"'
        f' font-weight="600" fill="#0D1117">{safe_label}</text>'
        f'<path d="M{ix:g} {arrow_top:g}v9m0 0l-3.5-3.5M{ix:g} {arrow_top + 9:g}l3.5-3.5M{ix - 5:g} {arrow_top + 15:g}h10"'
        f' fill="none" stroke="#0D1117" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    return render_piece(HALF_WIDTH, BOTTOM_HEIGHT, label, render_half(app_half_shapes(), button))

def render_site_cta(project):
    color = project["color"]
    site_cta = project["site_cta"]
    tx, ix = layout_label(site_cta, SITE_BUTTON_X, SITE_ICON_WIDTH)
    icon_y = BUTTON_Y + BUTTON_HEIGHT / 2
    safe_site_cta = html.escape(site_cta)
    button = (
        f'<rect x="{SITE_BUTTON_X + 0.5:g}" y="{BUTTON_Y + 0.5:g}" width="{BUTTON_WIDTH - 1}" height="{BUTTON_HEIGHT - 1}"'
        f' rx="{(BUTTON_HEIGHT - 1) / 2:g}" fill="{color}" fill-opacity="0.06" stroke="{color}" stroke-opacity="0.5"/>'
        f'<text x="{tx:g}" y="{LABEL_Y:g}" text-anchor="end" font-family="{FONT}" font-size="12"'
        f' font-weight="600" fill="{color}">{safe_site_cta}</text>'
        f'<path d="M{ix - 4:g} {icon_y + 4:g}l8-8M{ix - 2:g} {icon_y - 4:g}h6v6" fill="none"'
        f' stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    return render_piece(HALF_WIDTH, BOTTOM_HEIGHT, site_cta, render_half(site_half_shapes(), button))

def render_lines(lines):
    ys = [122, 141] if len(lines) > 1 else [131]
    return "".join(
        f'<text x="24" y="{y}" font-family="{FONT}" font-size="13" fill="#8B949E">{html.escape(line)}</text>'
        for y, line in zip(ys, lines)
    )

def render_card(project):
    color = project["color"]
    shape = top_shape()
    icon_svg = project["icon_path"]
    safe_name = html.escape(project["name"])
    safe_kind = html.escape(project["kind"])
    return render_piece(CARD_WIDTH, TOP_HEIGHT, project["name"], f"""<defs>
    <linearGradient id="icon_{project['slug']}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{color}" stop-opacity="0.25"/>
      <stop offset="1" stop-color="{color}" stop-opacity="0.05"/>
    </linearGradient>
    <radialGradient id="glow_{project['slug']}" cx="0.9" cy="0" r="0.95">
      <stop offset="0" stop-color="{color}" stop-opacity="0.10"/>
      <stop offset="1" stop-color="{color}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <path d="{shape}" fill="{CARD_BACKGROUND}" stroke="{CARD_BORDER}"/>
  <path d="{shape}" fill="url(#glow_{project['slug']})"/>
  <!-- Card Icon Box -->
  <rect x="24" y="24" width="52" height="52" rx="14" fill="url(#icon_{project['slug']})" stroke="{color}" stroke-opacity="0.4" stroke-width="1.2"/>
  <g>{icon_svg}</g>
  <text x="90" y="43" font-family="{FONT}" font-size="9.5" font-weight="600" letter-spacing="2" fill="#5B6672">{safe_kind}</text>
  <text x="89" y="69" font-family="{FONT}" font-size="22" font-weight="700" fill="{color}">{safe_name}</text>
  <line x1="24" y1="96" x2="{CARD_WIDTH - 24}" y2="96" stroke="#1E252F"/>
  {render_lines(project['lines'])}""")

for project in PROJECTS:
    with open(os.path.join(BASE, f"card-{project['slug']}-top.svg"), "w", encoding="utf-8") as f:
        f.write(render_card(project))
    with open(os.path.join(BASE, f"card-{project['slug']}-app.svg"), "w", encoding="utf-8") as f:
        f.write(render_cta(project))
    with open(os.path.join(BASE, f"card-{project['slug']}-site.svg"), "w", encoding="utf-8") as f:
        f.write(render_site_cta(project))

print("Assets successfully regenerated with valid XML escaping!")

