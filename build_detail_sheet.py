"""
Build the CFW Detail Sheet (ANSI B / 11x17 landscape) showing the five
container fire-rated wall assemblies on a single drawing.

Assemblies depicted (top row, plan-section views, container exterior at top):
  CFW-1A  - 1HR  - V497 2-layer (gypsum + ProForm Quick-Set)
  CFW-1B  - 1HR  - V497 3-layer
  CFW-2   - 2HR  - V497 4-layer
  CFW-1E  - 1HR symmetric (CFW-1B + intumescent on container exterior)
  CFW-2E  - 2HR symmetric (CFW-2 + intumescent on container exterior)

Output: details/CFW-Detail-Sheet.pdf
"""
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, grey
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTFILE = "/sessions/adoring-sleepy-einstein/mnt/ContainerFireWall/container-fire-assemblies/details/CFW-Detail-Sheet.pdf"

# ANSI B - 17 x 11 landscape
PAGE_W, PAGE_H = 17 * inch, 11 * inch

# Colors
BRAND_BLUE = HexColor("#2D5BFF")
LIGHT_GREY = HexColor("#E5E7EB")
MID_GREY = HexColor("#9CA3AF")
DARK_GREY = HexColor("#374151")
INK = HexColor("#0B1220")
GYPSUM_FILL = HexColor("#F4F1E8")
INSUL_FILL = HexColor("#FFE9B0")
SPF_FILL = HexColor("#D9C8FF")
STEEL_FILL = HexColor("#9AA0A6")
INTUMESC_FILL = HexColor("#FF7A59")

# Layout
MARGIN = 0.5 * inch
TITLE_BLOCK_W = 3.6 * inch
TITLE_BLOCK_H = 2.2 * inch

# Drawing area for the five assembly details
DRAW_TOP = PAGE_H - MARGIN - 0.45 * inch  # leave room for sheet title bar
DRAW_BOTTOM = MARGIN + TITLE_BLOCK_H + 0.2 * inch
DRAW_LEFT = MARGIN
DRAW_RIGHT = PAGE_W - MARGIN

NUM_DETAILS = 5
DETAIL_GAP = 0.18 * inch
DETAIL_W = (DRAW_RIGHT - DRAW_LEFT - (NUM_DETAILS - 1) * DETAIL_GAP) / NUM_DETAILS
DETAIL_H = DRAW_TOP - DRAW_BOTTOM


def setup_canvas():
    c = canvas.Canvas(OUTFILE, pagesize=(PAGE_W, PAGE_H))
    c.setTitle("CFW Detail Sheet - Container Fire-Rated Wall Assemblies")
    c.setAuthor("Oasis Engineering, PLLC")
    c.setSubject("Container fire-rated wall assemblies based on UL Design V497")
    return c


