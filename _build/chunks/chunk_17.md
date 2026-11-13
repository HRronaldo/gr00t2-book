### D.2. Designing Evaluation Tasks from First Principles ｜ D.2 从第一性原理设计评测任务

<a id="S1203"></a>
**Source:** p.66 S1203

**Original:** Want, represent, gauge. Our task suites are designed in three steps. First, we ask what the robot should be able to do: follow spatial and attribute-based language instructions, execute basic motion primitives reliably, and handle contact-rich and deformable-object skills. Second, we choose the tasks that best represent each capability, one physical arrangement per task, each with a partial-credit rubric that scores a rollout as the weighted fraction of completed sub-tasks between 0 and 1 (the task-progress metric of Sec. J.2.1). Third, we gauge every task on real checkpoints. A task that every checkpoint completes no longer separates anything and is archived, while a task that no checkpoint completes is shelved until the models catch up. Shelving is also enforced by the rating itself: a comparison in which both rollouts score exactly zero is dropped (Sec. D.4), so a task nobody can do contributes nothing. In the first suite, the zipper-closing task scored zero in every trial for every checkpoint, and drops out this way.

**中文:** 我们的任务套件分三步设计。第一步，先问机器人应该能做什么：能否遵循空间类与属性类的语言指令，能否可靠地执行基本运动原语，以及能否处理富接触和可形变物体的技能。第二步，为每项能力挑选最能代表它的任务，每个任务对应一种物理布局，并配有部分得分量表。该量表把一条 rollout 按已完成子任务的加权比例打分，取值在 0 到 1 之间（即 Sec. J.2.1 中的任务进度指标）。第三步，在真实检查点上度量每个任务。若所有检查点都能完成某任务，它就不再区分任何模型，会被归档；若没有检查点能完成，则先搁置，等模型追上来再说。搁置还由评分机制本身强制执行：两条 rollout 得分都恰为零的比较会被丢弃（见 Sec. D.4），因此无人能完成的任务不贡献任何信息。在第一个套件中，拉链任务在每个检查点的每次试次中都得零分，因此以这种方式被剔除。

<a id="S1204"></a>
**Source:** p.66 S1204

**Original:** Two suites. The first suite (YAM V1, July to October 2026) combined general manipulation tasks (wiping, slot insertion, unscrewing, opening and closing, scooping, flattening and folding, language following) with dexterous assembly and packing tasks (airplane and car assembly, iPhone box). The current suite (YAM V2, from September 21, 2026) has 38 tasks in three sub-suites: 14 language-following tasks (LF, e.g. place the cup between the bowl and the plate, put the second block from the left in the basket), 10 easy motion primitives (MP easy, e.g. flip a cup, pour beans between bowls), and 14 medium-to-hard motion primitives (MP mid/hard, e.g. screw a lid onto a jar, thread a cable tie into a bottle, roll a towel, unhook rings). Each A/B campaign on V2 runs one sub-suite with two trials per task per checkpoint.

**中文:** 共两个套件。第一个套件（YAM V1，2026 年 7 月至 10 月）把通用操作任务（擦拭、插槽、拧松、开合、舀取、展平与折叠、语言跟随）与灵巧装配及打包任务（飞机与汽车装配、iPhone 盒）放在一起。当前套件（YAM V2，自 2026 年 9 月 21 日起）共 38 个任务，分为三个子套件：14 个语言跟随任务（LF，例如把杯子放在碗和盘子之间，把从左数第二个积木放进篮子）、10 个简单运动原语（MP easy，例如翻转杯子、在碗之间倒豆子），以及 14 个中到难运动原语（MP mid/hard，例如把盖子拧到罐子上、把扎带穿进瓶中、卷毛巾、解开环扣）。V2 上的每次 A/B 评测批次运行一个子套件，每个检查点每个任务做两次试次。

<a id="S1206"></a>
**Source:** p.66 S1206

**Original:** The current suite is unsaturated. Fig. 34 applies the gauge to V2. Across 9,402 graded rollouts (the V2 rollouts of Tab. 12 without those of VLM-based policies and of one uncoded task), per-task mean scores range from 0.05 (rolling clay) to 0.73 (cup in basket), with a median of 0.28. No task is close to saturation, and six tasks (rolling clay, wiping a circle, wiping a blue mark, picking the second block from the left, stacking the middle block, and pushing a cup left) score at most 0.10 on average, which makes them candidates for shelving. The suite therefore still separates the strongest checkpoints, which is the property that makes its comparisons informative.

