#!/usr/bin/env python3
"""Generate every SVG used by the profile README.

Edit the DATA section below (experience, stack, about) and run:

    python3 scripts/build_assets.py

Icons come from scripts/icons.json (paths extracted from simple-icons, CC0).
Tools without an icon there get a coloured monogram tile instead.
"""
from __future__ import annotations

import json
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ICONS = json.loads((Path(__file__).parent / "icons.json").read_text())

# ----------------------------------------------------------------------------
# Design tokens
# ----------------------------------------------------------------------------
BG = "#0A0E1A"
SURFACE = "#0F1524"
SURFACE_2 = "#131A2B"
BORDER = "#1E293B"
TEXT = "#E2E8F0"
TEXT_2 = "#CBD5E1"
MUTED = "#64748B"
DIM = "#334155"
CYAN = "#22D3EE"
BLUE = "#60A5FA"
VIOLET = "#A78BFA"
PINK = "#F472B6"
GREEN = "#34D399"
AMBER = "#FBBF24"
ORANGE = "#FB923C"
RED = "#F87171"

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Inter, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', 'Cascadia Code', Menlo, Consolas, 'Liberation Mono', monospace"

W = 900  # every card shares the same width so they line up in the README

# ----------------------------------------------------------------------------
# DATA
# ----------------------------------------------------------------------------
TODAY = date.today()  # the monthly GitHub Action re-renders, so "now" stays current

# Timeline lanes: (company, role, start (y, m), end (y, m) or None = present, colour)
EXPERIENCE = [
    ("GPBank", "Senior Analytics Engineer", (2026, 6), None, CYAN),
    ("HV Holdings", "Analytics Engineer", (2026, 2), (2026, 7), VIOLET),
    ("UpBase", "Data Analytics Engineer", (2026, 1), (2026, 7), PINK),
    ("TNEX Finance", "Senior Data Analyst · GTM", (2025, 9), (2026, 6), BLUE),
    ("VNPAY", "Middle Data Analyst", (2023, 4), (2025, 9), AMBER),
    ("Shopee", "Project Management Officer", (2021, 11), (2023, 4), ORANGE),
    ("MPI Vietnam", "Consultant Network Operator", (2020, 10), (2021, 11), "#94A3B8"),
]
CAREER_START = (2021, 11)  # first data role; drives the "N+ years" copy
TEACHING = [
    ("GPBank", "Internal Data Trainer", (2026, 9), None, CYAN),
    ("Xóm Data", "Founder · data community", (2025, 5), None, GREEN),
    ("MindX", "Instructor & Curriculum Designer", (2025, 5), (2025, 9), RED),
    ("Freelance", "Power BI Instructor (B2B)", (2023, 6), (2026, 2), VIOLET),
]

# Impact tiles: (value, label, context, colour)
IMPACT = [
    ("100+", "dbt models", "4-layer medallion on Redshift · GPBank", CYAN),
    ("50+", "BI dashboards", "Power BI & Superset · VNPAY", AMBER),
    ("104K+", "community reach", "Xóm Data · first 70K in 300 days", GREEN),
    ("1,000+", "students mentored", "MindX · 95% scored above 80%", PINK),
    ("300+", "staff upskilled", "internal data program · GPBank", BLUE),
    ("+300%", "revenue growth", "VnShop relaunch, first year · VNPAY", VIOLET),
]

# Highlights rendered as `git log --oneline`: (type, scope, message)
COMMITS = [
    ("feat", "gpbank", "100+ dbt models in a 4-layer medallion on Redshift, SCD Type 2 across 5 domains"),
    ("sec", "gpbank", "12-role RBAC + hybrid PII protection (Redshift DDM & SHA-256) for the BI platform"),
    ("ci", "gpbank", "Team-wide GitLab CI standard: sqlfluff, black, manifest compile, metadata ingest"),
    ("docs", "gpbank", "DAMA-aligned governance on OpenMetadata: catalog, lineage, auto-generated docs"),
    ("teach", "gpbank", "Internal data upskilling program for 300+ staff, incl. division heads"),
    ("feat", "tnex", "6 end-to-end reporting solutions on a 50+ model dbt layer built with DRY macros"),
    ("perf", "tnex", "100% on-time delivery across every sprint; self-service data marts for Risk"),
    ("grow", "xomdata", "Community 0 → 70,000 members in 300 days; free SQL platform for 5,000+ learners"),
    ("teach", "mindx", "1,000+ students mentored, 95% scored above 80%; +15% course comprehension"),
    ("perf", "vnpay", "VnShop relaunch analytics: +300% revenue, +150% new users, +30% retention"),
    ("feat", "vnpay", "50+ Power BI & Superset dashboards; CDP automation cut manual campaign work 50%"),
    ("teach", "freelance", "B2B Power BI training for corporate clients incl. Honda, Agribank, Habeco"),
    ("perf", "shopee", "New-seller GMV +500% in 3 months, ADO +400%, team workload −50% via automation"),
    ("feat", "shopee", "Live performance dashboards for 20 team leads & 500 key account managers"),
    ("init", "mpi", "Initial commit: ran the Consultant section of the National SME Support Portal"),
]
COMMIT_COLORS = {"feat": GREEN, "perf": AMBER, "sec": RED, "ci": BLUE, "docs": VIOLET,
                 "teach": PINK, "grow": CYAN, "init": MUTED}

# Featured repos, shown highest-starred first. Stars/forks are fetched live at
# build time; the numbers here are only a fallback if the GitHub API is down.
GITHUB_USER = "tunguyenn99"
PROJECTS = [
    # repo, category, description, tech [(label, slug, mono, colour)], fallback stars, forks
    ("thu_vien_cua_xom_data", "community", "Xóm Data's free & public library of data books and learning resources.",
     [("Books", "bookstack", None, None), ("Open", "markdown", None, None)], 396, 109),
    ("data-road-map-by-roles", "community", "If I had to start over from scratch: learning roadmaps for every data role.",
     [("Roadmap", "roadmapdotsh", None, None), ("SQL", None, "SQL", "#38BDF8"), ("dbt", "dbt", None, None)], 200, 28),
    ("crawl-topcv-jobs", "analytics eng", "A pipeline to crawl job postings from TopCV, orchestrated and containerised.",
     [("Airflow", "apacheairflow", None, None), ("PostgreSQL", "postgresql", None, None), ("Docker", "docker", None, None)], 39, 5),
    ("dbt-trino-minio-iceberg-mage", "analytics eng", "On-premises ELT pipeline: dbt on Trino over Iceberg tables in MinIO, run by Mage.",
     [("dbt", "dbt", None, None), ("Trino", "trino", None, None), ("MinIO", "minio", None, None)], 32, 9),
    ("distributed-data-processing", "community", "Efficient data processing in distributed databases (Vietnamese docs).",
     [("Trino", "trino", None, None), ("Docker", "docker", None, None), ("SQL", None, "SQL", "#38BDF8")], 31, 10),
    ("son-tung-mtp-analytics", "analytics eng", "An end-to-end analytics project about Son Tung M-TP.",
     [("dbt", "dbt", None, None), ("Airflow", "apacheairflow", None, None), ("Snowflake", "snowflake", None, None)], 29, 4),
]

