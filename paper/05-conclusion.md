# 第 5 章 结论与开放问题

> **原文** 5. Conclusion and Open Problems　·　起于 p.26　·　本页中英对照：英文段在前，中文段在后。

---
<a id="S469"></a>

<!-- p.26 S469 -->

GR00T 2 is a world-action model: a single 2B-parameter transformer that predicts future observations and robot actions together, pretrained on egocentric human video, handheld UMI demonstrations, and teleoperation of gripper arms, dexterous hands, and a humanoid. Predicting the future gives all of these sources a common objective, including human video that carries no robot actions. On 50 dexterous tasks new to the robot, the resulting model succeeds zero-shot in 40% of trials and reaches 95% with five demonstrations (Sec. 3.1). It learns robot tasks without teleoperated demonstrations of those tasks (Sec. 3.2). Real-world RL raises its success on contact-rich skills to 88 to 98% (Sec. 3.3). With corrective data and a frontier agent, it completes cluttered long-horizon assemblies in at least 97% of trials (Sec. 3.4). GR00T 2 Turbo runs onboard a humanoid and directs a learned whole-body controller (Sec. 3.5).

GR00T 2 是一个世界-动作模型（WAM）：一个 20 亿参数的单一 Transformer，它同时预测未来观测与机器人动作，并在第一人称视角（egocentric）人类视频、手持 UMI 演示数据，以及夹爪机械臂、灵巧手和人形机器人的遥操作数据上完成预训练。预测未来为所有这些数据源提供了统一的目标，其中也包括不含机器人动作的人类视频。在 50 项对该机器人而言属于新任务的灵巧操作任务上，模型零样本成功率为 40%，使用五条演示后达到 95%（Sec. 3.1）。它无需该任务的遥操作演示即可学习机器人任务（Sec. 3.2）。真实世界强化学习（RL）将其在富接触技能上的成功率提升至 88% 至 98%（Sec. 3.3）。借助纠正性数据和前沿智能体，它能在杂乱的长时序装配任务中至少完成 97% 的试次（Sec. 3.4）。GR00T 2 Turbo 运行于机载人形机器人之上，并驱动一个习得的全身控制器（Sec. 3.5）。

<a id="S470"></a>

<!-- p.26 S470 -->

Three observations from building GR00T 2 shape the problems that follow.

构建 GR00T 2 的过程中有三点观察，它们决定了下文讨论的问题。

<a id="S471"></a>

<!-- p.26 S471 -->

• Much of what the robot learns need not come from robot data. Robot success on new tasks more than doubles with human video in pretraining and does not level off at the largest scale we tested (Fig. 10). For glove and Gripper UMI demonstrations, task-agnostic data from the target robot specify the embodiment, while the demonstrations specify the task (Sec. 3.2). • Reliability comes from complementary mechanisms, not from pretraining alone. Pretraining provides breadth. Corrective demonstrations and RL close gaps in precision and contact. The agent supplies memory, verification, and recovery over long horizons. • Progress depended on measurement. Blinded head-to-head evaluation and calibrated simulation (Sec. 4.3 and 4.5.2) turned close comparisons into decisions.

• 机器人学到的许多东西不必来自机器人数据。在预训练中加入人类视频后，机器人在新任务上的成功率增长超过一倍，并且在我们测试的最大规模下仍未趋于平缓（图 10）。对于手套式与 Gripper UMI 演示数据，来自目标机器人的任务无关数据界定本体，而演示数据界定任务（Sec. 3.2）。• 可靠性来自互补机制，而不仅仅来自预训练。预训练提供广度，纠正性演示与强化学习则弥补精度和接触方面的差距。智能体负责长时序任务中的记忆、验证与恢复。• 进展依赖于测量。盲法的两两直接评测与经过校准的仿真（Sec. 4.3 和 4.5.2）把接近的比较变成了明确的结论。

<a id="S472"></a>

<!-- p.26 S472 -->

Each observation also points to problems that remain open. We group them by part of the robot learning system, and start each group from the basic constraint that makes it hard.

每一条观察也指向仍然开放的问题。我们按机器人学习系统的组成部分对这些问题分组，并从使每组问题变得困难的基本约束出发展开讨论。

<a id="S473"></a>

<!-- p.26 S473 -->

Model. A robot policy learns from data dominated by observation rather than action, and it must act at the rate of the physical world. Joint video-action prediction turns every video into supervision, but most of the tokens it predicts encode future video, much of which does not bear on the next action. GR00T 2 Turbo predicts a spatial latent grid four times smaller than that of GR00T 2. After post-training, it loses 6.7 points of success on YAM but half of its success on dexterous tasks, falling from 68.6% to 34.3% (Tab. 1). The comparison does not isolate the cause, but it suggests that the visual detail a policy must predict depends on the task and the embodiment. Four questions follow.

