# -*- coding: utf-8 -*-
"""Assemble paper.md + source_map.json from translated chunks."""
import json, os, re, sys

OUT = r"D:\learning\gr00t2-book"
raw = json.load(open(os.path.join(OUT, "_build", "source_map_raw.json"), encoding="utf-8"))
blocks = raw["blocks"]
figures = raw["figures"]
manifest = json.load(open(os.path.join(OUT, "_build", "blocks", "manifest.json"), encoding="utf-8"))

head_map = {}
for b in blocks:
    if b["kind"] == "heading":
        head_map[b["text"]] = b

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

PARTS = {"chunk_10": ["chunk_10a", "chunk_10b"], "chunk_14": ["chunk_14a", "chunk_14b"]}

parts = []
missing = []
for m in manifest:
    names = PARTS.get(m["chunk_id"], [m["chunk_id"]])
    texts = []
    for name in names:
        p = os.path.join(OUT, "_build", "chunks", name + ".md")
        if not os.path.isfile(p):
            missing.append(name)
            continue
        texts.append(open(p, encoding="utf-8").read())
    parts.extend(texts)

body = "\n\n".join(parts)
body = body.replace("**中文（图注）：**", "**中文图注：**").replace("**中文（表注）：**", "**中文表注：**")
body = body.replace("**中文（图注）:**", "**中文图注：**").replace("**中文（表注）:**", "**中文表注：**")
body = body.replace("**中文：**", "**中文:**")

def fix_heading(m):
    en = norm(m.group(2))
    zh = m.group(3).strip()
    rec = head_map.get(en)
    if rec:
        hashes = "##" if rec.get("level", 2) == 1 else "###"
        return f'<a id="{rec["id"]}"></a>\n{hashes} {en} ｜ {zh}'
    return m.group(0)

body = re.sub(r"^(#{1,6})\s+(.+?)\s*｜\s*(.+)$", fix_heading, body, flags=re.MULTILINE)
body = re.sub(r"(\*\*中文(?:图注|表注)：\*\*)\s*(?:图注|表注)：", r"\1", body)
body = re.sub(r"(!\[[^\]]*\]\([^)]*\))\n\n(<a id=\"[SCE]\d+\"></a>\n\*\*Source:\*\* [^\n]+)\n",
              r"\2\n\n\1\n", body)

body = re.sub(r'(<a id="[SCE]\d+"></a>)\n(!\[[^\]]*\]\([^)]*\))\n\n(\*\*Source:\*\* [^\n]+)\n',
              r'\1\n\3\n\n\2\n', body)

for b in blocks:
    if b["kind"] != "caption" or not b.get("asset"):
        continue
    img = f'![{b["asset"]}](assets/{b["asset"]}.png)'
    if img in body:
        continue
    marker = f'<a id="{b["id"]}"></a>\n**Source:** '
    idx = body.find(marker)
    if idx == -1:
        continue
    src_at = body.find("**Source:**", idx)
    nl = body.find("\n", src_at)
    body = body[:nl + 1] + f"\n{img}\n" + body[nl + 1:]

for b in blocks:
    if b["kind"] != "equation":
        continue
    img = f'![{b["id"]}]({b["crop"]})'
    if img in body:
        continue
    body = body.replace(f'<a id="{b["id"]}"></a>', img + "\n\n" + f'<a id="{b["id"]}"></a>')

sections = [b for b in blocks if b["kind"] == "heading" and b["section"] not in
            ("Front matter", "Contents", "References")]
seen = set()
toc_lines = []
for b in sections:
    if b["id"] in seen:
        continue
    seen.add(b["id"])
    indent = "" if b.get("level", 2) == 1 else "  "
    toc_lines.append(f'{indent}- [{b["text"]}](#{b["id"]}) · p.{b["page"]}')

eq_blocks = [b for b in blocks if b["kind"] == "equation"]
eq_index = "\n".join(f'| {b["id"]} | p.{b["page"]} | {b["text"][:90].replace("|", "/")} |' for b in eq_blocks)