# (label, icon slug or None, monogram fallback, monogram colour)
STAGES = [
    ("Sources", [
        ("SQL Server", None, "SQL", "#CC2927"),
        ("Oracle", None, "O", "#F80000"),
        ("PostgreSQL", "postgresql", None, None),
        ("MySQL", "mysql", None, None),
        ("Supabase", "supabase", None, None),
    ]),
    ("Ingest", [
        ("Airbyte", "airbyte", None, None),
        ("Fivetran", None, "F", "#0073FF"),
        ("dlt", None, "dlt", "#59C1D5"),
        ("Selenium", "selenium", None, None),
        ("BeautifulSoup", None, "bs", "#A78BFA"),
    ]),
    ("Warehouse", [
        ("Redshift", None, "RS", "#8C4FFF"),
        ("BigQuery", "googlebigquery", None, None),
        ("ClickHouse", "clickhouse", None, None),
        ("Trino", "trino", None, None),
        ("SingleStore", "singlestore", None, None),
    ]),
    ("Transform", [
        ("dbt", "dbt", None, None),
        ("Jinja macros", "jinja", None, None),
        ("SQL", None, "SQL", "#38BDF8"),
        ("Python", "python", None, None),
        ("Spark", "apachespark", None, None),
    ]),
    ("Govern", [
        ("OpenMetadata", None, "OM", "#7147E8"),
        ("dbt tests", "dbt", None, None),
        ("Data Lineage", None, "L", "#22D3EE"),
        ("RBAC", None, "R", "#F87171"),
        ("PII masking", None, "PII", "#FBBF24"),
        ("DAMA", None, "D", "#34D399"),
    ]),
    ("Serve", [
        ("Power BI", None, "BI", "#F2C811"),
        ("Superset", "apachesuperset", None, None),
        ("QuickSight", None, "QS", "#FF9900"),
        ("Looker Studio", "looker", None, None),
        ("Metabase", "metabase", None, None),
        ("Redash", "redash", None, None),
    ]),
]

ORCHESTRATE = [
    ("Airflow", "apacheairflow", None, None),
    ("Astronomer Cosmos", None, "A", "#6366F1"),
    ("Dagster", None, "D", "#8B5CF6"),
    ("Mage", None, "M", "#A855F7"),
    ("Kestra", None, "K", "#C084FC"),
]

BOTTOM_BANDS = [
    ("Cloud & DataOps", [
        ("AWS", None, "aws", "#FF9900"),
        ("GCP", "googlecloud", None, None),
        ("Fabric", None, "F", "#0F9D58"),
        ("GitLab CI/CD", "gitlab", None, None),
        ("GitHub", "github", None, None),
        ("Argo CD", "argo", None, None),
        ("Docker", "docker", None, None),
    ]),
    ("Product & Workflow", [
        ("GA4", "googleanalytics", None, None),
        ("Smartlook", None, "S", "#FFAB00"),
        ("Jira", "jira", None, None),
        ("Confluence", "confluence", None, None),
        ("Figma", "figma", None, None),
        ("LarkSuite", None, "L", "#3370FF"),
    ]),
]

ABOUT_YAML = [
    ("comment", "# profile.yml — compiled from 5 years of real-world pipelines"),
    ("key", "senior_analytics_engineer:", 0),
    ("kv", "name", '"Tu Nguyen Minh"', 1),
    ("kv", "based_in", '"Hanoi, Vietnam"', 1),
    ("kv", "domains", "[e-commerce, fintech, banking]", 1),
    ("kv", "philosophy", '"Turn raw data complexity into clean, version-controlled business truths."', 1),
    ("key", "core_competencies:", 1),
    ("key", "platform_architecture:", 2),
    ("item", '"Medallion layers, SCD Type 2 history, IBM BDW-based warehouse & marts"', 3),
    ("item", '"Engineering standards: naming, SQL/Python style, reusable macros, CI/CD"', 3),
    ("key", "transformation_modeling:", 2),
    ("item", '"Modular, test-proven dbt projects with Jinja macros and DRY principles"', 3),
    ("key", "data_trust_governance:", 2),
    ("item", '"DAMA-aligned catalog & lineage on OpenMetadata; dbt tests as quality gates"', 3),
    ("item", '"Least-privilege RBAC and dynamic PII masking for regulated banking data"', 3),
    ("key", "bi_analytics:", 2),
    ("item", '"Self-service BI on Power BI & Superset that business teams actually use"', 3),
    ("key", "mentoring:", 2),
    ("item", '"Helping fresher & junior analysts land their first data role"', 3),
]


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def text_w(s: str, size: float, mono: bool = False, bold: bool = False) -> float:
    """Rough rendered width; deliberately generous so nothing collides."""
    if mono:
        return len(s) * size * 0.61
    w = 0.0
    for ch in s:
        if ch in "il.,:;'|!":
            w += 0.28
        elif ch in "fjrtI ":
            w += 0.36
        elif ch in "mwMW":
            w += 0.86
        elif ch.isupper() or ch.isdigit():
            w += 0.64
        else:
            w += 0.54
    return w * size * (1.06 if bold else 1.0)


def svg(width: int, height: int, body: str, title: str, style: str = "") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" fill="none" role="img" aria-label="{escape(title)}">\n'
        f"<title>{escape(title)}</title>\n"
        f"<style>{style}</style>\n{body}\n</svg>\n"
    )


def card_bg(width: int, height: int, uid: str, glow: bool = True) -> str:
    out = f"""
<defs>
  <pattern id="dots-{uid}" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r="1" fill="{DIM}" opacity="0.45"/>
  </pattern>
  <radialGradient id="g1-{uid}" cx="0.85" cy="0.1" r="0.6">
    <stop offset="0" stop-color="{VIOLET}" stop-opacity="0.16"/>
    <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="g2-{uid}" cx="0.05" cy="1" r="0.6">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.10"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>
  <clipPath id="clip-{uid}"><rect width="{width}" height="{height}" rx="16"/></clipPath>
</defs>
<g clip-path="url(#clip-{uid})">
  <rect width="{width}" height="{height}" fill="{BG}"/>
  <rect width="{width}" height="{height}" fill="url(#dots-{uid})"/>"""
    if glow:
        out += f"""
  <rect width="{width}" height="{height}" fill="url(#g1-{uid})"/>
  <rect width="{width}" height="{height}" fill="url(#g2-{uid})"/>"""
    out += f"""
</g>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="15.5" stroke="{BORDER}"/>"""
    return out


def window_chrome(width: int, label: str, right: str = "") -> str:
    out = f"""
<g>
  <circle cx="24" cy="22" r="5.5" fill="#FF5F57"/>
  <circle cx="42" cy="22" r="5.5" fill="#FEBC2E"/>
  <circle cx="60" cy="22" r="5.5" fill="#28C840"/>
  <text x="{width / 2}" y="26" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{MUTED}">{escape(label)}</text>"""
    if right:
        out += f"""
  <text x="{width - 24}" y="26" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUTED}">{escape(right)}</text>"""
    out += f"""
  <line x1="0" y1="44" x2="{width}" y2="44" stroke="{BORDER}"/>
</g>"""
    return out


