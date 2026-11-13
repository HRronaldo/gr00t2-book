### F.1. RL-Based Adaptation of World-Action Models ｜ 基于强化学习的世界-动作模型适配

<a id="S1494"></a>
**Source:** p.84 S1494

**Original:** We investigate two complementary strategies for adapting GR00T 2. Direct GR00T 2 post-training updates the pretrained model through RL or self-imitation, while residual RL freezes GR00T 2 and learns a lightweight corrective policy. The former improves the underlying generative policy, whereas the latter targets precisioncritical stages where GR00T 2 already produces approximately correct behaviors.

**中文:** 我们研究两种互补的 GR00T 2 适配策略。直接对 GR00T 2 进行后训练，会通过强化学习（RL）或自模仿（self-imitation）更新预训练模型本身；残差强化学习（residual RL）则冻结 GR00T 2，只学习一个轻量级的纠正策略。前者改进底层的生成式策略，后者针对精度关键阶段，即 GR00T 2 已经能给出近似正确行为的阶段。

<a id="S1495"></a>
**Source:** p.84 S1495

**Original:** F.1.1. Direct GR00T 2 Post-Training

**中文:** F.1.1. 直接 GR00T 2 后训练

<a id="S1496"></a>
**Source:** p.84 S1496

**Original:** Stochastic Exploration with CPS. To enable exploration and likelihood-based policy optimization (Liu et al., 2025; Lei et al., 2026), we replace GR00T 2’s deterministic Euler action updates with Coefficients-Preserving Sampling (CPS) (Wang and Yu, 2025) during rollout. Noise is injected only into the action denoising process. Video denoising remains deterministic given its initial latent, while video features continue to condition action generation.

**中文:** 基于 CPS 的随机探索。为了实现探索以及基于似然的策略优化（Liu et al., 2025; Lei et al., 2026），我们在 rollout（轨迹采样）时，把 GR00T 2 确定性的欧拉动作更新替换为保系数采样（CPS）（Wang and Yu, 2025）。噪声只注入动作去噪过程。给定初始潜变量，视频去噪仍是确定性的，而视频特征继续为动作生成提供条件。

<a id="S1497"></a>
**Source:** p.84 S1497

**Original:** Following DPPO (Ren et al., 2025) and RL-100 (Lei et al., 2026), we optimize GR00T 2 through its action denoising process. Let 𝑡index environment decisions and 𝑘index action-denoising events. GR00T 2 uses four such events: joint passes (𝑘= 0, 2) update video and action latents through a shared DiT, while cached passes (𝑘= 1, 3) update action tokens using video and state keys and values from the preceding joint pass (Fig. 46).

**中文:** 沿用 DPPO（Ren et al., 2025）与 RL-100（Lei et al., 2026）的做法，我们通过动作去噪过程优化 GR00T 2。令 𝑡 为环境决策的索引，𝑘 为动作去噪事件的索引。GR00T 2 共有四个这样的事件：联合前向传播（joint pass，𝑘= 0, 2）通过共享的 DiT 同时更新视频潜变量与动作潜变量；缓存前向传播（cached pass，𝑘= 1, 3）则利用前一次联合前向传播得到的视频与状态的键（key）和值（value）更新动作 token（Fig. 46）。

<a id="S1498"></a>
**Source:** p.84 S1498

**Original:** After denoising, the first 𝐻𝑒actions are executed, where 𝐻𝑒is the executed action horizon.

**中文:** 去噪完成后，执行前 𝐻𝑒 个动作，其中 𝐻𝑒 为执行动作时域（executed action horizon）。

<a id="S1500"></a>
**Source:** p.84 S1500

**Original:** 𝑡 the intermediate action latent at environment decision 𝑡and denoising event 𝑘, and v(𝑘)

**中文:** [存疑：抽取残片，句首主语缺失] 𝑡 为环境决策 𝑡 与去噪事件 𝑘 处的中间动作潜变量，v(𝑘)。[公式原文见 p.84]

<a id="S1501"></a>
**Source:** p.84 S1501

