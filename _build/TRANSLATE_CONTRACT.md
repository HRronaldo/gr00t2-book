# 翻译契约（TRANSLATION CONTRACT）— 违反任一条即视为任务失败

你在为一份中英对照学习读本翻译 NVIDIA《GR00T 2》技术报告（135 页 PDF，2026 年 11 月）。
读者是中文母语的机器人学习研究者，他要用这份读本**逐段精读**原文。

## 输入

- `blocks/chunk_XX.json`：`{chunk_id, sections, pages, blocks:[{id, page, kind, text, section, asset?, crop?}]}`
- `GLOSSARY.md`：术语账本，**强制标准**

## 输出

只写一个文件 `chunks/chunk_XX.md`，内容**只有**按 JSON 中 blocks 原始顺序排列的区块，不加任何前言、总结、结语、分隔线或编号列表。

### 区块模板

正文（kind = prose）：

```
<a id="S012"></a>
**Source:** p.6 S012

**Original:** <JSON 中 text 字段的逐字原文>

**中文:** <忠实中文翻译>
```

图注/表注（kind = caption，且 JSON 含 asset）：

```
![F001](assets/F001.png)

<a id="C001"></a>
**Source:** p.4 C001 · 图 F001

**Original (caption):** <逐字原文>

**中文（图注）：** <图注翻译>
```

表注把 `图` 换成 `表`、`中文（图注）` 换成 `中文（表注）`；`asset` 以 `T` 开头即表。

标题（kind = heading）：

```
### <逐字英文标题> ｜ <中文译名>
```

公式（kind = equation，含 crop）：

```
![E001](assets/equations/E001.png)

<a id="E001"></a>
**Source:** p.52 E001

**Original:** <逐字原文>

**中文:** <说明该公式在讲什么；公式本体放在 $$...$$ 内原样保留>
```

## 硬性规则

1. **逐字保留英文**：`**Original:**` 后必须与 JSON `text` 字段完全一致，只允许把多余空白压成一个空格。不得改写、缩写、纠错、补字。
2. **不得增删区块**：JSON 有多少个 block，就输出多少个区块，顺序一致，id 与页码一致。即使相邻两段读起来像同一段，也不得合并。
3. **不得摘要化**：中文必须完整传达原句信息，禁止把散文压成要点、禁止删掉从句、禁止丢掉限定词（may / can / often / up to）。
4. **术语服从 `GLOSSARY.md`**：同一术语全篇一个译名；不译清单里的名字原样保留英文与大小写。
5. **保留**：数字、单位、百分比、`Sec. 4.2`、`Tab. 27`、`Fig. 12`、`(NVIDIA et al., 2025a)`、引号、破折号 `—`、箭头 `→`、`%`。
6. **公式**：能确认的行内公式用 `$...$`；PDF 抽取残缺（如 `𝐾eff = 𝑠acp 𝑘𝑝`）时原样保留这些字符并追加 `[公式原文见 p.X]`，**绝不臆造 LaTeX**。
7. **不得添加评论**：不写“注：”“译者按”“这里的意思是”。确有必要标注抽取缺陷时，用 `[存疑：…]`。
8. 中文使用书面学术语体，避免口语化；不要用“我们”替代原文的 “we” 以外的泛指。
9. 不要使用 Markdown 表格承载散文。
10. 图片链接路径必须与 JSON 的 `asset` / `crop` 字段一致，不得改动。

## 自检（写完必须执行）

```powershell
python -c "import json,re,sys; d=json.load(open(r'D:\learning\gr00t2_reader\blocks\chunk_XX.json',encoding='utf-8')); s=open(r'D:\learning\gr00t2_reader\chunks\chunk_XX.md',encoding='utf-8').read(); ids=re.findall(r'<a id=\"([^\"]+)\"',s); exp=[b['id'] for b in d['blocks'] if b['kind']!='heading']; print('ids',len(ids),'expected',len(exp),'match',ids==exp); print('orig',s.count('**Original'),'zh',s.count('**中文'))"
```

要求：`match True`，且 `orig` 与 `zh` 计数相等（标题区块不计入 id）。若不满足，修正文件后重新自检，直到通过。

## 交付报告

一句话：写入区块数、自检结果。若某区块无法翻译（例如全是乱码），说明该 id 与原因，并在文件中保留原文与 `[存疑：抽取失败]`。
