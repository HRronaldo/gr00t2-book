### 4.2. Data ｜ 4.2 数据

<a id="S288"></a>
**Source:** p.15 S288

**Original:** GR00T 2 pretrains on human demonstrations, UMI demonstrations, and robot teleoperation, which play complementary roles. Egocentric human video from Human-1M provides broad coverage of physical interactions and environments, and robot performance grows with the amount of it (Sec. 4.2.1). UMI provides scalable, task-focused demonstrations with robot-compatible action representations (Sec. 4.2.2), and teleoperation grounds the model in embodiment-specific behaviors and executable actions (Sec. 4.2.3). Finally, Flora, our data engine, labels the subtask annotation of human and robot episodes at this scale (Sec. 4.2.4). App. C details the collection, processing, and curation of each source, and Sec. 4.7.3 describes the pipeline that converts raw data into training-ready format.

**中文:** GR00T 2 在人类演示、UMI 演示和机器人遥操作数据上进行预训练，三者各自扮演互补的角色。来自 Human-1M 的第一人称人类视频广泛覆盖了物理交互与环境，并且机器人性能会随其数量增长（Sec. 4.2.1）。UMI 提供可扩展、面向任务的演示，并附带与机器人兼容的动作表示（Sec. 4.2.2）；遥操作则使模型扎根于特定本体的行为与可执行动作（Sec. 4.2.3）。最后，我们的数据引擎 Flora 在这一规模上为人类与机器人片段标注子任务（Sec. 4.2.4）。附录 C 详述了每个数据源的采集、处理与整理，Sec. 4.7.3 描述了把原始数据转换为可训练格式的流程。

<a id="S289"></a>
**Source:** p.15 S289

**Original:** 4.2.1. Human Data

**中文:** 4.2.1. 人类数据

<a id="S290"></a>
**Source:** p.15 S290

**Original:** For a world action model, egocentric human experience captures the motion and visual diversity needed to achieve strong coverage across objects, affordances, tasks, scenes and environments. GR00T 2 leverages 402,730 hours across approximately 13.75 million episodes, spanning over 51,500 unique collectors and 123,000 scenes of high quality egocentric data filtered from Human-1M. The dataset is a 1 million hour egocentric human experience dataset of proficient human labor sensorized with egocentric cameras, dense language annotations, SLAM and 3D hand pose keypoints curated by NVIDIA, spanning demonstrations in both natural “in-the-wild” and controlled studio environments. Additional details on filters and dataset composition in Sec. C.1.

**中文:** 对于世界-动作模型（WAM）而言，第一人称人类经验能够捕捉实现对物体、可供性、任务、场景与环境之间强覆盖所需的运动与视觉多样性。GR00T 2 利用了从 Human-1M 中筛选出的高质量第一人称数据，共计 402,730 小时、约 1,375 万个片段，涵盖超过 51,500 名不同采集者与 123,000 个场景。该数据集是一个包含 100 万小时第一人称人类经验的数据集，记录了熟练的人类劳动，并通过第一人称相机进行传感化采集，附有密集的语言标注、SLAM 与 3D 手部姿态关键点，由 NVIDIA 整理，其演示既包括自然的“野外”（in-the-wild）环境，也包括受控的录影棚环境。筛选条件与数据集构成的更多细节见 Sec. C.1。

<a id="S291"></a>
**Source:** p.15 S291

**Original:** In-lab human data. To enable direct transfer to the target robot embodiment, GR00T 2 contains 3,000 hours of robot-aligned studio data, collected under a stricter protocol. The visual gap is mitigated by matching the egocentric and wrist camera viewpoints, while the motion gap is mitigated by matching demonstration speed with the robot. This data is demonstration-style where each task is demonstrated hundreds of times with a repeatable strategy (Sec. C.1.3).

**中文:** 实验室内人类数据。为了直接迁移到目标机器人本体，GR00T 2 包含 3,000 小时与机器人对齐的录影棚数据，采用更严格的协议采集。视觉差距通过匹配第一人称相机与腕部相机的视角来缓解，运动差距则通过使演示速度与机器人一致来缓解。该数据属于演示式数据，即每项任务都以可重复的策略被演示数百次（Sec. C.1.3）。

