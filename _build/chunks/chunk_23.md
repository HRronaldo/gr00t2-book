### F.2. Automated Discovery of RL Post-Training Algorithms ｜ 强化学习后训练算法的自动发现

<a id="S1591"></a>
**Source:** p.87 S1591

**Original:** Developing effective RL post-training algorithms for robot foundation models involves choices across objectives, exploration, credit assignment, reward design, and rollout horizons. These decisions interact with task characteristics and model architectures, making algorithm development an iterative process of experimentation and refinement.

**中文:** 为机器人基础模型开发有效的强化学习后训练算法，需要在目标函数、探索、信用分配、奖励设计以及 rollout（轨迹采样）时域等方面作出选择。这些决策与任务特性和模型架构相互影响，因此算法开发是一个通过实验与改进不断迭代的过程。

<a id="S1592"></a>
**Source:** p.87 S1592

**Original:** We leverage AutoRL, an autonomous research framework for closed-loop experimentation, to systematically improve RL post-training algorithms for GR00T 2. The research agent analyzes training failures, proposes hypotheses, modifies code, and evaluates candidate algorithms under fixed protocols. We ran AutoRL for

**中文:** 我们利用 AutoRL（一个用于闭环实验的自主研究框架），系统性地改进 GR00T 2 的强化学习后训练算法。研究智能体分析训练失败、提出假设、修改代码，并在固定协议下评估候选算法。我们将 AutoRL 运行了

![F047](assets/F047.png)

<a id="C064"></a>
**Source:** p.88 C064 · 图 F047

**Original (caption):** Figure 47: Autonomous RL recipe discovery with AutoRL. Hill-climbing performance on RoboCasa365 across successive agent-driven experiments. The curve shows the best evaluation performance achieved.

**中文（图注）：** 图 47：基于 AutoRL 的自主强化学习配方发现。在 RoboCasa365 上，相继由智能体驱动的实验中的爬山式性能变化。曲线表示所达到的最佳评测性能。

<a id="S1616"></a>
**Source:** p.88 S1616

**Original:** approximately 35 days on RoboCasa365 (Nasiriany et al., 2026), using an early developmental GR00T 2 checkpoint and the Atomic-Seen and Composite-Seen tasks.

**中文:** 约 35 天，在 RoboCasa365（Nasiriany et al., 2026）上进行，使用了早期开发版 GR00T 2 检查点以及 Atomic-Seen 与 Composite-Seen 任务。

<a id="S1617"></a>
**Source:** p.88 S1617

**Original:** F.2.1. Autonomous Experimentation Harness

**中文:** F.2.1. 自主实验框架

<a id="S1618"></a>
**Source:** p.88 S1618

**Original:** Each AutoRL discovery round follows four stages. First, the agent analyzes previous experiments, diagnostic metrics, and failure modes to identify bottlenecks. Second, it proposes up to four mutually orthogonal hypotheses, each specifying an isolated mechanism, expected outcome, and falsification criterion. A critic filters out redundant or insufficiently testable proposals. Third, valid hypotheses are implemented in independent branches, locally tested, and submitted for cluster training and evaluation. Finally, candidates are compared with the current best baseline and promoted only when improvements exceed a predefined margin. At most one candidate is promoted per round, while rejected hypotheses remain available as negative evidence.

**中文:** 每一轮 AutoRL 发现包含四个阶段。第一，智能体分析之前的实验、诊断指标和失败模式，以找出瓶颈。第二，它最多提出四个相互正交的假设，每个假设都需说明一个孤立的机制、预期结果和证伪准则。一个评审器（critic）会过滤掉冗余或可检验性不足的提议。第三，有效的假设在独立分支中实现，经过局部测试后提交到集群上进行训练与评测。最后，候选方案与当前最佳基线进行比较，只有当改进超过预定义裕度时才会被晋升。每一轮至多晋升一个候选方案，而被拒绝的假设仍作为负面证据保留可用。

<a id="S1619"></a>
**Source:** p.88 S1619

**Original:** This harness enables systematic exploration of algorithmic modifications beyond conventional hyperparameter tuning.

**中文:** 该实验框架使得对算法改动的系统性探索得以超越常规的超参数调优。