def icon(slug: str | None, mono: str | None, mono_color: str | None, x: float, y: float, size: float = 14) -> str:
    """Icon of `size` px with its top-left at (x, y)."""
    if slug and slug in ICONS:
        info = ICONS[slug]
        color = info["hex"]
        # very dark brand colours disappear on the dark card
        if color.upper() in ("#000000", "#181717", "#232F3E", "#382923", "#172B4D"):
            color = TEXT
        s = size / 24
        return f'<path transform="translate({x:.1f} {y:.1f}) scale({s:.4f})" d="{info["path"]}" fill="{color}"/>'
    label = mono or "?"
    fs = size * (0.62 if len(label) <= 1 else 0.5 if len(label) == 2 else 0.4)
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{size}" height="{size}" rx="3.5" fill="{mono_color}"/>'
        f'<text x="{x + size / 2:.1f}" y="{y + size / 2 + fs * 0.36:.1f}" text-anchor="middle" '
        f'font-family="{SANS}" font-weight="800" font-size="{fs:.1f}" fill="#0A0E1A">{escape(label)}</text>'
    )


CHIP_H = 24


def chip_width(label: str) -> float:
    return 30 + text_w(label, 11.5) + 10


def chip(label: str, slug, mono, mono_color, x: float, y: float, width: float | None = None, delay: float = 0) -> str:
    w = width or chip_width(label)
    return (
        f'<g class="chip" style="animation-delay:{delay:.2f}s">'
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{CHIP_H}" rx="7" fill="{SURFACE_2}" stroke="{BORDER}"/>'
        + icon(slug, mono, mono_color, x + 8, y + 5)
        + f'<text x="{x + 30:.1f}" y="{y + 16:.1f}" font-family="{SANS}" font-size="11.5" fill="{TEXT_2}">{escape(label)}</text>'
        "</g>"
    )


def career_years() -> int:
    return ((TODAY.year - CAREER_START[0]) * 12 + TODAY.month - CAREER_START[1]) // 12


def write(name: str, content: str) -> None:
    (ASSETS / name).parent.mkdir(parents=True, exist_ok=True)
    (ASSETS / name).write_text(content, encoding="utf-8")
    print(f"  wrote assets/{name}  ({len(content.encode()) / 1024:.1f} KB)")