**Original:** 𝜃,𝑡the corresponding action velocity in the noise-minus-data convention. The noise schedule 𝜎𝑘decreases from 𝜎0 = 1 to 𝜎4 = 0. The clean-action and noise estimates are

**中文:** 𝜃,𝑡 为对应的动作速度，采用“噪声减数据”约定。噪声调度 𝜎𝑘 从 𝜎0 = 1 递减至 𝜎4 = 0。干净动作估计与噪声估计为 [存疑：此处公式未抽取] [公式原文见 p.84]

![F046](assets/F046.png)

<a id="C063"></a>
**Source:** p.85 C063 · 图 F046

**Original (caption):** Figure 46: Joint video-action denoising with CPS exploration. Four action-denoising events alternate between joint and cached passes. CPS adds fresh noise only to executed action coordinates. Video denoising is deterministic given its initial latent. GRPO scores joint action transitions and backpropagates through their joint forward passes, with carried latents detached.

**中文（图注）：** 图 46：采用 CPS 探索的联合视频-动作去噪。四个动作去噪事件在联合前向传播与缓存前向传播之间交替。CPS 只向可执行的动作坐标加入新噪声。给定初始潜变量，视频去噪是确定性的。GRPO 对联合动作转移打分，并通过其联合前向传播反向传播，其中携带的潜变量被分离（detach）。

<a id="S1524"></a>
**Source:** p.85 S1524

**Original:** Using clipped transition standard deviations (Lei et al., 2026), we sample

**中文:** 利用截断后的转移标准差（Lei et al., 2026），我们按以下方式采样 [存疑：此处采样公式未抽取]

<a id="S1533"></a>
**Source:** p.85 S1533

**Original:** Here 𝜂controls stochastic exploration, 𝜇𝜃,𝑡,𝑘is the CPS transition mean, and 𝑠𝑘is its standard deviation, bounded by 𝑠min > 0 and 𝑠max. The subscript exec denotes active coordinates in the first 𝐻𝑒action rows. Noise injection and likelihood evaluation are restricted to these coordinates, excluding padding. CPS provides explicit Gaussian transition densities for subsequent policy optimization.

**中文:** 其中 𝜂 控制随机探索，𝜇𝜃,𝑡,𝑘 为 CPS 转移均值，𝑠𝑘 为其标准差，并受 𝑠min > 0 与 𝑠max 约束。下标 exec 表示前 𝐻𝑒 个动作行中的有效坐标。噪声注入与似然评估仅限于这些坐标，并排除填充部分。CPS 为后续策略优化提供了显式的高斯转移密度。

<a id="S1534"></a>
**Source:** p.85 S1534

**Original:** Online RL with GRPO. We optimize GR00T 2 from its own successful and failed rollouts with a GRPO-style algorithm developed through AutoRL (Sec. F.2). A training round collects 𝑁𝑔attempts for each selected reset context 𝑔(a task paired with a scene layout) under a fixed behavior policy. Attempt 𝑖of context 𝑔receives a binary return 𝑅𝑔,𝑖∈{0, 1}.

**中文:** 基于 GRPO 的在线 RL。我们使用通过 AutoRL 开发的类 GRPO 算法（Sec. F.2），基于 GR00T 2 自身成功与失败的 rollout 对其进行优化。每一轮训练在固定的行为策略下，为每个选定的重置上下文（reset context，即一个任务与一个场景布局的组合）收集 𝑁𝑔 次尝试。上下文 𝑔 的第 𝑖 次尝试获得二值回报 𝑅𝑔,𝑖∈{0, 1}。

<a id="S1535"></a>
**Source:** p.85 S1535

**Original:** Leave-one-out advantages with a context memory. With a baseline computed solely from the current group, uniform outcomes yield zero reward-based advantages. We incorporate a historical per-context mean to retain a learning signal when current outcomes differ from past performance. The baseline for attempt 𝑖pools the other 𝑁𝑔−1 returns of its context with ℎ𝑔pseudo-returns fixed at the context’s historical mean 𝑚𝑔:

**中文:** 带上下文记忆的留一优势。若基线仅由当前组计算，则结果一致时基于奖励的优势为零。我们引入每个上下文的历史均值，使当前结果与过去表现不同时仍能保留学习信号。第 𝑖 次尝试的基线，汇集了其上下文中其余 𝑁𝑔−1 个回报，以及 ℎ𝑔 个伪回报，这些伪回报固定为该上下文的历史均值 𝑚𝑔：

![E005](assets/equations/E005.png)

<a id="E005"></a>
**Source:** p.85 E005

**Original:** 𝑗̸=𝑖𝑅𝑔,𝑗 ℎ𝑔+ 𝑁𝑔−1 , 𝐴𝑔,𝑖= 𝑅𝑔,𝑖−𝑏𝑔,𝑖. (12)

**中文:** 式 (12) 给出基线 𝑏𝑔,𝑖：它是同一上下文中其余 𝑁𝑔−1 次尝试的回报与 ℎ𝑔 个固定为历史均值 𝑚𝑔 的伪回报的平均；优势 𝐴𝑔,𝑖 为 𝑅𝑔,𝑖 减去 𝑏𝑔,𝑖。

$$𝑗̸=𝑖𝑅𝑔,𝑗 ℎ𝑔+ 𝑁𝑔−1 , 𝐴𝑔,𝑖= 𝑅𝑔,𝑖−𝑏𝑔,𝑖. (12)$$ [公式原文见 p.85]

<a id="S1538"></a>
**Source:** p.85 S1538

**Original:** With ℎ𝑔= 0 this is the leave-one-out baseline of RLOO (Ahmadian et al., 2024). We use ℎ𝑔= 0 only on a context’s first visit and ℎ𝑔= ℎ= 2 afterwards. A uniform failure in a context that used to succeed at rate 𝑚𝑔 now yields a negative advantage of magnitude ℎ𝑚𝑔/(ℎ+ 𝑁𝑔−1), and a uniform success in a historically weak context yields the mirror image.

**中文:** 当 ℎ𝑔= 0 时，上式即 RLOO（Ahmadian et al., 2024）的留一基线。我们仅在上下文首次访问时使用 ℎ𝑔= 0，之后取 ℎ𝑔= ℎ= 2。若某上下文过去以成功率 𝑚𝑔 成功，而现在结果一致地失败，则其优势为负，幅度为 ℎ𝑚𝑔/(ℎ+ 𝑁𝑔−1)；若某个历史上表现较弱的上下文结果一致地成功，则得到镜像结果。

<a id="S1539"></a>
**Source:** p.85 S1539

**Original:** Let 𝑇𝑔,𝑖be the number of environment decisions in an attempt. The attempt’s advantage is spread evenly over its decisions and rescaled once per batch, so that long attempts do not dominate merely by containing more decisions, and 𝑐is applied only when the batch has nonzero advantage mass. The sums defining 𝑐run over the collected attempts.

**中文:** 设 𝑇𝑔,𝑖 为一次尝试中的环境决策数。该次尝试的优势被均匀分摊到其每个决策上，并在每个批次中统一重新缩放，使长尝试不会仅因包含更多决策而占据主导。仅当批次的优势总量非零时才应用 𝑐。定义 𝑐 的求和遍历所有已收集的尝试。

<a id="S1548"></a>
**Source:** p.86 S1548

**Original:** Persistent context table. The historical means 𝑚𝑔live in a global table indexed by context. The table persists across rounds and, through checkpointing, across training segments, so it records how well the policy has done in every context so far. Once a round’s advantages have been computed, each visited context is updated by an exponential moving average of its round mean, with 𝛼EMA = 0.25 and 𝑚𝑔= 𝜇𝑔on the first visit. Unvisited contexts are left untouched. Updating the table after advantage computation ensures that the historical term uses only preceding rounds.

**中文:** 持久化的上下文表。历史均值 𝑚𝑔 存放在一个按上下文索引的全局表中。该表跨轮次保留，并通过检查点跨越训练片段持续存在，因此它记录了策略迄今在每个上下文中的表现。每轮优势计算完成后，每个被访问的上下文都以其本轮均值的指数滑动平均（EMA）进行更新，其中 𝛼EMA = 0.25，首次访问时取 𝑚𝑔= 𝜇𝑔。未被访问的上下文保持不变。在优势计算之后再更新该表，可确保历史项只使用此前的轮次。