def draw_sheet_title_bar(c):
    """Top header bar with sheet title."""
    bar_h = 0.4 * inch
    bar_y = PAGE_H - MARGIN - bar_h
    c.setFillColor(INK)
    c.rect(MARGIN, bar_y, PAGE_W - 2 * MARGIN, bar_h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(MARGIN + 0.18 * inch, bar_y + 0.13 * inch,
                 "CONTAINER FIRE-RATED WALL ASSEMBLIES \u2014 CFW SERIES")
    c.setFillColor(BRAND_BLUE)
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(PAGE_W - MARGIN - 0.18 * inch, bar_y + 0.13 * inch,
                      "OASIS ENGINEERING")


def draw_title_block(c):
    """Bottom-right title/stamp block."""
    x = PAGE_W - MARGIN - TITLE_BLOCK_W
    y = MARGIN
    w, h = TITLE_BLOCK_W, TITLE_BLOCK_H

    # Outer frame
    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.rect(x, y, w, h, fill=0, stroke=1)

    # Brand band
    band_h = 0.5 * inch
    c.setFillColor(INK)
    c.rect(x, y + h - band_h, w, band_h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x + 0.15 * inch, y + h - band_h + 0.17 * inch, "OASIS ENGINEERING")
    c.setFillColor(BRAND_BLUE)
    c.setFont("Helvetica", 8)
    c.drawRightString(x + w - 0.15 * inch, y + h - band_h + 0.18 * inch,
                      "oasisengineering.com")

    # Body grid
    c.setStrokeColor(MID_GREY)
    c.setLineWidth(0.5)
    inner_top = y + h - band_h
    # Horizontal divisions
    row1 = inner_top - 0.32 * inch
    row2 = row1 - 0.32 * inch
    row3 = row2 - 0.32 * inch
    row4 = row3 - 0.32 * inch
    for ry in (row1, row2, row3, row4):
        c.line(x, ry, x + w, ry)
    # Vertical mid-line for stamp area
    mid_x = x + w * 0.55
    c.line(mid_x, row4, mid_x, y)

    # Labels
    c.setFillColor(DARK_GREY)
    c.setFont("Helvetica", 6.5)
    c.drawString(x + 0.10 * inch, inner_top - 0.10 * inch, "PROJECT")
    c.drawString(x + 0.10 * inch, row1 - 0.10 * inch, "SHEET TITLE")
    c.drawString(x + 0.10 * inch, row2 - 0.10 * inch, "ENGINEER OF RECORD")
    c.drawString(x + 0.10 * inch, row3 - 0.10 * inch, "DRAWN / CHECKED / DATE")

    # Values
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 0.10 * inch, inner_top - 0.24 * inch,
                 "Container Fire-Rated Wall Assemblies")
    c.setFont("Helvetica", 9)
    c.drawString(x + 0.10 * inch, row1 - 0.24 * inch,
                 "CFW Series \u2014 1HR & 2HR per UL V497")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x + 0.10 * inch, row2 - 0.24 * inch, "Enrique Lairet, PE")
    c.setFont("Helvetica", 8)
    c.drawString(x + 0.10 * inch, row3 - 0.24 * inch,
                 "EL / EL / Apr 2026")

    # Sheet number in bottom-left of title block
    c.setFont("Helvetica", 7)
    c.setFillColor(DARK_GREY)
    c.drawString(x + 0.10 * inch, y + 0.65 * inch, "SHEET")
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(BRAND_BLUE)
    c.drawString(x + 0.10 * inch, y + 0.20 * inch, "CFW-001")
    c.setFont("Helvetica", 7)
    c.setFillColor(DARK_GREY)
    c.drawString(x + 0.10 * inch, y + 0.08 * inch, "REV 1.2  \u00b7  Apr 2026")

    # PE stamp area
    stamp_x = mid_x + 0.05 * inch
    stamp_y = y + 0.05 * inch
    stamp_w = (x + w) - stamp_x - 0.05 * inch
    stamp_h = row4 - stamp_y - 0.05 * inch
    c.setStrokeColor(MID_GREY)
    c.setDash(2, 2)
    c.rect(stamp_x, stamp_y, stamp_w, stamp_h, fill=0, stroke=1)
    c.setDash()
    c.setFillColor(MID_GREY)
    c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(stamp_x + stamp_w / 2,
                        stamp_y + stamp_h / 2 + 6, "PE STAMP")
    c.drawCentredString(stamp_x + stamp_w / 2,
                        stamp_y + stamp_h / 2 - 4, "(project-specific)")


