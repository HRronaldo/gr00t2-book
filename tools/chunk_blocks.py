# -*- coding: utf-8 -*-
"""Pack source blocks into translation chunks."""
import json, os, re

OUT = r"D:\learning\gr00t2_reader"
BLOCKS = os.path.join(OUT, "blocks")
os.makedirs(BLOCKS, exist_ok=True)

SKIP_SECTIONS = {"Front matter", "Contents", "References"}
TARGET = 14000
MAXCH = 17000

raw = json.load(open(os.path.join(OUT, "source_map_raw.json"), encoding="utf-8"))
blocks = [b for b in raw["blocks"]
          if b["kind"] in ("prose", "caption", "equation", "heading")
          and b["section"] not in SKIP_SECTIONS]

merged = []
blocks = [b for b in blocks
          if not (b["kind"] == "prose" and not re.search(r"[A-Za-z]{3,}", b["text"]))]

for b in blocks:
    p = merged[-1] if merged else None
    if (p and p["kind"] == "prose" and b["kind"] == "prose" and p["section"] == b["section"]
            and not re.search(r"[.!?:;\"”’)]$", p["text"]) and re.match(r"[a-z(\[]", b["text"])
            and abs(b["page"] - p["page"]) <= 1):
        p["text"] = p["text"].rstrip() + " " + b["text"].lstrip()
        p["merged_pages"] = sorted(set(p.get("merged_pages", [p["page"]]) + [b["page"]]))
        p.setdefault("merged_ids", []).append(b["id"])
        continue
    merged.append(dict(b))

chunks, cur, cur_chars, cur_sec = [], [], 0, None
for b in merged:
    if b["kind"] == "heading":
        if cur and cur_chars > TARGET * 0.45:
            chunks.append(cur); cur, cur_chars = [], 0
        cur.append(b); cur_sec = b["text"]
        continue
    n = len(b["text"])
    if cur and cur_chars + n > TARGET and b["section"] != cur_sec:
        chunks.append(cur); cur, cur_chars = [], 0
    elif cur and cur_chars + n > MAXCH:
        chunks.append(cur); cur, cur_chars = [], 0
    cur.append(b); cur_chars += n; cur_sec = b["section"]
if cur:
    chunks.append(cur)

manifest = []
for i, ch in enumerate(chunks, 1):
    cid = f"chunk_{i:02d}"
    secs = []
    for b in ch:
        if b["section"] not in secs:
            secs.append(b["section"])
    payload = dict(chunk_id=cid, sections=secs,
                   pages=[min(b["page"] for b in ch), max(b["page"] for b in ch)],
                   chars=sum(len(b["text"]) for b in ch),
                   blocks=[dict(id=b["id"], page=b["page"], kind=b["kind"], text=b["text"],
                                section=b["section"],
                                **({"asset": b["asset"]} if b.get("asset") else {}),
                                **({"merged_ids": b["merged_ids"]} if b.get("merged_ids") else {}),
                                **({"crop": b["crop"]} if b.get("crop") else {}))
                           for b in ch])
    json.dump(payload, open(os.path.join(BLOCKS, cid + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    manifest.append(dict(chunk_id=cid, pages=payload["pages"], chars=payload["chars"],
                         sections=secs))

json.dump(manifest, open(os.path.join(BLOCKS, "manifest.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("chunks:", len(chunks), "total chars:", sum(m["chars"] for m in manifest))
for m in manifest:
    print(f"  {m['chunk_id']}  p{m['pages'][0]}-{m['pages'][1]}  {m['chars']:6d}  {m['sections'][0][:60]}")