模型。机器人策略从以观测为主而非以动作为主的数据中学习，并且必须以物理世界的速率行动。联合的视频-动作预测把每一段视频都变成了监督信号，但它所预测的 token 大多编码未来视频，其中许多与下一步动作无关。GR00T 2 Turbo 所预测的空间潜变量网格，比 GR00T 2 的小四倍。经过后训练后，它在 YAM 上的成功率下降 6.7 个百分点，而在灵巧任务上的成功率则下降了一半，从 68.6% 降至 34.3%（Tab. 1）。该比较并未分离出原因，但它表明策略必须预测的视觉细节取决于任务与本体。由此引出四个问题。

<a id="S474"></a>

<!-- p.26 S474 -->

• What to predict. It is unknown which aspects of the future a policy should predict, and at what resolution and horizon. It is also unclear whether prediction helps mainly as a training signal or also as imagination at inference time. • Memory. GR00T 2 observes 0.8 s of history, and tasks that require memory are delegated to the agent (Sec. 3.4). In imitation learning, longer raw context can invite shortcuts such as copying past ac- tions (de Haan et al., 2019; Wen et al., 2020), which suggests that memory should be structured rather than simply longer. • Force and touch. GR00T 2 handles force only as an output: from DexUMI demonstrations, it predicts joint torques that set the hand’s compliance (Sec. 4.4.3). It does not take touch as input, and tactile recordings are scarce compared with video. How to add force and touch as inputs without eroding visual priors, and at which control rate, is open. • Interfaces in the control hierarchy. Image-space points tell GR00T 2 where to act but not how, so requirements such as pouring or scooping still rest on language and learned skills (Sec. 3.4). Below GR00T 2 Turbo, the interface to SONIC is a motion latent decoded into joint position targets (Sec. 3.5), so contact force is not represented explicitly. Which representation should pass between reasoning, policy, and controller, and how it transfers to new embodiments, is unsettled.

• 预测什么。目前尚不清楚策略应预测未来的哪些方面，以及应以何种分辨率和时间跨度进行预测。同样不清楚的是，预测主要是作为训练信号起作用，还是在推理时也起到“想象”的作用。• 记忆。GR00T 2 只观察 0.8 秒的历史，需要记忆的任务则交由智能体处理（Sec. 3.4）。在模仿学习中，更长的原始上下文可能诱发捷径，例如复制过去的动作（de Haan et al., 2019; Wen et al., 2020），这表明记忆应当是结构化的，而不只是简单地加长。• 力与触觉。GR00T 2 仅把力当作输出处理：利用 DexUMI 演示数据，它预测用于设定手部柔顺性（compliance）的关节力矩（Sec. 4.4.3）。它不接收触觉作为输入，而且与视频相比，触觉记录十分稀少。如何在不损害视觉先验的前提下把力和触觉作为输入加入，以及以何种控制频率加入，仍是开放问题。• 控制层级中的接口。图像空间中的点告诉 GR00T 2 去哪里行动，却没有告诉它如何行动，因此倒酒或舀取等要求仍然依赖语言和习得的技能（Sec. 3.4）。在 GR00T 2 Turbo 之下，与 SONIC 的接口是一个被解码为关节位置目标的运动潜变量（Sec. 3.5），因此接触力没有被显式表示。在推理、策略与控制器之间应传递何种表示，以及这种表示如何迁移到新本体，目前尚无定论。

<a id="S477"></a>

<!-- p.27 S477 -->

Data. Every hour of robot data requires a robot and an operator, whereas human experience is abundant but recorded in a different body. GR00T 2 pretrains on about 400,000 hours of human video, 10,000 hours of UMI demonstrations, and 23,500 hours of teleoperation (Sec. 4.2). Human video brings coverage, UMI brings task-focused demonstrations in a robot-compatible format, and teleoperation grounds the embodiment.

数据。每一小时的机器人数据都需要一台机器人和一名操作员，而人类经验十分丰富，只是记录在另一种身体之中。GR00T 2 在约 400,000 小时的人类视频、10,000 小时的 UMI 演示数据和 23,500 小时的遥操作数据上进行预训练（Sec. 4.2）。人类视频带来覆盖面，UMI 以机器人兼容的格式提供聚焦任务的演示数据，遥操作则把模型锚定到本体上。

<a id="S478"></a>