# ----------------------------------------------------------------------------
# Hero
# ----------------------------------------------------------------------------
def build_hero() -> None:
    H = 340
    lines = [
        ("Senior Analytics Engineer", CYAN),
        ("dbt · Redshift · Airflow · Python", VIOLET),
        ("The truth behind every transaction", PINK),
        ("Founder of Xóm Data · 104K+ reach", GREEN),
    ]
    cycle = 4.0
    total = cycle * len(lines)
    fs = 17
    type_y = 206
    type_x = 48 + text_w("> ", fs, mono=True)

    typing = []
    for i, (txt, col) in enumerate(lines):
        tw = text_w(txt, fs, mono=True) + 2
        assert type_x + tw < 506, f"typing line too wide for the hero: {txt!r}"
        t0 = i * cycle / total
        t_typed = (i * cycle + 1.4) / total
        t_hold = (i * cycle + 3.2) / total
        t_gone = (i * cycle + 3.6) / total
        kt = [0, t0, t_typed, t_hold, t_gone, 1]
        kt = sorted(set(round(k, 4) for k in kt))
        # build matching values for widths
        def vals(a):
            m = {0: 0, round(t0, 4): 0, round(t_typed, 4): a, round(t_hold, 4): a, round(t_gone, 4): 0, 1: 0}
            return ";".join(f"{m[k]:.1f}" for k in kt)
        vis_kt = sorted(set([0, round(t0, 4), round(t_gone, 4), 1]))
        vis_m = {0: 0, round(t0, 4): 1, round(t_gone, 4): 0, 1: 0}
        if i == 0:
            vis_m[0] = 1
        vis_vals = ";".join(str(vis_m[k]) for k in vis_kt)
        kts = ";".join(f"{k:g}" for k in kt)
        typing.append(f"""
  <clipPath id="type-{i}"><rect x="{type_x:.1f}" y="{type_y - 20}" width="0" height="28">
    <animate attributeName="width" dur="{total}s" repeatCount="indefinite" keyTimes="{kts}" values="{vals(tw)}"/>
  </rect></clipPath>
  <text clip-path="url(#type-{i})" x="{type_x:.1f}" y="{type_y}" font-family="{MONO}" font-size="{fs}" font-weight="600" fill="{col}">{escape(txt)}</text>
  <rect y="{type_y - 16}" width="9" height="20" fill="{col}" class="blink" opacity="0">
    <animate attributeName="x" dur="{total}s" repeatCount="indefinite" keyTimes="{kts}" values="{';'.join(f'{type_x + float(v) + 2:.1f}' for v in vals(tw).split(';'))}"/>
    <animate attributeName="opacity" dur="{total}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{';'.join(f'{k:g}' for k in vis_kt)}" values="{vis_vals}"/>
  </rect>""")

    # ---- lineage DAG on the right
    nodes = {
        "src_pos": (548, 104, "src", MUTED),
        "src_core_bank": (548, 160, "src", MUTED),
        "src_ecom": (548, 216, "src", MUTED),
        "stg_orders": (668, 124, "stg", BLUE),
        "stg_txns": (668, 196, "stg", BLUE),
        "fct_revenue": (774, 124, "mart", GREEN),
        "dim_customer": (774, 196, "mart", GREEN),
    }
    widths = {"src": 104, "stg": 86, "mart": 98}
    edges = [
        ("src_pos", "stg_orders"), ("src_ecom", "stg_orders"),
        ("src_core_bank", "stg_txns"), ("src_ecom", "stg_txns"),
        ("stg_orders", "fct_revenue"), ("stg_txns", "fct_revenue"),
        ("stg_txns", "dim_customer"), ("stg_orders", "dim_customer"),
    ]
    dag = []
    for i, (a, b) in enumerate(edges):
        ax, ay, at, _ = nodes[a]
        bx, by, _, bc = nodes[b]
        x1, y1 = ax + widths[at], ay
        x2, y2 = bx, by
        mx = (x1 + x2) / 2
        d = f"M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}"
        dag.append(f'<path id="e{i}" d="{d}" stroke="{DIM}" stroke-width="1.4"/>')
        dag.append(f'<path d="{d}" stroke="{bc}" stroke-width="1.4" class="flow" style="animation-delay:{i * 0.35:.2f}s" opacity="0.55"/>')
        dag.append(
            f'<circle r="2.6" fill="{bc}"><animateMotion dur="2.4s" begin="{i * 0.3:.1f}s" repeatCount="indefinite">'
            f'<mpath href="#e{i}"/></animateMotion></circle>'
        )
    for name, (x, y, t, c) in nodes.items():
        w = widths[t]
        dag.append(
            f'<rect x="{x}" y="{y - 13}" width="{w}" height="26" rx="7" fill="{SURFACE_2}" stroke="{c}" stroke-opacity="0.55"/>'
            f'<circle cx="{x + 11}" cy="{y}" r="3" fill="{c}"/>'
            f'<text x="{x + 20}" y="{y + 4}" font-family="{MONO}" font-size="10.5" fill="{TEXT_2}">{name}</text>'
        )
    for label, x in (("sources", 548), ("staging", 668), ("marts", 774)):
        dag.append(f'<text x="{x}" y="76" font-family="{MONO}" font-size="9.5" letter-spacing="1.5" fill="{MUTED}">{label.upper()}</text>')
    dag.append(
        f'<g font-family="{MONO}" font-size="10.5"><circle cx="553" cy="262" r="3.5" fill="{GREEN}" class="pulse"/>'
        f'<text x="564" y="266" fill="{MUTED}">dbt build</text>'
        f'<text x="632" y="266" fill="{GREEN}">PASS</text>'
        f'<text x="666" y="266" fill="{MUTED}">· lineage healthy · tests green</text></g>'
    )

    # ---- chips under the bio
    tags = [("Hanoi, VN", ORANGE), ("E-commerce", PINK), ("FinTech", VIOLET), ("Banking", CYAN)]
    chips = []
    cx = 48
    cy = 284
    now_label = "Senior AE @ GPBank"
    w0 = text_w(now_label, 11.5, mono=True) + 34
    chips.append(
        f'<rect x="{cx}" y="{cy}" width="{w0:.0f}" height="26" rx="13" fill="{GREEN}" fill-opacity="0.10" stroke="{GREEN}" stroke-opacity="0.45"/>'
        f'<circle cx="{cx + 14}" cy="{cy + 13}" r="3.5" fill="{GREEN}" class="pulse"/>'
        f'<text x="{cx + 24}" y="{cy + 17.5}" font-family="{MONO}" font-size="11.5" fill="{GREEN}">{now_label}</text>'
    )
    cx += w0 + 10
    for t, c in tags:
        w = text_w(t, 11.5, mono=True) + 22
        chips.append(
            f'<rect x="{cx:.0f}" y="{cy}" width="{w:.0f}" height="26" rx="13" fill="{SURFACE_2}" stroke="{BORDER}"/>'
            f'<text x="{cx + 11:.0f}" y="{cy + 17.5}" font-family="{MONO}" font-size="11.5" fill="{c}">{t}</text>'
        )
        cx += w + 8

    style = f"""
.blink{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{fill-opacity:0}}}}
.pulse{{animation:pulse 2s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
@keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.35;transform:scale(1.5)}}}}
.flow{{stroke-dasharray:6 220;animation:flow 2.8s linear infinite}}
@keyframes flow{{from{{stroke-dashoffset:226}}to{{stroke-dashoffset:0}}}}
.fade{{opacity:0;animation:fade .8s ease-out forwards}}
@keyframes fade{{to{{opacity:1}}}}
"""
    body = card_bg(W, H, "hero") + window_chrome(W, "tunguyenn99@data-platform: ~", "main ●")
    body += f"""
<defs>
  <linearGradient id="name-grad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset="0.55" stop-color="#C7D2FE"/>
    <stop offset="1" stop-color="{CYAN}"/>
  </linearGradient>
</defs>
<g class="fade">
  <text x="48" y="90" font-family="{MONO}" font-size="14"><tspan fill="{GREEN}">❯</tspan><tspan fill="{TEXT_2}" dx="8">whoami</tspan></text>
  <text x="46" y="152" font-family="{SANS}" font-weight="800" font-size="58" letter-spacing="-1.5" fill="url(#name-grad)">Tu Nguyen</text>
  <text x="48" y="{type_y}" font-family="{MONO}" font-size="{fs}" font-weight="600" fill="{MUTED}">&gt;</text>
  {''.join(typing)}
  <text x="48" y="244" font-family="{SANS}" font-size="14.5" fill="#94A3B8">{career_years()}+ years across e-commerce, fintech &amp; banking — building</text>
  <text x="48" y="266" font-family="{SANS}" font-size="14.5" fill="#94A3B8">governed data platforms and teaching others to do the same.</text>
  {''.join(chips)}
</g>
<line x1="516" y1="68" x2="516" y2="306" stroke="{BORDER}" stroke-dasharray="3 5"/>
<g class="fade" style="animation-delay:.3s">{''.join(dag)}</g>
"""
    write("hero.svg", svg(W, H, body, "Tu Nguyen — Senior Analytics Engineer", style))


# ----------------------------------------------------------------------------
# Section headers
# ----------------------------------------------------------------------------
SECTIONS = [
    ("01", "About", "cat profile.yml", CYAN),
    ("02", "Impact", "SELECT metric, value FROM impact", BLUE),
    ("03", "Journey", "git log --graph --all", VIOLET),
    ("04", "Projects", "gh repo list --sort stars", ORANGE),
    ("05", "Data Stack", "dbt ls --select +dashboard", PINK),
    ("06", "Activity", "SELECT * FROM github.metrics", GREEN),
    ("07", "Beyond the Code", "curl /api/v1/fun-facts", AMBER),
]


def build_headers() -> None:
    H = 64
    for num, title, cmd, col in SECTIONS:
        uid = f"h{num}"
        tx = 72
        title_w = text_w(title, 22, bold=True)
        cmd_x = tx + title_w + 18
        cmd_txt = f"$ {cmd}"
        line_x = cmd_x + text_w(cmd_txt, 12, mono=True) + 18
        line_end = W - 16
        style = f"""
.pkt{{animation:run 3.6s cubic-bezier(.5,0,.5,1) infinite}}
@keyframes run{{0%{{transform:translateX(0);opacity:0}}10%{{opacity:1}}90%{{opacity:1}}100%{{transform:translateX({line_end - line_x - 4:.0f}px);opacity:0}}}}
"""
        body = f"""
<defs>
  <linearGradient id="ln-{uid}" gradientUnits="userSpaceOnUse" x1="{line_x:.0f}" y1="0" x2="{line_end}" y2="0">
    <stop offset="0" stop-color="{col}" stop-opacity="0.8"/>
    <stop offset="1" stop-color="{col}" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect x="8" y="16" width="48" height="32" rx="9" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-opacity="0.5"/>
<text x="32" y="37" text-anchor="middle" font-family="{MONO}" font-weight="700" font-size="14" fill="{col}">{num}</text>
<text x="{tx}" y="40" font-family="{SANS}" font-weight="700" font-size="22" letter-spacing="-0.3" fill="{col}">{escape(title)}</text>
<text x="{cmd_x:.0f}" y="39" font-family="{MONO}" font-size="12" fill="#8B98AD">{escape(cmd_txt)}</text>
<line x1="{line_x:.0f}" y1="32" x2="{line_end}" y2="32" stroke="url(#ln-{uid})" stroke-width="1.5"/>
<circle class="pkt" cx="{line_x + 2:.0f}" cy="32" r="3" fill="{col}"/>
"""
        write(f"header_{num}.svg", svg(W, H, body, f"{num} · {title}", style))