**中文:** 当前套件尚未饱和。图 34 把该度量应用于 V2。在 9,402 条已评分的 rollout 中（即表 12 中的 V2 rollout，去掉基于 VLM 的策略以及一个未编码任务），单任务平均分从 0.05（卷泥条）到 0.73（杯子放进篮子）不等，中位数为 0.28。没有任务接近饱和。其中六个任务（卷泥条、擦圆圈、擦蓝色标记、拾取从左数第二个积木、堆叠中间积木、把杯子向左推）的平均分至多为 0.10，是搁置的候选。因此，该套件仍然能区分最强的检查点，而这正是它的比较结果有信息量的原因。

<a id="S1207"></a>
**Source:** p.66 S1207

**Original:** Task identity. The rating treats each task name as one physical arrangement (one scene), so names matter. Several V2 tasks were recorded under two identifiers, a bare name and a coded one (e.g. T_Motion_Roll_Towel and T_Motion_Roll_Towel_M17_U), and the live leaderboard counts them as different tasks.2 Admission to a

**中文:** 任务身份。评分把每个任务名视为一种物理布局（一个场景），因此名称很重要。若干 V2 任务同时以两个标识符记录，一个是裸名，一个是带编码的名称（例如 T_Motion_Roll_Towel 与 T_Motion_Roll_Towel_M17_U），而实时排行榜把它们计为不同的任务。2 进入一个

<a id="S1208"></a>
**Source:** p.66 S1208

**Original:** 2Merging the two identifiers of each task (74 task names to the suite’s 38 tasks) changes no rating by more than 8 Elo, leaves the top eleven ranks unchanged, and moves every reported 𝑃(𝐴>𝐵) by at most 0.02 (offline re-fit on the same snapshot).

**中文:** 2 将每个任务的两个标识符合并（74 个任务名合并为套件的 38 个任务），任何评分变化不超过 8 Elo，前十一名保持不变，每个已报告的 𝑃(𝐴>𝐵) 变化不超过 0.02（基于同一快照的离线重拟合）。

![F035](assets/F035.png)

<a id="C047"></a>
**Source:** p.67 C047 · 图 F035

**Original (caption):** Figure 35: From an A/B request to a rating. A campaign is requested with its checkpoints, tasks, trial count, and station. The station runs a blinded session in which the operator stages each scene, runs every arm, and grades and ranks the rollouts without knowing which checkpoint produced which. Recordings, the blinding manifest, latency statistics, and a checksummed results snapshot are stored with the session. The arena ingests them, decodes the blinding, admits each graded trial to its suite, and refits the ratings. Researchers choose the next comparisons from the leaderboard.

**中文（图注）：** 图 35：从 A/B 请求到评分。提交评测批次时需给出检查点、任务、试次数和工位。工位运行一次盲测会话：操作员布置每个场景、运行每个臂，并在不知道哪个检查点产生了哪条 rollout 的情况下对其评分和排序。录像、盲化清单、时延统计以及带校验和的结果快照都与该会话一同存储。竞技场摄取这些数据，解除盲化，把每个已评分的试次纳入其所属套件，并重新拟合评分。研究人员依据排行榜选择下一批比较。

<a id="S1228"></a>
**Source:** p.67 S1228

**Original:** suite is explicit: each suite lists its task identifiers and the embodiment tags it accepts, so evidence cannot leak between suites.

**中文:** 套件的规则很明确：每个套件列出其任务标识符及其接受的本体标签，因此证据无法在套件之间泄露。

### D.3. The Arena: Stations, Operators, Campaigns, and Suites ｜ D.3 竞技场：工位、操作员、批次与套件

<a id="S1229"></a>
**Source:** p.67 S1229

**Original:** Campaigns and sessions. The unit of work is the campaign: one A/B evaluation request naming two to four checkpoints, a task list, the number of trials per task, and a station. A campaign runs in one or more recording sessions on that station, typically by one operator. In the snapshot, the two YAM suites hold 195 campaigns run on 10 YAM stations by more than 20 operators, with 16,044 graded rollouts in 5,570 trials (Tab. 12). Campaigns are collected continuously. The leaderboard counts graded trials of campaigns still in progress, and never counts an ungraded trial as a failure.

