### I.2. Policy Smoothness ｜ 策略平滑性

<a id="S2087"></a>
**Source:** p.115 S2087

**Original:** To account for inference latency, we build on training-time real-time chunking (RTC) (Black et al., 2025), which conditions each prediction on the committed action prefix from the previous prediction. We propose a simple extension of training-time RTC that we term noisy-prefix RTC. During fine-tuning, we perturb the conditioning action prefix with Gaussian noise. At inference, we condition on clean committed commands.

**中文:** 为了考虑推理时延，我们以训练时实时分块（RTC）（Black et al., 2025）为基础，让每次预测都以上一次预测中已提交的动作前缀为条件。我们对训练时实时分块提出了一个简单的扩展，称之为含噪前缀 RTC（noisy-prefix RTC）。在微调阶段，我们用高斯噪声扰动条件动作前缀；推理时，则以干净的已提交指令作为条件。

<a id="S2088"></a>
**Source:** p.115 S2088

**Original:** Simulation experiments on training-time RTC schemes. We evaluate task performance and action smoothness for GR00T 2 under fixed simulated inference delays, comparing RTC-conditioned execution with naive asynchronous execution.

**中文:** 训练时 RTC 方案的仿真实验。我们在固定的仿真推理延迟下评测 GR00T 2 的任务性能与动作平滑性，并将 RTC 条件化执行与朴素异步执行进行比较。

<a id="S2089"></a>
**Source:** p.115 S2089

**Original:** A simple noisy-prefix RTC adaptation. We initialize from a GR00T 2 policy post-trained for 30k steps on RoboDojo (Chen et al., 2026a) demonstrations without RTC. Our proposed adaptation applies 5k additional fine-tuning steps on 800 demonstrations spanning eight precision tasks, adding Gaussian noise with 𝜎= 0.1 to the conditioning action prefix during training. This trains the policy to generate continuations from perturbed prefixes. We compare against clean-prefix training-time RTC, which uses no prefix noise during fine-tuning.

**中文:** 一个简单的含噪前缀 RTC 适配。我们从一个 GR00T 2 策略出发，该策略在未使用 RTC 的 RoboDojo（Chen et al., 2026a）演示数据上完成了 30k 步后训练。我们提出的适配方法在覆盖八个精细操作任务的 800 条演示上额外进行 5k 步微调，训练时对条件动作前缀加入 𝜎= 0.1 的高斯噪声 [公式原文见 p.115]。这使策略学会从受扰动的前缀生成后续动作。我们与干净前缀的训练时实时分块进行比较，后者在微调时不对前缀加噪。

![T028](assets/T028.png)

<a id="C088"></a>
**Source:** p.116 C088 · 表 T028

**Original (caption):** Table 28: Evaluation of a simple noisy-prefix RTC extension under simulated inference latency. Success and progress use 1,200 matched episodes per condition, while jerk uses 120 matched diagnostic layouts. Jerk changes are relative to async execution of the noisy-prefix fine-tuned checkpoint at the same delay. Negative changes indicate lower jerk. Bold values indicate the best result within each delay setting.

**中文（表注）：** Table 28：在仿真推理时延下对简单含噪前缀 RTC 扩展的评测。成功率与进度各使用每种条件下 1,200 个匹配回合，而加加速度（jerk）使用 120 个匹配诊断布局。jerk 的变化相对于同一延迟下含噪前缀微调检查点的异步执行计算。负值表示 jerk 更低。加粗数值表示每种延迟设置内的最佳结果。

<a id="S2095"></a>
**Source:** p.116 S2095

**Original:** Both variants use clean committed prefixes during RTC inference. The naive async reference uses the same noisy-prefix fine-tuned checkpoint as the noisy RTC method, with prefix conditioning disabled at inference.

**中文:** 两种变体在 RTC 推理时都使用干净的已提交前缀。朴素异步参照使用与含噪 RTC 方法相同的含噪前缀微调检查点，但推理时禁用前缀条件化。

<a id="S2096"></a>
**Source:** p.116 S2096