<!-- p.27 S478 -->

What is missing is an exchange rate between these sources. It is not known how much robot performance an hour of each source yields, or how that yield changes with the data already present. It is also not known how little target-robot data suffices to specify a new embodiment. Simulation raises the same question. Compute widens coverage, but agreement with the real world still requires measurement and robot time. The scaling with human video shows only that one of these rates is positive (Fig. 10). Until they are measured, collection budgets cannot be allocated on principle.

目前缺失的是这些数据源之间的“兑换率”。我们不知道每一小时的各类数据能带来多少机器人性能，也不知道这种产出如何随已有数据的多少而变化。我们同样不知道，至少需要多少目标机器人数据才能界定一种新本体。仿真也提出了同样的问题。算力能扩大覆盖范围，但要与真实世界保持一致，仍然需要测量和机器人时间。与人类视频相关的缩放结果只表明，其中一种兑换率为正（图 10）。在这些兑换率被测量之前，采集预算无法有原则地分配。

<a id="S479"></a>

<!-- p.27 S479 -->

A second question is what makes data useful beyond its quantity. Demonstrations show mostly successful behavior, whereas RL, world models, and verifiers also need failures and recoveries; the world model we use for RL is trained on robot episodes that include both (Sec. 4.5.3). Labels of how well each demonstration was executed could serve as a further training signal.

第二个问题是：除了数量之外，是什么让数据变得有用。演示数据主要展示成功的行为，而强化学习、世界模型和验证器还需要失败与恢复的样本；我们用于强化学习的世界模型，正是在同时包含两者的机器人片段上训练的（Sec. 4.5.3）。记录每条演示执行质量的标签，还可以作为另一种训练信号。

<a id="S480"></a>

<!-- p.27 S480 -->

Evaluation. A success rate measured on real robots is a binomial estimate, and its uncertainty shrinks only with the square root of the number of trials. Our post-training benchmarks use up to 20 trials per task (Tab. 1). That is enough to resolve the large gaps between GR00T 2 and its baselines, but not the differences that matter in deployment. Distinguishing 95% from 99% success takes about 285 trials per policy, and 99% from 99.9% more than 1,000.1 Absolute rates also drift with station, operator, and day, which is why we rank checkpoints by blinded head-to-head comparisons (Sec. 4.3). Even then, the independent units are tasks rather than trials, and 30 to 35% of comparisons are ties (Sec. D.7). Three directions follow.

评测。在真实机器人上测得的成功率是一个二项估计，其不确定性只按试次数平方根的速度缩小。我们的后训练基准每个任务最多使用 20 次试次（Tab. 1）。这足以分辨 GR00T 2 与其基线之间的大幅差距，但不足以分辨部署中真正重要的差异。要区分 95% 与 99% 的成功率，每个策略大约需要 285 次试次；要区分 99% 与 99.9%，则需要超过 1,000¹ 次。绝对成功率还会随工位、操作员和日期而漂移，这正是我们通过盲法两两直接比较来对检查点排序的原因（Sec. 4.3）。即便如此，独立单元是任务而非试次，而且 30% 至 35% 的比较结果是平局（Sec. D.7）。由此引出三个方向。

<a id="S481"></a>

<!-- p.27 S481 -->

• Proxy evaluation at deployment scale. Across 25 YAM tasks, simulation predicts the real-robot task progress of 14 generalist checkpoints with a Pearson correlation of 0.93 (Sec. 4.5.2). It remains to be shown whether simulation is as predictive for contact-rich assembly, for RL-trained policies that exploit simulator errors, and for comparisons between training recipes rather than checkpoints. • Automated verification. In our long-horizon assemblies, three of the eight failures were screws left partly driven that both GR00T 2 and the agent judged complete (Sec. G.1). Verifying subtle physical state is a prerequisite for autonomous evaluation, for RL rewards, and for deciding when to ask a person for help. • Cost to reliability. Robot learning rarely reports the quantity that determines deployment: the robot time and human time needed to bring a new task to a target reliability. The same accounting, under matched budgets, would settle when RL is worth more than additional demonstrations or corrections.

• 部署规模下的代理评测。在 25 个 YAM 任务上，仿真对 14 个通用检查点的真实机器人任务进度的预测，其皮尔逊相关系数（Pearson correlation）为 0.93（Sec. 4.5.2）。仍需证明的是：对于富接触装配、利用仿真器误差的强化学习策略，以及训练配方（而非检查点）之间的比较，仿真是否同样具有预测性。• 自动验证。在我们的长时序装配任务中，八次失败里有三次是螺丝拧入不完全，而 GR00T 2 与智能体都判定其已完成（Sec. G.1）。验证细微的物理状态，是自主评测、强化学习奖励以及判断何时向人求助的前提。• 成本与可靠性。机器人学习很少报告决定部署的那个量：把一项新任务提升到目标可靠性所需的机器人时间和人力时间。在预算匹配的条件下进行同样的核算，就能确定何时强化学习比额外的演示或纠正更有价值。

