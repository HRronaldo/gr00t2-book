# -*- coding: utf-8 -*-
"""Build a block-level source map + figure/table/equation crops for the GR00T 2 whitepaper."""
import json, os, re, sys
import pymupdf

SRC = r"D:\learning\gr00t2_whitepaper.pdf"
OUT = r"D:\learning\gr00t2_reader"
ASSETS = os.path.join(OUT, "assets")
os.makedirs(ASSETS, exist_ok=True)

doc = pymupdf.open(SRC)
W, H = doc[0].rect.width, doc[0].rect.height
LEFT, RIGHT = 58.0, 538.0
TOP, BOTTOM = 48.0, 800.0

HEADER_RE = re.compile(r"^GR00T 2: Scaling Robot Foundation Models")
CAP_RE = re.compile(r"^(Figure|Table)\s+([A-Z]?\d+)\s*[:.]")
NUM_ONLY = re.compile(r"^\d{1,3}$")

toc = doc.get_toc()  # [level, title, page]

def norm(s):
    s = s.replace("\u00ad", "")
    s = re.sub(r"-\n(?=[a-z])", "", s)          # rejoin hyphenated line breaks
    s = s.replace("\n", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

def body_font_size(page):
    """most common span size on page"""
    from collections import Counter
    c = Counter()
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                c[round(s["size"], 1)] += len(s["text"])
    return c.most_common(1)[0][0] if c else 10.0

blocks_out = []   # ordered list of dicts
figs, tabs, eqs = [], [], []
cur_section = "Front matter"

# ---- pass 1: collect text blocks per page
page_blocks = {}
for pno in range(doc.page_count):
    page = doc[pno]
    bfs = body_font_size(page)
    items = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        x0, y0, x1, y1 = b["bbox"]
        if y1 < TOP or y0 > BOTTOM:
            continue
        txt = "".join(s["text"] for l in b["lines"] for s in l["spans"])
        raw = "\n".join("".join(s["text"] for s in l["spans"]) for l in b["lines"])
        if HEADER_RE.match(txt.strip()) or NUM_ONLY.match(txt.strip()):
            continue
        sizes = [round(s["size"], 1) for l in b["lines"] for s in l["spans"]]
        maxsz = max(sizes) if sizes else bfs
        bold = any("Bold" in s["font"] or "Semibold" in s["font"] or "bold" in s["font"]
                   for l in b["lines"] for s in l["spans"])
        items.append(dict(bbox=[x0, y0, x1, y1], text=norm(raw), maxsz=maxsz,
                          bold=bold, bfs=bfs, page=pno + 1))
    items.sort(key=lambda d: (round(d["bbox"][1], 1), d["bbox"][0]))
    page_blocks[pno + 1] = items

# ---- pass 2: classify
toc_titles = {}
for lvl, title, pg in toc:
    toc_titles.setdefault(pg, []).append((lvl, norm(title)))

for pno in range(1, doc.page_count + 1):
    items = page_blocks[pno]
    for idx, it in enumerate(items):
        t = it["text"]
        m = re.search(r"(Figure|Table)\s+[A-Z]?\d+\s*[:.]", t)
        if m and m.start() <= 90 and m.start() > 0:
            t = t[m.start():]
            it["text"] = t
        is_cap = bool(CAP_RE.match(t))
        # heading detection: matches TOC title on this page, short, larger/bold font
        is_head = False
        for lvl, title in toc_titles.get(pno, []):
            if t == title or (t.startswith(title) and len(t) - len(title) < 4):
                is_head = True
                it["level"] = lvl
                break
        if not is_head and it["maxsz"] > it["bfs"] + 1.2 and len(t) < 90 and not is_cap:
            is_head = True
            it["level"] = 2
        is_eq = (re.search(r"\(\d+[a-z]?\)\s*$", t) and len(t) < 220
                 and re.search(r"[=≈∑∇∈∏√^_∑∫]", t) and not is_cap)
        if is_cap:
            it["kind"] = "caption"
        elif is_head:
            it["kind"] = "heading"
        elif is_eq:
            it["kind"] = "equation"
        else:
            it["kind"] = "prose"
    # order within page: use y then x already

# ---- pass 3: assign ids + sections in reading order
sec_counter = 0
for pno in range(1, doc.page_count + 1):
    for it in page_blocks[pno]:
        if it["kind"] == "heading":
            cur_section = it["text"]
            blocks_out.append(dict(id=None, page=pno, kind="heading", text=it["text"],
                                   level=it.get("level", 2), section=cur_section,
                                   bbox=[round(v, 1) for v in it["bbox"]]))
        elif it["kind"] == "caption":
            kind = "table" if it["text"].startswith("Table") else "figure"
            it["cap_kind"] = kind
            blocks_out.append(dict(id=None, page=pno, kind="caption", cap_kind=kind,
                                   text=it["text"], section=cur_section,
                                   bbox=[round(v, 1) for v in it["bbox"]]))
        elif it["kind"] == "equation":
            blocks_out.append(dict(id=None, page=pno, kind="equation", text=it["text"],
                                   section=cur_section,
                                   bbox=[round(v, 1) for v in it["bbox"]]))
        else:
            blocks_out.append(dict(id=None, page=pno, kind="prose", text=it["text"],
                                   section=cur_section,
                                   bbox=[round(v, 1) for v in it["bbox"]]))

counters = dict(prose=0, caption=0, equation=0)
for b in blocks_out:
    if b["kind"] == "prose":
        counters["prose"] += 1; b["id"] = f"S{counters['prose']:03d}"
    elif b["kind"] == "caption":
        counters["caption"] += 1; b["id"] = f"C{counters['caption']:03d}"
    elif b["kind"] == "equation":
        counters["equation"] += 1; b["id"] = f"E{counters['equation']:03d}"

# ---- pass 4: figure / table crops via graphic clustering
def graphic_boxes(page):
    boxes = []
    for im in page.get_image_info():
        x0, y0, x1, y1 = im["bbox"]
        if (x1 - x0) > 8 and (y1 - y0) > 8:
            boxes.append([x0, y0, x1, y1])
    for d in page.get_drawings():
        r = d["rect"]
        if r.height < 2.0 and r.width < 2.0:
            continue
        if r.height < 1.2 and r.width > W * 0.6:   # full-width rule
            continue
        if r.width < 2 and r.height > 40:           # vertical rule
            continue
        boxes.append([r.x0, r.y0, r.x1, r.y1])
    return boxes

def label_boxes(items):
    """short text blocks that belong to figures/tables (labels, cells, sub-captions)"""
    out = []
    for it in items:
        t = it["text"]
        x0, y0, x1, y1 = it["bbox"]
        if it["kind"] in ("caption", "heading"):
            continue
        wide_prose = (x1 - x0) > 380 and len(t) > 260
        if not wide_prose:
            out.append([x0, y0, x1, y1])
    return out

def cluster(boxes, gap=14.0):
    if not boxes:
        return []
    boxes = sorted(boxes, key=lambda b: b[1])
    groups = []
    cur = list(boxes[0])
    for b in boxes[1:]:
        if b[1] <= cur[3] + gap:
            cur = [min(cur[0], b[0]), min(cur[1], b[1]), max(cur[2], b[2]), max(cur[3], b[3])]
        else:
            groups.append(cur); cur = list(b)
    groups.append(cur)
    return groups

fig_records = []
for pno in range(1, doc.page_count + 1):
    page = doc[pno - 1]
    items = page_blocks[pno]
    caps = [it for it in items if it["kind"] == "caption"]
    if not caps:
        continue
    gboxes = graphic_boxes(page) + label_boxes(items)
    groups = cluster(gboxes)
    for it in caps:
        cy0, cy1 = it["bbox"][1], it["bbox"][3]
        kind = "table" if it["text"].startswith("Table") else "figure"
        cand = None
        if kind == "figure":
            above = [g for g in groups if g[3] <= cy0 + 2]
            cand = max(above, key=lambda g: g[3]) if above else None
        else:
            below = [g for g in groups if g[1] >= cy1 - 2]
            cand = min(below, key=lambda g: g[1]) if below else None
        if cand is None:
            prose_above = [b["bbox"][3] for b in items
                           if b["kind"] in ("prose", "heading") and b["bbox"][3] <= cy0 - 2
                           and (b["bbox"][2] - b["bbox"][0]) > 380 and len(b["text"]) > 200]
            prose_below = [b["bbox"][1] for b in items
                           if b["kind"] in ("prose", "heading") and b["bbox"][1] >= cy1 + 2
                           and (b["bbox"][2] - b["bbox"][0]) > 380 and len(b["text"]) > 200]
            if kind == "table":
                top, bot = cy1 - 2, (min(prose_below) - 4 if prose_below else BOTTOM)
            else:
                top, bot = (max(prose_above) + 4 if prose_above else TOP), cy0 + 2
            band = [LEFT, max(TOP, top), RIGHT, min(BOTTOM, bot)]
            fallback = True
        else:
            band = [max(LEFT, cand[0] - 4), max(TOP, cand[1] - 6),
                    min(RIGHT, cand[2] + 4), min(BOTTOM, cand[3] + 6)]
            fallback = False
        fig_records.append(dict(page=pno, kind=kind, caption=it["text"], band=band,
                                fallback=fallback))

# assign F/T ids and render
f_i = t_i = 0
for rec in fig_records:
    if rec["kind"] == "figure":
        f_i += 1; rec["id"] = f"F{f_i:03d}"
    else:
        t_i += 1; rec["id"] = f"T{t_i:03d}"
    x0, y0, x1, y1 = rec["band"]
    if (y1 - y0) < 45 or (x1 - x0) < 60:
        x0, y0, x1, y1 = LEFT, TOP, RIGHT, BOTTOM
        rec["fallback"] = True
        rec["band"] = [x0, y0, x1, y1]
    clip = pymupdf.Rect(x0, y0, x1, y1)
    pix = doc[rec["page"] - 1].get_pixmap(clip=clip, dpi=200)
    path = os.path.join(ASSETS, rec["id"] + ".png")
    pix.save(path)
    rec["file"] = f"assets/{rec['id']}.png"
    rec["size"] = [pix.width, pix.height]

# equation crops
for b in blocks_out:
    if b["kind"] != "equation":
        continue
    x0, y0, x1, y1 = b["bbox"]
    clip = pymupdf.Rect(max(LEFT, x0 - 30), max(TOP, y0 - 6),
                        min(RIGHT, x1 + 30), min(BOTTOM, y1 + 6))
    pix = doc[b["page"] - 1].get_pixmap(clip=clip, dpi=220)
    p = os.path.join(ASSETS, "equations")
    os.makedirs(p, exist_ok=True)
    pix.save(os.path.join(p, b["id"] + ".png"))
    b["crop"] = f"assets/equations/{b['id']}.png"

# link captions <-> figures
cap_to_fig = {}
for rec in fig_records:
    for b in blocks_out:
        if b["kind"] == "caption" and b["page"] == rec["page"] and b["text"] == rec["caption"]:
            b["asset"] = rec["id"]
            cap_to_fig[b["id"]] = rec["id"]
            break

SECNUM_RE = re.compile(r"^(\d+(\.\d+)*|[A-Z](\.\d+)*)\s")
MATHY_RE = re.compile(r"[\U0001D400-\U0001D7FF\u2200-\u22FF]")

for b in blocks_out:
    if b["kind"] == "prose":
        inside = any(r["page"] == b["page"] and r["band"][1] - 2 <= b["bbox"][1]
                     and r["band"][3] + 2 >= b["bbox"][3] for r in fig_records)
        garbled_math = len(b["text"]) < 45 and len(MATHY_RE.findall(b["text"])) >= 1
        if (inside and len(b["text"]) < 220) or garbled_math:
            b["kind"] = "label"
            continue
    if b["kind"] != "heading" or SECNUM_RE.match(b["text"]):
        continue
    for r in fig_records:
        if r["page"] == b["page"] and r["band"][1] <= b["bbox"][1] and r["band"][3] >= b["bbox"][3]:
            b["kind"] = "label"
            break

hid = 0
for b in blocks_out:
    if b["kind"] == "heading":
        hid += 1
        b["id"] = f"H{hid:02d}"

json.dump(dict(blocks=blocks_out, figures=fig_records), open(os.path.join(OUT, "source_map_raw.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# report
prose = [b for b in blocks_out if b["kind"] == "prose"]
print("blocks:", len(blocks_out), "prose:", len(prose), "captions:", len([b for b in blocks_out if b['kind']=='caption']),
      "equations:", len([b for b in blocks_out if b['kind']=='equation']),
      "headings:", len([b for b in blocks_out if b['kind']=='heading']))
print("figures:", len([r for r in fig_records if r['kind']=='figure']),
      "tables:", len([r for r in fig_records if r['kind']=='table']),
      "fallbacks:", len([r for r in fig_records if r['fallback']]))
print("prose chars:", sum(len(b["text"]) for b in prose))
print("linked captions:", len(cap_to_fig))
secs = []
for b in blocks_out:
    if b["kind"] == "heading":
        secs.append((b["page"], b["text"]))
print("headings found:", len(secs))
for s in secs[:40]:
    print("  ", s)