**中文:** 批次与会话。工作单元是批次：一次 A/B 评测请求，指定两到四个检查点、一个任务列表、每个任务的试次数以及一个工位。批次在该工位上运行于一次或多次录制会话中，通常由同一名操作员完成。快照中，两个 YAM 套件共有 195 个批次，分布在 10 个 YAM 工位上，由 20 余名操作员完成，包含 5,570 次试次中的 16,044 条已评分 rollout（表 12）。批次是持续收集的。排行榜会统计仍在进行中的批次中已评分的试次，但从不把未评分的试次计为失败。

<a id="S1230"></a>
**Source:** p.67 S1230

**Original:** Suites as separate leagues. Each suite is its own league with its own evidence, ratings, and history: YAM V1, YAM V2, and a dexterous-hand suite on Tianji arms with Sharpa hands (Dex, 25 checkpoints, 29 campaigns, 1,492 matches). Ratings are comparable only within a suite. Within the dexterous suite, inference settings are part of a checkpoint’s identity: the same weights served with two different inference regimes are rated as separate entries, and disconnected groups of checkpoints that never met are reported as separate comparison groups rather than forced onto one scale.

**中文:** 作为独立联盟的套件。每个套件都是独立的联盟，拥有各自的证据、评分与历史：YAM V1、YAM V2，以及一个使用 Tianji 机械臂与 Sharpa 手的灵巧手套件（Dex，25 个检查点、29 个批次、1,492 场对局）。评分只在套件内部可比。在灵巧手套件中，推理设置是检查点身份的一部分：同一组权重若以两种不同的推理方式提供服务，就被当作两个独立条目评分；彼此从未对战过的检查点分组则作为独立的比较组报告，而不是强行放到同一尺度上。

<a id="S1231"></a>
**Source:** p.67 S1231

**Original:** Provenance and audit. The arena reads each campaign’s graded results from a checksummed snapshot stored with its recordings, falling back to the request record only when no snapshot exists, and records which source it used. A board history keeps every change point, so any past leaderboard can be replayed. A weekly audit re-checks every scored trial against its recording, and a campaign whose blinding is in doubt is withheld from every leaderboard (one campaign is withheld today, because its operator could see checkpoint labels).

**中文:** 来源与审计。竞技场从与录像一同存储的带校验和快照中读取每个批次的已评分结果，只有在不存在快照时才退回到请求记录，并记录所用的来源。看板历史保留每一个变更节点，因此任何过去的排行榜都可以重放。每周审计会把每次已评分试次与其录像重新核对；若某批次的盲化存在疑问，则会从所有排行榜中撤下（目前撤下一个批次，原因是其操作员能看到检查点标签）。

### D.4. Leaderboard Mathematics ｜ D.4 排行榜的数学

<a id="S1234"></a>
**Source:** p.67 S1234

**Original:** From trials to matches. In a trial with 𝑛arms, every pair of arms forms one match, in total. The outcome is the operator’s explicit ranking of the rollouts. When the operator graded two rollouts identically, the forced order between them carries no information, and the match counts as a tie. When both rollouts scored exactly zero, the match is dropped, since it bounds both checkpoints below the task’s difficulty without ordering them.

**中文:** 从试次到对局。在一个含 𝑛arms 个臂的试次中，每一对臂构成一场对局，总计 [存疑：“in total”之后的对局数公式在抽取中缺失]。结果取决于操作员对各条 rollout 的明确排序。若操作员给两条 rollout 的评分相同，则二者之间被强制给出的顺序不携带信息，该对局计为平局。若两条 rollout 得分都恰为零，该对局被丢弃，因为它只说明两个检查点都低于任务难度，并不能区分二者的先后。

<a id="S1236"></a>
**Source:** p.67 S1236

**Original:** Bradley-Terry model. Each checkpoint 𝑖has a strength 𝑝𝑖> 0, and

**中文:** Bradley-Terry 模型。每个检查点 𝑖 具有强度 𝑝𝑖 > 0，并且 [存疑：此处的模型公式在抽取中缺失]。