# ----------------------------------------------------------------------------
# About — editor window with highlighted YAML
# ----------------------------------------------------------------------------
def build_about() -> None:
    LH = 21
    top = 74
    H = top + LH * len(ABOUT_YAML) + 46
    gutter = 58
    fs = 12.8
    cw = fs * 0.61
    rows = []
    minimap = []
    for i, entry in enumerate(ABOUT_YAML):
        y = top + i * LH
        kind = entry[0]
        if kind == "comment":
            indent, parts = 0, [(entry[1], MUTED)]
        elif kind == "key":
            indent = entry[2]
            parts = [(entry[1][:-1], VIOLET if indent == 0 else CYAN if indent == 1 else BLUE), (":", MUTED)]
        elif kind == "kv":
            indent = entry[3]
            val = entry[2]
            vcol = AMBER if val.startswith("[") else GREEN
            parts = [(entry[1], CYAN), (": ", MUTED), (val, vcol)]
        else:  # item
            indent = entry[2]
            parts = [("- ", PINK), (entry[1], GREEN)]
        tspans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in parts)
        x = gutter + 18 + indent * 2 * cw
        rows.append(
            f'<g class="ln" style="animation-delay:{0.15 + i * 0.06:.2f}s">'
            f'<text x="{gutter - 8}" y="{y}" text-anchor="end" font-family="{MONO}" font-size="{fs}" fill="{DIM}">{i + 1}</text>'
            f'<text x="{x:.1f}" y="{y}" font-family="{MONO}" font-size="{fs}" xml:space="preserve">{tspans}</text></g>'
        )
        length = sum(len(t) for t, _ in parts)
        mx = W - 92 + indent * 3
        minimap.append(
            f'<rect x="{mx}" y="{top - 14 + i * 4.2:.1f}" width="{min(length * 0.75, 70):.1f}" height="2.2" rx="1" fill="{parts[-1][1]}" opacity="0.45"/>'
        )
    last_y = top + (len(ABOUT_YAML) - 1) * LH
    style = """
.ln{opacity:0;animation:ln .5s ease-out forwards}
@keyframes ln{from{opacity:0;transform:translateX(-6px)}to{opacity:1;transform:none}}
.blink{animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
"""
    body = card_bg(W, H, "about", glow=True)
    body += f"""
<rect x="0.5" y="0.5" width="{W - 1}" height="44" rx="15.5" fill="{SURFACE}"/>
<rect x="0.5" y="30" width="{W - 1}" height="15" fill="{SURFACE}"/>
{window_chrome(W, "", "YAML · UTF-8")}
<g font-family="{MONO}" font-size="11.5">
  <rect x="84" y="8" width="128" height="37" rx="0" fill="{BG}"/>
  <rect x="84" y="8" width="128" height="2" fill="{CYAN}"/>
  <text x="104" y="31" fill="{TEXT}">profile.yml</text>
  <text x="232" y="31" fill="{MUTED}">stack.yml</text>
  <text x="318" y="31" fill="{MUTED}">README.md</text>
</g>
<rect x="0" y="45" width="{gutter + 4}" height="{H - 45 - 26}" fill="{SURFACE}" opacity="0.5"/>
{''.join(rows)}
<rect x="{gutter + 18}" y="{last_y + LH - 14}" width="8" height="16" fill="{CYAN}" class="blink"/>
<g opacity="0.9">{''.join(minimap)}</g>
<rect x="{W - 96}" y="{top - 18}" width="84" height="{len(ABOUT_YAML) * 4.2 + 10:.0f}" rx="4" fill="{TEXT}" fill-opacity="0.03"/>
<line x1="0" y1="{H - 26}" x2="{W}" y2="{H - 26}" stroke="{BORDER}"/>
<g font-family="{MONO}" font-size="10.5">
  <text x="20" y="{H - 9}" fill="{GREEN}">✓ yamllint passed</text>
  <text x="160" y="{H - 9}" fill="{MUTED}">⎇ main</text>
  <text x="{W - 20}" y="{H - 9}" text-anchor="end" fill="{MUTED}">Ln {len(ABOUT_YAML)}, Col 1 · Spaces: 2</text>
</g>
"""
    write("about.svg", svg(W, H, body, "About Tu Nguyen — profile.yml", style))