<a id="S1555"></a>
**Source:** p.86 S1555

**Original:** Clipped transition-level objective for a denoising policy. GR00T 2 produces actions by iterative denoising, so the exact action log-likelihood that GRPO would compare between policies is not available. CPS, however, gives a Gaussian density for every action-denoising transition, and we score the policy on those transitions instead. On the selected joint denoising events 𝒦= {0, 2} we maximize the clipped surrogate (Liu et al., 2025; Lei et al., 2026; Schulman et al., 2017)

**中文:** 面向去噪策略的截断转移级目标。GR00T 2 通过迭代去噪生成动作，因此 GRPO 在策略之间比较时所需的精确动作对数似然不可得。然而，CPS 为每个动作去噪转移提供了高斯密度，因此我们改为在这些转移上对策略打分。在选定的联合去噪事件 𝒦= {0, 2} 上，我们最大化截断代理目标（clipped surrogate）（Liu et al., 2025; Lei et al., 2026; Schulman et al., 2017）。

<a id="S1558"></a>
**Source:** p.86 S1558

**Original:** 𝑟𝑔,𝑖,𝑡,𝑘ˆ𝐴𝑔,𝑖,𝑡, clip(𝑟𝑔,𝑖,𝑡,𝑘, 1 −𝜖clip, 1 + 𝜖clip) ˆ𝐴𝑔,𝑖,𝑡 min where ℬis the batch of recorded decisions, 𝜖clip is the clipping threshold, and 𝑟= exp(ℓ𝜃−ℓold) is the current-tobehavior likelihood ratio for one recorded transition. Gaussian log densities condition on the observation context and input action latent at event 𝑘and sum over executed coordinates. Ratios are not multiplied across events or decisions. In practice, rather than sampling 𝑘, each minibatch scores one joint event, alternating between 𝑘= 0 and 𝑘= 2. Recorded action latents are teacher-forced, while video computation is reconstructed under the current parameters. Gradients flow through the selected joint pass, including the shared DiT, state/action encoders, and action decoder. Carried latents are detached, yielding a local surrogate without backpropagation through the full denoising chain.

**中文:** 截断目标式的抽取残缺（残留片段为 `𝑟𝑔,𝑖,𝑡,𝑘ˆ𝐴𝑔,𝑖,𝑡, clip(…) ˆ𝐴𝑔,𝑖,𝑡 min`），[公式原文见 p.86]。其中 ℬ 为已记录决策的批次，𝜖clip 为截断阈值，𝑟= exp(ℓ𝜃−ℓold) 为单个已记录转移上，当前策略相对行为策略的似然比。高斯对数密度以观测上下文及事件 𝑘 处的输入动作潜变量为条件，并对可执行坐标求和。比值不会跨事件或跨决策相乘。实践中，并不对 𝑘 进行采样，而是每个小批次对一个联合事件打分，并在 𝑘= 0 与 𝑘= 2 之间交替。已记录的动作潜变量采用教师强制，而视频计算则在当前参数下重新构建。梯度经所选的联合前向传播回传，包括共享的 DiT、状态/动作编码器与动作解码器。携带的潜变量被分离（detach），从而得到一个局部代理目标，无需反向传播穿过完整的去噪链。

<a id="S1564"></a>
**Source:** p.86 S1564

**Original:** GRPO-Induced Self-Imitation. Online RL enables GR00T 2 to discover successful behaviors through exploration, while supervised learning provides a potentially more stable optimization approach for consolidating these behaviors. We investigate GRPO-induced self-imitation, combining the exploration capabilities of RL with the optimization stability of supervised fine-tuning.

**中文:** GRPO 诱导的自模仿。在线 RL 使 GR00T 2 能够通过探索发现成功行为，而监督学习则可能提供一种更稳定的优化方式，用于巩固这些行为。我们研究 GRPO 诱导的自模仿，将 RL 的探索能力与监督微调（SFT）的优化稳定性相结合。

<a id="S1565"></a>
**Source:** p.86 S1565