<a id="S482"></a>

<!-- p.27 S482 -->

Hardware. A model can learn only what the hardware allows people to demonstrate, sensors to record, and robots to repeat. Our teleoperation cannot demonstrate fast, targeted motions such as the conveyor toss, which GR00T 2 learned from human demonstrations instead (Sec. 3.2). Capture devices that match the robot shrink the gap the model must bridge. DexUMI replicates the joints and contact surfaces of the robot hand, so on that hand its demonstrations need no robot play data (Sec. 4.4). This argues for designing robots and capture devices together, with shared kinematics, camera placement, and tactile formats.

硬件。模型只能学会硬件允许人们演示、传感器记录、机器人复现的内容。我们的遥操作无法演示传送带投掷这类快速、定向的动作，而 GR00T 2 是从人类演示中学会这一动作的（Sec. 3.2）。与机器人相匹配的采集设备可以缩小模型必须跨越的差距。DexUMI 复刻了机器人手的关节与接触面，因此在该手上，其演示数据无需机器人自由操作数据（robot play data）（Sec. 4.4）。这说明应当把机器人与采集设备一并设计，并共享运动学、相机布置和触觉格式。

<a id="S483"></a>

<!-- p.27 S483 -->

1Two-sided two-proportion 𝑧-test at significance level 0.05 with 80% power.

1 双侧双比例 𝑧 检验，显著性水平 0.05，检验效能 80%。

<a id="S484"></a>

<!-- p.28 S484 -->

Learning from interaction makes further demands. Physical interaction and scene resets limit how fast realworld RL collects experience (Sec. F.3), so autonomous improvement needs stations that reset themselves, detect success, and withstand thousands of contact-rich attempts. Onboard compute and power, finally, bound the model itself: GR00T 2 Turbo exists because a humanoid must run its policy on an edge GPU (Sec. 2).

从交互中学习还会带来更多要求。物理交互与场景复位限制了真实世界强化学习收集经验的速度（Sec. F.3），因此自主改进需要能够自行复位、检测成功，并能承受数千次富接触尝试的工位。最后，机载算力与功耗限制了模型本身：GR00T 2 Turbo 之所以存在，是因为人形机器人必须在边缘 GPU 上运行其策略（Sec. 2）。

<a id="S485"></a>

<!-- p.28 S485 -->

Infrastructure. Joint video-action training processes multi-camera video at every step, and video dominates the cost of storage, decoding, and computation. Pretraining GR00T 2 used 1,024 GB300 GPUs and a data pipeline that processes petabyte-scale input each month (Sec. 4.7). It is not yet known how world-action models scale with model size, data, and compute, or how compute should be divided between video and action prediction. Scaling laws of this kind, under the constraint that the deployed model must run in real time, would guide the design of the next model.

基础设施。联合视频-动作训练在每一步都要处理多路相机视频，而视频在存储、解码和计算成本中占主导地位。预训练 GR00T 2 使用了 1,024 块 GB300 GPU，以及一条每月处理 PB 级输入的数据流水线（Sec. 4.7）。目前尚不清楚世界-动作模型如何随模型规模、数据和算力而扩展，也不清楚算力应如何在视频预测与动作预测之间分配。在部署模型必须实时运行的约束下，这类缩放定律（scaling laws）将指导下一代模型的设计。

<a id="S486"></a>

<!-- p.28 S486 -->

The larger shift is from offline to online learning. RL post-training already couples robots, training, and evaluation in one service that retains experience across interruptions (Sec. F.3). An agent found the basis of our RL recipe through about 35 days of autonomous experimentation in simulation (Sec. 4.1). Extending this loop from single stations to fleets requires infrastructure in which robot experience, simulation, and world-model rollouts feed training continuously while every model and dataset version stays reproducible.

更大的转变是从离线学习走向在线学习。强化学习后训练已经把机器人、训练和评测耦合在同一项服务中，并且能在中断之后保留经验（Sec. F.3）。一个智能体通过约 35 天的仿真自主实验，找到了我们强化学习方案的基础（Sec. 4.1）。要把这一闭环从单个工位扩展到机器人集群，需要这样一种基础设施：机器人经验、仿真以及世界模型的 rollout（轨迹采样）持续地输入训练，同时每个模型与数据集版本都保持可复现。