<a id="S292"></a>
**Source:** p.15 S292

**Original:** Human Data Scaling. Under the same GR00T 2 architecture, training recipe and post-training teleoperation data, we ablate four Human-1M data pre-training scales (0%, 1%, 10%, or 100%). We control training length in epochs. The 1%, 10%, and 100% models start from a shared human-video pretraining checkpoint and are each pretrained for about 0.5 epoch of their share, while the 0% model skips human-video pretraining entirely. The step from 0% to 1% therefore also includes this shared stage, and the 1%, 10%, and 100% models differ only in their share of human data and the matching training length. Here one epoch means the model passes once over every step of every 30 Hz trajectory. Every model is then trained on the same target Dexter teleoperation data, co-trained with its human share, for the same 3 epochs of that robot data. We measure real robot and video rollout success rate (%) and task progress (%) on 72 Dexter tasks, 22 out-of-distribution tasks with new kinds of instructions and 50 tasks absent from Dexter’s training data. Across all four settings, we see positive scaling in performance as human data is scaled (Fig. 10). Real robot success rates increase from 18% to 41% from 0% human data pre-training to 100%. Video rollout success rates similarly increase from 30% to 51%. Together, these results show that what GR00T 2 learns from human video transfers to the robot. With the robot data held fixed, pretraining on all of the multi-view human video more than doubles real-robot success on new tasks, and none of the metrics levels off at 100%, which suggests that more human video will keep improving robot performance (Sec. C.1.5).

**中文:** 人类数据规模化。在相同的 GR00T 2 架构、训练方案以及后训练遥操作数据下，我们消融了四种 Human-1M 数据预训练规模（0%、1%、10% 或 100%）。训练长度以 epoch 数控制。1%、10% 与 100% 的模型都从一个共享的人类视频预训练检查点出发，并各自对其所占份额预训练约 0.5 个 epoch；而 0% 的模型则完全跳过人类视频预训练。因此，从 0% 到 1% 的变化也包含了这一共享阶段，而 1%、10% 与 100% 的模型仅在人类数据占比及相应的训练长度上有所不同。这里一个 epoch 指模型遍历每条 30 Hz 轨迹的每一步一次。随后，每个模型都在相同的目标 Dexter 遥操作数据上训练，并与其人类数据份额联合训练，对该机器人数据训练相同的 3 个 epoch。我们在 72 个 Dexter 任务、22 个具有新指令类型的分布外任务，以及 50 个 Dexter 训练数据中未出现的任务上，测量了真实机器人与视频 rollout（轨迹采样）的成功率（%）和任务进度（%）。在全部四种设置下，性能都随人类数据规模的扩大而呈现正向扩展（图 10）。从 0% 人类数据预训练到 100%，真实机器人的成功率由 18% 提升至 41%；视频 rollout 的成功率同样由 30% 提升至 51%。综合来看，这些结果表明，GR00T 2 从人类视频中学到的内容能够迁移到机器人上。在机器人数据保持不变的情况下，对全部多视角人类视频进行预训练，使新任务上的真实机器人成功率提高了一倍以上，并且所有指标在 100% 时都未趋于平稳，这表明更多的人类视频可能会继续提升机器人性能（Sec. C.1.5）。

<a id="S294"></a>
**Source:** p.16 S294

**Original:** 4.2.2. UMI Data

**中文:** 4.2.2. UMI 数据

<a id="S295"></a>
**Source:** p.16 S295

**Original:** UMI-10K, recorded with the handheld UMI device (App. E), contributes 942k quality-controlled episodes and 10,184 hours of bimanual parallel-gripper demonstrations across 2,897 tasks. The dataset is extremely diverse with no single task contributing more than 1.2% of hours. The instructions span 356 object categories and 49 dextrous skills. The corpus covers 2,798 distinct skill-object combinations, including dynamic, articulated, and deformable manipulation that teleoperation rarely captures. Many tasks contain counterfactual pairs, which is aimed to improve policy instruction following (Sec. C.2).