<a id="S1239"></a>
**Source:** p.68 S1239

**Original:** The strengths are fit jointly to all matches by maximum likelihood (Bradley and Terry, 1952), using the minorization-maximization update (Hunter, 2004)

**中文:** 强度通过极大似然对所有对局进行联合拟合（Bradley and Terry, 1952），采用 Hunter (2004) 的 minorization-maximization 更新。

<a id="E002"></a>
**Source:** p.68 E002

**Original:** 𝑗̸=𝑖𝑛𝑖𝑗/(𝑝𝑖+ 𝑝𝑗), (5)

**中文:** 该式为 Eq. (5) 中的 minorization-maximization 更新式。求和遍历 𝑗 ≠ 𝑖（抽取文本为 𝑗̸=𝑖）。[公式原文见 p.68]

<a id="S1241"></a>
**Source:** p.68 S1241

**Original:** where 𝑊𝑖is checkpoint 𝑖’s total weighted wins (a tie counts half) and 𝑛𝑖𝑗the total weight of matches between 𝑖and 𝑗. Each checkpoint also receives one virtual tie against a fixed anchor, a weak prior that keeps undefeated or winless checkpoints finite and pulls checkpoints with little evidence toward the middle. Because the fit is a batch estimate, it does not depend on the order in which evaluations arrived. Ratings are reported on the Elo scale (Elo, 1978), with ¯𝑝the geometric mean of all strengths, so 1500 is the field average and a difference of 100 Elo corresponds to a 64% expected win rate.

**中文:** 其中 𝑊𝑖 是检查点 𝑖 的加权胜场总数（平局计一半），𝑛𝑖𝑗 是 𝑖 与 𝑗 之间对局的总权重。每个检查点还与一个固定锚点获得一次虚拟平局，这是一个弱先验，使全胜或全败的检查点仍有有限的取值，并把证据不足的检查点拉向中间。由于这是批量估计，结果不依赖评测到达的顺序。评分按 Elo 尺度报告（Elo, 1978），其中 ¯𝑝 为所有强度的几何平均，因此 1500 是场上的平均水平，100 Elo 的差值对应 64% 的期望胜率。

<a id="S1246"></a>
**Source:** p.68 S1246

**Original:** Task normalization. A raw fit would let a frequently evaluated task dominate. We instead normalize within each head-to-head: for every pair of checkpoints and every task, the matches of that pair on that task are rescaled to total weight one,

**中文:** 任务归一化。原始拟合会让被频繁评测的任务占据主导。我们因此在每一组两两对比内部做归一化：对每一对检查点及每个任务，该对在该任务上的对局被重新缩放为总权重 1，

<a id="E003"></a>
**Source:** p.68 E003

**Original:** 𝑤𝑚= 1 {𝑚′ : pair(𝑚′) = pair(𝑚), task(𝑚′) = task(𝑚)}⃒⃒, (7)

**中文:** 该式为 Eq. (7) 的权重定义：对局 𝑚 的权重 𝑤𝑚 等于 1 除以与 𝑚 具有相同检查点对且相同任务的对局数。[公式原文见 p.68]

<a id="S1247"></a>
**Source:** p.68 S1247

**Original:** so that within any head-to-head each task contributes the fraction of its trials won, and each distinct task counts once. Normalizing per pair, rather than per task across the whole leaderboard, keeps a checkpoint’s weights independent of evaluations it took no part in: under global normalization, a checkpoint that lost its only head-to-head could be ranked above the opponent that beat it, and adding one checkpoint shifted the relative standing of others by up to 27 Elo.

**中文:** 这样，在任一两两对比中，每个任务贡献的是其试次中获胜的比例，且每个不同的任务只计一次。按对归一化而不是在整个排行榜上按任务归一化，使检查点的权重不受其未参与的评测影响：在全局归一化下，一个仅有的一场对局即告失败的检查点，可能被排在击败它的对手之上；而且增加一个检查点，会使其他检查点的相对排名最多变动 27 Elo。

<a id="S1248"></a>
**Source:** p.68 S1248

