### 1. Introduction ｜ 引言

<a id="S021"></a>
**Source:** p.3 S021

**Original:** Building general-purpose robots requires models that can acquire diverse physical skills, generalize across tasks and embodiments, and adapt efficiently to new environments and objectives. Recent advances in vision-language-action (VLA) models have demonstrated the potential of large-scale pretraining for robotic manipulation. However, scaling robot intelligence involves challenges beyond learning from increasingly large demonstration datasets. A general-purpose robot foundation model must learn from heterogeneous sources of physical experience, acquire new capabilities with limited task-specific supervision, improve through interaction, and support reliable, responsive execution in complex robotic systems. Furthermore, as robots become increasingly autonomous, their learned physical capabilities must be accessible to higher-level reasoning and planning systems. Meeting these requirements calls for models that capture not only how robots act, but also how their actions change the physical world.

**中文:** 构建通用机器人需要这样的模型：它能够习得多样的物理技能，在任务与本体之间泛化，并高效适应新环境和新目标。视觉-语言-动作（VLA）模型的最新进展已经证明，大规模预训练在机器人操作中具有潜力。然而，扩展机器人智能所面临的挑战，不止于从规模越来越大的演示数据集中学习。通用机器人基础模型必须从异构的物理经验来源中学习，在有限的任务特定监督下获得新能力，通过交互持续改进，并在复杂的机器人系统中支持可靠且响应迅速的执行。此外，随着机器人日益自主，它们习得的物理能力必须能够被更高层的推理与规划系统调用。满足这些要求，需要的模型不仅要刻画机器人如何行动，还要刻画其动作如何改变物理世界。

<a id="S022"></a>
**Source:** p.3 S022

**Original:** We introduce GR00T 2, a new generation of foundation world-action models (WAMs). GR00T 2 jointly predicts future visual observations and embodied actions, learning how physical interactions unfold alongside the actions that produce them. Through large-scale pretraining on diverse human and robot experience, GR00T 2 develops general-purpose manipulation capabilities across both parallel-gripper robots and dexterous hands. We demonstrate four major advances. First, GR00T 2 delivers strong out-of-the-box performance across diverse manipulation tasks and embodiments. Second, its pretrained capabilities enable rapid adaptation to challenging new tasks from remarkably few demonstrations, while reinforcement learning (RL) further improves manipulation reliability through real-world interaction. Third, GR00T 2 enables x-adaptation (cross adaptation), allowing physical knowledge acquired from one embodiment to be transferred to another through joint prediction of future observations and actions. Finally, GR00T 2 supports agentic control through two complementary capabilities: skill composition and recovery with code-as-policy (CaP), enabling higher-level agents to orchestrate manipulation and recover from execution failures, and steerable world-action generation through a WAM API, allowing agents to guide and compose robot behaviors using visual targets.

**中文:** 我们推出 GR00T 2，这是新一代基础世界-动作模型（WAM）。GR00T 2 联合预测未来的视觉观测与具身动作，学习物理交互如何与产生它们的动作一同展开。通过在多样的人类与机器人经验上进行大规模预训练，GR00T 2 在平行夹爪机器人和灵巧手两类本体上都发展出了通用的操作能力。我们展示了四项主要进展。第一，GR00T 2 在多样的操作任务和本体上提供了强大的开箱即用性能。第二，其预训练得到的能力使其能够仅凭极少量演示快速适应具有挑战性的新任务，同时强化学习（RL）通过真实世界交互进一步提升操作可靠性。第三，GR00T 2 实现了跨本体适配（x-adapt，cross adaptation），通过对未来观测和动作的联合预测，使从一个本体习得的物理知识能够迁移到另一个本体。最后，GR00T 2 通过两种互补能力支持智能体化控制：一是借助代码即策略（code-as-policy, CaP）实现的技能组合与恢复，使更高层的智能体能够编排操作并从执行故障中恢复；二是通过 WAM API 实现的可引导的世界-动作生成，使智能体能够利用视觉目标引导并组合机器人行为。

<a id="S023"></a>
**Source:** p.3 S023

**Original:** Emergence of X-Adaptability. A central innovation of GR00T 2 is its cross-adaptation (x-adapt) capability, which allows the model to generalize to task-scene-embodiment combinations unseen during training. Consider a manipulation task observed only in human demonstrations and a robot embodiment represented by data from an entirely different set of tasks. Through joint world-action pretraining, GR00T 2 learns to imagine how the task would unfold when performed by the target robot and to generate actions corresponding to that imagined interaction. This creates a mechanism for transferring physical knowledge across heterogeneous sources of experience, including UMI demonstrations, dexterous UMI data, human hand interactions, and robot embodiments with substantially different kinematics. We explore this capability through cross-embodiment transfer experiments and a zero-teleoperation dexterous learning system, demonstrating the potential to acquire robot skills directly from human experience without collecting task-specific robot demonstrations. More broadly, cross-embodiment imagination points toward a new scaling property of robot foundation models: physical behaviors learned during pretraining can become executable capabilities across embodiments.