**中文:** UMI-10K 由手持 UMI 设备录制（附录 E），贡献了 942k 条经质量控制的片段，以及横跨 2,897 项任务的 10,184 小时双臂平行夹爪演示。该数据集非常多样，没有任何单一任务的时长占比超过 1.2%。指令涵盖 356 个物体类别与 49 种灵巧技能。语料覆盖 2,798 种不同的技能-物体组合，包括遥操作很少涉及的动态、关节式与可变形物体操作。许多任务包含反事实配对，旨在提升策略的指令遵循能力（Sec. C.2）。

<a id="S296"></a>
**Source:** p.16 S296

**Original:** 4.2.3. Teleoperation Data

**中文:** 4.2.3. 遥操作数据

<a id="S297"></a>
**Source:** p.16 S297

**Original:** Cross-embodiment teleoperated demonstrations provide robot action supervision for GR00T 2. The pre-training mixture contains a total of 23.5k hours and 1.16M episodes of teleoperation data including:

**中文:** 跨本体遥操作演示为 GR00T 2 提供机器人动作监督。预训练数据混合包含共计 23.5k 小时、1.16M 个片段的遥操作数据，具体包括：

<a id="S298"></a>
**Source:** p.16 S298

**Original:** • Bimanual YAM arms with parallel grippers (18.7k hours, including ABC-130k (XDOF, 2026)), • Bimanual arms with Sharpa hands (2.9k hours), • Bimanual arms with Wuji hands (1.3k hours), • The Unitree G1 humanoid (275 hours), • The single-arm Franka Panda from DROID (Khazatsky et al., 2024).

**中文:** • 配备平行夹爪的双臂 YAM 机械臂（18.7k 小时，包括 ABC-130k (XDOF, 2026)），• 配备 Sharpa 手的双臂机械臂（2.9k 小时），• 配备 Wuji 手的双臂机械臂（1.3k 小时），• Unitree G1 人形机器人（275 小时），• 来自 DROID 的单臂 Franka Panda（Khazatsky et al., 2024）。

<a id="S299"></a>
**Source:** p.16 S299

**Original:** Additional details are provided in Sec. C.3.

**中文:** 更多细节见 Sec. C.3。

<a id="S300"></a>
**Source:** p.16 S300

**Original:** 4.2.4. Data Annotation with Flora

**中文:** 4.2.4. 使用 Flora 进行数据标注

<a id="S301"></a>
**Source:** p.16 S301

**Original:** GR00T 2 pretraining uses dense timestamped language annotations for language conditioning, filtering and rebalancing. GR00T 2 RL post-training additionally requires process rewards, while policy evaluation requires outcome labelling. At the scale of Human-1M and our robot corpora, human labeling is too slow and frontier API models are too expensive. To provide these dense labels, we leverage Flora (Leng et al., 2026), the data engine that annotates training and evaluation data for GR00T 2. Flora consists of three models that identify action boundaries, annotate each action with a self-contained imperative instruction, and generate outcome, dense, and rubric-based rewards. On WGO-Bench (Macrodata Labs, 2026), Flora achieves a temporal segmentation F1 of 50.3, compared to 46.0 for the next-best model, GPT-6 Astra (OpenAI, 2026). Additional details are provided in Sec. C.4.

**中文:** GR00T 2 的预训练使用密集的带时间戳语言标注，用于语言条件化、过滤与重新配比。GR00T 2 的强化学习（RL）后训练还需要过程奖励，而策略评测则需要结果标注。在 Human-1M 与我们的机器人语料规模下，人工标注太慢，前沿 API 模型又过于昂贵。为获得这些密集标签，我们利用了 Flora（Leng et al., 2026），这是为 GR00T 2 标注训练与评测数据的数据引擎。Flora 由三个模型组成，分别用于识别动作边界、为每个动作标注一条自包含的祈使式指令，以及生成结果奖励、密集奖励和基于评分准则（rubric）的奖励。在 WGO-Bench（Macrodata Labs, 2026）上，Flora 的时序分割 F1 达到 50.3，而次优模型 GPT-6 Astra（OpenAI, 2026）为 46.0。更多细节见 Sec. C.4。