**Original:** Uncertainty from scenes, not trials. All trials of a task re-stage the same arrangement, so they are not independent. Confidence intervals therefore come from a cluster bootstrap (Davison and Hinkley, 1997) that resamples tasks with replacement, re-derives the weights of Eq. (7) inside every resample, and refits Eq. (4). We use 500 resamples and report the 2.5th and 97.5th percentiles (figures draw the 5th and 95th, i.e. 90% intervals, for legibility), withholding an interval when a checkpoint’s matches span fewer than three tasks. Re-deriving the weights matters: computing them once, before resampling, made intervals about 30% narrower than the estimator warrants on our July evaluations.

**中文:** 不确定性来自场景，而非试次。同一任务的所有试次都重新布置同一场景，因此它们并不独立。置信区间因此来自按任务有放回重采样的聚类自助法（Davison and Hinkley, 1997）：在每次重采样内部重新推导 Eq. (7) 的权重，并重新拟合 Eq. (4)。我们使用 500 次重采样，报告第 2.5 与第 97.5 百分位数（图中为便于阅读而绘制第 5 与第 95 百分位数，即 90% 区间）。当某检查点的对局跨越的任务少于三个时，不报告其区间。重新推导权重很重要：若在重采样前只计算一次权重，区间会比估计量所要求的窄约 30%（以我们七月的评测为依据）。

<a id="S1249"></a>
**Source:** p.68 S1249

**Original:** Comparing two checkpoints. Overlapping intervals do not imply that two checkpoints are equal (Schenker and Gentleman, 2001): a lucky draw of tasks lifts both, and that shared variation cancels in their difference. We therefore compare checkpoints with the paired statistic computed over the same 𝐵= 500 resamples, together with the percentile interval of the gap Elo(𝑏)

**中文:** 比较两个检查点。区间重叠并不意味着两个检查点相等（Schenker and Gentleman, 2001）：一次偶然的任务抽取会同时抬高两者，而这种共同波动会在二者之差中抵消。因此，我们在同一 𝐵 = 500 次重采样上计算配对统计量来比较检查点，并同时给出差值 Elo(𝑏) 的百分位区间。

<a id="S1263"></a>
**Source:** p.68 S1263

**Original:** 𝐵. On the current suite, the median interval is 93 Elo wide, and 176 of the 253 pairs among 23 checkpoints (the 20 in Fig. 36 and three further development checkpoints) are resolved at the 95% level.

**中文:** [存疑：Elo(𝑏) 的定义在 p.68 处被截断，以下为其尾部] 𝐵。在当前套件上，中位区间宽 93 Elo。在 23 个检查点之间的 253 对中（包括图 36 中的 20 个检查点以及另外三个开发检查点），有 176 对在 95% 水平上分出了高下。

<a id="S1264"></a>
**Source:** p.68 S1264

**Original:** Anchoring. Every new checkpoint’s first A/B campaign is against the reference checkpoint, which ties it to the rest of the leaderboard and gives it full task coverage in one session. A second campaign against its warm-start parent answers whether a change helped. The reference is the best-rated checkpoint on the A/B leaderboard unless one is pinned deliberately. Because the paired comparison benefits from shared variation, checkpoints that must be told apart are best run in the same campaign.

**中文:** 锚定。每个新检查点的第一次 A/B 批次都与参考检查点对比，这把它与排行榜其余部分连接起来，并在一次会话内提供完整的任务覆盖。第二次批次与其热启动的父检查点对比，用于回答某项改动是否有效。参考检查点为 A/B 排行榜上评分最高者，除非被刻意指定。由于配对比较受益于共同波动，需要区分的检查点最好在同一批次中运行。

![T013](assets/T013.png)

<a id="C048"></a>
**Source:** p.69 C048 · 表 T013

**Original (caption):** Table 13: Paired comparisons on YAM V2. Elo difference (A minus B) with its paired 95% interval, and the share of 500 bootstrap resamples in which A rates higher (Eq. (8)). “GR00T 2” is the released checkpoint, and the expected win rate follows from the Elo difference.

**中文（表注）：** 表 13：V2 上的配对比较。Elo 差值（A 减 B）及其配对 95% 区间，以及在 500 次自助重采样中 A 评分更高的比例（Eq. (8)）。“GR00T 2”为已发布的检查点，期望胜率由 Elo 差值推出。

<a id="S1266"></a>
**Source:** p.69 S1266