<a id="S1620"></a>
**Source:** p.88 S1620

**Original:** F.2.2. Discovering RL Recipes

**中文:** F.2.2. 强化学习配方的发现

<a id="S1621"></a>
**Source:** p.88 S1621

**Original:** AutoRL starts from a standard PPO implementation and iteratively improves the post-training recipe through successive experiments (Fig. 47). Below, we summarize the eight changes marked in Fig. 47 by the component they affect, each with the best gain over the base model reached after it.

**中文:** AutoRL 从标准的 PPO 实现出发，通过相继的实验迭代改进后训练配方（Fig. 47）。下文按所影响的组件，归纳图 47 中标出的八处改动，并给出每处改动之后相对基础模型所达到的最佳增益。

<a id="S1622"></a>
**Source:** p.88 S1622

**Original:** Weight anchoring and longer rollouts. Early runs showed the actor drifting rapidly from the pretrained weights, losing existing skills before any useful RL gradient appeared, and rollouts on the long-horizon RoboCasa365 tasks ending before the task could be completed. The agent added an 𝐿2 penalty toward the pretrained weights and extended the rollout horizon. Together these give 1.6 percentage points.

**中文:** 权重锚定与更长的 rollout 时域。早期实验显示，actor（策略网络）迅速偏离预训练权重，在出现任何有用的强化学习梯度之前就丢失了已有技能；同时，在长时序的 RoboCasa365 任务上，rollout 在任务完成之前就已结束。智能体加入了一项朝向预训练权重的 𝐿2 惩罚项，并延长了 rollout 时域。二者合计带来 1.6 个百分点的提升。

<a id="S1623"></a>
**Source:** p.89 S1623

**Original:** Replacing the critic (group-relative baseline). The critic’s explained variance stayed near zero, so its advantages were noise. More capacity and warm-up did not help. The agent removed it in favor of a grouprelative baseline in the style of GRPO (Shao et al., 2024), the ℎ𝑔= 0 case of Eq. (12), and extended the horizon further. Cumulative gain: 3.5 percentage points.

**中文:** 替换评判器（组相对基线）。评判器的解释方差始终接近于零，因此其给出的优势估计只是噪声。增加容量与预热也没有帮助。智能体移除了评判器，转而采用仿照 GRPO（Shao et al., 2024）方式的组相对基线，即式 (12) 中 ℎ𝑔= 0 的情形 [公式原文见 p.89]，并进一步延长了时域。累计增益：3.5 个百分点。

<a id="S1624"></a>
**Source:** p.89 S1624

**Original:** Shaping the return (stage progress). Six long-horizon composite tasks still did not move: with binary success every attempt in a group failed identically, leaving no relative signal. For these simulation experiments, the agent introduced stage-progress returns in [0, 1], assigning partial credit according to the furthest subgoal milestone reached. The real-robot experiments instead use binary task-success returns, as defined in Sec. F.1.1. Cumulative gain: 4.1 percentage points.

**中文:** 塑造回报（阶段进度）。六个长时序组合任务仍然没有改善：在二值成功信号下，组内每次尝试都以相同方式失败，因而没有相对信号。对于这些仿真实验，智能体引入了取值在 [0, 1] 之间的阶段进度回报，按照所达到的最远子目标里程碑给予部分得分。真实机器人实验则改用二值任务成功回报，其定义见 Sec. F.1.1。累计增益：4.1 个百分点。

<a id="S1625"></a>
**Source:** p.89 S1625

**Original:** Balancing long and short tasks. Long tasks were trained with an execution horizon of 16 but scored with 8, and training them at 8 as well raised the cumulative gain to 5.0 percentage points. An advantage weight of 2.5 on long tasks crowded out the short ones, and lowering it to 1.5 gave 6.5 percentage points.

**中文:** 平衡长短任务。长任务以执行时域 16 进行训练，却以 8 进行评分；若同样以 8 进行训练，累计增益提升至 5.0 个百分点。长任务上 2.5 的优势权重挤占了短任务，将其降至 1.5 后，累计增益达到 6.5 个百分点。

<a id="S1626"></a>
**Source:** p.89 S1626