def draw_code_basis_block(c):
    """Bottom-left code basis/notes block."""
    x = MARGIN
    y = MARGIN
    w = PAGE_W - 2 * MARGIN - TITLE_BLOCK_W - 0.2 * inch
    h = TITLE_BLOCK_H

    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.rect(x, y, w, h, fill=0, stroke=1)

    # Header
    c.setFillColor(BRAND_BLUE)
    c.rect(x, y + h - 0.32 * inch, w, 0.32 * inch, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 0.12 * inch, y + h - 0.32 * inch + 0.10 * inch,
                 "CODE BASIS  \u00b7  GENERAL NOTES  \u00b7  LEGEND")

    # Two columns of notes
    col_pad = 0.15 * inch
    col_w = (w - 3 * col_pad) / 2
    col1_x = x + col_pad
    col2_x = col1_x + col_w + col_pad
    text_top = y + h - 0.42 * inch

    # Column 1: code basis
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(col1_x, text_top, "CODE BASIS")
    c.setFont("Helvetica", 7.5)
    notes1 = [
        "1. CFW-1A, CFW-1B, CFW-2 are direct application of UL Design V497",
        "   (GA File WP 1297) per IBC \u00a7703.2.2(1) \u2014 approved listed source.",
        "   No alternative-means submittal required.",
        "2. CFW-1E, CFW-2E add a UL-listed intumescent coating on container",
        "   exterior steel; equivalency per IBC \u00a7703.2.2(4) (engineering",
        "   analysis) and submitted under IBC \u00a7104.11.",
        "3. V497 is asymmetric: gypsum on one side; opposite side may be",
        "   bare. Container skin replaces the unprotected side and is",
        "   conservatively additive to the listed assembly.",
        "4. Insulation per V497 listing is OPTIONAL. ccSPF may be applied",
        "   directly to container skin OUTBOARD of V497 stud cavity for",
        "   thermal/air-seal performance without affecting the listing.",
    ]
    line_y = text_top - 0.13 * inch
    for line in notes1:
        c.drawString(col1_x, line_y, line)
        line_y -= 0.115 * inch

    # Column 2: general notes + legend
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(col2_x, text_top, "GENERAL NOTES")
    c.setFont("Helvetica", 7.5)
    notes2 = [
        "A. All gypsum to be 5/8\" Gold Bond Fire-Shield Type X (FSW family)",
        "   per V497 listing. No off-brand substitutions.",
        "B. Steel studs: 3-5/8\" min., 24\" o.c. max., 25 ga or heavier.",
        "C. Top of wall: UL-listed head-of-wall firestop system at container",
        "   roof corrugation joint per UL 2079.",
        "D. All penetrations firestopped per UL 1479; joints per UL 2079.",
        "E. Intumescent coating thickness to be verified by WFT/DFT gauge",
        "   and documented per coating UL listing requirements.",
        "F. Surface prep for intumescent: SSPC-SP6 or coating manufacturer",
        "   approved alternative for COR-TEN A weathering steel.",
        "G. Confirm direction of rating requirement before specifying. CFW-1*",
        "   variants protect against interior fires; CFW-*E for symmetric.",
    ]
    line_y = text_top - 0.13 * inch
    for line in notes2:
        c.drawString(col2_x, line_y, line)
        line_y -= 0.115 * inch

    # Legend at bottom of column 2
    legend_y = y + 0.20 * inch
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(INK)
    c.drawString(col2_x, legend_y + 0.40 * inch, "MATERIAL LEGEND")
    legend_items = [
        (GYPSUM_FILL, "Type X gypsum"),
        (INSUL_FILL, "Glass fiber insul. (opt.)"),
        (SPF_FILL, "ccSPF (outboard, opt.)"),
        (STEEL_FILL, "Steel skin / studs"),
        (INTUMESC_FILL, "Intumescent coating"),
    ]
    sx = col2_x
    sy = legend_y + 0.20 * inch
    for fill, label in legend_items:
        c.setFillColor(fill)
        c.setStrokeColor(INK)
        c.setLineWidth(0.4)
        c.rect(sx, sy, 0.16 * inch, 0.12 * inch, fill=1, stroke=1)
        c.setFillColor(INK)
        c.setFont("Helvetica", 6.8)
        c.drawString(sx + 0.20 * inch, sy + 0.025 * inch, label)
        sx += 1.1 * inch
        if sx > col2_x + col_w - 0.5 * inch:
            sx = col2_x
            sy -= 0.16 * inch


# -----------------------------
# Assembly detail rendering
# -----------------------------