**Original:** Evaluation protocol. All conditions replan every eight commands at 25 Hz. Fixed delays of four and eight commands correspond to 160 ms and 320 ms, respectively. Delay is modeled through the action queue, without adding wall-clock sleeps to the simulator. Success rate and mean task progress are measured over 1,200 matched episodes per condition, comprising 150 layouts for each task. Jerk is measured in a separate diagnostic using 120 matched layouts per condition, with 15 layouts per task distributed across three layout banks.

**中文:** 评测协议。所有条件每 8 条指令以 25 Hz 重新规划一次。固定延迟 4 条与 8 条指令分别对应 160 ms 与 320 ms。延迟通过动作队列建模，不向仿真器添加挂钟睡眠。成功率（SR）与平均任务进度在每种条件的 1,200 个匹配回合上测量，其中每个任务包含 150 个布局。jerk 在单独的诊断中测量，每种条件使用 120 个匹配布局，每个任务 15 个布局，分布在三个布局库中。

<a id="S2097"></a>
**Source:** p.116 S2097

**Original:** We compute commanded joint jerk using third finite differences at ∆𝑡= 0.04 s, excluding grippers and startup. Cross-chunk jerk includes all three four-sample stencils crossing each old-to-new prediction handoff. The p95 statistic gives equal weight to each episode. Peak jerk is the largest observed absolute sample. At an eight-command delay, the prediction handoff coincides with the next replanning boundary.

**中文:** 我们在 ∆𝑡= 0.04 s 处使用三阶有限差分计算指令关节 jerk，并排除夹爪与启动阶段 [公式原文见 p.116]。跨块 jerk 包括穿过每个从旧预测到新预测交接点的全部三个四采样模板。p95 统计对每个回合赋予相同权重。峰值 jerk 为观测到的最大绝对采样值。在八条指令延迟下，预测交接恰好与下一次重新规划的边界重合。

<a id="S2098"></a>
**Source:** p.116 S2098

**Original:** Results. Table 28 reports performance and commanded-action smoothness relative to naive async execution. With identical noisy-prefix fine-tuned weights, RTC increases observed success from 32.83% to 34.75% at a four-command delay, while reducing p95 cross-chunk commanded jerk by 6.5% and peak jerk by 69.2%. At an eight-command delay, success increases from 15.00% to 21.42%, with reductions of 87.2% in p95 jerk and 22.5% in peak jerk.

**中文:** 结果。Table 28 报告了相对于朴素异步执行的性能与指令动作平滑性。在相同的含噪前缀微调权重下，四条指令延迟时 RTC 将观测成功率从 32.83% 提高到 34.75%，同时使 p95 跨块指令 jerk 降低 6.5%，峰值 jerk 降低 69.2%。八条指令延迟时，成功率从 15.00% 提高到 21.42%，p95 jerk 降低 87.2%，峰值 jerk 降低 22.5%。

<a id="S2099"></a>
**Source:** p.116 S2099

**Original:** Clean-prefix fine-tuning produces smoother commands at the four-command delay, but achieves lower task success than noisy-prefix fine-tuning. At the eight-command delay, the two RTC variants achieve the same observed success rate. The clean-prefix variant has lower p95 commanded jerk, whereas the noisy-prefix variant has lower peak commanded jerk. For simulated joint states at the eight-command delay, noisy RTC reduces p95 jerk by 40.1% but increases the observed peak by 13.4% relative to async execution.

**中文:** 干净前缀微调在四条指令延迟下产生更平滑的指令，但任务成功率低于含噪前缀微调。在八条指令延迟下，两种 RTC 变体取得相同的观测成功率。干净前缀变体的 p95 指令 jerk 更低，而含噪前缀变体的峰值指令 jerk 更低。对于八条指令延迟下的仿真关节状态，相对于异步执行，含噪 RTC 使 p95 jerk 降低 40.1%，但使观测峰值升高 13.4%。

### I.3. Accelerating Task Throughput Beyond Demonstrations ｜ 超越演示的任务吞吐加速

<a id="S2100"></a>
**Source:** p.116 S2100

