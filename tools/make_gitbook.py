# -*- coding: utf-8 -*-
"""Convert the annotated bilingual reader into Isaac-Lab-style GitBook pages."""
import os, re

ROOT = r"D:\learning\gr00t2-book"
SRC = os.path.join(ROOT, "_build", "paper-annotated.md")
OUTDIR = os.path.join(ROOT, "paper")
os.makedirs(OUTDIR, exist_ok=True)

SLUG = {
    "1": ("01-introduction", "第 1 章 引言"),
    "2": ("02-overview", "第 2 章 GR00T 2 总览"),
    "3": ("03-capabilities", "第 3 章 能力"),
    "4": ("04-method", "第 4 章 我们如何做出 GR00T 2"),
    "5": ("05-conclusion", "第 5 章 结论与开放问题"),
    "A": ("appendix-a-fast-adapt", "附录 A 快速适配"),
    "B": ("appendix-b-x-adapt", "附录 B 跨本体适配"),
    "C": ("appendix-c-data", "附录 C 数据"),
    "D": ("appendix-d-gearena", "附录 D GearArena 真机评测"),
    "E": ("appendix-e-umiverse", "附录 E UMIverse"),
    "F": ("appendix-f-rl-post-training", "附录 F RL 后训练"),
    "G": ("appendix-g-agentic", "附录 G 智能体化"),
    "H": ("appendix-h-loco-manipulation", "附录 H 人形移动操作"),
    "I": ("appendix-i-acceleration", "附录 I 加速"),
    "J": ("appendix-j-simulation", "附录 J 仿真"),
    "K": ("appendix-k-infrastructure", "附录 K 基础设施"),
}

CHAPTER_RE = re.compile(r"^(\d+|[A-K])\.\s")
SUBSEC_RE = re.compile(r"^(\d+\.\d+|[A-K]\.\d+)\.")

text = open(SRC, encoding="utf-8").read()
body = text[text.index('<a id="H'):]

HEAD_RE = re.compile(r'<a id="(H\d+)"></a>\n(#{2,3}) (.+?)\s*｜\s*(.+?)\n')
heads = [(m.start(), m) for m in HEAD_RE.finditer(body)]

BLOCK_RE = re.compile(
    r'<a id="(?P<id>[SCE]\d+)"></a>\s*\n'
    r'\*\*Source:\*\* (?P<src>[^\n]+)\n\n'
    r'(?P<body>.*?)(?=\n\n<a id="[SCE]\d+"></a>|\Z)', re.S)
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def emit_block(m):
    bid, src, chunk = m.group("id"), m.group("src").strip(), m.group("body").strip()
    out = []
    for im in IMG_RE.findall(chunk):
        out.append(f"![{bid}](../{im})")
    rest = IMG_RE.sub("", chunk).strip()
    orig = re.search(r"\*\*Original(?: \(caption\))?:\*\*\s*(.+?)(?=\n\n\*\*|\Z)", rest, re.S)
    zh = re.search(r"\*\*中文(?:图注|表注)?[:：]\*\*\s*(.+?)(?=\n\n\*\*|\Z)", rest, re.S)
    out.append(f'<a id="{bid}"></a>')
    out.append(f"<!-- {src} -->")
    if orig:
        out.append(orig.group(1).strip())
    if zh:
        out.append(zh.group(1).strip())
    return "\n\n".join(out)


chapters, order = {}, []
for idx, (pos, hm) in enumerate(heads):
    end = heads[idx + 1][0] if idx + 1 < len(heads) else len(body)
    seg = body[hm.end():end]
    en, zh = hm.group(3).strip(), hm.group(4).strip()
    page = re.search(r"p\.(\d+)", seg)
    page = int(page.group(1)) if page else 0

    rendered = []
    for m in BLOCK_RE.finditer(seg):
        rendered.append(emit_block(m))
        rendered.append("")

    if CHAPTER_RE.match(en) and not SUBSEC_RE.match(en):
        key = CHAPTER_RE.match(en).group(1)
        slug, zhname = SLUG.get(key, ("misc-" + key, "其他"))
        order.append(key)
        chapters[key] = dict(slug=slug, zh=zhname, en=en, page=page, lines=list(rendered))
    elif order:
        chapters[order[-1]]["lines"].append(f"## {en} · {zh}")
        chapters[order[-1]]["lines"].append("")
        chapters[order[-1]]["lines"].extend(rendered)

written = []
for key in order:
    c = chapters[key]
    first_page = re.search(r"<!-- p\.(\d+)", "\n".join(c["lines"]))
    if first_page:
        c["page"] = int(first_page.group(1))
    head = [
        f"# {c['zh']}",
        "",
        f"> **原文** {c['en']}　·　起于 p.{c['page']}　·　本页中英对照：英文段在前，中文段在后。",
        "",
        "---",
        "",
    ]
    content = "\n".join(head) + "\n".join(c["lines"]).strip() + "\n"
    open(os.path.join(OUTDIR, c["slug"] + ".md"), "w", encoding="utf-8").write(content)
    written.append((c["slug"], c["zh"], len(content)))

print("chapters written:", len(written))
for s, z, n in written:
    print(f"  {s:36s} {z:28s} {n:8d} chars")