def draw_detail_frame(c, x, y, w, h, tag, rating, code_basis, sub_title):
    """Draw the outer frame, header tag, and label area for one detail."""
    c.setStrokeColor(INK)
    c.setLineWidth(0.8)
    c.rect(x, y, w, h, fill=0, stroke=1)

    # Tag header
    tag_h = 0.36 * inch
    c.setFillColor(BRAND_BLUE)
    c.rect(x, y + h - tag_h, w, tag_h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x + 0.10 * inch, y + h - tag_h + 0.12 * inch, tag)
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(x + w - 0.10 * inch, y + h - tag_h + 0.12 * inch, rating)

    # Code basis sub-header
    sub_h = 0.22 * inch
    sub_y = y + h - tag_h - sub_h
    c.setFillColor(LIGHT_GREY)
    c.rect(x, sub_y, w, sub_h, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(x + 0.10 * inch, sub_y + 0.07 * inch, code_basis)
    c.setFont("Helvetica", 7)
    c.drawRightString(x + w - 0.10 * inch, sub_y + 0.07 * inch, sub_title)

    return sub_y  # top of available drawing area


def draw_corrugation_band(c, x, y, w, h, fill_color):
    """Container skin: corrugated steel band drawn with sine-like ridges."""
    c.saveState()
    # Solid base
    c.setFillColor(fill_color)
    c.setStrokeColor(INK)
    c.setLineWidth(0.6)
    c.rect(x, y, w, h, fill=1, stroke=1)

    # Vertical ridge marks to suggest corrugation
    c.setStrokeColor(DARK_GREY)
    c.setLineWidth(0.4)
    n_ridges = 16
    for i in range(1, n_ridges):
        rx = x + i * (w / n_ridges)
        c.line(rx, y + 0.02 * inch, rx, y + h - 0.02 * inch)
    c.restoreState()


def draw_assembly(c, x, y, w, h, layers, callouts):
    """
    Draw an assembly section view inside the available area.
    layers: list of (thickness_units, fill_color, hatch_label, layer_id)
            ordered from EXTERIOR (top) to INTERIOR (bottom)
    callouts: list of (layer_id, label_text) - drawn as leader lines to the right
    """
    # Stack layout: thickness_units are relative; we normalize to fit.
    total_units = sum(t for t, *_ in layers)
    pad = 0.15 * inch
    # We'll draw the section in the LEFT portion of the available area,
    # leaving room on the RIGHT for callouts.
    drawing_w = w * 0.36
    drawing_x = x + pad
    drawing_y = y + pad
    drawing_h = h - 2 * pad

    # Track each layer's center y for callout leader lines
    layer_centers = {}

    cur_y = drawing_y + drawing_h  # start at top (exterior)
    for (units, fill, hatch, lid) in layers:
        layer_h = (units / total_units) * drawing_h
        ly = cur_y - layer_h

        if fill == "CONTAINER_CORR":
            draw_corrugation_band(c, drawing_x, ly, drawing_w, layer_h, STEEL_FILL)
        elif fill == "AIR":
            # Dashed outline only for air gap
            c.setStrokeColor(MID_GREY)
            c.setLineWidth(0.4)
            c.setDash(2, 2)
            c.rect(drawing_x, ly, drawing_w, layer_h, fill=0, stroke=1)
            c.setDash()
        elif fill == "STUD":
            # Two C-stud cross sections (drawn as small C shapes)
            c.setFillColor(LIGHT_GREY)
            c.setStrokeColor(MID_GREY)
            c.setLineWidth(0.4)
            c.rect(drawing_x, ly, drawing_w, layer_h, fill=1, stroke=1)
            # Studs at 1/4 and 3/4 width
            stud_w = 0.10 * inch
            stud_h = layer_h - 0.04 * inch
            for sx_frac in (0.25, 0.75):
                sx_pos = drawing_x + sx_frac * drawing_w - stud_w / 2
                sy_pos = ly + 0.02 * inch
                c.setFillColor(STEEL_FILL)
                c.setStrokeColor(INK)
                c.setLineWidth(0.5)
                # C-shape: rect with cut-out
                c.rect(sx_pos, sy_pos, stud_w, stud_h, fill=1, stroke=1)
                c.setFillColor(white)
                c.rect(sx_pos + 0.025 * inch, sy_pos + 0.02 * inch,
                       stud_w - 0.05 * inch, stud_h - 0.04 * inch,
                       fill=1, stroke=0)
        elif fill == "INSUL":
            c.setFillColor(INSUL_FILL)
            c.setStrokeColor(INK)
            c.setLineWidth(0.4)
            c.rect(drawing_x, ly, drawing_w, layer_h, fill=1, stroke=1)
            # Wavy lines to suggest batt
            c.setStrokeColor(DARK_GREY)
            c.setLineWidth(0.3)
            n = 6
            for i in range(n):
                wy = ly + (i + 0.5) * (layer_h / n)
                c.line(drawing_x + 0.04 * inch, wy,
                       drawing_x + drawing_w - 0.04 * inch, wy)
        elif fill == "SPF":
            c.setFillColor(SPF_FILL)
            c.setStrokeColor(INK)
            c.setLineWidth(0.4)
            c.rect(drawing_x, ly, drawing_w, layer_h, fill=1, stroke=1)
            # Bubbly hatch
            c.setStrokeColor(DARK_GREY)
            c.setLineWidth(0.3)
            import math
            for i in range(20):
                cx = drawing_x + ((i * 7.3) % (drawing_w * 0.9)) + 0.03 * inch
                cy = ly + 0.04 * inch + ((i * 3.1) % (layer_h * 0.9))
                c.circle(cx, cy, 0.025 * inch, fill=0, stroke=1)
        elif fill == "INTUMESC":
            c.setFillColor(INTUMESC_FILL)
            c.setStrokeColor(INK)
            c.setLineWidth(0.4)
            c.rect(drawing_x, ly, drawing_w, layer_h, fill=1, stroke=1)
        else:
            # Generic gypsum / standard fill
            c.setFillColor(fill)
            c.setStrokeColor(INK)
            c.setLineWidth(0.4)
            c.rect(drawing_x, ly, drawing_w, layer_h, fill=1, stroke=1)

        # Center y for callouts
        layer_centers[lid] = ly + layer_h / 2

        cur_y = ly

    # EXT / INT axis labels
    c.setFillColor(DARK_GREY)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(drawing_x, drawing_y + drawing_h + 0.02 * inch, "EXTERIOR")
    c.drawString(drawing_x, drawing_y - 0.10 * inch, "INTERIOR (room)")

    # Callouts
    callout_x = drawing_x + drawing_w + 0.10 * inch
    callout_text_x = callout_x + 0.10 * inch
    callout_w = (x + w) - callout_text_x - pad
    c.setFont("Helvetica", 6.8)
    c.setFillColor(INK)
    for (lid, text) in callouts:
        if lid not in layer_centers:
            continue
        cy = layer_centers[lid]
        # Leader line from layer to callout text
        c.setStrokeColor(DARK_GREY)
        c.setLineWidth(0.4)
        c.line(drawing_x + drawing_w, cy, callout_x, cy)
        c.circle(callout_x, cy, 0.018 * inch, fill=1, stroke=0)
        # Wrap text to fit callout column
        _draw_wrapped_text(c, text, callout_text_x, cy, callout_w,
                           font_name="Helvetica", font_size=6.8,
                           leading=8.0)


def _draw_wrapped_text(c, text, x, y_center, max_w, font_name, font_size, leading):
    """Draw text wrapped to max_w, vertically centered around y_center."""
    c.setFont(font_name, font_size)
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, font_name, font_size) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    total_h = leading * (len(lines) - 1)
    start_y = y_center + total_h / 2 - font_size * 0.32
    for i, line in enumerate(lines):
        c.drawString(x, start_y - i * leading, line)