# ----------------------------------------------------------------------------
# Experience — branch timeline
# ----------------------------------------------------------------------------
MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def build_experience() -> None:
    lane_h = 44
    group_h = 30
    top = 96
    groups = [("Work", EXPERIENCE), ("Teaching & Community", TEACHING)]
    H = top + sum(group_h + lane_h * len(g) for _, g in groups) + 18
    x0, x1 = 340, W - 44
    start = (2020, 9)

    def m(ym):
        return (ym[0] - start[0]) * 12 + (ym[1] - start[1])

    now = (TODAY.year, TODAY.month)
    span = m(now) + 3

    def X(ym):
        return x0 + (x1 - x0) * m(ym) / span

    xn = X(now)
    grid_bottom = H - 20

    parts = []
    for yr in range(start[0] + 1, TODAY.year + 1):
        xx = X((yr, 1))
        parts.append(f'<line x1="{xx:.1f}" y1="{top - 22}" x2="{xx:.1f}" y2="{grid_bottom}" stroke="{BORDER}" stroke-dasharray="2 4"/>')
        if abs(xx - xn) > 34:
            parts.append(f'<text x="{xx:.1f}" y="{top - 30}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{MUTED}">{yr}</text>')
    parts.append(
        f'<line x1="{xn:.1f}" y1="{top - 22}" x2="{xn:.1f}" y2="{grid_bottom}" stroke="{CYAN}" stroke-opacity="0.5" stroke-dasharray="3 3"/>'
        f'<rect x="{xn - 18:.1f}" y="{top - 43}" width="36" height="18" rx="9" fill="{CYAN}" fill-opacity="0.15" stroke="{CYAN}" stroke-opacity="0.6"/>'
        f'<text x="{xn:.1f}" y="{top - 30}" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="700" fill="{CYAN}">now</text>'
    )

    y = top
    i = 0
    for gname, lanes in groups:
        parts.append(
            f'<text x="24" y="{y + 19}" font-family="{MONO}" font-size="10" font-weight="700" letter-spacing="1.6" fill="{MUTED}">{escape(gname.upper())}</text>'
            f'<line x1="{24 + text_w(gname.upper(), 10, mono=True) + gname.count(" ") * 0 + len(gname) * 1.6 + 10:.0f}" y1="{y + 15}" x2="{x0 - 16}" y2="{y + 15}" stroke="{BORDER}"/>'
        )
        y += group_h
        for co, role, s, e, col in lanes:
            cy = y + lane_h / 2 - 4
            present = e is None
            xs = X(s)
            xe = xn if present else X(e)
            dates = f"{MONTHS[s[1]]} {s[0]} – " + ("now" if present else f"{MONTHS[e[1]]} {e[0]}")
            delay = 0.2 + i * 0.1
            parts.append(
                f'<g class="fade" style="animation-delay:{delay:.2f}s">'
                f'<circle cx="34" cy="{cy - 2}" r="5" fill="{col}"/>'
                + (f'<circle cx="34" cy="{cy - 2}" r="5" fill="{col}" class="ring"/>' if present else "")
                + f'<text x="50" y="{cy + 3}" font-family="{SANS}" font-weight="700" font-size="14.5" fill="{TEXT}">{escape(co)}</text>'
                f'<text x="{x0 - 16}" y="{cy + 2}" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="{col if present else MUTED}">{dates}</text>'
                f'<text x="50" y="{cy + 19}" font-family="{SANS}" font-size="12" fill="#94A3B8">{escape(role)}</text>'
                "</g>"
            )
            parts.append(f'<line x1="{x0}" y1="{cy}" x2="{x1}" y2="{cy}" stroke="{BORDER}"/>')
            bw = max(xe - xs, 6)
            parts.append(
                f'<defs><linearGradient id="bar-{i}" x1="0" y1="0" x2="1" y2="0">'
                f'<stop offset="0" stop-color="{col}" stop-opacity="0.35"/><stop offset="1" stop-color="{col}"/></linearGradient></defs>'
                f'<rect class="grow" style="animation-delay:{delay:.2f}s" x="{xs:.1f}" y="{cy - 5}" width="{bw:.1f}" height="10" rx="5" fill="url(#bar-{i})"/>'
                f'<circle cx="{xs:.1f}" cy="{cy}" r="4.5" fill="{BG}" stroke="{col}" stroke-width="2"/>'
            )
            if present:
                parts.append(
                    f'<g class="fade" style="animation-delay:{delay + 1.0:.2f}s">'
                    f'<circle cx="{xe:.1f}" cy="{cy}" r="5" fill="{col}"/>'
                    f'<circle cx="{xe:.1f}" cy="{cy}" r="5" fill="{col}" class="ring"/></g>'
                )
            else:
                parts.append(
                    f'<g class="fade" style="animation-delay:{delay + 1.0:.2f}s"><circle cx="{xe:.1f}" cy="{cy}" r="4.5" fill="{BG}" stroke="{col}" stroke-width="2"/></g>'
                )
            y += lane_h
            i += 1

    style = """
.fade{opacity:0;animation:fade .6s ease-out forwards}
@keyframes fade{to{opacity:1}}
.ring{animation:ring 2.2s ease-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes ring{0%{transform:scale(1);opacity:.7}100%{transform:scale(2.8);opacity:0}}
.grow{transform:scaleX(0);transform-box:fill-box;transform-origin:left center;animation:grow 1.1s cubic-bezier(.2,.8,.2,1) forwards}
@keyframes grow{to{transform:scaleX(1)}}
"""
    yrs = career_years()
    body = card_bg(W, H, "exp")
    body += f"""
<g font-family="{MONO}" font-size="11.5">
  <text x="24" y="32"><tspan fill="{GREEN}">❯</tspan><tspan fill="{TEXT_2}" dx="8">career --timeline</tspan></text>
  <text x="{W - 24}" y="32" text-anchor="end" fill="{MUTED}">{yrs}+ yrs in data · e-commerce → fintech → banking</text>
</g>
{''.join(parts)}
"""
    write("experience.svg", svg(W, H, body, "Professional experience timeline", style))


# ----------------------------------------------------------------------------
# Highlights — git log --oneline
# ----------------------------------------------------------------------------
def build_commits() -> None:
    import hashlib

    LH = 27
    top = 70
    H = top + LH * len(COMMITS) + 6
    gx = 34
    parts = [f'<line x1="{gx}" y1="{top - 4}" x2="{gx}" y2="{top + LH * (len(COMMITS) - 1)}" stroke="{DIM}" stroke-width="2"/>']
    for i, (typ, scope, msg) in enumerate(COMMITS):
        y = top + i * LH
        col = COMMIT_COLORS[typ]
        sha = hashlib.sha1(f"{scope}:{msg}".encode()).hexdigest()[:7]
        delay = 0.15 + i * 0.07
        tag = f"{typ}({scope}):"
        tag_x = gx + 92
        msg_x = tag_x + max(text_w(f"{t}({sc}):", 12, mono=True) for t, sc, _ in COMMITS) + 12
        parts.append(
            f'<g class="ln" style="animation-delay:{delay:.2f}s">'
            f'<circle cx="{gx}" cy="{y - 4}" r="{5 if i == 0 else 4}" fill="{BG}" stroke="{col}" stroke-width="2"/>'
            f'<text x="{gx + 18}" y="{y}" font-family="{MONO}" font-size="12" fill="{AMBER}" fill-opacity="0.8">{sha}</text>'
            f'<text x="{tag_x}" y="{y}" font-family="{MONO}" font-size="12" fill="{col}">{escape(tag)}</text>'
            f'<text x="{msg_x:.0f}" y="{y}" font-family="{SANS}" font-size="13" fill="{TEXT_2}">{escape(msg)}</text>'
            "</g>"
        )
        assert msg_x + text_w(msg, 13) < W - 20, f"commit message too long: {msg!r}"
    style = """
.ln{opacity:0;animation:ln .45s ease-out forwards}
@keyframes ln{from{opacity:0;transform:translateX(-6px)}to{opacity:1;transform:none}}
"""
    body = card_bg(W, H, "log")
    body += f"""
<g font-family="{MONO}" font-size="11.5">
  <text x="24" y="32"><tspan fill="{GREEN}">❯</tspan><tspan fill="{TEXT_2}" dx="8">git log --oneline --author="Tu Nguyen" highlights</tspan></text>
  <text x="{W - 24}" y="32" text-anchor="end"><tspan fill="{CYAN}">(HEAD → main)</tspan><tspan fill="{MUTED}"> · {len(COMMITS)} commits</tspan></text>
</g>
{''.join(parts)}
"""
    write("highlights.svg", svg(W, H, body, "Career highlights as a git log", style))