**Original:** Less noisy advantages (grouping and stage credit). Task difficulty varied widely within a group, which made the group-relative advantages noisy. Grouping rollouts by initial scene and seed raised the cumulative gain to 7.5 percentage points. Failures often came after some stages had already been completed, so the agent added stage-aware credit within each episode, which gave 7.9 percentage points.

**中文:** 降低优势估计的噪声（分组与阶段信用）。组内任务难度差异很大，使得组相对优势噪声较大。按初始场景和随机种子对 rollout 进行分组后，累计增益提升至 7.5 个百分点。失败往往发生在部分阶段已经完成之后，因此智能体在每个回合内加入了阶段感知的信用分配，带来 7.9 个百分点的累计增益。

<a id="S1627"></a>
**Source:** p.89 S1627

**Original:** Remembering each context (persistent baseline). Progress rewards do not help contexts the policy already solves every time or never advances at all. Their groups stay uniform and a current-group baseline gives them zero advantage, and on RoboCasa365 such contexts are most of the data. The agent gave every context a memory of its past returns, an exponential moving average across rounds (Eq. (14)), folded into the leave-oneout baseline as a small number of pseudo-observations (Eq. (12)). This baseline retains a learning signal for uniform-outcome groups when their current returns differ from past performance. The same context statistics also guide rollout allocation away from consistently solved contexts. Cumulative gain: 10.0 percentage points.

**中文:** 记住每个上下文（持久基线）。对于策略每次都已解决或始终无法推进的上下文，进度奖励并无帮助。这些上下文所在的组结果始终一致，而当前组基线会给它们零优势；在 RoboCasa365 上，此类上下文占据了大部分数据。智能体为每个上下文记录了其过去回报的记忆，即跨轮次的指数移动平均（式 (14)），并以少量伪观测的形式并入留一法基线（式 (12)）。当结果一致的组其当前回报与过去表现不同时，该基线仍能为其保留学习信号。同样的上下文统计量还用于指导 rollout 分配，使其避开持续被解决的上下文。累计增益：10.0 个百分点。

<a id="S1628"></a>
**Source:** p.89 S1628

**Original:** These experiments demonstrate how AutoRL systematically discovers effective post-training strategies: stabilizing policy optimization, replacing an uninformative critic, balancing long and short tasks, improving credit assignment, and keeping a learning signal alive on saturated and unsolved tasks. The resulting algorithm forms the foundation of our direct GR00T 2 post-training approach, which we further adapt to GR00T 2’s joint video-action architecture and real-world robot interaction. As demonstrated in Sec. F.4, this approach achieves substantial improvements on contact-rich manipulation tasks.

**中文:** 这些实验展示了 AutoRL 如何系统性地发现有效的后训练策略：稳定策略优化、替换无信息量的评判器、平衡长短任务、改进信用分配，以及在已饱和和未解决的任务上保持学习信号。由此得到的算法构成了我们直接进行 GR00T 2 后训练方法的基础，我们进一步使其适配 GR00T 2 的视频-动作联合架构以及真实机器人交互。如 Sec. F.4 所示，该方法在富接触操作任务上取得了显著提升。

### F.3. Online RL Post-Training Infrastructure ｜ 在线强化学习后训练基础设施

<a id="S1629"></a>
**Source:** p.89 S1629

**Original:** Real-robot RL requires repeated coordination among data collection, reward annotation, policy optimization, and evaluation. These stages have different resource requirements and execution rates, while physical interaction and scene resets constrain collection throughput. We develop shared infrastructure that supports heterogeneous learning algorithms, reduces iteration overhead, and preserves experience across failures (Fig. 48).

**中文:** 真实机器人强化学习需要在数据采集、奖励标注、策略优化与评测之间反复协调。这些阶段的资源需求与执行速率各不相同，而物理交互与场景复位限制了采集的吞吐量。我们开发了共享基础设施，用以支持异构的学习算法、降低迭代开销，并在故障之后保留经验（Fig. 48）。

<a id="S1630"></a>
**Source:** p.89 S1630