**Original:** GR00T 2 𝜋0.5 (Physical Intelligence et al., 2025) +236 [+171, +325] > 0.99 80% GR00T 2 GR00T 1.7 (NVIDIA, 2026a) +95 [+50, +148] > 0.99 63% GR00T 2 GR00T 2 Turbo (early checkpoint) +12 [−20, +48] 0.80 52% GR00T 2 GR00T 2 Turbo (⋆) −14 [−58, +28] 0.28 48% GR00T 1.7 𝜋0.5 +141 [+78, +227] > 0.99 69% GR00T 2 Turbo GR00T 1.7 +109 [+54, +168] > 0.99 65%

**中文:** 表 13 的数据行在 PDF 中以纯文本抽取，按原文顺序列为：GR00T 2 对 𝜋0.5（Physical Intelligence et al., 2025）：+236 [+171, +325]，>0.99，80%；GR00T 2 对 GR00T 1.7（NVIDIA, 2026a）：+95 [+50, +148]，>0.99，63%；GR00T 2 对 GR00T 2 Turbo（早期检查点）：+12 [−20, +48]，0.80，52%；GR00T 2 对 GR00T 2 Turbo（⋆）：−14 [−58, +28]，0.28，48%；GR00T 1.7 对 𝜋0.5：+141 [+78, +227]，>0.99，69%；GR00T 2 Turbo 对 GR00T 1.7：+109 [+54, +168]，>0.99，65%。[存疑：列对应关系按抽取顺序推断]

<a id="S1270"></a>
**Source:** p.69 S1270

**Original:** switch between arms checks that the server reports the expected kind, so a misrouted port fails loudly rather than silently serving the wrong model. Baselines run with their native settings, such as their own prompts and action filtering, so that a comparison measures the policy rather than our serving of it.

**中文:** 切换机械臂时会检查服务器报告的类型是否与预期一致，因此错误的端口路由会明确报错，而不是悄悄提供错误的模型。基线按其原生设置运行，例如它们自己的提示词和动作滤波，使比较测量的是策略本身，而不是我们对它的服务。

<a id="S1271"></a>
**Source:** p.69 S1271

**Original:** Blinding. The operator sees only what is needed to run and grade the rollouts. The visualization shows the same information for every arm. The operator’s terminal shows nothing that names or times an arm: the client’s command line, which names every checkpoint, is kept away from the operator, per-query timing warnings are recorded rather than printed, and warm-up messages and recording timers behave identically for every arm. The mapping from rotation slots to checkpoints is written to a session manifest that is read only after grading.

**中文:** 盲化。操作员只看到运行和评分 rollout 所需的信息。可视化对每个臂显示相同的内容。操作员的终端不显示任何能指明或计时某个臂的内容：客户端命令行会列出每个检查点的名称，因此对操作员隐藏；每次查询的计时警告被记录而不打印；预热消息与录制计时器对每个臂的表现完全相同。轮换槽位到检查点的映射写入会话清单，且只在评分结束后读取。

<a id="S1272"></a>
**Source:** p.69 S1272

**Original:** Recording and grading. Every episode is recorded and uploaded with per-arm latency statistics, which supply the inference-speed axis of Fig. 38. Each trial is graded with its rubric and an explicit ranking of the arms. The arena decodes a trial only when the request declares that its labels are rotation slots. Rows it cannot resolve to checkpoints are skipped rather than guessed, and a weekly audit compares each scored trial with the checkpoint its recording says it served.

**中文:** 录制与评分。每一段 episode 都被录制并上传，附带每个臂的时延统计，这些统计提供图 38 的推理速度轴。每个试次依据其评分量表及对各臂的明确排序进行评分。只有当请求声明其标签为轮换槽位时，竞技场才会解码试次。无法解析到检查点的行会被跳过而不是猜测，每周审计会把每次已评分试次与其录像所声称提供服务的检查点进行比对。

<a id="S1273"></a>
**Source:** p.69 S1273

**Original:** The leaderboard. Fig. 36 shows the current suite. The top four places are held by GR00T 2 and GR00T 2 Turbo checkpoints, whose intervals overlap. The GR00T 1.7 checkpoint sits about 80 to 110 Elo below them, and 𝜋0.5, adapted to our robot, ranks near the bottom.