header = f"""# GR00T 2：面向泛化、灵巧与自适应的机器人基础模型（中英对照精读本）

**原文**：GR00T 2: Scaling Robot Foundation Models for Generalization, Dexterity, and Adaptation
**发布**：NVIDIA，2026 年 11 月 · 项目页 https://research.nvidia.com/labs/gear/gr00t-2
**本地原件**：`D:\\learning\\gr00t2_whitepaper.pdf`（135 页，含附录 A–K）
**本读本**：全文段落级中英对照，图表按原文位置就近插入，每个区块带 `p.页码 + 区块号` 锚点，可回原文逐字核对。

## 怎么用这份读本

1. 先读 `学习指南.md` 的第 1 讲，建立全局地图；再回到本文件按章精读。
2. 每个区块的 `**Source:**` 行给出 PDF 页码与区块号（S=正文，C=图注/表注，E=公式，H=小节）。
3. `**Original:**` 与 PDF 抽取文本逐字一致，可用于核对术语与数字；`**中文:**` 是对应译文。
4. 图表以 PNG 从原 PDF 裁切，插在其图注所在位置；个别无法精确裁切的图表退化为整页渲染，已在 `translation_notes.md` 标注。

## 目录（点击跳转）

{chr(10).join(toc_lines)}

---

## 公式索引

| 编号 | 页码 | 原文（抽取文本） |
|---|---|---|
{eq_index}

> 公式以原 PDF 裁切图为准；抽取文本中的数学字符常有残缺，凡不能确证者一律保留原字符并标注，不臆造 LaTeX。详见 `translation_notes.md`。

---

"""

footer = f"""

---

## 术语表（全篇统一）

见 `GLOSSARY.md`。核心对照：world-action model（WAM）= 世界-动作模型；embodiment = 本体；
x-adapt = 跨本体适配；loco-manipulation = 移动操作；teleoperation = 遥操作；
post-training = 后训练；action chunk = 动作块；code-as-policy（CaP）= 代码即策略。

## 阅读提示（读完正文后再看）

1. 这份报告的主张不是"更大的 VLA"，而是**把动作预测与世界模型绑在同一个去噪过程里**：动作 token 可以 attend 到模型正在生成的未来帧，因此动作能"跟着想象走"。判断其价值时，重点看 Sec. 2 的注意力结构与 Sec. 4.1 的联合流匹配目标是否真的支撑了 Sec. 3.2 的跨本体结论。
2. "X-Adapt"是全文最强的概念主张，也是最需要警惕的一处：它用人类/UMI 数据替代目标机器人遥操作数据。附录 B 给出的每个数字都绑定特定任务集与特定本体，读时务必确认"零样本"到底相对于什么分布。
3. 评测部分是这份报告最反常规的地方（附录 D 的 GearArena）。它用 A/B 配对比较与 Elo 而不是单一成功率，理由在 D.1。若你关心"如何可信地比较机器人策略"，D 章比正文更有价值。
4. 附录 F（RL 后训练）与附录 J（仿真）是工程含量最高的两章；附录 K 的分布式训练细节对复现最有参考价值。
5. 全文未给出模型参数量以外的训练细节（数据规模、算力总量、训练步数）时，不要假设它可复现——把它当作能力报告而非方法论文来读。
"""

paper = header + body + footer
open(os.path.join(OUT, "_build", "paper-annotated.md"), "w", encoding="utf-8").write(paper)

alias = {}
for m in manifest:
    p = os.path.join(OUT, "_build", "blocks", m["chunk_id"] + ".json")
    if not os.path.isfile(p):
        continue
    for b in json.load(open(p, encoding="utf-8"))["blocks"]:
        for mid in b.get("merged_ids", []):
            alias[mid] = b["id"]

sm = {
    "source": {
        "file": "gr00t2_whitepaper.pdf",
        "title": "GR00T 2: Scaling Robot Foundation Models for Generalization, Dexterity, and Adaptation",
        "publisher": "NVIDIA",
        "date": "2026-11",
        "pages": 135,
    },
    "blocks": [
        {"id": b["id"], "type": b["kind"], "page": b["page"], "section": b["section"],
         **({"image_path": b["crop"], "confidence": "low", "latex": None} if b["kind"] == "equation" else {}),
         **({"asset": b["asset"]} if b.get("asset") else {})}
        for b in blocks if b["kind"] != "label"
    ] + [
        {"id": mid, "type": "merged", "page": next(x["page"] for x in blocks if x["id"] == sid),
         "merged_into": sid}
        for mid, sid in sorted(alias.items())
    ],
    "equations": [
        {"id": b["id"], "page": b["page"], "confidence": "low", "latex": None,
         "image_path": b["crop"], "printed_text": b["text"]}
        for b in blocks if b["kind"] == "equation"
    ],
    "figures": [{"id": r["id"], "page": r["page"], "kind": r["kind"], "file": r["file"],
                 "fallback_page_render": r["fallback"], "caption": r["caption"][:200]}
                for r in figures],
}
json.dump(sm, open(os.path.join(OUT, "source_map.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

print("paper.md chars:", len(paper))
print("chunks missing:", missing)
print("blocks in map:", len(sm["blocks"]), "figures:", len(sm["figures"]), "equations:", len(sm["equations"]))
print("orig count:", paper.count("**Original"), "zh count:", paper.count("**中文"))
print("display math:", paper.count("$$") // 2, "E anchors:", len(re.findall(r'<a id="E\d+', paper)))
