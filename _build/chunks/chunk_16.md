### C.4. Data Annotations ｜ C.4. 数据标注

<a id="S1145"></a>
**Source:** p.63 S1145

**Original:** We built Flora (Leng et al., 2026), the data engine that annotates training data for GR00T 2 models. Flora consists of three models: Flora-TempSeg localizes actions in time, Flora-Captioner describes each localized action, and Flora-Rewarder produces outcome, dense, and rubric-based rewards. They are trained on opensource, licensed, and in-house data, where human annotators provide dense timestamped captions and action-quality labels under detailed labeling guidelines. The same models label human egocentric video and robot recordings from parallel-gripper and dexterous-hand embodiments, with one or more synchronized camera views.

**中文:** 我们构建了 Flora（Leng et al., 2026），这是为 GR00T 2 模型标注训练数据的数据引擎。Flora 由三个模型组成：Flora-TempSeg 在时间上定位动作，Flora-Captioner 为每个定位后的动作生成描述，Flora-Rewarder 产生结果奖励、稠密奖励以及基于评分量表的奖励。这些模型在开源数据、授权数据和内部数据上训练，其中人工标注员依据详细的标注指南，提供带时间戳的稠密字幕和动作质量标签。同一批模型还为来自平行夹爪本体和灵巧手本体、带有一个或多个同步相机视角的人类第一人称视角（egocentric）视频与机器人录制数据加注标签。

<a id="S1146"></a>
**Source:** p.64 S1146

**Original:** Timestamped captions. Given an episode video, Flora outputs a set of time intervals, each paired with a caption of the action performed in it. Flora-TempSeg runs on overlapping windows and predicts the start and end time of each action in a window, together with flags that mark actions continuing past the window edges. These predictions are mapped to episode time and stitched into episode-level intervals, while concurrent actions, such as two hands doing different things, remain separate intervals. Flora-Captioner then captions each interval independently. In addition to the frames of the interval, it sees frames from the neighboring actions before and after it, which help resolve object identity and intent, while the caption describes only the target interval. Synchronized camera views are tiled into one image per time step. Each caption is a self-contained imperative instruction that names the intended action, the objects, the role of each hand or arm, and relevant spatial relations, for example “hold tea leaves with right hand, pass tea leaves to left hand”. Failed attempts are captioned with their intended goal, without implying success. Both models are first fine-tuned on human-annotated captions and then trained with GRPO (Shao et al., 2024) on verifiable rewards: temporal F1 and boundary accuracy for Flora-TempSeg, and reference-grounded coverage of caption requirements with a penalty for factual errors for Flora-Captioner.

**中文:** 带时间戳的字幕。给定一段片段视频，Flora 输出一组时间区间，每个区间配有一条对该区间内所执行动作的描述。Flora-TempSeg 在重叠的窗口上运行，预测窗口内每个动作的起止时间，并附带标记，指示动作是否延续到窗口边缘之外。这些预测被映射回片段时间，并拼接成片段级区间；同时发生的动作（例如双手分别做不同的事）仍保持为独立区间。随后，Flora-Captioner 独立地为每个区间生成描述。除该区间的帧之外，它还能看到其前后相邻动作的帧，这些帧有助于确定物体身份与意图，而描述只针对目标区间。同步的相机视角在每个时间步被拼接成一张图像。每条描述都是自包含的祈使句指令，写明预期动作、涉及的物体、每只手或手臂的角色以及相关的空间关系，例如“用右手拿茶叶，把茶叶递给左手”。失败的尝试会按其预期目标进行描述，且不暗示成功。两个模型都先在人工标注的字幕上进行微调，然后以可验证的奖励通过 GRPO（Shao et al., 2024）训练：Flora-TempSeg 的奖励为时序 F1 与边界精度，Flora-Captioner 的奖励为对字幕要求的参考对齐覆盖度，并对事实性错误施加惩罚。

<a id="S1147"></a>
**Source:** p.64 S1147

**Original:** Quality and cost. On WGO-Bench (Macrodata Labs, 2026), Flora achieves the best temporal segmentation F1 of all evaluated models, 50.3 versus 46.0 for the next-best model, GPT-6 Astra (OpenAI, 2026). On our 300-episode in-house captioning benchmark, it leads all models on human episodes and ranks second to Astra on robot episodes.

**中文:** 质量与成本。在 WGO-Bench（Macrodata Labs, 2026）上，Flora 取得了所有被评测模型中最佳的时序分割 F1，为 50.3，而次优模型 GPT-6 Astra（OpenAI, 2026）为 46.0。在我们内部的 300 个片段字幕基准上，它在人类片段上领先所有模型，在机器人片段上仅次于 Astra，排名第二。