**中文:** 排行榜。图 36 展示当前套件。前四名由 GR00T 2 与 GR00T 2 Turbo 的检查点占据，它们的区间相互重叠。GR00T 1.7 检查点约比它们低 80 至 110 Elo，而适配到我们机器人上的 𝜋0.5 排在接近末尾的位置。

<a id="S1274"></a>
**Source:** p.69 S1274

**Original:** Head-to-head. Tab. 13 gives the paired comparisons. GR00T 2 is ahead of 𝜋0.5 by 236 Elo and of GR00T 1.7 by 95 Elo, and both differences hold in every bootstrap resample. GR00T 2 Turbo is statistically indistinguishable from GR00T 2. The same ordering appears in the raw rubric scores of the trials in which both checkpoints ran (Tab. 14): GR00T 2’s advantage over 𝜋0.5 is present on every sub-suite and largest on the medium-to-hard

**中文:** 两两对比。表 13 给出配对比较结果。GR00T 2 领先 𝜋0.5 236 Elo，领先 GR00T 1.7 95 Elo，且两个差值在每一次自助重采样中都成立。GR00T 2 Turbo 与 GR00T 2 在统计上不可区分。在两个检查点都运行过的试次中，原始量表分数呈现相同的排序（表 14）：GR00T 2 相对于 𝜋0.5 的优势在每个子套件上都存在，并且在中到难运动原语上最大。[存疑：该句在 p.69 处截断，原文如此]

<a id="S1276"></a>
**Source:** p.69 S1276

**Original:** The climb. Fig. 37 places every checkpoint against its suite’s reference by the date it was saved. On the current suite, the best checkpoint rose from 206 Elo below today’s best in June to 93 and then 43 below in September, and to 14 below in mid-October (GR00T 2), before the GR00T 2 Turbo checkpoint that now leads. On the

**中文:** 攀升。图 37 把每个检查点与其套件的参考检查点对比，并按其保存日期排列。在当前套件上，最佳检查点从 6 月时比今天的最佳低 206 Elo，到 9 月降为低 93 再降为低 43，到 10 月中旬（GR00T 2）降为低 14，之后是现在领先的 GR00T 2 Turbo 检查点。在

![F036](assets/F036.png)

<a id="C049"></a>
**Source:** p.70 C049 · 图 F036

**Original (caption):** Figure 36: YAM V2 leaderboard. Elo with 90% scene-clustered bootstrap intervals for 20 checkpoints, colored by model family. Numbers on the right are A/B matches. ⋆marks the A/B reference. Development checkpoints are shown under anonymized aliases.

**中文（图注）：** 图 36：YAM V2 排行榜。展示 20 个检查点的 Elo 及其 90% 场景聚类自助法区间，按模型族着色。右侧数字为 A/B 对局数。⋆ 标记 A/B 参考。开发检查点以匿名别名显示。

<a id="S1307"></a>
**Source:** p.70 S1307

**Original:** first suite, the best checkpoint rose from 185 below to 87 below between June and mid-September before the current leader. Because all points come from one fit, these gaps are measured on a common scale even though the checkpoints were evaluated months apart, which is exactly what absolute scores from different sessions cannot provide (Sec. D.1).

**中文:** 第一个套件上，最佳检查点在 6 月至 9 月中旬间从低 185 升至低 87，之后是当前领先者。由于所有点都来自同一次拟合，这些差距是在同一尺度上测量的，即使检查点是相隔数月评测的，而这正是不同会话的绝对分数无法提供的（见 Sec. D.1）。

<a id="S1308"></a>
**Source:** p.70 S1308

**Original:** Skill and speed. Fig. 38 adds the inference cost measured during the same A/B episodes. Among the 21 checkpoints served by the GR00T 2 policy server, the GR00T 2 Turbo reference is both the highest rated and the fastest, with no detectable loss in skill (Tab. 13). On a GeForce RTX 5090 workstation it runs about three times faster than GR00T 2 (52 vs. 171 ms per served call, Fig. 23). The timings in Fig. 38 are server compute recorded in the A/B serving logs. They rank checkpoints within one serving stack, but serving stacks differ in model size, hardware, and compilation, so the figure is not a like-for-like speed comparison across stacks.3