# ----------------------------------------------------------------------------
# Impact — KPI tiles
# ----------------------------------------------------------------------------
def build_impact() -> None:
    pad, gap = 20, 12
    cols = 3
    tw = (W - 2 * pad - (cols - 1) * gap) / cols
    th = 106
    rows = (len(IMPACT) + cols - 1) // cols
    H = pad + rows * th + (rows - 1) * gap + pad
    parts = []
    for i, (val, label, ctx, col) in enumerate(IMPACT):
        r, c = divmod(i, cols)
        x = pad + c * (tw + gap)
        y = pad + r * (th + gap)
        delay = 0.1 + i * 0.12
        parts.append(
            f'<g class="tile" style="animation-delay:{delay:.2f}s">'
            f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="{th}" rx="12" fill="{SURFACE}" stroke="{BORDER}"/>'
            f'<rect x="{x + 16:.1f}" y="{y}" width="40" height="2" rx="1" fill="{col}"/>'
            f'<circle cx="{x + tw - 20:.1f}" cy="{y + 20}" r="3" fill="{col}" class="pulse" style="animation-delay:{i * 0.3:.1f}s"/>'
            f'<text x="{x + 16:.1f}" y="{y + 46}" font-family="{SANS}" font-weight="800" font-size="32" letter-spacing="-1" fill="{col}">{escape(val)}</text>'
            f'<text x="{x + 16:.1f}" y="{y + 69}" font-family="{SANS}" font-weight="600" font-size="14" fill="{TEXT}">{escape(label)}</text>'
            f'<text x="{x + 16:.1f}" y="{y + 89}" font-family="{MONO}" font-size="10.5" fill="#8B98AD">{escape(ctx)}</text>'
            "</g>"
        )
        assert 16 + text_w(ctx, 10.5, mono=True) < tw - 10, f"impact context too wide: {ctx!r}"
    style = """
.tile{opacity:0;animation:tile .55s ease-out forwards}
@keyframes tile{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.pulse{animation:pulse 2s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.35;transform:scale(1.6)}}
"""
    body = card_bg(W, H, "impact") + "".join(parts)
    write("impact.svg", svg(W, H, body, "Impact in numbers", style))


# ----------------------------------------------------------------------------
# Stack — architecture view
# ----------------------------------------------------------------------------
def band(label: str, items, x: float, y: float, w: float, col: str, delay0: float, min_h: float = 0, label_w: float = 132, label_top: bool = False):
    """Horizontal band with wrapped chips; returns (svg, height)."""
    pad = 14
    if label_top:
        label_w = 18
    top_off = 34 if label_top else pad
    cx, cy = x + label_w, y + top_off
    out = []
    for j, it in enumerate(items):
        cwid = chip_width(it[0])
        if cx + cwid > x + w - pad:
            cx = x + label_w
            cy += CHIP_H + 8
        out.append(chip(*it, cx, cy, delay=delay0 + j * 0.04))
        cx += cwid + 8
    h = max((cy + CHIP_H + pad) - y, min_h)
    ly = y + 23 if label_top else y + h / 2 + 4
    head = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{SURFACE}" stroke="{BORDER}"/>'
        f'<rect x="{x}" y="{y + 12}" width="3" height="{h - 24}" rx="1.5" fill="{col}"/>'
        f'<text x="{x + 18}" y="{ly}" font-family="{MONO}" font-size="10.5" font-weight="700" letter-spacing="1.4" fill="{col}">{escape(label.upper())}</text>'
    )
    return head + "".join(out), h


def build_stack() -> None:
    pad = 20
    gap = 10
    ncol = len(STAGES)
    col_w = (W - 2 * pad - (ncol - 1) * gap) / ncol
    stage_cols = [CYAN, BLUE, VIOLET, PINK, AMBER, GREEN]

    parts = []
    y = 58
    orch_svg, orch_h = band("Orchestrate", ORCHESTRATE, pad, y, W - 2 * pad, VIOLET, 0.1)
    parts.append(orch_svg)
    y_cols = y + orch_h + 22
    max_items = max(len(items) for _, items in STAGES)
    col_h = 46 + max_items * (CHIP_H + 7) + 6

    for i, ((name, items), col) in enumerate(zip(STAGES, stage_cols)):
        x = pad + i * (col_w + gap)
        cxm = x + col_w / 2
        # trigger line from orchestration band
        parts.append(f'<line x1="{cxm:.1f}" y1="{y + orch_h}" x2="{cxm:.1f}" y2="{y_cols}" stroke="{VIOLET}" stroke-opacity="0.6" class="drop" style="animation-delay:{i * 0.2:.1f}s"/>')
        parts.append(
            f'<rect x="{x:.1f}" y="{y_cols}" width="{col_w:.1f}" height="{col_h}" rx="12" fill="{SURFACE}" stroke="{BORDER}"/>'
            f'<rect x="{x + 12:.1f}" y="{y_cols}" width="{col_w - 24:.1f}" height="2" rx="1" fill="{col}"/>'
            f'<text x="{x + 12:.1f}" y="{y_cols + 26}" font-family="{MONO}" font-size="10.5" font-weight="700" fill="{col}">0{i + 1}</text>'
            f'<text x="{x + 34:.1f}" y="{y_cols + 26}" font-family="{SANS}" font-size="13.5" font-weight="700" fill="{TEXT}">{escape(name)}</text>'
        )
        for j, it in enumerate(items):
            parts.append(chip(*it, x + 8, y_cols + 42 + j * (CHIP_H + 7), width=col_w - 16, delay=0.2 + i * 0.1 + j * 0.05))
        # chevrons between columns
        if i < ncol - 1:
            gx = x + col_w + gap / 2
            parts.append(
                f'<circle cx="{gx:.1f}" cy="{y_cols + 22}" r="7" fill="{BG}" stroke="{BORDER}"/>'
                f'<path d="M{gx - 2:.1f},{y_cols + 19} l3,3 l-3,3" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="chev" style="animation-delay:{i * 0.25:.2f}s"/>'
            )

    y_bottom = y_cols + col_h + 14
    bw = (W - 2 * pad - gap) / 2
    bh_max = 0
    specs = list(zip(BOTTOM_BANDS, [CYAN, PINK]))
    for _ in range(2):  # second pass equalises the heights
        rendered = [band(label, items, pad + k * (bw + gap), y_bottom, bw, col, 0.8, bh_max, label_top=True)
                    for k, ((label, items), col) in enumerate(specs)]
        bh_max = max(h for _, h in rendered)
    parts.extend(s for s, _ in rendered)
    H = int(y_bottom + bh_max + 20)

    style = f"""
.chip{{opacity:0;animation:pop .45s ease-out forwards}}
@keyframes pop{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:none}}}}
.drop{{stroke-dasharray:3 4;animation:drop 1s linear infinite}}
@keyframes drop{{to{{stroke-dashoffset:-14}}}}
.chev{{animation:chev 1.5s ease-in-out infinite}}
@keyframes chev{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
"""
    body = card_bg(W, H, "stack")
    body += f"""
<g font-family="{MONO}" font-size="11.5">
  <text x="24" y="34"><tspan fill="{GREEN}">❯</tspan><tspan fill="{TEXT_2}" dx="8">tree ./modern-data-stack</tspan></text>
  <text x="{W - 24}" y="34" text-anchor="end" fill="{MUTED}">source → staging → marts → decisions</text>
</g>
{''.join(parts)}
"""
    write("stack.svg", svg(W, H, body, "Modern data stack: ingest, store, transform, test, govern, serve", style))