**Original:** Shared Experience Buffer. Our infrastructure uses a shared experience buffer backed by Lance (Pace et al., 2025). Experience records are constructed incrementally as collection, scoring, and batch preparation produce their outputs. Workers can selectively access relevant fields, while training updates use pinned table versions to ensure stable inputs (Lance Contributors, 2026). Common record identities and policy provenance associate observations, rewards, and updates, and algorithm-defined schemas support different post-training methods within the same data infrastructure.

**中文:** 共享经验缓冲区。我们的基础设施使用由 Lance 支撑的共享经验缓冲区（Pace et al., 2025）。经验记录随采集、评分与批次准备的输出而逐步构建。工作节点可以有选择地访问相关字段，而训练更新则使用固定的表版本以保证输入稳定（Lance Contributors, 2026）。统一的记录标识与策略溯源将观测、奖励和更新关联起来，由算法定义的 schema 则使同一数据基础设施能够支持不同的后训练方法。

<a id="S1631"></a>
**Source:** p.89 S1631

**Original:** Resource-Efficient Execution. Collection, training, and evaluation use independently configurable resource pools. Compatible GPU resources can be reassigned according to workload dependencies, accommodating both on-policy and off-policy learning. Incremental uploads and prefetching overlap collection, data transfer, scoring, decoding, and training preparation, reducing idle time between iterations.

**中文:** 资源高效执行。采集、训练与评测分别使用可独立配置的资源池。兼容的 GPU 资源可根据工作负载的依赖关系重新分配，同时支持同策略与异策略学习。增量上传与预取使采集、数据传输、评分、解码和训练准备相互重叠，减少迭代之间的空闲时间。

<a id="S1632"></a>
**Source:** p.90 S1632

**Original:** A Algorithm interface Control Experience / policy

**中文:** A 算法接口 控制 经验 / 策略 [存疑：图内标签抽取顺序混乱]

<a id="S1633"></a>
**Source:** p.90 S1633

**Original:** Experience schema / Reward computation / Batch preparation / Optimization rules

**中文:** 经验 schema / 奖励计算 / 批次准备 / 优化规则

<a id="S1634"></a>
**Source:** p.90 S1634

**Original:** Policy updates Coordination

**中文:** 策略更新 协调

<a id="S1635"></a>
**Source:** p.90 S1635

**Original:** Assign work

**中文:** 分配任务

<a id="S1636"></a>
**Source:** p.90 S1636

**Original:** Collection Scoring Training Evaluation

**中文:** 采集 评分 训练 评测

<a id="S1637"></a>
**Source:** p.90 S1637

**Original:** Advance phases

**中文:** 推进阶段

<a id="S1638"></a>
**Source:** p.90 S1638

**Original:** Sync policies

**中文:** 同步策略

<a id="S1639"></a>
**Source:** p.90 S1639

**Original:** Monitor workers

**中文:** 监控工作节点

<a id="S1640"></a>
**Source:** p.90 S1640

**Original:** Shared experience buffer Training checkpoints

**中文:** 共享经验缓冲区 训练检查点

![F048](assets/F048.png)

<a id="C065"></a>
**Source:** p.90 C065 · 图 F048

**Original (caption):** Figure 48: Online post-training infrastructure. (A) Algorithm interfaces, worker groups, and shared services. (B) Resource allocation across execution roles. (C) Experience pipelining. (D) Stateful recovery. Execution patterns are illustrative.

**中文（图注）：** 图 48：在线后训练基础设施。(A) 算法接口、工作组与共享服务。(B) 跨执行角色的资源分配。(C) 经验流水线。(D) 有状态恢复。执行模式仅作示意。

<a id="S1656"></a>
**Source:** p.90 S1656

**Original:** Stateful Recovery. Physical experience is expensive to reproduce, making robustness to interrupted training essential. Our infrastructure retains experience data and feedback alongside model and optimizer checkpoints. Recovery distinguishes experience already reflected in a restored checkpoint, data associated with discarded updates, and unused data. Compatible experience can subsequently be reused for resumed training or offline learning, reducing redundant physical interaction. This complements prior work on distributed RL execution and durable robot experience data (Yu et al., 2026a; Zang et al., 2026a,b; Wang et al., 2026; Chen et al., 2026c).