**Original:** We retain successful episodes from the full set of rollouts used to train the best-performing GRPO checkpoint, forming 𝒟succ. Starting from the same SFT initialization as GRPO, we perform one round of fine-tuning using GR00T 2’s original joint video-action objective:

**中文:** 我们从用于训练表现最佳的 GRPO 检查点的全部 rollout 中保留成功的回合，构成 𝒟succ。从与 GRPO 相同的 SFT 初始化出发，我们使用 GR00T 2 原始的联合视频-动作目标进行一轮微调：

![E006](assets/equations/E006.png)

<a id="E006"></a>
**Source:** p.86 E006

**Original:** ℒSI(𝜃) = 𝜆vℒvideo(𝜃; 𝒟succ) + 𝜆aℒaction(𝜃; 𝒟succ). (16)

**中文:** 式 (16) 为自模仿的训练目标：以成功回合集合 𝒟succ 为数据，对视频损失与动作损失分别按权重 𝜆v、𝜆a 加权求和。

$$ℒSI(𝜃) = 𝜆vℒvideo(𝜃; 𝒟succ) + 𝜆aℒaction(𝜃; 𝒟succ). (16)$$

<a id="S1566"></a>
**Source:** p.86 S1566

**Original:** Here ℒvideo and ℒaction denote GR00T 2’s original video and action denoising objectives, and 𝜆v and 𝜆a control their relative weights.

**中文:** 其中 ℒvideo 与 ℒaction 分别表示 GR00T 2 原始的视频去噪目标与动作去噪目标，𝜆v 与 𝜆a 控制二者的相对权重。

<a id="S1567"></a>
**Source:** p.86 S1567

**Original:** Task success determines which trajectories are selected, while the learning signal comes from the original video and action supervision. This enables GR00T 2 to benefit from RL-discovered successful behaviors while optimizing a standard supervised objective, without additional robot rollouts, demonstrations, or human corrective actions.

**中文:** 任务成功与否决定选取哪些轨迹，而学习信号则来自原始的视频与动作监督。这使 GR00T 2 能够在优化标准监督目标的同时，利用 RL 发现的成功行为，且无需额外的机器人 rollout、演示数据或人工纠正动作。

<a id="S1569"></a>
**Source:** p.87 S1569

**Original:** F.1.2. Residual Reinforcement Learning

**中文:** F.1.2. 残差强化学习（Residual Reinforcement Learning）

<a id="S1570"></a>
**Source:** p.87 S1570

**Original:** Direct GR00T 2 post-training updates the generative policy itself. A complementary approach is to retain GR00T 2’s pretrained capabilities and learn targeted corrections for precision-critical stages, where approximately correct trajectories can still fail because of small alignment or contact errors.

**中文:** 直接对 GR00T 2 进行后训练，会更新生成式策略本身。另一种互补的做法是保留 GR00T 2 的预训练能力，并针对精度关键阶段学习有针对性的纠正。在这些阶段，即使轨迹大致正确，仍可能因微小的对齐或接触误差而失败。

<a id="S1571"></a>
**Source:** p.87 S1571

**Original:** We keep GR00T 2 frozen and train a lightweight residual policy to correct its actions online. Unlike direct GR00T 2 training, residual RL does not use CPS. Instead, it relies on the stochastic residual actor for exploration.

**中文:** 我们冻结 GR00T 2，并在线训练一个轻量级的残差策略来修正其动作。与直接训练 GR00T 2 不同，残差 RL 不使用 CPS，而是依靠随机残差 actor 进行探索。

<a id="S1572"></a>
**Source:** p.87 S1572

**Original:** The residual operates within designated task stages. At each decision 𝑗, a tanh-squashed Gaussian actor 𝜋𝜑 receives observations z𝑗comprising camera images, proprioception, GR00T 2’s forecast end-effector targets, and the current correction offset. The actor produces a bounded residual action a𝑗over the next control horizon.

**中文:** 残差在指定的任务阶段内运行。在每个决策 𝑗 处，tanh 压缩的高斯 actor 𝜋𝜑 接收观测 z𝑗，包括相机图像、本体感知、GR00T 2 预测的末端执行器目标以及当前的修正偏移。该 actor 在接下来的控制时域内输出一个有界的残差动作 a𝑗。