<a id="S487"></a>

<!-- p.28 S487 -->

Deployment. The value of a deployed robot is set by how often it needs a person, how fast it works, and whether it is safe. GR00T 2 predicts an action chunk for Dexter in 153 ms on a GeForce RTX 5090 workstation GPU, and GR00T 2 Turbo predicts one for the G1 humanoid in 124 ms on its onboard Jetson Thor (median prediction latency, Sec. 2 and Tab. 27). Phase-conditioned retiming shortens mean completion time by 15 to 26% on three dexterous tasks (Tab. 29). Reliability is less settled. On long-horizon tasks, post-training reaches about 70% average success (Tab. 1). From cluttered starts, assembly success of at least 97% required corrective data and an agent that monitors and repairs (Sec. 3.4). That agent is slow relative to the policy. In visually steered trash sorting on YAM, a median agent turn takes 7.5 s against about 0.6 s per unaccelerated policy call, and the robot waits for the agent during a median 38% of an episode (Sec. G.2). Three problems stand out.

部署。已部署机器人的价值，取决于它需要人工介入的频率、工作速度以及是否安全。GR00T 2 在 GeForce RTX 5090 工作站 GPU 上为 Dexter 预测一个动作块，耗时 153 毫秒；GR00T 2 Turbo 则在其机载 Jetson Thor 上为 G1 人形机器人预测动作块，耗时 124 毫秒（预测延迟中位数，见 Sec. 2 与 Tab. 27）。相位条件重定时（phase-conditioned retiming）在三项灵巧任务上使平均完成时间缩短 15% 至 26%（Tab. 29）。可靠性方面则尚未定论。在长时序任务上，后训练的平均成功率约为 70%（Tab. 1）。从杂乱的初始状态开始，要达到至少 97% 的装配成功率，需要纠正数据以及一个能够监控并修复问题的智能体（Sec. 3.4）。该智能体相对于策略而言速度较慢。在 YAM 上进行视觉引导（visual steering）的垃圾分拣时，智能体单轮中位耗时 7.5 秒，而未经加速的单次策略调用约需 0.6 秒；机器人在一个回合中位数 38% 的时间里都在等待智能体（Sec. G.2）。有三个问题尤为突出。

<a id="S488"></a>

<!-- p.28 S488 -->

• Routine improvement. RL and world-model training still require rollouts and adaptation for each task (Sec. 4.5.3). A loop in which deployment exposes failures, agents propose corrections, and successful behaviors are distilled back into the policy (Sec. G.3) would turn this per-task cost into a by-product of operation. • Latency across the hierarchy. Reasoning, verification, and recovery must move closer to the policy’s control rate, through faster agents, distilled verifiers, or a policy that absorbs recurring corrections. • Safe physical action. Safety training of language models constrains what they say, and it is not known to carry over to what a robot does. A policy that agents can steer needs its own checks on the physical consequences of each action, at the rate at which actions execute.

• 常规改进。强化学习和世界模型训练仍然需要针对每项任务进行 rollout 和适配（Sec. 4.5.3）。一个循环若能让部署暴露失败、让智能体提出纠正、再把成功的行为蒸馏回策略中（Sec. G.3），就能把这种逐任务的成本变成运行过程的副产品。• 层级之间的延迟。推理、验证与恢复必须更贴近策略的控制频率，途径包括更快的智能体、蒸馏得到的验证器，或能够吸收反复出现的纠正的策略。• 安全的物理动作。语言模型的安全训练约束的是它们说什么，而并不知道这种约束能否延伸到机器人做什么。可由智能体操控的策略，需要以动作执行的速率，对每个动作的物理后果进行自身的检查。

<a id="S490"></a>

<!-- p.28 S490 -->

GR00T 2 shows that one model, pretrained to predict how the physical world unfolds, can learn from human experience, transfer skills across embodiments, and serve as the manipulation layer of an agentic system. The open problems above share one structure. Each asks how to turn a scarce resource, whether robot hours, human time, or onboard compute, into reliable physical capability, and how to measure the result with enough confidence to act on it.

GR00T 2 表明，一个以预测物理世界如何演化为目标进行预训练的单一模型，能够从人类经验中学习、跨本体迁移技能，并充当智能体化系统的操作层。上述开放问题具有共同的结构。每一个问题都在追问：如何把稀缺资源（无论是机器人时长、人类时间还是机载算力）转化为可靠的物理能力，以及如何以足够的把握测量结果，从而据此行动。