# ----------------------------------------------------------------------------
# Projects — one clickable card per repo
# ----------------------------------------------------------------------------
def fetch_repo_stats() -> dict[str, tuple[int, int]]:
    import os
    import urllib.request

    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-asset-builder"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    stats = {}
    for repo, *_rest in PROJECTS:
        try:
            req = urllib.request.Request(f"https://api.github.com/repos/{GITHUB_USER}/{repo}", headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r:
                d = json.load(r)
            stats[repo] = (int(d["stargazers_count"]), int(d["forks_count"]))
        except Exception as exc:  # offline or rate-limited: keep the fallback numbers
            print(f"  ! could not fetch {repo}: {exc}")
    return stats


def wrap(text: str, size: float, max_w: float) -> list[str]:
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if cur and text_w(trial, size) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + [cur]


def kfmt(n: int) -> str:
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def build_projects() -> list[str]:
    live = fetch_repo_stats()
    rows = []
    for repo, cat, desc, tech, stars, forks in PROJECTS:
        stars, forks = live.get(repo, (stars, forks))
        rows.append((stars, repo, cat, desc, tech, forks))
    rows.sort(key=lambda r: -r[0])

    CW, CH = 440, 156
    for idx, (stars, repo, cat, desc, tech, forks) in enumerate(rows):
        col = CYAN if cat == "community" else VIOLET
        lines = wrap(desc, 12.5, CW - 44)
        assert len(lines) <= 2, f"description too long for a card: {repo}"
        name_size = 14 if text_w(repo, 14, mono=True) < CW - 150 else 12.5
        cat_w = text_w(cat.upper(), 9.5, mono=True) + len(cat) * 1.2 + 18
        parts = [card_bg(CW, CH, f"p{idx}")]
        parts.append(
            f'<rect x="0" y="22" width="3" height="28" rx="1.5" fill="{col}"/>'
            # octicon "repo"
            f'<path transform="translate(22 25) scale(1)" fill="{MUTED}" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/>'
            f'<text x="44" y="38" font-family="{MONO}" font-weight="700" font-size="{name_size}" fill="{TEXT}">{escape(repo)}</text>'
            f'<rect x="{CW - 20 - cat_w:.0f}" y="24" width="{cat_w:.0f}" height="19" rx="9.5" fill="{col}" fill-opacity="0.1" stroke="{col}" stroke-opacity="0.45"/>'
            f'<text x="{CW - 20 - cat_w / 2:.0f}" y="37" text-anchor="middle" font-family="{MONO}" font-size="9.5" letter-spacing="1.2" fill="{col}">{escape(cat.upper())}</text>'
        )
        for k, ln in enumerate(lines):
            parts.append(f'<text x="22" y="{68 + k * 18}" font-family="{SANS}" font-size="12.5" fill="#94A3B8">{escape(ln)}</text>')
        cx = 20
        for t in tech:
            parts.append(chip(*t, cx, 114))
            cx += chip_width(t[0]) + 6
        sx = CW - 20
        fork_txt, star_txt = kfmt(forks), kfmt(stars)
        fw = text_w(fork_txt, 12, mono=True)
        stw = text_w(star_txt, 12, mono=True)
        parts.append(
            f'<g font-family="{MONO}" font-size="12">'
            f'<text x="{sx}" y="131" text-anchor="end" fill="{MUTED}">{fork_txt}</text>'
            # octicon "repo-forked"
            f'<path transform="translate({sx - fw - 18:.0f} 120)" fill="{MUTED}" d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"/>'
            f'<text x="{sx - fw - 28:.0f}" y="131" text-anchor="end" fill="{AMBER}">{star_txt}</text>'
            # octicon "star-fill"
            f'<path class="tw" transform="translate({sx - fw - 28 - stw - 18:.0f} 120)" fill="{AMBER}" d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"/>'
            "</g>"
        )
        assert cx < CW - 20 - fw - stw - 60, f"too many tech chips on {repo}"
        style = """
.chip{opacity:0;animation:pop .45s ease-out forwards}
@keyframes pop{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.tw{animation:tw 2.6s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes tw{0%,100%{opacity:1}50%{opacity:.45}}
"""
        write(f"projects/{repo}.svg", svg(CW, CH, "".join(parts), f"{repo} — {desc} ★ {stars}", style))
    return [r[1] for r in rows]


def sync_readme_projects(order: list[str]) -> None:
    """Rewrite the project grid between the README markers, two cards per row."""
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    start, end = "<!--START_SECTION:projects-->", "<!--END_SECTION:projects-->"
    if start not in text or end not in text:
        print("  ! README has no projects markers; skipped")
        return
    cells = [
        f'    <td width="50%"><a href="https://github.com/{GITHUB_USER}/{repo}">'
        f'<img src="assets/projects/{repo}.svg" width="100%" alt="{repo}" /></a></td>'
        for repo in order
    ]
    rows = ["  <tr>\n" + "\n".join(cells[i:i + 2]) + "\n  </tr>" for i in range(0, len(cells), 2)]
    grid = f'{start}\n<table align="center">\n' + "\n".join(rows) + f"\n</table>\n{end}"
    head, rest = text.split(start, 1)
    _, tail = rest.split(end, 1)
    readme.write_text(head + grid + tail, encoding="utf-8")
    print("  synced README project grid")


# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
def build_footer() -> None:
    H = 170
    style = f"""
.blink{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
.wave{{animation:wave 6s linear infinite}}
@keyframes wave{{to{{transform:translateX(-300px)}}}}
"""
    wave_pts = []
    for k in range(0, 1501, 25):
        import math
        wave_pts.append(f"{k},{H - 34 + 9 * math.sin(k / 47.7):.1f}")
    wave = " ".join(wave_pts)
    body = card_bg(W, H, "foot")
    body += f"""
<defs>
  <linearGradient id="wv" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>
    <stop offset="0.3" stop-color="{CYAN}"/>
    <stop offset="0.7" stop-color="{VIOLET}"/>
    <stop offset="1" stop-color="{PINK}" stop-opacity="0"/>
  </linearGradient>
  <clipPath id="fc"><rect x="1" y="0" width="{W - 2}" height="{H - 1}" rx="15"/></clipPath>
</defs>
<text x="{W / 2}" y="64" text-anchor="middle" font-family="{SANS}" font-weight="800" font-size="26" letter-spacing="-0.5" fill="{TEXT}">Thanks for stopping by.</text>
<text x="{W / 2 - 6}" y="96" text-anchor="middle" font-family="{MONO}" font-size="14"><tspan fill="{GREEN}">❯</tspan><tspan fill="{CYAN}" dx="8">let's build data people can trust</tspan></text>
<rect x="{W / 2 + 168}" y="84" width="8" height="15" fill="{CYAN}" class="blink"/>
<g clip-path="url(#fc)" opacity="0.7">
  <g class="wave"><polyline points="{wave}" stroke="url(#wv)" stroke-width="1.6" fill="none"/></g>
</g>
<text x="{W / 2}" y="{H - 12}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{MUTED}">— EOF —</text>
"""
    write("footer.svg", svg(W, H, body, "Thanks for stopping by", style))


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    build_hero()
    build_headers()
    build_about()
    build_impact()
    build_experience()
    build_commits()
    sync_readme_projects(build_projects())
    build_stack()
    build_footer()