**Original:** We leverage an agentic task-throughput acceleration algorithm to enable GR00T 2 to complete tasks with higher task-completion throughput than the demonstration dataset. We decompose overall task execution into semantically meaningful phases, such as reaching, grasping, transporting, and screwing, which differ in their sensitivity to acceleration. An agent searches for a speed schedule over these phases by evaluating accelerated rollouts and refining the speed schedule based on observed failures. At deployment, a lightweight observationconditioned future subtask predictor predicts a sequence of future phases aligned with GR00T 2’s action-chunk horizon. Given the action chunk, predicted phases and a speed schedule, a trajectory transformation function produces a new action chunk for execution (see Fig 20). We train the predictor using temporally aligned phase annotations generated by an agent.

**中文:** 我们采用一种智能体化任务吞吐加速算法，使 GR00T 2 能以高于演示数据集的任务完成吞吐量完成任务。我们将整体任务执行分解为语义上有意义的阶段，例如抵达、抓取、搬运和拧螺丝，这些阶段对加速的敏感程度各不相同。智能体通过评估加速后的 rollout（轨迹采样），并根据观测到的失败修正速度调度方案，在这些阶段上搜索速度调度方案。部署时，一个轻量的、以观测为条件的未来子任务预测器会预测一串未来阶段，并与 GR00T 2 的动作块时域对齐。给定动作块、预测阶段和速度调度方案后，轨迹变换函数会生成一个新的动作块用于执行（见 Fig 20）。我们使用由智能体生成的、时间对齐的阶段标注来训练该预测器。

<a id="S2101"></a>
**Source:** p.117 S2101

**Original:** Evaluation Tasks. We showcase GR00T 2-Accelerated across three tasks on the Tianji Sharpa robot from the Dexter post-training benchmark task (see Section A.1). We report task progress scores, success rates and mean completion times of successful episodes in Table 29. Our experiments indicate that GR00T 2-Accelerated consistently decreases task completion times while preserving success rates across the evaluated long-horizon dexterous tasks.

**中文:** 评测任务。我们在 Dexter 后训练基准任务（见 Section A.1）中的 Tianji Sharpa 机器人上，展示了 GR00T 2-Accelerated 在三个任务上的表现。Table 29 报告了任务进度分数、成功率以及成功回合的平均完成时间。我们的实验表明，在所评测的长时序灵巧任务上，GR00T 2-Accelerated 持续缩短任务完成时间，同时保持成功率。

![T029](assets/T029.png)

<a id="C089"></a>
**Source:** p.117 C089 · 表 T029

**Original (caption):** Table 29: Task success rate and completion time on Dexter post-training tasks. Completion time is averaged over successful trials only.

**中文（表注）：** Table 29：Dexter 后训练任务上的任务成功率与完成时间。完成时间仅对成功的试次取平均。

![F061](assets/F061.png)

<a id="C090"></a>
**Source:** p.118 C090 · 图 F061

**Original (caption):** Figure 61: Subset of environments for Real-to-Sim Evaluation. Side-by-side of real-world tasks that are used to evaluate generalist capabilities of GR00T 2 and their simulation counterparts. Odd columns are the simulation environments and even columns are frames from the real-world robot workcell. Each task is evaluated five times in the real-world and ten times in simulation per checkpoint, with the results used to calculate the correlations between performance in simulation and the real-world.

**中文（图注）：** Figure 61：用于现实到仿真评测的环境子集。并排展示了用于评测 GR00T 2 通用能力的真实世界任务及其仿真对应物。奇数列为仿真环境，偶数列为真实机器人工作单元中的帧画面。每个任务在每个检查点上于真实世界中评测五次、于仿真中评测十次，结果用于计算仿真表现与真实世界表现之间的相关性。

### J. Simulations ｜ 仿真

<a id="S2116"></a>
**Source:** p.118 S2116

**Original:** In this section, we outline how simulation contributed to GR00T 2. We developed a real-to-sim workflow that recreates high-fidelity digital twins of real-world tasks used for evaluating GR00T 2 (Sec. J.1). Policy evaluations in these high-fidelity digital twins proved to have strong correlations with real-world evaluations, allowing them to accelerate GR00T 2 development (Sec. J.2). Finally, we showcase GR00T 2’s capabilities on standardized simulation environments, establishing new state-of-the-art results on several of the latest benchmarks (Sec. J.3).