<a id="S1573"></a>
**Source:** p.87 S1573

**Original:** Per-tick corrections are accumulated into bounded offsets and composed with GR00T 2’s targets:

**中文:** 逐 tick 的修正被累加为有界偏移，并与 GR00T 2 的目标合成：

<a id="S1576"></a>
**Source:** p.87 S1576

**Original:** xcmd

**中文:** [存疑：抽取失败，此处仅残留 xcmd，对应公式未能抽取] [公式原文见 p.87]

<a id="S1579"></a>
**Source:** p.87 S1579

**Original:** Here o𝑗is the accumulated correction offset, 𝛿is the per-tick correction scale, 𝛾is the correction gain, and B denotes axis-wise offset bounds. The operator ⊕composes the correction offset with GR00T 2’s end-effector target. Zero residual action leaves the current offset unchanged, while zero offset recovers the base policy.

**中文:** 其中 o𝑗 为累积的修正偏移，𝛿 为逐 tick 修正尺度，𝛾 为修正增益，B 表示逐轴的偏移界。算子 ⊕ 将修正偏移与 GR00T 2 的末端执行器目标合成。零残差动作使当前偏移保持不变，而零偏移则恢复为基础策略。

<a id="S1580"></a>
**Source:** p.87 S1580

**Original:** Following HIL-SERL (Luo et al., 2025), we train the residual actor using Soft Actor-Critic (SAC) (Haarnoja et al., 2018) with prior demonstrations and online interaction, including occasional human corrections. Evaluation episodes are manually scored using binary task-specific success criteria.

**中文:** 沿用 HIL-SERL（Luo et al., 2025）的做法，我们使用软演员-评论家算法（Soft Actor-Critic, SAC）（Haarnoja et al., 2018）训练残差 actor，训练数据包括先验演示数据、在线交互，以及偶尔出现的人工纠正。评测回合依据任务相关的二值成功标准进行人工评分。

<a id="S1581"></a>
**Source:** p.87 S1581

**Original:** We draw half of each critic batch from online data and half from demonstrations, and train an ensemble of critics using bootstrapped returns. The actor objective combines entropy-regularized policy improvement with a zero-residual prior and imitation of successful residual actions:

**中文:** 每个评论家（critic）批次的一半取自在线数据，另一半取自演示数据，并使用自举回报训练评论家集成。actor 目标结合了熵正则化的策略改进、零残差先验，以及对成功残差动作的模仿：

<a id="S1589"></a>
**Source:** p.87 S1589

**Original:** Here 𝜑and 𝜓denote the residual actor and critic parameters, respectively. The distribution 𝒟RL represents observations sampled from the training replay buffer. The function ¯𝑄𝜓is the ensemble critic mean, 𝜇𝜑is the actor mean, and 𝒟+ contains successful residual experience. The entropy coefficient 𝛼controls exploration, while 𝜆𝑄, 𝜆0, and 𝜆bc weight the critic, zero-residual regularization, and behavior-cloning terms, respectively.

**中文:** 其中 𝜑 与 𝜓 分别为残差 actor 与 critic 的参数。分布 𝒟RL 表示从训练回放缓冲区中采样的观测。函数 ¯𝑄𝜓 为评论家集成的均值，𝜇𝜑 为 actor 均值，𝒟+ 包含成功的残差经验。熵系数 𝛼 控制探索，而 𝜆𝑄、𝜆0 与 𝜆bc 分别为评论家项、零残差正则项与行为克隆项的权重。[存疑：紧邻的 actor 目标式未抽取]

<a id="S1590"></a>
**Source:** p.87 S1590

**Original:** The zero-residual prior discourages unnecessary corrections, while successful experience reinforces effective behavior. Residual RL thus enables targeted adaptation without modifying pretrained GR00T 2 weights.

**中文:** 零残差先验抑制不必要的修正，而成功经验则强化有效行为。因此，残差 RL 能够在不修改预训练 GR00T 2 权重的前提下，实现有针对性的适配。