# Layer composition for each assembly
# Each layer: (thickness_units, fill, hatch_unused, layer_id)
# Units are relative; only ratios matter within a single detail.

def cfw_1a_layers():
    return [
        # Exterior at top
        (3.0, "CONTAINER_CORR", None, "skin"),
        (1.5, "AIR", None, "air"),
        (5.0, "STUD", None, "studs"),    # stud cavity (insulation optional)
        (0.6, GYPSUM_FILL, None, "gyp_base"),
        (0.3, MID_GREY, None, "qset"),  # ProForm Quick-Set
        (0.6, GYPSUM_FILL, None, "gyp_face"),
    ]


def cfw_1a_callouts():
    return [
        ("skin", "Existing 14-ga corrugated COR-TEN A container side wall (non-rated, weather barrier)"),
        ("air", "Air gap behind stud cavity (corrugation depth)"),
        ("studs", "3-5/8\" steel studs @ 24\" o.c. max. Cavity insul. optional per V497."),
        ("gyp_base", "Base layer 5/8\" Type X Fire-Shield gypsum board"),
        ("qset", "ProForm Quick-Set setting compound between layers (per V497 2-layer variant)"),
        ("gyp_face", "Face layer 5/8\" Type X Fire-Shield gypsum board, joints taped & finished per GA-216"),
    ]