### 4.3. Real-World Benchmarking: Mapping the Hill We Climb ｜ 4.3 真实世界基准测试：绘制“我们攀登的山丘”

<a id="S302"></a>
**Source:** p.16 S302

**Original:** Every GR00T 2 candidate earned its place in blinded head-to-head matches on real robots, accumulated into a single leaderboard that tells us which checkpoint is better, by how much, and how sure we can be.

**中文:** 每一个 GR00T 2 候选模型都是通过真实机器人上的盲测正面对决赢得席位的，这些结果汇总进同一个排行榜，它告诉我们哪个检查点更好、优势有多大，以及我们对此有多大把握。

<a id="S303"></a>
**Source:** p.16 S303

**Original:** Why head-to-head. Real-robot evaluation is expensive, but its results accumulate, and months of evaluations are only worth keeping if they stay comparable. Absolute success rates do not: they drift with the station, the operator, the hardware, and the day, so a score from one session cannot be compared with a score from another.

**中文:** 为何采用正面对决。真实机器人评测成本高昂，但其结果会不断累积，而数月的评测只有保持可比时才值得保留。绝对成功率做不到这一点：它们会随工位、操作员、硬件和当天情况而漂移，因此某一次会话的得分无法与另一次会话的得分相比。

<a id="S305"></a>
**Source:** p.17 S305

**Original:** GR00T 2 Turbo other best so far 90% CI (new bests)

**中文:** GR00T 2 Turbo；其他迄今最佳；90% CI（新最佳）

![F011](assets/F011.png)

<a id="C012"></a>
**Source:** p.17 C012 · 图 F011

**Original (caption):** Figure 11: Mapping the hill we climb. Every checkpoint on the current YAM suite, rated relative to the A/B reference (⋆, the board’s top-rated checkpoint, here a GR00T 2 Turbo checkpoint) and placed at the date it was saved. The line tracks the best checkpoint so far, and bars are paired 90% bootstrap intervals for the checkpoints that set a new best. Evidence: the 6,035 blinded A/B comparisons of this suite, from 122 campaigns.

**中文（图注）：** 图 11：绘制我们攀登的山丘。当前 YAM 套件上的每个检查点都相对于 A/B 参考（⋆，即排行榜上评级最高的检查点，此处为一个 GR00T 2 Turbo 检查点）进行评级，并按其保存日期放置。折线追踪迄今最佳的检查点，柱条为创下新最佳的检查点所对应的配对 90% 自助法（bootstrap）区间。依据：本套件共 122 个评测批次中的 6,035 次盲测 A/B 比较。

<a id="S308"></a>
**Source:** p.17 S308

**Original:** Elo vs. reference ★

**中文:** 相对参考 ★ 的 Elo

<a id="S314"></a>
**Source:** p.17 S314

**Original:** Jul Aug Sep Oct Nov checkpoint date (2026)

**中文:** 7 月、8 月、9 月、10 月、11 月；检查点日期（2026）

<a id="S316"></a>
**Source:** p.17 S316

**Original:** A blinded A/B trial runs two to four checkpoints in randomized order on the same scene, by the same operator, within minutes, so the drift is shared and cancels in the comparison. GearArena, our real-robot leaderboard, pools every such trial. By the snapshot used here it held 195 A/B campaigns with 16,044 graded robot episodes and 11,767 pairwise comparisons, collected on 10 YAM stations by more than 20 operators between July and November 2026, rating 71 checkpoints.

**中文:** 一次盲测 A/B 试次会在几分钟之内，由同一名操作员，在同一场景中以随机顺序运行两到四个检查点，因此漂移是共有的，会在比较中相互抵消。GearArena 是我们的真实机器人排行榜，汇集了所有此类试次。截至本文所用的快照，它包含 195 个 A/B 评测批次、16,044 个带评分的机器人片段，以及 11,767 次成对比较，这些数据于 2026 年 7 月至 11 月间在 10 个 YAM 工位上采集，由 20 多名操作员完成，对 71 个检查点进行了评级。

<a id="S317"></a>
**Source:** p.17 S317