**中文:** 本节概述仿真如何服务于 GR00T 2 的研发。我们开发了一套现实到仿真（real-to-sim）工作流，用于重建 GR00T 2 评测所用真实世界任务的高保真数字孪生（Sec. J.1）。事实证明，在这些高保真数字孪生中进行的策略评测与真实世界评测之间具有很强的相关性，从而使它们能够加速 GR00T 2 的开发（Sec. J.2）。最后，我们在标准化仿真环境中展示了 GR00T 2 的能力，并在若干最新基准测试上取得了新的最优结果（Sec. J.3）。

### J.1. Real-to-Sim Generation of High-Fidelity Tasks ｜ 高保真任务的现实到仿真生成

<a id="S2117"></a>
**Source:** p.118 S2117

**Original:** J.1.1. GR00T 2 Simulation Task Suite

**中文:** J.1.1. GR00T 2 仿真任务套件

<a id="S2118"></a>
**Source:** p.118 S2118

**Original:** We seek to recreate the real-world tasks used in GR00T 2 development, including general manipulation tasks that are evaluated zero-shot and multi-stage assembly tasks. The task set spans rigid and articulated objects, deformable materials, and particles with diverse interactions including, but not limited to, sliding, pushing and scooping. We aim to reproduce both the visual setup and the physical interactions that determine whether each task succeeds, so that the resulting environments are useful for policy evaluation and skill development. This modeling can be challenging for tasks involving complex interactions with particles or deformables, since physics stability and fidelity must be maintained while running fast enough for large-scale evaluation. To enable this, we agentically integrate and tune different solvers such as the Finite Element Method (FEM) (Sifakis and Barbic, 2012) for deformable bodies, Position-Based Dynamics (PBD) (Müller et al., 2007) for granular media, in addition to rigid-body and articulation dynamics. Contact-rich assembly provides another demanding example of real-to-sim reconstruction. Parts must fit together, remain attached during manipulation, and interact with robot grippers and tools. We reconstruct toy plane, Hot Wheels, and toy tractor assembly assets with separate components, fasteners, and handheld drills (Fig. 62). Their initial and assembled configurations illustrate the component structure and geometric relationships that these environments must represent.

**中文:** 我们力图重现 GR00T 2 开发中使用的真实世界任务，包括以零样本方式评测的通用操作任务，以及多阶段装配任务。任务集合涵盖刚体与关节物体、可形变材料以及颗粒，并包含多种交互，包括但不限于滑动、推动和铲取。我们希望同时重现决定每个任务能否成功的视觉布置与物理交互，使所得环境既可用于策略评测，也可用于技能开发。对于涉及颗粒或可形变体复杂交互的任务，这种建模可能很有挑战性，因为必须在保持物理稳定性与保真度的同时，保证运行速度足以支持大规模评测。为此，我们以智能体化的方式集成并调节多种求解器，包括用于可形变体的有限元法（FEM）（Sifakis and Barbic, 2012）、用于颗粒介质的基于位置的动力学（PBD）（Müller et al., 2007），此外还包括刚体与关节动力学。富接触装配是现实到仿真重建的另一个高难度示例。零件必须能够相互配合，在操作过程中保持连接，并与机器人夹爪和工具发生相互作用。我们重建了玩具飞机、Hot Wheels 和玩具拖拉机的装配资产，包含各自独立的部件、紧固件以及手持电钻（Fig. 62）。它们的初始构型与装配后构型，展示了这些环境必须表示的部件结构与几何关系。

<a id="S2120"></a>
**Source:** p.119 S2120

**Original:** J.1.2. Agent-Guided Simulation Creation

**中文:** J.1.2. 智能体引导的仿真构建

<a id="S2121"></a>
**Source:** p.119 S2121

**Original:** We use complementary agent-assisted workflows to construct these environments. Tools from Sim- Foundry (Ranawaka et al., 2026) use real-world robot videos to guide scene reconstruction and refinement. We also use scans, photographs, and available physical measurements to reconstruct individual assets and their functional interfaces. Agents assist with geometry, appearance, collision modeling, and simulation setup, while human experts guide modeling decisions and review the resulting interactions.

**中文:** 我们采用互补的智能体辅助工作流来构建这些环境。Sim- Foundry（Ranawaka et al., 2026）中的工具利用真实世界机器人视频来引导场景重建与细化。我们还利用扫描数据、照片以及现有的物理测量，来重建单个资产及其功能接口。智能体协助处理几何、外观、碰撞建模与仿真设置，而人类专家负责指导建模决策，并审查最终的交互结果。