**中文:** 技能与速度。图 38 加入了同一 A/B 回合期间测得的推理开销。在由 GR00T 2 策略服务器提供服务的 21 个检查点中，GR00T 2 Turbo 参考既是评分最高的，也是最快的，且未检测到技能损失（表 13）。在 GeForce RTX 5090 工作站上，它的运行速度约为 GR00T 2 的三倍（每次服务调用 52 对 171 毫秒，图 23）。图 38 中的时间是 A/B 服务日志中记录的服务端计算时间。它们只能在同一服务栈内对检查点排序，但不同服务栈在模型规模、硬件和编译方式上各不相同，因此该图并非跨栈的同类速度比较。3

<a id="S1309"></a>
**Source:** p.70 S1309

**Original:** These serving-log timings are also a different measurement from the median model-prediction latencies on named GPUs in Tab. 27 and from the per-call latencies of the YAM post-training models in Fig. 23.

**中文:** 这些服务日志时间，也与表 27 中具名 GPU 上的中位模型预测时延，以及图 23 中 YAM 后训练模型的单次调用时延是不同的测量。

<a id="S1310"></a>
**Source:** p.70 S1310

**Original:** 3The serving stack is inferred from the model family, since each family runs its own policy server. The per-episode latency records do not include the GPU, host, or compilation settings.

**中文:** 3 服务栈是根据模型族推断的，因为每个族运行自己的策略服务器。逐回合的时延记录不包含 GPU、主机或编译设置。

<a id="C050"></a>
**Source:** p.71 C050 · 表 T014

**Original (caption):** Table 14: Matched rubric scores by sub-suite. Mean rubric score (0 to 1) over the trials in which both checkpoints were graded in the same campaign. Trial counts in parentheses.

**中文（表注）：** 表 14：按子套件的匹配 rubric 分数。两个检查点在同一批次中都被评分的试次上的平均 rubric 分数（0 至 1）。括号内为试次数。

![F037](assets/F037.png)

<a id="C051"></a>
**Source:** p.71 C051 · 图 F037

**Original (caption):** Figure 37: Climbing the hill. Every checkpoint on each suite, rated relative to that suite’s A/B reference (⋆, the top-rated checkpoint) and placed at the date the checkpoint was saved. The line tracks the best checkpoint so far. Bars are paired 90% bootstrap intervals, shown for the checkpoints that set a new best. All points in a panel come from one fit on the same evidence. The two suites are separate leagues. One V1 checkpoint lies below the plotted range.

**中文（图注）：** 图 37：攀升。每个套件上的每个检查点，都相对于该套件的 A/B 参考（⋆，评分最高的检查点）进行评分，并按其保存日期放置。曲线追踪目前为止的最佳检查点。柱子为配对的 90% 自助法区间，仅显示设定了新最佳的检查点。同一面板中的所有点都来自同一次拟合，基于同样的证据。两个套件是各自独立的联盟。有一个 V1 检查点位于绘图范围之下。

<a id="S1341"></a>
**Source:** p.71 S1341

**Original:** How the arena was used. In the final months of the project, the arena was read weekly at the team’s training sync, as the shared reference for which checkpoints had moved the frontier and which differences were still within noise. It separated effects that absolute scores conflated: on the dexterous suite, serving the same checkpoints with a new inference regime reordered the leaderboard (the previous leader fell from first of 13 to fifth of 9), which is why inference settings are part of a checkpoint’s identity there (Sec. D.3). It also provided the real-world ground truth for calibrating simulation: the Bradley-Terry ratings from blinded A/B trials are the real-world side of the simulation-reality correlation in Sec. 4.5.2 (𝑟= 0.93).

**中文:** 竞技场如何被使用。在项目的最后几个月，竞技场每周在团队的训练同步会上被查阅一次，作为判断哪些检查点推动了前沿、哪些差异仍在噪声范围内的共同依据。它把绝对分数混为一谈的效应区分开来：在灵巧手套件上，用新的推理方式服务同一检查点会重排排行榜（此前的领先者从 13 个中的第一降至 9 个中的第五），这也是推理设置在该套件中成为检查点身份一部分的原因（见 Sec. D.3）。它还为仿真校准提供了真实世界的基准：盲测 A/B 试验得到的 Bradley-Terry 评分，即 Sec. 4.5.2 中仿真-现实相关性的现实一侧（𝑟 = 0.93）。