**中文:** X-Adaptability 的涌现。GR00T 2 的核心创新之一是其跨本体适配（x-adapt）能力，该能力使模型能够泛化到训练中未见过的任务-场景-本体组合。设想一个只在人类演示中出现过的操作任务，以及一个由另一组完全不同任务的数据所表征的机器人本体。通过联合的世界-动作预训练，GR00T 2 学会想象目标机器人执行该任务时事情会如何展开，并生成与这一想象中的交互相对应的动作。这就形成了一种机制，能够在异构的经验来源之间迁移物理知识，这些来源包括 UMI 演示、灵巧 UMI 数据、人手交互，以及运动学差异显著的机器人本体。我们通过跨本体迁移实验和零遥操作灵巧学习系统来探索这一能力，展示了无需收集任务特定的机器人演示、直接从人类经验中习得机器人技能的潜力。更广泛地说，跨本体想象指向机器人基础模型的一种新的扩展特性：预训练期间习得的物理行为，可以转化为跨本体可执行的能力。

<a id="S024"></a>
**Source:** p.3 S024

**Original:** Fast Adaptation and Agentic Control. GR00T 2 advances the capabilities of pretrained robot policies across generalization, dexterity, and adaptation. A diverse pretraining mixture equips the model with a broad repertoire of physical behaviors, enabling strong out-of-the-box performance and rapid acquisition of challenging new skills from few demonstrations. We further extend these capabilities through RL to improve manipulation reliability and efficient inference for responsive, closed-loop control. Building on these learned skills, we integrate GR00T 2 with higher-level reasoning agents that use CaP to compose manipulation skills, monitor execution, and recover from unexpected failures, bringing GR00T 2 closer to deployment-level reliability on challenging long-horizon manipulation tasks. Beyond skill composition and recovery, GR00T 2’s joint world-action representation provides a natural interface for steering robot behavior through desired visual outcomes and intermediate future states. We develop a WAM API that exposes this capability to higher-level agents, allowing them to guide and compose robot behaviors through visual targets. Together, these capabilities

**中文:** 快速适应与智能体化控制。GR00T 2 提升了预训练机器人策略在泛化、灵巧性与适应性方面的能力。多样的预训练混合数据使模型具备广泛的物理行为库，从而实现强大的开箱即用性能，并能够仅凭少量演示快速习得具有挑战性的新技能。我们进一步通过强化学习扩展这些能力，以提升操作可靠性，并实现高效推理，支持响应迅速的闭环控制。基于这些习得的技能，我们将 GR00T 2 与更高层的推理智能体集成，这些智能体使用 CaP 来组合操作技能、监控执行过程，并从意外故障中恢复，从而使 GR00T 2 在具有挑战性的长时序操作任务上更接近部署级别的可靠性。除了技能组合与恢复之外，GR00T 2 的联合世界-动作表征还为通过期望的视觉结果和中间未来状态引导机器人行为提供了一种自然接口。我们开发了一个 WAM API，将这一能力开放给更高层的智能体，使其能够通过视觉目标引导并组合机器人行为。综上，这些能力 [存疑：原文在此处截断，未以句号结束]

![F001](assets/F001.png)

<a id="C001"></a>
**Source:** p.4 C001 · 图 F001

**Original (caption):** Figure 1: We introduce GR00T 2, a world-action model for general-purpose robots. Top: GR00T 2 pretrains on human and robot data. Second row: given a language goal, multi-view video from the egocentric and both wrist cameras, and the robot state, GR00T 2 jointly predicts multi-view future video and robot actions. Third row: with X-Adapt, GR00T 2 learns a new robot skill from sensorized human demonstrations (Human →Dexter, a Tianji robot with Sharpa hands), from handheld and wearable capture devices (UMI →YAM, DexUMI →XHAND, and DexUMI →Dexter), and through simulation, either from a single human video (Human video →Dexter) or by replaying teleoperated G1 motions across varied simulated scenes (G1 real →sim →real). Bottom: RL post-training on real robots and in a world model improves GR00T 2 beyond its demonstrations (left), a frontier agent runs and steers GR00T 2 (center), and GR00T 2 Turbo directs the SONIC whole-body controller for humanoid loco-manipulation (right).