def cfw_1b_layers():
    return [
        (3.0, "CONTAINER_CORR", None, "skin"),
        (1.5, "AIR", None, "air"),
        (5.0, "STUD", None, "studs"),
        (0.6, GYPSUM_FILL, None, "gyp1"),
        (0.6, GYPSUM_FILL, None, "gyp2"),
        (0.6, GYPSUM_FILL, None, "gyp3"),
    ]


def cfw_1b_callouts():
    return [
        ("skin", "Existing 14-ga corrugated COR-TEN A container side wall (non-rated)"),
        ("air", "Air gap behind stud cavity"),
        ("studs", "3-5/8\" steel studs @ 24\" o.c. max. Cavity insul. optional per V497."),
        ("gyp1", "Base layer 5/8\" Type X, fastened 24\" o.c. (1\" Type S screws)"),
        ("gyp2", "Middle layer 5/8\" Type X, fastened 24\" o.c. (1-5/8\" screws), joints staggered"),
        ("gyp3", "Face layer 5/8\" Type X, fastened 12\" o.c. (2-1/4\" screws), joints staggered, taped & finished"),
    ]


def cfw_2_layers():
    return [
        (3.0, "CONTAINER_CORR", None, "skin"),
        (1.5, "AIR", None, "air"),
        (5.0, "STUD", None, "studs"),
        (0.55, GYPSUM_FILL, None, "gyp1"),
        (0.55, GYPSUM_FILL, None, "gyp2"),
        (0.55, GYPSUM_FILL, None, "gyp3"),
        (0.55, GYPSUM_FILL, None, "gyp4"),
    ]


def cfw_2_callouts():
    return [
        ("skin", "Existing 14-ga corrugated COR-TEN A container side wall (non-rated)"),
        ("air", "Air gap behind stud cavity"),
        ("studs", "3-5/8\" steel studs @ 24\" o.c. max. Cavity insul. optional per V497."),
        ("gyp1", "Base layer 5/8\" Type X"),
        ("gyp2", "Layer 2 \u2014 5/8\" Type X, joints staggered"),
        ("gyp3", "Layer 3 \u2014 5/8\" Type X, joints staggered"),
        ("gyp4", "Outer face layer \u2014 5/8\" Type X, joints staggered, taped & finished"),
    ]


def cfw_1e_layers():
    return [
        (0.4, "INTUMESC", None, "intu"),
        (3.0, "CONTAINER_CORR", None, "skin"),
        (1.5, "AIR", None, "air"),
        (5.0, "STUD", None, "studs"),
        (0.6, GYPSUM_FILL, None, "gyp1"),
        (0.6, GYPSUM_FILL, None, "gyp2"),
        (0.6, GYPSUM_FILL, None, "gyp3"),
    ]