<a id="S2122"></a>
**Source:** p.119 S2122

**Original:** Visual reconstruction is paired with collision geometry tailored to the intended contacts. Fig. 63 illustrates this process for the tractor body, from the physical object and input scan to the reconstructed visual asset and its collision representations. Coarse handling geometry captures the overall shape, while detailed fitting geometry retains features such as bores and reconstructed threaded interfaces. The wheel-shaft close-ups show the two levels of detail: a simplified shape is sufficient for grasping and large-scale handling, whereas high-precision operations such as threading and insertion require the full fitting geometry.

**中文:** 视觉重建与为预期接触量身定制的碰撞几何相配对。Fig. 63 以拖拉机车身为例展示了这一过程，从实物、输入扫描到重建的视觉资产及其碰撞表示。粗略的操作几何捕捉整体形状，而精细的装配几何则保留了孔洞及重建的螺纹接口等特征。车轮轴近景展示了两个细节层次：简化形状足以用于抓取和大范围搬运，而螺纹连接与插入等高精度操作则需要完整的装配几何。

<a id="S2123"></a>
**Source:** p.119 S2123

**Original:** The toy plane and Hot Wheels assembly environments run in Isaac Lab Arena (NVIDIA Isaac Lab-Arena Contributors, 2025), using Newton (The Newton Contributors, 2025) with the MuJoCo Warp solver (Google DeepMind and NVIDIA, 2025). Each object has two sets of colliders: a coarse set for interactions such as grasping and contact with the worktable, and a detailed set for tight-fit insertion and threading bolts into nuts with a powered drill. We use convex and signed distance field (SDF) colliders for these representations. Collision masks determine which sets can interact, allowing larger-scale and fine-scale contacts to be simulated simultaneously. To support long-horizon, multi-stage assembly tasks, we developed an Isaac Lab extension for defining attachment points on individual parts. When a part reaches its intended assembly position within a predefined tolerance, the extension creates a joint between the corresponding rigid bodies, keeping the assembled parts connected during subsequent manipulation.

**中文:** 玩具飞机与 Hot Wheels 装配环境运行于 Isaac Lab Arena（NVIDIA Isaac Lab-Arena Contributors, 2025），使用 Newton（The Newton Contributors, 2025）以及 MuJoCo Warp 求解器（Google DeepMind and NVIDIA, 2025）。每个物体有两套碰撞体：粗略的一套用于抓取以及与工作台的接触等交互，精细的一套用于紧配合插入，以及用动力电钻将螺栓拧入螺母。我们对这些表示使用凸碰撞体和有向距离场（SDF）碰撞体。碰撞掩码决定哪些碰撞体集合可以相互作用，从而允许大尺度接触与精细尺度接触同时仿真。为支持长时序、多阶段装配任务，我们开发了一个 Isaac Lab 扩展，用于在单个零件上定义附着点。当某个零件在预定义容差范围内到达其预期装配位置时，该扩展会在对应的刚体之间创建一个关节，从而在后续操作中保持已装配零件的连接。

<a id="S2124"></a>
**Source:** p.119 S2124

**Original:** We validate the environments and assets in several stages. First, we test assembly without a robot, applying forces directly to the parts and the drill. These tests follow the real-world sequence of inserting parts and driving bolts. We also perform grasping and drop tests to check the stability of individual assets and the overall scene. Finally, we replay real-world robot demonstrations in simulation (Fig. 64) to assess asset stability and interactions such as grasping, insertion, and fastening. The validated environments then support the GR00T 2 applications described in Sec. J.2.

**中文:** 我们分几个阶段验证环境与资产。首先，在没有机器人的情况下测试装配，直接对零件和电钻施加力，这些测试遵循真实世界中插入零件与拧紧螺栓的顺序。我们还进行抓取与跌落测试，以检查单个资产以及整个场景的稳定性。最后，我们在仿真中重放真实世界的机器人演示（Fig. 64），以评估资产稳定性以及抓取、插入和紧固等交互。经过验证的环境随后支持 Sec. J.2 中所述的 GR00T 2 应用。