<a id="S1148"></a>
**Source:** p.64 S1148

**Original:** Annotating GR00T 2 data. For GR00T 2, Flora turns raw episodes into training-ready supervision. These instructions provide fine-grained language conditioning for pretraining. At the production rate above, relabeling the roughly 400k hours of Human-1M data used by GR00T 2 takes about two days.

**中文:** 为 GR00T 2 标注数据。对于 GR00T 2，Flora 将原始片段转化为可直接用于训练的监督信号。这些指令为预训练提供细粒度的语言条件。按上文所述的生产速率，为 GR00T 2 重新标注其所用的约 400k 小时 Human-1M 数据，大约需要两天。

### D. Real-World Benchmarking with GearArena ｜ D. 基于 GearArena 的真实世界基准测试

<a id="S1149"></a>
**Source:** p.65 S1149

**Original:** This appendix describes how we benchmark GR00T 2 on real robots: why we aggregate real-robot evaluations into a single leaderboard and why that leaderboard is built from blinded A/B comparisons (Sec. D.1), how the evaluation tasks are designed (Sec. D.2), how the arena is organized (Sec. D.3), the rating model (Sec. D.4), the A/B evaluation infrastructure (Sec. D.5), what the arena shows about GR00T 2 (Sec. D.6), and its limitations (Sec. D.7). Tab. 12 summarizes the evidence behind every number in this appendix.

**中文:** 本附录描述我们如何在真实机器人上对 GR00T 2 进行基准测试：为何将真实机器人评测汇总为单一排行榜，以及为何该排行榜基于盲式 A/B 比较构建（Sec. D.1）；评测任务如何设计（Sec. D.2）；竞技场如何组织（Sec. D.3）；评分模型（Sec. D.4）；A/B 评测基础设施（Sec. D.5）；竞技场揭示了关于 GR00T 2 的哪些信息（Sec. D.6），以及其局限性（Sec. D.7）。Tab. 12 概括了本附录中每个数字背后的证据依据。

![T012](assets/T012.png)

<a id="C045"></a>
**Source:** p.65 C045 · 表 T012

**Original (caption):** Table 12: GearArena at a glance (snapshot of November 6, 2026, 12:28 PT). A campaign is one A/B evaluation request, a trial runs every arm once on the same scene, a rollout is one graded robot episode, and a match is one pairwise comparison inside a trial. The three suites are separate leagues whose ratings are not comparable with each other. Five YAM campaigns ran tasks of both YAM suites and are counted in both columns, so the two YAM suites hold 195 distinct campaigns. †Dex records list stations by service identifier and do not record the operator.

**中文（表注）：** 表 12：GearArena 概览（2026 年 11 月 6 日 12:28 PT 快照）。评测批次（campaign）即一次 A/B 评测请求；试次（trial）指在同一场景中让每个臂各运行一次；rollout（轨迹采样）即一条经过评分的机器人片段；对战（match）即某次试次中的一次两两比较。三个套件是彼此独立的联赛，其评分之间不可比较。有五个 YAM 评测批次同时运行了两个 YAM 套件的任务，因此在两列中各计一次，两个 YAM 套件合计包含 195 个不重复的评测批次。†Dex 记录按服务标识符列出工位，且不记录操作员。

<a id="S1152"></a>
**Source:** p.65 S1152

**Original:** Graded trials 2,167 3,403 721 Graded rollouts 6,373 9,671 2,146 Pairwise matches (ties) 5,732 (30%) 6,035 (35%) 1,492 (33%) Tasks with matches 16 74 names (38 tasks) 56 Evidence window Jul 15 – Nov 6 Sep 21 – Nov 6 Sep 29 – Oct 29

**中文:** 已评分试次 2,167 3,403 721 已评分 rollout 6,373 9,671 2,146 两两对战（含平局） 5,732（30%） 6,035（35%） 1,492（33%） 含对战的任务数 16 74 names（38 个任务） 56 证据窗口 7 月 15 日 – 11 月 6 日 9 月 21 日 – 11 月 6 日 9 月 29 日 – 10 月 29 日 [存疑：原文为扁平化的单行文本，各列与数值的对应关系无法从抽取文本确认]

### D.1. Why Aggregate Real-Robot Evaluations, and Why A/B ｜ D.1. 为何汇总真实机器人评测，以及为何采用 A/B 比较

<a id="S1153"></a>
**Source:** p.65 S1153