**中文:** 有状态恢复。物理经验的复现成本高昂，因此对中断训练的鲁棒性至关重要。我们的基础设施将经验数据和反馈与模型及优化器检查点一并保存。恢复过程会区分三类数据：已体现在所恢复检查点中的经验、与被丢弃更新相关的数据，以及未使用的数据。兼容的经验随后可用于恢复训练或离线学习，从而减少重复的物理交互。这补充了已有关于分布式强化学习执行与持久化机器人经验数据的工作（Yu et al., 2026a; Zang et al., 2026a,b; Wang et al., 2026; Chen et al., 2026c）。

<a id="S1657"></a>
**Source:** p.90 S1657

**Original:** Execution Efficiency. We evaluate infrastructure efficiency in simulation and real-robot training.

**中文:** 执行效率。我们在仿真与真实机器人训练中评估基础设施的效率。

<a id="S1658"></a>
**Source:** p.90 S1658

**Original:** In RoboCasa365 GRPO, rollout and training alternate on a shared 40-GPU pool while evaluation retains 40 GPUs. This reduces total allocation from 120 to 80 GPUs and enables evaluation to overlap training. Across eight rounds and nine evaluations, execution time decreases from 14.1 to 8.8 hours, corresponding to approximately 1.6× improvement in update throughput.

**中文:** 在 RoboCasa365 GRPO 中，rollout 与训练交替使用一个共享的 40 块 GPU 资源池，而评测保留 40 块 GPU。这将总分配量从 120 块 GPU 减少到 80 块，并使评测能够与训练重叠进行。在八轮训练与九次评测中，执行时间从 14.1 小时减少到 8.8 小时，对应更新吞吐量提升约 1.6×。

<a id="S1659"></a>
**Source:** p.90 S1659

**Original:** For single-robot GRPO (Tab. 18), experience pipelining and trainer-ready records reduce upload and conversion time from approximately 50 minutes to one minute, while transferring only tuned weights reduces policy download time from approximately 30 minutes to one minute. Total iteration time decreases from between 140 and 160 minutes to between 62 and 72 minutes, yielding approximately 2.2× iteration throughput. Incremental uploads overlap data transfer with physical collection, leaving only a short data-handling delay at the end of each round. These mechanisms reduce overhead without requiring faster robot execution, allowing more

**中文:** 对于单机器人 GRPO（Tab. 18），经验流水线与可直接供训练器使用的记录将上传与转换时间从约 50 分钟缩短至 1 分钟，而仅传输调优后的权重则将策略下载时间从约 30 分钟缩短至 1 分钟。总迭代时间从 140 至 160 分钟减少到 62 至 72 分钟，迭代吞吐量约提升 2.2×。增量上传使数据传输与物理采集相互重叠，每轮结束时只剩下很短的数据处理延迟。这些机制在不要求机器人执行更快的前提下降低了开销，使得

![T018](assets/T018.png)

<a id="C066"></a>
**Source:** p.91 C066 · 表 T018

**Original (caption):** Table 18: Per-iteration time breakdown for single-robot GRPO. All times are reported in minutes.

**中文（表注）：** 表 18：单机器人 GRPO 每次迭代的时间分解。所有时间均以分钟为单位。

![F049](assets/F049.png)

<a id="C067"></a>
**Source:** p.91 C067 · 图 F049

**Original (caption):** Figure 49: Real-world RL tasks. (A) Fixed-pipe fittings: grasp, align, engage threads, turn, and release. (B) Finger placement: grasp, align two pins with the base holes, insert, and release. (C) Cable insertion: plug an Ethernet cable into a network switch. (D) Charger insertion: plug a charger into an outlet.

**中文（图注）：** 图 49：真实世界强化学习任务。(A) 固定管件：抓取、对准、啮合螺纹、旋转并释放。(B) 手指放置：抓取、将两根销钉对准底座孔位、插入并释放。(C) 线缆插入：将以太网线插入网络交换机。(D) 充电器插入：将充电器插入插座。

<a id="S1674"></a>
**Source:** p.91 S1674

**Original:** efficient use of limited physical interaction resources.

**中文:** 更高效地利用有限的物理交互资源。