**中文（图注）：** 图注：我们推出 GR00T 2，这是一种面向通用机器人的世界-动作模型。顶部：GR00T 2 基于人类数据和机器人数据进行预训练。第二行：给定语言目标，以及来自第一人称视角（egocentric）相机和双腕部相机的多视角视频与机器人状态，GR00T 2 联合预测多视角未来视频和机器人动作。第三行：借助 X-Adapt，GR00T 2 能够从带传感器的人类演示（Human →Dexter，搭载 Sharpa 手的 Tianji 机器人）、手持与可穿戴采集设备（UMI →YAM、DexUMI →XHAND 和 DexUMI →Dexter），以及仿真中习得新的机器人技能：既可以从单段人类视频（Human video →Dexter）中学习，也可以通过在多样的仿真场景中回放遥操作得到的 G1 动作来学习（G1 real →sim →real）。底部：在真实机器人上以及世界模型中进行的强化学习后训练，使 GR00T 2 超越其演示（左）；一个前沿智能体运行并引导 GR00T 2（中）；GR00T 2 Turbo 为人形机器人的移动操作指挥 SONIC 全身控制器（右）。

<a id="S053"></a>
**Source:** p.4 S053

**Original:** create a path toward agentic robotic systems in which high-level reasoning and planning can directly leverage the physical intelligence acquired through world-action pretraining.

**中文:** 开辟一条通往智能体化机器人系统的路径，在这类系统中，高层推理与规划能够直接利用通过世界-动作预训练获得的物理智能。

<a id="S054"></a>
**Source:** p.4 S054

**Original:** GR00T 2 Turbo: Token-Efficient World Modeling. We also introduce GR00T 2 Turbo, a lightweight variant of GR00T 2 designed for efficient world-action modeling. Joint video-action prediction enables actions to benefit from learned visual dynamics, but processing video tokens can be costly, particularly for multi-view, low-latency control. GR00T 2 Turbo addresses this cost with a more compact video representation while retaining the joint world-action modeling framework. This design enables faster training and inference, making GR00T 2 Turbo well suited for whole-body control while remaining well above the baselines on bimanual and dexterous manipulation tasks.

**中文:** GR00T 2 Turbo：token 高效的世界建模。我们还推出了 GR00T 2 Turbo，这是为高效世界-动作建模设计的 GR00T 2 轻量级变体。联合的视频-动作预测使动作能够受益于习得的视觉动力学，但处理视频 token 的代价可能很高，在多视角、低时延控制场景中尤其如此。GR00T 2 Turbo 通过更紧凑的视频表示来应对这一开销，同时保留联合世界-动作建模框架。这一设计使训练和推理更快，因此 GR00T 2 Turbo 非常适合全身控制，同时在双臂和灵巧操作任务上仍显著高于基线。

<a id="S056"></a>
**Source:** p.5 S056

**Original:** Realizing these advances requires innovations throughout the robot learning stack. We first describe the GR00T 2 architecture and pretraining framework, including Human-1M, our large-scale corpus of embodied human experience (Sec. 4.2.1), and the data processing and training infrastructure that support learning from heterogeneous sources. We then investigate cross-embodiment transfer and introduce a dexterous human-torobot learning system that combines motion retargeting, visual alignment, and world-action modeling. Beyond pretraining, we develop reinforcement learning methods for improving manipulation through interaction and a steerable WAM API that enables agentic planning and guided execution.

**中文:** 要实现这些进展，需要在整个机器人学习栈中进行创新。我们首先介绍 GR00T 2 的架构与预训练框架，包括我们的大规模具身人类经验语料库 Human-1M（Sec. 4.2.1），以及支撑从异构来源学习的数据处理与训练基础设施。随后，我们研究跨本体迁移，并提出一种灵巧的人到机器人学习系统，该系统结合了动作重定向、视觉对齐和世界-动作建模。在预训练之外，我们开发了通过交互改进操作的强化学习方法，以及一个可引导的 WAM API，用于支持智能体化规划与引导式执行。

<a id="S057"></a>
**Source:** p.5 S057

**Original:** We evaluate GR00T 2 across a broad suite of simulated and real-world manipulation tasks, spanning generalpurpose policy performance, few-shot adaptation, cross-embodiment transfer, dexterous manipulation, and whole-body humanoid control. Our results demonstrate the versatility of world-action pretraining as a foundation for acquiring and transferring physical skills, and highlight the complementary roles of large-scale pretraining, interactive post-training, and system-level integration. Together, GR00T 2 represents a step toward general-purpose robot foundation models whose physical knowledge can be transferred across embodiments, efficiently adapted to new tasks, and directly accessed and directed by intelligent agents.

**中文:** 我们在广泛的仿真与真实世界操作任务套件上评估 GR00T 2，涵盖通用策略性能、少样本适应、跨本体迁移、灵巧操作以及全身人形控制。结果表明，世界-动作预训练作为获取和迁移物理技能的基础具有通用性，并突出了大规模预训练、交互式后训练与系统级集成三者的互补作用。总之，GR00T 2 朝着通用机器人基础模型迈出了一步：其物理知识可以跨本体迁移、高效适应新任务，并可被智能体直接访问和引导。