**Original:** Real-robot evaluations are expensive but cumulative. A real-robot evaluation costs robot time, an operator, a staged scene, and grading. Each one answers a narrow question, but over months the evaluations of a project add up to far more evidence than any single study could afford. The question is whether that evidence can be pooled: a model trained in October should be comparable with one trained in July, even though they were never run side by side.

**中文:** 真实机器人评测成本高昂，但具有累积性。一次真实机器人评测需要占用机器人时间、操作员、搭建好的场景以及评分工作。每次评测只回答一个狭窄的问题，但经过数月，一个项目的评测加起来所提供的证据，远超任何单项研究所能负担的量。问题在于这些证据能否被合并：十月训练的模型应当可以与七月训练的模型进行比较，即便二者从未被并排运行过。

<a id="S1154"></a>
**Source:** p.65 S1154

**Original:** Absolute scores drift. Success rate and rubric score are not stable across evaluation sessions. They depend on the station (arm calibration, cameras, lighting, wear), on the operator (how a scene is staged and how borderline outcomes are graded), and on the day. Two checkpoints evaluated in different sessions therefore differ by their skill and by the drift between the sessions, and the two cannot be separated after the fact. The arena makes this concrete: it can also construct derived comparisons from independent evaluations of two checkpoints on the same task within 45 days, but because those comparisons cross sessions, it down-weights them to at most a quarter of a blinded comparison and excludes them from the default leaderboard.

**中文:** 绝对分数会漂移。成功率和评分量表得分在不同评测会话之间并不稳定。它们取决于工位（机械臂标定、相机、光照、磨损）、操作员（场景如何搭建、临界结果如何评分）以及当天的情况。因此，在不同会话中评测的两个检查点，其差异既包含各自的能力，也包含会话之间的漂移，而二者在事后无法被分离。竞技场使这一点变得具体：它还能从对同一任务、相隔 45 天以内的两个检查点的独立评测中构造派生比较；但由于这些比较跨越了会话，竞技场会将其权重降至盲式比较的至多四分之一，并将其排除在默认排行榜之外。

<a id="S1155"></a>
**Source:** p.65 S1155

**Original:** A/B comparisons cancel the drift. In a blinded A/B trial, two to four checkpoints run in randomized order on the same staged scene, on the same station, by the same operator, within minutes, and the operator does not know which checkpoint is which (Sec. D.5). Whatever the session does to one checkpoint it does to the others, so the comparison is free of the drift that corrupts the absolute score. Pairwise outcomes from many such trials can then be fit jointly into one rating scale (Sec. D.4), in the same way that Chatbot Arena ranks language models from pairwise human preferences (Chiang et al., 2024). Three differences from that setting shape our design. Robot checkpoints are frozen, so all history can be pooled in one batch fit rather than updated sequentially. The comparisons from one trial share a scene and are correlated, so uncertainty must be estimated at the level of scenes. Each checkpoint has tens to hundreds of comparisons rather than thousands, so confidence intervals are essential.

**中文:** A/B 比较消除了漂移。在盲式 A/B 试验中，两到四个检查点以随机顺序，在同一搭建好的场景、同一工位、由同一操作员、几分钟之内运行，且操作员不知道哪个检查点是哪个（Sec. D.5）。会话对某个检查点造成的任何影响，同样会作用于其他检查点，因此该比较不受那种会破坏绝对分数的漂移影响。来自大量此类试验的两两结果随后可以被联合拟合到同一个评分尺度上（Sec. D.4），这与 Chatbot Arena 从两两人类偏好中对语言模型排名的做法相同（Chiang et al., 2024）。与该场景相比，有三点差异塑造了我们的设计。机器人检查点是冻结的，因此所有历史数据可以在一次批量拟合中汇总，而无需顺序更新。同一试验中的比较共享一个场景并彼此相关，因此不确定性必须在场景层面估计。每个检查点只有数十到数百次比较，而非数千次，因此置信区间至关重要。

![F034](assets/F034.png)

<a id="C046"></a>
**Source:** p.66 C046 · 图 F034

**Original (caption):** Figure 34: Gauging the current suite. Mean rubric score (bars) and full-credit rate (dots) per task over all graded A/B rollouts on YAM V2, grouped by sub-suite and ordered by task code (M05* is a variant of M05 with 20 rollouts). No task is near the ceiling, and six sit in the shelving zone, where nearly every rollout fails.

**中文（图注）：** 图 34：对当前套件的衡量。图中在 YAM V2 上所有已评分的 A/B rollout 基础上，按任务绘制平均评分量表得分（柱）与满分率（点），按子套件分组，并按任务代码排序（M05* 为 M05 的变体，含 20 次 rollout）。没有任何任务接近天花板，其中六个任务位于“搁置区”，该区域几乎每次 rollout 都失败。