**Original:** Tasks from first principles. We design evaluation tasks by asking what the robot should be able to do, then choosing tasks that expose those capabilities, and finally gauging them on real checkpoints: a task every checkpoint completes is archived, and one no checkpoint completes is shelved until models catch up, since neither separates anything. Two suites resulted: a first suite of general and dexterous manipulation tasks and the current suite of 38 language-following and motion-primitive tasks, each run with partial-credit rubrics.

**中文:** 从第一性原理出发设计任务。我们先问机器人应当能够做什么，再选择能够暴露这些能力的任务，最后在真实检查点上对其进行评估：所有检查点都能完成的任务会被归档，没有任何检查点能完成的任务则被搁置，直到模型追上来，因为这两类任务都无法区分模型。由此形成两套套件：第一套是通用与灵巧操作任务，当前套件则包含 38 个语言跟随与运动基元任务，每项任务都采用部分得分评分准则（rubric）进行评估。

<a id="S318"></a>
**Source:** p.17 S318

**Original:** From matches to a map. Every pair of checkpoints in a trial forms one comparison, decided by the operator’s explicit ranking (equal grades count as ties). A Bradley-Terry model (Bradley and Terry, 1952), fit jointly to all comparisons, gives each checkpoint an Elo rating. Within each head-to-head, every task carries equal weight, and confidence intervals come from a bootstrap that resamples tasks rather than trials. Every new checkpoint is first matched against the A/B reference, the best-rated checkpoint on the board, which keeps all ratings on one connected scale (App. D).

**中文:** 从对决到地图。试次中的每一对检查点构成一次比较，由操作员明确给出的排名决定（同等评级计为平局）。对所有比较联合拟合的 Bradley-Terry 模型（Bradley and Terry, 1952）为每个检查点给出一个 Elo 评分。在每一次正面对决中，每项任务权重相等，置信区间则来自对任务而非试次进行重采样的自助法。每个新检查点都会先与 A/B 参考对比，即排行榜上评级最高的检查点，这使所有评分处于同一个相互连通的尺度上（App. D）。

<a id="S319"></a>
**Source:** p.17 S319

**Original:** What it bought us. Arena turned close calls into decisions. GR00T 2 outrates 𝜋0.5 by 236 Elo (95% CI 171 to 325), an expected 80% head-to-head win rate, and GR00T 1.7 by 95 Elo (CI 50 to 148), both in all 500 bootstrap resamples (Tab. 13). On our YAM V2 task suite, which focuses on foundational skills such as language following and motion primitives (Tab. 2), GR00T 2 Turbo is statistically indistinguishable from GR00T 2 in skill while running each inference about three times faster (52 vs. 171 ms per served call on a GeForce RTX 5090 workstation, Fig. 23). Over four months, the best checkpoint on the current suite climbed 206 Elo, from a June model that today’s top checkpoint would beat 77% of the time (Fig. 11). Simulated evaluations reproduce Elo ratings fit to blinded A/B trials of this kind with Pearson 𝑟= 0.93 (Sec. 4.5.2). App. D details the task design, the rating model, the A/B infrastructure, and the full results.

**中文:** 它带来的价值。Arena 把难以分辨的情况变成了明确的决策。GR00T 2 以 236 Elo 的优势（95% CI 171 至 325）超过 π0.5，对应期望的 80% 正面对决胜率；以 95 Elo（CI 50 至 148）超过 GR00T 1.7，两者在全部 500 次自助法重采样中均成立（Tab. 13）。在我们侧重语言跟随与运动基元等基础技能的 YAM V2 任务套件上（Tab. 2），GR00T 2 Turbo 在技能上与 GR00T 2 没有统计学差异，而每次推理的速度约快三倍（在 GeForce RTX 5090 工作站上，每次服务调用分别为 52 毫秒与 171 毫秒，Fig. 23）。经过四个月，当前套件上的最佳检查点提升了 206 Elo，从一个 6 月份的模型起步，如今的最佳检查点对其的胜率为 77%（Fig. 11）。模拟评测以皮尔逊相关系数 $r=0.93$ 复现了由此类盲测 A/B 试次拟合出的 Elo 评分（Sec. 4.5.2）。附录 D 详述了任务设计、评分模型、A/B 基础设施与完整结果。