def cfw_1e_callouts():
    return [
        ("intu", "UL-listed intumescent coating, 1HR rating on steel substrate (Carboline Nullifire SC902, PPG Pitt-Char NX, or eq.). Apply per listed DFT over SSPC-SP6 prep + manufacturer primer. Topcoat for exterior exposure."),
        ("skin", "Existing 14-ga corrugated COR-TEN A container side wall"),
        ("air", "Air gap"),
        ("studs", "3-5/8\" steel studs @ 24\" o.c. max"),
        ("gyp1", "Base layer 5/8\" Type X"),
        ("gyp2", "Middle layer 5/8\" Type X, joints staggered"),
        ("gyp3", "Face layer 5/8\" Type X, joints staggered, taped & finished"),
    ]


def cfw_2e_layers():
    return [
        (0.6, "INTUMESC", None, "intu"),
        (3.0, "CONTAINER_CORR", None, "skin"),
        (1.5, "AIR", None, "air"),
        (5.0, "STUD", None, "studs"),
        (0.55, GYPSUM_FILL, None, "gyp1"),
        (0.55, GYPSUM_FILL, None, "gyp2"),
        (0.55, GYPSUM_FILL, None, "gyp3"),
        (0.55, GYPSUM_FILL, None, "gyp4"),
    ]


def cfw_2e_callouts():
    return [
        ("intu", "UL-listed intumescent coating, 2HR rating on steel substrate (per X-series UL design). Apply per listed DFT (typ. 3.0\u20134.0 mm) over SSPC-SP6 + primer + topcoat."),
        ("skin", "Existing 14-ga corrugated COR-TEN A container side wall"),
        ("air", "Air gap"),
        ("studs", "3-5/8\" steel studs @ 24\" o.c. max"),
        ("gyp1", "Base layer 5/8\" Type X"),
        ("gyp2", "Layer 2 \u2014 5/8\" Type X, joints staggered"),
        ("gyp3", "Layer 3 \u2014 5/8\" Type X, joints staggered"),
        ("gyp4", "Outer face layer \u2014 5/8\" Type X, joints staggered, taped & finished"),
    ]


ASSEMBLIES = [
    ("CFW-1A", "1 HR", "Per IBC \u00a7703.2.2(1)", "UL V497  \u00b7  2-layer + Quick-Set",
     cfw_1a_layers, cfw_1a_callouts),
    ("CFW-1B", "1 HR", "Per IBC \u00a7703.2.2(1)", "UL V497  \u00b7  3-layer",
     cfw_1b_layers, cfw_1b_callouts),
    ("CFW-2",  "2 HR", "Per IBC \u00a7703.2.2(1)", "UL V497  \u00b7  4-layer",
     cfw_2_layers, cfw_2_callouts),
    ("CFW-1E", "1 HR  \u2194", "Per IBC \u00a7703.2.2(4)", "V497 + intumescent (1HR)",
     cfw_1e_layers, cfw_1e_callouts),
    ("CFW-2E", "2 HR  \u2194", "Per IBC \u00a7703.2.2(4)", "V497 + intumescent (2HR)",
     cfw_2e_layers, cfw_2e_callouts),
]


def main():
    c = setup_canvas()
    draw_sheet_title_bar(c)

    # Draw the five details
    for i, (tag, rating, basis, sub, layers_fn, callouts_fn) in enumerate(ASSEMBLIES):
        x = DRAW_LEFT + i * (DETAIL_W + DETAIL_GAP)
        y = DRAW_BOTTOM
        sub_y = draw_detail_frame(c, x, y, DETAIL_W, DETAIL_H,
                                  tag, rating, basis, sub)
        # Draw assembly inside the available area below sub_y
        draw_assembly(c, x, y, DETAIL_W, sub_y - y,
                      layers_fn(), callouts_fn())

    draw_code_basis_block(c)
    draw_title_block(c)

    c.showPage()
    c.save()
    print(f"Wrote {OUTFILE}")


if __name__ == "__main__":
    main()
