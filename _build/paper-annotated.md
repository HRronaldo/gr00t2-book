# GR00T 2：面向泛化、灵巧与自适应的机器人基础模型（中英对照精读本）

**原文**：GR00T 2: Scaling Robot Foundation Models for Generalization, Dexterity, and Adaptation
**发布**：NVIDIA，2026 年 11 月 · 项目页 https://research.nvidia.com/labs/gear/gr00t-2
**本地原件**：`D:\learning\gr00t2_whitepaper.pdf`（135 页，含附录 A–K）
**本读本**：全文段落级中英对照，图表按原文位置就近插入，每个区块带 `p.页码 + 区块号` 锚点，可回原文逐字核对。

## 怎么用这份读本

1. 先读 `学习指南.md` 的第 1 讲，建立全局地图；再回到本文件按章精读。
2. 每个区块的 `**Source:**` 行给出 PDF 页码与区块号（S=正文，C=图注/表注，E=公式，H=小节）。
3. `**Original:**` 与 PDF 抽取文本逐字一致，可用于核对术语与数字；`**中文:**` 是对应译文。
4. 图表以 PNG 从原 PDF 裁切，插在其图注所在位置；个别无法精确裁切的图表退化为整页渲染，已在 `translation_notes.md` 标注。

## 目录（点击跳转）

  - [1. Introduction](#H02) · p.3
  - [2. GR00T 2 Overview](#H03) · p.5
  - [3. GR00T 2 Capabilities](#H04) · p.6
  - [3.1. Fast Adaptation: Zero-Shot Generalization and Few-Shot Mastery](#H05) · p.6
  - [3.2. X-Adaptability: Cross-Embodiment Skill Transfer](#H06) · p.8
  - [3.3. Robust Deployment through Reinforcement Learning](#H07) · p.9
  - [3.4. Agentic GR00T 2](#H08) · p.10
  - [3.5. Humanoid Loco-Manipulation](#H09) · p.13
  - [4. How We Made GR00T 2](#H10) · p.14
  - [4.1. Training: Pre-Training and RL Post-Training](#H11) · p.14
  - [4.2. Data](#H12) · p.15
  - [4.3. Real-World Benchmarking: Mapping the Hill We Climb](#H13) · p.16
  - [4.4. Learning without Teleoperation: Devices and Pipelines](#H14) · p.17
  - [4.5. Simulation and Evaluation](#H15) · p.20
  - [4.6. Deployment and Real-Time Inference](#H16) · p.22
  - [4.7. Infrastructure](#H17) · p.24
  - [5. Conclusion and Open Problems](#H18) · p.26
  - [A. Fast-Adapt with GR00T 2](#H20) · p.38
  - [A.1. Benchmark Tasks](#H21) · p.38
  - [A.2. Zero-Shot Generalization with GR00T 2](#H22) · p.40
  - [A.3. Dexter-50: Emergent Cross-Embodiment Zero-Shot and Few-Shot Transfer.](#H23) · p.41
  - [B. X-Adapt with GR00T 2](#H24) · p.42
  - [B.1. Human →Tianji + Sharpa](#H25) · p.42
  - [B.2. UMI →YAM](#H26) · p.48
  - [B.3. DexUMI for Complex, Long-Horizon, and Dynamic Post-Training](#H27) · p.50
  - [B.4. DexUMI →Tianji + Sharpa](#H28) · p.52
  - [B.5. Human →Simulation →Tianji + Sharpa](#H29) · p.53
  - [C. Data for GR00T 2](#H30) · p.57
  - [C.1. Human Data for GR00T 2](#H31) · p.57
  - [C.2. UMI-10K for GR00T 2](#H32) · p.61
  - [C.3. Teleoperation Data for GR00T 2](#H33) · p.62
  - [C.4. Data Annotations](#H34) · p.63
  - [D. Real-World Benchmarking with GearArena](#H35) · p.65
  - [D.1. Why Aggregate Real-Robot Evaluations, and Why A/B](#H36) · p.65
  - [D.2. Designing Evaluation Tasks from First Principles](#H37) · p.66
  - [D.3. The Arena: Stations, Operators, Campaigns, and Suites](#H38) · p.67
  - [D.4. Leaderboard Mathematics](#H39) · p.67
  - [D.7. Limitations](#H40) · p.71
  - [E. UMIverse for GR00T 2](#H41) · p.73
  - [E.1. Gripper UMI Hardware](#H42) · p.73
  - [E.2. UMI Direct](#H43) · p.74
  - [E.3. UMI →YAM Transfer: Embodiment Gaps and Ablations](#H44) · p.75
  - [E.4. DexUMI Exoskeleton Hardware](#H45) · p.81
  - [E.5. DexUMI Post-Training Recipe](#H46) · p.82
  - [E.6. DexUMI WAM-Native Inpainting](#H47) · p.82
  - [F. RL Post-Training](#H48) · p.84
  - [F.1. RL-Based Adaptation of World-Action Models](#H49) · p.84
  - [F.2. Automated Discovery of RL Post-Training Algorithms](#H50) · p.87
  - [F.3. Online RL Post-Training Infrastructure](#H51) · p.89
  - [F.4. Precision Manipulation through RL Post-Training](#H52) · p.91
  - [F.5. Reinforcement Learning with Neural Simulation](#H53) · p.92
  - [G. Agentic GR00T 2](#H54) · p.98
  - [G.1. Agentic Skill Composition and Recovery with Code-as-Policy](#H55) · p.98
  - [G.2. Agentic Steering with Visual Guidance](#H56) · p.102
  - [G.3. Toward Robotic Self-Improvement](#H57) · p.107
  - [H. Humanoid Loco-Manipulation](#H58) · p.109
  - [H.1. GR00T 2 Turbo on Whole-Body Latent Actions](#H59) · p.109
  - [H.2. Real-World Whole-Body Loco-Manipulation](#H60) · p.109
  - [H.3. WAMs Consume Simulation Data Better than VLAs](#H61) · p.111
  - [I. Accelerating GR00T 2](#H62) · p.113
  - [I.1. Accelerating Model Inference](#H63) · p.113
  - [I.2. Policy Smoothness](#H64) · p.115
  - [I.3. Accelerating Task Throughput Beyond Demonstrations](#H65) · p.116
  - [J. Simulations](#H66) · p.118
  - [J.1. Real-to-Sim Generation of High-Fidelity Tasks](#H67) · p.118
  - [J.2. Accelerating GR00T 2 Development with Simulation](#H68) · p.119
  - [J.3. Simulation Benchmarking](#H69) · p.123
  - [K. Infrastructure](#H70) · p.127
  - [K.1. Overall Software and Hardware Stack](#H71) · p.127
  - [K.2. Hardware](#H72) · p.127
  - [K.3. Cluster and Job Management](#H73) · p.128
  - [K.4. Distributed Training](#H74) · p.129
  - [K.5. Inference Infrastructure](#H75) · p.132
  - [K.6. Scalable Multi-Modal Data Processing](#H76) · p.133

---

## 公式索引

| 编号 | 页码 | 原文（抽取文本） |
|---|---|---|
| E001 | p.52 | 𝐾eff = 𝑠acp 𝑘𝑝, (2) |
| E002 | p.68 | 𝑗̸=𝑖𝑛𝑖𝑗/(𝑝𝑖+ 𝑝𝑗), (5) |
| E003 | p.68 | 𝑤𝑚= 1 {𝑚′ : pair(𝑚′) = pair(𝑚), task(𝑚′) = task(𝑚)}⃒⃒, (7) |
| E004 | p.83 | , 𝛼= 𝐺𝜎* 𝑚, (9) |
| E005 | p.85 | 𝑗̸=𝑖𝑅𝑔,𝑗 ℎ𝑔+ 𝑁𝑔−1 , 𝐴𝑔,𝑖= 𝑅𝑔,𝑖−𝑏𝑔,𝑖. (12) |
| E006 | p.86 | ℒSI(𝜃) = 𝜆vℒvideo(𝜃; 𝒟succ) + 𝜆aℒaction(𝜃; 𝒟succ). (16) |
| E007 | p.94 | 𝐶= (1 −𝜎)𝐶+ 𝜎𝜖, 𝜖∼𝒩(0, 𝐼). (20) |

> 公式以原 PDF 裁切图为准；抽取文本中的数学字符常有残缺，凡不能确证者一律保留原字符并标注，不臆造 LaTeX。详见 `translation_notes.md`。

---

<a id="H02"></a>
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

<a id="C001"></a>
**Source:** p.4 C001 · 图 F001

![F001](assets/F001.png)

**Original (caption):** Figure 1: We introduce GR00T 2, a world-action model for general-purpose robots. Top: GR00T 2 pretrains on human and robot data. Second row: given a language goal, multi-view video from the egocentric and both wrist cameras, and the robot state, GR00T 2 jointly predicts multi-view future video and robot actions. Third row: with X-Adapt, GR00T 2 learns a new robot skill from sensorized human demonstrations (Human →Dexter, a Tianji robot with Sharpa hands), from handheld and wearable capture devices (UMI →YAM, DexUMI →XHAND, and DexUMI →Dexter), and through simulation, either from a single human video (Human video →Dexter) or by replaying teleoperated G1 motions across varied simulated scenes (G1 real →sim →real). Bottom: RL post-training on real robots and in a world model improves GR00T 2 beyond its demonstrations (left), a frontier agent runs and steers GR00T 2 (center), and GR00T 2 Turbo directs the SONIC whole-body controller for humanoid loco-manipulation (right).

**中文图注：**我们推出 GR00T 2，这是一种面向通用机器人的世界-动作模型。顶部：GR00T 2 基于人类数据和机器人数据进行预训练。第二行：给定语言目标，以及来自第一人称视角（egocentric）相机和双腕部相机的多视角视频与机器人状态，GR00T 2 联合预测多视角未来视频和机器人动作。第三行：借助 X-Adapt，GR00T 2 能够从带传感器的人类演示（Human →Dexter，搭载 Sharpa 手的 Tianji 机器人）、手持与可穿戴采集设备（UMI →YAM、DexUMI →XHAND 和 DexUMI →Dexter），以及仿真中习得新的机器人技能：既可以从单段人类视频（Human video →Dexter）中学习，也可以通过在多样的仿真场景中回放遥操作得到的 G1 动作来学习（G1 real →sim →real）。底部：在真实机器人上以及世界模型中进行的强化学习后训练，使 GR00T 2 超越其演示（左）；一个前沿智能体运行并引导 GR00T 2（中）；GR00T 2 Turbo 为人形机器人的移动操作指挥 SONIC 全身控制器（右）。

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


<a id="H03"></a>
### 2. GR00T 2 Overview ｜ 2. GR00T 2 概览

<a id="S058"></a>
**Source:** p.5 S058

**Original:** GR00T 2 is a world-action model (WAM): a single model that, given the robot’s visual and proprioceptive input and a user instruction, predicts both how the scene will unfold and the robot’s actions. One pretrained checkpoint covers parallel-gripper arms, dexterous hands, and a humanoid, and learns diverse source data sources including human egocentric videos, handheld UMI gripper data, and robot teleopration data. (Sec. 4.2).

**中文:** GR00T 2 是一种世界-动作模型（WAM）：给定机器人的视觉与本体感知输入以及用户指令，由同一个模型同时预测场景将如何演化，以及机器人的动作。一个预训练检查点即可覆盖平行夹爪机械臂、灵巧手和人形机器人，并从多样的数据来源中学习，包括人类第一人称视角（egocentric）视频、手持式 UMI 夹爪数据以及机器人遥操作数据。(Sec. 4.2).

<a id="S059"></a>
**Source:** p.5 S059

**Original:** Inputs and outputs. At every control step, GR00T 2 receives (i) a 0.8s history of 224 × 320 images from up to four cameras at 5 fps, typically a head camera and one camera on each wrist, (ii) the robot’s proprioceptive state, and (iii) a natural-language instruction. It returns a chunk of future actions together with the predicted future frames of every camera. The robot executes the chunk through its own controller while the next chunk is computed (Sec. K.5).

**中文:** 输入与输出。在每个控制步，GR00T 2 接收 (i) 来自至多四台相机的 0.8 秒历史图像（224 × 320，5 fps，通常为一台头部相机加上每个腕部各一台）、(ii) 机器人的本体感知状态，以及 (iii) 一条自然语言指令。它返回一段未来动作块，以及每台相机的预测未来帧。机器人通过自身控制器执行该动作块，同时下一个动作块正在计算（Sec. K.5）。

<a id="S060"></a>
**Source:** p.5 S060

**Original:** Architecture. GR00T 2 is built on Cosmos-Predict2.5-2B, a video diffusion transformer pretrained for world simulation (NVIDIA et al., 2025a). Video, state, and action inputs become tokens in one sequence that a single 2B-parameter transformer processes (Fig. 1):

**中文:** 架构。GR00T 2 构建于 Cosmos-Predict2.5-2B 之上，后者是一个为世界仿真而预训练的视频扩散 Transformer（NVIDIA et al., 2025a）。视频、状态和动作输入被转换为同一序列中的 token，由单个 2B 参数的 Transformer 统一处理（Fig. 1）：

<a id="S061"></a>
**Source:** p.5 S061

**Original:** • Video. A frozen Wan 2.1 video VAE (Wan Team et al., 2025) compresses each camera stream 4× in time and 8× in each spatial dimension. The latents are split into patches, giving 280 tokens per latent frame and camera at 224 × 320. A learned view embedding tells the model which camera each token comes from. Past frames enter as context, and future frames are generated. • Language. A frozen Cosmos-Reason1 vision-language model (NVIDIA et al., 2025b) encodes the instruction, and the transformer reads it through cross-attention. • State and actions. Small embodiment-specific MLPs map the robot state and the noisy action chunk into the transformer’s width, and an embodiment-specific decoder maps the output tokens back to actions.

**中文:** • 视频。一个冻结的 Wan 2.1 视频 VAE（Wan Team et al., 2025）将每路相机流在时间维度上压缩 4×、在每个空间维度上压缩 8×。潜变量被切分为图块（patch），在 224 × 320 分辨率下，每个潜变量帧、每路相机对应 280 个 token。一个可学习的视角嵌入（view embedding）告诉模型每个 token 来自哪台相机。过去的帧作为上下文输入，未来的帧则由模型生成。• 语言。一个冻结的 Cosmos-Reason1 视觉语言模型（NVIDIA et al., 2025b）对指令进行编码，Transformer 通过交叉注意力读取该编码。• 状态与动作。小型的本体专用 MLP 将机器人状态和带噪动作块映射到 Transformer 的宽度，本体专用解码器再将输出 token 映射回动作。

<a id="S062"></a>
**Source:** p.5 S062

**Original:** Inside the transformer, video tokens attend to one another across time and cameras, and action tokens attend to all video tokens, including the future frames being generated. Actions can therefore follow the future the model imagines. GR00T 2 is trained with flow matching (Lipman et al., 2023) on future video latents and actions together, with one loss for each. At inference, a few denoising steps suffice: one or two for video and two to four for actions in our deployments (Sec. I.1).

**中文:** 在 Transformer 内部，视频 token 在时间和相机之间相互注意，动作 token 则关注所有视频 token，包括正在生成的未来帧。因此，动作可以依循模型所想象的未来来展开。GR00T 2 使用流匹配（Lipman et al., 2023）在未来视频潜变量与动作上联合训练，二者各对应一项损失。推理时，几个去噪步即可满足需要：在我们的部署中，视频用一到两步，动作用两到四步（Sec. I.1）。

<a id="S063"></a>
**Source:** p.5 S063

**Original:** GR00T 2 Turbo: Efficient World-Action Modeling. While GR00T 2 already runs in real time when served from a workstation GPU (a median of 153 ms to predict an action chunk for Dexter from three camera views on a GeForce RTX 5090, Tab. 27), humanoid whole-body loco-manipulation sets a much stricter budget. The policy must react quickly to keep the whole body coordinated as the robot moves, and it must run onboard on

**中文:** GR00T 2 Turbo：高效的世界-动作建模。虽然 GR00T 2 在工作站 GPU 上部署时已能实时运行（在 GeForce RTX 5090 上，利用三路相机视图为 Dexter 预测一个动作块的中位时延为 153 ms，见 Tab. 27），但人形机器人全身移动操作对时延预算的要求要严格得多。策略必须快速响应，才能在机器人运动时保持全身协调，并且它必须在机载端运行，

<a id="C002"></a>
**Source:** p.6 C002 · 图 F002

![F002](assets/F002.png)

**Original (caption):** Figure 2: Cross-embodiment transfer to Dexter with 0, 1, and 5 Dexter episodes. Results on the Dexter-50 tasks, which have no Dexter training data but appear in YAM teleoperation data, human video, or both. Zero-shot runs the pretrained model directly, while 1-shot and 5-shot fine-tune it with LoRA on 1 or 5 Dexter episodes. Left: average success rate over the 50 tasks. Right: number of tasks in each success-rate range. The tasks are those the model learns with five episodes (at least 80% success). Per-task results are in Fig. 24.

**中文图注：** 图 2：使用 0、1 和 5 个 Dexter episode 的跨本体迁移至 Dexter 的结果。结果基于 Dexter-50 任务集，这些任务在 Dexter 训练数据中没有出现，但出现在 YAM 遥操作数据、人类视频或二者之中。Zero-shot 直接运行预训练模型，而 1-shot 与 5-shot 则使用 LoRA 在 1 个或 5 个 Dexter episode 上进行微调。左图：50 个任务的平均成功率。右图：各成功率区间内的任务数量。这些任务是模型用五个 episode 即可学会的任务（成功率至少为 80%）。逐任务结果见 Fig. 24。

<a id="S078"></a>
**Source:** p.6 S078

**Original:** an edge GPU such as the NVIDIA Jetson AGX Thor, which has far less compute. We therefore design GR00T 2 Turbo to make the world-modeling objective itself even cheaper. Most of the tokens GR00T 2 predicts are future video, and video is highly redundant. Turbo keeps the 2B transformer that models video and actions jointly but encodes video with a higher-compression VAE, so it still predicts future observations and actions together, with far fewer visual tokens. This makes both training and inference faster. Turbo predicts in 124 ms on the onboard Jetson Thor of the Unitree G1, where it plans whole-body motion for the SONIC controller (Sec. 3.5 and 4.6.1). Turbo trails GR00T 2 on dexterous tasks but remains well above the baselines on bimanual and dexterous manipulation, and offers a favorable tradeoff between task performance and inference latency (Sec. 3.1 and Fig. 23).

**中文:** 例如 NVIDIA Jetson AGX Thor 这样的边缘 GPU，其算力要少得多。因此，我们设计了 GR00T 2 Turbo，使世界建模目标本身的开销进一步降低。GR00T 2 预测的大部分 token 是未来视频，而视频具有高度冗余性。Turbo 保留了联合建模视频与动作的 2B Transformer，但使用压缩率更高的 VAE 编码视频，因此它仍然同时预测未来观测与动作，只是视觉 token 数量少得多。这使训练与推理都更快。Turbo 在 Unitree G1 的机载 Jetson Thor 上以 124 ms 完成预测，并在此基础上为 SONIC 控制器规划全身运动（Sec. 3.5 and 4.6.1）。Turbo 在灵巧任务上落后于 GR00T 2，但在双臂与灵巧操作上仍远高于基线，并在任务性能与推理时延之间提供了有利的权衡（Sec. 3.1 and Fig. 23）。

<a id="S080"></a>
**Source:** p.6 S080

**Original:** Specifically, Turbo replaces the video VAE with the Wan 2.2 VAE (Wan Team et al., 2025), increasing spatial compression from 8× to 16× per dimension and producing a 4× smaller spatial latent grid. The latent input and output projections are adapted to the new VAE, while the action horizon remains unchanged.

**中文:** 具体而言，Turbo 将视频 VAE 替换为 Wan 2.2 VAE（Wan Team et al., 2025），将每个维度的空间压缩率从 8× 提高到 16×，使空间潜变量网格缩小 4×。潜变量的输入与输出投影层已适配新的 VAE，而动作时域（action horizon）保持不变。

<a id="S081"></a>
**Source:** p.6 S081

**Original:** Using GR00T 2 on a new robot. To bring up a robot, a practitioner maps its cameras to the head and wrist views, expresses its actions in a supported action space (or adds a new one), and post-trains GR00T 2 on demonstrations of the target tasks. Sec. 3 shows how few demonstrations this takes, and how to replace teleoperation with human or UMI demonstrations altogether.

**中文:** 在新机器人上使用 GR00T 2。要让一台机器人运行起来，实践者需要把它的相机映射到头部与腕部视角，将其动作表示为受支持的动作空间（或新增一个动作空间），然后在目标任务的演示数据上对 GR00T 2 进行后训练。第 3 节说明只需多少演示即可完成这一过程，以及如何完全用人类演示或 UMI 演示替代遥操作。

<a id="H04"></a>
### 3. GR00T 2 Capabilities ｜ 3. GR00T 2 能力

<a id="S082"></a>
**Source:** p.6 S082

**Original:** We now present the capabilities of GR00T 2. Sec. 3.1 shows zero-shot deployment and few-shot adaptation on new tasks and post-training on long-horizon tasks that demand precision and dexterity, and Sec. 3.2 studies cross-embodiment transfer, in which GR00T 2 learns a skill on a robot without teleoperated demonstrations of that skill. Sec. 3.3 shows that reinforcement learning improves GR00T 2 beyond its demonstrations, Sec. 3.4 pairs GR00T 2 with a frontier agent for long-horizon tasks, and Sec. 3.5 extends GR00T 2 to whole-body humanoid loco-manipulation. We report the main results here and defer the full evaluations to the appendix.

**中文:** 下面介绍 GR00T 2 的能力。第 3.1 节展示其在新任务上的零样本部署与少样本适配，以及在要求精确与灵巧的长时序任务上的后训练；第 3.2 节研究跨本体迁移，即 GR00T 2 在某台机器人上学会一项技能，而无需该技能的遥操作演示。第 3.3 节表明，强化学习能使 GR00T 2 超越其演示数据；第 3.4 节将 GR00T 2 与前沿智能体配对，用于长时序任务；第 3.5 节将 GR00T 2 扩展到全身人形机器人移动操作。这里只报告主要结果，完整评测留待附录。

<a id="H05"></a>
### 3.1. Fast Adaptation: Zero-Shot Generalization and Few-Shot Mastery ｜ 3.1. 快速适配：零样本泛化与少样本精通

<a id="S083"></a>
**Source:** p.6 S083

**Original:** Zero-shot deployment on new tasks. Pretraining on teleoperation data from many robots and on Human-1M human video (Sec. 4.2) gives GR00T 2 an emergent ability to perform tasks it has never seen on the target robot. We test this on Dexter (Tianji robot + Sharpa hands), a bimanual robot with two 22-DoF dexterous hands, with 50 tasks that are absent from Dexter’s own data and appear only in YAM gripper data, human video, or both. Deployed out of the box and conditioned only on the language instruction, GR00T 2 succeeds in 40% of trials and completes 40 of the 50 tasks at least once (Fig. 2). Most failures come from a single step

**中文:** 在新任务上的零样本部署。在许多机器人的遥操作数据以及 Human-1M 人类视频上进行预训练（Sec. 4.2），使 GR00T 2 获得了一种涌现能力，能够在目标机器人上完成它从未见过的任务。我们在 Dexter（Tianji 机器人 + Sharpa 手）上检验这一能力。Dexter 是一台双臂机器人，配备两只 22-DoF 灵巧手。测试包含 50 个任务，这些任务不在 Dexter 自身的数据中，只出现在 YAM 夹爪数据、人类视频或二者之中。GR00T 2 开箱即用，仅以语言指令为条件，在 40% 的试次中成功，并且 50 个任务中至少完成一次的有 40 个（Fig. 2）。大多数失败来自一个步骤

<a id="C003"></a>
**Source:** p.7 C003 · 表 T001

![T001](assets/T001.png)

**Original (caption):** Table 1: Post-training benchmarks. For each model, Prog. is the average task progress score across all trials and SR is the success rate, both on a scale from 0 to 100. Bold marks the best Prog. and SR in each row, and the last row of each table averages its tasks. Each YAM result is based on up to 20 trials. On Truck Assembly, GR00T 2 and GR00T 2 Turbo were evaluated on a revised, easier set of start scenes, and on the original scenes GR00T 2 succeeds in 7 of 20 trials with a progress score of 94.0. Baselines: 𝜋0.5 (Physical Intelligence et al., 2025), GR00T 1.7 (NVIDIA, 2026a), FastWAM (Yuan et al., 2026), MolmoAct2 (Fang et al., 2026), and FLUX 3 Action (Black Forest Labs, 2026).

**中文表注：** 表 1：后训练基准测试。对每个模型，Prog. 为所有试次的平均任务进度得分，SR 为成功率，二者均取 0 到 100 的刻度。每行中最佳的 Prog. 与 SR 加粗标出，每个表的最后一行对其所有任务取平均。每个 YAM 结果基于至多 20 次试验。在 Truck Assembly 上，GR00T 2 与 GR00T 2 Turbo 是在修订后、更容易的一组起始场景上评测的；在原始场景上，GR00T 2 在 20 次试验中成功 7 次，进度得分为 94.0。基线：𝜋0.5（Physical Intelligence et al., 2025）、GR00T 1.7（NVIDIA, 2026a）、FastWAM（Yuan et al., 2026）、MolmoAct2（Fang et al., 2026）以及 FLUX 3 Action（Black Forest Labs, 2026）。

<a id="S088"></a>
**Source:** p.7 S088

**Original:** Hot Wheels Assembly 95.4 85.0 68.6 50.0 13.1 0.0 19.5 0.0 0.8 0.0 1.5 0.0 0.5 0.0 Toy Tractor Assembly 63.8 45.0 54.5 40.0 8.4 0.0 3.6 0.0 1.9 0.0 1.1 0.0 2.4 0.0 Toy Plane Assembly 71.0 70.0 63.5 55.0 24.0 10.0 11.0 0.0 10.0 0.0 13.5 0.0 10.0 0.0 iPhone into Box 89.0 65.0 91.0 55.0 67.5 5.0 49.5 15.0 17.0 0.0 38.0 0.0 19.5 0.0 Fixed-Pipe Fittings 70.0 70.0 90.0 90.0 30.0 30.0 35.0 35.0 45.0 45.0 35.0 35.0 0.0 0.0 Wire into Breaker 98.5 95.0 100.0 100.0 30.0 30.0 17.0 0.0 18.5 5.0 10.0 10.0 8.0 0.0

**中文:** [存疑：抽取文本为表格行的扁平化结果，列结构丢失，无法确定各数值所属的列，以下按原始顺序保留。] 任务行依次为：Hot Wheels Assembly（Hot Wheels 组装）95.4 85.0 68.6 50.0 13.1 0.0 19.5 0.0 0.8 0.0 1.5 0.0 0.5 0.0；Toy Tractor Assembly（玩具拖拉机组装）63.8 45.0 54.5 40.0 8.4 0.0 3.6 0.0 1.9 0.0 1.1 0.0 2.4 0.0；Toy Plane Assembly（玩具飞机组装）71.0 70.0 63.5 55.0 24.0 10.0 11.0 0.0 10.0 0.0 13.5 0.0 10.0 0.0；iPhone into Box（将 iPhone 放入盒中）89.0 65.0 91.0 55.0 67.5 5.0 49.5 15.0 17.0 0.0 38.0 0.0 19.5 0.0；Fixed-Pipe Fittings（固定管路接头）70.0 70.0 90.0 90.0 30.0 30.0 35.0 35.0 45.0 45.0 35.0 35.0 0.0 0.0；Wire into Breaker（将线缆接入断路器）98.5 95.0 100.0 100.0 30.0 30.0 17.0 0.0 18.5 5.0 10.0 10.0 8.0 0.0。

<a id="S094"></a>
**Source:** p.7 S094

**Original:** Make Shipping Label 78.0 60.0 73.0 60.0 41.0 5.0 16.0 0.0 Flashlight Battery Replacement 86.0 55.0 49.0 15.0 34.0 0.0 41.0 0.0 GB300 Memory 96.0 85.0 81.0 50.0 43.0 0.0 55.0 0.0 Truck Assembly 98.0 65.0 43.0 5.0 0.0 0.0 0.0 0.0 Crude Salt Filtering 98.0 85.0 88.0 65.0 17.0 0.0 14.0 0.0 Vitamin C Test 86.0 75.0 67.0 25.0 9.0 0.0 14.0 0.0 Microscope 64.0 55.0 33.0 20.0 10.0 0.0 9.0 0.0

**中文:** [存疑：抽取文本为表格行的扁平化结果，列结构丢失，无法确定各数值所属的列，以下按原始顺序保留。] 任务行依次为：Make Shipping Label（制作运输标签）78.0 60.0 73.0 60.0 41.0 5.0 16.0 0.0；Flashlight Battery Replacement（更换手电筒电池）86.0 55.0 49.0 15.0 34.0 0.0 41.0 0.0；GB300 Memory（GB300 内存模块）96.0 85.0 81.0 50.0 43.0 0.0 55.0 0.0；Truck Assembly（卡车组装）98.0 65.0 43.0 5.0 0.0 0.0 0.0 0.0；Crude Salt Filtering（粗盐过滤）98.0 85.0 88.0 65.0 17.0 0.0 14.0 0.0；Vitamin C Test（维生素 C 检测）86.0 75.0 67.0 25.0 9.0 0.0 14.0 0.0；Microscope（显微镜操作）64.0 55.0 33.0 20.0 10.0 0.0 9.0 0.0。

<a id="C004"></a>
**Source:** p.7 C004 · 图 F003

![F003](assets/F003.png)

**Original (caption):** Figure 3: Representative tasks from the two post-training benchmarks. Hot Wheels Assembly on YAM (top) and Make Shipping Label on Dexter (bottom).

**中文图注：** 图 3：两个后训练基准测试中的代表性任务。YAM 上的 Hot Wheels Assembly（上）与 Dexter 上的 Make Shipping Label（下）。

<a id="S096"></a>
**Source:** p.7 S096

**Original:** that falls short on precision within an otherwise correct execution. The ability grows with data, and zero-shot success on new Dexter tasks more than doubles as the amount of human video in pretraining increases (Fig. 10). On broader zero-shot suites for YAM and Dexter, GR00T 2 also leads the VLA baselines in success rate (Tabs. 2 and 3).

**中文:** 该步骤在精度上不足，而其余执行本身是正确的。这种能力随数据增长：随着预训练中人类视频数量的增加，Dexter 新任务上的零样本成功率增长超过一倍（Fig. 10）。在 YAM 与 Dexter 更广泛的零样本测试集上，GR00T 2 的成功率同样领先于 VLA 基线（Tabs. 2 and 3）。

<a id="S097"></a>
**Source:** p.7 S097

**Original:** Few-shot mastery with minutes of robot data. Because the pretrained model already knows how to approach

**中文:** 仅用几分钟机器人数据实现少样本精通。由于预训练模型已经知道如何接近

<a id="C005"></a>
**Source:** p.8 C005 · 图 F004

![F004](assets/F004.png)

**Original (caption):** Figure 4: Learning new tasks without teleoperation. Each column is one way to demonstrate a task without the target robot. It shows a demonstration, a GR00T 2 rollout on the robot, and the real-robot success rate per task. Best baseline is the highest success among the other models evaluated on that task (GR00T 1.7 (NVIDIA, 2026a), 𝜋0.5 (Physical Intelligence et al., 2025), LingBot-VA (Li et al., 2026)). *For Conveyor Sorting, the bars show the share of the 50 conveyor items sorted, not the share of successful trials. Full results are in Fig. 27 and Tabs. 4, 5 and 7.

**中文图注：** 图 4：不依赖遥操作学习新任务。每一列对应一种无需目标机器人即可演示任务的方式，展示了演示、GR00T 2 在机器人上的一次 rollout（轨迹采样），以及每个任务的真机成功率。Best baseline 指在该任务上其他被评测模型中的最高成功率（GR00T 1.7（NVIDIA, 2026a）、𝜋0.5（Physical Intelligence et al., 2025）、LingBot-VA（Li et al., 2026））。*对于 Conveyor Sorting，柱状图表示所分拣的 50 件传送带物品所占的比例，而非成功试次的比例。完整结果见 Fig. 27 和 Tabs. 4, 5 and 7。

<a id="S130"></a>
**Source:** p.8 S130

**Original:** these tasks, very little robot data closes the gap. One teleoperated episode per task lifts success to 71%, and five episodes, under three minutes of robot data, lift it to 95%, with 37 of the 50 tasks succeeding in every trial. The 50 tasks were chosen among those the model learns with five episodes (at least 80% success), so the five-episode rate is high partly by construction. Each adaptation is a LoRA fine-tune of about 30 minutes on a single RTX 5090, and merging the adapter into the weights means the adapted model is served exactly like the pretrained one (Sec. A.3).

**中文:** 这些任务上，极少量的机器人数据即可弥合差距。每个任务一个遥操作 episode 即可将成功率提升至 71%；五个 episode（不足三分钟的机器人数据）则将其提升至 95%，其中 50 个任务中有 37 个在每次试验中都成功。这 50 个任务是从模型用五个 episode 即可学会（成功率至少为 80%）的任务中挑选出来的，因此五个 episode 的成功率在一定程度上由挑选方式决定。每次适配都是在单张 RTX 5090 上约 30 分钟的 LoRA 微调；将适配器合并进权重后，适配后的模型与预训练模型的部署方式完全相同（Sec. A.3）。

<a id="S131"></a>
**Source:** p.8 S131

**Original:** Long-horizon tasks that demand precision and dexterity. The same pretraining pays off when GR00T 2 is post-trained on long-horizon tasks that chain many precise steps. On six YAM tasks, from assembling a toy car end to end in 24 stages to inserting a wire into a breaker, GR00T 2 reaches 71.7% average success, compared with at most 12.5% for the VLA and WAM baselines (Tab. 1a and Fig. 3). On seven dexterous-hand tasks, such as filtering crude salt, testing for vitamin C, and swapping a GB300 memory module, GR00T 2 reaches 68.6% average success, compared with at most 0.7% for GR00T 1.7 and 𝜋0.5 (Tab. 1b). Completing such tasks end to end, with dexterous hands and tight tolerances at every step, is a new capability for a generalist robot model. All tasks of both benchmarks are shown in Sec. A.1.

**中文:** 需要精确与灵巧的长时序任务。当 GR00T 2 在串联多个精细步骤的长时序任务上进行后训练时，同样的预训练也带来了收益。在六个 YAM 任务上（从分 24 个阶段端到端组装玩具汽车，到将线缆插入断路器），GR00T 2 的平均成功率达到 71.7%，而 VLA 与 WAM 基线至多为 12.5%（Tab. 1a and Fig. 3）。在七个灵巧手任务上（例如过滤粗盐、维生素 C 检测，以及更换 GB300 内存模块），GR00T 2 的平均成功率达到 68.6%，而 GR00T 1.7 与 𝜋0.5 至多为 0.7%（Tab. 1b）。在每一步都要求灵巧手与严苛公差的前提下端到端完成此类任务，对通用机器人模型而言是一项新能力。两个基准测试的全部任务均展示于 Sec. A.1。

<a id="S132"></a>
**Source:** p.8 S132

**Original:** GR00T 2 Turbo. Although Turbo is designed primarily for onboard deployment on edge devices (Sec. 2), it still retains much of GR00T 2 capability. In zero-shot evaluation, it stays close to GR00T 2 on YAM and ranks second among the evaluated models on Dexter (Tabs. 2 and 3). After post-training it gives up some success, reaching 65.0% on the YAM tasks and 34.3% on the dexterous-hand tasks, still well above the baselines. Fig. 23 shows the resulting trade-off between task progress and inference latency.

**中文:** GR00T 2 Turbo。尽管 Turbo 主要为边缘设备上的机载部署而设计（Sec. 2），它仍保留了 GR00T 2 的大部分能力。在零样本评测中，它在 YAM 上与 GR00T 2 接近，在 Dexter 上在所评测模型中排名第二（Tabs. 2 and 3）。经过后训练后，它损失了一部分成功率：在 YAM 任务上达到 65.0%，在灵巧手任务上达到 34.3%，仍远高于基线。Fig. 23 展示了任务进度与推理时延之间由此产生的权衡。


<a id="H06"></a>
### 3.2. X-Adaptability: Cross-Embodiment Skill Transfer ｜ 3.2. 跨本体适配（x-adapt）：跨本体技能迁移

<a id="S133"></a>
**Source:** p.8 S133

**Original:** GR00T 2 can learn a new task on a robot without any task-specific teleoperated demonstration. Fig. 4 summarizes four ways to teach it such a task, from demonstrations recorded with a motion-capture glove, the DexUMI exoskeleton, or the handheld Gripper UMI, and from a single human video expanded in simulation.

**中文:** GR00T 2 无需任何针对特定任务的遥操作演示，即可在机器人上学习新任务。图 4 总结了教授其此类任务的四种方式：演示数据分别来自动作捕捉手套、DexUMI 外骨骼或手持式 Gripper UMI，还有一种是将单段人类视频在仿真中扩展后得到的数据。

<a id="S134"></a>
**Source:** p.9 S134

**Original:** For the glove and Gripper UMI demonstrations, which come from a different embodiment than the robot, one recipe bridges the gap. Demonstrations recorded without the robot specify the task, task-agnostic play data from the target robot specify the embodiment, and cross-embodiment pretraining connects the two. Without this pretraining, the same post-training data yield substantially lower performance (Sec. B.1.5). For the glove, DexUMI, and Gripper UMI demonstrations, the baselines are post-trained on the same data as GR00T 2 (Fig. 27 and Tabs. 4 and 5). When teleoperated demonstrations are available, they complement rather than replace the human data (App. B).

**中文:** 对于手套和 Gripper UMI 的演示（它们来自与机器人不同的本体（embodiment）），一套方案即可弥合这一差距。脱离机器人采集的演示负责指定任务，目标机器人的任务无关 play 数据负责指定本体，跨本体预训练则将两者连接起来。若没有这一预训练，使用相同的后训练数据时性能会显著下降（Sec. B.1.5）。对于手套、DexUMI 和 Gripper UMI 演示，基线模型所用的后训练数据与 GR00T 2 相同（Fig. 27 及 Tabs. 4 和 5）。当遥操作演示可用时，它们是对人类数据的补充，而非替代（App. B）。

<a id="S135"></a>
**Source:** p.9 S135

**Original:** Transfer to dexterous hands. Two devices record dexterous demonstrations without the robot: a motioncapture glove worn on the bare hand, and the DexUMI exoskeleton, which replicates the robot hand’s joints and contact surfaces and records fingertip forces in the hand’s tactile format. With the glove, human demonstrations are recorded with head and wrist cameras, retargeted offline to the robot hand, and co-trained with play data of the target robot (Sec. B.1.3). On a bimanual robot with Sharpa hands, this recipe teaches precise chemistry-lab tasks and a fast conveyor toss that cannot be demonstrated through teleoperation. On one task, GR00T 2 trained without any teleoperated demonstration outperforms a baseline without cross-embodiment pretraining that receives ten (Fig. 27). DexUMI extends robot-free collection to tasks that depend on force and compliance: from its force recordings, GR00T 2 learns to predict the force to apply along with the motion, and the hand’s stiffness adapts to that force. Trained on DexUMI demonstrations alone, GR00T 2 slices a banana and unscrews a jar in a long-horizon breakfast task and lights a lamp with a struck match, with 60 to 80% success per task, whereas GR00T 1.7 and 𝜋0.5 complete none (Fig. 15 and Tab. 5). DexUMI demonstrations also transfer to a hand that the exoskeleton does not replicate. After retargeting to the 22-DoF Sharpa hand, GR00T 2 succeeds in 60% of trials on microscope slide dabbing and 65% on conveyor package selection and tossing, and the same two baselines succeed in none (Tab. 6).

**中文:** 迁移到灵巧手。两种设备可以在不使用机器人的情况下采集灵巧操作演示：一是戴在裸手上的动作捕捉手套，二是 DexUMI 外骨骼，它复现机器人手的关节和接触面，并以手部触觉格式记录指尖力。使用手套时，人类演示通过头部和腕部相机记录，离线重定向到机器人手上，并与目标机器人的 play 数据联合训练（Sec. B.1.3）。在搭载 Sharpa 灵巧手的双臂机器人上，这一方案教会了精确的化学实验室任务，以及无法通过遥操作演示的快速传送带抛掷动作。在某一任务上，未使用任何遥操作演示、仅依靠此方案训练的 GR00T 2，其表现优于未经跨本体预训练的基线，而后者接收了 ten（原文如此）（Fig. 27）。DexUMI 将无机器人采集扩展到依赖力与柔顺性（compliance）的任务：GR00T 2 从其力记录中学习，在预测运动的同时预测应施加的力，手部刚度随该力自适应。仅用 DexUMI 演示训练，GR00T 2 即可在一个长时序早餐任务中切香蕉、拧开罐子，并用划燃的火柴点亮台灯，每项任务成功率为 60% 至 80%；而 GR00T 1.7 和 π0.5 均未完成任何一项（Fig. 15 及 Tab. 5）。DexUMI 演示还可迁移到外骨骼未复现的手上。将其重定向到 22 自由度（DoF）的 Sharpa 手后，GR00T 2 在显微镜载玻片蘸取任务上的试次成功率为 60%，在传送带包裹挑选与抛掷任务上为 65%，而同样的两个基线均无成功（Tab. 6）。

<a id="S136"></a>
**Source:** p.9 S136

**Original:** Transfer to parallel-gripper robots. Demonstrations are recorded with the handheld Gripper UMI, in robot format through robot-style wrist cameras and a width encoder, and deployed on YAM, a robot that shares neither its cameras, nor its gripper, nor its workspace. GR00T 2 co-trains them with task-agnostic YAM play data that supply the embodiment and aligns them to YAM’s camera geometry and action space (Sec. 4.4.2). With 41 to 75 demonstrations per task and no teleoperation, GR00T 2 completes a long-horizon toy assembly and a board disassembly in 60% and 50% of trials and sorts 86% of the items off a moving conveyor, whereas the baselines complete neither long-horizon task (Tab. 4). As few as 10 to 20 demonstrations yield end-to-end success. Collection is thus decoupled from the robot, and human-speed motion makes dynamic skills learnable.

**中文:** 迁移到平行夹爪（parallel-gripper）机器人。演示使用手持式 Gripper UMI 采集，以机器人格式通过机器人风格的腕部相机和宽度编码器记录，并部署到 YAM 上。YAM 机器人与采集设备既不共享相机，也不共享夹爪或工作空间。GR00T 2 将这些演示与与任务无关的 YAM play 数据联合训练，后者提供本体信息，并使演示与 YAM 的相机几何和动作空间对齐（Sec. 4.4.2）。每项任务使用 41 至 75 条演示且不使用遥操作时，GR00T 2 在长时序玩具组装和板件拆卸任务中的试次成功率分别为 60% 和 50%，并能从移动的传送带上分拣出 86% 的物品；而基线在两项长时序任务上均未完成。仅 10 至 20 条演示即可实现端到端成功。因此，数据采集与机器人解耦，而人类速度的动作使动态技能变得可学习。

<a id="S137"></a>
**Source:** p.9 S137

**Original:** Transfer from a single human video through simulation. From one human video, we reconstruct the objects and the hand-object motion, train an RL expert in simulation, and fine-tune GR00T 2 on visually randomized rollouts of that expert. The resulting policy transfers zero-shot to the real robot and drives a nail in 9 of 10 trials, whereas GR00T 1.7 and 𝜋0.5 complete none of the real-world tasks (Sec. B.5).

**中文:** 通过仿真从单段人类视频迁移。我们从一段人类视频中重建物体及手与物体的运动，在仿真中训练 RL 专家策略，并在该专家策略的视觉随机化 rollout（轨迹采样）上微调 GR00T 2。所得策略以零样本方式迁移到真实机器人上，在 10 次试次中有 9 次成功将钉子敲入；而 GR00T 1.7 和 π0.5 在真实世界任务中均未完成（Sec. B.5）。

<a id="H07"></a>
### 3.3. Robust Deployment through Reinforcement Learning ｜ 3.3. 通过强化学习实现鲁棒部署

<a id="S138"></a>
**Source:** p.9 S138

**Original:** Supervised fine-tuning (SFT) equips GR00T 2 with manipulation skills, but contact-rich tasks remain sensitive to small errors in alignment and physical interaction. We apply real-world RL on top of SFT policy to further improve the reliability of GR00T 2 through real-world interaction and task-level success feedback.

**中文:** 监督微调（SFT）使 GR00T 2 具备了操作技能，但富接触任务对对齐和物理交互中的微小误差依然敏感。我们在 SFT 策略之上施加真实世界 RL，借助真实世界交互和任务级成功反馈，进一步提升 GR00T 2 的可靠性。

<a id="S139"></a>
**Source:** p.9 S139

**Original:** We evaluate four precision manipulation tasks: fixed-pipe fittings (the task of Tab. 1a, started from harder fitting poses), finger placement, cable insertion, and charger insertion (Fig. 5). We directly optimize GR00T 2 using Group Relative Policy Optimization (GRPO) (Shao et al., 2024) and further train on successful GRPO rollouts through GRPO-induced self-imitation. We also compare against residual RL, which learns corrections on top of a frozen GR00T 2 policy (Sec. 4.1).

**中文:** 我们评测了四项精密操作任务：固定管路接头（即 Tab. 1a 中的任务，但从更困难的接头姿态开始）、手指定位、线缆插入和充电器插入（Fig. 5）。我们使用 Group Relative Policy Optimization（GRPO）（Shao et al., 2024）直接优化 GR00T 2，并通过 GRPO 诱导的自模仿，在成功的 GRPO rollout 上进一步训练。我们还与残差 RL 进行了比较，后者在冻结的 GR00T 2 策略之上学习修正量（Sec. 4.1）。

<a id="S140"></a>
**Source:** p.9 S140

**Original:** GRPO-induced self-imitation achieves 88%, 98%, 94%, and 96% success on the four tasks, respectively, compared with 40 to 76% after SFT. Residual RL also improves performance, but without updating the underlying GR00T 2 model (Fig. 5). These results show that real-world RL improves the reliability of GR00T 2

**中文:** GRPO 诱导的自模仿在四项任务上的成功率分别为 88%、98%、94% 和 96%，而 SFT 之后的成功率为 40% 至 76%。残差 RL 同样提升了性能，但它不更新底层的 GR00T 2 模型（Fig. 5）。这些结果表明，真实世界 RL 提升了 GR00T 2 的可靠性。

<a id="C006"></a>
**Source:** p.10 C006 · 图 F005

![F005](assets/F005.png)

**Original (caption):** Figure 5: Real-robot post-training on four contact-rich manipulation tasks. Labels report success rates, and whiskers are 95% Wilson intervals over 50 trials per bar. Bold marks each task’s best method. GRPO and GRPO-induced self-imitation update GR00T 2 directly, whereas residual RL learns a correction policy on top of a frozen GR00T 2. GRPO-induced self-imitation trains on successful GRPO rollouts. *Evaluated with CPS sampling noise.

**中文图注：** 图 5：四项富接触操作任务上的真机后训练。标签为成功率，误差线为每个柱体基于 50 次试次计算的 95% Wilson 区间。加粗表示各任务的最佳方法。GRPO 与 GRPO 诱导的自模仿直接更新 GR00T 2，而残差 RL 在冻结的 GR00T 2 之上学习修正策略。GRPO 诱导的自模仿在成功的 GRPO rollout 上训练。*使用保系数采样（CPS）的采样噪声进行评测。

<a id="C007"></a>
**Source:** p.10 C007 · 图 F006

![F006](assets/F006.png)

**Original (caption):** Figure 6: Agentic runtime architecture. System 2 monitors execution and invokes GR00T 2 and CaP tools through an observe-reason-act-verify loop. GR00T 2 or ASPIRE-generated program serves as execution backends with shared execution environment interface.

**中文图注：** 图 6：智能体化运行时架构。系统 2（S2）通过“观察-推理-行动-验证”循环监控执行，并调用 GR00T 2 与代码即策略（code-as-policy, CaP）工具。GR00T 2 或 ASPIRE 生成的程序均可作为执行后端，共享同一执行环境接口。

<a id="S190"></a>
**Source:** p.10 S190

**Original:** on contact-rich manipulation. The resulting skills can be integrated into agentic execution for more complex, long-horizon tasks (Sec. 3.4), as we will introduce next.

**中文:** [存疑：文本从句中开始，句首缺失] 在接触密集型操作上。所得技能可以整合进智能体化执行，用于更复杂的长时序任务（Sec. 3.4），下文将对此作介绍。

<a id="H08"></a>
### 3.4. Agentic GR00T 2 ｜ 3.4. 智能体化 GR00T 2

<a id="S191"></a>
**Source:** p.10 S191

**Original:** A frontier multimodal agent and GR00T 2 address complementary parts of a task. The agent determines what to do: it decomposes long tasks, monitors progress, and writes code. GR00T 2 determines how to do it, performing the contact-rich manipulation that is difficult to script. The agent serves as System 2 and calls GR00T 2 as a tool alongside camera, state, and CaP tools (Fig. 6). It supports GR00T 2 in four ways. Augment: for tasks that need memory or explicit reasoning, the agent runs a task-level program that calls GR00T 2 for each manipulation step. Together with RL post-training, this puts GR00T 2 first on both the RoboCasa365 (Nasiriany et al., 2026) and RoboDojo (Chen et al., 2026a) leaderboards (Tab. 19). Assist: on real robots, the agent watches GR00T 2 and, when it sees a dropped part or stalled progress, repairs the state with a CaP skill and hands control back, lifting a post-trained GR00T 2 to near-perfect success on three cluttered assembly tasks (Fig. 7). Guide: beyond language, the agent can steer GR00T 2 with visual targets through the WAM API, described below. Improve: an autonomous research agent discovered the basis of the RL recipe we use to post-train GR00T 2 (Sec. 4.1

**中文:** 一个前沿多模态智能体与 GR00T 2 分别负责任务的互补部分。智能体决定做什么：它分解长任务、监控进展并编写代码。GR00T 2 决定怎样做，执行那些难以脚本化的富接触操作。智能体作为系统 2（S2），与相机、状态和 CaP 工具一并，将 GR00T 2 当作工具来调用（Fig. 6）。它以四种方式支持 GR00T 2。增强（Augment）：对于需要记忆或显式推理的任务，智能体运行一个任务级程序，为每个操作步骤调用 GR00T 2。结合 RL 后训练，这使 GR00T 2 在 RoboCasa365（Nasiriany et al., 2026）和 RoboDojo（Chen et al., 2026a）两个排行榜上均居首位（Tab. 19）。辅助（Assist）：在真实机器人上，智能体观察 GR00T 2 的执行过程，当其发现零件掉落或进展停滞时，用 CaP 技能修复状态并将控制权交还，使经过后训练的 GR00T 2 在三项杂乱装配任务上接近完美的成功率（Fig. 7）。引导（Guide）：除语言之外，智能体还可以通过 WAM API 用视觉目标引导 GR00T 2，下文将介绍。改进（Improve）：一个自主研究智能体发现了我们用于 GR00T 2 后训练的 RL 方案的基础（Sec. 4.1 [存疑：文本在此截断]

<a id="C008"></a>
**Source:** p.11 C008 · 图 F007

![F007](assets/F007.png)

**Original (caption):** Figure 7: Agentic assistance on real robots. (a) Successful trials out of 100 per method on three long-horizon assembly tasks on YAM. Before every trial a person randomly dumps all parts onto the table, a cluttered starting configuration never seen in post-training and much harder than the arranged layouts of Tab. 1a. A trial that needed human help counts as a failure. The agent lifts GR00T 2 after SFT + DAgger to at least 97% on all three tasks. (b) Full-task success over 20 repeated-insertion episodes with SFT and RL-post-trained GR00T 2 in the same agentic framework. RL post-training raises success from 60% to 95% on multi-cable and from 10% to 100% on multi-charger insertion.

**中文图注：** 图 7：真实机器人上的智能体辅助。(a) 在 YAM 上完成三项长时序装配任务时，每种方法 100 次试次中的成功次数。每次试次前，由人工随机将所有零件倒在桌面上，形成从未在后训练中出现过的杂乱起始配置，难度远高于 Tab. 1a 中整齐排列的布局。需要人工帮助的试次计为失败。经 SFT + DAgger 后的 GR00T 2 在智能体辅助下，三项任务均至少达到 97%。(b) 在同一智能体化框架中，使用 SFT 与经 RL 后训练的 GR00T 2，对 20 个重复插入回合的整任务成功率。RL 后训练将多线缆插入的成功率从 60% 提升至 95%，将多充电器插入的成功率从 10% 提升至 100%。

<a id="S199"></a>
**Source:** p.11 S199

**Original:** and F.2). We therefore recommend assigning manipulation to GR00T 2 and providing the agent with the task structure, success checks, and a small library of recovery skills (Sec. G.1).

**中文:** [存疑：文本从句中开始，句首缺失] 和 F.2）。因此我们建议将操作交给 GR00T 2，并为智能体提供任务结构、成功检查以及一小套恢复技能库（Sec. G.1）。

<a id="S200"></a>
**Source:** p.11 S200

**Original:** Agentic Skill Composition and Recovery with Code-as-Policy. In simulation, we use ASPIRE (Lu et al., 2026) to discover task-level programs that compose GR00T 2 calls with perception, reasoning, and CaP primitives. These programs use GR00T 2 as a manipulation tool within more complex task sequences, while System 2 monitors execution and invokes online CaP recovery when unexpected failures occur. Combined with RL post-training, this approach achieves 88.0% success on RoboCasa365 and 75.8% on RoboDojo, evaluated on one of its three official layout banks, the highest reported success rates on both leaderboards as of November 6, 2026 (Tab. 19).

**中文:** 基于代码即策略的智能体化技能组合与恢复。在仿真中，我们使用 ASPIRE（Lu et al., 2026）发现任务级程序，这些程序将 GR00T 2 的调用与感知、推理和 CaP 原语组合在一起。它们把 GR00T 2 用作更复杂任务序列中的操作工具，而系统 2 监控执行过程，并在出现意外故障时调用在线 CaP 恢复。结合 RL 后训练，该方法在 RoboCasa365 上达到 88.0% 的成功率，在 RoboDojo 上达到 75.8%，评测基于其三个官方布局库中的一个。截至 2026 年 11 月 6 日，这是两个排行榜上报告的最高成功率（Tab. 19）。

<a id="S201"></a>
**Source:** p.11 S201

**Original:** On physical robots, GR00T 2 remains the primary executor, while the agent monitors progress and invokes CaP skills for targeted recovery. We stress-test this approach on three long-horizon assembly tasks on YAM, a Toy Plane, a Toy Tractor, and a Hot Wheels car (Fig. 55), under conditions much harder than the post-training benchmark in Tab. 1a. There, every trial starts from an arranged layout of the parts. Here, a person randomly dumps all parts onto the table before each trial, so every trial starts from a new cluttered configuration, with overlapping parts and arbitrary poses never seen in post-training, and each method runs 100 trials. The robot must find the parts, assemble them in order, fasten them with a toy drill, and recover from its own errors, all within a single trial that typically lasts 5 to 14 minutes. These numbers therefore measure robustness and are not directly comparable with Tab. 1a. For Hot Wheels Assembly, the benchmark reports 85% success from its fixed layout, while the SFT policy completes 23 of 100 trials once the parts are dumped. DAgger (Ross et al., 2011) raises the three tasks to 84, 71, and 78 successes out of 100, and with the agent repairing dropped parts and stalls before handing control back to GR00T 2, hybrid execution reaches 98, 97, and 97 successes out of 100 trials (Fig. 7). These results bring GR00T 2 closer to deployment-level reliability, with robust long-horizon manipulation from highly variable, unseen initial configurations.

**中文:** 在物理机器人上，GR00T 2 仍是主要执行者，而智能体监控进展，并在需要针对性恢复时调用 CaP 技能。我们在 YAM 上对三项长时序装配任务进行了压力测试，分别是玩具飞机（Toy Plane）、玩具拖拉机（Toy Tractor）和 Hot Wheels 小车（Fig. 55），其条件远比 Tab. 1a 中的后训练基准困难。在基准中，每次试次都从整齐排列的零件布局开始；而在这里，每次试次前都由人工将所有零件随机倒在桌面上，因此每次试次都从新的杂乱配置开始，零件相互重叠、姿态任意，这些情况在后训练中从未出现过，且每种方法各运行 100 次试次。机器人必须找到零件、按顺序装配、用玩具电钻紧固，并从自身错误中恢复，而这一切都要在通常持续 5 至 14 分钟的单次试次内完成。因此，这些数字衡量的是鲁棒性，不能与 Tab. 1a 直接比较。对于 Hot Wheels Assembly，基准在固定布局下报告的成功率为 85%，而 SFT 策略在零件倒下后仅完成了 100 次试次中的 23 次。DAgger（Ross et al., 2011）将三项任务的成功次数提升至 100 次中的 84、71 和 78 次；而在智能体修复掉落零件和停滞、再将控制权交还给 GR00T 2 的混合执行方式下，成功次数达到 100 次试次中的 98、97 和 97 次（Fig. 7）。这些结果使 GR00T 2 更接近部署级别的可靠性，能够在高度多变、未见过的初始配置下完成鲁棒的长时序操作。

<a id="S202"></a>
**Source:** p.11 S202

**Original:** Building on the RL-trained precision skills from Sec. 3.3, agentic execution composes these skills into longer tasks. In repeated cable and charger insertion, the robot must consecutively insert five Ethernet cables into a network switch or five chargers into selected outlets (Fig. 55). CaP handles object localization, grasping, and positioning, while RL-trained GR00T 2 performs the precision-critical insertions. The agent coordinates the sequence, verifies each insertion, and invokes CaP recovery when needed. Within the same agentic framework, replacing SFT policies with RL-post-trained GR00T 2 improves full-task success from 12/20 to 19/20 for cable insertion and from 2/20 to 20/20 for charger insertion (Fig. 7).

**中文:** 在 Sec. 3.3 中经 RL 训练的精密技能基础上，智能体化执行将这些技能组合成更长的任务。在重复的线缆和充电器插入中，机器人需要连续将五根以太网线缆插入网络交换机，或将五个充电器插入指定插座（Fig. 55）。CaP 负责物体定位、抓取与摆放定位，而经 RL 训练的 GR00T 2 完成对精度要求最高的插入动作。智能体负责协调整个序列，验证每一次插入，并在需要时调用 CaP 恢复。在同一智能体化框架内，将 SFT 策略替换为经 RL 后训练的 GR00T 2 后，线缆插入的整任务成功率由 12/20 提升至 19/20，充电器插入则由 2/20 提升至 20/20（Fig. 7）。

<a id="S204"></a>
**Source:** p.12 S204

**Original:** Agentic Steering. With the agent acting as System 2 and GR00T 2 as System 1, a central design question is what the interface between them should be, that is, what the agent sends to GR00T 2 for each step; we refer to this interface as the WAM API. Language is the natural choice, but grounding it in the scene is hard: GR00T 2 must itself find the objects and locations that an instruction refers to. We therefore explore guiding GR00T 2 with image-space grasp and release points in addition to language: the points specify directly which object to manipulate, where to place it, and which arm acts. We mid-train GR00T 2 to condition on these points, rendered as arm-colored markers on its camera image alongside the language instruction. Point supervision is generated automatically from the gripper and hand states in existing demonstrations, requiring neither additional manual annotation nor new robot demonstrations. Once mid-trained, GR00T 2 can be steered by agent-generated points without task-specific policy fine-tuning. During execution, GR00T 2 generates the robot’s actions, while the agent monitors progress and revises its guidance to advance, retry, or finish. In these experiments, the agent is used zero-shot, with one conversation per episode (Sec. G.2).

**中文:** 智能体化引导（Agentic Steering）。在智能体作为系统 2、GR00T 2 作为系统 1 的情况下，核心设计问题是两者之间的接口应是什么，也就是说，智能体在每一步向 GR00T 2 发送什么内容；我们将这一接口称为 WAM API。语言是自然的选择，但要将其锚定到场景中很困难：GR00T 2 必须自己找到指令所指的物体和位置。因此，除语言之外，我们还探索用图像空间中的抓取点和释放点来引导 GR00T 2：这些点直接指定要操作哪个物体、放置到哪里，以及由哪只手臂执行。我们对 GR00T 2 进行中期训练，使其以这些点为条件，这些点被渲染为相机图像上按手臂着色的标记，并与语言指令一同输入。点监督由现有演示中的夹爪和手部状态自动生成，无需额外的人工标注，也无需新的机器人演示。完成中期训练后，GR00T 2 无需针对特定任务的策略微调，即可由智能体生成的点来引导。执行过程中，GR00T 2 生成机器人的动作，而智能体监控进展，并修改其指导，以推进、重试或结束任务。在这些实验中，智能体以零样本方式使用，每个回合使用一次对话（Sec. G.2）。

<a id="C009"></a>
**Source:** p.12 C009 · 图 F008

![F008](assets/F008.png)

**Original (caption):** Figure 8: Higher average success with visual steering on both evaluation tiers. (a) Left- and right-hand steering examples. Circles mark grasp targets and crosses mark release targets, and colors identify the acting arm. (b, c) Equalweight means of benchmark success rates, not pooled trial rates. Short horizon averages two benchmarks (144 and 64 trials per configuration; the Dexter benchmark was obtained with an earlier implementation of the model), and long horizon averages three robot-task combinations: trash sorting on both robots (20 episodes each) and a YAM-only board-disassembly stress test (10 episodes). Robot-specific protocols and results are given in Sec. G.2.

**中文图注：** 图 8：在两个评测层级上，采用视觉引导（visual steering）均取得更高的平均成功率。(a) 左手与右手的引导示例。圆圈标记抓取目标，叉号标记释放目标，颜色标识执行动作的手臂。(b, c) 为基准成功率的等权平均值，而非汇总后的试次成功率。短时序结果取两个基准的平均值（每种配置分别为 144 和 64 次试次；Dexter 基准采用模型的早期实现获得）；长时序结果则平均三种机器人-任务组合：两台机器人上的垃圾分拣（各 20 个回合），以及仅在 YAM 上进行的板件拆卸压力测试（10 个回合）。各机器人的具体协议与结果见 Sec. G.2。

<a id="S218"></a>
**Source:** p.12 S218

**Original:** We evaluate this approach on two embodiments, YAM and Dexter, in two tiers: short-horizon benchmarks test only a few steps instruction following, while long-horizon benchmarks require completing an entire trash-sorting task on both robots, plus board disassembly on YAM as a stress test. Short-horizon instructions are organized by reference type to assess distinct grounding requirements (nominal, spatial, ordinal, cardinal, arm, and object-exclusion references) and execution requirements (action and grasp references). Sec. G.2 details this taxonomy together with the evaluation protocols, individual benchmarks, and instruction-category breakdowns. We compare three settings: GR00T 2 given the original task instruction, GR00T 2 given the agent’s language guidance, and the point-conditioned GR00T 2 given the agent’s language guidance and visual markers. Visual steering achieves the highest average success in both tiers: benchmark-mean success of 76.8% on short-horizon tasks and mean full-task success of 53.3% on long-horizon tasks, compared with 44.2% and 1.7% using the agent’s language guidance alone (Fig. 8).

**中文:** 我们在两种本体（embodiment）YAM 和 Dexter 上、以两个层级评测该方法：短时序基准仅测试少量步骤的指令遵循能力，而长时序基准要求在两台机器人上完成整个垃圾分拣任务，并在 YAM 上加测板件拆卸作为压力测试。短时序指令按指代类型组织，以评估不同的定位需求（名义、空间、序数、基数、手臂和排除物体指代），以及执行需求（动作指代与抓取指代）。Sec. G.2 详细介绍了该分类体系，以及评测协议、各个基准和指令类别的细分结果。我们比较了三种设置：给定原始任务指令的 GR00T 2、给定智能体语言指导的 GR00T 2，以及同时给定智能体语言指导与视觉标记、以点为条件的 GR00T 2。视觉引导在两个层级上均取得最高平均成功率：短时序任务的基准平均成功率为 76.8%，长时序任务的平均整任务成功率为 53.3%；而仅使用智能体语言指导时，分别为 44.2% 和 1.7%（Fig. 8）。

<a id="S219"></a>
**Source:** p.12 S219

**Original:** Despite these gains, grasp and release points cannot convey every task requirement. The markers specify spatial

**中文:** 尽管有这些收益，抓取点与释放点仍无法传达每一项任务要求。这些标记指定的是空间 [存疑：文本在此截断]

<a id="C010"></a>
**Source:** p.13 C010 · 图 F009

![F009](assets/F009.png)

**Original (caption):** Figure 9: Three-level stack for whole-body loco-manipulation. An optional reasoning model (S2) picks the task and the prompt. GR00T 2 Turbo (S1) reads RGB images and proprioception and predicts 1.6 s chunks of SONIC whole-body motion tokens at about 1 Hz. SONIC (S0) decodes the tokens into joint position targets at 50 Hz, which the robot’s PD controller tracks at 1000 Hz. S1 runs onboard on an NVIDIA Jetson AGX Thor, and S0 runs onboard on an NVIDIA Jetson Orin NX.

**中文图注：** 图 9：用于全身移动操作的三层堆栈。一个可选的推理模型（S2）负责选择任务与提示。GR00T 2 Turbo（S1）读取 RGB 图像与本体感知状态，并以约 1 Hz 的频率预测 1.6 秒长的 SONIC 全身运动 token 块。SONIC（S0）将这些 token 解码为 50 Hz 的关节位置目标，再由机器人的 PD 控制器以 1000 Hz 进行跟踪。S1 运行在机载的 NVIDIA Jetson AGX Thor 上，S0 运行在机载的 NVIDIA Jetson Orin NX 上。

<a id="S262"></a>
**Source:** p.13 S262

**Original:** targets, not a complete manipulation strategy: requirements such as placing an object on its side, pouring, or scooping still depend on language and GR00T 2’s learned skills. Richer guidance, including target 6D object poses, goal images, or affordance-based marking, could extend this interface.

**中文:** [存疑：文本从句中开始，句首缺失] 目标，而不是完整的操作策略：诸如将物体侧放、倾倒或舀取等要求，仍然依赖语言以及 GR00T 2 习得的技能。更丰富的指导，包括目标 6D 物体位姿、目标图像或基于可供性（affordance）的标记，可以扩展这一接口。


<a id="H09"></a>
### 3.5. Humanoid Loco-Manipulation ｜ 人形机器人移动操作

<a id="S263"></a>
**Source:** p.13 S263

**Original:** Bipedal humanoid loco-manipulation poses additional challenges to robotic foundation models: the robot must stay balanced through every motion, which requires high-frequency whole-body control at 50 Hz. We bring GR00T 2 to this setting by pairing GR00T 2 Turbo with SONIC (Luo et al., 2026), a learned whole-body controller (Fig. 9). Turbo uses camera observations and proprioception to choose what motion to take next, and SONIC turns that desired motion into joint commands for execution. Both models run onboard the humanoid using a multi-layer stack (Sec. H.1).

**中文:** 双足人形机器人移动操作（loco-manipulation）给机器人基础模型带来了额外挑战：机器人在每个动作中都必须保持平衡，这需要以 50 Hz 运行高频全身控制。我们将 GR00T 2 用于这一场景的方式是，把 GR00T 2 Turbo 与 SONIC（Luo et al., 2026）配对使用，后者是一个经过学习的全身控制器（Fig. 9）。Turbo 利用相机观测与本体感知来选择接下来要执行的动作，SONIC 则把该期望动作转换为关节指令以便执行。两个模型都借助多层软件栈（multi-layer stack）（Sec. H.1）运行在人形机器人本体上。

<a id="S264"></a>
**Source:** p.13 S264

**Original:** Whole-body Loco-manipulation. Using SONIC’s whole-body motion latent interface as its action space, GR00T 2 Turbo coordinates the humanoid’s entire body for locomotion and manipulation. We evaluate the resulting policies on four real-world long horizon whole-body tasks. In popcorn serving, the robot holds a cup while scooping and pouring with the other hand. In table clean-up, it repeatedly grasps diverse objects, walks to the trash bins, and places them inside. In ground pick-up, it bends down to pick up diverse objects. In whole-body cleaning, it picks up a cup from the floor, wipes a spill with a towel under its foot, then kneels to retrieve and discard the towel. On popcorn serving, Turbo completes all 48 trials, compared with 83.3% for GR00T 1.7 using the same demonstrations and controller. Each trial requires two filled cups. Detailed results for all four real-world tasks are reported in Sec. H.2 and Tab. 25.

**中文:** 全身移动操作。GR00T 2 Turbo 以 SONIC 的全身运动潜变量接口作为其动作空间，协调人形机器人的整个身体完成移动与操作。我们在四个真实世界的长时序全身任务上评估所得策略。在“爆米花服务”任务中，机器人一只手托着杯子，另一只手舀取并倒入爆米花。在“桌面清理”任务中，它反复抓取各种物体，走到垃圾桶旁，将物体放入其中。在“地面拾取”任务中，它弯腰拾起各种物体。在“全身清洁”任务中，它从地上捡起杯子，用脚下的毛巾擦掉洒出的液体，然后跪下取回并丢弃毛巾。在爆米花服务任务上，Turbo 完成了全部 48 次试次，而使用相同演示数据和控制器的 GR00T 1.7 对应数值为 83.3%。每次试次需要两个装满的杯子。四个真实任务的详细结果见 Sec. H.2 和 Tab. 25。

<a id="S265"></a>
**Source:** p.13 S265

**Original:** Sim-and-real for Loco-manipulation. Whole-body teleoperation data is costly to collect, so we design a motion-centric real-to-sim pipeline that turns each recorded motion into demonstrations across varied scenes. We replay the motion through SONIC in simulation, keeping it fixed while fitting table and object placements so that the robot completes the pick, then render successful rollouts in diverse rooms. These demonstrations expand visual diversity while preserving the real robot’s controller and action representation (Sec. H.3). The WAM makes better use of this simulated data than the VLA baseline on out-of-distribution table pick-and-place: starting from the same 6.7% success with real data alone, co-training raises GR00T 2 Turbo to 63.3%, compared with 40.0% for GR00T 1.7, over 30 trials each (Tab. 26). Reusing real motions in simulation therefore provides a practical way to improve the WAM’s generalization without collecting additional teleoperated demonstrations.

**中文:** 移动操作的仿真与现实结合。全身遥操作数据采集成本高，因此我们设计了一条以动作为中心的现实到仿真（real-to-sim）流水线，将每段录制的动作转化为多种场景中的演示。我们在仿真中通过 SONIC 重放该动作，保持动作不变，同时调整桌面和物体的摆放位置，使机器人能够完成抓取，然后在多样化的房间中渲染成功的轨迹采样（rollout）。这些演示在保留真实机器人控制器和动作表示（Sec. H.3）的同时扩展了视觉多样性。在分布外（out-of-distribution）的桌面抓放任务上，WAM 比 VLA 基线更好地利用了这些仿真数据。两者在仅使用真实数据时同样以 6.7% 的成功率起步，经联合训练后，GR00T 2 Turbo 提升至 63.3%，而 GR00T 1.7 为 40.0%，每项各进行 30 次试次（Tab. 26）。因此，在仿真中复用真实动作，为提升 WAM 的泛化能力提供了一条实用途径，无需额外采集遥操作演示。

<a id="H10"></a>
### 4. How We Made GR00T 2 ｜ 我们如何构建 GR00T 2

<a id="S266"></a>
**Source:** p.14 S266

**Original:** This section describes the methods behind GR00T 2, focusing on the key design decisions, while the appendix provides the full details. Sec. 4.1 presents the training recipe, from pretraining to RL post-training, and Sec. 4.2 the training data. Sec. 4.3 describes how we benchmark checkpoints against each other on real robots. Sec. 4.4 describes the capture devices and pipelines for learning without teleoperation, Sec. 4.5 the simulation and evaluation framework, Sec. 4.6 real-time deployment, and Sec. 4.7 the training and data infrastructure.

**中文:** 本节介绍 GR00T 2 背后的方法，重点讨论关键设计决策，完整细节见附录。Sec. 4.1 介绍从预训练到 RL 后训练的训练方案，Sec. 4.2 介绍训练数据。Sec. 4.3 描述如何在真实机器人上对检查点进行相互基准测试。Sec. 4.4 描述无需遥操作即可学习时所用的采集设备与流水线，Sec. 4.5 介绍仿真与评测框架，Sec. 4.6 介绍实时部署，Sec. 4.7 介绍训练与数据基础设施。

<a id="H11"></a>
### 4.1. Training: Pre-Training and RL Post-Training ｜ 4.1. 训练：预训练与强化学习后训练

<a id="S267"></a>
**Source:** p.14 S267

**Original:** Pre-training. We initialize GR00T 2 from the pretrained Cosmos-Predict2.5-2B video diffusion transformer. To turn this video model into a general-purpose robot policy, we need it both to understand how physical interactions unfold and to connect those dynamics to actions across embodiments. We therefore train on a diverse mixture of human and robot experience in three stages: we first adapt the video model to embodied interactions, then learn video and actions jointly, and finally place greater emphasis on robot data. This progression lets us draw on the breadth of human experience while focusing the resulting model on robot execution.

**中文:** 预训练。我们以预训练的 Cosmos-Predict2.5-2B 视频扩散 Transformer 初始化 GR00T 2。要把这个视频模型变成通用机器人策略，一方面需要它理解物理交互如何展开，另一方面需要它把这些动力学与跨本体的动作联系起来。为此，我们在人类与机器人经验的多样化数据配比上分三个阶段训练：先使视频模型适应具身交互（embodied interaction），再联合学习视频与动作，最后更加侧重机器人数据。这一递进式流程既利用了人类经验的广度，又使最终模型聚焦于机器人执行。

<a id="S268"></a>
**Source:** p.14 S268

**Original:** Stage 1: Single-view video pre-training. We first adapt the pretrained video model to embodied visual experience from egocentric human video, supplemented by robot data. Human demonstrations provide diverse examples of hands interacting with objects across tasks and environments, while robot observations introduce the visual conditions of robot manipulation. Each training example uses a single camera view, and the model is trained to predict future video from the observation history. The goal is to establish a visual dynamics prior for embodied interaction before training the model to generate actions.

**中文:** 第一阶段：单视角视频预训练。我们首先利用第一人称视角（egocentric）人类视频，辅以机器人数据，使预训练视频模型适应具身视觉经验。人类演示提供了跨任务与环境中手与物体交互的多样示例，机器人观测则引入了机器人操作的视觉条件。每个训练样本使用单一相机视角，模型被训练为基于观测历史预测未来视频。其目标是在训练模型生成动作之前，先为具身交互建立视觉动力学先验。

<a id="S269"></a>
**Source:** p.14 S269

**Original:** Stage 2: Multi-view video-action training. We next connect the learned visual dynamics to actions by extending the model with embodiment-specific state and action modules. We jointly train video and action prediction on human and robot data, using multi-view observations where available to capture interactions from complementary viewpoints. Robot trajectories provide embodiment-specific actions, while human demonstrations provide tracked hand-pose trajectories as action supervision. Video and action are trained with flow-matching objectives, and the action loss is applied when valid action supervision is available. The mixture increases the contribution of YAM and dexterous-hand sources while retaining substantial egocentric human data. Joint training is intended to bring experience from these different embodiments into a shared model that can predict both the evolution of a scene and actions for the target robot.

**中文:** 第二阶段：多视角视频-动作训练。接下来，我们为模型增加本体特定的状态模块与动作模块，从而将习得的视觉动力学与动作联系起来。我们在人类与机器人数据上联合训练视频与动作预测，并在可用时使用多视角观测，以从互补视角捕捉交互。机器人轨迹提供本体特定的动作，人类演示则提供追踪得到的手部姿态轨迹作为动作监督。视频与动作均采用流匹配目标进行训练，且仅在存在有效动作监督时才施加动作损失。该数据配比提高了 YAM 与灵巧手数据源的贡献，同时保留了大量第一人称视角的人类数据。联合训练旨在把来自这些不同本体的经验汇入同一个共享模型，使其既能预测场景的演化，也能预测目标机器人的动作。

<a id="S270"></a>
**Source:** p.14 S270

**Original:** Stage 3: Robot-upweighted video-action training. A broad mixture of human and robot data provides diverse physical experience, but the final policy must generate actions in the robot’s own action space. We therefore continue joint video-action training with a stronger emphasis on robot demonstrations, particularly YAM, while retaining dexterous-hand, egocentric human, and other data sources. This reweighting focuses training on the observations and control required for robot execution while continuing to draw on the broader experience acquired in the earlier stages.

**中文:** 第三阶段：提高机器人数据权重的视频-动作训练。广泛的人类与机器人数据混合提供了多样的物理经验，但最终策略必须在机器人自身的动作空间中生成动作。因此，我们以更强的侧重点继续联合视频-动作训练，尤其是 YAM 上的机器人演示，同时保留灵巧手、第一人称视角的人类数据及其他数据源。这种重新加权使训练聚焦于机器人执行所需的观测与控制，同时继续利用前几个阶段获得的更广泛经验。

<a id="S271"></a>
**Source:** p.14 S271

**Original:** The resulting model serves as the starting point for the task-specific adaptation and RL post-training described below. Details of the data sources are provided in Sec. 4.2.

**中文:** 得到的模型作为下文所述特定任务适配与 RL 后训练的起点。数据源的详细信息见 Sec. 4.2。

<a id="S272"></a>
**Source:** p.14 S272

**Original:** RL post-training. To explore, we replace GR00T 2’s deterministic action denoising with Coefficients-Preserving Sampling (CPS) (Wang and Yu, 2025) during rollouts, injecting noise only into the action denoising process while video denoising stays deterministic. Policy updates use a group-relative objective in the style of GRPO whose baseline also remembers each context’s past returns, so that groups in which every attempt succeeds, or every attempt fails, still carry a learning signal. The basis of this recipe was found by AutoRL, a research agent that iterated on the algorithm in simulation for about 35 days (Sec. F.2). Two complementary approaches are GRPO-induced self-imitation, which fine-tunes GR00T 2 on successful GRPO rollouts, and residual RL, which learns a small corrective policy on top of a frozen GR00T 2 (Sec. F.1.2). For RL without the real robot, we adapt the DreamDojo world model to the target tasks from rollouts of the initial policy and use a learned

**中文:** RL 后训练。为了探索，我们在轨迹采样（rollout）期间，用保系数采样（Coefficients-Preserving Sampling, CPS）（Wang and Yu, 2025）替换 GR00T 2 的确定性动作去噪，仅向动作去噪过程注入噪声，视频去噪则保持确定性。策略更新采用仿照 GRPO 的组相对目标，其基线还会记住每个上下文过去的回报，因此即使一组中所有尝试都成功或都失败，该组仍能提供学习信号。这一方案的基础由研究智能体 AutoRL 发现，它在仿真中迭代该算法约 35 天（Sec. F.2）。两种互补的方法分别是：GRPO 诱导的自我模仿，即在成功的 GRPO 轨迹采样上微调 GR00T 2；以及残差 RL，即在冻结的 GR00T 2 之上学习一个小型纠正策略（Sec. F.1.2）。对于无需真实机器人的 RL，我们利用初始策略的轨迹采样，将 DreamDojo 世界模型适配到目标任务，并使用一个经过学习的

<a id="C011"></a>
**Source:** p.15 C011 · 图 F010

![F010](assets/F010.png)

**Original (caption):** Figure 10: Scaling human video in pretraining. Human-1M data pre-training (0%, 1%, 10%, or 100%) post-trained with Dexter teleoperation data and evaluated on 72 tasks. Real Robot: 3 rollout episodes per task. An operator grades binary success and a vision-language model scores task progress. Video rollout: autoregressive video generation from 3 recorded initial configurations per task and 10 generation seeds per configuration. A vision-language model judges success and scores task progress. We report % progress and success rate with ±1 SEM bars.

**中文图注：** 预训练中的人类视频规模扩展。在 Human-1M 数据上以 0%、1%、10% 或 100% 的比例进行预训练，再使用 Dexter 遥操作数据进行后训练，并在 72 个任务上评估。真实机器人：每个任务 3 个轨迹采样回合。由操作员判定二元成功，由视觉语言模型给出任务进度评分。视频轨迹采样：对每个任务，从 3 个记录的初始配置出发，每个配置使用 10 个生成种子进行自回归视频生成。由视觉语言模型判断成功并给出任务进度评分。我们报告任务进度（%）与成功率，误差线为 ±1 SEM。

<a id="S287"></a>
**Source:** p.15 S287

**Original:** completion detector as the reward (Sec. F.5). An online infrastructure coordinates robot interaction, training, and evaluation, and retains experience across interruptions (Sec. F.3).

**中文:** 完成检测器（completion detector）作为奖励（Sec. F.5）。一套在线基础设施负责协调机器人交互、训练与评测，并在中断之后保留经验（Sec. F.3）。


<a id="H12"></a>
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

<a id="H13"></a>
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

<a id="C012"></a>
**Source:** p.17 C012 · 图 F011

![F011](assets/F011.png)

**Original (caption):** Figure 11: Mapping the hill we climb. Every checkpoint on the current YAM suite, rated relative to the A/B reference (⋆, the board’s top-rated checkpoint, here a GR00T 2 Turbo checkpoint) and placed at the date it was saved. The line tracks the best checkpoint so far, and bars are paired 90% bootstrap intervals for the checkpoints that set a new best. Evidence: the 6,035 blinded A/B comparisons of this suite, from 122 campaigns.

**中文图注：** 图 11：绘制我们攀登的山丘。当前 YAM 套件上的每个检查点都相对于 A/B 参考（⋆，即排行榜上评级最高的检查点，此处为一个 GR00T 2 Turbo 检查点）进行评级，并按其保存日期放置。折线追踪迄今最佳的检查点，柱条为创下新最佳的检查点所对应的配对 90% 自助法（bootstrap）区间。依据：本套件共 122 个评测批次中的 6,035 次盲测 A/B 比较。

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


<a id="H14"></a>
### 4.4. Learning without Teleoperation: Devices and Pipelines ｜ 无遥操作学习：设备与流程

<a id="S320"></a>
**Source:** p.17 S320

**Original:** GR00T 2 learns a skill on a robot from demonstrations recorded without that robot (Sec. 3.2). In all four sources below, the demonstrations specify the task. For human motion capture and the Gripper UMI, whose devices differ from the robot, task-agnostic data from the target robot specify the embodiment, and cross-embodiment pretraining connects the two. The DexUMI exoskeleton replicates the robot hand it is built for, so on that hand its demonstrations need no robot play data (Sec. 4.4.3). Capture and conversion remove what can be removed before training, namely differences in camera geometry (Sec. C.1.3), kinematics, and action semantics

**中文:** GR00T 2 从未操作该机器人时录制的演示中学习技能（见第 3.2 节）。下列四种来源中，演示都指明了任务。对于人体动作捕捉和 Gripper UMI 这两种与机器人设备不同的来源，目标机器人的任务无关数据用于指定本体（embodiment），跨本体预训练则把两者连接起来。DexUMI 外骨骼复刻了其所适配的机器人手，因此在该手上，其演示无需机器人自由操作数据（robot play data）（见第 4.4.3 节）。采集与转换环节会在训练前尽量消除可消除的差异，即相机几何（见第 C.1.3 节）、运动学以及动作语义上的差异。

<a id="C013"></a>
**Source:** p.18 C013 · 图 F012

![F012](assets/F012.png)

**Original (caption):** Figure 12: GR00T 2 learns new robot tasks from human demonstrations. (1) A person performs the task wearing GMSL head and wrist cameras at robot-matched poses, PICO controllers that track 6-DoF wrist poses, and Manus gloves that track finger joints. (2) Retargeting maps each wrist pose to the 7-DoF arm and each hand pose to the 22-DoF hand, and the video stays unmodified. (3) GR00T 2 co-trains on the retargeted human demonstrations and on robot data of other tasks: videos supervise video prediction, and human and robot actions train one shared action head. (4) On the robot, GR00T 2 takes the observation and the instruction, predicts a sequence of future frames, and outputs the actions the robot executes. No teleoperated demonstration of the new task enters training.

**中文图注：** 图 12：GR00T 2 从人类演示中学习新的机器人任务。(1) 人员佩戴与机器人姿态匹配的 GMSL 头部与腕部相机，同时手持追踪 6-DoF 腕部位姿的 PICO 控制器，并戴上追踪手指关节的 Manus 手套来完成任务。(2) 重定向把每个腕部位姿映射到 7-DoF 手臂，把每个手部位姿映射到 22-DoF 手，视频保持不修改。(3) GR00T 2 在重定向后的人类演示与其他任务的机器人数据上联合训练：视频用于监督视频预测，人类动作与机器人动作共同训练同一个动作头。(4) 在机器人上，GR00T 2 接收观测与指令，预测未来若干帧的序列，并输出机器人执行的动作。训练中不包含新任务的任何遥操作演示。

<a id="S324"></a>
**Source:** p.18 S324

**Original:** A person performs the task wearing head and wrist cameras at robot-matched poses, a motion-capture glove, and a 6-DoF tracker on each wrist (Fig. 12). With the head camera at the robot’s head-camera pose, the wrists are anchored in the robot base frame, and a closed-form inverse-kinematics solver (Chen et al., 2026b; Kong et al., 2026) retargets them offline to the 7-DoF arms and 22-DoF Sharpa hands, placing the robot fingertips at the human fingertips to preserve the pinch geometry. The video stays unmodified. At about 118,000 bimanual solves per second, the same solver also drives teleoperation, which collects task-agnostic play data on the target robot. One play pool, sampled 1:1 with the human demonstrations, serves every task (Sec. B.1.1 to B.1.3 and C.3.1). For tasks that only humans demonstrated, GR00T 2 then predicts the robot’s own hands completing each step (Fig. 13).

**中文:** 人员佩戴头部与腕部相机，并在每只腕部佩戴一副动作捕捉手套和一个 6-DoF 追踪器，以与机器人姿态匹配的方式完成任务（见图 12）。头部相机处于机器人的头部相机姿态时，腕部被锚定在机器人基座坐标系中，随后由闭式逆运动学求解器（Chen et al., 2026b; Kong et al., 2026）离线将其重定向到 7-DoF 手臂和 22-DoF 的 Sharpa 手上，并使机器人指尖对准人类指尖，以保留捏取几何。视频保持不修改。该求解器每秒可完成约 118,000 次双臂求解，同样也驱动遥操作，用于在目标机器人上采集与任务无关的自由操作数据（play data）。一个自由操作数据池与人类演示按 1:1 采样，服务于所有任务（见第 B.1.1 至 B.1.3 节与第 C.3.1 节）。对于仅由人类演示过的任务，GR00T 2 随后预测机器人自己的手完成每个步骤（见图 13）。

<a id="S325"></a>
**Source:** p.18 S325

**Original:** Filter Paper Setup

**中文:** 滤纸装配

<a id="S326"></a>
**Source:** p.18 S326

**Original:** 1 Place filter 2 Secure it 3 Wet it Dropper-to-Beaker Dispensing

**中文:** 1 放置滤纸 2 固定滤纸 3 润湿滤纸 滴管至烧杯分液

<a id="S327"></a>
**Source:** p.18 S327

**Original:** 1 Grasp pipette 2 Draw liquid 3 Dispense

**中文:** 1 抓取移液管 2 吸取液体 3 分液

<a id="S328"></a>
**Source:** p.18 S328

**Original:** Human demo

**中文:** 人类演示

<a id="S329"></a>
**Source:** p.18 S329

**Original:** Human demo training data training data real input real input prediction prediction

**中文:** 人类演示 训练数据 训练数据 真实输入 真实输入 预测 预测 [存疑：抽取文本中词语重复，疑为图中标签]

<a id="C014"></a>
**Source:** p.18 C014 · 图 F013

**Original (caption):** Figure 13: Human demonstrations and GR00T 2 predictions. Two tasks that only humans demonstrated. Given one robot start frame and the instruction, GR00T 2 predicts the robot’s ego view. Times are measured from the start frame. Human demonstrations (top rows) appear only in training. All four tasks are shown in Fig. 28.

**中文图注：** 图 13：人类演示与 GR00T 2 预测。两个仅由人类演示过的任务。给定一帧机器人起始画面与指令，GR00T 2 预测机器人的第一人称视角。时间以起始帧为起点计算。人类演示（上方各行）仅出现在训练中。全部四个任务见图 28。

<a id="C015"></a>
**Source:** p.19 C015 · 图 F014

![F013](assets/F013.png)

**Original (caption):** Figure 14: GR00T 2-generated future frames on YAM, without and with YAM co-training. Both models observe the same YAM top-camera frame (left) and predict eight future steps of Toy Dumptruck Assembly, a task demonstrated only with Gripper UMI. Trained on UMI data alone (top), GR00T 2 renders human arms and the blue UMI fingers entering the scene. Co-trained with task-agnostic YAM data (bottom), it renders YAM’s own arms. The co-training data supply the robot’s appearance as well as its action statistics.

**中文图注：** 图 14：GR00T 2 在 YAM 上生成的未来帧，分别为未经 YAM 联合训练与经过 YAM 联合训练的结果。两个模型观测到相同的 YAM 顶部相机画面（左），并预测 Toy Dumptruck Assembly 任务的八个未来步。该任务仅用 Gripper UMI 演示。仅用 UMI 数据训练时（上方），GR00T 2 渲染出人手与蓝色 UMI 手指进入画面。与任务无关的 YAM 数据联合训练后（下方），它渲染出的是 YAM 自身的手臂。联合训练数据既提供了机器人的外观，也提供了其动作统计特性。

<a id="C016"></a>
**Source:** p.19 C016 · 图 F015

![F014](assets/F014.png)

**Original (caption):** Figure 15: DexUMI demonstration and GR00T 2 rollout. Prepare Banana Yogurt, with keyframes numbered by subtask: a person demonstrating the task with the DexUMI exoskeletons (top) and a GR00T 2 rollout on a Tianji robot with XHAND1 Pro-U hands (bottom). The task is demonstrated only with DexUMI. All three DexUMI tasks are shown in Fig. 30.

**中文图注：** 图 15：DexUMI 演示与 GR00T 2 的 rollout（轨迹采样）。Prepare Banana Yogurt 任务，关键帧按子任务编号：上方为人员佩戴 DexUMI 外骨骼演示该任务，下方为 GR00T 2 在搭配 XHAND1 Pro-U 手的 Tianji 机器人上的 rollout。该任务仅用 DexUMI 演示。全部三个 DexUMI 任务见图 30。

<a id="S346"></a>
**Source:** p.19 S346

![F015](assets/F015.png)

**Original:** 4.4.2. Gripper UMI

**中文:** 4.4.2 Gripper UMI

<a id="S347"></a>
**Source:** p.19 S347

**Original:** Gripper UMI is a handheld parallel gripper in the lineage of UMI (Chi et al., 2024). We use our open-source GEAR UMI (NVIDIA GEAR Team, 2026): its robot-style wrist cameras and width encoder record human demonstrations in robot coordinates without a robot (Sec. E.1), and it also yields the UMI-10K pretraining corpus (Sec. 4.2.2). A robot end-effector that reproduces the handheld’s cameras and fingers removes the sensing and gripper gaps by construction (Sec. E.2). For an off-the-shelf robot such as YAM, which shares none of them, three findings make the transfer work. (1) Co-training with task-agnostic YAM data closes the appearance and scene gap: GR00T 2 then predicts YAM’s arms performing the handheld-demonstrated task (Fig. 14). (2) The model absorbs appearance but not geometry, so the fisheye wrist view is re-rendered to imitate YAM’s wrist camera, and a rough match of field of view and viewing direction suffices. (3) Handheld actions are re-expressed in YAM’s action space and decoded by its own action head. With cross-embodiment pretraining, 41 to 75 handheld episodes per task reach high success rates, and 10 to 20 already yield end-to-end success. The rarest subskill, not the task length, sets this number (Sec. B.2 and E.3).

**中文:** Gripper UMI 是一种手持式平行夹爪，属于 UMI（Chi et al., 2024）这一脉络。我们使用开源的 GEAR UMI（NVIDIA GEAR Team, 2026）：其机器人式腕部相机与宽度编码器可在没有机器人的条件下，以机器人坐标记录人类演示（见第 E.1 节），同时它还能产出 UMI-10K 预训练语料（见第 4.2.2 节）。让机器人末端执行器复刻手持设备的相机与手指，可以在构造上消除感知与夹爪两方面的差距（见第 E.2 节）。对于 YAM 这类现成机器人，它与手持设备一样都不具备上述特征，三项发现使迁移得以成立。(1) 与任务无关的 YAM 数据联合训练弥合了外观与场景差距：此后 GR00T 2 可以预测 YAM 的手臂执行手持设备所演示任务的过程（见图 14）。(2) 模型能够吸收外观，却吸收不了几何，因此鱼眼腕部视角被重新渲染，以模仿 YAM 的腕部相机，视场角与观察方向只需大致匹配即可。(3) 手持动作被重新表达到 YAM 的动作空间中，并由其自身的动作头解码。借助跨本体预训练，每个任务 41 至 75 条手持设备采集的片段即可达到较高成功率，10 至 20 条片段便已能实现端到端成功。决定这一数字的是最稀少的子技能，而不是任务长度（见第 B.2 节与第 E.3 节）。

<a id="S349"></a>
**Source:** p.19 S349

**Original:** 4.4.3. DexUMI

**中文:** 4.4.3 DexUMI

<a id="S350"></a>
**Source:** p.19 S350

**Original:** DexUMI (Xu et al., 2025) extends robot-free collection from parallel grippers to five-fingered hands. We use our open-source GEAR DexUMI (NVIDIA GEAR Team, 2026): the wearable exoskeleton replicates the kinematics of the target XHAND1 Pro-U hand, with its 16 degrees of freedom mapped one-to-one onto the

**中文:** DexUMI（Xu et al., 2025）将无机器人采集从平行夹爪扩展到了五指手。我们使用开源的 GEAR DexUMI（NVIDIA GEAR Team, 2026）：可穿戴外骨骼复刻目标 XHAND1 Pro-U 手的运动学，其 16 个自由度一一映射到

<a id="C017"></a>
**Source:** p.20 C017 · 图 F016

**Original (caption):** Figure 16: Human-to-sim-to-real transfer for GR00T 2. (1) Human-to-sim reconstructs assets and motions from one human demonstration. (2) RL trains a state-based manipulation policy in simulation. (3) Data collection under perturbations expands state coverage and captures recovery behavior. (4) GR00T 2 is fine-tuned exclusively on simulation data and deployed zero-shot in the real world.

**中文图注：** 图 16：GR00T 2 的人类到仿真再到现实的迁移（Human-to-sim-to-real）。(1) 人到仿真环节从一次人类演示中重建资产与运动。(2) 强化学习在仿真中训练基于状态的操作策略。(3) 在扰动下采集数据，扩展状态覆盖范围并捕获恢复行为。(4) GR00T 2 仅在仿真数据上微调，并以零样本方式部署到真实世界。

<a id="S372"></a>
**Source:** p.20 S372

![F016](assets/F016.png)

**Original:** robot joints, and matches the hand’s contact surfaces, wrist-camera mount, and tactile format (Sec. E.4). Two choices adapt GR00T 2 to these data. First, the exoskeleton is handled in training rather than by editing video: its green parts are segmented by color, and their appearance is randomized consistently in the conditioning and predicted frames, which removes the earlier step of replaying each demonstration on a robot hand for inpainting (Sec. E.6). Second, following the Adaptive Compliance Policy (Hou et al., 2025), fingertip forces are projected onto the hand joints as torques and added to the action. At execution, the predicted torque lowers each joint’s stiffness and offsets its position target, so that the hand applies the predicted force and remains robust to positional uncertainty (Sec. B.3). Because the exoskeleton replicates the hand, no robot play data are needed: post-trained on DexUMI demonstrations alone, GR00T 2 performs long-horizon tool use with both hands (Fig. 15).

**中文:** 机器人关节，并匹配手的接触表面、腕部相机安装位与触觉格式（见第 E.4 节）。有两项选择使 GR00T 2 适配这些数据。第一，外骨骼在训练中处理，而不是通过编辑视频来处理：其绿色部件按颜色分割，其外观在条件帧与预测帧中被一致地随机化，这样就省去了此前将每条演示在机器人手上重放以进行补全（inpainting）的步骤（见第 E.6 节）。第二，遵循自适应柔顺策略（ACP）（Hou et al., 2025），指尖受力被投影为各手部关节的扭矩，并加入动作中。执行时，预测的扭矩会降低每个关节的刚度并偏移其位置目标，使手施加预测的力，同时对位置不确定性保持鲁棒（见第 B.3 节）。由于外骨骼复刻了手，因此不需要机器人自由操作数据（robot play data）：仅在 DexUMI 演示上进行后训练，GR00T 2 即可用双手完成长时序的工具使用（见图 15）。

<a id="S373"></a>
**Source:** p.20 S373

**Original:** DexUMI demonstrations can also be converted for a hand that the exoskeleton does not replicate. For the 22-DoF Sharpa hand, we compute the XHAND fingertip positions from the recorded joint angles and retarget them with the closed-form solver used for glove teleoperation (Sec. B.1.2). As with Gripper UMI, we warp each DexUMI wrist frame to match the Sharpa wrist camera, which sits at a different pose. The demonstrations are co-trained with Sharpa play data in the robot’s action space and with its normalization statistics (Sec. B.4).

**中文:** DexUMI 演示也可以转换给外骨骼并未复刻的手。对于 22-DoF 的 Sharpa 手，我们根据记录的关节角计算 XHAND 指尖位置，并使用手套遥操作所用的闭式求解器对其进行重定向（见第 B.1.2 节）。与 Gripper UMI 一样，我们将每个 DexUMI 腕部帧做变换，以匹配位于不同位姿的 Sharpa 腕部相机。这些演示与 Sharpa 自由操作数据在机器人动作空间中联合训练，并使用后者的归一化统计量（见第 B.4 节）。

<a id="S374"></a>
**Source:** p.20 S374

**Original:** 4.4.4. Human-to-Sim-to-Real

**中文:** 4.4.4 人类到仿真再到现实

<a id="S375"></a>
**Source:** p.20 S375

**Original:** Contact-rich skills such as in-hand reorientation and forceful tool use remain difficult for WAMs to learn, and recovery behaviors are difficult to demonstrate. Reinforcement learning in simulation supplies them from a single human video (Fig. 16). The NVIDIA Video to Data pipeline (NVIDIA, 2026b) reconstructs the object assets and the hand and object motion. A state-based RL expert, trained with CHORD (Zhu et al., 2026) under identified robot dynamics and randomized physics, learns to track the object motion and complete the task. Its rollouts become image-based training data, perturbed by random action bursts and teleports so that they contain corrections, and rendered in Isaac Lab with randomized appearance, lighting, and camera calibration. GR00T 2 is fine-tuned on 1.5k such episodes per task with training-time real-time chunking (Sec. 4.6.2) and deployed on the real robot without any real-world robot data (Sec. B.5).

**中文:** 富接触技能（如手内姿态调整与高力度工具使用）对 WAM 而言仍然难以学习，而恢复行为也难以通过演示来展示。仿真中的强化学习可以从单段人类视频中提供这些技能（见图 16）。NVIDIA Video to Data 流程（NVIDIA, 2026b）重建物体资产以及手与物体的运动。一个基于状态的 RL 专家在已辨识的机器人动力学与随机化物理条件下，使用 CHORD（Zhu et al., 2026）训练，学会跟踪物体运动并完成任务。其 rollout 被转化为基于图像的训练数据，并通过随机动作脉冲与瞬移加以扰动，使其包含修正行为，然后在 Isaac Lab 中以随机化的外观、光照与相机标定进行渲染。GR00T 2 在每个任务 1.5k 条此类片段上微调，并使用训练时实时分块（见第 4.6.2 节），随后部署到真实机器人上，且不使用任何真实世界机器人数据（见第 B.5 节）。


<a id="H15"></a>
### 4.5. Simulation and Evaluation ｜ 4.5 仿真与评测

<a id="S376"></a>
**Source:** p.20 S376

**Original:** Simulation serves GR00T 2 in two roles. Physics simulation of digital twins of our real-world tasks provides a fast, repeatable, and calibrated proxy for real-robot evaluation, which we use throughout development (Sec. 4.5.1 and 4.5.2). Neural simulation with a learned world model, adapted from recorded rollouts, provides an environment for reinforcement learning (Sec. 4.5.3). We also evaluate GR00T 2 on five public simulation benchmarks (Sec. 4.5.4).

**中文:** 仿真在 GR00T 2 的研发中承担两种角色。针对真实任务构建的数字孪生（digital twin）物理仿真，为真机评测提供了快速、可重复且经过校准的代理，我们在整个开发过程中都在使用它（见 Sec. 4.5.1 和 4.5.2）。基于学习得到的世界模型、并利用录制的轨迹采样（rollout）数据加以适配的神经仿真，为强化学习提供了环境（见 Sec. 4.5.3）。我们还在五个公开仿真基准测试上评估了 GR00T 2（见 Sec. 4.5.4）。

<a id="C018"></a>
**Source:** p.21 C018 · 图 F017

![F017](assets/F017.png)

**Original (caption):** Figure 17: Real-world tasks and their simulated counterparts. Each pair shows the real workcell’s top camera (Real) and the same moment when the recorded robot commands are replayed in simulation (Sim), for five general manipulation tasks and one stage of the multi-stage airplane assembly. More tasks are shown in Fig. 61.

**中文图注：** 真实任务及其仿真对应物。每组图像展示真实工作单元（workcell）的顶部相机画面（Real），以及同一时刻将录制的机器人指令在仿真中回放的画面（Sim），涵盖五项通用操作任务，以及多阶段飞机装配中的一个阶段。更多任务见 Fig. 61。

<a id="C019"></a>
**Source:** p.21 C019 · 图 F018

![F018](assets/F018.png)

**Original (caption):** Figure 18: Simulated vs. real-world performance per policy. (a) Task progress (mean rubric score) and (b) success rate, averaged over 25 tasks (dashed: y = x). (c) Bradley-Terry Elo ratings fitted separately to pairwise outcomes in simulation and in real-world A/B evaluations (dashed: least-squares fit, since the two Elo scales differ). r: Pearson, 𝜌: Spearman, MMRV: mean maximum rank violation. Each point is a generalist checkpoint of GR00T 2 trained for the YAM embodiment.

**中文图注：** 按策略划分的仿真与真实世界表现对比。(a) 任务进度（平均评分标准得分，mean rubric score）与 (b) 成功率，均在 25 项任务上取平均（虚线：y = x）。(c) 分别依据仿真中与真实世界 A/B 评测中的成对结果拟合的 Bradley-Terry Elo 评分（虚线：最小二乘拟合，因为两套 Elo 尺度不同）。r：Pearson 相关系数，𝜌：Spearman 秩相关系数，MMRV：平均最大秩违例（mean maximum rank violation）。每个点都是针对 YAM 本体训练的 GR00T 2 通用检查点。

<a id="S407"></a>
**Source:** p.21 S407

**Original:** 4.5.1. Real-to-Sim Task Construction

**中文:** 4.5.1. 现实到仿真（real-to-sim）的任务构建

<a id="S408"></a>
**Source:** p.21 S408

**Original:** We recreate in simulation the real-world tasks used to develop GR00T 2, from general manipulation tasks evaluated zero-shot to multi-stage assembly, with rigid and articulated objects, deformable materials, and particles (Fig. 17). The aim is to reproduce both the visual setup and the physical interactions that determine whether a task succeeds. Agent-assisted workflows build the environments: agents use inputs such as real robot videos, 3D scans, and photographs, along with tools from SimFoundry (Ranawaka et al., 2026), to handle scene and asset reconstruction, including geometry, appearance, and collision modeling. Human experts review the resulting content and provide feedback to guide refinement. The simulation environments run in Isaac Lab Arena (NVIDIA Isaac Lab-Arena Contributors, 2025) on Newton (The Newton Contributors, 2025) with the MuJoCo Warp solver (Google DeepMind and NVIDIA, 2025). Environments are validated through several means including grasp and drop tests (for assets), replaying real robot demonstrations, and for assembly environments, testing assembly without a robot (Sec. J.1). For the humanoid, a separate motion-centric pipeline turns teleoperated whole-body motions into simulated demonstrations (Sec. 3.5).

**中文:** 我们在仿真中复现了用于开发 GR00T 2 的真实任务，既包括以零样本方式评测的通用操作任务，也包括多阶段装配任务，涉及刚性与铰接物体、可形变材料和粒子（见 Fig. 17）。目标是同时复现视觉布置与决定任务能否成功的物理交互。智能体辅助的工作流负责构建环境：智能体利用真实机器人视频、3D 扫描和照片等输入，并借助 SimFoundry（Ranawaka et al., 2026）的工具，完成场景与资产重建，包括几何、外观和碰撞建模。人类专家审核生成的内容，并提供反馈以指导修正。仿真环境在 Newton（The Newton Contributors, 2025）上通过 Isaac Lab Arena（NVIDIA Isaac Lab-Arena Contributors, 2025）运行，求解器为 MuJoCo Warp（Google DeepMind and NVIDIA, 2025）。环境通过多种方式验证，包括针对资产的抓取与跌落测试、回放真实机器人演示，以及对于装配环境，在不使用机器人的情况下测试装配过程（见 Sec. J.1）。对于人形机器人，一条独立的、以运动为中心的流程将遥操作的全身运动转换为仿真演示（见 Sec. 3.5）。

<a id="S409"></a>
**Source:** p.21 S409

**Original:** 4.5.2. Simulation as a Proxy for Real-World Evaluation

**中文:** 4.5.2. 以仿真作为真实世界评测的代理

<a id="S410"></a>
**Source:** p.21 S410

**Original:** Policies trained on real data are evaluated in these environments directly, without fine-tuning or co-training on simulation data. On 25 YAM tasks, 14 GR00T 2 checkpoints evaluated in both settings, with 5 blinded A/B trials on the real robot and 10 simulated trials per task, give Pearson correlations of 0.93 for task progress, 0.92 for success rate, and 0.93 for Bradley-Terry Elo ratings. These values are 95 to 99% of the correlation that a perfect simulator would reach with the same number of trials (Figs. 18 and 65). Environments reconstructed from DROID setups reach 0.98, 0.95, and 0.97 for five generalist checkpoints. This calibration makes simulation a development tool: during pretraining, simulated evaluations tracked intermediate checkpoints and narrowed the final model candidates to three, which we then compared on real robots. We tested changes to the data pipeline, such as sequence packing and mixed-shard sampling, with small-scale training and closed-loop simulation before adopting them in pretraining. Inference settings were screened in simulation before robot tests. Beyond success rate, simulation testing revealed how inference settings affect motion smoothness, and we confirmed this finding in physical trials. Simulation also served to develop the agent’s recovery skills on the toy plane assembly task (Sec. 3.4). While physical-robot evaluation remains the final validation for every design choice (Sec. J.2), simulation evaluation significantly increased development speed and iteration frequency.

**中文:** 训练于真实数据的策略直接在这些环境中评测，无需在仿真数据上进行微调或联合训练。在 25 项 YAM 任务上，14 个 GR00T 2 检查点在两种设置下均进行了评测：每项任务在真机上进行 5 次盲测 A/B 试验，仿真中进行 10 次试验，所得任务进度的 Pearson 相关系数为 0.93，成功率为 0.92，Bradley-Terry Elo 评分为 0.93。这些数值达到了使用相同试验次数时，完美仿真器所能达到相关性的 95% 至 99%（见 Figs. 18 和 65）。从 DROID 设置复现的环境，对五个通用检查点的相关系数分别为 0.98、0.95 和 0.97。这一校准使仿真成为一种开发工具：在预训练期间，仿真评测跟踪了中间检查点，并将最终模型候选缩小到三个，随后我们在真实机器人上对这三个候选进行了比较。在预训练中采纳数据流程的改动之前，例如序列打包（sequence packing）与混合分片采样（mixed-shard sampling），我们先用小规模训练和闭环仿真对其进行了测试。推理设置在真机测试之前已在仿真中筛选。除成功率外，仿真测试还揭示了推理设置如何影响动作平滑度，我们在实机试验中证实了这一发现。仿真还用于在玩具飞机装配任务上开发智能体的恢复技能（见 Sec. 3.4）。尽管实机评测仍是每项设计选择的最终验证（见 Sec. J.2），仿真评测显著提高了开发速度和迭代频率。

<a id="S412"></a>
**Source:** p.22 S412

**Original:** 4.5.3. Neural Simulation

**中文:** 4.5.3. 神经仿真

<a id="S413"></a>
**Source:** p.22 S413

**Original:** Physics simulation requires reconstructing each task, whereas a learned world model can be built from recorded robot interaction. We turn DreamDojo (Gao et al., 2026), a world model initialized from pretrained video priors, into an environment in which GR00T 2 collects RL experience (Sec. 4.1). DreamDojo is first mid-trained on multi-view robot episodes, 8,310 from YAM (about 227 hours, including failed attempts and recoveries) and 57,773 from DROID (about 273 hours), with the camera views tiled into one video canvas so that they are predicted jointly. It is then adapted to the target tasks from a few hundred successful and failed rollouts of the initial policy per task. In closed loop, GR00T 2 predicts an action chunk, the world model predicts the multi-view frames that result from executing it, and these frames become GR00T 2’s next observation. The world model carries its history in latent space, and the last commanded action stands in for the robot state. Because each episode chains many short predictions, the world model conditions on its own imperfect outputs. For the model used in RoboLab, perturbing the conditioning latents with noise during training exposes it to such histories. Rewards come from compact video classifiers that detect task success, trained offline on labels that a vision-language model proposes and humans review. A sparse success reward is used because dense progress scores are expensive to annotate and can be exploited by the policy. RL in this environment raises the success of GR00T 2 from 43% to 72% on average over four real-world tasks (peg insertion, rack-hole insertion, and bun placement on two cups; Fig. 52) and from 51% to 71% on ten RoboLab tasks, both measured outside the learned environment (Sec. F.5).

**中文:** 物理仿真需要对每项任务分别进行重建，而学习得到的世界模型可以从录制的机器人交互数据中构建。我们将 DreamDojo（Gao et al., 2026）改造为一个环境，GR00T 2 在其中收集强化学习（RL）经验（见 Sec. 4.1）。DreamDojo 是一个以预训练视频先验初始化的世界模型，首先在多视角机器人回合（episode）上进行中期训练：来自 YAM 的 8,310 个回合（约 227 小时，包括失败尝试与恢复过程），以及来自 DROID 的 57,773 个回合（约 273 小时）。各相机视角被平铺到一张视频画布（video canvas）上，从而被联合预测。随后，针对每项目标任务，使用初始策略的数百条成功与失败轨迹采样（rollout）对其进行适配。在闭环中，GR00T 2 预测一个动作块，世界模型预测执行该动作块所产生的多视角帧，这些帧随即成为 GR00T 2 的下一次观测。世界模型在潜空间中保存其历史，并以最后一条下发的动作代替机器人状态。由于每个回合都由许多短预测串联而成，世界模型会以自身不完美的输出作为条件。对于 RoboLab 中使用的模型，训练时对条件潜变量施加噪声扰动，使其接触到此类历史。奖励来自紧凑的视频分类器，它们用于检测任务是否成功，并在离线状态下训练，标签由视觉语言模型（VLM）提出、经人工审核。之所以采用稀疏的成功奖励，是因为稠密的进度评分标注成本高，并且可能被策略利用。在该环境中进行强化学习后，GR00T 2 在四项真实任务（插销插入 peg insertion、机架孔插入 rack-hole insertion，以及将面包卷 bun 放置于两个杯子上；见 Fig. 52）上的平均成功率从 43% 提升至 72%，在十项 RoboLab 任务上则从 51% 提升至 71%。两项结果均在学习得到的环境之外测得（见 Sec. F.5）。

<a id="S414"></a>
**Source:** p.22 S414

**Original:** 4.5.4. Simulation Benchmarks

**中文:** 4.5.4. 仿真基准测试

<a id="S415"></a>
**Source:** p.22 S415

**Original:** We evaluate GR00T 2 on five public benchmarks with their official task sets, episode budgets, and success criteria, using for each a single checkpoint post-trained from the same pretrained model (Sec. J.3). Baseline results are taken from the official leaderboards as of November 6, 2026, except GR00T 1.7, which we retrain and evaluate ourselves. Among VLA and WAM policies on the public leaderboards, GR00T 2 achieves the highest success rate on RoboCasa365 (Nasiriany et al., 2026), a single-arm mobile manipulation benchmark (67.2%, 2.8 points above the best prior entry), and on RoboDojo (Chen et al., 2026a), a bimanual benchmark (35.5%). On RoboLab (Yang et al., 2026) and MolmoSpaces (Kim et al., 2026), it places third (47.4%) and second (45.1%) after post-training only on real DROID data, so both evaluations are zero-shot real-to-sim transfer. On the G1 Factory humanoid benchmark (NVIDIA, 2026c), it reaches 84.7% success against 69.4% for GR00T 1.7. With RL post-training and agentic execution, GR00T 2 ranks first on the RoboCasa365 and RoboDojo leaderboards, the latter evaluated on one of its three official layout banks (Sec. 3.4 and Tab. 19).

**中文:** 我们在五个公开基准测试上评估 GR00T 2，每个基准测试都使用其官方任务集、回合预算和成功标准，并且每个基准测试都使用由同一预训练模型后训练得到的单个检查点（见 Sec. J.3）。基线结果取自截至 2026 年 11 月 6 日的官方排行榜，GR00T 1.7 除外，它由我们自行重新训练并评测。在公开排行榜上的 VLA 与 WAM 策略中，GR00T 2 在 RoboCasa365（Nasiriany et al., 2026）上取得最高成功率，该基准为单臂移动操作基准测试，成功率为 67.2%，比此前最佳记录高出 2.8 个百分点；在 RoboDojo（Chen et al., 2026a）上，这一双臂基准测试的成功率为 35.5%。在 RoboLab（Yang et al., 2026）和 MolmoSpaces（Kim et al., 2026）上，GR00T 2 分别排名第三（47.4%）和第二（45.1%），且仅在真实 DROID 数据上进行后训练，因此这两项评测都属于零样本的真实到仿真迁移。在 G1 Factory 人形机器人基准测试（NVIDIA, 2026c）上，它的成功率达到 84.7%，而 GR00T 1.7 为 69.4%。借助强化学习后训练与智能体化执行，GR00T 2 在 RoboCasa365 和 RoboDojo 排行榜上排名第一，其中后者的评测在其三个官方布局库（layout bank）之一上进行（见 Sec. 3.4 与 Tab. 19）。


<a id="H16"></a>
### 4.6. Deployment and Real-Time Inference ｜ 4.6. 部署与实时推理

<a id="S417"></a>
**Source:** p.22 S417

**Original:** Deployment requires timely predictions, continuous motion, and efficient task completion, both on workstation GPUs and on edge hardware with limited compute, memory, and power. Compared with VLA policies, these requirements are more difficult to meet for a world-action model: GR00T 2 encodes multi-camera video and

**中文:** 部署需要及时的预测、连续的运动以及高效的任务完成，无论是在工作站 GPU 上，还是在算力、内存与功耗都有限的边缘硬件上。与 VLA 策略相比，这些要求对世界-动作模型而言更难满足：GR00T 2 对多相机视频和

<a id="C020"></a>
**Source:** p.23 C020 · 图 F019

![F019](assets/F019.png)

**Original (caption):** Figure 19: Model-prediction latency for GR00T 2 Turbo on G1 using (a) a GeForce RTX 5090 and (b) Jetson Thor in 120 W mode. Bars show medians of 500 predictions after 20 warmup requests, using the same checkpoint weights and input observations. The panels use independent horizontal scales. Denoising-step tuning changes 2v4a to 1v2a.

**中文图注：** 图 19：GR00T 2 Turbo 在 G1 上的模型预测时延，分别使用 (a) GeForce RTX 5090 和 (b) 处于 120 W 模式的 Jetson Thor。柱状图为 500 次预测的中位数，预测前先进行 20 次预热请求，所用检查点权重与输入观测相同。两个子图使用各自独立的水平刻度。去噪步数调优会将 2v4a 改为 1v2a。

<a id="S440"></a>
**Source:** p.23 S440

**Original:** iteratively denoises video and action latents, and in our setting it incurs higher inference latency. We address them with accelerated inference (Sec. 4.6.1), training-time real-time chunking for smooth execution under the remaining delay (Sec. 4.6.2), and phase-conditioned action chunk transforms that enables faster than demonstration task completion throughput (Sec. 4.6.3).

**中文:** 迭代地对视频与动作潜变量进行去噪，在我们的设定中，这会带来更高的推理时延。我们通过加速推理（Sec. 4.6.1）、在剩余时延下实现平滑执行的训练时实时分块（Sec. 4.6.2），以及能够实现快于演示的任务完成吞吐量的阶段条件化动作块变换（Sec. 4.6.3）来应对这些问题。

<a id="S441"></a>
**Source:** p.23 S441

**Original:** 4.6.1. Policy Serving and Accelerated Inference

**中文:** 4.6.1. 策略服务与加速推理

<a id="S442"></a>
**Source:** p.23 S442

**Original:** GR00T 2 is served through a client-server interface: a robot client sends the camera history, robot state, and instruction, and the server returns an action chunk, which the client buffers and executes at the controller’s rate while it requests the next one (Sec. K.5). The server first removes repeated computation. It reuses the text features while the instruction is unchanged, precomputes the timestep conditioning, and lets action-only denoising steps reuse the attention keys and values of the latest video step. It then compiles the video encoder and the transformer into TensorRT engines replayed with CUDA graphs, for supported checkpoints applies FP8 to selected projection and feed-forward layers after calibration on robot observations, and reduces the number of denoising steps where task success and smoothness allow. On the serving path, streaming and prefetching move video encoding ahead of the prediction request. For GR00T 2 Turbo on the G1, TensorRT compilation gives the largest single reduction on both GPUs (Fig. 19). Together, these optimizations reduce median prediction latency by 2.9× to 7.2× relative to eager BF16 execution of the same checkpoint (Tab. 27). On a DGX Station GB300, GR00T 2 predicts in 48 ms on Dexter and 54 ms on YAM, with video encoding prefetched. For the Unitree G1, GR00T 2 Turbo predicts in 38 ms on a GeForce RTX 5090 and in 124 ms on the robot’s onboard Jetson Thor, where it plans 1.6 s chunks of whole-body motion tokens about once per second for the SONIC controller to execute at 50 Hz (Fig. 9). Numerical comparisons with eager BF16 execution help identify changes in predicted actions, but prediction error alone does not establish task success in closed-loop control. We make deployment decisions to screen inference changes and make deployment decisions through evaluation on the physical robot, considering task success, completion time, and motion quality together (Sec. I.1).

**中文:** GR00T 2 通过客户端-服务器接口提供服务：机器人客户端发送相机历史、机器人状态和指令，服务器返回一个动作块，客户端将其缓存并以控制器的频率执行，同时请求下一个动作块（Sec. K.5）。服务器首先消除重复计算：指令不变时复用文本特征，预先计算时间步条件，并让仅动作的去噪步复用最新视频步的注意力 key 与 value。随后，它将视频编码器和 Transformer 编译为 TensorRT 引擎，并通过 CUDA graph 回放；对于支持的检查点，在使用机器人观测完成校准后，对选定的投影层和前馈层应用 FP8；并在任务成功率与运动平滑性允许的情况下减少去噪步数。在服务路径上，流式传输与预取会把视频编码提前到预测请求之前完成。对于 G1 上的 GR00T 2 Turbo，TensorRT 编译在两种 GPU 上都带来了最大的单项降幅（图 19）。综合这些优化，相较于同一检查点的 eager BF16 执行，中位预测时延降低了 2.9× 至 7.2×（表 27）。在 DGX Station GB300 上，GR00T 2 在 Dexter 上的预测耗时为 48 ms，在 YAM 上为 54 ms（视频编码已预取）。对于 Unitree G1，GR00T 2 Turbo 在 GeForce RTX 5090 上的预测耗时为 38 ms，在机器人自带的 Jetson Thor 上为 124 ms；后者约每秒规划一次 1.6 s 的全身运动 token 块，由 SONIC 控制器以 50 Hz 执行（图 9）。与 eager BF16 执行的数值比较有助于识别预测动作的变化，但在闭环控制中，仅凭预测误差无法证明任务成功。我们借助数值比较来筛查推理变更，并通过实体机器人上的评测做出部署决策，同时综合考虑任务成功率、完成时间与运动质量（Sec. I.1）。

<a id="S443"></a>
**Source:** p.23 S443

**Original:** 4.6.2. Smooth Execution with Real-Time Chunking

**中文:** 4.6.2. 借助实时分块实现平滑执行

<a id="S444"></a>
**Source:** p.23 S444

**Original:** Some delay remains after acceleration, and the robot must keep moving while the next chunk is computed. Waiting for each prediction interrupts the motion, and executing predictions asynchronously without accounting for the delay creates discontinuities between successive chunks. Training-time real-time chunking (RTC) (Black et al., 2025) conditions each prediction on the prefix of actions already committed for execution. In our setting, conditioning on a clean prefix improves continuity but lowers task success at the shorter delay. We therefore use noisy-prefix RTC: during fine-tuning, the conditioning prefix is perturbed with Gaussian noise, which is intended to reduce reliance on the previous plan while retaining the context needed for a smooth continuation,

**中文:** 加速之后仍存在一定时延，而机器人必须在计算下一个动作块的同时持续运动。等待每次预测会打断运动，而在不考虑时延的情况下异步执行预测，则会使相邻动作块之间出现不连续。训练时实时分块（RTC）（Black et al., 2025）让每次预测以已确定用于执行的动作前缀为条件。在我们的设定中，以干净前缀为条件可以改善连续性，但在较短时延下会降低任务成功率。因此，我们采用带噪前缀实时分块（noisy-prefix RTC）：在微调期间，条件前缀被施加高斯噪声扰动，目的是在保留平滑衔接所需上下文的同时，降低对先前规划的依赖，

<a id="C021"></a>
**Source:** p.24 C021 · 图 F020

![F020](assets/F020.png)

**Original (caption):** Figure 20: Phase-conditioned task-completion throughput acceleration of GR00T 2. GR00T 2 predicts a future action chunk, while a subtask predictor identifies its task phases. Using a phase-specific speed schedule, we transform the original action chunk to accelerate execution and boost task-completion throughput while preserving success rates.

**中文图注：** 图 20：GR00T 2 的阶段条件化任务完成吞吐量加速。GR00T 2 预测未来的一个动作块，同时子任务预测器识别其所处的任务阶段。借助阶段特定的速度调度，我们对原始动作块进行变换，在保持成功率的同时加快执行并提升任务完成吞吐量。

<a id="S456"></a>
**Source:** p.24 S456

**Original:** and at inference the policy conditions on the clean committed actions. A short fine-tuning stage of 5k steps on a post-trained policy captures most of the continuity benefit, so RTC does not require repeating the full training pipeline. On eight RoboDojo precision tasks with simulated inference delays, noisy-prefix RTC raises success over asynchronous execution of the same weights from 32.8% to 34.8% at a 160 ms delay and from 15.0% to 21.4% at 320 ms. It reduces peak commanded jerk by 69% at 160 ms and the 95th-percentile cross-chunk jerk by 87% at 320 ms, whereas clean-prefix RTC lowers success at 160 ms to 30.7% (Sec. I.2).

**中文:** 而在推理时，策略以干净的已提交动作为条件。在经过后训练的策略上进行 5k 步的短程微调，即可获得大部分连续性收益，因此 RTC 无需重复完整的训练流程。在八个带模拟推理时延的 RoboDojo 精细任务上，相较于使用同一权重的异步执行，带噪前缀 RTC 将 160 ms 时延下的成功率从 32.8% 提升至 34.8%，将 320 ms 时延下的成功率从 15.0% 提升至 21.4%。在 160 ms 时延下，它使峰值指令加加速度（jerk）降低 69%；在 320 ms 时延下，它使跨块加加速度的第 95 百分位数降低 87%。相比之下，干净前缀 RTC 在 160 ms 时延下的成功率降至 30.7%（Sec. I.2）。

<a id="S457"></a>
**Source:** p.24 S457

**Original:** 4.6.3. Accelerating Task Throughput Beyond Demonstrations

**中文:** 4.6.3. 超越演示的任务吞吐量加速

<a id="S458"></a>
**Source:** p.24 S458

**Original:** Continuous execution and low latency do not by themselves boost task completion throughput, which remains bound to the pace of the demonstrations. We therefore retime GR00T 2’s action chunks by task phase. A task is decomposed into semantically meaningful phases, such as reaching, grasping, transporting, and screwing, which tolerate different degrees of acceleration. An agent searches for a per-phase speed schedule by evaluating accelerated rollouts and refining the schedule after observed failures. At deployment, a lightweight subtask predictor, trained on phase annotations generated by an agent, predicts from the current observation the phases spanned by each action chunk, and the chunk is retimed according to the schedule (Fig. 20). Because retiming changes the timing between successive chunks, temporal chunk alignment and cross-chunk jerk smoothing keep the execution continuous (Sec. I.3).

**中文:** 连续执行与低时延本身并不能提升任务完成吞吐量，后者仍受限于演示的节奏。因此，我们按任务阶段对 GR00T 2 的动作块进行时间重标定。任务被分解为若干语义上有意义的阶段，例如接近、抓取、搬运和拧螺丝，这些阶段能够容忍不同程度的加速。智能体通过评估加速后的 rollout（轨迹采样），并在观察到失败后细化调度，为每个阶段搜索逐阶段的速度调度。部署时，一个轻量级子任务预测器根据当前观测预测每个动作块所覆盖的阶段；该预测器基于由智能体生成的阶段标注训练。随后，动作块按照调度进行重标定（图 20）。由于重标定会改变相邻块之间的时间关系，时间块对齐与跨块加加速度平滑可以保证执行的连续性（Sec. I.3）。

<a id="H17"></a>
### 4.7. Infrastructure ｜ 4.7. 基础设施

<a id="S459"></a>
**Source:** p.24 S459

**Original:** Training GR00T 2 runs a joint video-action model over multi-camera video from human, UMI, and robot sources. Its infrastructure must provide the memory and compute for this model at scale, deliver decoded video windows to every GPU without stalling synchronous training, and turn raw recordings into training-ready data at the scale of the pretraining corpus. We describe the pretraining compute and distributed training runtime (Sec. 4.7.1), the training data loader (Sec. 4.7.2), and the multimodal data processing pipeline (Sec. 4.7.3).

**中文:** GR00T 2 的训练运行一个联合视频-动作模型，其输入来自人类、UMI 与机器人等多个来源的多相机视频。其基础设施必须为这一规模的模型提供所需的内存与算力，将解码后的视频窗口送达每个 GPU 而不阻塞同步训练，并将原始录制数据转换为可直接用于训练的数据，且规模要与预训练语料相当。我们依次介绍预训练算力与分布式训练运行时（Sec. 4.7.1）、训练数据加载器（Sec. 4.7.2）以及多模态数据处理流水线（Sec. 4.7.3）。

<a id="S460"></a>
**Source:** p.24 S460

**Original:** Policy serving is described with deployment (Sec. 4.6.1), and the online RL infrastructure with RL post-training (Sec. 4.1).

**中文:** 策略服务在部署部分中说明（Sec. 4.6.1），在线 RL 基础设施则在 RL 后训练部分中说明（Sec. 4.1）。

<a id="S461"></a>
**Source:** p.24 S461

**Original:** 4.7.1. Pretraining Compute and Distributed Training

**中文:** 4.7.1. 预训练算力与分布式训练

<a id="S462"></a>
**Source:** p.24 S462

**Original:** GR00T 2 is pretrained on NVIDIA GB300 NVL72 systems, chosen for GPU memory capacity, Tensor Core throughput, and acceleration of collective communication. Each Blackwell Ultra GPU provides up to 288 GB of HBM3e with 8 TB/s of bandwidth and about 2.5 PFLOPS of dense BF16/FP16 Tensor Core compute. A rack connects 72 GPUs into one NVLink domain with 1.8 TB/s of bidirectional bandwidth per GPU, in which NVLink SHARP offloads reductions to the switches, and racks communicate over a RoCE fabric with one 800 Gb/s ConnectX-8 SuperNIC per GPU. The cluster has 2,016 GPUs in 28 racks, and the main pretraining run used 1,024 of them, while the rest ran other training experiments concurrently (Sec. K.2.1).

**中文:** GR00T 2 在 NVIDIA GB300 NVL72 系统上进行预训练，选择该平台是因为其 GPU 显存容量、Tensor Core 吞吐量以及对集合通信的加速能力。每块 Blackwell Ultra GPU 提供最高 288 GB 的 HBM3e 显存，带宽为 8 TB/s，并具有约 2.5 PFLOPS 的稠密 BF16/FP16 Tensor Core 算力。一个机架将 72 块 GPU 连接为一个 NVLink 域，每块 GPU 的双向带宽为 1.8 TB/s，其中 NVLink SHARP 将归约操作卸载到交换机上；机架之间则通过 RoCE 网络互连，每块 GPU 配备一块 800 Gb/s 的 ConnectX-8 SuperNIC。集群共有 2,016 块 GPU，分布在 28 个机架中，主预训练运行使用其中 1,024 块，其余 GPU 同时运行其他训练实验（Sec. K.2.1）。

<a id="S463"></a>
**Source:** p.25 S463

**Original:** Training uses synchronous data parallelism with DeepSpeed ZeRO-2: every GPU holds the full weights, gradients and optimizer state are partitioned across ranks, and BF16 gradient synchronization overlaps with computation. Because the model fits without pipeline parallelism, the GPU memory keeps the parameters, each rank’s optimizer partition, and the activations of a per-device batch of 16 resident, and the large per-device batch gives the Tensor Cores more matrix-multiplication work and amortizes kernel-launch overhead. Part of each step runs in frozen feature encoders rather than the trainable model. Depending on the recipe, the runtime uses TensorRT for video encoding, fused text-encoder operations, efficient attention kernels that keep the model’s masking rules, PyTorch compilation, and activation recomputation, and it can encode the next batch’s features while the current batch synchronizes gradients and updates the optimizer. We judge efficiency across the whole step, from input retrieval and feature encoding to gradient synchronization and the optimizer update. A hardware-counter-based utilization metric, Overall FLOP Utilization (Pedersen et al., 2026), is monitored alongside step time, but elapsed time and model quality decide whether a change is kept, since an optimization can shorten the step without moving the utilization signal (Sec. K.4).

**中文:** 训练采用同步数据并行与 DeepSpeed ZeRO-2：每块 GPU 持有完整权重，梯度与优化器状态在各 rank 之间分片，BF16 梯度同步与计算重叠进行。由于模型无需流水线并行即可装下，GPU 显存中常驻的内容包括参数、每个 rank 的优化器分片，以及每设备批量为 16 的激活值。这种较大的每设备批量能为 Tensor Core 提供更多矩阵乘法工作，并摊销内核启动开销。每一步的一部分计算在冻结的特征编码器中完成，而非在可训练模型中进行。根据训练配方的不同，运行时会使用 TensorRT 进行视频编码、融合文本编码器运算、保留模型掩码规则的高效注意力内核、PyTorch 编译以及激活重计算，并且可以在当前批次同步梯度、更新优化器的同时，对下一批次的特征进行编码。我们从整体上衡量每一步的效率，涵盖从输入读取、特征编码到梯度同步和优化器更新的全过程。我们同时监控一个基于硬件计数器的利用率指标，即整体 FLOP 利用率（Overall FLOP Utilization）（Pedersen et al., 2026），并与单步耗时一同观察；但是否保留某项改动，取决于实际耗时与模型质量，因为一项优化可能缩短单步耗时，却不会改变该利用率信号（Sec. K.4）。

<a id="S464"></a>
**Source:** p.25 S464

**Original:** 4.7.2. Training Data Loading

**中文:** 4.7.2. 训练数据加载

<a id="S465"></a>
**Source:** p.25 S465

**Original:** Training data are stored in LanceDS, built on the Lance columnar format (Pace et al., 2025; Lance Contributors, 2026). Each dataset holds a step table with state, actions, annotations, and quality-control (QC) signals, an episode table, and a media table with the original videos. Lance versioning preserves earlier snapshots when episodes are added or annotations and QC signals change, and new QC columns are added without rewriting existing ones. A training run pins one snapshot per dataset, so its data, normalization statistics, and metadata are reproduced together. All datasets share one schema, and the recipe’s embodiment tag selects at read time the state and action groups, cameras, annotations, and normalization statistics of that embodiment, as well as the model’s embodiment-specific projection layers. QC rules are not applied in the loading path: they are evaluated offline over the temporal window that each training sample reads, its observations and its action targets, and stored as views of the eligible sample starts. The views are rebuilt with every new snapshot and carry normalization statistics computed over the samples they keep. Sampling is drawn on demand from deterministic per-rank seeds and mixes shards so that each global step follows the recipe’s dataset proportions. Batch preparation runs in three asynchronous stages: video shards are prefetched from shared storage to node-local NVMe, frames are decoded (about 90% of preparation time in a three-view shard benchmark), and samples are augmented, collated, and copied to the GPU from pinned memory. Variable-length token packing reduces padding. Over 100 steady-state pretraining steps on 1,024 GB300 GPUs, reading 25 dataset stores with 15.6 million episode records and 46.2 billion time steps, the loader delivered about 12,000 sample windows per second, and the mean exposed wait for input was 0.37 ms (0.61 ms at the 99th percentile), or 0.049% of the measured step time (Tab. 35). These numbers characterize input delivery, not the model’s FLOP utilization. In the measured run, packing filled 94.5% of the positions in 32,768-token rows. Loader changes are validated in closed-loop simulation before adoption (Sec. 4.5.2), and Sec. K.4.3 details the loader.

**中文:** 训练数据存储在 LanceDS 中，它构建于 Lance 列式格式之上（Pace et al., 2025；Lance Contributors, 2026）。每个数据集包含一张 step 表（记录状态、动作、标注以及质量控制（QC）信号）、一张 episode 表，以及一张保存原始视频的 media 表。当新增 episode，或标注与 QC 信号发生变化时，Lance 版本管理会保留更早的快照；新增的 QC 列无需重写已有列。一次训练运行会为每个数据集固定一个快照，因此其数据、归一化统计量与元数据能够被一并复现。所有数据集共享同一套 schema，配方中的本体标签（embodiment tag）会在读取时选定该本体对应的状态与动作组、相机、标注和归一化统计量，以及模型中特定于本体的投影层。QC 规则不在加载路径中应用：它们以离线方式在每个训练样本所读取的时间窗口（即其观测与动作目标）上评估，并存储为合格样本起点的视图。每当生成新快照时，这些视图都会被重建，并携带基于其所保留样本计算的归一化统计量。采样按需从确定性的逐 rank 随机种子中抽取，并混合各分片，使每个全局步都遵循配方规定的数据集比例。批次准备分为三个异步阶段：视频分片从共享存储预取到节点本地 NVMe，帧被解码（在三视角分片基准测试中，解码约占准备时间的 90%），样本经过数据增广、整理（collate）后，从锁页内存复制到 GPU。变长 token 打包减少了填充。在 1,024 块 GB300 GPU 上进行的 100 个稳态预训练步中，加载器读取了 25 个数据集存储，共包含 1,560 万条 episode 记录和 462 亿个时间步，平均每秒交付约 12,000 个样本窗口；输入等待的平均暴露时间为 0.37 ms（第 99 百分位为 0.61 ms），占实测单步耗时的 0.049%（Tab. 35）。这些数字刻画的是输入交付的情况，而非模型的 FLOP 利用率。在实测运行中，打包使 32,768 token 行中 94.5% 的位置被填充。加载器的改动会先经闭环仿真验证再被采用（Sec. 4.5.2），Sec. K.4.3 则详细介绍了加载器。

<a id="S466"></a>
**Source:** p.25 S466

**Original:** 4.7.3. Multi-Modal Data Processing

**中文:** 4.7.3. 多模态数据处理

<a id="S467"></a>
**Source:** p.25 S467

**Original:** Before they can be loaded, raw human demonstration recordings are converted into training-ready data. Multi-camera video is retrieved, decoded, and resized. Motion records are transformed and, where needed, retargeted to the training hand representation. Observations, actions, and annotations are then aligned in time and packaged as indexed episodes in training-ready shards. The pipeline processes petabyte-scale input each month, with individual production jobs using nearly 10,000 vCPUs. The central difficulty is that these conversions share inputs and compete for limited working storage. A long video can contain many episodes, and one episode can depend on several camera files and separately stored motion records, so a shared input can be reclaimed only after its slowest consumer finishes, and a slow conversion or upload can block the retrieval of unrelated inputs and leave workers idle. The pipeline therefore ties the lifetime of each input to execution progress. Files stream from object storage directly to the processing nodes, without staging on a shared filesystem, so conversion starts before a collection has been fully retrieved. New inputs are admitted against each node’s storage budget, counting resident files, pending transfers, and output headroom, and work is dispatched to the node that holds its inputs. An episode releases its claim on an input only after its outputs are uploaded, so the completion of consumers, rather than prefetching, governs when new inputs enter. After an interruption, lost inputs are rebuilt through the same admission path, and durable checkpoints let the resumed job reuse completed conversions and published shards. In three production jobs on 100 nodes with 96 vCPUs each, the pipeline processed 722 to 780 demonstration-hours of recordings per hour, published the first training-ready shard within 28 minutes, and averaged 97.8% CPU utilization during conversion. Across five interrupted jobs, 92.4% of the completed conversion time went to work that did not have to be repeated, and publication resumed 2.4 to 5.3 minutes after a restart (Sec. K.6 and Tab. 36).

**中文:** 原始人类演示录制数据需先转换为可用于训练的数据，才能被加载。多相机视频被读取、解码并缩放。运动记录被变换，并在需要时重定向到训练所用的手部表示。随后，观测、动作与标注在时间上对齐，并作为带索引的 episode 打包成训练就绪的分片。该流水线每月处理 PB 级输入，单个生产作业使用接近 10,000 个 vCPU。核心难点在于，这些转换会共享输入，并争用有限的工作存储。一段长视频可能包含许多 episode，而一个 episode 可能依赖多个相机文件以及单独存储的运动记录，因此共享输入只有在其最慢的消费者完成后才能被回收；转换或上传缓慢还会阻塞无关输入的读取，使工作节点空转。为此，该流水线将每个输入的生命周期与执行进度绑定。文件直接从对象存储流式传输到处理节点，无需在共享文件系统上暂存，因此转换可以在一次采集完全读取之前就开始。新输入的准入需对照每个节点的存储预算进行判断，预算计入常驻文件、待处理传输以及输出余量；工作则被分派到持有其输入的节点。一个 episode 只有在其输出上传完成后才释放对某个输入的占用，因此新输入何时进入，取决于消费者的完成情况，而非预取。中断之后，丢失的输入会通过同一准入路径重新构建；持久化检查点则让恢复后的作业能够复用已完成的转换与已发布的分片。在 100 个节点（每节点 96 个 vCPU）上的三个生产作业中，该流水线每小时处理 722 至 780 个演示小时的录制数据，在 28 分钟内发布了第一个训练就绪分片，转换期间的 CPU 平均利用率为 97.8%。在五次中断的作业中，已完成的转换时间中有 92.4% 用于不必重复的工作，重启后发布恢复耗时 2.4 至 5.3 分钟（Sec. K.6 与 Tab. 36）。


<a id="H18"></a>
### 5. Conclusion and Open Problems ｜ 结论与开放问题

<a id="S469"></a>
**Source:** p.26 S469

**Original:** GR00T 2 is a world-action model: a single 2B-parameter transformer that predicts future observations and robot actions together, pretrained on egocentric human video, handheld UMI demonstrations, and teleoperation of gripper arms, dexterous hands, and a humanoid. Predicting the future gives all of these sources a common objective, including human video that carries no robot actions. On 50 dexterous tasks new to the robot, the resulting model succeeds zero-shot in 40% of trials and reaches 95% with five demonstrations (Sec. 3.1). It learns robot tasks without teleoperated demonstrations of those tasks (Sec. 3.2). Real-world RL raises its success on contact-rich skills to 88 to 98% (Sec. 3.3). With corrective data and a frontier agent, it completes cluttered long-horizon assemblies in at least 97% of trials (Sec. 3.4). GR00T 2 Turbo runs onboard a humanoid and directs a learned whole-body controller (Sec. 3.5).

**中文:** GR00T 2 是一个世界-动作模型（WAM）：一个 20 亿参数的单一 Transformer，它同时预测未来观测与机器人动作，并在第一人称视角（egocentric）人类视频、手持 UMI 演示数据，以及夹爪机械臂、灵巧手和人形机器人的遥操作数据上完成预训练。预测未来为所有这些数据源提供了统一的目标，其中也包括不含机器人动作的人类视频。在 50 项对该机器人而言属于新任务的灵巧操作任务上，模型零样本成功率为 40%，使用五条演示后达到 95%（Sec. 3.1）。它无需该任务的遥操作演示即可学习机器人任务（Sec. 3.2）。真实世界强化学习（RL）将其在富接触技能上的成功率提升至 88% 至 98%（Sec. 3.3）。借助纠正性数据和前沿智能体，它能在杂乱的长时序装配任务中至少完成 97% 的试次（Sec. 3.4）。GR00T 2 Turbo 运行于机载人形机器人之上，并驱动一个习得的全身控制器（Sec. 3.5）。

<a id="S470"></a>
**Source:** p.26 S470

**Original:** Three observations from building GR00T 2 shape the problems that follow.

**中文:** 构建 GR00T 2 的过程中有三点观察，它们决定了下文讨论的问题。

<a id="S471"></a>
**Source:** p.26 S471

**Original:** • Much of what the robot learns need not come from robot data. Robot success on new tasks more than doubles with human video in pretraining and does not level off at the largest scale we tested (Fig. 10). For glove and Gripper UMI demonstrations, task-agnostic data from the target robot specify the embodiment, while the demonstrations specify the task (Sec. 3.2). • Reliability comes from complementary mechanisms, not from pretraining alone. Pretraining provides breadth. Corrective demonstrations and RL close gaps in precision and contact. The agent supplies memory, verification, and recovery over long horizons. • Progress depended on measurement. Blinded head-to-head evaluation and calibrated simulation (Sec. 4.3 and 4.5.2) turned close comparisons into decisions.

**中文:** • 机器人学到的许多东西不必来自机器人数据。在预训练中加入人类视频后，机器人在新任务上的成功率增长超过一倍，并且在我们测试的最大规模下仍未趋于平缓（图 10）。对于手套式与 Gripper UMI 演示数据，来自目标机器人的任务无关数据界定本体，而演示数据界定任务（Sec. 3.2）。• 可靠性来自互补机制，而不仅仅来自预训练。预训练提供广度，纠正性演示与强化学习则弥补精度和接触方面的差距。智能体负责长时序任务中的记忆、验证与恢复。• 进展依赖于测量。盲法的两两直接评测与经过校准的仿真（Sec. 4.3 和 4.5.2）把接近的比较变成了明确的结论。

<a id="S472"></a>
**Source:** p.26 S472

**Original:** Each observation also points to problems that remain open. We group them by part of the robot learning system, and start each group from the basic constraint that makes it hard.

**中文:** 每一条观察也指向仍然开放的问题。我们按机器人学习系统的组成部分对这些问题分组，并从使每组问题变得困难的基本约束出发展开讨论。

<a id="S473"></a>
**Source:** p.26 S473

**Original:** Model. A robot policy learns from data dominated by observation rather than action, and it must act at the rate of the physical world. Joint video-action prediction turns every video into supervision, but most of the tokens it predicts encode future video, much of which does not bear on the next action. GR00T 2 Turbo predicts a spatial latent grid four times smaller than that of GR00T 2. After post-training, it loses 6.7 points of success on YAM but half of its success on dexterous tasks, falling from 68.6% to 34.3% (Tab. 1). The comparison does not isolate the cause, but it suggests that the visual detail a policy must predict depends on the task and the embodiment. Four questions follow.

**中文:** 模型。机器人策略从以观测为主而非以动作为主的数据中学习，并且必须以物理世界的速率行动。联合的视频-动作预测把每一段视频都变成了监督信号，但它所预测的 token 大多编码未来视频，其中许多与下一步动作无关。GR00T 2 Turbo 所预测的空间潜变量网格，比 GR00T 2 的小四倍。经过后训练后，它在 YAM 上的成功率下降 6.7 个百分点，而在灵巧任务上的成功率则下降了一半，从 68.6% 降至 34.3%（Tab. 1）。该比较并未分离出原因，但它表明策略必须预测的视觉细节取决于任务与本体。由此引出四个问题。

<a id="S474"></a>
**Source:** p.26 S474

**Original:** • What to predict. It is unknown which aspects of the future a policy should predict, and at what resolution and horizon. It is also unclear whether prediction helps mainly as a training signal or also as imagination at inference time. • Memory. GR00T 2 observes 0.8 s of history, and tasks that require memory are delegated to the agent (Sec. 3.4). In imitation learning, longer raw context can invite shortcuts such as copying past ac- tions (de Haan et al., 2019; Wen et al., 2020), which suggests that memory should be structured rather than simply longer. • Force and touch. GR00T 2 handles force only as an output: from DexUMI demonstrations, it predicts joint torques that set the hand’s compliance (Sec. 4.4.3). It does not take touch as input, and tactile recordings are scarce compared with video. How to add force and touch as inputs without eroding visual priors, and at which control rate, is open. • Interfaces in the control hierarchy. Image-space points tell GR00T 2 where to act but not how, so requirements such as pouring or scooping still rest on language and learned skills (Sec. 3.4). Below GR00T 2 Turbo, the interface to SONIC is a motion latent decoded into joint position targets (Sec. 3.5), so contact force is not represented explicitly. Which representation should pass between reasoning, policy, and controller, and how it transfers to new embodiments, is unsettled.

**中文:** • 预测什么。目前尚不清楚策略应预测未来的哪些方面，以及应以何种分辨率和时间跨度进行预测。同样不清楚的是，预测主要是作为训练信号起作用，还是在推理时也起到“想象”的作用。• 记忆。GR00T 2 只观察 0.8 秒的历史，需要记忆的任务则交由智能体处理（Sec. 3.4）。在模仿学习中，更长的原始上下文可能诱发捷径，例如复制过去的动作（de Haan et al., 2019; Wen et al., 2020），这表明记忆应当是结构化的，而不只是简单地加长。• 力与触觉。GR00T 2 仅把力当作输出处理：利用 DexUMI 演示数据，它预测用于设定手部柔顺性（compliance）的关节力矩（Sec. 4.4.3）。它不接收触觉作为输入，而且与视频相比，触觉记录十分稀少。如何在不损害视觉先验的前提下把力和触觉作为输入加入，以及以何种控制频率加入，仍是开放问题。• 控制层级中的接口。图像空间中的点告诉 GR00T 2 去哪里行动，却没有告诉它如何行动，因此倒酒或舀取等要求仍然依赖语言和习得的技能（Sec. 3.4）。在 GR00T 2 Turbo 之下，与 SONIC 的接口是一个被解码为关节位置目标的运动潜变量（Sec. 3.5），因此接触力没有被显式表示。在推理、策略与控制器之间应传递何种表示，以及这种表示如何迁移到新本体，目前尚无定论。

<a id="S477"></a>
**Source:** p.27 S477

**Original:** Data. Every hour of robot data requires a robot and an operator, whereas human experience is abundant but recorded in a different body. GR00T 2 pretrains on about 400,000 hours of human video, 10,000 hours of UMI demonstrations, and 23,500 hours of teleoperation (Sec. 4.2). Human video brings coverage, UMI brings task-focused demonstrations in a robot-compatible format, and teleoperation grounds the embodiment.

**中文:** 数据。每一小时的机器人数据都需要一台机器人和一名操作员，而人类经验十分丰富，只是记录在另一种身体之中。GR00T 2 在约 400,000 小时的人类视频、10,000 小时的 UMI 演示数据和 23,500 小时的遥操作数据上进行预训练（Sec. 4.2）。人类视频带来覆盖面，UMI 以机器人兼容的格式提供聚焦任务的演示数据，遥操作则把模型锚定到本体上。

<a id="S478"></a>
**Source:** p.27 S478

**Original:** What is missing is an exchange rate between these sources. It is not known how much robot performance an hour of each source yields, or how that yield changes with the data already present. It is also not known how little target-robot data suffices to specify a new embodiment. Simulation raises the same question. Compute widens coverage, but agreement with the real world still requires measurement and robot time. The scaling with human video shows only that one of these rates is positive (Fig. 10). Until they are measured, collection budgets cannot be allocated on principle.

**中文:** 目前缺失的是这些数据源之间的“兑换率”。我们不知道每一小时的各类数据能带来多少机器人性能，也不知道这种产出如何随已有数据的多少而变化。我们同样不知道，至少需要多少目标机器人数据才能界定一种新本体。仿真也提出了同样的问题。算力能扩大覆盖范围，但要与真实世界保持一致，仍然需要测量和机器人时间。与人类视频相关的缩放结果只表明，其中一种兑换率为正（图 10）。在这些兑换率被测量之前，采集预算无法有原则地分配。

<a id="S479"></a>
**Source:** p.27 S479

**Original:** A second question is what makes data useful beyond its quantity. Demonstrations show mostly successful behavior, whereas RL, world models, and verifiers also need failures and recoveries; the world model we use for RL is trained on robot episodes that include both (Sec. 4.5.3). Labels of how well each demonstration was executed could serve as a further training signal.

**中文:** 第二个问题是：除了数量之外，是什么让数据变得有用。演示数据主要展示成功的行为，而强化学习、世界模型和验证器还需要失败与恢复的样本；我们用于强化学习的世界模型，正是在同时包含两者的机器人片段上训练的（Sec. 4.5.3）。记录每条演示执行质量的标签，还可以作为另一种训练信号。

<a id="S480"></a>
**Source:** p.27 S480

**Original:** Evaluation. A success rate measured on real robots is a binomial estimate, and its uncertainty shrinks only with the square root of the number of trials. Our post-training benchmarks use up to 20 trials per task (Tab. 1). That is enough to resolve the large gaps between GR00T 2 and its baselines, but not the differences that matter in deployment. Distinguishing 95% from 99% success takes about 285 trials per policy, and 99% from 99.9% more than 1,000.1 Absolute rates also drift with station, operator, and day, which is why we rank checkpoints by blinded head-to-head comparisons (Sec. 4.3). Even then, the independent units are tasks rather than trials, and 30 to 35% of comparisons are ties (Sec. D.7). Three directions follow.

**中文:** 评测。在真实机器人上测得的成功率是一个二项估计，其不确定性只按试次数平方根的速度缩小。我们的后训练基准每个任务最多使用 20 次试次（Tab. 1）。这足以分辨 GR00T 2 与其基线之间的大幅差距，但不足以分辨部署中真正重要的差异。要区分 95% 与 99% 的成功率，每个策略大约需要 285 次试次；要区分 99% 与 99.9%，则需要超过 1,000¹ 次。绝对成功率还会随工位、操作员和日期而漂移，这正是我们通过盲法两两直接比较来对检查点排序的原因（Sec. 4.3）。即便如此，独立单元是任务而非试次，而且 30% 至 35% 的比较结果是平局（Sec. D.7）。由此引出三个方向。

<a id="S481"></a>
**Source:** p.27 S481

**Original:** • Proxy evaluation at deployment scale. Across 25 YAM tasks, simulation predicts the real-robot task progress of 14 generalist checkpoints with a Pearson correlation of 0.93 (Sec. 4.5.2). It remains to be shown whether simulation is as predictive for contact-rich assembly, for RL-trained policies that exploit simulator errors, and for comparisons between training recipes rather than checkpoints. • Automated verification. In our long-horizon assemblies, three of the eight failures were screws left partly driven that both GR00T 2 and the agent judged complete (Sec. G.1). Verifying subtle physical state is a prerequisite for autonomous evaluation, for RL rewards, and for deciding when to ask a person for help. • Cost to reliability. Robot learning rarely reports the quantity that determines deployment: the robot time and human time needed to bring a new task to a target reliability. The same accounting, under matched budgets, would settle when RL is worth more than additional demonstrations or corrections.

**中文:** • 部署规模下的代理评测。在 25 个 YAM 任务上，仿真对 14 个通用检查点的真实机器人任务进度的预测，其皮尔逊相关系数（Pearson correlation）为 0.93（Sec. 4.5.2）。仍需证明的是：对于富接触装配、利用仿真器误差的强化学习策略，以及训练配方（而非检查点）之间的比较，仿真是否同样具有预测性。• 自动验证。在我们的长时序装配任务中，八次失败里有三次是螺丝拧入不完全，而 GR00T 2 与智能体都判定其已完成（Sec. G.1）。验证细微的物理状态，是自主评测、强化学习奖励以及判断何时向人求助的前提。• 成本与可靠性。机器人学习很少报告决定部署的那个量：把一项新任务提升到目标可靠性所需的机器人时间和人力时间。在预算匹配的条件下进行同样的核算，就能确定何时强化学习比额外的演示或纠正更有价值。

<a id="S482"></a>
**Source:** p.27 S482

**Original:** Hardware. A model can learn only what the hardware allows people to demonstrate, sensors to record, and robots to repeat. Our teleoperation cannot demonstrate fast, targeted motions such as the conveyor toss, which GR00T 2 learned from human demonstrations instead (Sec. 3.2). Capture devices that match the robot shrink the gap the model must bridge. DexUMI replicates the joints and contact surfaces of the robot hand, so on that hand its demonstrations need no robot play data (Sec. 4.4). This argues for designing robots and capture devices together, with shared kinematics, camera placement, and tactile formats.

**中文:** 硬件。模型只能学会硬件允许人们演示、传感器记录、机器人复现的内容。我们的遥操作无法演示传送带投掷这类快速、定向的动作，而 GR00T 2 是从人类演示中学会这一动作的（Sec. 3.2）。与机器人相匹配的采集设备可以缩小模型必须跨越的差距。DexUMI 复刻了机器人手的关节与接触面，因此在该手上，其演示数据无需机器人自由操作数据（robot play data）（Sec. 4.4）。这说明应当把机器人与采集设备一并设计，并共享运动学、相机布置和触觉格式。

<a id="S483"></a>
**Source:** p.27 S483

**Original:** 1Two-sided two-proportion 𝑧-test at significance level 0.05 with 80% power.

**中文:** 1 双侧双比例 𝑧 检验，显著性水平 0.05，检验效能 80%。

<a id="S484"></a>
**Source:** p.28 S484

**Original:** Learning from interaction makes further demands. Physical interaction and scene resets limit how fast realworld RL collects experience (Sec. F.3), so autonomous improvement needs stations that reset themselves, detect success, and withstand thousands of contact-rich attempts. Onboard compute and power, finally, bound the model itself: GR00T 2 Turbo exists because a humanoid must run its policy on an edge GPU (Sec. 2).

**中文:** 从交互中学习还会带来更多要求。物理交互与场景复位限制了真实世界强化学习收集经验的速度（Sec. F.3），因此自主改进需要能够自行复位、检测成功，并能承受数千次富接触尝试的工位。最后，机载算力与功耗限制了模型本身：GR00T 2 Turbo 之所以存在，是因为人形机器人必须在边缘 GPU 上运行其策略（Sec. 2）。

<a id="S485"></a>
**Source:** p.28 S485

**Original:** Infrastructure. Joint video-action training processes multi-camera video at every step, and video dominates the cost of storage, decoding, and computation. Pretraining GR00T 2 used 1,024 GB300 GPUs and a data pipeline that processes petabyte-scale input each month (Sec. 4.7). It is not yet known how world-action models scale with model size, data, and compute, or how compute should be divided between video and action prediction. Scaling laws of this kind, under the constraint that the deployed model must run in real time, would guide the design of the next model.

**中文:** 基础设施。联合视频-动作训练在每一步都要处理多路相机视频，而视频在存储、解码和计算成本中占主导地位。预训练 GR00T 2 使用了 1,024 块 GB300 GPU，以及一条每月处理 PB 级输入的数据流水线（Sec. 4.7）。目前尚不清楚世界-动作模型如何随模型规模、数据和算力而扩展，也不清楚算力应如何在视频预测与动作预测之间分配。在部署模型必须实时运行的约束下，这类缩放定律（scaling laws）将指导下一代模型的设计。

<a id="S486"></a>
**Source:** p.28 S486

**Original:** The larger shift is from offline to online learning. RL post-training already couples robots, training, and evaluation in one service that retains experience across interruptions (Sec. F.3). An agent found the basis of our RL recipe through about 35 days of autonomous experimentation in simulation (Sec. 4.1). Extending this loop from single stations to fleets requires infrastructure in which robot experience, simulation, and world-model rollouts feed training continuously while every model and dataset version stays reproducible.

**中文:** 更大的转变是从离线学习走向在线学习。强化学习后训练已经把机器人、训练和评测耦合在同一项服务中，并且能在中断之后保留经验（Sec. F.3）。一个智能体通过约 35 天的仿真自主实验，找到了我们强化学习方案的基础（Sec. 4.1）。要把这一闭环从单个工位扩展到机器人集群，需要这样一种基础设施：机器人经验、仿真以及世界模型的 rollout（轨迹采样）持续地输入训练，同时每个模型与数据集版本都保持可复现。

<a id="S487"></a>
**Source:** p.28 S487

**Original:** Deployment. The value of a deployed robot is set by how often it needs a person, how fast it works, and whether it is safe. GR00T 2 predicts an action chunk for Dexter in 153 ms on a GeForce RTX 5090 workstation GPU, and GR00T 2 Turbo predicts one for the G1 humanoid in 124 ms on its onboard Jetson Thor (median prediction latency, Sec. 2 and Tab. 27). Phase-conditioned retiming shortens mean completion time by 15 to 26% on three dexterous tasks (Tab. 29). Reliability is less settled. On long-horizon tasks, post-training reaches about 70% average success (Tab. 1). From cluttered starts, assembly success of at least 97% required corrective data and an agent that monitors and repairs (Sec. 3.4). That agent is slow relative to the policy. In visually steered trash sorting on YAM, a median agent turn takes 7.5 s against about 0.6 s per unaccelerated policy call, and the robot waits for the agent during a median 38% of an episode (Sec. G.2). Three problems stand out.

**中文:** 部署。已部署机器人的价值，取决于它需要人工介入的频率、工作速度以及是否安全。GR00T 2 在 GeForce RTX 5090 工作站 GPU 上为 Dexter 预测一个动作块，耗时 153 毫秒；GR00T 2 Turbo 则在其机载 Jetson Thor 上为 G1 人形机器人预测动作块，耗时 124 毫秒（预测延迟中位数，见 Sec. 2 与 Tab. 27）。相位条件重定时（phase-conditioned retiming）在三项灵巧任务上使平均完成时间缩短 15% 至 26%（Tab. 29）。可靠性方面则尚未定论。在长时序任务上，后训练的平均成功率约为 70%（Tab. 1）。从杂乱的初始状态开始，要达到至少 97% 的装配成功率，需要纠正数据以及一个能够监控并修复问题的智能体（Sec. 3.4）。该智能体相对于策略而言速度较慢。在 YAM 上进行视觉引导（visual steering）的垃圾分拣时，智能体单轮中位耗时 7.5 秒，而未经加速的单次策略调用约需 0.6 秒；机器人在一个回合中位数 38% 的时间里都在等待智能体（Sec. G.2）。有三个问题尤为突出。

<a id="S488"></a>
**Source:** p.28 S488

**Original:** • Routine improvement. RL and world-model training still require rollouts and adaptation for each task (Sec. 4.5.3). A loop in which deployment exposes failures, agents propose corrections, and successful behaviors are distilled back into the policy (Sec. G.3) would turn this per-task cost into a by-product of operation. • Latency across the hierarchy. Reasoning, verification, and recovery must move closer to the policy’s control rate, through faster agents, distilled verifiers, or a policy that absorbs recurring corrections. • Safe physical action. Safety training of language models constrains what they say, and it is not known to carry over to what a robot does. A policy that agents can steer needs its own checks on the physical consequences of each action, at the rate at which actions execute.

**中文:** • 常规改进。强化学习和世界模型训练仍然需要针对每项任务进行 rollout 和适配（Sec. 4.5.3）。一个循环若能让部署暴露失败、让智能体提出纠正、再把成功的行为蒸馏回策略中（Sec. G.3），就能把这种逐任务的成本变成运行过程的副产品。• 层级之间的延迟。推理、验证与恢复必须更贴近策略的控制频率，途径包括更快的智能体、蒸馏得到的验证器，或能够吸收反复出现的纠正的策略。• 安全的物理动作。语言模型的安全训练约束的是它们说什么，而并不知道这种约束能否延伸到机器人做什么。可由智能体操控的策略，需要以动作执行的速率，对每个动作的物理后果进行自身的检查。

<a id="S490"></a>
**Source:** p.28 S490

**Original:** GR00T 2 shows that one model, pretrained to predict how the physical world unfolds, can learn from human experience, transfer skills across embodiments, and serve as the manipulation layer of an agentic system. The open problems above share one structure. Each asks how to turn a scarce resource, whether robot hours, human time, or onboard compute, into reliable physical capability, and how to measure the result with enough confidence to act on it.

**中文:** GR00T 2 表明，一个以预测物理世界如何演化为目标进行预训练的单一模型，能够从人类经验中学习、跨本体迁移技能，并充当智能体化系统的操作层。上述开放问题具有共同的结构。每一个问题都在追问：如何把稀缺资源（无论是机器人时长、人类时间还是机载算力）转化为可靠的物理能力，以及如何以足够的把握测量结果，从而据此行动。


<a id="H20"></a>
### A. Fast-Adapt with GR00T 2 ｜ 附录 A：GR00T 2 的快速适配

<a id="H21"></a>
### A.1. Benchmark Tasks ｜ A.1 基准任务

<a id="C022"></a>
**Source:** p.38 C022 · 图 F021

![F021](assets/F021.png)

**Original (caption):** Figure 21: YAM post-training benchmark tasks. The six tasks of Tab. 1a, one per row. Left: task name and a short description. Right: key frames from four representative stages of each task, which has more stages than shown (Hot Wheels Assembly has 24).

**中文图注：** 图 21：YAM 后训练基准任务。Tab. 1a 中的六个任务，每行一个。左：任务名称与简短描述。右：每个任务四个代表性阶段的关键帧；任务实际阶段多于所示（Hot Wheels Assembly 共 24 个阶段）。

<a id="C023"></a>
**Source:** p.39 C023 · 图 F022

![F022](assets/F022.png)

**Original (caption):** Figure 22: Dexter post-training benchmark tasks. The seven tasks of Tab. 1b, one per row. Left: task name and a short description. Right: key frames from four representative stages of each task.

**中文图注：** 图 22：Dexter 后训练基准任务。Tab. 1b 中的七个任务，每行一个。左：任务名称与简短描述。右：每个任务四个代表性阶段的关键帧。

<a id="S768"></a>
**Source:** p.39 S768

**Original:** Fig. 23 plots the average task progress of each model in Tab. 1a against its inference latency.

**中文:** Fig. 23 把 Tab. 1a 中每个模型在六项任务上的平均任务进度对其推理时延作图。

<a id="C024"></a>
**Source:** p.40 C024 · 图 F023

![F023](assets/F023.png)

**Original (caption):** Figure 23: YAM post-training Pareto frontier. Average task progress across the six tasks in Tab. 1a versus inference latency per served call on a GeForce RTX 5090 workstation. The dashed line indicates the Pareto frontier.

**中文图注：** 图 23：YAM 后训练的帕累托前沿。Tab. 1a 六项任务的平均任务进度，对比在 GeForce RTX 5090 工作站上每次服务调用的推理时延。虚线标出帕累托前沿。

<a id="H22"></a>
### A.2. Zero-Shot Generalization with GR00T 2 ｜ A.2 GR00T 2 的零样本泛化

<a id="S773"></a>
**Source:** p.40 S773

**Original:** YAM Zero-Shot Benchmark. We evaluate the pretrained policies without task-specific post-training on the YAM V2 benchmark. For 𝜋0.5, we use a checkpoint adapted on in-domain data. We report results for the three unseen evaluation pools: Language Following, Motion Primitives (Easy), and Motion Primitives (Medium/Hard), comprising 14, 10, and 14 tasks, respectively. The benchmark evaluates language grounding and a range of manipulation motions, including actions beyond pick-and-place (Tab. 2).

**中文:** YAM 零样本基准。我们在 YAM V2 基准上评测未经任务特定后训练的预训练策略。对 𝜋0.5，我们使用在域内数据上适配过的检查点。我们报告三个未见评测池的结果：语言跟随、运动基元（简单）、运动基元（中/难），分别包含 14、10 和 14 项任务。该基准评测语言落地能力以及一系列操作运动，包括超出抓取-放置范畴的动作（Tab. 2）。

<a id="C025"></a>
**Source:** p.40 C025 · 表 T002

![T002](assets/T002.png)

**Original (caption):** Table 2: YAM V2 zero-shot evaluation. For each model, Prog. is the average task score and SR is the success rate, both on a 0 to 100 scale. We pool graded trials across available evaluations and weight tasks equally within each group. Trial counts vary across tasks and models, and results include graded trials from ongoing evaluations. †GR00T 1.7 results are preliminary. –: no result available. Bold marks the best Prog. and SR in each row.

**中文表注：** 表 2：YAM V2 零样本评测。对每个模型，Prog. 是平均任务得分，SR 是成功率，均采用 0 至 100 的刻度。我们汇总现有各次评测中已评分的试次，并在每组内对任务等权。各任务与各模型的试次数不同，结果包含仍在进行的评测中已评分的试次。†GR00T 1.7 的结果为初步结果。–：无可用结果。粗体标出每行中最好的 Prog. 与 SR。

<a id="S780"></a>
**Source:** p.40 S780

**Original:** Dexter Zero-Shot Benchmark. We further evaluate zero-shot transfer on Dexter, a bimanual robot with two dexterous hands, again without task-specific post-training. The evaluation covers 71 tasks: 49 dexterous manipulation tasks and 22 out-of-distribution instruction tasks that probe language grounding through color, size, ordinal position, negation, spatial relations, counting, and named targets. Each model is run for three trials per task, and we report results pooled over all tasks (Tab. 3).

**中文:** Dexter 零样本基准。我们进一步在 Dexter（一台配备两只灵巧手的双臂机器人）上评测零样本迁移，同样不做任务特定后训练。评测覆盖 71 项任务：49 项灵巧操作任务，以及 22 项分布外指令任务，后者通过颜色、尺寸、序数位置、否定、空间关系、计数和具名目标来考察语言落地能力。每个模型在每项任务上运行三次试次，我们报告在全部任务上汇总的结果（Tab. 3）。

<a id="C026"></a>
**Source:** p.41 C026 · 表 T003

![T003](assets/T003.png)

**Original (caption):** Table 3: Dexter zero-shot evaluation. For each model, Prog. is the average task progress and SR is the success rate, both on a 0 to 100 scale, pooled over 71 tasks (49 manipulation tasks and 22 out-of-distribution instruction tasks) with three trials per task. The four models run interleaved in the same sessions, and the operator who labels success is not told which model is running. Task progress is rated per episode by a vision-language model from the head and wrist camera videos. Bold marks the best Prog. and SR in each row.

**中文表注：** 表 3：Dexter 零样本评测。对每个模型，Prog. 是平均任务进度，SR 是成功率，均采用 0 至 100 的刻度，在 71 项任务（49 项操作任务与 22 项分布外指令任务）上汇总，每项任务三次试次。四个模型在同一批会话中交错运行，负责判定成功的操作员不知道当前运行的是哪个模型。任务进度由视觉语言模型依据头部与腕部相机视频逐 episode 评定。粗体标出每行中最好的 Prog. 与 SR。

<a id="H23"></a>
### A.3. Dexter-50: Emergent Cross-Embodiment Zero-Shot and Few-Shot Transfer. ｜ A.3 Dexter-50：涌现的跨本体零样本与少样本迁移

<a id="S785"></a>
**Source:** p.41 S785

**Original:** GR00T 2 transfers tasks across embodiments. We evaluate it on Dexter, a bimanual robot with two 7-DoF arms and two 22-DoF Sharpa hands, on Dexter-50: 50 tasks that never appear in Dexter’s training data but do appear in data from other embodiments, namely YAM parallel-gripper teleoperation, human video, or both. In the zero-shot setting, the pretrained model receives only the task instruction. In the few-shot setting, we adapt the same checkpoint to each task with 1 or 5 teleoperated Dexter episodes, a few minutes of robot data. We train rank-32 LoRA adapters on every linear layer of the transformer and keep the text encoder, video VAE, action and state heads, and all pretrained weights frozen. The adapters receive the same joint video and action flow-matching loss used in pretraining. We cut each episode into 100 evenly spaced training windows and sample them in proportion to the frozen model’s loss on each window, so that updates concentrate on the hard phases of the task, such as grasping or insertion. All tasks share the same hyperparameters, with no per-task tuning. One run fits on a single RTX 5090 and takes about 30 minutes. We merge the adapters into the base weights after training, so the adapted model is served exactly like the pretrained one.

**中文:** GR00T 2 能跨本体迁移任务。我们在 Dexter（一台配两条 7-DoF 手臂和两只 22-DoF Sharpa 手的双臂机器人）上，用 Dexter-50 评测这一能力：这 50 项任务从未出现在 Dexter 的训练数据中，但出现在其他本体的数据里，即 YAM 平行夹爪遥操作数据、人类视频，或两者兼有。在零样本设置下，预训练模型只接收任务指令。在少样本设置下，我们用 1 条或 5 条 Dexter 遥操作 episode（数分钟机器人数据）把同一检查点适配到每项任务。我们在 Transformer 的每个线性层上训练秩为 32 的 LoRA 适配器，并冻结文本编码器、视频 VAE、动作头与状态头以及全部预训练权重。适配器接收与预训练相同的视频-动作联合流匹配损失。我们把每条 episode 切成 100 个等距训练窗口，并按冻结模型在各窗口上的损失成比例采样，使更新集中在任务的困难阶段，例如抓取或插入。所有任务共享同一组超参数，不做逐任务调参。一次运行可在单张 RTX 5090 上完成，耗时约 30 分钟。训练后我们把适配器合并进基础权重，因此适配后的模型的服务方式与预训练模型完全一致。

<a id="S786"></a>
**Source:** p.41 S786

**Original:** Across the 50 tasks, GR00T 2 succeeds 40% of the time zero-shot, 71% with one episode, and 95% with five (Fig. 24). Zero-shot, it completes 40 of the 50 tasks at least once and succeeds in every trial of four, such as unloading a dish rack and unstacking Rubik’s cubes, skills it has seen only on a parallel-gripper robot or in human video. With five episodes, 37 of the 50 tasks reach 100%, including tasks the zero-shot model never completes, such as emptying a bag, turning a lazy susan, and unfolding a tripod. In most of the failures shown in Fig. 25, the zero-shot model goes for the right steps, but its new hands fail at one of them, such as lifting a teapot lid or opening a drawstring bag. One or five Dexter episodes fix this.

**中文:** 在这 50 项任务上，GR00T 2 零样本成功率 40%，给定一条 episode 后为 71%，给定五条后为 95%（Fig. 24）。零样本时，它在 50 项任务中有 40 项至少成功一次，并有四项在每次试次中都成功，例如卸下碗架、叠放魔方——这些技能它只在平行夹爪机器人上或人类视频中见过。给定五条 episode 后，50 项任务中有 37 项达到 100%，其中包括零样本模型从未完成的任务，例如清空袋子、转动转盘、展开三脚架。在 Fig. 25 所示的大多数失败中，零样本模型走的是正确的步骤，但它新换的双手在其中某一步失败，例如提起茶壶盖或拉开抽绳袋。一条或五条 Dexter episode 就能修正这一点。

<a id="C027"></a>
**Source:** p.42 C027 · 图 F024

![F024](assets/F024.png)

**Original (caption):** Figure 24: Cross-embodiment transfer to Dexter with 0, 1, and 5 Dexter episodes, per task. Success rate on the Dexter-50 tasks, which have no Dexter training data but appear in YAM teleoperation data, human video, or both, sorted by zero-shot success. Zero-shot runs the pretrained model directly, while 1-shot and 5-shot fine-tune it with LoRA on 1 or 5 Dexter episodes. The first group (gray band) is the average over all 50 tasks. Tasks are those the model learns with five episodes (at least 80% success).

**中文图注：** 图 24：给定 0、1、5 条 Dexter episode 时向 Dexter 的跨本体迁移，逐任务结果。Dexter-50 任务的成功率——这些任务没有 Dexter 训练数据，但出现在 YAM 遥操作数据、人类视频或两者中——按零样本成功率排序。零样本直接运行预训练模型，1-shot 与 5-shot 则用 LoRA 在 1 条或 5 条 Dexter episode 上微调。第一组（灰带）是全部 50 项任务的平均。任务集合为模型用五条 episode 即可学会（成功率至少 80%）的那些任务。

<a id="H24"></a>
### B. X-Adapt with GR00T 2 ｜ 附录 B：GR00T 2 的跨本体适配

<a id="S844"></a>
**Source:** p.42 S844

**Original:** This section details the cross-embodiment transfer summarized in Sec. 3.2 and the devices and pipelines described in Sec. 4.4.

**中文:** 本附录详述 Sec. 3.2 概述的跨本体迁移，以及 Sec. 4.4 描述的采集设备与流程。

<a id="H25"></a>
### B.1. Human →Tianji + Sharpa ｜ B.1 人类 →Tianji + Sharpa

<a id="S845"></a>
**Source:** p.42 S845

**Original:** GR00T 2 can also learn a dexterous task on a robot from human demonstrations alone. Here every task-specific demonstration comes from a person recorded with our human data capture pipeline, which pairs head and wrist cameras with wrist trackers and data gloves, and the resulting policy runs on the Tianji, a bimanual robot with two 7-DoF arms and two 22-DoF Sharpa hands. The embodiment gap now centers on the hand. Appearance differs because the cameras observe a human hand during demonstration and a robot hand at deployment. Kinematics differ because the larger Sharpa hand does not share the size or joint structure of the human hand, so retargeting must map every finger motion onto the 22-DoF robot hand. Dynamics differ because the human moves at natural speed, which teleoperation cannot reproduce on the robot. Three components bridge these gaps: the capture pipeline records robot-aligned views (Sec. B.1.1), a geometric retargeter converts every demonstration into robot actions (Sec. B.1.2), and co-training with task-agnostic play data, collected with our teleoperation system (Sec. C.3.1), grounds the model in the robot (Sec. B.1.3).

**中文:** GR00T 2 也能仅凭人类演示就在机器人上学会灵巧任务。这里每一条任务特定演示都来自一个人，由我们的人类数据采集流程录制：该流程把头戴与腕部相机与腕部跟踪器、数据手套配对；由此得到的策略运行在 Tianji 上——一台配两条 7-DoF 手臂和两只 22-DoF Sharpa 手的双臂机器人。此时本体差距集中在手上。外观不同，因为演示时相机看到的是人手，部署时看到的是机器手。运动学不同，因为更大的 Sharpa 手与人手在尺寸和关节结构上都不一致，所以重定向必须把每一根手指的运动映射到 22-DoF 的机器手上。动力学不同，因为人以自然速度运动，而遥操作无法在机器人上复现这一速度。三个组件弥合这些差距：采集流程录制与机器人对齐的视角（Sec. B.1.1）；几何重定向器把每条演示转换为机器人动作（Sec. B.1.2）；与任务无关的 play 数据（用我们的遥操作系统采集，Sec. C.3.1）联合训练，把模型锚定在机器人上（Sec. B.1.3）。

<a id="C028"></a>
**Source:** p.43 C028 · 图 F025

![F025](assets/F025.png)

**Original (caption):** Figure 25: Example Dexter rollouts. Top: zero-shot successes. Middle and bottom: tasks the zero-shot model attempts but fails, mostly at a step its new hands cannot yet do (left, with the failure noted above each row), and completes after fine-tuning on one or five Dexter episodes (right). Rollouts ran on different Dexter stations, so the backgrounds differ.

**中文图注：** 图 25：Dexter rollout 示例。上：零样本成功案例。中与下：零样本模型尝试但失败的任务，失败大多发生在它新换的双手尚不能完成的某一步（左列，每行上方标注失败点），以及在一或五条 Dexter episode 上微调后完成该任务的情形（右列）。各次 rollout 在不同 Dexter 工位上运行，因此背景不同。


<a id="S866"></a>
**Source:** p.43 S866

**Original:** We evaluate on four tasks (Fig. 26). Filter Paper Setup, Dropper-to-Beaker Dispensing, and Microscope Slide Dabbing are chemistry-lab tasks that handle small, often transparent labware and leave little tolerance for fingertip error. Conveyor Package Tossing is a dynamic task: the robot grasps each package from a moving belt and throws it over the belt into the bin assigned to that package, a targeted throw that teleoperation cannot demonstrate. For each task, we co-train the retargeted human demonstrations with task-agnostic Tianji play data. The play data contain no demonstrations of the target tasks. All models are post-trained with an identical data recipe and number of optimization steps. Without a single teleoperated demonstration of the target tasks, GR00T 2 succeeds in 65%, 30%, 10%, and 50% of 20 trials on the four tasks, whereas GR00T 1.7 and GR00T 2 without cross-embodiment pretraining fail every chemistry-lab trial and reach only 5% and 20% on tossing (Fig. 27). Adding 10 teleoperated demonstrations raises GR00T 2 to 95%, 70%, and 50% on the chemistry-lab tasks, against 45%, 40%, and 30% without cross-embodiment pretraining and 0% for GR00T 1.7. One hundred human demonstrations per task therefore suffice to deploy precise and dynamic dexterous tasks on a robot that has never been teleoperated for them. Sec. B.1.4 details the protocol, and Sec. B.1.5 analyzes why the transfer works.

**中文:** 我们在四项任务上评测（Fig. 26）。滤纸准备、滴管到烧杯的移液、载玻片涂抹属于化学实验室任务，操作的是小型且往往透明的实验器皿，对指尖误差几乎没有容忍度。传送带包裹抛掷是动态任务：机器人从运动中的传送带上抓取每个包裹，越过传送带把它抛进该包裹对应的料箱——这是一种遥操作无法演示的定向抛掷。对每项任务，我们把重定向后的人类演示与任务无关的 Tianji play 数据联合训练。play 数据中不含目标任务的任何演示。所有模型用完全相同的数据配方和优化步数做后训练。在完全没有目标任务的遥操作演示的情况下，GR00T 2 在四项任务各 20 次试次中成功率为 65%、30%、10% 和 50%；而 GR00T 1.7 与未做跨本体预训练的 GR00T 2 在全部化学实验室试次中均失败，抛掷任务上仅达 5% 与 20%（Fig. 27）。加入 10 条遥操作演示后，GR00T 2 在化学实验室任务上提升到 95%、70% 和 50%，未做跨本体预训练的版本为 45%、40% 和 30%，GR00T 1.7 为 0%。因此，每项任务约一百条人类演示，就足以在一台从未为该任务遥操作过的机器人上部署精确且动态的灵巧任务。Sec. B.1.4 详述协议，Sec. B.1.5 分析迁移为何有效。

<a id="S869"></a>
**Source:** p.44 S869

**Original:** B.1.1. Human Data Capture and Conversion

**中文:** B.1.1 人类数据的采集与转换

<a id="S870"></a>
**Source:** p.44 S870

**Original:** Human data capture. Each demonstration is recorded with a lightweight egocentric rig: a head-mounted camera provides the ego view, wrist-mounted cameras provide close-up views of hand-object contact, and the hands are tracked by a motion-capture glove (Manus) paired with a 6-DoF tracker (PICO) rigidly attached to each wrist. The glove provides per-finger joint angles, while the tracker provides the global wrist pose. Together they yield a full 3D hand pose at every timestep without any robot in the loop. Because the tracker’s IMU does not coincide with the anatomical wrist, we calibrate the tracker-to-wrist rigid transform per session: an annotator clicks fingertip locations in a handful of frames spanning diverse hand poses, and we solve for the transform that minimizes the reprojection error of the glove-predicted fingertips. Camera intrinsics and extrinsics are verified in the same tool by overlaying the tracked controller pose onto the video, so that calibration errors are caught before any data is converted. The raw stream (ego and wrist video, wrist poses, finger joints, and language annotations) is captured at 60 Hz, stored in a time-synchronized format and quality-checked by visualizing the reconstructed hand trajectory against the video.

**中文:** 人类数据采集。每条演示都用一套轻量第一人称设备录制：头戴相机提供第一人称视角，腕戴相机提供手-物接触的近景视角，手部由动捕手套（Manus）跟踪，并配一个刚性固定在每个腕部的 6-DoF 跟踪器（PICO）。手套给出每根手指的关节角，跟踪器给出全局腕部位姿。两者结合，可在每个时间步得到完整的三维手部位姿，全程无需机器人在环。由于跟踪器的 IMU 与解剖学意义上的腕部并不重合，我们逐次会话标定"跟踪器到腕部"的刚体变换：标注员在若干覆盖多样手部姿态的帧里点击指尖位置，我们求解使手套预测指尖重投影误差最小的变换。相机内参与外参在同一工具中校验——把跟踪到的控制器位姿叠加到视频上，从而在任何数据被转换之前就发现标定错误。原始数据流（第一人称与腕部视频、腕部位姿、手指关节、语言标注）以 60 Hz 采集，以时间同步格式存储，并通过把重建的手部轨迹与视频叠加可视化来做质量检查。

<a id="S871"></a>
**Source:** p.44 S871

**Original:** From human data to robot data. The captured human trajectories are converted into robot-space supervision in a single offline pass, with no task-specific robot teleoperation. First, each wrist pose is anchored globally in the gravity-aligned robot base frame: the human’s head camera is placed at the robot’s head camera, and a per-task offset shifts the hands into the robot workspace. The converted trajectories therefore carry absolute wrist poses in the robot frame, not wrist displacements alone. Second, the human finger configuration is retargeted to the robot hand via inverse kinematics on fingertip targets, producing joint commands that respect the robot’s kinematic limits while preserving the task-relevant contact geometry rather than the literal human pose. Third, the ego and wrist camera streams are kept as the policy’s visual inputs, so that the resulting episodes, downsampled to 30 Hz, have the same observation and action schema as native robot data. During post-training, we sample converted human episodes and generic, non-task-specific robot play data with equal probability. This co-training grounds the model in the robot’s appearance and dynamics, while human demonstrations provide all task-specific supervision.

**中文:** 从人类数据到机器人数据。采集到的人类轨迹在一次离线处理中转换为机器人空间中的监督信号，不需要任何任务特定的机器人遥操作。第一，每个腕部位姿被全局锚定在重力对齐的机器人基座坐标系中：把人的头戴相机放置在机器人头部相机处，再用一个逐任务的偏移把手移入机器人工作空间。因此转换后的轨迹携带的是机器人坐标系下的绝对腕部位姿，而不只是腕部位移。第二，通过以指尖为目标的逆运动学，把人手的手指构型重定向到机器手，产生既遵守机器人运动学极限、又保留任务相关接触几何（而非照搬人手姿态）的关节指令。第三，第一人称与腕部相机流保留为策略的视觉输入，因此所得 episode（降采样到 30 Hz）与原生机器人数据具有相同的观测与动作 schema。后训练时，我们以相等概率采样转换后的人类 episode 与通用的、非任务特定的机器人 play 数据。这种联合训练把模型锚定在机器人的外观与动力学上，而人类演示提供全部任务特定的监督。

<a id="S872"></a>
**Source:** p.44 S872

**Original:** B.1.2. Geometric Retargeting

**中文:** B.1.2 几何重定向

<a id="S873"></a>
**Source:** p.44 S873

**Original:** The role of our retargeting solver is to bring sub-millimeter accuracy to robot finger tips with kHz computation speed. Given that the conversion is solely offline without human supervision, we ask for automated singularity handling near workspace boundary and robust redundancy DoF management. To achieve this we make use of a closed-form geometric inverse kinematic solving technique introduced in Chen et al. (2026b) and Kong et al. (2026) to handle both the 7-DoF arms and 22 DoF robot hands. Given 6D pose data of ego camera and left / right wrist mount, we first find the ideal placement of human data in robot frame for each task. The solver then retargets the hands before the arm, and both stages track fingertip targets. A unified “palm-box” hand frame introduced in Kong et al. (2026), anchored at the index fingertip, aligns human and robot hands. The 22-DoF hand solver places the robot thumb tip relative to the solved index fingertip, which preserves the pinch geometry, while the other fingers follow the human bone directions. The arm’s geometric inverse-kinematics solver then tracks the palm-box origin, so the robot index fingertip lands on the human index fingertip.

**中文:** 我们的重定向求解器的作用，是以 kHz 级计算速度把机器人指尖精度带到亚毫米级。考虑到转换完全离线且无人工监督，我们要求能自动处理工作空间边界附近的奇异位形，并对冗余自由度做稳健管理。为此我们采用 Chen et al. (2026b) 与 Kong et al. (2026) 提出的闭式几何逆运动学求解技术，同时处理 7-DoF 手臂与 22 自由度机器手。给定第一人称相机与左/右腕部安装座的 6D 位姿数据，我们首先为每项任务找出人类数据在机器人坐标系中的理想放置。随后求解器先重定向手、再重定向臂，两个阶段都跟踪指尖目标。Kong et al. (2026) 提出的统一"掌盒"（palm-box）手部坐标系以食指指尖为锚点，用于对齐人手与机器手。22-DoF 手求解器把机器拇指指尖相对已求解的食指指尖放置，从而保留捏合几何，其余手指则沿人骨方向跟随。随后手臂的几何逆运动学求解器跟踪掌盒原点，使机器食指指尖落到人的食指指尖上。

<a id="S875"></a>
**Source:** p.44 S875

**Original:** Our combined arm-hand solver achieves approximately 118,000 bimanual solves per second on a single core of an Intel Core Ultra 9 285K CPU, with a mean native computation time of 8.48 𝜇s, excluding Python interface overhead. Across 1,024 synthetic in-range wrist targets, maximum forward-kinematics-verified pose errors remain below 10−15 m and 10−15 rad. This throughput supports real-time teleoperation (Sec. C.3.1) and offline human-data conversion.

**中文:** 我们的臂-手联合求解器在 Intel Core Ultra 9 285K 的单核上达到约每秒 118,000 次双臂求解，原生平均计算时间 8.48 𝜇s（不含 Python 接口开销）。在 1,024 个合成的射程内腕部目标上，经正运动学验证的最大位姿误差保持在 $10^{-15}$ m 与 $10^{-15}$ rad 以下。这一吞吐量同时支持实时遥操作（Sec. C.3.1）与离线人类数据转换。

<a id="C029"></a>
**Source:** p.45 C029 · 图 F026

![F026](assets/F026.png)

**Original (caption):** Figure 26: Sensorized human transfer benchmark tasks. Each row shows the ordered stages of one task, with the language instruction that GR00T 2 receives.

**中文图注：** 图 26：带传感器人类演示迁移的基准任务。每行展示一项任务的有序阶段，以及 GR00T 2 接收到的语言指令。

<a id="S876"></a>
**Source:** p.45 S876

**Original:** B.1.3. Co-Training with Robot Play Data

**中文:** B.1.3 与机器人 play 数据联合训练

<a id="S877"></a>
**Source:** p.45 S877

**Original:** GR00T 2 turns retargeted human demonstrations into a robot policy by co-training them with robot play data. Starting from its cross-embodiment pretrained checkpoint, GR00T 2 fine-tunes on two complementary sources: retargeted human demonstrations of the target task, which contain the task but not the robot, and task-agnostic play data from the target robot, collected with the teleoperation system of Sec. C.3.1, which contain the robot but not the task. Human data teach GR00T 2 what to do: the task intent, the object interactions, and the motion strategy, such as which hand leads, which fingers make contact, and how fast the wrist moves. Play data teach GR00T 2 how this robot looks and moves: its appearance, kinematics, and dynamics, which stay the same across tasks, so one play pool serves every task. Without teleoperation, the play data are the only robot data in post-training. Each new task therefore adds only cheap human demonstrations.

**中文:** GR00T 2 通过把重定向后的人类演示与机器人 play 数据联合训练，把前者变成机器人策略。从跨本体预训练检查点出发，GR00T 2 在两个互补来源上微调：目标任务的、重定向后的人类演示——它包含"任务"但不含"机器人"；以及来自目标机器人的任务无关 play 数据（用 Sec. C.3.1 的遥操作系统采集）——它包含"机器人"但不含"任务"。人类数据教 GR00T 2 做什么：任务意图、物体交互、运动策略，例如哪只手先动、哪些手指接触、腕部移动多快。play 数据教 GR00T 2 这台机器人长什么样、怎么动：它的外观、运动学与动力学，这些跨任务不变，因此一个 play 池可服务所有任务。在没有遥操作的情况下，play 数据就是后训练中唯一的机器人数据。于是每新增一个任务，只需追加廉价的人类演示。

<a id="S878"></a>
**Source:** p.45 S878

**Original:** Human and robot episodes share one data format, so the two sources mix freely within a training batch. Both provide three camera views (ego and two wrists) at 30 Hz, a 62-D state of absolute wrist poses in the robot base frame and hand-joint positions, and a 62-D action chunk of wrist poses relative to the current state and absolute hand-joint positions.

**中文:** 人类 episode 与机器人 episode 共用一种数据格式，因此两个来源可以在同一训练批次内自由混合。两者都提供 30 Hz 的三路相机视角（第一人称与两个腕部）、一个 62 维状态（机器人基座坐标系下的绝对腕部位姿与手部关节位置），以及一个 62 维动作块（相对当前状态的腕部位姿与绝对手部关节位置）。

<a id="S879"></a>
**Source:** p.45 S879

**Original:** B.1.4. Learning New Tasks without Teleoperation

**中文:** B.1.4 无遥操作地学习新任务

<a id="S880"></a>
**Source:** p.45 S880

**Original:** GR00T 2 learns new robot tasks from human demonstrations alone. Four tasks on the Tianji, a bimanual robot with two 7-DoF arms and two 22-DoF Sharpa hands, test this claim and stress two parts of the embodiment gap. Three chemistry-lab tasks handle small, often transparent labware and test precision under the kinematic gap, where retargeting error and the larger robot hand both consume the tolerance. The dynamic task tests the kinodynamic gap on a fast, targeted throw that teleoperation cannot demonstrate (Fig. 26).

**中文:** GR00T 2 仅凭人类演示就能学会新的机器人任务。Tianji（一台配两条 7-DoF 手臂和两只 22-DoF Sharpa 手的双臂机器人）上的四项任务检验这一主张，并分别施压本体差距的两个方面。三项化学实验室任务操作小型且往往透明的实验器皿，检验运动学差距下的精度——在这里重定向误差与更大的机器手共同消耗容忍度。动态任务检验运动动力学差距，形式是遥操作无法演示的快速定向抛掷（Fig. 26）。

<a id="S881"></a>
**Source:** p.45 S881

**Original:** Tasks and metrics. A rubric splits each task into 𝐾ordered stages, and we grade each trial by the number of stages 𝑘it completes in order. A trial succeeds when 𝑘= 𝐾, its task progress is 𝑘/𝐾, and any human intervention counts as a failure.

**中文:** 任务与指标。评分细则把每项任务拆成 $K$ 个有序阶段，我们按一次试次按序完成的阶段数 $k$ 来评分。当 $k=K$ 时试次成功，其任务进度为 $k/K$，任何人工干预都计为失败。

<a id="S882"></a>
**Source:** p.45 S882

**Original:** • Filter Paper Setup (𝐾=6): grasp the filter paper, place it in the funnel, unfold and seat it in the funnel,

**中文:** • 滤纸准备（$K=6$）：抓起滤纸，放入漏斗，将其展开并安置在漏斗中，

<a id="C030"></a>
**Source:** p.46 C030 · 图 F027

![F027](assets/F027.png)

**Original (caption):** Figure 27: Learning new tasks with zero or few teleoperated demonstrations. Success rate (top) and task progress (bottom) over 20 trials per point, with 0, 1, or 10 teleoperated demonstrations of the target task added to post-training. At

**中文图注：** 图 27：在零条或少量遥操作演示下学习新任务。每个数据点为 20 次试次上的成功率（上）与任务进度（下），横轴为后训练中加入的目标任务遥操作演示条数：0、1 或 10。在

<a id="S892"></a>
**Source:** p.46 S892

**Original:** 0, no training data contain a robot trajectory of the task. All models share the human demonstrations, robot data, and post-training recipe. Each baseline changes one factor relative to GR00T 2, either the model formulation (GR00T 1.7, a VLA) or the pretraining data (GR00T 2 w/o cross-embodiment pretraining, pretrained on target-robot data alone, Sec. B.1.5). Conveyor Package Tossing is evaluated at 0 only, since teleoperation cannot demonstrate its fast, targeted throw.

**中文:** 0 条时，没有任何训练数据包含该任务的机器人轨迹。所有模型共享相同的人类演示、机器人数据与后训练配方。每个基线相对 GR00T 2 只改变一个因素：或改变模型形式（GR00T 1.7，一个 VLA），或改变预训练数据（GR00T 2 w/o cross-embodiment pretraining，仅在目标机器人数据上预训练，Sec. B.1.5）。传送带包裹抛掷仅在 0 条设置下评测，因为遥操作无法演示其快速定向抛掷。

<a id="S893"></a>
**Source:** p.46 S893

**Original:** grasp the water bottle, wet the filter paper, and put the bottle back. • Dropper-to-Beaker Dispensing (𝐾=3): grasp the pipette, draw the clear liquid, and release it into the blue liquid. • Microscope Slide Dabbing (𝐾=4): grasp the swab, dip it into the water, bring it to the slide, and dab the slide. • Conveyor Package Tossing (𝐾=3): grasp a package from the moving belt, toss it over the belt, and land it in the bin assigned to that package.

**中文:** 抓起水瓶，润湿滤纸，再把瓶子放回。• 滴管到烧杯移液（$K=3$）：抓起移液管，吸取澄清液体，并将其释放到蓝色液体中。• 载玻片涂抹（$K=4$）：抓起棉签，蘸水，移到载玻片上，涂抹载玻片。• 传送带包裹抛掷（$K=3$）：从运动中的传送带上抓起一个包裹，越过传送带抛出，使其落入该包裹对应的料箱。

<a id="S894"></a>
**Source:** p.46 S894

**Original:** All models post-train on one mixture, retargeted human demonstrations and robot play data sampled 1:1, with one recipe and step budget and no per-task tuning or checkpoint selection. To measure what teleoperation still adds, we also add 1 or 10 teleoperated demonstrations of the target task to the mixture. Each point averages 20 trials.

**中文:** 所有模型都在同一数据配比上后训练：重定向后的人类演示与机器人 play 数据按 1:1 采样，使用同一配方与步数预算，不做逐任务调参或检查点挑选。为衡量遥操作仍能带来什么，我们还在配比中加入 1 条或 10 条目标任务的遥操作演示。每个数据点平均 20 次试次。


<a id="S895"></a>
**Source:** p.46 S895

**Original:** Learning without teleoperation. Without a single teleoperated demonstration, GR00T 2 succeeds in 65%, 30%, 10%, and 50% of trials on Filter Paper Setup, Dropper-to-Beaker Dispensing, Microscope Slide Dabbing, and Conveyor Package Tossing (Fig. 27). Both baselines fail every chemistry-lab trial in the same setting and succeed only on tossing, with 20% without cross-embodiment pretraining and 5% for GR00T 1.7. The human demonstrations carry the task: without them, the same GR00T 2 recipe succeeds in 0% of trials on every task. Tossing shows that this transfer extends beyond teleoperation: GR00T 2 learns the throw entirely from humans.

**中文:** 无需遥操作的学习。在没有任何一条遥操作演示的情况下，GR00T 2 在 Filter Paper Setup、Dropper-to-Beaker Dispensing、Microscope Slide Dabbing 和 Conveyor Package Tossing 四项任务上的试次成功率分别为 65%、30%、10% 和 50%（Fig. 27）。两个基线在同一设置下的每个化学实验室试次中均告失败，仅在抛掷任务上取得成功：不做跨本体预训练的基线成功率为 20%，GR00T 1.7 为 5%。承担任务的是人类演示：去掉它们后，同一套 GR00T 2 配方在每项任务上的成功率均为 0%。抛掷任务表明，这种迁移并不局限于遥操作：GR00T 2 完全从人类那里学会了抛掷动作。

<a id="S896"></a>
**Source:** p.46 S896

**Original:** Teleoperation adds to human data. Teleoperated demonstrations refine the task that human demonstrations teach rather than replace them. With 10 demonstrations, GR00T 2 succeeds in 95%, 70%, and 50% of chemistry-lab trials, compared with 45%, 40%, and 30% without cross-embodiment pretraining and 0% for GR00T 1.7. On Filter Paper Setup, GR00T 2 without teleoperation already outperforms the baseline trained with 10 teleoperated demonstrations.

**中文:** 遥操作对人类数据起补充作用。遥操作演示细化的是人类演示所教授的任务，而不是取代它们。使用 10 条演示时，GR00T 2 在化学实验室试次上的成功率分别为 95%、70% 和 50%；不做跨本体预训练时分别为 45%、40% 和 30%，GR00T 1.7 为 0%。在 Filter Paper Setup 上，不使用遥操作的 GR00T 2 已经超过使用 10 条遥操作演示训练的基线。

<a id="C031"></a>
**Source:** p.47 C031 · 图 F028

![F028](assets/F028.png)

**Original (caption):** Figure 28: Predicted futures for tasks that only humans demonstrated. Given one robot start frame and the instruction, GR00T 2 predicts the robot’s ego view autoregressively. Each GR00T 2 row comes from a single rollout that starts at the first frame of an evaluation episode, and times are measured from that frame. Human demonstrations (top rows) appear only in training.

**中文图注：** 图 28：仅由人类演示的任务的预测未来画面。给定一个机器人起始帧和指令，GR00T 2 以自回归方式预测机器人的第一人称视角画面。每一行 GR00T 2 结果都来自一次 rollout（轨迹采样），其起点为某个评测片段的第一帧，时间自该帧起算。人类演示（顶部几行）仅出现在训练中。

<a id="S939"></a>
**Source:** p.47 S939

**Original:** B.1.5. Why GR00T 2 Learns without Teleoperation

**中文:** B.1.5. 为什么 GR00T 2 无需遥操作也能学习

<a id="S940"></a>
**Source:** p.47 S940

**Original:** Two baselines test the two properties that let GR00T 2 learn without teleoperation (Fig. 27). Each replaces one component of GR00T 2, the model formulation or the pretraining data, and keeps the post-training data, sampling weights, step budget, and evaluation protocol fixed.

**中文:** 两个基线分别检验让 GR00T 2 无需遥操作即可学习的两项特性（Fig. 27）。每个基线替换 GR00T 2 的一个组件，即模型形式或预训练数据，同时保持后训练数据、采样权重、步数预算和评测协议不变。

<a id="S941"></a>
**Source:** p.47 S941

**Original:** World-action model. GR00T 2 learns from human-only task data because it is a world-action model. Unlike a VLA that must learn task and embodiment in one observation-to-action map, from human-hand observations paired with retargeted actions, GR00T 2 factorizes the problem into two parts. Future-video prediction learns what should happen to the scene, a change that human and robot largely share, while action prediction learns how this robot produces that change, from robot play data. To test the formulation, we compare GR00T 2 with GR00T 1.7, a VLA pretrained on the same data and post-trained with the same recipe. The two models also differ in backbone and initialization, so the comparison tests the WAM design as a whole rather than the prediction target alone. GR00T 1.7 fails every chemistry-lab trial, even with 10 teleoperated demonstrations: under the same data and step budget, the VLA learns these precise tasks neither from human demonstrations nor from a few robot demonstrations. The factorization also makes a direct prediction: for a task that only humans demonstrated, GR00T 2 should predict robot hands rather than human hands. Conditioned on one robot start frame, GR00T 2 predicts the robot’s own hands reaching each milestone of all four tasks (Fig. 28).

**中文:** 世界-动作模型（WAM）。GR00T 2 仅从人类任务数据中学习，是因为它是一个世界-动作模型。与视觉-语言-动作（VLA）模型不同，后者必须在一个观测到动作的映射中同时学习任务和本体，而该映射的训练数据是人手观测与重定向动作的配对；GR00T 2 则把问题分解为两部分。未来视频预测学习场景应当如何变化，这一变化在人类与机器人之间大体相同；动作预测则从机器人自由操作数据中学习该机器人如何产生这种变化。为检验这一形式，我们将 GR00T 2 与 GR00T 1.7 进行比较。GR00T 1.7 是一个在同样数据上预训练、并用相同配方后训练的 VLA。两个模型在主干网络和初始化上也有差异，因此该比较检验的是 WAM 设计的整体，而不仅是预测目标。即使使用 10 条遥操作演示，GR00T 1.7 在每个化学实验室试次上仍告失败：在相同的数据和步数预算下，该 VLA 既无法从人类演示中学会这些精细任务，也无法从少量机器人演示中学会。这种分解还带来一个直接预测：对于只由人类演示过的任务，GR00T 2 应当预测机器人的手，而不是人手。给定一个机器人起始帧，GR00T 2 预测的是机器人自身的手在四项任务的每个里程碑处伸出的画面（Fig. 28）。

<a id="S942"></a>
**Source:** p.47 S942

**Original:** Cross-embodiment pretraining. GR00T 2 transfers task knowledge from the human hand to the robot hand because it pretrains across embodiments. Unlike target-only pretraining that ties task knowledge to one body, cross-embodiment pretraining teaches GR00T 2 to express one task through many bodies. To test this property, we fix the GR00T 2 model and its post-training and replace the full pretraining mixture with target-robot data alone, at a matched pretraining budget. The full mixture adds robot embodiments, human data, and scale at once, so this comparison measures the value of the GR00T 2 mixture as a whole. Without cross-embodiment pretraining, GR00T 2 fails every chemistry-lab trial without teleoperation and trails the full model at every number of teleoperated demonstrations, 45%, 40%, and 30% against 95%, 70%, and 50% at 10.

**中文:** 跨本体预训练。GR00T 2 能把任务知识从人手迁移到机器人手上，是因为它在多种本体上进行预训练。与只针对目标本体预训练、把任务知识绑定到单一身体上的做法不同，跨本体预训练让 GR00T 2 能够通过多种身体表达同一项任务。为检验这一特性，我们固定 GR00T 2 模型及其后训练，仅把完整预训练混合数据替换为目标机器人数据，且预训练预算保持一致。完整混合数据同时增加了机器人本体、人类数据和数据规模，因此该比较衡量的是 GR00T 2 数据混合的整体价值。去掉跨本体预训练后，GR00T 2 在不使用遥操作时的每个化学实验室试次中均告失败，并且在每一种遥操作演示数量下都落后于完整模型：分别为 45%、40% 和 30%，完整模型则为 95%、70% 和 50%（最后一组对应 10 条演示）。

<a id="S943"></a>
**Source:** p.47 S943

**Original:** Human-level motion beyond teleoperation. GR00T 2 achieves human-level motion agility, because learning directly from human demonstrations removes the speed ceiling that teleoperation imposes on robot data. A teleoperator perceives the scene through delayed video, feels no contact, and acts through a mismatched impedance, so teleoperated demonstrations are inherently slower and more conservative than natural human motion, and policies trained on them inherit this limit. Conveyor Package Tossing tests this directly: it is a targeted throw, not a simple toss. The robot must identify each package, grasp it from the moving belt, and release it at the correct phase of a fast arm swing so that it lands in the bin assigned to that package, a skill that is impractical to teleoperate. The demonstrator performs the task at natural speed in the capture rig, and GR00T 2 learns it from the converted demonstrations and robot play data alone, with no task-specific robot data, succeeding in 50% of trials. Removing the teleoperator thus does more than lower collection cost: it expands the set of behaviors a robot can learn to those that require human-level speed.

**中文:** 超越遥操作的人类水平动作。GR00T 2 实现了人类水平的动作敏捷性，因为直接从人类演示中学习，消除了遥操作施加在机器人数据上的速度上限。遥操作者通过有延迟的视频感知场景，无法感受接触，并以不匹配的阻抗进行操作，因此遥操作演示天生比自然的人类动作更慢、更保守，而在其上训练的策略也继承了这一限制。Conveyor Package Tossing 对此做了直接检验：它是一次有目标的抛掷，而不是简单的扔。机器人必须识别每个包裹，从移动的传送带上抓起它，并在手臂快速摆动的正确阶段松开，使包裹落入分配给它的箱子中，这种技能很难通过遥操作完成。示范者在采集装置中以自然速度完成该任务，GR00T 2 仅从转换后的演示和机器人自由操作数据中学习，没有任何任务专用的机器人数据，成功率达到 50%。因此，去掉遥操作者不只是降低了采集成本，还扩展了机器人可以学会的行为范围，使其包括那些需要人类水平速度的行为。

<a id="H26"></a>
### B.2. UMI →YAM ｜ B.2 节：从 UMI 到 YAM 的迁移

<a id="S945"></a>
**Source:** p.48 S945

**Original:** Suppose a bimanual gripper robot must learn to take apart an electronics assembly on a factory bench it has never seen: unscrew a nut, lift out a gear and two housings, unplug the connectors and cables, and place every part in a tray. No teleoperation data exist for this robot, and collecting them would tie up the robot, a station, and an operator for the full campaign. With GR00T 2 the task can instead be demonstrated with Gripper UMI, a handheld parallel gripper in the lineage of the Universal Manipulation Interface (UMI, Chi et al., 2024 and Sec. E.2): a person holding the device performs the job with natural motions at natural speed, while robot-style wrist cameras and a width encoder record the demonstration in robot coordinates, with no robot in the loop (Sec. E.1). The difficulty is that the handheld device and the robot are different embodiments. Whereas prior

**中文:** 设想一台双臂夹爪机器人需要在一张从未见过的工厂工作台上拆解电子组件：拧下螺母，取出一个齿轮和两个外壳，拔下连接器和线缆，并把每个零件放进托盘。这台机器人没有遥操作数据，而采集这些数据会让一台机器人、一个工位和一名操作员在整个评测批次中都被占用。借助 GR00T 2，这项任务可以改用 Gripper UMI 来演示。Gripper UMI 是一款手持平行夹爪，属于 Universal Manipulation Interface（UMI，Chi et al., 2024 and Sec. E.2）的技术谱系：持设备的人以自然动作、自然速度完成工作，同时类机器人的腕部相机和宽度编码器以机器人坐标记录演示，全程无需机器人参与（Sec. E.1）。难点在于，手持设备与机器人是不同的本体。而此前的 [存疑：句子在第 48 页截断，续句见 S946]

<a id="S946"></a>
**Source:** p.48 S946

**Original:** UMI deployments avoid this by construction, with a robot end-effector that reproduces the handheld device’s cameras and fingers (Chi et al., 2024), the target robot here, YAM, shares none of these components, and the two embodiments differ in all three respects at once: in sensing because YAM’s wrist cameras share neither the lens nor the viewpoint of the handheld device, in actuation because YAM’s arm, gripper, and control space have no counterpart in handheld data, and in environment because the demonstrations are collected in the wild and the policy runs in a robot cell the demonstrations never show (Fig. 42).

**中文:** 以往的 UMI 部署通过构造规避了这一问题，即采用一个复现手持设备相机和手指的机器人末端执行器（Chi et al., 2024）。而这里的目标机器人 YAM 不与手持设备共享这些组件，两种本体在三个方面同时存在差异：在感知上，YAM 的腕部相机与手持设备既不共用镜头，也不共用视点；在驱动上，YAM 的机械臂、夹爪和控制空间在手持数据中没有对应项；在环境上，演示是在野外采集的，而策略运行于演示中从未出现过的机器人工作单元（robot cell）中（Fig. 42）。

<a id="S947"></a>
**Source:** p.48 S947

**Original:** Closing this gap decouples data collection from the deployment platform, and the decoupling pays off along three axes. The first is generality: the same handheld demonstrations transfer to off-the-shelf robots with their own cameras, grippers, and controllers, so a task collected once need not be re-collected for each platform. The second is capability: the handheld device records motion at human speed with natural contact feedback, so dynamic skills such as tossing, which teleoperation renders slow and conservative, become learnable. The third is efficiency: adding a task requires no robot, no instrumented cell, and no operator training. Demonstrations are recorded in the wild after a few dozen minutes of setup, whereas teleoperation ties up a robot, a station, and a trained operator for the entire collection. The demonstration budget itself is small: with roughly 20 handheld episodes, the policy still completes Toy Dumptruck Assembly end to end (10% success, 81 progress) and still sorts 84% of the conveyor items on Conveyor Belt Sorting and Tossing, and even 10 episodes sort 70% (Tab. 17).

**中文:** 弥合这一差距使数据采集与部署平台解耦，而解耦的收益体现在三个方面。第一是通用性：同一套手持演示可以迁移到带有自身相机、夹爪和控制器的现成机器人上，因此一项任务只需采集一次，无需为每个平台重新采集。第二是能力：手持设备以人类速度记录动作，并保留自然的接触反馈，因此抛掷这类动态技能变得可以学习，而遥操作会使其变得缓慢而保守。第三是效率：增加一项任务不需要机器人、带仪器的工作单元，也不需要培训操作员。演示可以在几十分钟的准备之后，在野外录制；而遥操作会在整个采集过程中占用一台机器人、一个工位和一名受过训练的操作员。演示预算本身也很小：仅用约 20 个手持片段，策略仍能端到端完成 Toy Dumptruck Assembly（成功率 10%，进度 81），仍能分拣 Conveyor Belt Sorting and Tossing 中 84% 的传送带物品，即使只有 10 个片段也能分拣 70%（Tab. 17）。

<a id="S948"></a>
**Source:** p.48 S948

**Original:** What makes the transfer work. Three design choices carry the transfer, each closing one gap, and Sec. E.3 ablates all of them.

**中文:** 使迁移成功的关键。三项设计选择承担了迁移，每一项弥合一种差距，Sec. E.3 对它们逐一做了消融。

<a id="S949"></a>
**Source:** p.48 S949

**Original:** • Co-training with task-agnostic robot data closes the embodiment and scene gap. GR00T 2 is post-trained on the UMI demonstrations together with YAM teleoperation data from four general in-lab corpora that contain no episode of the target tasks, typically at a 0.6 : 0.4 ratio: the YAM data supply the embodiment and the scene, the UMI data supply the task. The effect is visible in the model’s own predictions, which render YAM’s arms rather than the demonstrator’s once YAM data are present (Fig. 14). • Aligning the wrist view closes the geometric part of the sensing gap. We re-render the UMI fisheye as a virtual pinhole camera that imitates YAM’s wrist view, fitted in Isaac Sim on 112 paired renders (Fig. 43). The alignment is only approximate, yet without it end-to-end success falls to 0% on both long-horizon tasks. • Sharing the action head grounds the task in the robot’s own action space. UMI actions are re-expressed in YAM’s semantics and decoded by YAM’s weights, so the task evidence lands directly in the statistics

**中文:** • 与任务无关的机器人数据的联合训练弥合了本体与场景差距。GR00T 2 在 UMI 演示之外，还与 YAM 遥操作数据一同进行后训练；这些数据来自四个通用的实验室内语料库，不包含任何目标任务片段，通常按 0.6 : 0.4 的比例混合：YAM 数据提供本体与场景，UMI 数据提供任务。这一效果可以从模型自身的预测中看出：一旦加入 YAM 数据，模型渲染出的是 YAM 的机械臂，而非演示者的手臂（Fig. 14）。• 对齐腕部视角弥合了感知差距中的几何部分。我们把 UMI 鱼眼图像重新渲染为一台模拟 YAM 腕部视角的虚拟针孔相机，并在 Isaac Sim 中利用 112 组成对渲染图进行拟合（Fig. 43）。这一对齐只是近似的，但若没有它，两项长时序任务的端到端成功率都会降至 0%。• 共享动作头使任务落在机器人自身的动作空间中。UMI 动作被重新表达为 YAM 的语义，并由 YAM 的权重解码，因此任务证据直接落入

<a id="C032"></a>
**Source:** p.49 C032 · 图 F029

**Original (caption):** Figure 29: Zero-teleop transfer from UMI to YAM. Each row shows one task with the language instruction GR00T 2 receives and six keyframes of a YAM rollout, numbered by stage: Toy Dumptruck Assembly, NIST Board Disassembly, and Conveyor Belt Sorting and Tossing. Every task is demonstrated only with the handheld Gripper UMI, and YAM has no teleoperation data of these tasks.

**中文图注：** 图 29：从 UMI 到 YAM 的零遥操作迁移。每一行展示一项任务，包括 GR00T 2 接收到的语言指令，以及一次 YAM rollout（轨迹采样）中按阶段编号的六个关键帧，任务依次为 Toy Dumptruck Assembly、NIST Board Disassembly，以及 Conveyor Belt Sorting and Tossing。每项任务都只通过手持 Gripper UMI 演示，而 YAM 没有这些任务的遥操作数据。

<a id="S950"></a>
**Source:** p.49 S950

![F029](assets/F029.png)

**Original:** the controller executes.

**中文:** 控制器执行。 [存疑：抽取断句，为 S949 的续句]

<a id="S951"></a>
**Source:** p.49 S951

**Original:** Tasks and protocol. We evaluate on three tasks (Fig. 29): Toy Dumptruck Assembly and NIST Board Disassembly, two long-horizon tasks, an assembly and a disassembly, that chain unscrewing, part removal, flipping, and drilling, and Conveyor Belt Sorting and Tossing, a dynamic task paced by the belt. Each task is demonstrated with 41 to 75 handheld episodes and co-trained with YAM teleoperation data that contain no episode of the target tasks. All models share the post-training recipe and step budget, and the policy predicts 48-step action chunks, of which 30 are executed.

**中文:** 任务与协议。我们在三项任务上进行评测（Fig. 29）：Toy Dumptruck Assembly 与 NIST Board Disassembly 是两项长时序任务，分别为装配与拆解，串联了拧螺丝、取出零件、翻转和钻孔；Conveyor Belt Sorting and Tossing 则是由传送带节奏限定的动态任务。每项任务使用 41 至 75 条手持片段进行演示，并与不包含任何目标任务片段的 YAM 遥操作数据联合训练。所有模型共享相同的后训练配方与步数预算，策略预测 48 步的动作块，其中 30 步被执行。

<a id="C033"></a>
**Source:** p.49 C033 · 表 T004

**Original (caption):** Table 4: Zero-teleop transfer from UMI to YAM. For each model, Prog. is the average substage score and SR the end-to-end success rate on YAM, both on a 0 to 100 scale. Every task is demonstrated only with Gripper UMI (41 to 75 episodes) and co-trained with task-agnostic YAM teleoperation data. All models share the post-training recipe and step budget. GR00T 2 w/o UMI pretraining starts from an earlier GR00T 2 pretraining checkpoint whose mixture contains no UMI data (Sec. E.2). Toy Dumptruck Assembly and NIST Board Disassembly use 10 trials. Conveyor Belt Sorting and Tossing scores each of 50 items as sorted or missed, so its SR is the share of items sorted and it has no separate progress score. The last row averages SR over the three tasks and therefore mixes this per-item rate with the per-trial success rates of the two long-horizon tasks. Bold marks the best Prog. and SR in each row.

**中文表注：** 表 4：从 UMI 到 YAM 的零遥操作迁移。对每个模型，任务进度（Prog.）为其在 YAM 上的平均子阶段得分，成功率（SR）为 YAM 上的端到端成功率，两者均采用 0 至 100 的标度。每项任务仅用 Gripper UMI 演示（41 至 75 条片段），并与不针对任务的 YAM 遥操作数据联合训练。所有模型共享相同的后训练配方与步数预算。GR00T 2 w/o UMI pretraining 从较早的 GR00T 2 预训练检查点开始，其混合数据不含 UMI 数据（Sec. E.2）。Toy Dumptruck Assembly 与 NIST Board Disassembly 使用 10 次试次。Conveyor Belt Sorting and Tossing 将 50 个物品各自计为已分拣或已遗漏，因此其成功率为已分拣物品的比例，且没有单独的任务进度得分。最后一行对三项任务的成功率取平均，因此把该任务的逐物品比例与两项长时序任务的逐试次成功率混在了一起。每行中最佳的任务进度与成功率以粗体标出。

<a id="S956"></a>
**Source:** p.49 S956

![T004](assets/T004.png)

**Original:** Results. With 41 to 75 handheld episodes per task, GR00T 2 reaches 60% and 50% end-to-end success on the two long-horizon tasks, with progress scores of 96 and 86, and sorts 86% of the 50 conveyor items, on a robot never teleoperated for any of these tasks, whereas the baselines 𝜋0.5, LingBot-VA, and GR00T 1.7 complete neither long-horizon task and sort at most 28% of the conveyor items (Tab. 4). The decisive ingredient lies upstream of the recipe: starting from a pretraining checkpoint without UMI data, with identical post-training data, drops success to 20% and 0% on the long-horizon tasks and the share of conveyor items sorted to 34%. A few dozen handheld demonstrations therefore suffice because the embodiments were aligned before post-training began. Sec. E.3 quantifies the three gaps and ablates each component of the recipe.

**中文:** 结果。每项任务使用 41 至 75 条手持片段，GR00T 2 在两项长时序任务上分别达到 60% 和 50% 的端到端成功率，进度得分分别为 96 与 86，并在 50 个传送带物品中分拣出 86%。这台机器人从未针对这些任务接受过遥操作。相比之下，基线 𝜋0.5、LingBot-VA 和 GR00T 1.7 在两项长时序任务上均未完成，分拣的传送带物品至多为 28%（Tab. 4）。决定性因素位于配方的上游：若从不含 UMI 数据的预训练检查点开始，并使用完全相同的后训练数据，则长时序任务的成功率降至 20% 和 0%，分拣比例降至 34%。因此，几十条手持演示就已足够，原因在于各本体在后训练开始之前已经对齐。Sec. E.3 量化了三类差距，并对配方的每个组件做了消融。

<a id="C034"></a>
**Source:** p.50 C034 · 表 T005

**Original (caption):** Table 5: DexUMI post-training results. Fraction of real-robot trials that reach the end of each subtask. Overall is the fraction that completes the whole task.

**中文表注：** 表 5：DexUMI 后训练结果。表示真实机器人试次中到达每个子任务终点的比例。Overall 表示完成整个任务的比例。

![T005](assets/T005.png)


<a id="H27"></a>
### B.3. DexUMI for Complex, Long-Horizon, and Dynamic Post-Training ｜ 面向复杂、长时序与动态后训练的 DexUMI

<a id="S964"></a>
**Source:** p.50 S964

**Original:** DexUMI (Xu et al., 2025) extends UMI from parallel grippers to five-fingered hands. We use the GEAR DexUMI exoskeleton (NVIDIA GEAR Team, 2026), which replicates the kinematics, contact surfaces, and camera mount of the XHAND1 Pro-U robot hand, so that every recorded finger joint, fingertip force, and camera view has a robot counterpart. Unlike the original DexUMI, which sensed force with force-sensitive resistors and removed the exoskeleton from video with SAM2 and ProPainter, GEAR DexUMI maps its 16 degrees of freedom one-toone onto the robot’s joints (Sec. E.4), measures three-axis fingertip force in the robot hand’s own tactile format, and leaves the video unedited (Sec. E.6). DexUMI provides post-training data for complex, long-horizon, and dynamic dexterous tasks, which GR00T 2 learns with compliance labels derived from fingertip force (Eqs. (1) and (3)).

**中文:** DexUMI（Xu et al., 2025）把 UMI 从平行夹爪扩展到了五指手。我们使用 GEAR DexUMI 外骨骼（NVIDIA GEAR Team, 2026），它复现了 XHAND1 Pro-U 机器人手的运动学、接触面和相机安装件，因此每一个被记录的手指关节、指尖力和相机视角都在机器人上有对应量。原版 DexUMI 用力敏电阻感知力，并用 SAM2 和 ProPainter 从视频中去除外骨骼；与之不同，GEAR DexUMI 将其 16 个自由度一一映射到机器人关节上（Sec. E.4），以机器人手自身的触觉格式测量三轴指尖力，并保持视频不做编辑（Sec. E.6）。DexUMI 为复杂、长时序且动态的灵巧任务提供后训练数据，GR00T 2 利用由指尖力推导出的柔顺性标签（Eqs. (1) and (3)）来学习这些任务。

<a id="S965"></a>
**Source:** p.50 S965

**Original:** Because the exoskeleton replicates the robot hand, we post-train GR00T 2 from the GR00T 2 pretraining checkpoint (Sec. E.5) on DexUMI demonstrations alone, without robot play data, and evaluate it on three bimanual tasks on a Tianji robot with two 7-DoF arms and two XHAND1 Pro-U hands (Fig. 30). Prepare Banana Yogurt and Scoop Granola are the two halves of a long make-breakfast task. One policy learns both, and each half is evaluated separately. Fire Chemistry is a short, dynamic tool task: the robot strikes a match, lights a lamp under a flask with it, and puts the match out in water. Each task is scored by subtask:

**中文:** 由于外骨骼复现了机器人手，我们仅使用 DexUMI 演示数据、不使用机器人 play 数据（自由操作数据），从 GR00T 2 预训练检查点（Sec. E.5）出发对 GR00T 2 进行后训练，并在一台配备两条 7 自由度手臂和两只 XHAND1 Pro-U 手的 Tianji 机器人上，评测三项双臂任务（Fig. 30）。准备香蕉酸奶（Prepare Banana Yogurt）与舀取格兰诺拉麦片（Scoop Granola）是一个长时序“做早餐”任务的两半，同一个策略同时学习这两部分，并分别进行评测。火焰化学（Fire Chemistry）是一个短时、动态的工具任务：机器人划燃火柴，用火柴点亮灯下的烧瓶，然后把火柴丢进水中熄灭。每项任务按子任务逐项计分：

<a id="S966"></a>
**Source:** p.50 S966

**Original:** • Prepare Banana Yogurt: (1) place a banana on the cutting board, (2) draw a knife from the knife block, slice the banana, set the knife down, and lift the lid off a bowl of yogurt, (3) drop the banana pieces into the bowl and move the bowl onto the board in the center of the table. • Scoop Granola: (1) pick up the granola jar, pass it to the other hand, and unscrew its lid, (2) grab a spatula and scoop granola from the jar into the bowl, (3) pass the jar back and set it down on the table. • Fire Chemistry: (1) pull a long match from its holder, pick up the matchbox with the other hand, and strike the match on it, (2) light the lamp with the match and put the match out in a cup of water.

**中文:** • 准备香蕉酸奶：（1）把香蕉放在切菜板上，（2）从刀座中抽出刀，切开香蕉，放下刀，再掀开一碗酸奶的盖子，（3）把香蕉块放入碗中，并把碗移到桌子中央的切菜板上。• 舀取格兰诺拉麦片：（1）拿起格兰诺拉麦片罐，递给另一只手，并拧开罐盖，（2）拿起铲子，把麦片从罐中舀进碗里，（3）把罐子递回去，放在桌上。• 火焰化学：（1）从火柴架上抽出一根长火柴，另一只手拿起火柴盒，并在盒上划燃火柴，（2）用火柴点亮灯，然后把火柴放入一杯水中熄灭。

<a id="S967"></a>
**Source:** p.50 S967

**Original:** The tasks combine tool use (a knife, a spatula, and a match), hand-to-hand transfers, contact-rich twisting to unscrew a lid, and a fast strike that must ignite the match.

**中文:** 这些任务综合了工具使用（小刀、铲子和火柴）、手与手之间的传递、用于拧开盖子的富接触旋拧动作，以及必须能点燃火柴的快速击划动作。

<a id="S968"></a>
**Source:** p.50 S968

**Original:** Baselines and evaluation. We compare GR00T 2 with two vision-language-action models, GR00T 1.7 and 𝜋0.5 (Physical Intelligence et al., 2025). Each starts from its own pretrained model and is post-trained on DexUMI demonstrations of the same tasks with GR00T 2’s data recipe: the same action space, normalization, and prompts. We report the fraction of trials that reach the end of each subtask and the fraction that completes the whole task (Tab. 5).

**中文:** 基线与评测。我们将 GR00T 2 与两个视觉-语言-动作（VLA）模型 GR00T 1.7 和 π0.5（Physical Intelligence et al., 2025）进行比较。每个基线都从其各自的预训练模型出发，并使用 GR00T 2 的数据配方，即相同的动作空间、归一化方式和提示词，在相同任务的 DexUMI 演示数据上进行后训练。我们报告到达每个子任务终点的试次比例，以及完成整个任务的试次比例（Tab. 5）。

<a id="C035"></a>
**Source:** p.51 C035 · 图 F030

![F030](assets/F030.png)

**Original (caption):** Figure 30: DexUMI tasks. Each block shows one task with six keyframes, numbered by subtask as in Tab. 5: a person demonstrating the task with the DexUMI exoskeletons (top) and a GR00T 2 rollout on a Tianji robot with XHAND1 Pro-U hands (bottom). Prepare Banana Yogurt and Scoop Granola are the two halves of one continuous make-breakfast demonstration and rollout, and every task is demonstrated only with DexUMI.

**中文图注：** Figure 30：DexUMI 任务。每个区块展示一项任务的六个关键帧，按 Tab. 5 中的子任务编号排列：上排为人使用 DexUMI 外骨骼演示该任务，下排为 GR00T 2 在配备 XHAND1 Pro-U 手的 Tianji 机器人上的 rollout（轨迹采样）。准备香蕉酸奶与舀取格兰诺拉麦片是一段连续“做早餐”演示与 rollout 的两半，且每项任务都只用 DexUMI 演示。

<a id="S969"></a>
**Source:** p.52 S969

**Original:** GR00T 2 performs all three tasks from DexUMI demonstrations alone: it completes Prepare Banana Yogurt, Scoop Granola, and Fire Chemistry in 60%, 80%, and 75% of trials, whereas GR00T 1.7 and 𝜋0.5 complete no trial of any task.

**中文:** GR00T 2 仅凭 DexUMI 演示即可完成全部三项任务：它分别在 60%、80% 和 75% 的试次中完成准备香蕉酸奶、舀取格兰诺拉麦片和火焰化学；而 GR00T 1.7 和 π0.5 在任何任务中都没有完成一次试次。

<a id="S970"></a>
**Source:** p.52 S970

**Original:** While DexUMI captures detailed data of human manipulation motion, using position label alone is not sufficient to describe the human manipulation strategy. Two more pieces of information are required: the force being applied, and the compliance profile being used. Force encourages forming and maintaining the desired contact modes, while a suitable compliance profile make the manipulation robust against positional uncertainties and even disturbance forces. We adopt the Adaptive Compliance Policy (ACP) (Hou et al., 2025) to give our policy the ability to reason about force and compliance: the DexUMI collected force/motion data are converted offline to stiffness and virtual target labels used to augment the policy action vector. In GR00T 2, we adapt the original ACP formulation for dexterous hands:

**中文:** 尽管 DexUMI 能够捕捉人类操作动作的细节数据，但仅用位置标签不足以描述人类的操作策略，还需要两类信息：所施加的力，以及所用的柔顺性配置（compliance profile）。力有助于形成并维持期望的接触模式，而合适的柔顺性配置使操作能够抵抗位置不确定性，甚至干扰力。我们采用自适应柔顺策略（ACP）（Hou et al., 2025），使策略具备对力和柔顺性进行推理的能力：DexUMI 采集的力/运动数据被离线转换为刚度与虚拟目标标签，用于扩充策略的动作向量。在 GR00T 2 中，我们将原始 ACP 公式改造为适用于灵巧手的形式：

<a id="S971"></a>
**Source:** p.52 S971

**Original:** Joint space action formulation. The original ACP assumes Cartesian pose as the robot’s action, and works the best when the robot has six or more degrees-of-freedoms (DOFs). For dexterous hands with typically three to five joints per finger, the Cartesian space ACP formulation could produce actions that the hand cannot execute. Instead, we define the ACP action in joint space, including position target, virtual target and stiffness.

**中文:** 关节空间动作表述。原始 ACP 假设机器人的动作为笛卡尔位姿，并且在机器人具有六个或更多自由度（DoF）时效果最好。对于每根手指通常只有三到五个关节的灵巧手，笛卡尔空间的 ACP 表述可能产生手无法执行的动作。因此，我们改为在关节空间中定义 ACP 动作，包括位置目标、虚拟目标和刚度。

<a id="S972"></a>
**Source:** p.52 S972

**Original:** Joint torque as the unified hand force representation. Different hand or DexUMI hardware may use different force sensing solutions, such as joint torque sensor, force-torque sensor, or tactile sensors. To work with our joint space action, we choose joint torque as the unified force representation for dexterous hands, and project the Cartesian space force measurements, if any, back to the joint space. In the case of the XHAND1 Pro-U, force 𝑓𝑖,𝑡is estimated for each finger 𝑖from the fingertip tactile sensors, with exponential moving average and a 0.1N cutoff. The fingertip force is then projected onto the actuated joints through the robot hand’s Jacobians, where 𝑞𝑡denotes the finger joint configuration, 𝐵maps the actuated joints to the full configuration. We augment the policy action space with the predicted finger joint torque.

**中文:** 以关节力矩作为统一的手部力表示。不同的手或 DexUMI 硬件可能采用不同的力感知方案，例如关节力矩传感器、力-力矩传感器或触觉传感器。为了与关节空间动作配合，我们选择关节力矩作为灵巧手的统一力表示，并将笛卡尔空间的力测量（如果有的话）投影回关节空间。对于 XHAND1 Pro-U，每根手指 𝑖 的力 𝑓𝑖,𝑡 由指尖触觉传感器估计，并经过指数滑动平均和 0.1N 的截止值处理。随后，指尖力通过机器人手的雅可比矩阵（Jacobians）投影到驱动关节上，其中 𝑞𝑡 表示手指关节构型，𝐵 将驱动关节映射到完整构型。我们用预测的手指关节力矩扩充策略动作空间。[公式原文见 p.52]

<a id="S977"></a>
**Source:** p.52 S977

**Original:** Stiffness and virtual targets. Following ACP, we scale the time-varying per joint stiffness value based on the joint torque magnitude:

**中文:** 刚度与虚拟目标。遵循 ACP，我们根据关节力矩的大小，缩放随时间变化的各关节刚度值：

<a id="E001"></a>
**Source:** p.52 E001

![E001](assets/equations/E001.png)

**Original:** 𝐾eff = 𝑠acp 𝑘𝑝, (2)

**中文:** 式 (2) 给出有效刚度 𝐾eff 的计算方式，即默认位置增益 𝑘𝑝 与自适应因子 𝑠acp 的乘积。公式本体：$$𝐾eff = 𝑠acp 𝑘𝑝, (2)$$ [公式原文见 p.52]

<a id="S978"></a>
**Source:** p.52 S978

**Original:** where 𝑘𝑝is the default position gain of the joint, 𝑠acp is the adaptive factor that falls linearly from 1.0 to 𝑠min = 0.3 as joint torque 𝜏𝑡rises from 0.1 to 0.4 N m, softening the hand under load. The intuition is that large force can only come from rigid contacts, for which the robot needs to exhibit more compliance. With the policy predicting both position and force, the stiffness 2 is computed online, then used to update the position set point. This is the virtual target 𝑎𝑡in ACP:

**中文:** 其中 𝑘𝑝 是该关节的默认位置增益，𝑠acp 是自适应因子，它随关节力矩 𝜏𝑡 从 0.1 增大到 0.4 N m 而线性地从 1.0 下降到 𝑠min = 0.3，从而使手在负载下变软。其直觉是，较大的力只能来自刚性接触，此时机器人需要表现出更强的柔顺性。策略同时预测位置和力之后，刚度 2 被在线计算，再用于更新位置设定点。这就是 ACP 中的虚拟目标 𝑎𝑡。[存疑：“刚度 2”中的 “2” 疑为抽取残缺的符号] [公式原文见 p.52]

<a id="S985"></a>
**Source:** p.52 S985

**Original:** The hand can achieve the predicted force when tracking the virtual target with the computed stiffness 𝐾eff.

**中文:** 当手以计算得到的刚度 𝐾eff 跟踪虚拟目标时，手即可实现预测的力。[公式原文见 p.52]

<a id="H28"></a>
### B.4. DexUMI →Tianji + Sharpa ｜ 从 DexUMI 到 Tianji + Sharpa 的迁移

<a id="S986"></a>
**Source:** p.52 S986

**Original:** GR00T 2 can also learn a task on a dexterous hand from demonstrations recorded with an exoskeleton built for a different hand. The DexUMI exoskeleton replicates the 16-DoF XHAND1 Pro-U hand (Sec. B.3), and the policy runs on the Tianji, a bimanual robot with two 7-DoF arms and two 22-DoF Sharpa hands. Kinematics differ because the Sharpa hand has a different joint layout from the XHAND, with 22 degrees of freedom instead of 16, so the recorded joint angles must be retargeted before they can be used as Sharpa commands. Camera viewpoints differ because the wrist cameras are mounted on the DexUMI wrist during data collection and on the Sharpa wrist during evaluation, and because the head camera is worn by the operator during data collection but fixed on the robot during evaluation. Appearance differs because the demonstrations show the exoskeleton and the operator’s arms.

**中文:** GR00T 2 还能在灵巧手上学习任务，所用的演示由为另一种手设计的外骨骼录制。DexUMI 外骨骼复现的是 16 自由度的 XHAND1 Pro-U 手（Sec. B.3），而策略运行在 Tianji 上。Tianji 是一台双臂机器人，配备两条 7 自由度手臂和两只 22 自由度的 Sharpa 手。运动学存在差异，因为 Sharpa 手的关节布局与 XHAND 不同，自由度为 22 而非 16，因此录制的关节角在用作 Sharpa 指令之前必须先经过重定向。相机视角也存在差异：采集数据时腕部相机安装在 DexUMI 手腕上，评测时则安装在 Sharpa 手腕上；头部相机在采集数据时由操作员佩戴，评测时则固定在机器人上。外观同样不同，因为演示画面中会出现外骨骼以及操作员的手臂。

<a id="S988"></a>
**Source:** p.53 S988

**Original:** We evaluate on two tasks. Microscope Slide Dabbing is the chemistry-lab task of the same name in Fig. 26. In Conveyor Package Selection and Tossing, the robot must pick out the packages from mixed objects on a moving belt and toss them into the bin, leaving the other objects untouched on the belt. Each task is demonstrated with 100 DexUMI episodes and co-trained with Tianji + Sharpa play data that contain no demonstration of the target task. We compare against GR00T 1.7 and 𝜋0.5 (Physical Intelligence et al., 2025), post-trained on the same data with the same recipe. GR00T 2 succeeds in 60% and 65% of 20 trials, whereas neither baseline completes a single trial (Tab. 6).

**中文:** 我们在两项任务上进行评测。Microscope Slide Dabbing（显微镜载玻片蘸取）是 Fig. 26 中同名的化学实验室任务。在 Conveyor Package Selection and Tossing（传送带包裹挑选与投掷）中，机器人必须从移动传送带上的混合物体中挑出包裹并投入箱中，同时不触碰传送带上的其他物体。每项任务都用 100 条 DexUMI 演示片段（episode）进行演示，并与不包含目标任务演示的 Tianji + Sharpa play 数据联合训练。我们与 GR00T 1.7 和 π0.5（Physical Intelligence et al., 2025）进行比较，两者在相同数据和相同配方下进行后训练。GR00T 2 在 20 次试次中分别成功 60% 和 65%，而两个基线都没有完成一次试次（Tab. 6）。

<a id="S989"></a>
**Source:** p.53 S989

**Original:** In the DexUMI experiments above, the exoskeleton replicates the robot hand joint for joint, so the recorded joint angles are used directly as hand commands. This setting corresponds to UMI direct (Sec. E.2). Here we use DexUMI demonstrations on a hand that the exoskeleton does not replicate, the 22-DoF Sharpa hand on the Tianji, which is the robot used in the human-to-robot experiments (Sec. B.1). This setting corresponds to UMI →YAM transfer (Sec. B.2), and it avoids building a separate exoskeleton for each robot hand.

**中文:** 在上文的 DexUMI 实验中，外骨骼与机器人手逐关节一一对应，因此录制的关节角直接用作手部指令，该设定对应于 UMI direct（Sec. E.2）。这里我们则在外骨骼并未复现的手上使用 DexUMI 演示，即 Tianji 上的 22 自由度 Sharpa 手，它也是人到机器人实验中所用的机器人（Sec. B.1）。该设定对应于 UMI →YAM 迁移（Sec. B.2），并且避免了为每种机器人手单独制作外骨骼。

<a id="S990"></a>
**Source:** p.53 S990

**Original:** The recorded joint angles and fingertip forces correspond to the XHAND. The force labels (Eq. (1)) are computed with the XHAND Jacobians and do not apply to the Sharpa hand, so the policy is trained on joint positions only, and the hand tracks position targets in its admittance mode with fixed gains.

**中文:** 录制的关节角和指尖力对应的是 XHAND。力标签（Eq. (1)）是用 XHAND 的雅可比矩阵计算的，不适用于 Sharpa 手，因此策略仅在关节位置上训练，手则以固定增益在其导纳模式下跟踪位置目标。

<a id="S991"></a>
**Source:** p.53 S991

**Original:** Fingertip retargeting. We compute fingertip positions from the recorded joint angles with the XHAND forward kinematics and treat them as the fingertip readings of a motion-capture glove. The closed-form geometric solver used for glove teleoperation (Sec. B.1.2) then places the Sharpa fingertips at these positions, with the two hands aligned at the thumb-index pinch point, and solves the 7-DoF arm for the resulting hand pose. The thumb, index, middle, and ring fingertips are matched to their targets, and the pinky follows the alignment of the hand.

**中文:** 指尖重定向。我们用 XHAND 的正向运动学，从录制的关节角计算指尖位置，并把这些位置视为动作捕捉手套的指尖读数。随后，用于手套遥操作的闭式几何求解器（Sec. B.1.2）将 Sharpa 指尖放置到这些位置，并使两只手在拇指-食指捏合点处对齐，再求解 7 自由度手臂，以得到相应的手部位姿。拇指、食指、中指和无名指的指尖与其目标匹配，小指则跟随手部的对齐关系。

<a id="S992"></a>
**Source:** p.53 S992

**Original:** Wrist-view reprojection. The wrist cameras are mounted differently on the DexUMI and Sharpa wrists, and retargeting also changes the wrist pose. As a result, the Sharpa wrist camera ends up about 31∘away from the DexUMI wrist camera. We calibrate both camera mounts by hand-eye calibration, solving for each camera’s pose relative to the wrist from its image motion and the tracked wrist motion. We then reproject each DexUMI wrist frame into the Sharpa wrist camera, mapping each pixel through a fronto-parallel plane at the depth of the pinch point. During training, random rotations and zooms of the wrist views account for the remaining calibration error.

**中文:** 腕部视角重投影。DexUMI 与 Sharpa 手腕上的腕部相机安装方式不同，而重定向还会改变腕部位姿。因此，Sharpa 腕部相机最终与 DexUMI 腕部相机相差约 31∘。我们通过手眼标定（hand-eye calibration）分别标定两个相机的安装，即根据相机的图像运动与被跟踪的腕部运动，求出每个相机相对于腕部的位姿。随后，我们将每一帧 DexUMI 腕部图像重投影到 Sharpa 腕部相机中：每个像素都通过位于捏合点深度处、与正视平面平行的平面进行映射。训练时，腕部视图的随机旋转和缩放用于吸收剩余的标定误差。

<a id="S993"></a>
**Source:** p.53 S993

**Original:** Co-training with robot play data. The converted demonstrations use the robot’s 62-D state and action, consisting of relative wrist poses and absolute Sharpa joint positions, as in the human-to-robot pipeline (Sec. B.1.3). We resample them from 45 to 30 Hz and assign them the robot’s embodiment tag, so that they share its action encoder, action decoder, and normalization statistics. They are co-trained with Tianji + Sharpa play data that contain no demonstration of the target task, sampled 75 : 25 for slide dabbing and 50 : 50 for package selection and tossing.

**中文:** 与机器人 play 数据联合训练。转换后的演示使用机器人的 62 维状态与动作，由相对腕部位姿和绝对 Sharpa 关节位置组成，与人到机器人的流程（Sec. B.1.3）保持一致。我们将其从 45 Hz 重采样到 30 Hz，并赋予机器人的本体标签（embodiment tag），从而使其与机器人共享动作编码器、动作解码器和归一化统计量。它们与不包含目标任务演示的 Tianji + Sharpa play 数据联合训练，其中载玻片蘸取任务的采样比为 75 : 25，包裹挑选与投掷任务的采样比为 50 : 50。

<a id="S995"></a>
**Source:** p.53 S995

**Original:** Evaluation. Microscope Slide Dabbing is scored with the rubric of Sec. B.1.4, and a trial succeeds when it completes every stage. A Conveyor Package Selection and Tossing trial succeeds when the packages are tossed into the bin and no other object is touched. Any human intervention counts as a failure. GR00T 1.7 and 𝜋0.5 each start from their own pretrained model and share the post-training mixture, recipe, and step budget of GR00T 2. We report the fraction of 20 trials per task that complete the whole task (Tab. 6).

**中文:** 评测。Microscope Slide Dabbing 使用 Sec. B.1.4 的评分细则进行评分，试次完成每个阶段即判为成功。Conveyor Package Selection and Tossing 的试次在包裹被投入箱中且未触碰其他物体时判为成功。任何人工干预都计为失败。GR00T 1.7 和 π0.5 各自从其预训练模型出发，并与 GR00T 2 共享后训练数据配比、配方和步数预算。我们报告每项任务 20 次试次中完成整个任务的比例（Tab. 6）。


<a id="H29"></a>
### B.5. Human →Simulation →Tianji + Sharpa ｜ B.5. 人类 →仿真 →Tianji + Sharpa

<a id="S996"></a>
**Source:** p.53 S996

**Original:** Despite their broad capabilities, WAMs still struggle with contact-rich dexterous manipulation, such as in-hand object reorientation. Reinforcement learning (RL) in simulation offers a complementary source of skills, including forceful tool use, precise contact interactions, and recovery behaviors that are difficult to demonstrate

**中文:** 尽管 WAM 能力广泛，它们在富接触的灵巧操作上仍然吃力，例如手内物体重定向。强化学习（RL）在仿真中可以提供另一类互补的技能，包括用力的工具使用、精确的接触交互，以及一些难以演示的恢复行为。

<a id="C036"></a>
**Source:** p.54 C036 · 表 T006

![T006](assets/T006.png)

**Original (caption):** Table 6: DexUMI →Tianji + Sharpa results. Fraction of real-robot trials that complete the whole task, over 20 trials per task. No training data contain a robot trajectory of either task.

**中文表注：** 表 6：DexUMI →Tianji + Sharpa 的结果。表中为每个任务在 20 次试次中，真机完整完成任务的比例。训练数据中没有任何一项任务的机器人轨迹。

<a id="S999"></a>
**Source:** p.54 S999

**Original:** reliably through teleoperation or kinematic retargeting. We introduce a human-to-sim-to-real pipeline that enables GR00T 2 to acquire these skills from a single human demonstration video per task.

**中文:** 这些行为很难通过遥操作或运动学重定向可靠地演示出来。我们提出一条人类到仿真再到现实（human-to-sim-to-real）的流程，使 GR00T 2 只需每个任务一段人类演示视频，就能习得这些技能。

<a id="S1000"></a>
**Source:** p.54 S1000

**Original:** Building on NVIDIA’s Video to Data (V2D) (NVIDIA, 2026b) pipeline, we reconstruct 3D object assets, hand– object motion, and contacts from stereo video, then train a state-based RL expert using CHORD (Zhu et al., 2026). We collect expert demonstrations with native simulation rendering, physical and visual randomization, and state perturbations that broaden state coverage and elicit recovery behaviors beyond nominal trajectories. Fig. 16 illustrates the full pipeline.

**中文:** 基于 NVIDIA 的 Video to Data（V2D）（NVIDIA, 2026b）流程，我们从立体视频中重建三维物体资产、手-物体运动和接触，然后使用 CHORD（Zhu et al., 2026）训练一个基于状态的 RL 专家。我们借助原生仿真渲染、物理与视觉随机化，以及状态扰动来采集专家演示。这些状态扰动扩大了状态覆盖范围，并引发超出标称轨迹的恢复行为。Fig. 16 展示了完整流程。

<a id="S1001"></a>
**Source:** p.54 S1001

**Original:** We fine-tune GR00T 2’s diffusion transformer (DiT) on 1.5K simulation episodes, incorporating training-time Real-Time Chunking (RTC) for continuous execution. The resulting policy is deployed zero-shot using RGB observations, robot state, and task instructions, without additional real-world robot data or scene-specific reconstruction or alignment. By expanding one human demonstration into diverse robot rollouts, this approach provides a scalable source of dexterous manipulation data. We hypothesize that GR00T 2’s pretrained priors support compositional generalization: fine-tuning combines simulation-learned contact-rich skills with the perceptual and behavioral knowledge acquired during large-scale pretraining.

**中文:** 我们在 1.5K 个仿真回合（episode）上微调 GR00T 2 的扩散 Transformer（DiT），并引入训练时实时分块（RTC）以实现连续执行。得到的策略以 RGB 观测、机器人状态和任务指令进行零样本部署，无需额外的真实机器人数据，也无需针对具体场景的重建或对齐。通过把一段人类演示扩展为多样的机器人 rollout（轨迹采样），该方法提供了一个可扩展的灵巧操作数据来源。我们假设 GR00T 2 的预训练先验支持组合泛化：微调把仿真中习得的富接触技能，与大规模预训练期间获得的感知和行为知识结合起来。

<a id="S1002"></a>
**Source:** p.54 S1002

**Original:** We evaluate nail hammering, flask handover, and table sweeping, comparing GR00T 2 against GR00T 1.7 and 𝜋0.5. GR00T 2 demonstrates successful transfer of dexterous manipulation skills from simulation to the real world. Although 𝜋0.5 performs well in simulation, its real-world execution is limited to grasping and lifting, with no successful completion of the full tasks, which require subsequent reorientation and object interactions.

**中文:** 我们评测了钉钉子、递交烧瓶和桌面清扫三项任务，并将 GR00T 2 与 GR00T 1.7 和 π0.5 进行比较。GR00T 2 展示了灵巧操作技能从仿真到真实世界的成功迁移。尽管 π0.5 在仿真中表现良好，但其真机执行仅限于抓取和提起，没有一项能完整完成任务，而完整任务还需要后续的重定向和物体交互。

<a id="S1003"></a>
**Source:** p.54 S1003

**Original:** Human and Object Reconstruction. Stable simulation and policy training require accurate, geometrically consistent reconstructions of hand motion, object trajectories, and their contacts. Independent estimates of hands and objects can be inconsistent, particularly when the supplied object mesh differs from the object observed in the video. We use V2D’s agentic pipeline for 4D hand-object reconstruction, coordinating tools such as SAM3 (Carion et al., 2025), FoundationPose (Wen et al., 2024), and GATOR (Wu et al., 2026) for segmentation, object tracking, and hand tracking. To resolve geometric inconsistencies, the reconstructed hands are refined against the supplied object mesh while keeping the mesh and reference object motion fixed. Contact-wrench objectives and geometric checks guide alignment, followed by penetration correction and finger repair. This formulation adapts hand configurations and contact locations to the supplied geometry while targeting the interaction’s mechanical effect on the object. These anchors provide persistent references for downstream robotic grounding. Evaluated on 15 stereo trajectories from SHOW3D (Rim et al., 2026), a dataset of hand-object interactions captured in the wild with annotated 3D hand and object poses, the reconstruction pipeline achieves an average hand reconstruction error of 17.5 mm and an object Chamfer distance of 3.0 mm.

**中文:** 人与物体重建。稳定的仿真与策略训练需要对手部运动、物体轨迹及其接触进行准确且几何一致的重建。手和物体的独立估计可能彼此不一致，尤其是在所给的物体网格与视频中观察到的物体不同时。我们使用 V2D 的智能体化（agentic）流程进行四维（4D）手-物体重建，协调 SAM3（Carion et al., 2025）、FoundationPose（Wen et al., 2024）和 GATOR（Wu et al., 2026）等工具，分别完成分割、物体跟踪和手部跟踪。为解决几何不一致问题，重建得到的手部在保持网格和参考物体运动固定的前提下，相对于所给物体网格进行细化。接触力旋量目标和几何检查引导对齐，随后进行穿透修正和手指修复。该公式使手部构型和接触位置适应所给几何，同时以交互对物体产生的力学效果为目标。这些锚点为下游机器人落地提供持续的参照。在 SHOW3D（Rim et al., 2026）的 15 条立体轨迹上评估（该数据集为真实场景中采集的手-物体交互，带有标注的三维手部与物体位姿），重建流程的平均手部重建误差为 17.5 mm，物体 Chamfer 距离为 3.0 mm。

<a id="S1004"></a>
**Source:** p.54 S1004

**Original:** RL in Simulation. Using the reconstructed object assets and trajectories, we train a state-based RL expert to perform dexterous manipulation in simulation. The policy observes privileged robot and object states and outputs arm and hand joint targets. Training follows CHORD, with a warm-up procedure following SimToolReal (Kedia et al., 2026).

**中文:** 仿真中的强化学习（RL）。利用重建得到的物体资产和轨迹，我们在仿真中训练一个基于状态的 RL 专家来完成灵巧操作。该策略观测特权的机器人与物体状态，输出手臂和手部的关节目标。训练遵循 CHORD，并采用 SimToolReal（Kedia et al., 2026）的预热（warm-up）流程。

<a id="S1005"></a>
**Source:** p.54 S1005

**Original:** We calibrate the simulated robot’s joint dynamics through system identification of stiffness, damping, armature, friction, and delay. To improve robustness to physical variation, we randomize robot dynamics, object properties, and scene geometry during training. We also vary initial robot and object configurations, fixture geometry, and table dimensions, while ensuring valid, collision-free initialization.

**中文:** 我们通过对刚度、阻尼、转子惯量（armature）、摩擦和延迟进行系统辨识，来标定仿真机器人的关节动力学。为提高对物理变化的鲁棒性，训练期间我们随机化机器人动力学、物体属性和场景几何。我们还改变机器人与物体的初始构型、夹具几何和桌面尺寸，同时保证初始化有效且无碰撞。

<a id="C037"></a>
**Source:** p.55 C037 · 图 F031

![F031](assets/F031.png)

**Original (caption):** Figure 31: GR00T 2 learns dexterous manipulation through human-to-sim-to-real transfer. Starting from a single human demonstration per task captured with an egocentric stereo camera, the Video-to-Data pipeline generates simulation data for SFT of GR00T 2. The resulting policies transfer zero-shot to the real world on Hammer Nail, Handover Flask, and Brushing Trash, demonstrating dexterous in-hand object reorientation, handover, tool use, and bimanual coordination.

**中文图注：** GR00T 2 通过人类到仿真再到现实的迁移学习灵巧操作。每个任务从一段用第一人称视角立体相机（egocentric stereo camera）采集的人类演示出发，Video-to-Data 流程为 GR00T 2 的 SFT 生成仿真数据。所得策略以零样本方式迁移到真实世界，完成敲钉（Hammer Nail）、递交烧瓶（Handover Flask）和扫纸屑（Brushing Trash）三项任务，展示了灵巧的手内物体重定向、递交、工具使用以及双臂协调。

<a id="S1006"></a>
**Source:** p.55 S1006

**Original:** The reward follows CHORD (Zhu et al., 2026) and combines task execution, motion regularization, and contact quality to encourage reliable, human-like tool interactions. Task rewards include keypoint-based tracking of the demonstrated object trajectory, subgoal completion, task progress, and terminal success. Joint-speed penalties regularize motion. Contact rewards use contact wrenches to encourage human-like grasps, improve grasp quality, and sustain object holding. We optimize the policy using a PPO-based SAPG (Singla et al., 2024).

**中文:** 奖励遵循 CHORD（Zhu et al., 2026），综合任务执行、运动正则化和接触质量，以鼓励可靠、类人的工具交互。任务奖励包括基于关键点跟踪演示物体轨迹的奖励、子目标完成、任务进度以及终止时的成功。关节速度惩罚用于正则化运动。接触奖励使用接触力旋量，以鼓励类人的抓取、提高抓取质量并维持对物体的持握。我们使用基于 PPO 的 SAPG（Singla et al., 2024）优化策略。

<a id="S1007"></a>
**Source:** p.55 S1007

**Original:** Harvest Dexterity from Simulation. We convert the RL expert’s skills into demonstrations for supervised fine-tuning (SFT). Each rollout records RGB observations, robot states, expert actions, and task instructions. The privileged tool and goal keypoints available to the RL expert are excluded from GR00T 2’s inputs. We continue to randomize physical properties and scene configurations during collection to capture expert behavior across diverse conditions.

**中文:** 从仿真中获取灵巧性。我们把 RL 专家的技能转化为用于监督微调（SFT）的演示。每条 rollout（轨迹采样）记录 RGB 观测、机器人状态、专家动作和任务指令。RL 专家可用的特权工具关键点与目标关键点不纳入 GR00T 2 的输入。采集过程中，我们持续随机化物理属性和场景配置，以捕获专家在多样条件下的行为。

<a id="S1008"></a>
**Source:** p.55 S1008

**Original:** To broaden state coverage and capture recovery behavior, we introduce random-action bursts, object teleports, and robot-joint teleports during data collection. These perturbations move the system away from nominal trajectories and elicit corrective behavior from the expert. The resulting demonstrations cover states that GR00T 2 may encounter when its own actions deviate, helping mitigate the narrow state coverage and compounding errors observed with naive expert-rollout collection.

**中文:** 为扩大状态覆盖并捕获恢复行为，我们在数据采集时引入随机动作脉冲、物体瞬移和机器人关节瞬移。这些扰动使系统偏离标称轨迹，并引发专家的纠正行为。由此得到的演示覆盖了 GR00T 2 自身动作发生偏差时可能遇到的状态，有助于缓解朴素专家 rollout 采集中观察到的状态覆盖面窄和误差累积问题。

<a id="S1009"></a>
**Source:** p.55 S1009

**Original:** We also randomize visual appearance using native Isaac Lab (Mittal et al., 2025) rendering, without visual inpainting or style transfer models. Randomization covers object and scene colors, textures, material properties, illumination, environment lighting, and camera calibration. Small perturbations to camera poses and intrinsics model calibration uncertainty, while image noise models sensor variation.

**中文:** 我们还使用原生 Isaac Lab（Mittal et al., 2025）渲染对视觉外观进行随机化，未使用视觉补全（inpainting）或风格迁移模型。随机化涵盖物体与场景的颜色、纹理、材质属性、光照、环境照明和相机标定。相机位姿与内参的微小扰动用于模拟标定不确定性，图像噪声则用于模拟传感器差异。

<a id="S1010"></a>
**Source:** p.55 S1010

**Original:** SFT with Simulation Data. We fine-tune GR00T 2 for each task using 1.5k simulation episodes, sourced from one human demonstration video. During SFT, we update the DiT, retain the pretrained action normalization statistics, and freeze the action decoder and video output projection. The fine-tuned policy is deployed zero-shot in the real world using RGB observations, robot state, and a task instruction, with no additional real-world robot data. To support continuous real-time execution of action chunks, we incorporate training-time Real-Time Chunking (RTC).

**中文:** 基于仿真数据的 SFT。我们为每个任务使用 1.5k 个仿真回合微调 GR00T 2，这些回合源自一段人类演示视频。SFT 期间，我们更新 DiT，保留预训练的动作归一化统计量，并冻结动作解码器和视频输出投影。微调后的策略以 RGB 观测、机器人状态和任务指令进行零样本的真实世界部署，不使用额外的真实机器人数据。为支持动作块的连续实时执行，我们引入了训练时实时分块（RTC）。

<a id="C038"></a>
**Source:** p.56 C038 · 表 T007

![T007](assets/T007.png)

**Original (caption):** Table 7: GR00T 2 learns dexterous manipulation skills from simulation demonstrations generated from human videos and transfers these skills zero-shot to the real world. Fine-tuned models are evaluated in simulation (s) and the real world (r).

**中文表注：** 表 7：GR00T 2 从人类视频生成的仿真演示中学习灵巧操作技能，并将这些技能零样本迁移到真实世界。微调后的模型分别在仿真（s）和真实世界（r）中评估。

<a id="S1014"></a>
**Source:** p.56 S1014

**Original:** Learning Tasks with Human-to-Sim-to-Real. We evaluate GR00T 2 on three tasks requiring dexterous manipulation, with success defined as follows:

**中文:** 借助人类到仿真再到现实完成任务学习。我们在三项需要灵巧操作的任务上评估 GR00T 2，成功的定义如下：

<a id="S1015"></a>
**Source:** p.56 S1015

**Original:** • Hammer Nail: The nail is driven into the fixture until its head contacts the fixture’s top surface. • Handover Flask: The flask is lifted off the table, handed over, and tilted to a pouring angle without being dropped. • Brushing Trash: Paper waste is swept into the red dustpan using the brush.

**中文:** • 敲钉（Hammer Nail）：钉子被敲入夹具，直至钉头接触夹具的顶面。• 递交烧瓶（Handover Flask）：烧瓶被从桌面提起、递交，并倾斜至倾倒角度，且不能掉落。• 扫纸屑（Brushing Trash）：使用刷子将纸质废弃物扫入红色簸箕。

<a id="S1016"></a>
**Source:** p.56 S1016

**Original:** GR00T 2 is deployed with 2 action 1 video denoising steps during inference with RTC enabled at 20 Hz. 𝜋0.5 is deployed with the settings recommended in the official implementation: each inference integrates the flow-matching action expert for 10 steps, and the robot executes the first 8 actions of each predicted 30-step chunk (0.4 s at 20 Hz) before synchronously querying the policy again, with 𝜋0.5 observing only the most recent frame of each camera view.

**中文:** 推理时，GR00T 2 以 2 个动作去噪步和 1 个视频去噪步进行部署，并以 20 Hz 启用 RTC。π0.5 按照官方实现推荐的设置进行部署：每次推理对流匹配动作专家积分 10 步，机器人执行每个预测的 30 步动作块中的前 8 个动作（在 20 Hz 下为 0.4 s），然后同步地再次查询策略；π0.5 仅观测每个相机视角的最新一帧。

<a id="S1017"></a>
**Source:** p.56 S1017

**Original:** We compare against GR00T 1.7 and 𝜋0.5 in both simulation and the real world. Figure 31 shows execution rollouts for each task. Tab. 7 reports the number of successful episodes for each method. With simulation-only post-training, GR00T 2 achieves 20/20, 13/20, and 19/20 full-task successes in simulation on nail hammering, flask handover, and trash sweeping, respectively (Table 7). In real-world evaluation, it completes nail hammering in 9/10 trials and trash sweeping in 8/10 trials, demonstrating zero-shot transfer on both tasks. Both GR00T 1.7 and 𝜋0.5 achieve 0/10 full-task successes on every real-world task despite making intermediate progress. On nail hammering, GR00T 1.7 lifts the hammer in 10/10 trials and completes in-hand reorientation in 6/10 trials, but never drives the nail to the required depth. On trash sweeping, it lifts the brush in 7/10 trials but never completes the sweep. Similarly, 𝜋0.5 lifts the hammer, flask, and brush in 6/10, 4/10, and 9/10 trials, respectively, but completes none of the full tasks. These results distinguish successful grasp acquisition from full task execution, which requires subsequent reorientation and contact interactions. For the Handover Flask task, the high-frequency specialist policy succeeds in the real world. However, the handover requires precise spatiotemporal coordination and contact control, making it particularly sensitive to observation and inference delays.

**中文:** 我们在仿真和真实世界中都将 GR00T 2 与 GR00T 1.7 及 π0.5 进行比较。图 31 展示了每项任务的执行 rollout（轨迹采样）。Tab. 7 报告了每种方法成功的回合数。仅经过仿真后训练时，GR00T 2 在仿真中完成完整任务的成功次数分别为：敲钉 20/20、递交烧瓶 13/20、扫纸屑 19/20（Table 7）。在真实世界评估中，它完成敲钉的试次为 9/10，完成扫纸屑的试次为 8/10，证明了两项任务上的零样本迁移。尽管取得了中间进展，GR00T 1.7 和 π0.5 在每项真实世界任务上的完整任务成功率都是 0/10。在敲钉任务上，GR00T 1.7 在 10/10 次试次中举起了锤子，并在 6/10 次中完成了手内重定向，但从未将钉子敲到所需深度。在扫纸屑任务上，它在 7/10 次中举起了刷子，但从未完成清扫。类似地，π0.5 分别在 6/10、4/10 和 9/10 次试次中举起了锤子、烧瓶和刷子，但没有完成任何一项完整任务。这些结果区分了成功抓取与完整执行任务：后者还需要后续的重定向和接触交互。对于递交烧瓶任务，高频专用策略在真实世界中取得了成功。然而，递交需要精确的时空协调和接触控制，因此对观测和推理延迟尤为敏感。


<a id="H30"></a>
### C. Data for GR00T 2 ｜ 附录 C：GR00T 2 的数据

<a id="S1018"></a>
**Source:** p.57 S1018

**Original:** This appendix details the sources and roles of data for GR00T 2 summarized in Sec. 4.2.

**中文:** 本附录详述 Sec. 4.2 概述的 GR00T 2 各数据来源及其作用。

<a id="H31"></a>
### C.1. Human Data for GR00T 2 ｜ C.1 GR00T 2 的人类数据

<a id="S1019"></a>
**Source:** p.57 S1019

**Original:** Prior work in scaling data for robot learning has showcased emergent transfer and generalization through scaling egocentric data (Kareer et al., 2025; Punamiya et al., 2026; Zheng et al., 2026).

**中文:** 在机器人学习的数据规模化方面，既有工作已经展示了通过扩展第一人称数据而出现的迁移与泛化能力（Kareer et al., 2025; Punamiya et al., 2026; Zheng et al., 2026）。

<a id="S1020"></a>
**Source:** p.57 S1020

**Original:** Human-1M is a large and diverse egocentric dataset curated by NVIDIA, which supplies the large scale human experience data in GR00T 2’s cross embodiment training mixture. Human-1M contains approximately 1 million hours of proficient human labor sensorized with egocentric cameras, dense language annotation, SLAM and hand pose estimation which are filtered down. The collection spans different environments and sensing configurations, including monocular and stereo head cameras and additional wrist views. We additionally incorporate capture setups that bring human observations closer to those of dexterous robots to examine the transfer of human data at various hierarchies.

**中文:** Human-1M 是 NVIDIA 整理的一个大规模、多样化的第一人称数据集，为 GR00T 2 的跨本体训练配比提供大规模人类经验数据。Human-1M 包含约 100 万小时的熟练人类劳动，用第一人称相机做传感器化记录，并配有密集语言标注、SLAM 与手部位姿估计，随后经过过滤。采集覆盖不同环境与传感配置，包括单目与立体头戴相机，以及额外的腕部视角。我们还引入了使人类观测更接近灵巧机器人观测的采集装置，以考察人类数据在不同层级上的迁移。

<a id="S1021"></a>
**Source:** p.57 S1021

**Original:** C.1.1. Dataset Composition

**中文:** C.1.1 数据集构成

<a id="S1022"></a>
**Source:** p.57 S1022

**Original:** The Human-1M inventory used within GR00T 2 contains 402,730 hours across approximately 13.75 million episodes, spanning over 51,500 unique collectors and 123,000 scenes.

**中文:** GR00T 2 中实际使用的 Human-1M 库存包含 402,730 小时、约 1,375 万条 episode，覆盖 51,500 名以上不重复的采集者与 123,000 个场景。

<a id="S1023"></a>
**Source:** p.57 S1023

**Original:** Collection Settings. We collect demonstrations in both natural “in-the-wild” and controlled studio environments. In-the-wild collection captures proficient laborers in economically valuable scenarios across households, industry workplaces, agriculture, commercial kitchens, service, retail, and logistics. Studio collection concentrates on tabletop manipulation under standardized protocols, resembling demonstration style robotics datasets. Studio data comprises of assembly tasks that involve assembling various kits, curated tasks selected to cover target robot skills and task distributions. Within studio data, “in-lab” collection follows a stricter protocol where demonstrators keep both hands in view, avoid idle periods, and perform motions at speeds chosen to match the robot. Approximately 80,000 hours of the total mixture is studio data. These settings serve complementary purposes. Natural environments broaden the range of interactions observed during pretraining for the world-action model, while controlled collection makes it possible to target particular skills and capture them under more consistent conditions for better transfer to the downstream robot embodiments.

**中文:** 采集设置。我们在自然的"野外"环境与受控的影棚环境中都采集演示。野外采集记录熟练劳动者在具有经济价值的场景中的作业，涵盖家庭、工业工作场所、农业、商业厨房、服务业、零售与物流。影棚采集聚焦标准化协议下的桌面操作，形态类似演示风格的机器人数据集。影棚数据由装配任务构成，涉及组装各类套件，以及为覆盖目标机器人技能与任务分布而挑选的定制任务。在影棚数据中，"实验室内"（in-lab）采集遵循更严格的协议：演示者保持双手在视野内、避免空转时段，并以与机器人匹配的速度完成动作。整个配比中约 80,000 小时为影棚数据。这些设置互为补充：自然环境拓宽了世界-动作模型预训练时观察到的交互范围；受控采集则使针对特定技能、在更一致条件下采集成为可能，从而更好地迁移到下游机器人本体。

<a id="S1024"></a>
**Source:** p.57 S1024

**Original:** Egocentric Cameras. The dataset includes monocular and stereo egocentric recordings. Monocular setups use a single head-mounted RGB camera. Stereo setups provide synchronized two camera RGB head views with optional additional multi-view cameras for better hand pose estimation.

**中文:** 第一人称相机。数据集包含单目与立体第一人称录制。单目配置使用单个头戴 RGB 相机。立体配置提供同步的双相机 RGB 头部视角，并可选用额外的多视角相机以改善手部位姿估计。

<a id="S1025"></a>
**Source:** p.57 S1025

**Original:** Wrist Cameras. Approximately 90,000 hours of the collection also includes wrist cameras, which provide close-up views of manipulation and hand-object interactions to reduce partial observability during fine-grained manipulation. Additionally, a portion of the studio data contains robot-aligned wrist viewpoints to address the visual alignment gap.

**中文:** 腕部相机。约 90,000 小时的采集还包含腕部相机，提供操作与手-物交互的近景视角，以减少细粒度操作中的部分可观测性。此外，一部分影棚数据包含与机器人对齐的腕部视角，用以解决视觉对齐差距。

<a id="S1026"></a>
**Source:** p.57 S1026

**Original:** Even when humans and robots perform the same grasp, wrist-camera placement can change the apparent size and orientation of the hand and object, as well as the visibility of their interaction. We studied this alignment process with the Sharpa platform. We screened 13 initial mount designs and conducted a controlled comparison of four mounts across four operators. The human and robot perform the same four thumb-finger grasps and their viewpoints are compared in a 640x480 image frame. The evaluation measured hand-object overlap, object scale, camera-to-object distance, and camera orientation. We further optimized image rotation and scaling for visual alignment, and used ChArUco (Garrido-Jurado et al., 2014) calibration together with directional motions to optimize angular alignment.

**中文:** 即使人与机器人执行同一个抓取，腕部相机的安装位置也会改变手与物体的表观尺寸和朝向，以及二者交互的可见程度。我们用 Sharpa 平台研究了这一对齐过程。我们筛选了 13 种初始安装设计，并在四名操作员上对四种安装座做了受控比较。人与机器人执行同样的四种拇指-手指抓取，并在 640×480 的图像帧中比较二者的视角。评测测量手-物重叠度、物体尺度、相机到物体的距离以及相机朝向。我们进一步优化图像旋转与缩放以实现视觉对齐，并使用 ChArUco（Garrido-Jurado et al., 2014）标定配合定向运动来优化角度对齐。

<a id="S1027"></a>
**Source:** p.57 S1027

**Original:** Annotations. Each egocentric episode contains language annotations along with frame-aligned estimations of hand and head motion following prior work on learning from egocentric human experience (Kareer et al., 2025; Punamiya et al., 2026).

**中文:** 标注。每条第一人称 episode 都包含语言标注，以及与视频帧对齐的手部与头部运动估计，做法沿用从第一人称人类经验中学习的既有工作（Kareer et al., 2025; Punamiya et al., 2026）。

<a id="S1028"></a>
**Source:** p.58 S1028

**Original:** Hand and Camera Pose. Hand motion is represented by 21 three-dimensional keypoints per hand: the wrist and four landmarks along each finger, including the fingertips. Keypoint positions are expressed in meters in the reference head-camera coordinate frame and aligned with the corresponding video frames. Head motion is represented by the six-degree-of-freedom pose of the head-mounted reference camera, estimated using simultaneous localization and mapping (SLAM) in a canonical per episode world frame.

**中文:** 手部与相机位姿。手部运动由每只手 21 个三维关键点表示：腕部，以及每根手指上的四个标志点（含指尖）。关键点位置以米为单位、在参考头戴相机坐标系中表达，并与对应视频帧对齐。头部运动由头戴参考相机的六自由度位姿表示，用同步定位与建图（SLAM）在每条 episode 各自的标准世界坐标系中估计。

<a id="S1029"></a>
**Source:** p.58 S1029

**Original:** Language Annotation. Language describes demonstrations at two levels. Tier 1 (T1) annotations provide a one- to two-sentence episode summary identifying the primary goal, major actions, and key objects. Tier 2 (T2) annotations describe individual actions in contiguous, timestamped segments of 1-10 seconds. Each description is self-contained and specifies the relevant hand, action, and objects. These annotations support language-conditioned learning and task-based data curation. The language annotations are validated by human quality control checks. The highest quality annotations are used for the training mixture of Flora pipeline described in Sec. C.4. The Flora pipeline is then used to further enrich or provide T2 language annotations across the dataset.

**中文:** 语言标注。语言在两个层级上描述演示。第 1 层（T1）标注提供一到两句话的 episode 摘要，指明主要目标、主要动作与关键物体。第 2 层（T2）标注以 1–10 秒的连续、带时间戳的片段描述单个动作。每条描述自包含，并指明相关的手、动作与物体。这些标注支撑语言条件学习与基于任务的数据整理。语言标注经人工质量控制检查验证。质量最高的标注用于 Sec. C.4 所述 Flora 流程的训练配比。随后再用 Flora 流程在整个数据集上进一步丰富或补足 T2 语言标注。

<a id="S1030"></a>
**Source:** p.58 S1030

**Original:** C.1.2. Data Filtering and Quality Control

**中文:** C.1.2 数据过滤与质量控制

<a id="S1031"></a>
**Source:** p.58 S1031

**Original:** The usefulness of a human demonstration for tabletop manipulation settings depends on both the interaction it contains and the reliability of its recorded motion. We therefore apply quality control at two levels. Batch-level review checks the content and annotations of a delivery, while quantitative filtering selects timesteps with sufficiently stable observations and hand trajectories. Additional details about the quality control are in the accompanying Human-1M dataset release.

**中文:** 一条人类演示对桌面操作场景是否有用，既取决于它包含的交互，也取决于其记录运动的可靠性。因此我们在两个层级上做质量控制。批次级审核检查一次交付的内容与标注；定量过滤则挑选观测与手部轨迹足够稳定的时间步。关于质量控制的更多细节见随 Human-1M 数据集发布的说明。

<a id="S1032"></a>
**Source:** p.58 S1032

**Original:** Human review. Human auditors check language-annotation validity, task quality and idle time as per our collection specs at a 95% per episode pass rate. These criteria screen deliveries before individual training timesteps are selected by the quantitative filters.

**中文:** 人工审核。人工审核员按我们的采集规范检查语言标注有效性、任务质量与空转时间，要求每条 episode 通过率 95%。这些准则在定量过滤器挑选单个训练时间步之前，先对交付批次做筛选。

<a id="S1033"></a>
**Source:** p.58 S1033

**Original:** Quantitative Filtering. At each candidate training timestep, we evaluate a window extending 24 frames into the past and 48 frames into the future. We retain the timestep only if all quality criteria pass over this window. The checks constrain head rotation and translation, hand visibility, consistency of reconstructed bone lengths, and wrist speed (Tab. 8). The bone-length error of a hand in a frame is the median absolute deviation of its 20 finger-bone lengths from their per-episode medians, divided by the mean of those medians, so the threshold of 0.05 corresponds to 5% of the mean bone length.

**中文:** 定量过滤。对每个候选训练时间步，我们评估一个向前 24 帧、向后 48 帧的窗口。只有当全部质量准则在该窗口上都通过时，我们才保留该时间步。检查项约束头部旋转与平移、手部可见性、重建骨长的一致性以及腕部速度（Tab. 8）。某帧中某只手的骨长误差定义为：20 根手指骨长相对其本 episode 中位数的中位绝对偏差，除以这些中位数的均值；因此阈值 0.05 对应平均骨长的 5%。

<a id="C039"></a>
**Source:** p.58 C039 · 表 T008

![T008](assets/T008.png)

**Original (caption):** Table 8: Quantitative criteria for selecting training timesteps.

**中文表注：** 表 8：用于挑选训练时间步的定量准则。


<a id="S1036"></a>
**Source:** p.58 S1036

**Original:** C.1.3. In-Lab Human Data

**中文:** C.1.3 实验室人类数据

<a id="S1037"></a>
**Source:** p.58 S1037

**Original:** In-lab data is the part of human data that transfers most directly to a robot policy. Two gaps separate a human demonstration from a robot rollout, and both can be narrowed at collection time rather than left to the model. The observation gap: in-the-wild wrist cameras are not placed with reference to any robot, so the hand appears at a different angle, scale, and position than in the robot’s wrist view, and the model must imagine across this viewpoint change before it can imagine across embodiments (Sec. B.1.5). The motion gap: natural human execution is faster than teleoperated robot execution, interleaves pauses and task-irrelevant gestures, and uses motions the robot hand cannot reproduce. In-lab collection follows our studio collection guidelines, which fix camera placement, motion, and task protocol with the target robot in mind.

**中文:** 实验室数据是人类数据中向机器人策略迁移最直接的那一部分。人类演示与机器人 rollout 之间存在两道差距，而这两道差距都可以在采集时收窄，而不必留给模型。观测差距：野外腕部相机并不是参照某台机器人摆放的，因此手在画面中出现的角度、尺度与位置都与机器人腕部视角不同，模型必须先跨越这一视角变化去想象，然后才能跨越本体去想象（Sec. B.1.5）。运动差距：自然的人类执行比遥操作的机器人执行更快，其间夹杂停顿与与任务无关的手势，并使用机器手无法复现的运动。实验室采集遵循我们的影棚采集指南，该指南在摆放相机、规定动作与任务协议时都以目标机器人为参照。

<a id="S1038"></a>
**Source:** p.59 S1038

**Original:** Collection protocol. Demonstrators keep the head still, keep both hands and the manipulated objects visible in every frame, avoid idle time, rehearse each task before recording, and follow a reference video where one exists. Pace is controlled through bounds on wrist speed, which exclude motion too fast for the robot on one side and near-stationary hands on the other. Each task is recorded by several operators in several environments, and episodes that a robot could not reproduce are rejected before delivery. The complete criteria, including the acceptance thresholds for the wrist camera and for hand-pose quality, are listed in Sec. C.1.4.

**中文:** 采集协议。演示者保持头部静止，使双手与被操作物体在每一帧中都可见，避免空转时间，录制前先排练每个任务，并在存在参考视频时照着参考视频做。节奏通过腕部速度上下界来控制：一端排除对机器人而言过快的运动，另一端排除近乎静止的手。每个任务由多名操作员在多个环境中录制，机器人无法复现的 episode 在交付前即被剔除。完整准则（含腕部相机与手部位姿质量的验收阈值）见 Sec. C.1.4。

<a id="S1039"></a>
**Source:** p.59 S1039

**Original:** Alignment to the target embodiment. The target is Tianji with Sharpa hands, the platform of the human-torobot transfer (Sec. B.1), whose teleoperation system is described in Sec. C.3.1. On the observation side, the human wrist camera is mounted to reproduce the view of the robot’s wrist camera. It is accepted only when the hand and the object appear at the same scale and position as in the robot view. The head camera stands in for the robot’s head camera and is held still, and demonstrators whose hands are close to the robot hand in size are preferred. On the motion side, tasks mirror the robot’s teleoperation tasks with the same objects and step order, robot-paired tasks come with reference videos recorded on the robot, and the speed bounds keep the pace within what the robot can execute. In-lab episodes pass through the same filtering and annotation as the rest of Human-1M (Tab. 8, Sec. C.4), and their hand keypoints can be retargeted with the solver of Sec. B.1.2 into the observation and action schema of a teleoperated Tianji episode (Sec. B.1.3).

**中文:** 与目标本体对齐。目标平台是配 Sharpa 手的 Tianji，即人→机器人迁移所用的平台（Sec. B.1），其遥操作系统见 Sec. C.3.1。在观测方面，人类腕部相机的安装方式被设计成复现机器人腕部相机的视角；只有当手与物体以与机器人视角相同的尺度和位置出现时才被接受。头戴相机代替机器人的头部相机并保持静止，且优先选用手部尺寸接近机器手的演示者。在运动方面，任务镜像机器人的遥操作任务，使用相同物体与相同步骤顺序；与机器人配对的任务附带在机器人上录制的参考视频；速度上下界把节奏限制在机器人可执行的范围内。实验室 episode 与 Human-1M 其余部分一样经过相同的过滤与标注（Tab. 8、Sec. C.4），其手部关键点可用 Sec. B.1.2 的求解器重定向成一条遥操作 Tianji episode 的观测与动作 schema（Sec. B.1.3）。

<a id="S1040"></a>
**Source:** p.59 S1040

**Original:** Scale and diversity. In-lab collection has delivered about 3,000 hours and 700k episodes. The tasks are drawn from more than 2,000 task specifications, which span short single-goal tabletop tasks that each isolate a grasp or a skill, robot-paired tasks with fixed objects and reference videos that stress dexterity and dynamics, longer multi-step chores, and tasks paired with UMI reference demonstrations (Sec. C.2), so that the same task exists as human, UMI, and robot data. Episodes are short and dense, and each task is demonstrated hundreds of times by different operators, which gives the model many views of the same manipulation rather than many unrelated clips.

**中文:** 规模与多样性。实验室采集已交付约 3,000 小时、70 万条 episode。任务取自 2,000 余份任务规范，覆盖：短的单一目标桌面任务（每个只隔离一项抓取或一项技能）；带固定物体与参考视频、施加灵巧性与动力学压力的机器人配对任务；较长的多步骤杂务；以及配有 UMI 参考演示的任务（Sec. C.2），使同一任务同时以人类、UMI 与机器人数据的形式存在。episode 短而密集，每项任务由不同操作员演示数百次，这给模型提供的是同一操作的大量视角，而不是大量互不相关的片段。

<a id="S1042"></a>
**Source:** p.59 S1042

**Original:** This section lists the acceptance criteria of our studio collection guidelines (v1.3.2) for the in-lab human data of Sec. C.1.3. The wrist-camera criterion is checked once per mount design: the demonstrator repeats, with the same 4.4 cm calibration block, the calibration motions recorded from the robot’s wrist camera (a thumb pinch with each finger and a whole-hand grasp), and the human video is overlaid on the robot video. The remaining criteria are checked per delivery. Tab. 9 summarizes them.

**中文:** 本节列出我们影棚采集指南（v1.3.2）中针对 Sec. C.1.3 实验室人类数据的验收准则。腕部相机准则对每种安装设计检查一次：演示者用同一块 4.4 cm 标定块，重复从机器人腕部相机录制的标定动作（与每根手指做拇指捏合，以及整手握持），并把人类视频叠加到机器人视频上。其余准则按每次交付检查。Tab. 9 对其作了汇总。

<a id="C040"></a>
**Source:** p.59 C040 · 表 T009

![T009](assets/T009.png)

**Original (caption):** Table 9: In-lab collection criteria.

**中文表注：** 表 9：实验室采集准则。

<a id="S1044"></a>
**Source:** p.59 S1044

**Original:** Head motion Stable head pose, no rotation Hand visibility Both hands in 100% of frames Idle motion None, brief task-relevant inspection allowed Wrist speed < 5% of samples at ≥0.40 m/s, ≤60% below 0.03 m/s, follow the reference video pace Wrist camera Calibration block at 0.8–1.2× its size in the robot view, human-robot hand IoU > 0.5 with arms extended Hand-pose quality Speed-conditioned jitter ≤4× the robot reference per speed band, perframe confidence, audited reprojections Operators One per environment, hand size close to the robot hand preferred Demonstrations 400 per task: 8 environments, 50 each Objects Robot-paired tasks: specified SKU, or 3 variants of similar shape and size Deliverables Head and wrist intrinsics, stereo extrinsics, per-delivery wrist-speed statistics

**中文:** 头部运动：头部位姿稳定、无旋转。手部可见性：双手在 100% 的帧中可见。空转动作：无；允许简短的、与任务相关的查看。腕部速度：速度 ≥0.40 m/s 的样本占比 < 5%，速度低于 0.03 m/s 的样本占比 ≤ 60%，并遵循参考视频节奏。腕部相机：标定块在机器人视角中为其尺寸的 0.8–1.2 倍；双臂伸展时人-机器人手部 IoU > 0.5。手部位姿质量：按速度分段的抖动 ≤ 机器人参考的 4 倍；逐帧置信度；重投影经审核。操作员：每个环境一名，优先选择手部尺寸接近机器手者。演示数量：每项任务 400 条，即 8 个环境、每个 50 条。物体：机器人配对任务使用指定 SKU，或 3 个形状与尺寸相近的变体。交付物：头部与腕部内参、立体外参、每次交付的腕部速度统计。

<a id="S1045"></a>
**Source:** p.60 S1045

**Original:** C.1.5. Scaling Human Video

**中文:** C.1.5 人类视频的规模化

<a id="S1046"></a>
**Source:** p.60 S1046

**Original:** GR00T 2 pretrains on egocentric human video from Human-1M as well as on robot data. To measure how much the human video contributes to robot performance, we train four models that differ in how much human video they see. We test each one on new tasks on Dexter, a bimanual robot with two 7-DoF arms and two 22-DoF Sharpa hands, and on the video rollouts each model generates for the same tasks.

**中文:** GR00T 2 既在机器人数据上预训练，也在来自 Human-1M 的第一人称人类视频上预训练。为衡量人类视频对机器人性能的贡献有多大，我们训练了四个只在"看到多少人类视频"上不同的模型。我们在 Dexter（一台配两条 7-DoF 手臂和两只 22-DoF Sharpa 手的双臂机器人）的新任务上测试每一个模型，也测试各模型为相同任务生成的视频 rollout。

<a id="S1047"></a>
**Source:** p.60 S1047

**Original:** Setup. The four models share the GR00T 2 architecture and train on the same Dexter teleoperation data with the same recipe. They differ only in the human video they see. The 0% model sees none. The other three start from a common human-video pretraining checkpoint, then continue on 1%, 10%, or 100% of the tasks in the multi-view human video of Human-1M (0.87k, 8.1k, and 84.4k hours after the timestep filters of Tab. 8) and co-train on it with the Dexter data. The 0% model does not have this shared stage, so comparisons with it measure the shared stage and the human share together, whereas the 1%, 10%, and 100% models differ only in the share and the matching training length. Training length is matched in epochs. Each human share is pretrained for about 0.5 epoch of that share, so the larger shares also take more steps, and every model, including the 0% model, is then trained for 3 epochs of the Dexter data, where one epoch passes once over every step of every 30 Hz trajectory. During this stage, the 1%, 10%, and 100% models draw 45% of their training samples from Dexter and 55% from human video, while the 0% model trains on the Dexter data alone. Multi-view human video is recorded with wrist cameras as well as a head camera, like the robot. GR00T 2 itself pretrains on 403k hours of Human-1M. We pick each model’s checkpoint offline with the same rule for all four, without robot evaluation.

**中文:** 设置。四个模型共享 GR00T 2 架构，用相同配方在同一批 Dexter 遥操作数据上训练，只在所看到的人类视频上不同。0% 模型完全看不到人类视频。另外三个从同一个人类视频预训练检查点出发，随后在 Human-1M 多视角人类视频中 1%、10% 或 100% 的任务上继续训练（经 Tab. 8 的时间步过滤后分别为 0.87k、8.1k 与 84.4k 小时），并与 Dexter 数据联合训练。0% 模型没有这个共享阶段，因此与它的比较同时衡量了共享阶段与人类数据份额；而 1%、10%、100% 三个模型只在份额与相应训练长度上不同。训练长度按 epoch 对齐。每个人类份额预训练约 0.5 个该份额的 epoch，因此份额越大步数也越多；随后每个模型（包括 0% 模型）都在 Dexter 数据上训练 3 个 epoch，其中一个 epoch 指把每条 30 Hz 轨迹的每个时间步过一遍。此阶段中，1%、10%、100% 模型的训练样本 45% 来自 Dexter、55% 来自人类视频，而 0% 模型只在 Dexter 数据上训练。多视角人类视频与机器人一样，既有腕部相机也有头部相机。GR00T 2 本身在 403k 小时的 Human-1M 上预训练。四个模型的检查点都用同一规则离线挑选，不做机器人评测。

<a id="S1048"></a>
**Source:** p.60 S1048

**Original:** We test on 72 Dexter tasks, giving each model only the task instruction. 22 of them are out-of-distribution (OOD) tasks. They use objects and pick-and-place skills from Dexter’s training data, with new kinds of instructions such as color, negation, size, order, count, and spatial relations. The other 50 never appear in Dexter’s training data, and 47 of them are in Dexter-50. Each model runs 3 episodes per task, for 864 episodes in total. On each task, the four models run back to back on the same station and scene, in the order 0%, 1%, 10%, 100%. One operator grades all of them on whether the task’s end state is reached. We also score task progress, the fraction of the task completed, with a vision-language model on the real robot rollout video from the head and both wrist cameras.

**中文:** 我们在 72 项 Dexter 任务上测试，只给每个模型任务指令。其中 22 项是分布外（OOD）任务：它们使用 Dexter 训练数据中的物体与抓取-放置技能，但指令类型是新的，例如颜色、否定、尺寸、顺序、计数与空间关系。另外 50 项从未出现在 Dexter 的训练数据中，其中 47 项属于 Dexter-50。每个模型在每项任务上运行 3 条 episode，共 864 条。每项任务上，四个模型在同一工位、同一场景上按 0%、1%、10%、100% 的顺序背靠背运行。由同一名操作员判定它们是否达到任务的终止状态。我们还用视觉语言模型基于头部与双腕相机的真机 rollout 视频，给任务进度（任务完成的比例）打分。

<a id="S1049"></a>
**Source:** p.60 S1049

**Original:** GR00T 2 also predicts video, so we evaluate the same 72 tasks without a robot as well. From 3 recorded start scenes per task, each model generates video rollouts for the task instruction with 10 generation seeds, for 2,160 videos per model. The same vision-language model judges whether a rollout performs the commanded action on the target object (video success) and scores its task progress with the same prompt as the real episodes.

**中文:** GR00T 2 还会预测视频，因此我们也在没有机器人的情况下评测同样的 72 项任务。从每项任务 3 个录制的起始场景出发，每个模型针对任务指令以 10 个生成种子生成视频 rollout，每个模型共 2,160 段视频。同一个视觉语言模型判定某段 rollout 是否对目标物体执行了被指令的动作（视频成功），并用与真机 episode 相同的提示词为其任务进度打分。

<a id="S1050"></a>
**Source:** p.60 S1050

**Original:** Results. All four metrics rise with the amount of human video (Fig. 10). On the robot, success goes from 18% without human video to 27%, 28%, and 41% with 1%, 10%, and 100%, and task progress from 50% to 58%, 61%, and 70%. In video rollouts, success goes from 30% to 33%, 38%, and 51%, and task progress from 64% to 66%, 72%, and 77%. Using all of the multi-view human video instead of none raises success on the robot by 23.1 points (95% confidence interval 13.4 to 33.3, paired over tasks) and task progress by 20.1 points (12.3 to 27.9). In video rollouts it raises success by 21.3 points (14.3 to 28.2) and task progress by 12.4 points (7.8 to 17.1).

**中文:** 结果。四项指标都随人类视频量上升（Fig. 10）。真机上，成功率从无人类视频时的 18% 升到 1%、10%、100% 时的 27%、28%、41%，任务进度从 50% 升到 58%、61%、70%。在视频 rollout 中，成功率从 30% 升到 33%、38%、51%，任务进度从 64% 升到 66%、72%、77%。使用全部多视角人类视频（而非完全不用）使真机成功率提高 23.1 个百分点（95% 置信区间 13.4 至 33.3，按任务配对），任务进度提高 20.1 个百分点（12.3 至 27.9）。在视频 rollout 中，成功率提高 21.3 个百分点（14.3 至 28.2），任务进度提高 12.4 个百分点（7.8 至 17.1）。

<a id="S1051"></a>
**Source:** p.60 S1051

**Original:** From 1% to 100%, task progress on the robot gains about 6 points for each tenfold increase in human video (2.5 to 9.6), and video success about 9 points (5.9 to 12.0). The step from 10% to 100% is clear on every metric. On the robot, success gains 12.5 points (4.2 to 21.3). The step from 1% to 10% is within noise on the robot (success +0.9 and progress +3.2 points), but shows in video rollouts (success +4.7 points, 0.1 to 9.4, and progress +6.2 points, 2.6 to 9.9), which average 30 rollouts per task instead of 3. None of the metrics levels off at 100%, which suggests that more human video would help further. Each data share is a single training run, so the error bars show how much the results vary across repeated rollouts, not across training runs.

**中文:** 从 1% 到 100%，人类视频每增加十倍，真机任务进度约提升 6 个点（2.5 至 9.6），视频成功率约提升 9 个点（5.9 至 12.0）。从 10% 到 100% 这一步在每一项指标上都清晰可见：真机成功率提升 12.5 个点（4.2 至 21.3）。从 1% 到 10% 这一步在真机上处于噪声范围内（成功率 +0.9、任务进度 +3.2 个点），但在视频 rollout 中显现出来（成功率 +4.7 个点，0.1 至 9.4；任务进度 +6.2 个点，2.6 至 9.9）——视频 rollout 每项任务平均有 30 条，而真机只有 3 条。没有任何指标在 100% 处趋于饱和，这提示更多人类视频还会带来进一步收益。每个数据份额只对应一次训练运行，因此误差棒反映的是重复 rollout 之间的波动，而不是训练运行之间的波动。

<a id="C041"></a>
**Source:** p.61 C041 · 表 T010

![T010](assets/T010.png)

**Original (caption):** Table 10: UMI-10K for GR00T 2. Gripper UMI episodes in the pretraining corpus.

**中文表注：** 表 10：供 GR00T 2 使用的 UMI-10K。预训练语料中的夹爪 UMI episode。

<a id="C042"></a>
**Source:** p.61 C042 · 图 F032

![F032](assets/F032.png)

**Original (caption):** Figure 32: Skill distribution of the Gripper UMI corpus. Episodes per skill on a logarithmic scale, colored by skill group. An episode counts toward every skill its instruction exercises. Pick-and-place is the most common skill, but 88% of episodes also exercise at least one other skill.

**中文图注：** 图 32：夹爪 UMI 语料的技能分布。每项技能的 episode 数（对数刻度），按技能组着色。一条 episode 计入其指令所涉及的每一项技能。抓取-放置是最常见的技能，但 88% 的 episode 还涉及至少一项其他技能。


<a id="H32"></a>
### C.2. UMI-10K for GR00T 2 ｜ 面向 GR00T 2 的 UMI-10K 数据

<a id="S1110"></a>
**Source:** p.61 S1110

**Original:** Scale. The Gripper UMI corpus (App. E) contributes 942k quality-controlled episodes and 10,184 hours of bimanual parallel-gripper demonstrations across 2,897 tasks to GR00T 2 pretraining (Tab. 10). The corpus is built for breadth, focusing on short to mid-horizon tasks with wide behavior coverage, rather than depth on a few specialized tasks: no task accounts for more than 1.2% of the hours, and the instructions span 356 object categories and 49 skills in our manipulation vocabulary.

**中文:** 规模。Gripper UMI 语料（App. E）为 GR00T 2 预训练贡献了 942k 条经质量控制的片段（episode），共 10,184 小时的双臂平行夹爪演示数据，覆盖 2,897 项任务（Tab. 10）。该语料以广度为目标，重点是覆盖多种行为的短到中等时序任务，而非深耕少数专门任务：没有任何一项任务占比超过总时长的 1.2%，指令涵盖 356 个物体类别，以及我们操作词表中的 49 项技能。

<a id="S1111"></a>
**Source:** p.61 S1111

**Original:** Task distribution. We characterize the corpus by tagging every task instruction with a 49-skill vocabulary organized in four groups by manipulation and object type: prehensile, non-prehensile, articulated, and deformable, the same vocabulary that drives task generation (below). The skill distribution is shown in (Fig. 32): pick-and-place appears in 64% of episodes, while 88% of episodes also exercise at least one other skill to ensure diversity and complexity of actions captured. 29% of episodes involve a dynamic skill such as throwing, toppling, shaking, or sweeping, and 17% involve a precision skill such as insertion or capping. Articulated-object skills, drawers, lids, zippers, box flaps, doors, knobs, and cranks, appear in 29% of episodes, and deformable-object skills, folding, spreading, rolling, tearing, and tying, in 15%. Tasks are graded into three difficulty tiers along two axes, the number of sequential subgoals and the share of more complex motion beyond pick-and-place, which both increase with difficulty tier. By hours, 41% of the corpus is simple (two or more subgoals, any motion), 38% moderate (three or more state-dependent subgoals with at least one non-pickand-place skill), and 21% complex (four or more state-dependent subgoals dominated by non-pick-and-place skills).

**中文:** 任务分布。我们用一个 49 项技能词表为每条任务指令打标签，该词表按操作方式和物体类型分为四组：可抓取型（prehensile）、非抓取型（non-prehensile）、铰接型（articulated）和可变形型（deformable），与下文驱动任务生成的词表相同。技能分布见（Fig. 32）：抓放（pick-and-place）出现在 64% 的片段中，同时 88% 的片段还至少包含另一项技能，以保证所采集动作的多样性与复杂度。29% 的片段涉及投掷、推倒、摇晃或扫动等动态技能；17% 涉及插入或盖帽等精密技能。铰接物体技能（抽屉、盖子、拉链、箱盖、门、旋钮和摇柄）出现在 29% 的片段中，可变形物体技能（折叠、铺展、卷起、撕扯和打结）出现在 15% 的片段中。任务按两个维度分为三个难度等级：连续子目标的数量，以及超出抓放的更复杂运动所占的比例，二者均随难度等级递增。按时长计，语料中 41% 为简单任务（两个或以上子目标，任意运动），38% 为中等任务（三个或以上依赖状态的子目标，且至少包含一项非抓放技能），21% 为复杂任务（四个或以上依赖状态的子目标，以非抓放技能为主）。[存疑：原文 “non-pickand-place” 疑为 “non-pick-and-place” 的断行抽取错误，中文按原意译出。]

<a id="S1113"></a>
**Source:** p.61 S1113

**Original:** Task design. Tasks are generated using a language-model based agent which pairs skills from the vocabulary

**中文:** 任务设计。任务由基于语言模型的智能体生成，该智能体从词表中配对技能。[存疑：原文在此处截断，句子在 S1120 续接。]

<a id="C043"></a>
**Source:** p.62 C043 · 表 T011

![T011](assets/T011.png)

**Original (caption):** Table 11: Robot teleoperation data in the GR00T 2 pretraining mixture. Share is the fraction of robot-data samples drawn from each source.

**中文表注：** 表 11：GR00T 2 预训练数据配比中的机器人遥操作数据。Share 为从各数据源抽取的机器人数据样本所占的比例。

<a id="S1120"></a>
**Source:** p.62 S1120

**Original:** with objects from an object inventory into task templates, which are linted, deduplicated against every existing task. A human then inspects each task and manually accepts or rejects it. Each template is instantiated into concrete tasks by sampling different object, count, color, and position, which yields counterfactual pairs that share a scene but differ in one attribute of the instruction, and each generation round under-samples skills that are already common. The result is broad compositional coverage: 2,798 distinct skill-object pairs, with 70% of the top-24-skill by top-30-object grid populated.

**中文:** 将物体清单中的物体填入任务模板，这些模板经过规范检查，并与所有已有任务做去重。随后由人工逐条检查任务，并手动接受或拒绝。每个模板通过采样不同的物体、数量、颜色和位置被实例化为具体任务，由此得到的反事实对共享同一场景，但指令中只有一个属性不同；每一轮生成也会对已经常见的技能进行欠采样。最终形成了广泛的组合覆盖：共 2,798 种不同的技能-物体对，在由前 24 项技能与前 30 个物体构成的网格中，有 70% 的格子被填充。

<a id="S1121"></a>
**Source:** p.62 S1121

**Original:** Quality control. Every episode passes a three-stage quality pipeline before it enters the corpus. First, an autonomous station-side check rejects recordings with uneven frame timing, dropped frames, or tracking and gripper faults at the point of capture. Second, an agentic QC pipeline reviews each remaining episode from its videos and instruction and scores four aspects: task completion (every step of the instruction is carried out on the objects, counts, and targets the instruction names, and the result is left in the specified state), motion quality (no micro-adjustments, jerky or abrupt movements, or idle hesitation), scene validity (a clean workspace without distracting or occluding objects or people), and view quality (both grippers and the task area visible in every camera); an episode is rejected on any critical failure or on a low aspect score. Third, human reviewers audit the agent’s verdicts on sampled and disputed episodes against a golden set, and their corrections feed back into the judge. Together these stages filter out roughly a quarter of recorded episodes (about 11% at the station and 16% at the agentic gate), so the corpus contains only clean, instruction-faithful demonstrations whose motion reflects natural human manipulation: the 95th-percentile gripper speed within an episode is 0.28 m/s on each arm, and peak speeds exceed 0.68 m/s in a tenth of the episodes.

**中文:** 质量控制。每条片段在进入语料前都要经过三阶段质量流水线。第一，工位端的自动检查会在采集时直接剔除帧时间不均匀、丢帧，或跟踪与夹爪故障的录制。第二，智能体化的 QC 流水线根据视频和指令审查每条剩余片段，并对四个方面打分：任务完成度（指令中的每一步都在指令所指定的物体、数量和目标上执行，且结果保持在指定状态）、动作质量（没有微调、抖动或突兀动作，也没有空闲迟疑）、场景有效性（工作区整洁，没有分散注意力或遮挡的物体或人员），以及视角质量（每个相机中都能看到两个夹爪和任务区域）。只要出现任何关键失败或某一方面得分过低，片段即被剔除。第三，人工审核员针对抽检和有争议的片段，对照黄金集（golden set）审核智能体的判定，其修正结果会反馈给判定器（judge）。这些阶段合计过滤掉约四分之一的录制片段（工位端约 11%，智能体关卡约 16%），因此语料中只保留干净、与指令一致的演示，其动作体现了人类自然的操作方式：片段内夹爪速度的第 95 百分位在每条手臂上为 0.28 m/s，十分之一的片段峰值速度超过 0.68 m/s。

<a id="H33"></a>
### C.3. Teleoperation Data for GR00T 2 ｜ 面向 GR00T 2 的遥操作数据

<a id="S1123"></a>
**Source:** p.62 S1123

**Original:** GR00T 2 pretrains on about 23.5k hours and 1.16M episodes of teleoperation from six sources. They span bimanual parallel-gripper arms, bimanual arms with dexterous hands, a humanoid, and a single-arm manipulator (Tab. 11).

**中文:** GR00T 2 在来自六个数据源的约 23.5k 小时、1.16M 条遥操作片段上进行预训练。这些数据涵盖双臂平行夹爪机械臂、带灵巧手的双臂机械臂、一台人形机器人，以及一台单臂操作器（Tab. 11）。

<a id="S1124"></a>
**Source:** p.62 S1124

**Original:** Embodiments and sources. Bimanual parallel-gripper data come from YAM arms and make up the largest block: 18.7k hours covering a broad range of household and tabletop tasks, including 3.6k hours from ABC- 130k (XDOF, 2026). Dexterous data come from bimanual arms with multi-fingered hands. The Sharpa data (22-DoF Sharpa hands) cover 2.9k hours, and Wuji (20-DoF Wuji hands on 7-DoF Tianji arms) adds 1.3k hours. Humanoid data come from the Unitree G1 (App. H), and DROID (Khazatsky et al., 2024) contributes single-arm Franka data from 564 scenes. Every bimanual platform records a head or top-down view and two wrist views.

**中文:** 本体与数据来源。双臂平行夹爪数据来自 YAM 机械臂，是占比最大的部分：18.7k 小时，覆盖广泛的家庭与桌面任务，其中包括来自 ABC-130k（XDOF, 2026）的 3.6k 小时。灵巧数据来自配备多指手的双臂机械臂。Sharpa 数据（22-DoF Sharpa 手）覆盖 2.9k 小时，Wuji（7-DoF Tianji 机械臂上装配的 20-DoF Wuji 手）增加了 1.3k 小时。人形机器人数据来自 Unitree G1（App. H），DROID（Khazatsky et al., 2024）则提供来自 564 个场景的单臂 Franka 数据。每个双臂平台都记录一路头部或俯视视角，以及两路腕部视角。

<a id="C044"></a>
**Source:** p.63 C044 · 图 F033

![F033](assets/F033.png)

**Original (caption):** Figure 33: Teleoperation system for Tianji + Sharpa. (A) Teleoperation pipeline from operator devices to the robot. The retargeter is the solver used for human-data conversion. (B) Robot platform: Tianji arms, Sharpa hands, and the GEAR Neck. (C) Key upgrades: hardware, numbered at their location in (B), and software.

**中文图注：** 图 33：Tianji + Sharpa 的遥操作系统。（A）从操作员设备到机器人的遥操作流水线。重定向器（retargeter）是用于人类数据转换的求解器。（B）机器人平台：Tianji 机械臂、Sharpa 手和 GEAR Neck。（C）关键升级：硬件（编号位置对应（B）中的位置）和软件。

<a id="S1140"></a>
**Source:** p.63 S1140

**Original:** Mixture. Sampling shares are set per source rather than in proportion to hours (Tab. 11). YAM holds 64% of robot hours but receives 51% of samples. The dexterous Sharpa and Wuji data together hold 18% of hours and receive 35% of samples.

**中文:** 数据配比。采样占比按数据源分别设定，而非按时长比例分配（Tab. 11）。YAM 占机器人时长的 64%，却只获得 51% 的样本。灵巧类的 Sharpa 与 Wuji 数据合计占时长的 18%，获得 35% 的样本。

<a id="S1141"></a>
**Source:** p.63 S1141

**Original:** C.3.1. In-Lab Teleoperation System for Tianji + Sharpa

**中文:** C.3.1. 实验室内 Tianji + Sharpa 遥操作系统

<a id="S1142"></a>
**Source:** p.63 S1142

**Original:** The sources in Tab. 11 form the pretraining mixture. In addition, we collect robot data in our lab, mainly for post-training, with the Tianji + Sharpa teleoperation system in Fig. 33. It shares its devices and retargeting with the human-data pipeline (Sec. B.1.1 and B.1.2) and collects, for example, the task-agnostic play data used to learn new tasks without teleoperation (Sec. B.1.3) and the 1 or 10 target-task demonstrations added for comparison (Sec. B.1.4).

**中文:** Tab. 11 中的数据源构成预训练数据配比。此外，我们主要为后训练在实验室中采集机器人数据，所用的是 Fig. 33 中的 Tianji + Sharpa 遥操作系统。该系统与人类数据流水线共享设备和重定向（Sec. B.1.1 和 B.1.2），例如采集用于在无需遥操作的情况下学习新任务的任务无关自由玩耍（play）数据（Sec. B.1.3），以及为对比而添加的 1 条或 10 条目标任务演示（Sec. B.1.4）。

<a id="S1143"></a>
**Source:** p.63 S1143

**Original:** Platform and pipeline. Tianji + Sharpa pairs two 7-DoF Tianji arms with two 22-DoF Sharpa Wave hands. A longer upper arm (288 to 400 mm) recovers the workspace in front of the chest, and a 220 ∘/s joint limit keeps up with human wrist motion. A teleoperation server ingests all devices through Isaac Teleop, a retargeter maps them to arm and hand commands, and a robot server executes them.

**中文:** 平台与流水线。Tianji + Sharpa 将两台 7-DoF Tianji 机械臂与两只 22-DoF Sharpa Wave 手配对。更长的大臂（288 至 400 mm）可恢复胸前的工作空间，220 ∘/s 的关节限速则能跟上人手腕部的运动。遥操作服务器通过 Isaac Teleop 接入所有设备，重定向器将其映射为机械臂与手部指令，机器人服务器负责执行这些指令。

<a id="S1144"></a>
**Source:** p.63 S1144

**Original:** Active head without motion sickness. The cameras ride on the GEAR Neck, our open-source 3-DoF neck that follows the headset, and stream at 60 fps for lower latency and less blur. A moving head camera normally causes motion sickness, because the image lags the operator’s head turn by the capture, transport, and neck delay. Our 3-DoF reprojection in Televiz renders each frame at its capture-time orientation and lets the headset re-render it against the current head pose at its own rate, so head rotation is answered locally and end-to-end latency no longer drives operator comfort.

**中文:** 无晕动症的主动头部。相机安装在 GEAR Neck 上，这是我们开源的 3-DoF 颈部，跟随头显运动，并以 60 fps 串流，以降低时延和模糊。移动的头部相机通常会引起晕动症，因为图像会因采集、传输和颈部延迟而落后于操作员的头部转动。我们在 Televiz 中的 3-DoF 重投影会以采集时的姿态渲染每一帧，并让头显以自身的速率、依据当前头部位姿重新渲染该帧，因此头部转动可以在本地响应，端到端时延不再决定操作员的舒适度。


<a id="H34"></a>
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

<a id="H35"></a>
### D. Real-World Benchmarking with GearArena ｜ D. 基于 GearArena 的真实世界基准测试

<a id="S1149"></a>
**Source:** p.65 S1149

**Original:** This appendix describes how we benchmark GR00T 2 on real robots: why we aggregate real-robot evaluations into a single leaderboard and why that leaderboard is built from blinded A/B comparisons (Sec. D.1), how the evaluation tasks are designed (Sec. D.2), how the arena is organized (Sec. D.3), the rating model (Sec. D.4), the A/B evaluation infrastructure (Sec. D.5), what the arena shows about GR00T 2 (Sec. D.6), and its limitations (Sec. D.7). Tab. 12 summarizes the evidence behind every number in this appendix.

**中文:** 本附录描述我们如何在真实机器人上对 GR00T 2 进行基准测试：为何将真实机器人评测汇总为单一排行榜，以及为何该排行榜基于盲式 A/B 比较构建（Sec. D.1）；评测任务如何设计（Sec. D.2）；竞技场如何组织（Sec. D.3）；评分模型（Sec. D.4）；A/B 评测基础设施（Sec. D.5）；竞技场揭示了关于 GR00T 2 的哪些信息（Sec. D.6），以及其局限性（Sec. D.7）。Tab. 12 概括了本附录中每个数字背后的证据依据。

<a id="C045"></a>
**Source:** p.65 C045 · 表 T012

![T012](assets/T012.png)

**Original (caption):** Table 12: GearArena at a glance (snapshot of November 6, 2026, 12:28 PT). A campaign is one A/B evaluation request, a trial runs every arm once on the same scene, a rollout is one graded robot episode, and a match is one pairwise comparison inside a trial. The three suites are separate leagues whose ratings are not comparable with each other. Five YAM campaigns ran tasks of both YAM suites and are counted in both columns, so the two YAM suites hold 195 distinct campaigns. †Dex records list stations by service identifier and do not record the operator.

**中文表注：** 表 12：GearArena 概览（2026 年 11 月 6 日 12:28 PT 快照）。评测批次（campaign）即一次 A/B 评测请求；试次（trial）指在同一场景中让每个臂各运行一次；rollout（轨迹采样）即一条经过评分的机器人片段；对战（match）即某次试次中的一次两两比较。三个套件是彼此独立的联赛，其评分之间不可比较。有五个 YAM 评测批次同时运行了两个 YAM 套件的任务，因此在两列中各计一次，两个 YAM 套件合计包含 195 个不重复的评测批次。†Dex 记录按服务标识符列出工位，且不记录操作员。

<a id="S1152"></a>
**Source:** p.65 S1152

**Original:** Graded trials 2,167 3,403 721 Graded rollouts 6,373 9,671 2,146 Pairwise matches (ties) 5,732 (30%) 6,035 (35%) 1,492 (33%) Tasks with matches 16 74 names (38 tasks) 56 Evidence window Jul 15 – Nov 6 Sep 21 – Nov 6 Sep 29 – Oct 29

**中文:** 已评分试次 2,167 3,403 721 已评分 rollout 6,373 9,671 2,146 两两对战（含平局） 5,732（30%） 6,035（35%） 1,492（33%） 含对战的任务数 16 74 names（38 个任务） 56 证据窗口 7 月 15 日 – 11 月 6 日 9 月 21 日 – 11 月 6 日 9 月 29 日 – 10 月 29 日 [存疑：原文为扁平化的单行文本，各列与数值的对应关系无法从抽取文本确认]

<a id="H36"></a>
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

<a id="C046"></a>
**Source:** p.66 C046 · 图 F034

![F034](assets/F034.png)

**Original (caption):** Figure 34: Gauging the current suite. Mean rubric score (bars) and full-credit rate (dots) per task over all graded A/B rollouts on YAM V2, grouped by sub-suite and ordered by task code (M05* is a variant of M05 with 20 rollouts). No task is near the ceiling, and six sit in the shelving zone, where nearly every rollout fails.

**中文图注：** 图 34：对当前套件的衡量。图中在 YAM V2 上所有已评分的 A/B rollout 基础上，按任务绘制平均评分量表得分（柱）与满分率（点），按子套件分组，并按任务代码排序（M05* 为 M05 的变体，含 20 次 rollout）。没有任何任务接近天花板，其中六个任务位于“搁置区”，该区域几乎每次 rollout 都失败。


<a id="H37"></a>
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

<a id="C047"></a>
**Source:** p.67 C047 · 图 F035

![F035](assets/F035.png)

**Original (caption):** Figure 35: From an A/B request to a rating. A campaign is requested with its checkpoints, tasks, trial count, and station. The station runs a blinded session in which the operator stages each scene, runs every arm, and grades and ranks the rollouts without knowing which checkpoint produced which. Recordings, the blinding manifest, latency statistics, and a checksummed results snapshot are stored with the session. The arena ingests them, decodes the blinding, admits each graded trial to its suite, and refits the ratings. Researchers choose the next comparisons from the leaderboard.

**中文图注：** 图 35：从 A/B 请求到评分。提交评测批次时需给出检查点、任务、试次数和工位。工位运行一次盲测会话：操作员布置每个场景、运行每个臂，并在不知道哪个检查点产生了哪条 rollout 的情况下对其评分和排序。录像、盲化清单、时延统计以及带校验和的结果快照都与该会话一同存储。竞技场摄取这些数据，解除盲化，把每个已评分的试次纳入其所属套件，并重新拟合评分。研究人员依据排行榜选择下一批比较。

<a id="S1228"></a>
**Source:** p.67 S1228

**Original:** suite is explicit: each suite lists its task identifiers and the embodiment tags it accepts, so evidence cannot leak between suites.

**中文:** 套件的规则很明确：每个套件列出其任务标识符及其接受的本体标签，因此证据无法在套件之间泄露。

<a id="H38"></a>
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

<a id="H39"></a>
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

![E002](assets/equations/E002.png)

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

![E003](assets/equations/E003.png)

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

<a id="C048"></a>
**Source:** p.69 C048 · 表 T013

![T013](assets/T013.png)

**Original (caption):** Table 13: Paired comparisons on YAM V2. Elo difference (A minus B) with its paired 95% interval, and the share of 500 bootstrap resamples in which A rates higher (Eq. (8)). “GR00T 2” is the released checkpoint, and the expected win rate follows from the Elo difference.

**中文表注：** 表 13：V2 上的配对比较。Elo 差值（A 减 B）及其配对 95% 区间，以及在 500 次自助重采样中 A 评分更高的比例（Eq. (8)）。“GR00T 2”为已发布的检查点，期望胜率由 Elo 差值推出。

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

<a id="C049"></a>
**Source:** p.70 C049 · 图 F036

![F036](assets/F036.png)

**Original (caption):** Figure 36: YAM V2 leaderboard. Elo with 90% scene-clustered bootstrap intervals for 20 checkpoints, colored by model family. Numbers on the right are A/B matches. ⋆marks the A/B reference. Development checkpoints are shown under anonymized aliases.

**中文图注：** 图 36：YAM V2 排行榜。展示 20 个检查点的 Elo 及其 90% 场景聚类自助法区间，按模型族着色。右侧数字为 A/B 对局数。⋆ 标记 A/B 参考。开发检查点以匿名别名显示。

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

![T014](assets/T014.png)

**Original (caption):** Table 14: Matched rubric scores by sub-suite. Mean rubric score (0 to 1) over the trials in which both checkpoints were graded in the same campaign. Trial counts in parentheses.

**中文表注：** 表 14：按子套件的匹配 rubric 分数。两个检查点在同一批次中都被评分的试次上的平均 rubric 分数（0 至 1）。括号内为试次数。

<a id="C051"></a>
**Source:** p.71 C051 · 图 F037

![F037](assets/F037.png)

**Original (caption):** Figure 37: Climbing the hill. Every checkpoint on each suite, rated relative to that suite’s A/B reference (⋆, the top-rated checkpoint) and placed at the date the checkpoint was saved. The line tracks the best checkpoint so far. Bars are paired 90% bootstrap intervals, shown for the checkpoints that set a new best. All points in a panel come from one fit on the same evidence. The two suites are separate leagues. One V1 checkpoint lies below the plotted range.

**中文图注：** 图 37：攀升。每个套件上的每个检查点，都相对于该套件的 A/B 参考（⋆，评分最高的检查点）进行评分，并按其保存日期放置。曲线追踪目前为止的最佳检查点。柱子为配对的 90% 自助法区间，仅显示设定了新最佳的检查点。同一面板中的所有点都来自同一次拟合，基于同样的证据。两个套件是各自独立的联盟。有一个 V1 检查点位于绘图范围之下。

<a id="S1341"></a>
**Source:** p.71 S1341

**Original:** How the arena was used. In the final months of the project, the arena was read weekly at the team’s training sync, as the shared reference for which checkpoints had moved the frontier and which differences were still within noise. It separated effects that absolute scores conflated: on the dexterous suite, serving the same checkpoints with a new inference regime reordered the leaderboard (the previous leader fell from first of 13 to fifth of 9), which is why inference settings are part of a checkpoint’s identity there (Sec. D.3). It also provided the real-world ground truth for calibrating simulation: the Bradley-Terry ratings from blinded A/B trials are the real-world side of the simulation-reality correlation in Sec. 4.5.2 (𝑟= 0.93).

**中文:** 竞技场如何被使用。在项目的最后几个月，竞技场每周在团队的训练同步会上被查阅一次，作为判断哪些检查点推动了前沿、哪些差异仍在噪声范围内的共同依据。它把绝对分数混为一谈的效应区分开来：在灵巧手套件上，用新的推理方式服务同一检查点会重排排行榜（此前的领先者从 13 个中的第一降至 9 个中的第五），这也是推理设置在该套件中成为检查点身份一部分的原因（见 Sec. D.3）。它还为仿真校准提供了真实世界的基准：盲测 A/B 试验得到的 Bradley-Terry 评分，即 Sec. 4.5.2 中仿真-现实相关性的现实一侧（𝑟 = 0.93）。


<a id="H40"></a>
### D.7. Limitations ｜ 局限性

<a id="S1342"></a>
**Source:** p.71 S1342

**Original:** • Relative, suite-specific ratings. Elo measures skill relative to the other checkpoints on the same suite. Ratings from different suites are not comparable, and adding a checkpoint shifts all ratings of a suite by a common constant. • Few independent units. Independent replication comes from distinct tasks, not trials: the first suite has 16 tasks with A/B comparisons, the current one 38. Intervals are correspondingly wide (median 93 Elo on V2, 128 on V1), and some checkpoints with few tasks have none. On V1, one checkpoint’s point estimate (Elo 840) lies outside its own bootstrap interval [853, 995]. We make no claims about it.

**中文:** • 相对性的、按套件区分的评分。Elo 衡量的是某个检查点相对于同一套件中其他检查点的技能。不同套件的评分不可直接比较，而且新增一个检查点会使该套件的所有评分整体平移同一个常数。• 独立单元较少。独立的重复来自不同的任务，而不是试次：第一个套件有 16 个包含 A/B 比较的任务，当前套件有 38 个。置信区间相应地较宽（V2 上的中位数为 93 Elo，V1 上为 128 Elo），而一些任务较少的检查点甚至没有区间。在 V1 上，某个检查点的点估计（Elo 840）落在其自身自助法（bootstrap）区间 [853, 995] 之外。我们不对该结果作任何结论。

<a id="C052"></a>
**Source:** p.72 C052 · 图 F038

![F038](assets/F038.png)

**Original (caption):** Figure 38: Skill versus inference speed on YAM V2. Elo against policy inferences per second (log scale), measured as server-side compute per inference during the same A/B episodes. Bars are 90% Elo intervals, shown for the labelled checkpoints (all intervals are in Fig. 36). Inference-rate intervals are narrower than the markers. Colour is the model family and marker shape the serving stack. Dashed: frontier of point estimates across stacks. Ringed: the checkpoint that dominates all others served by the GR00T 2 policy server.

**中文图注：** 图 38：YAM V2 上的技能与推理速度对比。纵轴为 Elo，横轴为每秒策略推理次数（对数刻度），按同一 A/B 回合期间每次推理的服务端计算量测得。柱体为 90% Elo 区间，仅显示带标签的检查点（所有区间见图 36）。推理速率的区间比标记更窄。颜色表示模型系列，标记形状表示服务栈。虚线：跨服务栈的点估计前沿。圈出的检查点：支配由 GR00T 2 策略服务器提供的所有其他检查点的那一个。

<a id="S1366"></a>
**Source:** p.72 S1366

**Original:** • Ties and grading. Ties are 30 to 35% of matches. Rankings come from human operators, and the rubric bounds but does not remove their judgment. • Confounds across campaigns. A/B trials remove drift within a campaign. Differences between stations and operators across campaigns are absorbed only through shared opponents, and the reference-first pairing policy keeps most checkpoints connected to the same opponents. • Live evidence. Graded trials of campaigns still in progress count immediately. Four V2 campaigns were paused at the snapshot, and the comparisons of GR00T 1.7 and 𝜋0.5 rest on campaigns from the last week before it. • Curated metadata. Model-family labels, checkpoint dates (storage timestamps), and serving stacks are recorded or inferred outside the A/B record itself. Embodiment tags and serving settings, such as 𝜋0.5’s separate embodiment tag or video-codec settings, are admission criteria but are not part of the rating.

**中文:** • 平局与评分。平局占全部比赛的 30% 至 35%。排名来自人类操作员，评分细则约束了他们的判断，但并未消除这些判断。• 跨评测批次的混杂因素。A/B 试次消除了同一评测批次（campaign）内的漂移。不同批次之间工位与操作员的差异，只能通过共同对手来吸收；参照优先的配对策略使大多数检查点仍与相同的对手相连。• 实时证据。仍在进行中的评测批次，其已评分的试次会被立即计入。快照时有四个 V2 评测批次处于暂停状态，而 GR00T 1.7 与 π0.5 的比较依赖于其之前最后一周的评测批次。• 人工整理的元数据。模型系列标签、检查点日期（存储时间戳）和服务栈，是在 A/B 记录之外记录或推断的。本体标签与服务设置（例如 π0.5 单独的本体标签或视频编解码器设置）属于准入标准，但不计入评分。

<a id="H41"></a>
### E. UMIverse for GR00T 2 ｜ GR00T 2 的 UMIverse

<a id="S1367"></a>
**Source:** p.73 S1367

**Original:** UMIverse is our family of robot-free interfaces that record human demonstrations in a robot’s own sensory and action space. Gripper UMI is a handheld parallel gripper in the lineage of the Universal Manipulation Interface (Chi et al., 2024): it carries the robot’s wrist cameras and measures the gripper width that the robot later commands. DexUMI (Xu et al., 2025) is a wearable hand exoskeleton that replicates the kinematics, contact surfaces, and camera mount of a dexterous robot hand, so that every recorded finger joint, fingertip force, and camera view has a robot counterpart. Our GEAR DexUMI (NVIDIA GEAR Team, 2026) replicates the XHAND1 Pro-U (Sec. E.4). Unlike teleoperation, neither interface needs a robot during collection. Unlike human video, both record actions in robot coordinates and observations through robot cameras.

**中文:** UMIverse 是我们的一族无需机器人的接口，用于在机器人自身的感知空间与动作空间中记录人类演示。Gripper UMI 是一款手持式平行夹爪，属于通用操作接口（Universal Manipulation Interface）（Chi et al., 2024）的谱系：它搭载机器人的腕部相机，并测量机器人随后要下达指令的夹爪宽度。DexUMI（Xu et al., 2025）是一种可穿戴的手部外骨骼，复现了灵巧机器人手的运动学、接触面与相机安装位置，因此每一个被记录的手指关节、指尖力与相机视角，在机器人侧都有对应量。我们的 GEAR DexUMI（NVIDIA GEAR Team, 2026）复现的是 XHAND1 Pro-U（Sec. E.4）。与遥操作不同，这两种接口在采集过程中都不需要机器人。与人类视频也不同，两者都以机器人坐标记录动作，并通过机器人相机记录观测。

<a id="S1368"></a>
**Source:** p.73 S1368

**Original:** The two interfaces play complementary roles in GR00T 2. Gripper UMI provides scale: collection stations in three regions supply thousands of hours of bimanual pretraining demonstrations, and the resulting policies deploy directly onto a matching robot (Sec. E.2) or transfer across an embodiment gap to YAM (Sec. B.2), a test of the cross-embodiment imagination that GR00T 2 is built for. DexUMI provides depth: post-training data for complex, long-horizon, and dynamic dexterous tasks (Sec. B.3), which GR00T 2 learns with compliance labels derived from fingertip force (Eqs. (1) and (3)). For DexUMI, the visual gap between the exoskeleton and the robot hand is addressed inside the world-action model rather than by editing video (Sec. E.6). DexUMI demonstrations can also be retargeted to a hand that the exoskeleton does not replicate, such as the Sharpa hand (Sec. B.4). The UMI →YAM transfer and the DexUMI post-training results are presented in Sec. B.2 and B.3. This appendix describes the hardware of both interfaces (Sec. E.1 and E.4), UMI direct (Sec. E.2), the embodiment gaps and ablations of the UMI →YAM transfer (Sec. E.3), and DexUMI’s post-training recipe and WAM-native inpainting (Sec. E.5 and E.6).

**中文:** 这两种接口在 GR00T 2 中扮演互补的角色。Gripper UMI 提供规模：三个地区的采集工位提供了数千小时的双臂预训练演示，所得策略既可以直接部署到匹配的机器人上（Sec. E.2），也可以跨越本体差距迁移到 YAM 上（Sec. B.2），这是对 GR00T 2 所要实现的跨本体想象力（cross-embodiment imagination）的一项检验。DexUMI 提供深度：为复杂、长时序且动态的灵巧任务提供后训练数据（Sec. B.3），GR00T 2 利用由指尖力推导出的柔顺性标签（Eqs. (1) and (3)）学习这些数据。对于 DexUMI，外骨骼与机器人手之间的视觉差异是在世界-动作模型内部处理的，而不是通过编辑视频来解决（Sec. E.6）。DexUMI 的演示也可以重定向到外骨骼并未复现的手上，例如 Sharpa 手（Sec. B.4）。UMI →YAM 迁移与 DexUMI 后训练结果分别见 Sec. B.2 和 B.3。本附录描述两种接口的硬件（Sec. E.1 和 E.4）、UMI direct（Sec. E.2）、UMI →YAM 迁移的本体差距与消融实验（Sec. E.3），以及 DexUMI 的后训练方案与 WAM 原生补全（inpainting）（Sec. E.5 和 E.6）。

<a id="H42"></a>
### E.1. Gripper UMI Hardware ｜ E.1. Gripper UMI 硬件

<a id="S1369"></a>
**Source:** p.73 S1369

**Original:** The handheld gripper mirrors its robot counterpart. Relative to the original UMI gripper (Chi et al., 2024), the main mechanical change is that the pin joints, bearings, and return springs of the finger-trigger linkage are replaced by a single compliant flexure linkage (Fig. 39) that is printed entirely on a desktop printer. This yields the following improvements over the previous design:

**中文:** 手持夹爪在结构上与其机器人版本保持一致。相较于原始的 UMI 夹爪（Chi et al., 2024），主要的机械改动在于：手指扳机连杆中原有的销轴关节、轴承与回位弹簧，被替换为一个完整的柔顺柔性铰链连杆（flexure linkage）（图 39），并且整体可直接用桌面打印机打印。相较于此前的设计，这带来以下改进：

<a id="S1370"></a>
**Source:** p.73 S1370

**Original:** • Constant force scaling. The finger-to-jaw force scaling is constant over the gripper’s entire range of motion. In the original UMI gripper, the scaling is large when the gripper is fully open but varies nonlinearly with opening, and when the gripper is fully closed the fingertip force falls to roughly 20% of the force applied at the trigger. The constant scaling of the new design instead delivers substantially higher fingertip force at small openings, which is better suited to fine-grained dexterous manipulation. • Fewer parts and faster assembly. The flexure joints are printed directly into the links, so the linkage needs no pins, bearings, or return springs and only a few fasteners, which greatly reduces part count and assembly time. • Simpler linkage and less backlash. The complex multi-part linkage is replaced by a single compliant mechanism with no discrete sliding or pivoting interfaces, which significantly reduces backlash. • Encoder-based width sensing. An encoder measures the gripper opening directly, which avoids the visual occlusion that can affect a camera-and-marker approach to width sensing.

**中文:** • 恒定的力放大比。在夹爪的整个运动范围内，从手指到钳口的力放大比都是恒定的。在原始 UMI 夹爪中，夹爪完全张开时放大比很大，并且会随开合度非线性变化；夹爪完全闭合时，指尖力降至扳机处所施力的约 20%。新设计的恒定放大比则在小开合度下提供明显更大的指尖力，更适合精细的灵巧操作。• 更少的零件与更快的装配。柔性铰链直接打印在连杆之中，因此连杆无需销轴、轴承或回位弹簧，只需少量紧固件，这大幅减少了零件数量和装配时间。• 更简单的连杆与更小的回差（backlash）。复杂的多零件连杆被替换为单一的柔顺机构，不存在离散的滑动或枢转界面，从而显著降低了回差。• 基于编码器的宽度感知。编码器直接测量夹爪开合度，避免了基于相机与标记的宽度感知方法可能受到的视觉遮挡。

<a id="S1371"></a>
**Source:** p.73 S1371

**Original:** Flexure linkage. The linkage is mirror-symmetric and rides on a 150 mm linear rail (MGN9). Rigid links and finger mounts are printed in PLA, and four TPU 90A flexure joints are printed directly into them. Each joint is a short, thin strip with a T-shaped head embedded in a pocket of the PLA part, so load transfers without additional fasteners. The operator’s finger pinch acts on the long links, and the bottom joint is guided along the symmetry plane, so pinch maps to jaw motion through a fixed lever ratio: the jaws move about 2.9× as far as the fingertips and, ideally, carry about 0.35× the finger force. Because the rigid links meet the flexures directly, the operator’s input reaches the jaws through a short, stiff load path with little lost motion.

**中文:** 柔性铰链连杆。连杆呈镜像对称，安装在一条 150 mm 直线导轨（MGN9）上。刚性连杆与手指安装件采用 PLA 打印，四个 TPU 90A 柔性铰链直接打印在其中。每个铰链是一段短而薄的条带，其一端带有 T 形头部，嵌入 PLA 零件的凹槽中，因此载荷传递无需额外紧固件。操作员的手指捏合作用于长连杆，底部铰链沿对称面导向，因此捏合动作通过固定的杠杆比转换为钳口运动：钳口的移动距离约为指尖的 2.9 倍，理想情况下所承受的手指力约为手指力的 0.35 倍。由于刚性连杆直接与柔性铰链相接，操作员的输入经由一条短而刚的载荷路径传递到钳口，几乎没有运动损耗。

<a id="S1372"></a>
**Source:** p.73 S1372

**Original:** Design rules from rapid prototyping.

**中文:** 快速原型制作中的设计规则。

<a id="C053"></a>
**Source:** p.74 C053 · 图 F039

![F039](assets/F039.png)

**Original (caption):** Figure 39: Flexure linkage of the handheld gripper. (a) Cut view at the symmetry plane with main dimensions in mm: black parts are PLA, blue parts are TPU 90A, the gray shape is the operator’s finger contour, and the four TPU joints are numbered 1 to 4 (top, mid, static, bottom). (b) Section views of joints 1 to 4: T-shaped TPU anchors sit in pockets of the PLA parts, and the short exposed strip between them forms the flexure (strip thickness 𝑡and out-of-plane width 𝑤in mm).

**中文图注：** 图 39：手持夹爪的柔性铰链连杆。(a) 对称面处的剖视图，主要尺寸单位为 mm：黑色零件为 PLA，蓝色零件为 TPU 90A，灰色轮廓为操作员手指的轮廓，四个 TPU 铰链编号为 1 至 4（顶部、中部、静态、底部）。(b) 铰链 1 至 4 的截面视图：T 形 TPU 锚固件嵌在 PLA 零件的凹槽中，二者之间裸露的短条带构成柔性铰链（条带厚度 𝑡and、面外宽度 𝑤in，单位为 mm）[公式原文见 p.74]。

<a id="S1391"></a>
**Source:** p.74 S1391

**Original:** • Thin strips: strip thickness is set by print accuracy, 1.8 mm (2.3 mm at the top joint), about four extrusion lines, so it prints reliably yet still bends. • Short necks: each exposed neck is kept short so the flexure behaves like a rotary joint, with bending concentrated at one location instead of along a long leaf spring. • Width: links and joints are 23 mm wide out of plane (16 mm for the short link and inner joints). Narrower variants twisted under side loads, while wider ones needed a firm grip to close. • Compliance: the finite compliance of TPU absorbs small mismatches between rail, mounts, and link lengths that a rigid pin-jointed version would not tolerate.

**中文:** • 薄条带：条带厚度由打印精度决定，为 1.8 mm（顶部铰链为 2.3 mm），约等于四条挤出线，因此既能可靠打印，又仍然能够弯曲。• 短颈部：每个裸露的颈部都保持较短，使柔性铰链表现得像一个转动关节，弯曲集中在一处，而不是沿着长片簧分布。• 宽度：连杆与铰链的面外宽度为 23 mm（短连杆与内侧铰链为 16 mm）。较窄的变体在侧向载荷下会扭转，而较宽的变体需要用力抓握才能闭合。• 柔顺性：TPU 有限的柔顺性能够吸收导轨、安装件与连杆长度之间的微小失配，而刚性销接版本无法承受这些失配。

<a id="S1392"></a>
**Source:** p.74 S1392

**Original:** Pre-strained open state. The linkage is printed wider than the rail allows (163.8 mm relaxed pivot span versus 118.1 mm at the rail stops), so the TPU joints are pre-strained at the open stop (Fig. 40). This provides a passive restoring force that returns the gripper to its open state and replaces separate return springs.

**中文:** 预应变张开状态。连杆的打印宽度大于导轨所允许的范围（松弛状态下的枢转跨距为 163.8 mm，而在导轨限位处为 118.1 mm），因此 TPU 铰链在张开限位处处于预应变状态（图 40）。这提供了一个被动的恢复力，使夹爪回到张开状态，并取代了单独的回位弹簧。

<a id="S1393"></a>
**Source:** p.74 S1393

**Original:** End effector. Apart from the added width encoder, sensor placement is kept consistent with the existing UMI configuration, which preserves compatibility with established data-collection pipelines. Further end-effector details, including sensing and assembly, are available in our open-source documentation (NVIDIA GEAR Team, 2026).

**中文:** 末端执行器。除新增的宽度编码器外，传感器布置与现有 UMI 配置保持一致，从而保留了与既有数据采集流程的兼容性。关于末端执行器的更多细节（包括传感与装配），请参阅我们的开源文档（NVIDIA GEAR Team, 2026）。


<a id="H43"></a>
### E.2. UMI Direct ｜ UMI 直接部署

<a id="S1394"></a>
**Source:** p.74 S1394

**Original:** UMI direct means deploying a UMI-trained policy on the corresponding UMI robot gripper, the robot counterpart of the handheld: the same sensors (the same camera board with its fisheye wrist camera and trigger camera), the same gripper kinematics (two soft-fingered carriages driven symmetrically along a rail), and the same gripper fingers. Observations and actions therefore carry over without translation: the policy sees the scene through the cameras it was trained on and commands the finger width the handheld measured, so the camera and gripper gaps are removed by construction (Sec. E.1). The robot side exchanges poses in the handheld’s wrist frame, which a per-robot hand-eye calibration maps onto the robot, and gripper widths in millimetres, the quantity the handheld measured. A policy trained on grasp-point poses and normalized widths (Sec. B.2) is wrapped so that its outputs are converted back to these quantities. On the deployment robot, the policy

**中文:** UMI 直接部署是指将基于 UMI 训练的策略部署到对应的 UMI 机器人夹爪上，该夹爪是手持设备的机器人版本：传感器相同（同一块相机板，包括鱼眼腕部相机和触发相机），夹爪运动学相同（两个软指滑块沿导轨对称驱动），夹爪手指也相同。因此，观测和动作无需转换即可直接迁移：策略通过训练时所用的相机观察场景，并下达手持设备所测得的手指宽度指令，所以相机和夹爪方面的差距在构造上即已消除（Sec. E.1）。机器人一侧以手持设备的腕部坐标系交换位姿，再经由每台机器人各自的手眼标定映射到机器人上；夹爪宽度以毫米为单位，即手持设备所测量的量。基于抓取点位姿和归一化宽度训练的策略（Sec. B.2）会被包装，使其输出换算回这些量。在部署机器人上，该策略

<a id="C054"></a>
**Source:** p.75 C054 · 图 F040

![F040](assets/F040.png)

**Original (caption):** Figure 40: Pre-strain and motion of the flexure linkage. (a) Relaxed (printed) shape (dashed) and its pose at the open stop (solid). The 22.858 mm difference per side pre-strains the TPU joints. (b) Shadows of the linkage closing from the open stop to the closed pose: the finger mounts slide inward along the rail and the bottom joint moves along the symmetry plane.

**中文图注：** 柔性铰链机构的预应变与运动。(a) 松弛（打印）形状（虚线）及其在张开限位处的姿态（实线）。每侧 22.858 mm 的差值会对 TPU 关节施加预应变。(b) 连杆从张开限位闭合到闭合姿态的阴影图：手指安装座沿导轨向内滑动，底部关节沿对称平面移动。

<a id="S1402"></a>
**Source:** p.75 S1402

**Original:** predicts 48-step action chunks, of which 30 are executed, at 30 Hz inside a 60 Hz control loop. Fig. 41 shows rollouts of UMI-direct policies on four assembly tasks.

**中文:** 策略在 60 Hz 控制循环中以 30 Hz 运行，预测 48 步动作块，其中 30 步被执行。Fig. 41 展示了 UMI 直接部署策略在四项装配任务上的 rollout（轨迹采样）。

<a id="S1403"></a>
**Source:** p.75 S1403

**Original:** Training. We post-train GR00T 2 on the Gripper UMI demonstrations of each target task alone. UMI uses the grasp-point representation on the action-head row it shares with YAM (the shared-head design of Sec. B.2), even though no YAM data enter these mixtures, and it observes four views: the head camera, the two fisheye wrist views re-projected stereographically to 320 × 240 as in pretraining, and the bottom camera.

**中文:** 训练。我们仅使用每项目标任务的 Gripper UMI 演示数据对 GR00T 2 进行后训练。UMI 在其与 YAM 共享的动作头行上采用抓取点表示（即 Sec. B.2 中的共享头设计），尽管这些数据配比中没有任何 YAM 数据。它观察四路视角：头部相机、两路鱼眼腕部视图（与预训练时相同，经立体投影重投影到 320 × 240），以及底部相机。

<a id="S1404"></a>
**Source:** p.75 S1404

**Original:** Ablation: UMI-10K in pretraining. To test whether UMI-10K data in pretraining help UMI direct, we post-train the same UMI-only recipe from two GR00T 2 pretraining checkpoints (Tab. 15): the default checkpoint, whose pretraining mixture includes UMI-10K, and a checkpoint pretrained without any UMI-10K data, the same GR00T 2 w/o UMI pretraining baseline as in Tab. 4. This checkpoint comes from an earlier pretraining run, with fewer pretraining samples, a different robot mixture, and small model differences, so part of the gap may come from these differences rather than from UMI data alone. It is not the GR00T 2 w/o cross-embodiment pretraining baseline of Sec. B.1.5, which is pretrained on target-robot data alone. The difference is large and consistent. With UMI-10K in pretraining, the four assembly tasks reach 30%, 50%, 10%, and 50% end-to-end success (average 35%) with progress scores of 79 to 94. Without it, the same post-training yields 0%, 10%, 0%, and 0% (average 2.5%) with progress scores of 60 to 75. The gap in progress is smaller than the gap in success: the policy without UMI pretraining still performs most coarse steps but fails the precision steps, screw insertion and part seating, that an assembly must chain to completion. We read this as the handheld observation domain being in-distribution for the pretrained backbone, so that post-training can spend its few hours of demonstrations on the task rather than on learning to see a handheld gripper through fisheye cameras. One caveat bounds the claim: because UMI-direct post-training places UMI on the action-head row it shares with YAM rather than on the row it was pretrained on, any benefit reaches the policy through the shared transformer, not through the pretrained action head.

**中文:** 消融实验：预训练中的 UMI-10K。为检验预训练中的 UMI-10K 数据是否有助于 UMI 直接部署，我们从两个 GR00T 2 预训练检查点（Tab. 15）出发，对同一套仅使用 UMI 的配方进行后训练：一个是默认检查点，其预训练数据配比包含 UMI-10K；另一个是未使用任何 UMI-10K 数据预训练的检查点，即与 Tab. 4 中相同的 GR00T 2 w/o UMI pretraining 基线。该检查点来自更早的预训练运行，预训练样本更少，机器人数据配比不同，模型也有细微差异，因此部分差距可能来自这些差异，而不只来自 UMI 数据。它也不同于 Sec. B.1.5 中的 GR00T 2 w/o cross-embodiment pretraining 基线（后者仅在目标机器人数据上预训练）。差距很大且一致。预训练中包含 UMI-10K 时，四项装配任务的端到端成功率分别为 30%、50%、10% 和 50%（平均 35%），任务进度分数为 79 至 94。没有 UMI-10K 时，相同的后训练得到的成功率分别为 0%、10%、0% 和 0%（平均 2.5%），任务进度分数为 60 至 75。任务进度上的差距小于成功率上的差距：未经 UMI 预训练的策略仍能完成大部分粗略步骤，但在装配必须连贯完成的精细步骤（螺钉插入和零件就位）上失败。我们认为，这是因为手持设备的观测域对预训练主干而言属于分布内，因此后训练可以把有限的几小时演示用于任务本身，而不必去学习通过鱼眼相机识别手持夹爪。有一项限定条件约束了这一论断：由于 UMI 直接部署的后训练把 UMI 放在与 YAM 共享的动作头行上，而非其预训练时所在的行，任何收益都是通过共享的 Transformer 传递给策略的，而不是通过预训练的动作头。

<a id="H44"></a>
### E.3. UMI →YAM Transfer: Embodiment Gaps and Ablations ｜ UMI→YAM 迁移：本体差距与消融实验

<a id="S1405"></a>
**Source:** p.75 S1405

**Original:** As described in Sec. 3.2 and Sec. B.2, GR00T 2 can be adapted to a bimanual gripper robot from handheld Gripper UMI demonstrations alone, with no teleoperation of the target robot. In this section, we present the details behind that result: how co-training lets the model absorb the appearance difference on its own (Fig. 14),

**中文:** 如 Sec. 3.2 和 Sec. B.2 所述，GR00T 2 仅凭手持 Gripper UMI 演示即可适配到双臂夹爪机器人，无需对目标机器人进行遥操作。本节给出该结果背后的细节：联合训练如何让模型自行吸收外观差异（Fig. 14），

<a id="C055"></a>
**Source:** p.76 C055 · 图 F041

![F041](assets/F041.png)

**Original (caption):** Figure 41: UMI direct rollouts. Each row shows one task with its instruction and six keyframes of a GR00T 2 policy post-trained on Gripper UMI demonstrations alone and deployed on the UMI robot gripper, numbered by stage: Toy Dumptruck Assembly, Toy Plane Assembly, Bluey Car Assembly, and Monster Truck Assembly. Each task requires placing parts, driving screws, and reorienting the body of the toy.

**中文图注：** UMI 直接部署的 rollout。每行展示一项任务，包括其指令以及一个 GR00T 2 策略的六个关键帧。该策略仅在 Gripper UMI 演示上进行后训练，并部署在 UMI 机器人夹爪上，关键帧按阶段编号。任务包括 Toy Dumptruck Assembly、Toy Plane Assembly、Bluey Car Assembly 和 Monster Truck Assembly。每项任务都需要放置零件、拧入螺钉，并调整玩具主体的朝向。

<a id="C056"></a>
**Source:** p.76 C056 · 表 T015

![T015](assets/T015.png)

**Original (caption):** Table 15: UMI direct. Prog. is the average substage score and SR the end-to-end success rate on the UMI robot gripper, both on a 0 to 100 scale, of GR00T 2 post-trained on Gripper UMI demonstrations alone. GR00T 2 w/o UMI pretraining starts from an earlier pretraining checkpoint whose mixture contains no UMI-10K data, while GR00T 2 starts from the default checkpoint, whose pretraining mixture includes UMI-10K. Each task uses 10 trials, and the last row averages the four tasks. Bold marks the best Prog. and SR in each row.

**中文表注：** UMI 直接部署。任务进度（Prog.）为各子阶段分数的平均值，成功率（SR）为 UMI 机器人夹爪上的端到端成功率，两者均为 0 到 100 的刻度，对象是仅在 Gripper UMI 演示上后训练的 GR00T 2。GR00T 2 w/o UMI pretraining 从一个更早的预训练检查点出发，其数据配比不含 UMI-10K；GR00T 2 则从默认检查点出发，其预训练数据配比包含 UMI-10K。每项任务使用 10 次试次，最后一行为四项任务的平均值。每行中最优的 Prog. 和 SR 以粗体标出。

<a id="S1410"></a>
**Source:** p.76 S1410

**Original:** the three gaps that remain in sensing, actuation, and environment and the quantities that define them (Tab. 16), and four ablations that isolate the design choices on which the transfer depends (Tab. 17).

**中文:** 仍然存在的三类差距（感知、驱动和环境）以及定义这些差距的量（Tab. 16），还有四项消融实验，用于隔离迁移所依赖的设计选择（Tab. 17）。

<a id="S1411"></a>
**Source:** p.76 S1411

**Original:** E.3.1. Setup

**中文:** E.3.1. 实验设置

<a id="S1412"></a>
**Source:** p.76 S1412

**Original:** The UMI head, wrist, and bottom cameras fill YAM’s top, wrist, and bottom view slots (Fig. 42). The benchmark comprises Toy Dumptruck Assembly, NIST Board Disassembly, and Conveyor Belt Sorting and Tossing (Fig. 29 and Tab. 4). The UMI cohorts comprise 75 episodes for Toy Dumptruck Assembly, 74 for NIST Board Disassembly, and 41 for Conveyor Belt Sorting and Tossing. None of the YAM co-training sources contains a demonstration of any benchmark task. As in UMI direct, the policy predicts 48-step action chunks, of which 30 are executed.

**中文:** UMI 的头部、腕部和底部相机分别填充 YAM 的顶部、腕部和底部视角槽位（Fig. 42）。基准测试包括 Toy Dumptruck Assembly、NIST Board Disassembly，以及 Conveyor Belt Sorting and Tossing（Fig. 29 和 Tab. 4）。UMI 数据组分别包含 Toy Dumptruck Assembly 的 75 个片段、NIST Board Disassembly 的 74 个片段，以及 Conveyor Belt Sorting and Tossing 的 41 个片段。YAM 联合训练数据源中没有任何一个包含基准测试任务的演示。与 UMI 直接部署相同，策略预测 48 步动作块，其中 30 步被执行。

<a id="S1413"></a>
**Source:** p.76 S1413

**Original:** E.3.2. What Co-Training Absorbs

**中文:** E.3.2. 联合训练吸收了什么

<a id="S1414"></a>
**Source:** p.76 S1414

**Original:** The model imagines the robot. The UMI demonstrations show a human’s arms and the blue-fingered handheld gripper, whereas the deployed policy sees YAM’s own arms and gripper. GR00T 2 bridges this appearance difference natively rather than by editing the training videos. Because it predicts future frames jointly with actions, the task-agnostic YAM data teach it what YAM looks like and the UMI data teach it what the task

**中文:** 模型会想象机器人本身。UMI 演示中呈现的是人的手臂和蓝色手指的手持夹爪，而部署时的策略看到的是 YAM 自身的手臂和夹爪。GR00T 2 原生地弥合了这种外观差异，而不是通过编辑训练视频来实现。由于它与动作联合预测未来帧，与任务无关的 YAM 数据教会它 YAM 长什么样，UMI 数据教会它任务长什么样

<a id="C057"></a>
**Source:** p.77 C057 · 表 T016

![T016](assets/T016.png)

**Original (caption):** Table 16: Gripper UMI versus YAM. YAM differs from the handheld gripper in its cameras, its gripper interface, and its control frame.

**中文表注：** Gripper UMI 与 YAM 的对比。YAM 在相机、夹爪接口和控制坐标系上与手持夹爪不同。

<a id="S1425"></a>
**Source:** p.77 S1425

**Original:** looks like, and at deployment the two combine in the model’s imagined future. Fig. 14 shows this directly: conditioned on the same YAM top-camera frame, a model post-trained on UMI data alone predicts human arms and UMI fingers entering the scene, whereas the co-trained model predicts YAM’s arms performing the assembly. The co-training data therefore supply more than action statistics. They give the world model the robot’s body, so that a task seen only in human hands is imagined, and then executed, on the robot.

**中文:** 长什么样，并在部署时两者会在模型想象的未来中结合。Fig. 14 直接展示了这一点：以同一张 YAM 顶部相机帧为条件，仅在 UMI 数据上后训练的模型预测人的手臂和 UMI 手指进入画面，而联合训练的模型则预测 YAM 的手臂执行装配。因此，联合训练数据提供的不只是动作统计量。它们给世界模型提供了机器人的身体，使得一项只在人手中见过的任务，能够在机器人上被想象并随后执行。

<a id="S1426"></a>
**Source:** p.77 S1426

**Original:** E.3.3. What Remains: Three Embodiment Gaps

**中文:** E.3.3. 尚存的问题：三类本体差距

<a id="S1427"></a>
**Source:** p.77 S1427

**Original:** Co-training absorbs the visual appearance of the robot, but it does not by itself close the embodiment gap. Three gaps remain, in sensing, actuation, and environment, and each requires a deliberate design choice. We quantify them in turn (Tab. 16) and then ablate the choices that close them.

**中文:** 联合训练可以吸收机器人的视觉外观，但它本身并不能消除本体差距。仍有三类差距，分别在感知、驱动和环境方面，每一类都需要有意识的设计选择。我们依次对它们进行量化（Tab. 16），然后对能够消除它们的设计选择进行消融。

<a id="S1428"></a>
**Source:** p.77 S1428

**Original:** • Sensing gap. The two embodiments observe the scene through cameras with substantially different fields of view (Tab. 16 and Fig. 42). UMI pairs a wide-FOV head camera with fisheye wrist cameras of about 180∘(OAK), whereas YAM uses a standard-FOV top camera and pinhole wrist cameras of 78 × 63∘ (RealSense D405). The two wrist cameras also differ in orientation and in where they sit relative to the fingers. As a result, even the stereographic re-projection of the wrist fisheye used in pretraining places the scene 74 to 94 px from where YAM’s camera shows it at 320 × 240 (Fig. 43). The lens centers are also 4.9 cm apart, so a re-projection can align the scene but not the fingers, which stay smaller in the UMI view than in YAM’s. Beyond geometry, the UMI frames show the operator’s arms and the handheld gripper, whereas YAM’s frames show its own arms and gripper (Fig. 42). • Actuation gap. Beyond sensing, the two embodiments differ in how actions relate to states and in the space in which actions are expressed (Tab. 16). First is action versus state. A UMI demonstration only records the pose the handheld gripper reached, so action and state coincide and the data assume zero tracking error. On YAM, the action is the command of a teleoperation leader arm and the state is where the follower arrives, and the two differ because the follower is a low-stiffness position-controlled arm (brushless motors with 40:1 shoulder and 10:1 wrist reductions under a PD controller with joint stiffness from 80 down to 10 N m/rad). It lags the leader by about four frames (133 ms at 30 Hz) and settles at a load-dependent offset from the command. YAM data thus teach the policy to command ahead of, and offset from, the observed state, whereas UMI data teach it to command the state itself. Second is the control space. UMI acts in end-effector space, with gripper widths as labels. YAM’s action row holds the end-effector pose and width plus the six joint positions of each arm, 32 dimensions in all. Handheld data supply only the 20 end-effector dimensions, and the 12 joint dimensions have no counterpart. Even the shared dimensions use different conventions: UMI poses refer to a wrist frame at the gripper motor center

**中文:** • 感知差距。两种本体通过视场差异显著的相机观察场景（Tab. 16 和 Fig. 42）。UMI 配有宽视场头部相机和约 180∘（OAK）的鱼眼腕部相机，而 YAM 使用标准视场顶部相机和 78 × 63∘（RealSense D405）的针孔腕部相机。两路腕部相机的朝向不同，相对于手指的位置也不同。因此，即使对预训练中所用的腕部鱼眼进行立体投影重投影，场景在 320 × 240 图像中的位置，与 YAM 相机中的位置仍相差 74 至 94 px（Fig. 43）。两个镜头的中心相距 4.9 cm，所以重投影可以让场景对齐，但无法让手指对齐，手指在 UMI 视图中仍比在 YAM 视图中显得更小。除几何差异外，UMI 画面中可以看到操作者的手臂和手持夹爪，而 YAM 画面中看到的是它自身的手臂和夹爪（Fig. 42）。• 驱动差距。除感知外，两种本体在动作与状态的关系以及动作所处的空间上也不同（Tab. 16）。首先是动作与状态。UMI 演示只记录手持夹爪到达的位姿，因此动作与状态重合，数据隐含了零跟踪误差的假设。在 YAM 上，动作是遥操作主臂的指令，状态是从臂实际到达的位置。两者之所以不同，是因为从臂是低刚度的位置控制机械臂（无刷电机，肩部减速比 40:1、腕部减速比 10:1，在 PD 控制器下关节刚度从 80 降至 10 N m/rad）。它比主臂滞后约四帧（30 Hz 下为 133 ms），并稳定在与指令相差的、随负载变化的偏移量上。因此，YAM 数据教会策略提前于并偏离观测到的状态发出指令，而 UMI 数据则教会它直接对状态本身发出指令。其次是控制空间。UMI 在末端执行器空间中动作，以夹爪宽度作为标签。YAM 的动作行包含末端执行器位姿和宽度，以及每条机械臂的六个关节位置，共 32 维。手持数据只提供其中的 20 维末端执行器维度，12 维关节维度在 UMI 中没有对应项。即使是共享的维度，两者的约定也不同：UMI 位姿参照位于夹爪电机中心的腕部坐标系 [存疑：抽取文本在此截断]

<a id="C058"></a>
**Source:** p.78 C058 · 图 F042

![F042](assets/F042.png)

**Original (caption):** Figure 42: Gripper UMI versus YAM, same task, same camera slots. Top: a Gripper UMI demonstration of Toy Dumptruck Assembly seen through its wide-FOV head camera and two fisheye wrist cameras, recorded in the wild. Bottom: the YAM robot performing the task in its cell, seen through the standard-FOV top camera and two wrist RealSense cameras that fill the same observation slots. Right: the handheld UMI gripper and the YAM gripper, each with its wrist camera. The lines mark the full opening between the fingertips (85.55 mm and 96 mm). Both frames show the same step: the left gripper holds the truck while the right gripper brings the second wheel to the axle.

**中文图注：** Gripper UMI 与 YAM 对比，同一任务，同样的相机槽位。上方：Gripper UMI 演示 Toy Dumptruck Assembly，通过宽视场头部相机和两路鱼眼腕部相机在野外采集。下方：YAM 机器人在其工作单元中执行同一任务，通过标准视场顶部相机和两路 RealSense 腕部相机观察，这些相机占据相同的观测槽位。右侧：手持 UMI 夹爪与 YAM 夹爪，各自带有腕部相机。线条标出指尖之间的完整开口（85.55 mm 和 96 mm）。两帧展示的是同一步骤：左侧夹爪夹住卡车，右侧夹爪将第二个车轮送到车轴上。

<a id="C059"></a>
**Source:** p.78 C059 · 图 F043

![F043](assets/F043.png)

**Original (caption):** Figure 43: Wrist views for UMI →YAM transfer. The same UMI wrist frame as (a) the raw fisheye, (b) the stereographic view used in pretraining, and (c) the YAM-aligned re-render that imitates YAM’s wrist camera. (d) The real YAM wrist camera at the same step.

**中文图注：** UMI→YAM 迁移的腕部视图。同一 UMI 腕部画面的 (a) 原始鱼眼图像、(b) 预训练中使用的立体投影视图，以及 (c) 模仿 YAM 腕部相机的 YAM 对齐重渲染。(d) 同一步骤下真实的 YAM 腕部相机画面。

<a id="S1446"></a>
**Source:** p.79 S1446

**Original:** and YAM poses to a grasp site 0.1347 m from the flange, and UMI records the width in millimetres against an 85.55 mm opening whereas YAM takes a normalized [0, 1] command against 96 mm. In training, we move the UMI wrist frame 0.1347 m along its approach axis to the grasp site and normalize the widths to match YAM. • Environment gap. Finally, the UMI demonstrations are recorded in the wild, whereas the policy is evaluated in a YAM cell whose workspace, lighting, and background never appear in the demonstrations (Fig. 42). The YAM co-training data show the cell but contain no demonstration of the target tasks, so they provide observations of the evaluation scene but no evidence of the target tasks.

**中文:** 并将 YAM 的位姿对应到距法兰 0.1347 m 处的抓取点；UMI 以毫米记录宽度，对应 85.55 mm 的开口，而 YAM 以归一化的 [0, 1] 指令对应 96 mm 的开口。训练时，我们将 UMI 腕部坐标系沿其接近轴移动 0.1347 m 到抓取点，并对宽度进行归一化以匹配 YAM。• 环境差距。最后，UMI 演示是在野外采集的，而策略是在 YAM 工作单元中评测的，该工作单元的工作空间、光照和背景从未出现在演示中（Fig. 42）。YAM 联合训练数据展示了该工作单元，但不包含目标任务的演示，因此它们提供了评测场景的观测，却没有目标任务的证据。

<a id="S1447"></a>
**Source:** p.79 S1447

**Original:** E.3.4. Ablations

**中文:** E.3.4. 消融实验

<a id="S1448"></a>
**Source:** p.79 S1448

**Original:** The default recipe uses a shared action head, YAM-aligned wrist views, all UMI episodes, and a pretrained checkpoint that includes UMI-10K data. Four ablations each change one of these choices and report the result in Tab. 17: whether UMI shares YAM’s action head (actuation gap), whether the UMI wrist views are aligned to YAM’s camera (sensing gap), how many UMI demonstrations are needed, and whether UMI data in pretraining matter.

**中文:** 默认配方使用共享动作头、与 YAM 对齐的腕部视图、全部 UMI 片段，以及包含 UMI-10K 数据的预训练检查点。四项消融实验各自改变其中一项选择，并在 Tab. 17 中报告结果：UMI 是否与 YAM 共享动作头（驱动差距）、UMI 腕部视图是否与 YAM 相机对齐（感知差距）、需要多少条 UMI 演示，以及预训练中的 UMI 数据是否重要。

<a id="C060"></a>
**Source:** p.79 C060 · 表 T017

![T017](assets/T017.png)

**Original (caption):** Table 17: UMI →YAM ablations. Prog. is the average substage score and SR the end-to-end success rate on YAM, both on a 0 to 100 scale, as in Tab. 4. The shaded row in each block is the default configuration (shared action head, YAM-aligned wrist-view warping, all UMI episodes, pretraining with UMI-10K data), and the other rows change that one choice. For Conveyor Belt Sorting and Tossing, SR is the share of 50 items sorted, and there is no separate progress score. Bold marks the best value in each block.

**中文表注：** UMI→YAM 消融实验。任务进度（Prog.）为 YAM 上各子阶段分数的平均值，成功率（SR）为端到端成功率，两者均为 0 到 100 的刻度，与 Tab. 4 相同。每个区块中的阴影行为默认配置（共享动作头、YAM 对齐的腕部视图扭曲、全部 UMI 片段、包含 UMI-10K 数据的预训练），其他行则只改变其中一项选择。对于 Conveyor Belt Sorting and Tossing，SR 为 50 件物品中被分拣的占比，没有单独的进度分数。每个区块中的最佳值以粗体标出。

<a id="S1460"></a>
**Source:** p.79 S1460

**Original:** Ablation 1: shared versus separate action head. GR00T 2 shares its diffusion transformer across embodiments but keeps one row of action-encoder, state-encoder, and action-decoder weights per embodiment. The sharedhead arm re-expresses UMI in YAM’s semantics and places it on YAM’s row: grasp-site poses, absolute widths normalized by the 85.55 mm full opening, the first 20 of YAM’s 32 action dimensions, and YAM’s normalization statistics. The separate-head arm keeps UMI on the row it was pretrained on, with wrist-frame relative poses, relative widths in millimetres, and its own statistics. The separate arm therefore changes the action representation as well as the head, so the comparison is not a single-variable change. The two arms trade embodiment grounding against skill coverage, and the results in Tab. 17 split along that line. The shared head is clearly stronger on Toy Dumptruck Assembly (60% versus 10%) and Conveyor Belt Sorting and Tossing (86% versus 64%), whereas the separate head is slightly better on NIST Board Disassembly (60% versus 50%, progress 93 versus 86). The NIST margin is concentrated in the hex-nut subtask, which the separate head completes in 7 of 10 trials and the shared head in 5 of 10. This is also the subtask on which the demonstrations are most specific: the UMI demonstrators slide the nut off its post without rotating the wrist, and the YAM co-training data do not contain this way of removing a nut. With the shared head, UMI actions are decoded by the same weights as the YAM data, so the decoder’s prior follows YAM’s motion statistics, and a strategy that appears only in the demonstrations is reproduced less reliably. The separate head keeps UMI on the row it was pretrained on and preserves the demonstrators’ strategy. The same mechanism explains the reverse outcome on the other two tasks: where the demonstrated motions are ones the YAM data already perform, placing UMI on YAM’s row grounds the task evidence directly in YAM’s action statistics and controller, whereas the separate head must rely on the transformer to map YAM observations onto a row it has never seen paired with them. The shared head is therefore the better default, while the separate head helps only where the demonstrations rely on a motion strategy that the co-training data do not share.

**中文:** 消融实验 1：共享动作头与独立动作头。GR00T 2 在各本体之间共享其扩散 Transformer，但为每个本体保留一组动作编码器、状态编码器和动作解码器权重。共享头方案[存疑：原文 "sharedhead" 疑为漏空格]将 UMI 重新表达为 YAM 的语义，并放在 YAM 的动作行上：抓取点位姿、以 85.55 mm 全开口归一化的绝对宽度、YAM 32 个动作维度中的前 20 维，以及 YAM 的归一化统计量。独立头方案则让 UMI 保留在其预训练时所在的行上，使用腕部坐标系下的相对位姿、以毫米为单位的相对宽度以及其自身的统计量。因此，独立方案同时改变了动作表示和动作头，两者的对比并非单变量改变。两种方案是在本体锚定与技能覆盖之间做取舍，Tab. 17 中的结果恰好沿此方向分化。共享头在 Toy Dumptruck Assembly（60% 对 10%）和 Conveyor Belt Sorting and Tossing（86% 对 64%）上明显更强，而独立头在 NIST Board Disassembly（60% 对 50%，进度 93 对 86）上略胜一筹。NIST 上的优势集中在六角螺母子任务上：独立头在 10 次试次中完成了 7 次，共享头则完成了 5 次。这也是演示最具特殊性的子任务：UMI 演示者不转动手腕，而是将螺母从其柱子上滑下来，而 YAM 联合训练数据中不包含这种取出螺母的方式。使用共享头时，UMI 动作由与 YAM 数据相同的权重解码，因此解码器的先验遵循 YAM 的运动统计，而仅出现在演示中的策略则被复现得不够可靠。独立头使 UMI 保留在其预训练所在的行上，从而保留了演示者的策略。同样的机制也解释了另外两项任务上的相反结果：当演示的运动正是 YAM 数据已经执行过的动作时，把 UMI 放在 YAM 的行上可以将任务证据直接锚定到 YAM 的动作统计量和控制器上，而独立头则必须依靠 Transformer 将 YAM 观测映射到一个从未与之配对过的行上。因此，共享头是更好的默认选择，而独立头只在演示依赖于联合训练数据并不共享的运动策略时才有帮助。


<a id="S1463"></a>
**Source:** p.80 S1463

**Original:** Ablation 2: wrist-view alignment. We re-render the native UMI fisheye (≈180∘) as a virtual standard-FOV pinhole camera at the same optical center that imitates YAM’s 78 × 63∘wrist view (Tab. 16 and Fig. 43): a 202.96 px focal length at 320 × 240 (76.5 × 61.2∘), pitched about 27.1∘down, with rotation and focal length fitted in Isaac Sim on 112 same-scene UMI/YAM render pairs. On held-out pairs, the scene error is 8 px for objects closer than 30 cm and 11 px beyond, versus 74 and 94 px for the stereographic view, and the grasp zone is resolved at 12.5 rather than 6.9 px/cm for the raw fisheye. Identical maps back-fill the training data and run at deployment. We stress that this alignment is approximate. It matches the field of view and the viewing direction of YAM’s wrist camera, but not the lens, the stereo baseline, the offset of the optical center from the gripper, or the appearance of the arm and fingers in the frame, and the residual discrepancy is visible in Fig. 43. We compare three training views for the UMI wrist cameras: the stereographic view used in pretraining, the YAM-aligned view, and a random choice between the two on every training sample. Only the aligned view transfers on the two long-horizon tasks (Tab. 17). With the stereographic view, end-to-end success is 0% on both long-horizon tasks, and 46% of the items are sorted on Conveyor Belt Sorting and Tossing. The random mixture recovers 60% on tossing but still 0% on the long-horizon tasks, while the aligned view reaches 60%, 50%, and 86%. The progress scores tell a more specific story. They fall only moderately without alignment (96 to 79 on Toy Dumptruck Assembly, 86 to 76 on NIST Board Disassembly), so the policy still performs most steps. What it loses is the precision steps, in which the gripper must meet a screw hole or a nut within a few millimetres. A view mismatch moves the grasp zone in the image and changes its pixel scale (12.5 versus 6.9 px/cm), which corrupts exactly the image-to-action mapping those steps depend on, while leaving coarse transport intact. The random mixture helps only on tossing (60% versus 46%), where coarse transport suffices, and not on the precision steps, because it asks the policy to be invariant to a viewpoint change that is informative for those steps. The policy averages over two geometries and is sharp in neither. We draw two conclusions. First, the video model absorbs the appearance gap, since human arms and a handheld gripper in training versus robot arms in deployment do not prevent transfer, but it does not absorb a geometric gap. Second, the geometry need only be roughly matched: coarse agreement in field of view and viewing direction is sufficient to recover most of the transfer, which makes the method practical for new target robots whose wrist cameras are known only from a datasheet.

**中文:** 消融实验 2：腕部视角对齐。我们将原生 UMI 鱼眼相机（≈180∘）重新渲染为一个虚拟的标准视场针孔相机，光心保持不变，使其模仿 YAM 的 78 × 63∘ 腕部视角（见表 16 与图 43）：焦距为 202.96 px，分辨率为 320 × 240（视场 76.5 × 61.2∘），并向下俯仰约 27.1∘。旋转与焦距在 Isaac Sim 中，依据 112 组同一场景的 UMI/YAM 渲染图像对拟合得到。在留出的图像对上，距离小于 30 cm 的物体场景误差为 8 px，更远处为 11 px；相比之下，立体投影视图的误差分别为 74 px 和 94 px。抓取区域在对齐后的分辨率为 12.5 px/cm，而原始鱼眼图像仅为 6.9 px/cm。相同的映射既用于回填训练数据，也用于部署运行。我们强调，这种对齐只是近似的。它匹配了 YAM 腕部相机的视场与观察方向，但没有匹配镜头、立体基线、光心相对夹爪的偏移，也没有匹配画面中手臂与手指的外观；剩余的差异在图 43 中清晰可见。我们为 UMI 腕部相机比较了三种训练视图：预训练中使用的立体投影视图（stereographic）、YAM 对齐视图，以及对每个训练样本在两者之间随机选择。只有对齐视图能在两个长时序任务上实现迁移（见表 17）。使用立体投影视图时，两个长时序任务的端到端成功率均为 0%，而在 Conveyor Belt Sorting and Tossing 任务中，有 46% 的物品被分拣。随机混合在抛掷任务上达到 60%，但在两个长时序任务上仍为 0%；对齐视图则分别达到 60%、50% 和 86%。任务进度分数呈现的情况更为具体。在不对齐的情况下，它们只是适度下降（Toy Dumptruck Assembly 从 96 降到 79，NIST Board Disassembly 从 86 降到 76），因此策略仍能完成大部分步骤。它丢失的是精细步骤：此时夹爪必须在数毫米内对准螺丝孔或螺母。视图失配会使抓取区域在图像中移位，并改变其像素尺度（12.5 对 6.9 px/cm），这恰恰破坏了这些步骤所依赖的图像到动作映射，而粗略的搬运则基本不受影响。随机混合仅在抛掷任务上有帮助（60% 对 46%），因为粗略搬运已经足够；但在精细步骤上它没有帮助，因为它要求策略对视角变化保持不变，而这种视角变化恰恰对这些步骤有信息价值。策略在两种几何结构之间取平均，结果在两者上都不够精确。我们得出两个结论。第一，视频模型能够吸收外观差异：训练中是人手臂与手持夹爪、部署中是机器人手臂，这并不妨碍迁移；但它无法吸收几何差异。第二，几何只需大致匹配：视场与观察方向的粗略一致就足以恢复大部分迁移效果，这使得该方法适用于仅能从数据手册获知腕部相机参数的新目标机器人。

<a id="S1465"></a>
**Source:** p.80 S1465

**Original:** Ablation 3: amount of UMI data. The UMI demonstrations are the only source of the target task, so their number bounds how much task evidence post-training can draw on. We shrink each cohort to about half and a quarter of its episodes at a fixed 0.6 : 0.4 UMI : YAM sampling ratio (Tab. 17). The three tasks degrade very differently. Conveyor Belt Sorting and Tossing is nearly flat (86%, 84%, 70%): it is a short-horizon dynamic skill with one decisive event, and 20 episodes already cover it. Toy Dumptruck Assembly degrades gradually in end-to-end success (60%, 30%, 10%) while its progress score stays high (96, 92, 81), the signature of a long horizon in which small per-step losses compound multiplicatively. Notably, the policy trained on only 20 demonstrations still completes the full four-stage assembly end to end in 1 of 10 trials and 81% of its individual steps, on a robot that has never been teleoperated for the task. NIST Board Disassembly collapses at the first halving (50% to 0%), and the substage table shows why: the nut subtask goes from 5 of 10 to 0 of 10 while the other four subtasks barely move. The data requirement of a task is therefore set not by its length but by its hardest subskill, the one with the least support in both the pretraining and the co-training data. That subskill is the first to disappear as demonstrations are removed, and in a sequential task its loss zeroes the end-to-end rate. In practice, 41 to 75 handheld demonstrations sufficed for every task here, and half of that sufficed whenever the task contained no such rare subskill.

**中文:** 消融实验 3：UMI 数据量。UMI 演示是目标任务的唯一来源，因此其数量限定了后训练能够利用的任务证据规模。我们在固定的 0.6 : 0.4 UMI : YAM 采样比例下，将每个数据队列缩减至约一半和四分之一的回合数（见表 17）。三项任务的退化方式差异很大。Conveyor Belt Sorting and Tossing 几乎保持不变（86%、84%、70%）：它是一项短时序的动态技能，只包含一个决定性事件，20 个回合即足以覆盖它。Toy Dumptruck Assembly 的端到端成功率逐步下降（60%、30%、10%），而其任务进度分数仍保持较高水平（96、92、81），这是长时序任务的典型特征：每一步的微小损失会以乘法方式累积。值得注意的是，仅用 20 条演示训练的策略，仍能在 10 次试次中有 1 次端到端地完整完成四阶段装配，并完成 81% 的单个步骤，而该机器人从未针对此任务接受过遥操作。NIST Board Disassembly 在第一次减半时即崩溃（50% 到 0%），子阶段表格说明了原因：螺母子任务从 10 次中成功 5 次降为 0 次，而其余四个子任务几乎没有变化。因此，一项任务所需的数据量并非由其长度决定，而是由其最困难的子技能决定，即在预训练与联合训练数据中支持最少的那项子技能。随着演示数据被移除，这项子技能会最先消失；在顺序任务中，它的缺失会使端到端成功率归零。实际上，这里每项任务只需 41 至 75 条手持演示即可满足；只要任务中不包含此类稀有子技能，所需数量约为其一半。

<a id="S1467"></a>
**Source:** p.81 S1467

**Original:** Ablation 4: UMI-10K in pretraining. The main result (Tab. 4) already shows that starting from a checkpoint pretrained without UMI data reduces transfer success to 20% and 0% on the long-horizon tasks and the share of conveyor items sorted to 34%. We repeat the row in Tab. 17 and examine what pretraining contributes. Both models see the same post-training data and the same number of steps, so the difference lies entirely in what the pretrained weights already encode. The checkpoint without UMI also differs in pretraining length, robot mixture, and small model details (Sec. E.2), so not all of the gap need come from UMI data. We identify two contributions. First, with UMI-10 data in pretraining, UMI’s observation domain, a handheld gripper and human arms seen through fisheye wrist views, is already in-distribution for the video backbone, so post-training does not have to learn to see the demonstrations. Second, and more important for transfer, pretraining on UMI alongside YAM and the other robot corpora aligns UMI’s actions with the other embodiments inside the shared transformer: the model has already learned that a UMI grasp and a YAM grasp are the same event. Post-training then only needs to attach task evidence to an alignment that exists, whereas without UMI in pretraining the same 41 to 75 episodes must simultaneously teach the observation domain, bind it to YAM’s action semantics, and teach the task. The few-shot budget is spent on the embodiment rather than on the task. The progress scores are consistent with this reading. Without UMI pretraining the policy still performs most coarse steps (84 and 65), so it does learn the task structure. It fails at the precision steps, where an imprecise embodiment alignment turns into a missed hole or a dropped part. UMI data in cross-embodiment pretraining are thus not a convenience but the mechanism that makes a few dozen demonstrations sufficient.

**中文:** 消融实验 4：预训练中的 UMI-10K。主要结果（表 4）已经表明，若从未使用 UMI 数据预训练的检查点出发，迁移成功率在长时序任务上降至 20% 和 0%，传送带分拣的物品比例降至 34%。我们在表 17 中重复了该行，并考察预训练究竟贡献了什么。两个模型使用相同的后训练数据和相同的步数，因此差异完全来自预训练权重已经编码的内容。未使用 UMI 的检查点在预训练时长、机器人混合比例以及一些细小的模型细节（见第 E.2 节）上也有所不同，因此并非所有差距都必然来自 UMI 数据。我们识别出两项贡献。第一，预训练中包含 UMI-10 数据[存疑：原文为 UMI-10，疑为 UMI-10K 的抽取截断]后，UMI 的观测域（手持夹爪以及通过鱼眼腕部视角看到的人类手臂）已经属于视频骨干网络的分布内数据，因此后训练无需再学习看懂这些演示。第二，也是对迁移更重要的一点：在预训练中，UMI 与 YAM 及其他机器人语料一同训练，会在共享的 Transformer 中将 UMI 动作与其他本体对齐：模型已经学会，UMI 的抓取与 YAM 的抓取是同一事件。此时后训练只需将任务证据附着到已经存在的对齐关系上；而若预训练中没有 UMI，同样的 41 至 75 个回合就必须同时教会观测域、将其与 YAM 的动作语义绑定，并教会任务本身。少样本的预算因此被用于本体适配，而非任务学习。任务进度分数与这一解读一致。没有 UMI 预训练时，策略仍能完成大部分粗略步骤（84 与 65），因此它确实学会了任务结构。它在精细步骤上失败，此时不精确的本体对齐会转化为漏插或掉落零件。因此，跨本体预训练中的 UMI 数据并非锦上添花，而是使几十条演示就足以奏效的机制。


<a id="H45"></a>
### E.4. DexUMI Exoskeleton Hardware ｜ E.4. DexUMI 外骨骼硬件

<a id="S1468"></a>
**Source:** p.81 S1468

**Original:** The GEAR DexUMI exoskeleton (NVIDIA GEAR Team, 2026) replicates the kinematics of the target robot hand (XHAND1 Pro-U) joint for joint and reproduces its fingertip and palm contact surfaces, which keeps the visual and physical gap to the robot small for policy training. It is also designed for wearability, so that operators can comfortably collect high-quality data across long, dexterous tasks. Compared with the original DexUMI, it offers the following improvements:

**中文:** GEAR DexUMI 外骨骼（NVIDIA GEAR Team, 2026）逐关节复刻了目标机器人手（XHAND1 Pro-U）的运动学，并还原了其指尖与手掌的接触表面，使策略训练时人手采集环境与机器人之间的视觉和物理差距保持较小。该外骨骼还考虑了穿戴性，使操作员能够舒适地在长时序、灵巧的任务中采集高质量数据。与原始 DexUMI 相比，它有以下改进：

<a id="S1470"></a>
**Source:** p.81 S1470

**Original:** • More degrees of freedom. The exoskeleton captures 16 degrees of freedom, using 20 joints of which four pairs are coupled. • Higher precision and durability. Machined parts give higher precision and durability. • No over-constraint, better tracking and wearability. Removing non-essential contact surfaces and adopting a remote-center-of-motion (RCM) linkage resolves the over-constraint of the original structure. The structure flexes less, which improves tracking precision and wearability. • Daisy-chained encoders. The joint encoders are daisy-chained, which simplifies cable management. • Left and right hands. Both left- and right-hand versions are available, enabling bimanual tasks.

**中文:** • 更多自由度。该外骨骼可采集 16 个自由度，使用 20 个关节，其中四对关节存在耦合。• 更高的精度与耐久性。机加工零件带来更高的精度与耐久性。• 消除过约束，跟踪与穿戴性更好。去除非必要的接触表面，并采用远程运动中心（RCM）连杆机构，解决了原结构的过约束问题。结构形变更小，从而提升了跟踪精度与穿戴性。• 编码器串联。各关节编码器采用串联连接，简化了线缆管理。• 左手与右手版本。左右手版本均可提供，支持双臂任务。

<a id="S1471"></a>
**Source:** p.81 S1471

**Original:** Remote-center-of-motion joints. Matching the robot hand’s abduction/adduction (AB/AD) and flexion joints is a packaging problem, since those joint centers lie where the operator’s finger is. We replicate them with an RCM linkage that creates a virtual joint at the robot hand’s joint center without placing hardware in the operator’s workspace (Fig. 44a). The RCM is a parallel four-bar linkage. To avoid over-constraining it, only two of the four holes at the top joint are used. Leaving the other two unused reduces binding from manufacturing tolerances and keeps motion smooth.

**中文:** 远程运动中心关节。要匹配机器人手的外展/内收（AB/AD）关节与屈曲关节，是一个封装问题，因为这些关节中心恰好位于操作员手指所在的位置。我们用 RCM 连杆机构来复刻它们：该机构在机器人手的关节中心处形成一个虚拟关节，同时不在操作员的工作空间内放置硬件（Fig. 44a）。RCM 是一个平行四连杆机构。为避免对它造成过约束，顶部关节的四个孔中只使用其中两个。保留另外两个孔不用，可以减少制造公差造成的卡滞，并使运动更顺滑。

<a id="S1472"></a>
**Source:** p.81 S1472

**Original:** Thumb. The thumb linkages use a “kicked-out” geometry that preserves the robot hand’s thumb kinematics while clearing space for the operator’s own thumb, so its range of motion is unobstructed during dexterous manipulation (Fig. 44b).

**中文:** 拇指。拇指连杆采用“外撇式”几何结构，在保留机器人手拇指运动学的同时，为操作员自己的拇指留出空间，使其在灵巧操作过程中的运动范围不受阻碍（Fig. 44b）。

<a id="S1473"></a>
**Source:** p.81 S1473

**Original:** Rigid, compact joints. Every joint is supported on both sides to prevent deflection and improve measurement precision. Custom pins keep joint bulk low while forming secure connections, and a variant with a direct keying interface mates to the joint encoders, reducing backlash and improving sensor accuracy (Fig. 45a).

**中文:** 刚性紧凑的关节。每个关节两侧均有支撑，以防止形变并提高测量精度。定制销钉在形成可靠连接的同时保持关节体积较小；另一种带有直接键连接接口的版本与关节编码器配合，可以减小回差并提高传感器精度（Fig. 45a）。

<a id="C061"></a>
**Source:** p.82 C061 · 图 F044

![F044](assets/F044.png)

**Original (caption):** Figure 44: GEAR DexUMI kinematic design. (a) A remote-center-of-motion linkage places a virtual joint at the robot hand’s AB/AD and flexion joint centers. (b) The kicked-out thumb linkage keeps the robot hand’s thumb kinematics while clearing the operator’s thumb.

**中文图注：** 图 44：GEAR DexUMI 运动学设计。(a) 远程运动中心连杆机构在机器人手的 AB/AD 关节与屈曲关节中心处设置虚拟关节。(b) 外撇式拇指连杆在保留机器人手拇指运动学的同时，为操作员的拇指留出空间。

<a id="S1476"></a>
**Source:** p.82 S1476

**Original:** Contact surfaces and camera. The fingertip and palm tactile-sensor contact surfaces match the robot hand’s, and the fingertip geometry is reproduced on the exoskeleton to reduce the visual gap between human collection and robot execution (Fig. 45b). Non-essential contact surfaces are removed to improve wearability. The camera mounting angle and alignment are carried over to the robot hand’s mount, so the collected images match the deployed field of view (Fig. 45c). Finally, the chassis is anodized green so that a color threshold can segment it for the masked-video augmentation (Sec. E.6).

**中文:** 接触表面与相机。指尖与手掌的触觉传感器接触表面与机器人手保持一致，外骨骼上还原了指尖几何形状，以减小人工采集与机器人执行之间的视觉差距（Fig. 45b）。为提高穿戴性，去除了非必要的接触表面。相机的安装角度与对准方式沿用到机器人手的安装座上，因此采集的图像与部署时的视场一致（Fig. 45c）。最后，外壳采用阳极氧化的绿色，使颜色阈值能够将其分割出来，用于掩码视频增广（Sec. E.6）。

<a id="S1477"></a>
**Source:** p.82 S1477

**Original:** Sensing. The exoskeleton fingertips report force in the robot hand’s own tactile format: five fingertip sensors with two pads and three force axes each, 30 channels per hand. Per hand, an iPhone tracks a wrist frame 12.6 cm from its lens, which a per-arm hand-eye calibration maps onto the robot, and the same 640 × 400, 45 fps wrist and head cameras serve collection and deployment.

**中文:** 传感。外骨骼指尖以机器人手自身的触觉格式回传力信息：每个指尖配有五个传感器，每个传感器包含两个触点和三个力分量，每只手共 30 个通道。每只手通过一部 iPhone 跟踪腕部坐标系，该坐标系位于其镜头前方 12.6 cm 处，并由每条手臂的手眼标定映射到机器人上。同一套 640 × 400、45 fps 的腕部相机与头部相机同时用于采集与部署。

<a id="H46"></a>
### E.5. DexUMI Post-Training Recipe ｜ DexUMI 后训练方案

<a id="S1478"></a>
**Source:** p.82 S1478

**Original:** For the DexUMI results of Sec. B.3, we post-train the 2B GR00T 2 model from the GR00T 2 pretraining checkpoint for 60,000 steps at a learning rate of 3 × 10−5, with 224 × 320 images from the wrist cameras and, optionally, the head camera. The policy predicts 40-step action chunks at stride 2 on the 45 fps data: relative end-effector poses for each arm and, for each hand, either absolute joint positions with joint torques or offset joint positions in their place (Eqs. (1) and (3)).

**中文:** 对于 Sec. B.3 中的 DexUMI 结果，我们从 GR00T 2 预训练检查点出发，对 2B 的 GR00T 2 模型进行后训练，训练 60,000 步，学习率为 3 × 10−5，输入为腕部相机的 224 × 320 图像，并可选地加入头部相机图像。策略在 45 fps 数据上以步长 2 预测 40 步动作块：各手臂的相对末端执行器位姿，以及各只手的一组量，二者择一，即绝对关节位置加关节力矩，或以偏移关节位置代替之（Eqs. (1) and (3)）。

<a id="H47"></a>
### E.6. DexUMI WAM-Native Inpainting ｜ DexUMI 的 WAM 原生补全（inpainting）

<a id="S1479"></a>
**Source:** p.82 S1479

**Original:** GR00T 2 addresses the visual gap between the exoskeleton and the robot hand inside training rather than by editing video: it corrupts the exoskeleton region so that the model cannot rely on exoskeleton-specific appearance. By WAM-native inpainting we mean this in-model treatment, in place of offline video editing. Our earlier pipeline, following the original DexUMI (Xu et al., 2025), filmed each demonstration replayed on a real robot hand, segmented the exoskeleton from manually picked keypoints, inpainted it with ProPainter, and composited the robot hand back in, at the cost of robot time, manual input, and GPU-heavy segmentation and inpainting.

**中文:** GR00T 2 在训练过程中处理外骨骼与机器人手之间的视觉差距，而不是通过编辑视频来解决。它会对外骨骼区域施加扰动，使模型无法依赖外骨骼特有的外观。这里的“WAM 原生补全”指的正是这种模型内部的处理方式，用以替代离线视频编辑。我们早期的流程沿用原始 DexUMI（Xu et al., 2025）：每段演示在真实机器人手上回放并拍摄，然后根据人工选取的关键点分割出外骨骼，用 ProPainter 进行补全，再把机器人手合成回画面中。这一流程需要付出机器人时间、人工输入，以及计算开销较大的分割与补全工作。

<a id="S1480"></a>
**Source:** p.82 S1480

**Original:** Exoskeleton masks. We segment the green regions in every camera video with HSV color bands, morphological cleanup, and a ±2-frame temporal majority vote, and store each mask as a lossless binary video beside its RGB stream.

**中文:** 外骨骼掩码。我们对每个相机视频中的绿色区域进行分割：先用 HSV 颜色阈值，再做形态学清理，并结合 ±2 帧的时间多数投票。每个掩码以无损二值视频的形式，与其 RGB 视频流一同存储。

<a id="C062"></a>
**Source:** p.83 C062 · 图 F045

![F045](assets/F045.png)

**Original (caption):** Figure 45: GEAR DexUMI joints, contact surfaces, and camera. (a) Double-sided joint support and a custom pin with a direct keying interface to the joint encoder. (b) Fingertip and palm contact surfaces replicate the robot hand’s tactile sensors. (c) The camera mount matches the robot hand’s mounting angle and alignment.

**中文图注：** 图 45：GEAR DexUMI 的关节、接触表面与相机。(a) 双面关节支撑，以及带有直接键连接接口、与关节编码器相连的定制销钉。(b) 指尖与手掌的接触表面复现了机器人手的触觉传感器。(c) 相机支架的安装角度与对准方式与机器人手一致。

<a id="S1484"></a>
**Source:** p.83 S1484

**Original:** Masked-video augmentation. During training only, GR00T 2 corrupts the masked region before cropping and resizing, with one draw of corruption parameters per sample shared across frames and views, blended in through a feathered mask:

**中文:** 掩码视频增广。仅在训练时，GR00T 2 会在裁剪和缩放之前对掩码区域施加扰动。每个样本只抽取一次扰动参数，并在所有帧与所有视角之间共享，再通过羽化掩码混合回原图：

![E004](assets/equations/E004.png)

<a id="E004"></a>
**Source:** p.83 E004

**Original:** , 𝛼= 𝐺𝜎* 𝑚, (9)

**中文:** 该式定义混合权重 α：先对二值掩码 𝑚 施加高斯模糊 𝐺𝜎，得到随掩码边界平滑衰减的权重。式中 (9) 为公式编号。$$, 𝛼= 𝐺𝜎* 𝑚, (9)$$ [公式原文见 p.83]

<a id="S1489"></a>
**Source:** p.83 S1489

**Original:** where 𝑚is the binary mask and 𝐺𝜎a Gaussian blur with 𝜎= 6 px at 640 px width, so the corruption fades out over a narrow band around the mask and pixels farther from it stay bit-identical. The default corruption 𝑐rotates hue over the full color wheel, scales saturation by 𝑈[0.1, 1.2] and value by 𝑈[0.2, 1.15], and adds luminance noise. The saturation and value ranges deliberately reach dark, desaturated colors because the deployed robot hand is largely black. Masks are dropped from the deployed model’s inputs, so a checkpoint needs only RGB and inference frames pass through unchanged.

**中文:** 其中 𝑚 为二值掩码，𝐺𝜎 为高斯模糊，𝜎 = 6 px（以 640 px 宽度计），因此扰动会在掩码周围的一条窄带内逐渐衰减，远离掩码的像素保持逐位一致。默认扰动 𝑐 在整个色轮上旋转色相，按 𝑈[0.1, 1.2] 缩放饱和度，按 𝑈[0.2, 1.15] 缩放明度，并加入亮度噪声。饱和度与明度的取值范围特意覆盖暗色与低饱和度颜色，因为部署的机器人手大部分是黑色的。掩码不进入已部署模型的输入，因此检查点只需要 RGB 输入，推理帧则原样通过。[公式原文见 p.83]

<a id="H48"></a>
### F. RL Post-Training ｜ 强化学习后训练

<a id="S1490"></a>
**Source:** p.84 S1490

**Original:** Pretraining equips GR00T 2 with broad visual and motor priors, but reliable real-world manipulation often requires adaptation to precise alignment, contact dynamics, and physical interaction. Reinforcement learning (RL) provides a complementary approach to supervised fine-tuning (SFT), enabling policies to improve through robot experience and task-level feedback.

**中文:** 预训练为 GR00T 2 提供了广泛的视觉与运动先验，但可靠的真实世界操作往往还需要适应精确对齐、接触动力学和物理交互。强化学习（RL）是监督微调（SFT）的一种补充方法，使策略能够借助机器人经验和任务层面的反馈不断改进。

<a id="S1492"></a>
**Source:** p.84 S1492

**Original:** Applying RL to GR00T 2 introduces unique challenges. Unlike action-only policies, GR00T 2 jointly generates actions and predicted visual futures through iterative denoising. Policy optimization must therefore accommodate joint video-action computation while enabling effective exploration. Furthermore, physical interaction is expensive, requiring efficient algorithms and infrastructure to make iterative post-training practical.

**中文:** 将 RL 应用于 GR00T 2 带来了独特的挑战。与仅输出动作的策略不同，GR00T 2 通过迭代去噪同时生成动作与预测的视觉未来。因此，策略优化必须既能适应视频-动作的联合计算，又能支持有效的探索。此外，物理交互代价高昂，需要高效的算法与基础设施，才能使迭代式后训练切实可行。

<a id="S1493"></a>
**Source:** p.84 S1493

**Original:** We address these challenges through three complementary components. First, we develop direct GR00T 2 posttraining methods, including GRPO-based optimization (Shao et al., 2024) and self-imitation from successful RL exploration, alongside residual RL for localized corrections (Sec. F.1). Second, we leverage AutoRL, an autonomous research system that discovers and improves RL post-training algorithms through closed-loop experimentation in simulation (Sec. F.2). Third, we develop scalable infrastructure that coordinates robot interaction, training, and evaluation while preserving experience and minimizing iteration overhead (Sec. F.3). We demonstrate these capabilities on four real-world precision manipulation tasks (Sec. F.4). We also investigate RL post-training through interaction with a learned neural simulator. We adapt DreamDojo (Gao et al., 2026) to recorded policy rollouts, then demonstrate that GR00T 2 can improve through world-model-based RL (Sec. F.5).

**中文:** 我们通过三个互补的部分应对这些挑战。第一，我们开发直接的 GR00T 2 后训练方法，包括基于 GRPO 的优化（Shao et al., 2024）、来自成功 RL 探索的自模仿（self-imitation），以及用于局部修正的残差强化学习（residual RL）（Sec. F.1）。第二，我们利用 AutoRL，这是一个自主研究系统，通过仿真中的闭环实验发现并改进 RL 后训练算法（Sec. F.2）。第三，我们开发了可扩展的基础设施，用于协调机器人交互、训练与评测，同时保存经验并尽量减少迭代开销（Sec. F.3）。我们在四项真实世界的精确操作任务上展示了这些能力（Sec. F.4）。我们还通过与一个学习得到的神经仿真器交互，研究 RL 后训练。我们将 DreamDojo（Gao et al., 2026）适配到录制的策略 rollout（轨迹采样）上，然后证明 GR00T 2 可以通过基于世界模型的强化学习（world-model-based RL）得到改进（Sec. F.5）。


<a id="H49"></a>
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

<a id="C063"></a>
**Source:** p.85 C063 · 图 F046

![F046](assets/F046.png)

**Original (caption):** Figure 46: Joint video-action denoising with CPS exploration. Four action-denoising events alternate between joint and cached passes. CPS adds fresh noise only to executed action coordinates. Video denoising is deterministic given its initial latent. GRPO scores joint action transitions and backpropagates through their joint forward passes, with carried latents detached.

**中文图注：** 图 46：采用 CPS 探索的联合视频-动作去噪。四个动作去噪事件在联合前向传播与缓存前向传播之间交替。CPS 只向可执行的动作坐标加入新噪声。给定初始潜变量，视频去噪是确定性的。GRPO 对联合动作转移打分，并通过其联合前向传播反向传播，其中携带的潜变量被分离（detach）。

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

<a id="E005"></a>
**Source:** p.85 E005

![E005](assets/equations/E005.png)

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

<a id="E006"></a>
**Source:** p.86 E006

![E006](assets/equations/E006.png)

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


<a id="H50"></a>
### F.2. Automated Discovery of RL Post-Training Algorithms ｜ 强化学习后训练算法的自动发现

<a id="S1591"></a>
**Source:** p.87 S1591

**Original:** Developing effective RL post-training algorithms for robot foundation models involves choices across objectives, exploration, credit assignment, reward design, and rollout horizons. These decisions interact with task characteristics and model architectures, making algorithm development an iterative process of experimentation and refinement.

**中文:** 为机器人基础模型开发有效的强化学习后训练算法，需要在目标函数、探索、信用分配、奖励设计以及 rollout（轨迹采样）时域等方面作出选择。这些决策与任务特性和模型架构相互影响，因此算法开发是一个通过实验与改进不断迭代的过程。

<a id="S1592"></a>
**Source:** p.87 S1592

**Original:** We leverage AutoRL, an autonomous research framework for closed-loop experimentation, to systematically improve RL post-training algorithms for GR00T 2. The research agent analyzes training failures, proposes hypotheses, modifies code, and evaluates candidate algorithms under fixed protocols. We ran AutoRL for

**中文:** 我们利用 AutoRL（一个用于闭环实验的自主研究框架），系统性地改进 GR00T 2 的强化学习后训练算法。研究智能体分析训练失败、提出假设、修改代码，并在固定协议下评估候选算法。我们将 AutoRL 运行了

<a id="C064"></a>
**Source:** p.88 C064 · 图 F047

![F047](assets/F047.png)

**Original (caption):** Figure 47: Autonomous RL recipe discovery with AutoRL. Hill-climbing performance on RoboCasa365 across successive agent-driven experiments. The curve shows the best evaluation performance achieved.

**中文图注：** 图 47：基于 AutoRL 的自主强化学习配方发现。在 RoboCasa365 上，相继由智能体驱动的实验中的爬山式性能变化。曲线表示所达到的最佳评测性能。

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

<a id="H51"></a>
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

<a id="C065"></a>
**Source:** p.90 C065 · 图 F048

![F048](assets/F048.png)

**Original (caption):** Figure 48: Online post-training infrastructure. (A) Algorithm interfaces, worker groups, and shared services. (B) Resource allocation across execution roles. (C) Experience pipelining. (D) Stateful recovery. Execution patterns are illustrative.

**中文图注：** 图 48：在线后训练基础设施。(A) 算法接口、工作组与共享服务。(B) 跨执行角色的资源分配。(C) 经验流水线。(D) 有状态恢复。执行模式仅作示意。

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

<a id="C066"></a>
**Source:** p.91 C066 · 表 T018

![T018](assets/T018.png)

**Original (caption):** Table 18: Per-iteration time breakdown for single-robot GRPO. All times are reported in minutes.

**中文表注：** 表 18：单机器人 GRPO 每次迭代的时间分解。所有时间均以分钟为单位。

<a id="C067"></a>
**Source:** p.91 C067 · 图 F049

![F049](assets/F049.png)

**Original (caption):** Figure 49: Real-world RL tasks. (A) Fixed-pipe fittings: grasp, align, engage threads, turn, and release. (B) Finger placement: grasp, align two pins with the base holes, insert, and release. (C) Cable insertion: plug an Ethernet cable into a network switch. (D) Charger insertion: plug a charger into an outlet.

**中文图注：** 图 49：真实世界强化学习任务。(A) 固定管件：抓取、对准、啮合螺纹、旋转并释放。(B) 手指放置：抓取、将两根销钉对准底座孔位、插入并释放。(C) 线缆插入：将以太网线插入网络交换机。(D) 充电器插入：将充电器插入插座。

<a id="S1674"></a>
**Source:** p.91 S1674

**Original:** efficient use of limited physical interaction resources.

**中文:** 更高效地利用有限的物理交互资源。


<a id="H52"></a>
### F.4. Precision Manipulation through RL Post-Training ｜ 通过 RL 后训练实现精密操作

<a id="S1675"></a>
**Source:** p.91 S1675

**Original:** We evaluate three complementary post-training approaches on four real-world contact-rich manipulation tasks, demonstrating how GR00T 2 improves through RL-based learning and targeted policy adaptation.

**中文:** 我们在四个真实世界的富接触操作任务上评估了三种互补的后训练方法，展示 GR00T 2 如何通过基于强化学习（RL）的学习和有针对性的策略适配获得提升。

<a id="S1676"></a>
**Source:** p.91 S1676

**Original:** Tasks. Our evaluation includes four precision manipulation tasks (Fig. 49). In fixed-pipe fittings, the robot grasps a threaded tee fitting, aligns it with a horizontally mounted pipe, engages the threads, and completes one full turn. This is the Fixed-Pipe Fittings task of Tab. 1a, but each RL trial starts from a fitting pose that the post-trained policy struggles with. In finger placement, the robot inserts two 3 mm pins on a gripper finger into matching holes on a fixed base, requiring accurate position and yaw alignment.

**中文:** 任务。我们的评估包含四个精密操作任务（Fig. 49）。在固定管件（fixed-pipe fittings）任务中，机器人抓取一个带螺纹的三通管件，将其与水平安装的管道对齐，咬合螺纹，并完整旋转一圈。这就是 Tab. 1a 中的 Fixed-Pipe Fittings 任务，但每次 RL 试次都从一个后训练策略难以应对的管件位姿开始。在手指放置（finger placement）任务中，机器人需要把夹爪手指上的两根 3 mm 销钉插入固定底座上对应的孔中，这要求准确的位置对齐和偏航（yaw）对齐。

<a id="S1677"></a>
**Source:** p.91 S1677

**Original:** In cable insertion, the robot inserts an Ethernet connector into a designated network-switch port, with success determined by network-link connectivity. In charger insertion, the robot inserts a two-prong charger into a specified outlet within a 2 × 6 grid. These tasks involve tight geometric tolerances, partial occlusion, and contact-sensitive execution.

**中文:** 在线缆插入（cable insertion）任务中，机器人将以太网接头插入指定的网络交换机端口，成功与否以网络链路是否连通为准。在充电器插入（charger insertion）任务中，机器人需要把两极插头的充电器插入 2 × 6 网格中指定的插座。这些任务涉及严格的几何公差、部分遮挡以及对接触敏感的执行过程。

<a id="S1678"></a>
**Source:** p.91 S1678

**Original:** Evaluation Protocol. All evaluated methods build on the same SFT-initialized GR00T 2 checkpoint, either as an initialization or as a frozen base. GRPO directly updates GR00T 2 using both successful and failed trajectories. Self-imitation reuses successful GRPO rollouts without additional collection. Residual RL instead learns a separate controller on top of the frozen base, using human-assisted training experience.

**中文:** 评估协议。所有被评估的方法都以同一个经监督微调（SFT）初始化的 GR00T 2 检查点为基础，它要么作为初始化，要么作为冻结的基座。GRPO 直接使用成功和失败的轨迹来更新 GR00T 2。自模仿（self-imitation）复用成功的 GRPO rollout，不需要额外采集。残差强化学习（Residual RL）则相反，它在冻结的基座之上学习一个独立的控制器，并使用人工辅助的训练经验。

<a id="S1680"></a>
**Source:** p.92 S1680

**Original:** For each task, evaluations use the same target distribution, reset conditions, and time limits, with no human intervention during evaluation. Trials are independent of training rollouts, and we report per-task success rates. An episode is considered a failure if misalignment prevents the policy from recovering or if the insertion exceeds the time limit.

**中文:** 对每个任务，评估都使用相同的目标分布、重置条件和时间限制，评估期间不进行人工干预。试次与训练 rollout 相互独立，我们报告各任务的成功率。若错位使策略无法恢复，或插入过程超过时间限制，则该回合记为失败。

<a id="S1681"></a>
**Source:** p.92 S1681

**Original:** Real-World Results. Direct RL on GR00T 2 improves precision manipulation. GRPO increases success rates on all four tasks (Fig. 5), raising fixed-pipe fittings from 66% to 86%, finger placement from 58% to 72%, cable insertion from 76% to 92%, and charger insertion from 40% to 94%. With 50 trials per task, the gains on charger insertion and fixed-pipe fittings are significant at the 5% level (two-sided Fisher exact test), whereas those on cable insertion (38 to 46 successes) and finger placement (29 to 36) are not conclusive at this sample size.

**中文:** 真实世界结果。对 GR00T 2 直接进行 RL 可以提升精密操作能力。GRPO 在全部四个任务上都提高了成功率（Fig. 5），固定管件从 66% 提高到 86%，手指放置从 58% 提高到 72%，线缆插入从 76% 提高到 92%，充电器插入从 40% 提高到 94%。每个任务进行 50 次试次时，充电器插入和固定管件的提升在双侧 Fisher 精确检验下达到 5% 显著性水平；而线缆插入（成功次数从 38 增至 46）和手指放置（从 29 增至 36）的提升在此样本量下尚无定论。

<a id="S1682"></a>
**Source:** p.92 S1682

**Original:** Self-imitation consolidates successful RL exploration. Self-imitation reaches 88% on fixed-pipe fittings, 98% on finger placement, 94% on cable insertion, and 96% on charger insertion, matching or exceeding GRPO on all four tasks. The gain is most pronounced on finger placement, where success rises from 72% to 98%.

**中文:** 自模仿巩固了成功的 RL 探索。自模仿在固定管件上达到 88%，在手指放置上达到 98%，在线缆插入上达到 94%，在充电器插入上达到 96%，在全部四个任务上都与 GRPO 持平或超过 GRPO。提升最明显的是手指放置任务，其成功率从 72% 升至 98%。

<a id="S1683"></a>
**Source:** p.92 S1683

**Original:** These results highlight the potential of combining RL exploration with supervised policy optimization. RL discovers successful behaviors through interaction, while self-imitation consolidates them under a stable supervised objective. This offers a complementary route to improving GR00T 2 beyond direct policy-gradient optimization.

**中文:** 这些结果凸显了将 RL 探索与监督式策略优化相结合的潜力。RL 通过交互发现成功的行为，而自模仿则在稳定的监督目标下巩固这些行为。这为改进 GR00T 2 提供了一条补充途径，超越了直接的策略梯度优化。

<a id="S1684"></a>
**Source:** p.92 S1684

**Original:** Residual RL enables targeted adaptation without updating GR00T 2. Residual RL reaches 76% on fixed-pipe fittings, 84% on finger placement, 82% on cable insertion, and 70% on charger insertion, with clear gains over supervised post-training on finger placement and charger insertion. These results show that lightweight corrective controllers can improve precision execution while leaving the pretrained GR00T 2 intact.

**中文:** 残差 RL 无需更新 GR00T 2 即可实现有针对性的适配。残差 RL 在固定管件上达到 76%，在手指放置上达到 84%，在线缆插入上达到 82%，在充电器插入上达到 70%，并且在手指放置和充电器插入上相对监督后训练有明显提升。这些结果表明，轻量级的纠正性控制器可以在保持预训练 GR00T 2 完整不变的同时，提升精密执行能力。

<a id="S1685"></a>
**Source:** p.92 S1685

**Original:** These experiments show that direct RL, self-imitation, and residual RL can improve GR00T 2’s precision manipulation through complementary forms of post-training.

**中文:** 这些实验表明，直接 RL、自模仿和残差 RL 都能通过各自互补的后训练形式，提升 GR00T 2 的精密操作能力。

<a id="S1686"></a>
**Source:** p.92 S1686

**Original:** The preceding experiments improve policies through physical interaction. We next investigate a complementary source of training experience: interaction with a learned environment constructed from recorded policy rollouts.

**中文:** 前面的实验是通过物理交互来改进策略的。接下来，我们研究另一种互补的训练经验来源：与一个由已录制的策略 rollout 构建而成的学习环境进行交互。

<a id="H53"></a>
### F.5. Reinforcement Learning with Neural Simulation ｜ 基于神经仿真的强化学习

<a id="S1687"></a>
**Source:** p.92 S1687

**Original:** In neural-simulation RL, the policy interacts with a learned world model in place of the physical environment. This changes how training experience is generated while retaining reward-based optimization of the pretrained world-action policy.

**中文:** 在神经仿真 RL 中，策略与一个学习得到的世界模型交互，以代替物理环境。这改变了训练经验的生成方式，同时保留了对预训练世界-动作策略进行基于奖励的优化。

<a id="S1688"></a>
**Source:** p.92 S1688

**Original:** We use DreamDojo (Gao et al., 2026), initialized from pretrained video priors, to turn recorded robot interactions into a learning environment. Successful and failed attempts provide supervision for task-specific adaptation. A pretrained GR00T 2 policy can then collect further training experience through interaction with the adapted model. Task rollouts are still required to construct this environment, while subsequent policy-learning rollouts are generated in neural simulation.

**中文:** 我们使用 DreamDojo（Gao et al., 2026），以预训练的视频先验进行初始化，将已录制的机器人交互转化为学习环境。成功和失败的尝试为面向具体任务的适配提供监督。随后，预训练的 GR00T 2 策略可以通过与适配后的模型交互，收集更多训练经验。构建该环境仍然需要任务 rollout，而之后的策略学习 rollout 则在神经仿真中生成。

<a id="S1689"></a>
**Source:** p.92 S1689

**Original:** To support policy learning, the model’s predictions must provide usable inputs to GR00T 2 throughout an episode. We provide multi-view camera predictions, align them with executed action chunks, and approximate proprioceptive inputs using action targets. We also maintain visual history across successive world-model calls. We first describe world-model construction and the closed-loop policy interface, including support for long-horizon interaction. We then present the experimental setup, reward modeling and policy optimization, and results in RoboLab and on real-world tasks.

**中文:** 为支持策略学习，模型的预测在整个回合中都必须能为 GR00T 2 提供可用的输入。我们提供多视角相机预测，将其与已执行的动作块对齐，并使用动作目标近似本体感知输入。我们还在连续的世界模型调用之间维持视觉历史。我们首先介绍世界模型的构建以及闭环策略接口，包括对长时序交互的支持。随后介绍实验设置、奖励建模与策略优化，以及在 RoboLab 和真实世界任务上的结果。

<a id="S1690"></a>
**Source:** p.92 S1690

**Original:** Training Data and Task Adaptation. We first mid-train DreamDojo on multi-view episodes, then adapt the resulting model to downstream tasks. The bimanual YAM corpus contains 8,310 four-view episodes from policy rollouts and DAgger collection, including failed attempts and recovery. These episodes total approximately 226.8 hours at 30 Hz. The DROID source corpus contains 57,773 episodes, approximately 273 hours at 15 Hz, with three synchronized camera views and recorded joint and gripper actions.

**中文:** 训练数据与任务适配。我们先在多视角回合上对 DreamDojo 进行中段训练（mid-training），然后将得到的模型适配到下游任务。双臂 YAM 数据集包含 8,310 个四视角回合，来自策略 rollout 和 DAgger 采集，其中包括失败尝试和恢复过程。这些回合合计约 226.8 小时，采样频率为 30 Hz。DROID 源数据集包含 57,773 个回合，约 273 小时，采样频率为 15 Hz，具有三个同步的相机视角，并记录了关节动作和夹爪动作。

<a id="S1692"></a>
**Source:** p.93 S1692

**Original:** We tile synchronized camera views into one video canvas so that the model predicts them jointly using DreamDojo’s existing video backbone and causal variational autoencoder (VAE). YAM uses a 2 × 2 layout at 480 × 640 pixels. DROID concatenates three 180 × 320 views horizontally and pads the canvas vertically to 192 × 960 pixels.

**中文:** 我们把同步的相机视角平铺拼接成一张视频画布，使模型能够利用 DreamDojo 现有的视频主干网络和因果变分自编码器（VAE）对它们进行联合预测。YAM 采用 480 × 640 像素的 2 × 2 布局。DROID 将三个 180 × 320 的视角水平拼接，并在垂直方向上将画布填充至 192 × 960 像素。

<a id="S1693"></a>
**Source:** p.93 S1693

**Original:** Video and action sampling are aligned separately. For YAM, we downsample video from 30 to 15 Hz while retaining fourteen-dimensional actions at 30 Hz. Each window contains five conditioning frames and twelve future frames, paired with 24 future actions. DROID video and eight-dimensional actions both remain at 15 Hz, and each window contains five conditioning frames and sixteen future frames. We precompute and cache VAE latents, which are the compressed video representations used by the world model. We sample temporally aligned training windows from this cache, avoiding repeated encoding of the same recorded videos.

**中文:** 视频采样与动作采样分别对齐。对于 YAM，我们将视频从 30 Hz 降采样到 15 Hz，同时保留 30 Hz 的十四维动作。每个窗口包含五个条件帧和十二个未来帧，并与 24 个未来动作配对。DROID 的视频和八维动作均保持在 15 Hz，每个窗口包含五个条件帧和十六个未来帧。我们预先计算并缓存 VAE 潜变量，它们是世界模型所使用的压缩视频表示。我们从该缓存中采样时间对齐的训练窗口，避免对相同的已录制视频重复编码。

<a id="S1694"></a>
**Source:** p.93 S1694

**Original:** Task adaptation. We adapt the mid-trained world model to the scenes and action distributions encountered by the target policy. Successful and failed rollouts provide supervision on the states reached during execution, allowing the model to learn task-relevant visual changes and action effects. We fine-tune the model on these rollouts using the multi-view representation and temporal alignment used during policy interaction. Recorded robot actions and world-model inputs use consistent action coordinates and normalization.

**中文:** 任务适配。我们将中段训练后的世界模型适配到目标策略所遇到的场景和动作分布。成功和失败的 rollout 为执行过程中到达的状态提供监督，使模型能够学习与任务相关的视觉变化和动作效果。我们在策略交互时所用的多视角表示和时间对齐方式下，利用这些 rollout 对模型进行微调。已录制的机器人动作与世界模型输入使用一致的动作坐标和归一化方式。

<a id="S1695"></a>
**Source:** p.93 S1695

**Original:** Closed-Loop Simulation Interface. To collect experience for policy optimization, we alternate GR00T 2 action prediction with world-model prediction throughout a task episode. A rollout starts from recorded multi-view observations. GR00T 2 predicts an action sequence, and the world model predicts the camera observations resulting from its executed prefix. These predicted images become the policy’s next visual input, allowing GR00T 2 to respond to the consequences of its own actions. Repeating this interaction produces a trajectory for reward evaluation and policy learning.

**中文:** 闭环仿真接口。为了收集策略优化所需的经验，我们在整个任务回合中交替进行 GR00T 2 的动作预测与世界模型预测。rollout 从已录制的多视角观测开始。GR00T 2 预测一段动作序列，世界模型则预测其已执行前缀所导致的相机观测。这些预测图像成为策略的下一个视觉输入，使 GR00T 2 能够对自身动作的后果作出响应。重复这一交互过程，即可得到用于奖励评估和策略学习的轨迹。

<a id="S1696"></a>
**Source:** p.93 S1696

**Original:** At interaction round 𝑟, GR00T 2 samples an action plan from the current observation and task instruction. Let 𝐴𝑟denote its executed prefix of 𝐻actions and 𝐶𝑟the world model’s conditioning latents. Initially, 𝐶0 is obtained by encoding five recorded video frames into two latent frames. The mapping 𝑔converts actions into the world model’s action coordinates and normalization. Future latents and the next conditioning history are then given by

**中文:** 在第 𝑟 轮交互中，GR00T 2 从当前观测和任务指令中采样一个动作计划。记 𝐴𝑟 为其已执行的 𝐻 个动作前缀，𝐶𝑟 为世界模型的条件潜变量。初始时，𝐶0 通过将五个已录制视频帧编码为两个潜变量帧得到。映射 𝑔 将动作转换为世界模型的动作坐标和归一化方式。未来潜变量及下一个条件历史由下式给出：[存疑：抽取结果中缺少该公式] [公式原文见 p.93]

<a id="S1700"></a>
**Source:** p.93 S1700

**Original:** Here, Tail2 retains the final two latent frames of the concatenated conditioning and predicted sequence. After decoding, we remove the overlapping conditioning prefix and append the newly predicted images to the policy’s visual history. The views and historical frames required by GR00T 2 form its next observation, closing the interaction loop.

**中文:** 这里，Tail2 保留拼接后的条件序列与预测序列中的最后两个潜变量帧。解码之后，我们去掉重叠的条件前缀，并将新预测的图像追加到策略的视觉历史中。GR00T 2 所需的视角和历史帧构成其下一步观测，从而闭合交互回路。

<a id="S1701"></a>
**Source:** p.93 S1701

**Original:** The rollout preserves the video-action alignment used during training. For YAM, the world model predicts twelve new video frames at 15 Hz for 24 native actions at 30 Hz. For DROID/RoboLab, it predicts sixteen frames for sixteen actions, both at 15 Hz. We query the policy again after executing this action prefix and truncate the final round at the task horizon.

**中文:** rollout 保持了训练时使用的视频-动作对齐方式。对于 YAM，世界模型以 15 Hz 预测 12 个新视频帧，对应 30 Hz 下的 24 个原生动作。对于 DROID/RoboLab，它预测 16 帧，对应 16 个动作，两者均以 15 Hz 运行。执行完该动作前缀后，我们会再次查询策略，并在任务时限处截断最后一轮。

<a id="S1702"></a>
**Source:** p.93 S1702

**Original:** We exclude the five-frame conditioning prefix from the images returned to the policy. RoboLab decodes the complete latent window at each round. YAM retains the causal decoder cache and decodes only new latents after the first round. This decoder cache is separate from the latent history passed to the world model. For policies requiring proprioception, we initialize the state input from the recorded reset state. At each later policy query, we use the last executed action target as an approximation of the current robot state.

**中文:** 返回给策略的图像不包含五帧条件前缀。RoboLab 在每一轮都解码完整的潜变量窗口。YAM 则保留因果解码器缓存，仅在第一轮之后解码新的潜变量。该解码器缓存与传入世界模型的潜变量历史是分开的。对于需要本体感知的策略，我们从已录制的重置状态初始化状态输入。在之后的每次策略查询中，我们使用上一次已执行的动作目标作为当前机器人状态的近似。

<a id="S1703"></a>
**Source:** p.94 S1703

**Original:** Long-Horizon Prediction. Policy learning requires multiple rounds of interaction, whereas the world model is trained on short video windows. We therefore generate successive segments autoregressively. After the first segment, the model conditions on its own predictions rather than recorded observations. Errors in this history can affect subsequent predictions and policy decisions.

**中文:** 长时序预测。策略学习需要多轮交互，而世界模型是在短视频窗口上训练的。因此，我们以自回归方式生成连续片段。在第一个片段之后，模型以自身的预测而非已录制的观测作为条件。该历史中的误差可能影响后续的预测和策略决策。

<a id="S1704"></a>
**Source:** p.94 S1704

**Original:** For the DROID-derived model used in RoboLab, we perturb recorded conditioning latents during training to expose the model to imperfect visual histories, while keeping recorded future latents as prediction targets. For a clean conditioning tensor 𝐶, we use

**中文:** 对于 RoboLab 所用的 DROID 衍生模型，我们在训练时扰动已录制的条件潜变量，使模型接触到不完美的视觉历史，同时保留已录制的未来潜变量作为预测目标。对于干净的条件张量 𝐶，我们采用下式：

<a id="E007"></a>
**Source:** p.94 E007

![E007](assets/equations/E007.png)

**Original:** 𝐶= (1 −𝜎)𝐶+ 𝜎𝜖, 𝜖∼𝒩(0, 𝐼). (20)

**中文:** 该式描述对条件张量加噪的方式：以噪声强度 𝜎 将 𝐶 与标准高斯噪声 𝜖 混合，式中原样保留为 $$𝐶= (1 −𝜎)𝐶+ 𝜎𝜖, 𝜖∼𝒩(0, 𝐼). (20)$$ [公式原文见 p.94] [存疑：左侧 𝐶 与右侧 𝐶 可能是不同符号，抽取未保留其区别]

<a id="S1705"></a>
**Source:** p.94 S1705

**Original:** The noise strength 𝜎is sampled from 0, 0.0245, 0.0480, and 0.0925 with probabilities 0.2, 0.2, 0.4, and 0.2, respectively. We also explored replacing recorded history with a model-generated preceding segment, with gradients stopped through that history. These preliminary trials showed no clear additional benefit over noise augmentation, which we retain in the final training recipe.

**中文:** 噪声强度 𝜎 从 0、0.0245、0.0480 和 0.0925 中采样，对应概率分别为 0.2、0.2、0.4 和 0.2。我们也尝试过用模型生成的前序片段替代已录制的历史，并让梯度在该历史处截断。这些初步试验表明，它相对于噪声增广（noise augmentation）并没有明显的额外收益，因此我们在最终训练配方中保留了噪声增广。

<a id="S1706"></a>
**Source:** p.94 S1706

**Original:** At rollout time, we pass the final two predicted latent frames to the next world-model segment as its conditioning history. This avoids decoding and re-encoding images to construct that history. We still decode predicted latents into images for GR00T 2: the world model carries its history in latent space, while the policy receives camera observations in pixel space.

**中文:** 在 rollout 时，我们将最后两个预测潜变量帧作为下一个世界模型片段的条件历史传入。这样就无需先解码再重新编码图像来构建该历史。不过，我们仍会将预测的潜变量解码为图像供 GR00T 2 使用：世界模型在潜空间中保存其历史，而策略则在像素空间中接收相机观测。

<a id="S1707"></a>
**Source:** p.94 S1707

**Original:** Experimental Setup. Starting from SFT, GRPO updates GR00T 2 through interaction with the learned environment, while the world model and learned success detector remain fixed. Native RoboLab evaluation and real-world execution test whether these updates improve behavior outside the learned environment.

**中文:** 实验设置。以 SFT 为起点，GRPO 通过与学习得到的环境交互来更新 GR00T 2，同时世界模型和学习得到的成功检测器保持固定。原生 RoboLab 评测与真实世界执行用于检验这些更新能否在学习得到的环境之外改善行为。

<a id="S1708"></a>
**Source:** p.94 S1708

**Original:** We collect rollouts from the initial GR00T 2 policy, retaining successful and failed attempts for world-model adaptation and reward supervision. The study covers ten RoboLab tasks and four families of physical manipulation: peg insertion, test-tube insertion into a specified rack hole, bun placement on yellow and white cups, and hardware sorting with nine instructions. Hardware sorting tests whether the policy selects the requested target object and destination from three target object categories and three colored trays in the presence of distractors. Fig. 52 illustrates the physical task setups.

**中文:** 我们从初始的 GR00T 2 策略采集 rollout，保留成功和失败的尝试，用于世界模型适配和奖励监督。该研究涵盖十个 RoboLab 任务，以及四类物理操作：插销插入（peg insertion）、将试管插入指定的试管架孔位、将小圆面包放置到黄色和白色杯子上，以及根据九条指令进行硬件分拣。硬件分拣用于检验策略在存在干扰物时，能否从三类目标物体和三个彩色托盘中选出所要求的目标物体与目的地。Fig. 52 展示了物理任务的设置。

<a id="S1709"></a>
**Source:** p.94 S1709

**Original:** World-model adaptation uses 300 physical rollouts for each insertion task and each of the two bun-placement tasks, and approximately 300 rollouts in total for hardware sorting. The insertion and hardware tasks share a jointly adapted world model, while a separate model is adapted for bun placement. For RoboLab, we adapt one shared world model using 450 training trajectories per task across 64 tasks, with 50 trajectories per task held out. Joint policy RL uses ten tasks from this collection. Each RL run starts from its SFT baseline and keeps the world model and reward model fixed. RoboLab reward supervision uses 450 training and 50 validation trajectories per task. The test-tube success detector uses a separate set of 600 training and 120 validation videos labeled for insertion and release in the designated rack hole.

**中文:** 世界模型适配使用的物理 rollout 数量为：每个插入任务以及两个小圆面包放置任务各 300 条，硬件分拣总计约 300 条。插入任务与硬件分拣任务共享一个联合适配的世界模型，而小圆面包放置则单独适配一个模型。对于 RoboLab，我们使用 64 个任务、每个任务 450 条训练轨迹适配一个共享的世界模型，并且每个任务另留出 50 条轨迹。联合策略 RL 使用该集合中的十个任务。每次 RL 运行都从其 SFT 基线开始，并保持世界模型和奖励模型固定。RoboLab 奖励监督使用每个任务 450 条训练轨迹和 50 条验证轨迹。试管成功检测器使用另外一组 600 段训练视频和 120 段验证视频，这些视频标注了在指定试管架孔位中的插入与释放。

<a id="S1710"></a>
**Source:** p.94 S1710

**Original:** Reward Modeling and Policy Optimization. Sparse rewards. Dense progress rewards are difficult to obtain consistently across manipulation tasks and expensive to annotate. They can also introduce reward hacking when a policy increases a proxy score without completing the requested goal. We therefore use sparse task-completion rewards, learning a binary success detector rather than a continuous progress score.

**中文:** 奖励建模与策略优化。稀疏奖励。稠密的进度奖励难以在各类操作任务中稳定获得，且标注成本高昂。当策略提升了代理分数却没有完成所要求的目标时，它们还可能引入奖励投机（reward hacking）。因此，我们采用稀疏的任务完成奖励，即学习一个二值成功检测器，而不是连续的进度分数。

<a id="S1711"></a>
**Source:** p.94 S1711

**Original:** We train compact success detectors based on VideoMAE (Tong et al., 2022) to provide rewards during RL. For physical videos, a vision-language model (VLM) proposes outcome labels and supporting visual evidence, and targeted human review resolves ambiguous cases. These offline labels supervise the compact detectors, avoiding VLM queries during policy learning. For hardware sorting only, annotated world-model rollouts augment the recorded videos to cover observations encountered in neural simulation. The other reward models use recorded task data.

**中文:** 我们基于 VideoMAE（Tong et al., 2022）训练紧凑的成功检测器，在 RL 过程中提供奖励。对于物理视频，视觉语言模型（VLM）提出结果标签及支撑性的视觉证据，有针对性的人工复核则解决有歧义的情况。这些离线标签用于监督紧凑检测器，从而避免在策略学习过程中调用 VLM。仅针对硬件分拣，已标注的世界模型 rollout 会对已录制的视频进行增广，以覆盖神经仿真中遇到的观测。其他奖励模型使用已录制的任务数据。

<a id="S1712"></a>
**Source:** p.94 S1712

**Original:** Success is defined by the requested instruction: choosing the wrong object or destination is a negative outcome.

**中文:** 成功由所请求的指令定义：选错物体或目的地属于负面结果。

<a id="S1713"></a>
**Source:** p.95 S1713

**Original:** We use task-specific detectors, including instruction-specific outputs for joint hardware sorting. RoboLab provides native success labels, while physical-task labels use recorded outcomes and reviewed visual evidence. The detector and its task-specific decision rule remain fixed during RL. Final policy evaluation uses native RoboLab outcomes and physical execution, independently of the learned reward model.

**中文:** 我们使用面向具体任务的检测器，其中包括用于联合硬件分拣的指令特定输出。RoboLab 提供原生成功标签，物理任务的标签则使用已录制的结果及经复核的视觉证据。在 RL 过程中，检测器及其面向具体任务的判定规则保持固定。最终的策略评测使用 RoboLab 原生结果和物理执行结果，且与学习得到的奖励模型相互独立。

<a id="S1714"></a>
**Source:** p.95 S1714

**Original:** Policy optimization. We apply the clipped transition-level policy optimization principle of Sec. F.1.1 to interaction with a fixed learned environment. We collect groups of attempts from the same recorded reset context and score them with the learned success detector. The neural-simulation experiments use Flow-SDE (Liu et al., 2025) for stochastic action denoising, while the physical-RL recipe uses CPS. Both provide tractable transition densities for likelihood-ratio updates.

**中文:** 策略优化。我们将 Sec. F.1.1 中的截断式转移级策略优化原则，应用于与固定学习环境的交互。我们从同一条已录制的重置上下文中采集多组尝试，并用学习得到的成功检测器对其打分。神经仿真实验使用 Flow-SDE（Liu et al., 2025）进行随机动作去噪，而物理 RL 配方使用保系数采样（CPS）。两者都为似然比更新提供了可计算的转移密度。

<a id="S1715"></a>
**Source:** p.95 S1715

**Original:** We optimize a clipped likelihood-ratio objective on selected action-denoising transitions. For each selected transition, we store the sampled latent input and output, denoising index, conditioning inputs, and behaviorpolicy probability. During optimization, we replay the same transition and recompute its probability under the current parameters with gradients enabled. The sampled transition and noise schedule remain fixed, so the likelihood ratio compares the two policies on the same sampled event.

**中文:** 我们在选定的动作去噪转移上优化一个截断似然比目标。对于每个选定的转移，我们存储采样得到的潜变量输入与输出、去噪索引、条件输入以及行为策略概率。在优化过程中，我们重放同一转移，并在开启梯度的情况下，用当前参数重新计算其概率。采样得到的转移与噪声调度保持固定，因此似然比是在同一个采样事件上比较两个策略。

<a id="S1716"></a>
**Source:** p.95 S1716

**Original:** Consistent replay is necessary because numerical differences can produce an apparent policy change before any update. We disable dropout, preserve positional-encoding precision, and check rollout and replay logprobabilities under unchanged weights before the first optimizer update. Activation checkpointing reduces memory use during backpropagation through the joint world-action model described in Sec. F.1.1. The likelihood ratio scores the selected action transition, with no separate video-likelihood objective or learned critic. In the physical-task recipe, we compute the actor loss using actions up to and including the first chunk in which success is confirmed. Later actions are excluded.

**中文:** 保持重放一致是必要的，因为数值差异可能在任何更新之前就产生看似存在的策略变化。我们关闭随机丢弃（dropout），保留位置编码的精度，并在第一次优化器更新之前，在权重不变的情况下检查 rollout 与重放的对数概率。激活值检查点（activation checkpointing）降低了在 Sec. F.1.1 中所述的联合世界-动作模型上进行反向传播时的内存占用。似然比只对所选的动作转移进行评分，不使用单独的视频似然目标，也不使用学习得到的评论者（critic）。在物理任务配方中，我们使用直到并包含首个确认成功的动作块为止的动作来计算 actor 损失，之后的动作则被排除在外。

<a id="S1717"></a>
**Source:** p.95 S1717

**Original:** Policy Improvement in RoboLab. We evaluate task success using native RoboLab outcomes, independently of the learned world model and reward model. Fig. 50 compares the SFT policy with the policy obtained by joint RL from that initialization. Each policy is evaluated for 500 episodes per task, or 5,000 episodes in total, using matched observation and action settings and full task horizons. Mean success increases from 51.32% to 70.88%, a gain of 19.56 percentage points.

**中文:** RoboLab 中的策略改进。我们使用 RoboLab 原生结果评估任务成功情况，且与学习得到的世界模型和奖励模型相互独立。Fig. 50 比较了 SFT 策略与从同一初始化出发经联合 RL 得到的策略。每个策略在每个任务上评估 500 个回合，总计 5,000 个回合，观测与动作设置一致，并使用完整的任务时限。平均成功率从 51.32% 提高到 70.88%，提升 19.56 个百分点。

<a id="S1718"></a>
**Source:** p.95 S1718

**Original:** Batch and group size. Sparse rewards connect exploration to optimization: a larger group can reveal a return difference that a smaller group misses. In RoboLab, we compare (𝐵, 𝐺) = (512, 8) and (1536, 24), where 𝐵is the number of trajectories collected per round and 𝐺the number of attempts per reset group. Both recipes collect 64 groups and perform four optimizer updates per round.

**中文:** 批量与分组大小。稀疏奖励将探索与优化联系在一起：较大的分组可能揭示较小分组会遗漏的回报差异。在 RoboLab 中，我们比较了 (𝐵, 𝐺) = (512, 8) 与 (1536, 24)，其中 𝐵 为每轮采集的轨迹数，𝐺 为每个重置分组中的尝试次数。两种配方都采集 64 个分组，并在每轮执行四次优化器更新。


<a id="S1719"></a>
**Source:** p.95 S1719

**Original:** [英文原文未复制，见 PDF p.95 · S1719]

**中文:** 图 51(a) 展示了 DreamDojo 中的 rollout（轨迹采样）成功率与原生 RoboLab 成功率，覆盖十二个策略检查点（包括 SFT）。在每个策略 100 个回合的评测中，原生 RoboLab 成功率达到 71%。单独的最终评测每个策略使用 5,000 个回合，成功率从 51.32% 提升到 70.88%。DreamDojo 的成功率由学习到的奖励在训练 rollout 上测得，而 RoboLab 的评测使用原生任务结果。由于采样流程和时间范围不同，这些曲线只能反映各自设定内的学习进程，不能用来衡量仿真器的校准程度。

<a id="S1720"></a>
**Source:** p.95 S1720

**Original:** [英文原文未复制，见 PDF p.95 · S1720]

**中文:** 图 51(b) 比较了十一个匹配的数据采集预算下、共计 67,584 条轨迹的结果。较大的组合批次/分组配置在十个预算点上原生 RoboLab 成功率更高，在十一个预算上的平均成功率高出 11.1 个百分点。在最终预算下，成功率为 71% 对 54%，相差 17 个百分点。在 24,576 条轨迹时，两者分别为 68% 和 47%。

<a id="S1721"></a>
**Source:** p.95 S1721

**Original:** [英文原文未复制，见 PDF p.95 · S1721]

**中文:** 这些单次运行的结果有利于较大的组合配方。两者在优化过程和重置布局上也有差异：在最终预算下，较小配方进行了 528 次优化器更新，较大配方进行了 176 次。较小配方后期的延续训练还去掉了一个数值上的对数比下界。这些差异使得无法把结果归因于任一规模参数，而且每种配置只运行一次，也无法说明结果在独立运行之间是否稳定。

<a id="S1722"></a>
**Source:** p.95 S1722

**Original:** [英文原文未复制，见 PDF p.95 · S1722]

**中文:** 真实任务上的策略改进。我们在以下任务上部署固定策略：插销、将试管插入指定试管架孔位、把面包放到黄杯和白杯上，以及九条指令的硬件分拣。对于

<a id="C068"></a>
**Source:** p.96 C068 · 图 F050

![F050](assets/F050.png)

**Original (caption):** [英文图注未复制，见 PDF p.96 · C068]

**中文图注：** 图 50：在十个 RoboLab 任务上的联合 RL。在 DreamDojo 中训练 GR00T 2 后，任务平均成功率从 51.32% 提升到 70.88%，每个任务和策略各评估 500 个回合。误差条表示 95% Wilson 置信区间。

<a id="C069"></a>
**Source:** p.96 C069 · 图 F051

![F051](assets/F051.png)

**Original (caption):** [英文图注未复制，见 PDF p.96 · C069]

**中文图注：** 图 51：通过神经仿真进行的策略改进。(a) RL 过程中 DreamDojo 的 rollout 成功率与原生 RoboLab 成功率。(b) 两种批次/分组配置在匹配数据采集预算下的原生 RoboLab 成功率，分别达到 71% 和 54%。每种配置各有一次训练运行。批次和分组大小同时变化。

<a id="S1781"></a>
**Source:** p.96 S1781

**Original:** [英文原文未复制，见 PDF p.96 · S1781]

**中文:** 插入类任务中，成功需要插入指定孔位并随后释放。对于面包放置，面包必须被释放到指定的杯子上。对于硬件分拣，目标物体必须被释放到指定的托盘中。结果以操作员记录为准，并在有的情况下采用经核对的人工复核标签。每个 RL 策略都与其 SFT 初始化进行比较。只有在确认使用相同参考场景时，硬件分拣的试次才会被纳入。

<a id="S1782"></a>
**Source:** p.96 S1782

**Original:** [英文原文未复制，见 PDF p.96 · S1782]

**中文:** 图 52 比较了四个真实任务，每个策略和任务各 60 次试次。插销从 43.3% 提升到 81.7%，插入指定试管架孔位从 51.7% 提升到 73.3%。面包放置在黄杯上从 63.3% 提升到 76.7%，在白杯上从 11.7% 提升到 55.0%。四个任务等权平均的

<a id="C070"></a>
**Source:** p.97 C070 · 图 F052

![F052](assets/F052.png)

**Original (caption):** [英文图注未复制，见 PDF p.97 · C070]

**中文图注：** 图 52：基于 DreamDojo 的真实世界策略改进。上排：双腿插销、将试管插入第五个试管架孔位、把面包放到黄杯和白杯上，以及硬件分拣。下排：RL 前后的任务成功率；九条硬件分拣指令由同一个 GR00T 2 策略联合训练。误差条表示 95% Wilson 置信区间。

<a id="S1829"></a>
**Source:** p.97 S1829

**Original:** [英文原文未复制，见 PDF p.97 · S1829]

**中文:** 平均成功率从 42.5% 提升到 71.7%，增益为 29.2 个百分点。

<a id="S1830"></a>
**Source:** p.97 S1830

**Original:** [英文原文未复制，见 PDF p.97 · S1830]

**中文:** 对于硬件分拣，一个 GR00T 2 策略在九条指令上与 RL 联合训练。这九条指令由三个目标物体（黑色管、齿轮铰链和黄铜接头）与三个目标托盘两两配对组成（图 52）。九条指令的成功率等权平均后，成功率从 51.2% 提升到 70.4%，增益为 19.2 个百分点。

<a id="S1831"></a>
**Source:** p.97 S1831

**Original:** [英文原文未复制，见 PDF p.97 · S1831]

**中文:** 每条硬件指令有 70 或 71 次 SFT 试次和 24 次 RL 试次。RL 样本包括四次检查点选择试次，以及每条指令之后的 20 次重复评估试次。SFT 与 RL 在同一参考场景下、分别于不同批次中采集。

<a id="S1832"></a>
**Source:** p.97 S1832

**Original:** [英文原文未复制，见 PDF p.97 · S1832]

**中文:** 讨论。这些结果表明，利用由世界模型产生的经验可以改进策略，而该世界模型已根据初始策略的 rollout 做过适配。GR00T 2 在此环境中学习，并在 RoboLab 以及真实机器人上接受评估。当前流程仍需要收集任务 rollout，并进行任务特定的世界模型适配。跨新任务复用已学习的环境，以及重复完整的世界模型与策略改进循环，仍是未来工作的方向。

<a id="S1833"></a>
**Source:** p.97 S1833

**Original:** [英文原文未复制，见 PDF p.97 · S1833]

**中文:** 我们的实验聚焦于单项操作技能，这些技能是更复杂机器人行为的组成单元。这些技能可以整合进智能体式执行（第 G.1 节），由高层编排、进度监测和恢复机制协调跨更长任务时序的动作。因此，基于 RL 的适配与智能体式执行提供了互补的机制，共同提升机器人的可靠性，覆盖从精细的物理交互到长时序任务完成的范围。

<a id="S1834"></a>
**Source:** p.97 S1834

**Original:** [英文原文未复制，见 PDF p.97 · S1834]

**中文:** 我们更长远的目标是开发可扩展的后训练方法，使世界-动作模型能够通过真实世界经验持续改进，并把能力扩展到日益困难的操作任务。

<a id="H54"></a>
### G. Agentic GR00T 2 ｜ 智能体化 GR00T 2

<a id="S1835"></a>
**Source:** p.98 S1835

**Original:** [英文原文未复制，见 PDF p.98 · S1835]

**中文:** 预训练和后训练为 GR00T 2 提供了越来越强的操作技能，但稳健的长时序执行需要的不只是一个强大的底层策略。复杂任务包含多个阶段、任务层面的决策以及意外故障，仅靠连续的策略执行很难解决这些问题。语言指令也可能让任务意图的重要方面没有说清，例如要操作哪个物体，或者应该把它放到哪里。

<a id="S1836"></a>
**Source:** p.98 S1836

**Original:** [英文原文未复制，见 PDF p.98 · S1836]

**中文:** 我们探索了两种互补的智能体化操作方法。第一，智能体式技能组合与恢复将 GR00T 2 与 CaP 集成，使高层智能体能够组合操作技能、监测执行并从意外故障中恢复（第 G.1 节）。第二，可引导的世界-动作生成通过 WAM API 暴露 GR00T 2 习得的能力，使智能体能够利用视觉目标引导并组合机器人行为（第 G.2 节）。两者结合，使高层推理智能体能够借助 GR00T 2 完成复杂的长时序操作。

<a id="H55"></a>
### G.1. Agentic Skill Composition and Recovery with Code-as-Policy ｜ 基于代码即策略的智能体式技能组合与恢复

<a id="S1837"></a>
**Source:** p.98 S1837

**Original:** [英文原文未复制，见 PDF p.98 · S1837]

**中文:** 即便经过后训练，长时序操作仍容易受到误差累积和未预见状态的影响（Ross et al., 2011）。我们提出一种智能体式执行框架，其中一个前沿多模态编码智能体担任系统 2（S2），组合 GR00T 2 与 CaP 工具，同时监测任务进度并从故障中恢复。智能体在恢复执行前会先核实每次干预，因此无需让 GR00T 2 学会每一种突发情况。

<a id="S1838"></a>
**Source:** p.98 S1838

**Original:** [英文原文未复制，见 PDF p.98 · S1838]

**中文:** 同一框架支持互补的执行策略。在仿真中，我们使用 ASPIRE（Lu et al., 2026）发现把 GR00T 2 当作操作工具调用的任务级程序；每个任务要么运行其程序，要么以 GR00T 2 单独作为默认执行器，取两者中在开发种子上成功次数更多的一个。在真实机器人上，由于 GR00T 2 已能处理大多数操作，它仍作为默认控制器。两种情况下，S2 都提供监测以及基于 CaP 的恢复。关键区别在于两次干预之间由谁执行。

<a id="S1839"></a>
**Source:** p.98 S1839

**Original:** [英文原文未复制，见 PDF p.98 · S1839]

**中文:** 智能体运行时架构。运行时通过模型上下文协议（MCP）暴露 GR00T 2 执行、机器人观测以及 CaP 原语。S2 以“观测-推理-行动-验证”循环使用这些工具（图 6）。

<a id="S1840"></a>
**Source:** p.98 S1840

**Original:** [英文原文未复制，见 PDF p.98 · S1840]

**中文:** wam_act 工具以任务提示执行 GR00T 2，并返回执行反馈。智能体可以通过专用观测工具访问相机观测和机器人状态，必要时还可以在执行过程中调整 GR00T 2 的语言提示。当恢复动作需要接管控制时，stop_wam 工具会终止 GR00T 2 的执行。CaP 动作原语通过逆运动学和运动规划下发末端执行器与夹爪指令，而观测原语则借助视觉基础模型获取物体定位和位姿估计等信息。CaP 程序将这些原语组合成可执行的技能，无需重新训练 GR00T 2 即可在测试时添加。单一控制工作进程负责协调执行，使 GR00T 2 与 CaP 不会同时下发相互冲突的机器人指令。

<a id="S1841"></a>
**Source:** p.98 S1841

**Original:** [英文原文未复制，见 PDF p.98 · S1841]

**中文:** 智能体会收到操作指南（AGENTS.md）、技能文档以及任务上下文，其中描述了各阶段、成功标准和已知的失效模式。它会检查观测和工具反馈，看是否存在进度停滞或错误，并在需要时调用恢复动作。恢复可能包括重新抓取掉落的零件、调整部件朝向，或在恢复执行前把机器人带回有效构型。

<a id="S1842"></a>
**Source:** p.98 S1842

**Original:** [英文原文未复制，见 PDF p.98 · S1842]

**中文:** 程序与技能获取。ASPIRE 学习与 GR00T 2 配合使用的可执行行为，但在不同场景下范围有所不同。在仿真中，它发现任务级 CaP 程序，把 GR00T 2 的调用与感知、几何推理和操作原语组合起来。在线执行期间，S2 可能会复用或改写这些程序中的代码用于恢复。在真实机器人上，ASPIRE 则获取有针对性的 CaP 技能，途径可以是直接的机器人交互，也可以是 CaP 仿真到现实的迁移，即在仿真中学习技能并将其适配到真实条件（第 J.2.4 节）。

<a id="C071"></a>
**Source:** p.99 C071 · 表 T019

![T019](assets/T019.png)

**Original (caption):** [英文表注未复制，见 PDF p.99 · C071]

**中文表注：** 表 19：与 RoboCasa365 和 RoboDojo 排行榜前七名（包括智能体提交）的比较。我们报告总体及各类别的成功率（%）。RoboDojo 平均值为五个能力维度上的官方均值。排行榜数据截至 2026 年 11 月 6 日。我们的 RoboDojo 结果使用布局库 0，因此 GR00T 2 SFT 行与同一基准在表 31 中的官方三库评测（平均成功率 35.5%）略有不同。在智能体行中，每个任务的默认执行器在同一基准的开发种子上选定，与测试种子不相交。最佳和次佳结果分别以粗体和下划线标出。

<a id="S1845"></a>
**Source:** p.99 S1845

**Original:** [英文原文未复制，见 PDF p.99 · S1845]

**中文:** 表 19 数据行（数值顺序与原表一致，列名见原表）：HexaShell 1.5，Agent，85.6 / 91.1 / 85.0 / 80.0；Awomo-0.5I（Awomo-WAM Team, 2026），WAM，64.4 / 86.5 / 58.8 / 45.2；minionx，VLA，62.6 / 81.8 / 60.0 / 43.6；Awomo-0.5V（Awomo-WAM Team, 2026），WAM，62.5 / 85.0 / 60.4 / 39.4；Axiom-0（Shu et al., 2026），VLA，61.6 / 86.5 / 59.4 / 35.8；Paimon-0，VLA，58.1 / 79.3 / 55.8 / 36.7；Xiaomi-Robotics-1，VLA，57.4 / 80.2 / 57.1 / 32.1。

<a id="S1846"></a>
**Source:** p.99 S1846

**Original:** [英文原文未复制，见 PDF p.99 · S1846]

**中文:** 表 19 数据行（本文结果）：GR00T 2 - SFT（Ours），WAM，67.2 / 87.4 / 73.6 / 38.2；GR00T 2 - SFT + RL（Ours），WAM，72.4 / 92.5 / 81.5 / 40.6；GR00T 2 - SFT + Agent（Ours），Agent + WAM，81.8 / 88.2 / 86.9 / 69.5；GR00T 2 - SFT + RL + Agent（Ours），Agent + WAM，88.0 / 95.6 / 92.0 / 75.5。

<a id="S1849"></a>
**Source:** p.99 S1849

**Original:** [英文原文未复制，见 PDF p.99 · S1849]

**中文:** 表 19 数据行（RoboDojo 排行榜，数值顺序与原表一致）：Q0-Preview，Agent，68.9 / 58.7 / 58.5 / 58.5 / 93.7 / 75.0；GO-3 Nano Preview，Agent + WAM，56.4 / 33.7 / 76.0 / 53.5 / 63.7 / 55.3；PyRUA-Lean，Agent，50.4 / 43.2 / 38.3 / 43.8 / 68.3 / 58.3；HexaShell-Preview，Agent，46.9 / 34.5 / 32.0 / 31.5 / 81.0 / 55.3；WorldScape-R2SI，Agent + WAM，39.4 / 35.8 / 15.5 / 34.3 / 63.7 / 47.5；EmbodiedEvo，Agent，39.0 / 30.8 / 16.3 / 21.8 / 76.7 / 49.3；WALL-OSS-1.0-lite，VLA，35.0 / 37.9 / 29.1 / 32.3 / 56.0 / 19.6。

<a id="S1850"></a>
**Source:** p.99 S1850

**Original:** [英文原文未复制，见 PDF p.99 · S1850]

**中文:** 表 19 数据行（本文结果，RoboDojo 布局库 0）：GR00T 2 - SFT（Ours），WAM，35.2 / 40.0 / 40.5 / 53.8 / 36.0 / 5.8；GR00T 2 - SFT + RL（Ours），WAM，40.8 / 45.0 / 53.7 / 55.0 / 39.3 / 11.0；GR00T 2 - SFT + Agent（Ours），Agent + WAM，72.3 / 64.0 / 62.5 / 62.3 / 93.7 / 79.2；GR00T 2 - SFT + RL + Agent（Ours），Agent + WAM，75.8 / 67.7 / 68.8 / 68.0 / 95.0 / 79.5。

<a id="S1851"></a>
**Source:** p.99 S1851

**Original:** [英文原文未复制，见 PDF p.99 · S1851]

**中文:** 仿真评测。我们在 RoboCasa365（Nasiriany et al., 2026）和 RoboDojo（Chen et al., 2026a）上使用四种配置进行评测：SFT、SFT + RL、SFT + Agent 和 SFT + RL + Agent。对于智能体式执行，ASPIRE 使用每个任务 15 个开发种子发现程序。在包括这 15 个在内的 30 个开发种子上，我们随后分别运行每个任务的程序和单独的 GR00T 2，并将成功次数更多的一方设为该任务的默认执行器，平局时保留程序。使用 SFT 检查点时，这一规则在 RoboCasa365 的 50 个任务中选中 GR00T 2 的有 23 个，在 RoboDojo 的 54 个任务配置中有 12 个。S2 在每个回合开始时使用默认执行器，对其进行监测，并在需要时调用在线 CaP 恢复。我们在两个基准上各使用每个任务 50 个留出种子进行测试（RoboDojo 泛化任务的标准版本与随机化版本各 25 个），这些种子与开发种子不相交。

<a id="S1852"></a>
**Source:** p.99 S1852

**Original:** [英文原文未复制，见 PDF p.99 · S1852]

**中文:** 仅使用 SFT 时，GR00T 2 在 RoboCasa365 和 RoboDojo 排行榜上取得了所有非智能体策略中最高的成功率（第 J.3 节和表 19）。基于记忆和推理的任务以及高精度操作仍有提升空间。

<a id="S1853"></a>
**Source:** p.100 S1853

**Original:** [英文原文未复制，见 PDF p.100 · S1853]

**中文:** 借助 AutoRL 进行的 RL 后训练（第 F.2 节）主要提升精度：RoboDojo 精度任务（Precision）的成功率从 40.5% 提高到 53.7%；RoboCasa365 上的平均成功率从 67.2% 提高到 72.4%，RoboDojo 布局库 0 上从 35.2% 提高到 40.8%（表 19）。智能体式执行对以记忆和推理为主的任务帮助最大：ASPIRE 程序与 S2 将 RoboCasa365 Composite-Unseen 任务的成功率从 38.2% 提升到 69.5%，把 RoboDojo 记忆类任务从 36.0% 提升到 93.7%。总体而言，它使 RoboCasa365 的平均成功率达到 81.8%，RoboDojo 达到 72.3%；与 RL 结合后，两个基准上都取得了最佳结果。与两个公开排行榜前列（包括智能体提交）相比，SFT + RL + Agent 在 RoboCasa365 上排名第一（88.0% 对比 HexaShell 1.5 的 85.6%），在 RoboDojo 上也排名第一（我们仅评测布局库 0，75.8% 对比 Q0-Preview 的 68.9%）（表 19）。

<a id="C072"></a>
**Source:** p.100 C072 · 表 T020

![T020](assets/T020.png)

**Original (caption):** [英文表注未复制，见 PDF p.100 · C072]

**中文表注：** 表 20：按 S2 是否干预划分的回合结果（SFT + Agent）。每个单元格给出回合数及其中成功的数量，统计对象为 SFT + Agent 运行的全部回合（RoboDojo 为 2,093 个，RoboCasa365 为 2,500 个）。

<a id="S1856"></a>
**Source:** p.100 S1856

**Original:** [英文原文未复制，见 PDF p.100 · S1856]

**中文:** 为刻画 SFT + Agent 设定下的在线恢复，我们按 S2 是否干预对回合进行划分（表 20）。S2 很少放过失败：在它未干预的回合中，RoboDojo 上 1,320 个中只有 29 个失败，RoboCasa365 上 1,512 个中有 20 个失败。在它干预的回合中，RoboDojo 的成功率为 24%（773 个中的 188 个），RoboCasa365 为 56%（988 个中的 553 个）。图 53 展示了一次成功挽救和一次失败的恢复。

<a id="S1857"></a>
**Source:** p.100 S1857

**Original:** [英文原文未复制，见 PDF p.100 · S1857]

**中文:** 我们对两个基准上失败的 SFT + Agent 回合进行了人工复核（图 54），结果显示大部分失败落入两类：一类是恢复所需的操作精度超出了 S2 借助运动规划工具所能达到的水平（RoboCasa365 上占 38%，RoboDojo 上占 39%）；另一类是回合进入了无法再恢复的状态，例如物体掉到地上或剩余时间太少（分别为 24% 和 38%）。其余大多数失败看起来已经完成，但未满足基准的成功判定。

<a id="S1859"></a>
**Source:** p.100 S1859

**Original:** [英文原文未复制，见 PDF p.100 · S1859]

**中文:** 真实世界长时序操作。我们以 GR00T 2 作为默认控制器评测智能体式执行，考察多阶段装配和重复精密插入任务，并观察 CaP 恢复如何与策略后训练互补。

<a id="S1860"></a>
**Source:** p.100 S1860

**Original:** [英文原文未复制，见 PDF p.100 · S1860]

**中文:** 多阶段装配。我们考虑玩具飞机、玩具拖拉机和 Hot Wheels 玩具车的装配（图 55）。为了检验鲁棒性，每个回合开始时都会把零件倒在桌面上，形成杂乱的场景和多样的物体位姿。机器人必须按顺序装配零件，使用玩具电钻，并从执行错误中恢复。我们比较了 SFT、SFT + DAgger（Ross et al., 2011）以及 SFT + DAgger + Agent。

<a id="S1861"></a>
**Source:** p.100 S1861

**Original:** [英文原文未复制，见 PDF p.100 · S1861]

**中文:** 玩具飞机任务需要用玩具电钻装配机身、两只机翼和两颗螺丝。它要求先装上并固定下机翼，然后把飞机翻转过来，再固定上机翼，过程中需要双臂交接并精确对齐螺丝孔。成功要求两只机翼都已固定，且电钻被放回原位。玩具拖拉机任务需要安装并固定两个小前轮和两个大后轮，在两侧之间翻转车身，最后将其扶正。Hot Wheels 任务需要安装正确的前后轮，并装上朝向正确的引擎盖，用电钻固定各部件。

<a id="S1862"></a>
**Source:** p.100 S1862

**Original:** [英文原文未复制，见 PDF p.100 · S1862]

**中文:** 图 7a 给出了结果。DAgger 把玩具飞机装配、玩具拖拉机装配和 Hot Wheels 装配的成功率分别从 69%、51% 和 23% 提升到 84%、71% 和 78%。加入智能体式执行后，成功率进一步提升到 98%、97% 和 97%。这一提升来自 S2 检测并修复局部执行失败的能力，同时保留了 GR00T 2 习得的操作能力。由于每次试次都从随机倒入的零件开始，这些成功率衡量的是对未见初始构型的鲁棒性，与后训练基准（表 1a）并不直接可比，因为后者的试次从整齐排列的布局开始。以 Hot Wheels 装配为例，基准在固定布局下报告的成功率为 85%。

<a id="S1863"></a>
**Source:** p.100 S1863

**Original:** [英文原文未复制，见 PDF p.100 · S1863]

**中文:** 重复精密插入。我们使用其中的精密技能，连续测试五次线缆和充电器插入，

<a id="C073"></a>
**Source:** p.101 C073 · 图 F053

![F053](assets/F053.png)

**Original (caption):** [英文图注未复制，见 PDF p.101 · C073]

**中文图注：** 图 53：RoboCasa365 上的在线恢复（SFT + Agent）。两个回合的关键帧。每一行下方的条形表示该回合中由谁控制机器人。(A) ASPIRE 程序抓取了烤箱把手而非抽屉把手。S2 将其停止，并用 CaP 抓取抽屉把手，抽屉随之打开。(B) 程序把吐司从烤面包机中拉出，但吐司平放落在了顶部。S2 停止程序，其对平放吐司的 CaP 抓取失败，交还给 GR00T 2 时已超时。

<a id="S1864"></a>
**Source:** p.101 S1864

**Original:** [英文原文未复制，见 PDF p.101 · S1864]

**中文:** 参见第 F.4 节，在同一智能体系统内比较 SFT 与经过 RL 后训练的 GR00T 2（图 55）。


<a id="S1865"></a>
**Source:** p.101 S1865

**Original:** For multi-cable insertion, five Ethernet (RJ45) cables stand upright beside a network switch. The robot must connect them in a fixed order to five designated ports. CaP first localizes all twelve candidate port faces using SAM 3 (Carion et al., 2025) and camera depth, then grasps each connector and transports it along a collision-free path to a pre-insertion pose. GR00T 2 performs the insertion, and S2 checks for an Ethernet link and verifies that the connector occupies the assigned port. If insertion stalls or exceeds 60 s, CaP retracts the connector and prepares another attempt, allowing up to three attempts per port. S2 can stop retries early if the connector has rotated in the gripper. The episode succeeds only if all five connectors are inserted, a setting that compounds insertion errors and introduces occlusion from previously inserted cables.

**中文:** 在多线缆插接任务中，五根以太网（RJ45）线缆竖立在网络交换机旁边。机器人必须按固定顺序，把它们分别接入五个指定端口。代码即策略（code-as-policy, CaP）首先利用 SAM 3（Carion et al., 2025）和相机深度信息，定位全部十二个候选端口面；随后抓取每根接头，并沿无碰撞路径将其运送至插接前位姿。GR00T 2 执行插接，系统 2（S2）检查是否建立了以太网链路，并核实接头是否位于分配的端口。若插接停滞或超过 60 s，CaP 会收回接头并准备再次尝试，每个端口最多允许三次尝试。若接头在夹爪中发生了旋转，S2 可以提前停止重试。只有五根接头全部插接成功，该回合才算成功；这一设定会累积插接误差，并且已插好的线缆会造成遮挡。

<a id="S1866"></a>
**Source:** p.101 S1866

**Original:** For multi-charger insertion, a human specifies five target outlets by pointing to them in order among twelve visually identical outlets arranged as a 2 × 6 grid. S2 grounds the gestures to individual outlets, with SAM 3 providing an independent interpretation. CaP grasps and transports each charger from its holder to the selected pre-insertion pose, and GR00T 2 performs the insertion. S2 checks whether the corresponding letter of an illuminated sign turns on and verifies the final target. Stalled or timed-out attempts can trigger CaP recovery, with at most three attempts per outlet and a 90 s limit per attempt. The task requires both accurate grounding of nonverbal instructions and precise insertion as the scene grows more cluttered.

**中文:** 在多充电器插接任务中，由人类依次指向排成 2 × 6 网格的十二个外观完全相同的插座，从中指定五个目标插座。S2 将手势指代定位（grounding）到各个插座，同时 SAM 3 提供一种独立的解读作为对照。CaP 将每个充电器从其支架抓取并运送到所选的插接前位姿，GR00T 2 执行插接。S2 检查发光标牌上对应的字母是否亮起，并核实最终目标。停滞或超时的尝试可以触发 CaP 恢复，每个插座最多三次尝试，每次尝试限时 90 s。随着场景愈发杂乱，该任务既要求准确理解非语言指令，也要求精确插接。

<a id="S1867"></a>
**Source:** p.101 S1867

**Original:** Fig. 7b shows that RL post-training improves long-horizon insertion reliability within the same agentic system. For multi-cable insertion, success rises from 12/20 to 19/20, and for multi-charger insertion, it rises from 2/20 to 20/20. The gains highlight the value of RL-trained precision skills within long-horizon agentic execution.

**中文:** 图 7b 表明，在同一智能体化系统内，RL 后训练提升了长时序插接的可靠性。多线缆插接的成功率从 12/20 升至 19/20，多充电器插接则从 2/20 升至 20/20。这些提升凸显了经 RL 训练的精确技能在长时序智能体化执行中的价值。

<a id="S1868"></a>
**Source:** p.101 S1868

**Original:** Failure Analysis. Of the 300 SFT + DAgger + Agent assembly episodes, eight fail in three categories. Incomplete fastening accounts for three failures (two airplane, one Hot Wheels): a screw remains partially driven, but both

**中文:** 失败分析。在 300 个 SFT + DAgger + Agent 装配回合中，有八次失败，分为三类。紧固不完整造成三次失败（两次为飞机，一次为 Hot Wheels）：螺丝仍有一部分未拧到位，但两者 [存疑：原文在此截断，句子未完]

<a id="C074"></a>
**Source:** p.102 C074 · 图 F054

![F054](assets/F054.png)

**Original (caption):** Figure 54: Why SFT + Agent episodes fail. Primary cause of manually reviewed failed SFT + Agent episodes: 87 on RoboCasa365 and 80 on RoboDojo.

**中文图注：** 图 54：SFT + Agent 回合失败的原因。人工复核的失败 SFT + Agent 回合的主要原因：RoboCasa365 上 87 次，RoboDojo 上 80 次。

<a id="S1884"></a>
**Source:** p.102 S1884

**Original:** GR00T 2 and S2 judge the step complete because the visual difference is subtle. Late intervention accounts for three failures (one tractor, two Hot Wheels): GR00T 2 mounts a small wheel on an incorrect rear hub before S2 stops it, and the available CaP skills cannot reliably reverse the operation. Physical limitations account for two tractor failures: one screw falls off the table, while another becomes mechanically jammed. Both of these episodes can be completed after brief human intervention, but are counted as failures under the autonomous evaluation protocol.

**中文:** GR00T 2 和 S2 判定该步骤已完成，因为视觉差异很细微。较晚干预造成三次失败（一次为拖拉机，两次为 Hot Wheels）：GR00T 2 在 S2 叫停之前，把一个小轮子装到了错误的后轮轮毂上，而现有的 CaP 技能无法可靠地撤销该操作。物理限制造成两次拖拉机失败：一颗螺丝从桌上掉落，另一颗则机械卡死。这两个回合在人工简短干预后都可以完成，但按照自主评测协议仍计为失败。

<a id="S1885"></a>
**Source:** p.102 S1885

**Original:** On repeated insertion, SFT + RL + Agent fails in only one of the 40 evaluated episodes, due to a timeout during multi-cable insertion. SAM 3 yields an imprecise connector grasp, leading to an offset pre-insertion pose. Although the RL-trained policy moves toward the port, alignment recovery requires small exploratory motions while maintaining forward pressure and supporting the connector against gravity, and the attempt exceeds the 60 s limit. This case illustrates how residual pose errors can still make recovery too slow under a fixed execution budget.

**中文:** 在重复插接中，SFT + RL + Agent 在 40 个评测回合中仅失败一次，原因是多线缆插接超时。SAM 3 给出的接头抓取不精确，导致插接前位姿发生偏移。尽管经 RL 训练的策略会朝端口移动，但对齐恢复需要小幅探索性运动，同时保持向前的压力并托住接头以抵抗重力，这次尝试超过了 60 s 的时限。该案例说明，即便残余位姿误差不大，在固定执行预算下恢复也可能过慢。

<a id="S1886"></a>
**Source:** p.102 S1886

**Original:** Together, these evaluations demonstrate two complementary forms of agentic execution. In simulation, ASPIREgenerated programs provide the task structure that direct GR00T 2 execution may lack, with online CaP recovery addressing unexpected states. In the real world, GR00T 2 performs most manipulation directly, while S2 detects failures and invokes targeted CaP skills, including skills acquired through CaP sim-to-real transfer. Both strategies extend GR00T 2’s capabilities through programmable recovery without requiring every contingency to be absorbed into the foundation policy itself.

**中文:** 综合来看，这些评测展示了两种互补的智能体化执行形式。在仿真中，ASPIREgenerated 程序提供了直接执行 GR00T 2 可能缺乏的任务结构，在线 CaP 恢复则处理意外状态。在现实世界中，GR00T 2 直接完成大部分操作，而 S2 检测失败并调用有针对性的 CaP 技能，其中包括通过 CaP 仿真到现实（sim-to-real）迁移获得的技能。两种策略都通过可编程恢复扩展了 GR00T 2 的能力，而无需把每一种应急情形都内化到基础策略本身之中。

<a id="H56"></a>
### G.2. Agentic Steering with Visual Guidance ｜ 智能体化视觉引导

<a id="S1887"></a>
**Source:** p.102 S1887

**Original:** Agentic skill composition and recovery (Sec. G.1) integrates GR00T 2 with external CaP programs and skills, whereas agentic steering keeps GR00T 2 as the only controller and lets the agent shape its behavior through the WAM API. We first describe the three parts of visual steering, in which the agent adds visual guidance to its language instructions: the interface, the agent loop, and the mid-training of GR00T 2. We then evaluate visual steering on short- and long-horizon benchmarks on YAM and Dexter.

**中文:** 智能体化技能组合与恢复（见 Sec. G.1）将 GR00T 2 与外部 CaP 程序和技能相结合，而智能体化引导（agentic steering）则让 GR00T 2 仍作为唯一控制器，由智能体通过 WAM API 塑造其行为。我们首先描述视觉引导的三个组成部分：智能体在语言指令之上叠加视觉引导的交互界面、智能体循环，以及 GR00T 2 的中期训练（mid-training）。随后，我们在 YAM 和 Dexter 上，分别于短时序与长时序基准中评估视觉引导。

<a id="S1888"></a>
**Source:** p.102 S1888

**Original:** Visual Guidance Interface. The interface separates what and where from how. For each step, the agent names the acting arm and gives a grasp point and a release point as pixel coordinates in the image of one scene camera (Tab. 21), while GR00T 2 determines the grasp pose, the approach, and all motion in between. We observed that GR00T 2 conditions strongly on fine visual details in its conditioning frames, so we pass the points by drawing them as markers directly on the conditioning frame rather than through a separate input: a filled disc for the grasp point and a plus-shaped cross for the release point, in the acting arm’s color (magenta for the left arm, cyan for the right), as in Fig. 8a. Only the acting arm is marked, and only on the current frame of the scene camera. Alongside the markers, GR00T 2 receives the agent’s per-step instruction, which names the

**中文:** 视觉引导接口。该接口将“做什么、在哪里做”与“怎么做”分开。对于每一步，智能体指定执行动作的手臂，并以某一场景相机图像（Tab. 21）中的像素坐标给出抓取点和释放点，而 GR00T 2 负责决定抓取位姿、接近方式以及其间的全部运动。我们观察到，GR00T 2 对其条件帧中的精细视觉细节高度敏感，因此我们不通过单独的输入传递这些点，而是把它们直接画在条件帧上作为标记：抓取点用实心圆盘表示，释放点用加号形十字表示，颜色取执行动作手臂的颜色（左臂为品红色，右臂为青色），如图 8a 所示。只标记执行动作的手臂，并且只标记场景相机的当前帧。除标记外，GR00T 2 还接收智能体的逐步指令，该指令指明

<a id="C075"></a>
**Source:** p.103 C075 · 图 F055

![F055](assets/F055.png)

**Original (caption):** Figure 55: Real-world tasks. (A) Toy Plane assembly: dump the parts, attach and fasten the bottom wing, turn the airplane over, and fasten the top wing. (B) Toy Tractor assembly: dump the parts, fasten the wheels on one side, turn the body over, and complete the other side. (C) Hot Wheels assembly: dump the parts, mount and fasten four wheels, and install and fasten the hood. (D) Multi-cable insertion: plug five Ethernet cables into a network switch. (E) Multi-charger insertion: plug five chargers into a power strip.

**中文图注：** 图 55：真实世界任务。（A）玩具飞机装配：倒出零件，安装并拧紧下机翼，将飞机翻转，再拧紧上机翼。（B）玩具拖拉机装配：倒出零件，拧紧一侧的车轮，将车身翻转，并完成另一侧。（C）Hot Wheels 装配：倒出零件，安装并拧紧四个车轮，再安装并拧紧引擎盖。（D）多线缆插接：将五根以太网线缆插入网络交换机。（E）多充电器插接：将五个充电器插入排插。

<a id="S1902"></a>
**Source:** p.103 S1902

**Original:** acting arm, in place of the task instruction.

**中文:** 执行动作的手臂，取代原任务指令。

<a id="S1903"></a>
**Source:** p.103 S1903

**Original:** Agent Loop. The agent loop has three layers. System 2 is the agent, which plans the steps and judges whether each step is done and what comes next. System 1 is GR00T 2, which executes the current step from the agent’s instruction and points. The harness is the rule-based program between them, which passes the agent’s instruction and points to GR00T 2 and decides when to query the agent. We use GPT-6 Astra as the agent, zero-shot and with one conversation per episode. At the start of an episode, it receives the task instruction and the images from all of the policy’s cameras, plans the steps, and returns the acting arm and the two points for the first step. The harness queries the agent again when an arm releases an object, when a fast vision-language model, used as a completion checker reports the step done, or after 45 s without a step end. The agent then decides whether to advance to the next step, redo the current one, replan the remaining steps, or finish.

**中文:** 智能体循环。智能体循环包含三层。系统 2（S2）即智能体，负责规划步骤，判断每一步是否完成以及接下来该做什么。系统 1（S1）即 GR00T 2，依据智能体的指令和指点执行当前步骤。调度框架（harness）是二者之间基于规则的程序，负责把智能体的指令和指点传给 GR00T 2，并决定何时向智能体发起查询。我们以零样本方式使用 GPT-6 Astra 作为智能体，每个回合使用一段对话。回合开始时，它接收任务指令以及策略所有相机的图像，规划步骤，并返回第一步的执行手臂和两个点。当某只手臂释放物体时、当用作完成判定器的快速视觉语言模型（VLM）报告该步骤已完成时，或在 45 s 内没有步骤结束时，调度框架会再次查询智能体。随后，智能体决定推进到下一步、重做当前步骤、重新规划剩余步骤，还是结束任务。

<a id="S1904"></a>
**Source:** p.103 S1904

**Original:** Mid-Training for Visual Guidance. Following the points requires mid-training, because pretraining never shows GR00T 2 markers on its observations. We generate the point labels automatically from existing demonstrations by detecting grasp and release events for each arm (Tab. 21). If an arm’s next event is a grasp, its grasp marker is placed at that grasp and its release marker at the following release. If the arm already holds an object, the grasp marker stays at the preceding grasp and the release marker is placed at the next release. Each marker is the end-effector position at the event, projected into the scene camera. Markers are drawn for the arm that acts next, and an arm is never marked alone while the other arm is the one that acts next, so an unmarked arm next to a marked one should not act, as at evaluation. Each sample is conditioned on its annotated sub-task instruction, or on the task instruction where none exists.

**中文:** 视觉引导的中期训练。要让 GR00T 2 遵循这些点，就需要中期训练，因为预训练时其观测中从未出现过标记。我们依据现有演示数据，通过检测每只手臂的抓取和释放事件，自动生成点标签（Tab. 21）。若某只手臂的下一个事件是抓取，则其抓取标记放在该次抓取处，释放标记放在随后的释放处。若手臂已经握着物体，则抓取标记保持在之前的抓取处，释放标记放在下一次释放处。每个标记都是事件发生时末端执行器的位置，并投影到场景相机中。标记针对下一步执行动作的手臂绘制；当另一只手臂是下一步的执行者时，不会单独标记某只手臂。因此，与有标记手臂相邻的未标记手臂不应动作，这与评测时的情况一致。每个样本以其标注的子任务指令为条件；若不存在子任务标注，则以任务指令为条件。

<a id="S1905"></a>
**Source:** p.103 S1905

**Original:** Each point-conditioned checkpoint is mid-trained from the pretrained GR00T 2 checkpoint for 20k steps with AdamW (learning rate 5 × 10−5, warmup-stable-decay schedule). For each, we also train a languageonly checkpoint on the same data, cameras, schedule, and compute, without markers, which serves as the language-only baseline in the evaluation on YAM and on Dexter trash sorting.

**中文:** 每个点条件化检查点都从预训练的 GR00T 2 检查点出发，使用 AdamW 进行 20k 步中期训练（学习率 5 × 10−5，预热-稳定-衰减调度）。对于每个点条件化检查点，我们还在相同的数据、相机、调度和计算预算下训练一个仅语言的检查点（不含标记），它在 YAM 和 Dexter 垃圾分类的评测中作为纯语言基线。

<a id="C076"></a>
**Source:** p.104 C076 · 表 T021

![T021](assets/T021.png)

**Original (caption):** Table 21: Embodiment-specific choices for visual steering. Everything not listed follows the shared rules in the text. The Dexter column describes the joint YAM and Dexter recipe used for Dexter trash sorting.

**中文表注：** 表 21：视觉引导的本体专用设置。未列出的内容均遵循正文中的共享规则。Dexter 一列描述的是用于 Dexter 垃圾分类的 YAM 与 Dexter 联合配方。

<a id="S1907"></a>
**Source:** p.104 S1907

**Original:** End effectors Two parallel grippers Two Sharpa five-fingered hands Policy cameras Top, two wrists, bottom Head, two wrists Marked camera Top Head Grasp and release events Gripper opening Fingertip contact forces Marker projection Per-station calibration (in-lab data), nominal camera model (additional teleoperation data)

**中文:** 末端执行器 两个平行夹爪 两只 Sharpa 五指手 策略相机 顶部、两个腕部、底部 头部、两个腕部 标记相机 顶部 头部 抓取与释放事件 夹爪开合度 指尖接触力 标记投影 每工位标定（实验室数据），标称相机模型（额外遥操作数据） [存疑：表格列在抽取中已展平，列与设备的对应关系不明]

<a id="S1911"></a>
**Source:** p.104 S1911

**Original:** strations (about 11.3k episodes, weight 0.29) Global batch, GPUs 320, 32 GB300 448 (on average 320 YAM and 128 Dexter), 64 GB300 Action chunk 48 predicted actions (1.6 s at 30 Hz), of which the first 30 are executed per policy call Per-step instruction “use the <arm> arm to ...” “... with the <arm> hand”

**中文:** [存疑：句首缺失，抽取文本以 “strations” 开头] 演示数据（约 11.3k 回合，权重 0.29）。全局批量，GPUs 320，32 GB300 448（平均 YAM 320、Dexter 128），64 GB300。动作块：48 个预测动作（30 Hz 下 1.6 s），其中每次策略调用执行前 30 个。逐步指令：“use the <arm> arm to ...”“... with the <arm> hand”。 [存疑：该单元格在抽取中已展平，数字归属不明]

<a id="S1912"></a>
**Source:** p.104 S1912

**Original:** Evaluation Settings. Each real-robot benchmark compares three settings, named as in Fig. 8. GR00T 2 is a language-only checkpoint given the original task instruction. GR00T 2 + Agent (language) is the same checkpoint given the agent’s per-step instructions, from the same agent loop with a prompt that omits the points. GR00T 2 + Agent (language + visual) is a point-conditioned checkpoint given the agent’s per-step instructions and markers. We refer to the last two settings as language guidance and visual guidance.

**中文:** 评测设置。每个真实机器人基准比较三种设置，命名方式与图 8 相同。GR00T 2 是接收原始任务指令的纯语言检查点。GR00T 2 + Agent（language）是同一检查点，接收来自同一智能体循环的逐步指令，但提示中不含点。GR00T 2 + Agent（language + visual）是点条件化检查点，接收智能体的逐步指令和标记。我们将后两种设置分别称为语言引导和视觉引导。

<a id="S1913"></a>
**Source:** p.104 S1913

**Original:** Short-Horizon Instruction Following. The short-horizon benchmarks test whether the guidance steers the policy. The YAM benchmark uses counterfactual instruction pairs: both instructions in a pair start from the same scene, which includes distractor objects, and differ only in the requested behavior, so a policy that repeats one plausible behavior regardless of the instruction can succeed on at most one instruction of each pair. It spans eight reference categories with three pairs each, giving 24 pairs and 48 instructions (Fig. 56). Six categories test grounding: nominal references identify objects or receptacles by name, category, or color; spatial references specify a position, relation, or distance; ordinal references select within an ordering, including relative size; cardinal references specify a number of objects or operations; arm references specify the acting arm; and exclusion references name an object that must be left untouched. Two categories test execution: action references distinguish operations such as opening versus closing, and grasp references constrain the approach or contact region. Each instruction is evaluated in three trials per setting (144 trials per setting). We report pass@1, the mean trial success, and pass@3, the fraction of instructions solved in at least one of their three trials.

**中文:** 短时序指令遵循。短时序基准检验引导是否能够改变策略的行为。YAM 基准采用反事实指令对：同一对中的两条指令从包含干扰物的同一场景出发，仅在所要求的行为上有所不同，因此无论指令如何都重复某一种合理行为的策略，在每对中至多只能成功完成一条指令。该基准涵盖八个参考类别，每类三对，共 24 对、48 条指令（图 56）。其中六类考察指代定位：名义参考通过名称、类别或颜色来识别物体或容器；空间参考指定位置、关系或距离；序数参考在某一排序中做选择，包括相对大小；基数参考指定物体数量或操作次数；手臂参考指定执行动作的手臂；排除参考指定一个必须保持不动的物体。另外两类考察执行能力：动作参考区分开启与关闭等不同操作，抓取参考约束接近方式或接触区域。每条指令在每种设置下评测三次试验（每种设置 144 次试验）。我们报告 pass@1（试验成功率的均值），以及 pass@3（其三次试验中至少有一次成功完成的指令所占比例）。

<a id="S1914"></a>
**Source:** p.104 S1914

**Original:** The Dexter benchmark likewise separates reference types, without counterfactual pairs, in dexterous pickand-place with colored cubes. It contains 32 tasks, each requiring the robot to move a specified cube into a specified basket with a permitted hand, grouped into four overlapping categories: attribute references (color, the Dexter counterpart of nominal references, 6 tasks), spatial references (12), ordinal references (7), and compositions of these references and constraints (9). A trial succeeds if the correct cube is released inside the specified basket by a permitted hand and remains stable for 2 s. Each task is evaluated in two trials per setting (64 trials per setting).

**中文:** Dexter 基准同样区分参考类型，但不使用反事实对，任务是用彩色方块进行灵巧抓放。它包含 32 个任务，每个任务都要求机器人使用许可的手，把指定方块移动到指定篮子中。任务分为四个相互重叠的类别：属性参考（颜色，即 Dexter 中对应名义参考的类别，6 个任务）、空间参考（12 个）、序数参考（7 个），以及这些参考与约束的组合（9 个）。只有当正确的方块被许可的手释放到指定篮子内，并保持稳定 2 s 时，试验才算成功。每个任务在每种设置下评测两次试验（每种设置 64 次试验）。

<a id="S1915"></a>
**Source:** p.104 S1915

**Original:** Long-Horizon Tasks. The long-horizon benchmarks require completing an entire multi-step task from a single instruction: trash sorting on both robots, and board disassembly on YAM as a stress test. In trash sorting, the robot places five items (on YAM: a glove, a crushed can, a plastic bottle, a sandwich, and a pepper; on Dexter:

**中文:** 长时序任务。长时序基准要求机器人仅凭一条指令完成整个多步骤任务：两台机器人上的垃圾分类，以及 YAM 上作为压力测试的板件拆解。在垃圾分类中，机器人需要放置五件物品（YAM 上为：一只手套、一个压扁的易拉罐、一个塑料瓶、一个三明治和一个辣椒；Dexter 上为：

<a id="C077"></a>
**Source:** p.105 C077 · 图 F056

![F056](assets/F056.png)

**Original (caption):** Figure 56: Short-horizon instruction following benchmark on YAM. Eight reference categories, each illustrated by a shared starting scene and two contrasting instructions. Blue and orange text denote the alternatives, and all remaining wording is identical. The panel labeled Constraint shows an exclusion reference.

**中文图注：** 图 56：YAM 上的短时序指令遵循基准。八个参考类别各由一个共享的起始场景和两条对比指令加以说明。蓝色与橙色文字表示两种备选，其余措辞完全相同。标为 Constraint 的面板展示的是排除参考。

<a id="S1932"></a>
**Source:** p.105 S1932

**Original:** a glove, a crushed can, a drink bottle, a sandwich, and a food scrap) into labeled compost, recycling, and trash bins whose order varies across 20 layouts per robot. Each item scores 0.2 if it ends in its correct bin. In board disassembly (Kimble et al., 2020), the robot removes the USB cable, two plugs, and two gears from a NIST task board and places the cable on a tray, the plugs in the right bin, and the gears in the left bin. Each item scores 0.1 for removal and 0.1 for correct placement. We report full-task success, in which all five items are completed, together with the mean rubric score. On YAM, the long-horizon runs were split between two stations with different operators, so the three settings were not all evaluated under the same station and operator.

**中文:** 一只手套、一个压扁的易拉罐、一个饮料瓶、一个三明治和一片食物残渣），并分别放入贴有标签的堆肥桶、回收桶和垃圾桶中，桶的顺序在每台机器人的 20 种布局中各不相同。若每件物品最终落入正确的桶，则该件计 0.2 分。在板件拆解（Kimble et al., 2020）中，机器人从 NIST 任务板上取下 USB 线缆、两个插头和两个齿轮，并把线缆放到托盘上，把插头放入右侧的桶，把齿轮放入左侧的桶。每件物品的取下计 0.1 分，正确放置计 0.1 分。我们报告全任务成功率（即五件物品全部完成），以及平均评分细则分数。在 YAM 上，长时序运行分配在两个工位进行，且操作员不同，因此三种设置并非全部在相同工位和相同操作员条件下评测。

<a id="S1933"></a>
**Source:** p.105 S1933

**Original:** Results. Tab. 22 lists every benchmark behind Fig. 8. On short-horizon tasks, visual guidance gives the highest success on both robots. On YAM, pass@1 rises from 41.7% for GR00T 2 and 55.6% with language guidance to 83.3% with visual guidance, and the gap narrows but persists at pass@3 (64.6%, 79.2%, and 89.6%). On Dexter, success rises from 29.7% and 32.8% to 70.3%. On long-horizon tasks, visual guidance completes 17 of 20 YAM trash-sorting episodes and 3 of 10 episodes of the board-disassembly stress test, whereas neither GR00T 2 nor language guidance completes any episode of either task. On Dexter trash sorting, visual guidance completes 9 of 20 episodes, against none for GR00T 2 and 1 with language guidance. Paired by layout, it sorts more items correctly than language guidance on 15 of the 20 layouts and fewer on 3 (two-sided sign test, 𝑝= 0.008).

**中文:** 结果。表 22 列出了图 8 背后的全部基准。在短时序任务上，视觉引导在两台机器人上都取得了最高成功率。在 YAM 上，pass@1 由 GR00T 2 的 41.7% 和语言引导的 55.6% 升至视觉引导的 83.3%；在 pass@3 上差距有所缩小但依然存在（分别为 64.6%、79.2% 和 89.6%）。在 Dexter 上，成功率由 29.7% 和 32.8% 升至 70.3%。在长时序任务上，视觉引导完成了 YAM 垃圾分类 20 个回合中的 17 个，以及板件拆解压力测试 10 个回合中的 3 个；而 GR00T 2 和语言引导在这两项任务中均未完成任何一个回合。在 Dexter 垃圾分类中，视觉引导完成了 20 个回合中的 9 个，GR00T 2 为 0 个，语言引导为 1 个。按布局配对比较，视觉引导在 20 个布局中的 15 个上比语言引导正确分拣更多物品，在 3 个布局上则更少（双侧符号检验，𝑝= 0.008 [公式原文见 p.105]）。

<a id="S1934"></a>
**Source:** p.105 S1934

**Original:** The YAM category breakdown (Tab. 23) shows where visual guidance helps. It reaches 100% pass@1 on nominal, spatial, and exclusion references and 94.4% on ordinal references. Language guidance alone already helps on nominal and ordinal references (88.9% each) but barely on spatial references (from 50.0% to 55.6%), where the marked grasp or release point resolves the relation directly. Gains are smaller on the two execution categories: relative to GR00T 2, success rises from 55.6% to 72.2% on action references and from 27.8% to 55.6% on grasp references. The markers do not specify the grasp approach, object orientation, or the motion required for operations such as flipping, pouring, and scooping. On Dexter, visual guidance gains most over GR00T 2 on spatial, ordinal, and compositional tasks (50.0, 57.1, and 50.0 points) and little on attribute tasks

**中文:** YAM 按类别的细分（Tab. 23）显示了视觉引导在哪些地方起作用。在名义参考、空间参考和排除参考上，它的 pass@1 达到 100%，在序数参考上为 94.4%。仅有语言引导时，名义参考和序数参考已有所改善（各为 88.9%），但在空间参考上几乎没有作用（从 50.0% 升至 55.6%），而空间参考中，标记的抓取点或释放点可以直接解决该关系。两类执行类别的增益较小：相对于 GR00T 2，动作参考的成功率从 55.6% 升至 72.2%，抓取参考则从 27.8% 升至 55.6%。标记并不指定抓取方式、物体朝向，也不指定翻转、倾倒和舀取等操作所需的运动。在 Dexter 上，相对于 GR00T 2，视觉引导在空间、序数和组合任务上的增益最大，而在属性任务上增益很小

<a id="C078"></a>
**Source:** p.106 C078 · 表 T022

![T022](assets/T022.png)

**Original (caption):** Table 22: Visual steering results on every benchmark. Short horizon: success rate (%), with successful trials in parentheses (pass@1 on YAM). Long horizon: full-task successes over episodes, with the mean rubric score (0 to 1) in parentheses. 𝑛counts trials (short horizon) or episodes (long horizon). The success rates and full-task counts are the components averaged in Fig. 8. †Obtained with an earlier implementation of the model.

**中文表注：** 表 22：每个基准上的视觉引导结果。短时序：成功率（%），括号内为成功试验数（YAM 为 pass@1）。长时序：按回合计的全任务成功数，括号内为平均评分细则分数（0 至 1）。𝑛 表示试验数（短时序）或回合数（长时序）。成功率和全任务成功数即图 8 中取平均所用的组成部分。†由该模型的早期实现获得。

<a id="C079"></a>
**Source:** p.106 C079 · 表 T023

![T023](assets/T023.png)

**Original (caption):** Table 23: YAM short-horizon pass@1 (%) by reference category. Each category has six instructions and 18 scored trials per setting.

**中文表注：** 表 23：YAM 短时序 pass@1（%），按参考类别划分。每个类别包含六条指令，每种设置下计分的试验为 18 次。

<a id="S1945"></a>
**Source:** p.106 S1945

**Original:** (8.3 points), where GR00T 2 already reaches 75.0%.

**中文:** （8.3 个百分点），其中 GR00T 2 已达到 75.0%。

<a id="S1946"></a>
**Source:** p.106 S1946

**Original:** Guidance Following. Success rates alone do not show that GR00T 2 follows the guidance, because a steerable policy should change its behavior when only the guidance changes (Chen et al., 2026d). The counterfactual pairs of the YAM short-horizon benchmark are designed to test a system-level version of this: within a pair, the scene is fixed and only the requested behavior changes. Counting a pair as solved if both of its instructions succeed in at least two of three trials, GR00T 2 solves 4 of the 24 pairs (16.7%), language guidance 10 (41.7%), and visual guidance 19 (79.2%). Conversely, 24 of the 60 successful trials of GR00T 2 (40.0%) come from instructions whose counterpart fails all three trials, as expected from a policy that repeats one behavior regardless of the instruction. This share falls to 12.5% (10 of 80) with language guidance and 5.8% (7 of 120) with visual guidance. On YAM trash sorting, GR00T 2 also follows the arm assignment: with visual guidance, the marked (and named) arm made 169 of 172 gripper closures (98.3%), against 164 of 181 (90.6%) for the named arm with language guidance, so wrong-arm closures fall from 9.4% to 1.7%. Its releases also follow the markers: with visual guidance, every release aimed at a bin landed in the marked bin, with one case unclear, whereas with language guidance, 21 items went into a wrong bin, or a different item was moved, after the agent had named the correct bin (see Failure Analysis).

**中文:** 指引遵循。仅看成功率并不能说明 GR00T 2 是否遵循了指引，因为一个可引导的策略应当在且仅在指引改变时改变其行为（Chen et al., 2026d）。YAM 短时序基准的反事实对正是为了从系统层面检验这一点而设计：在同一对中，场景固定，只有所要求的行为发生变化。若一对中的两条指令在三次试验中各自至少成功两次，则该对视为已解决。按此标准，GR00T 2 解决了 24 对中的 4 对（16.7%），语言引导解决了 10 对（41.7%），视觉引导解决了 19 对（79.2%）。反过来，GR00T 2 的 60 次成功试验中，有 24 次（40.0%）来自其对应指令三次试验全部失败的指令，这与一个无论指令如何都重复同一行为的策略的预期一致。语言引导下这一比例降至 12.5%（80 次中的 10 次），视觉引导下则降至 5.8%（120 次中的 7 次）。在 YAM 垃圾分类中，GR00T 2 也遵循了手臂分配：使用视觉引导时，被标记（并被命名）的手臂完成了 172 次夹爪闭合中的 169 次（98.3%），而语言引导下被命名手臂则为 181 次中的 164 次（90.6%），因此错误手臂的闭合率从 9.4% 降至 1.7%。它的释放也遵循标记：使用视觉引导时，每一次指向容器的释放都落入被标记的容器，仅有一例不明确；而使用语言引导时，在智能体已命名正确容器之后，仍有 21 件物品落入错误容器，或移动了另一件物品（见失败分析）。


<a id="S1948"></a>
**Source:** p.106 S1948

**Original:** Agent Cost and Latency. Steering adds the agent’s cost and latency to every episode, which we measure on trash sorting on both robots (Tab. 24). With visual guidance, an episode takes a median of 9 agent turns and costs $0.26 on YAM and $0.14 on Dexter, and the robot waits for the agent during 38% and 32% of the episode. GR00T 2 was served without the accelerations of Sec. 4.6.1 on YAM (about 0.6 s per policy call) and with TensorRT on Dexter (about 0.14 s).

**中文:** 智能体成本与时延。引导会为每个回合（episode）增加智能体的成本和时延，我们在两台机器人上对垃圾分拣任务进行了测量（Tab. 24）。加入视觉引导后，一个回合的中位数为 9 次智能体轮次，智能体成本在 YAM 上为 0.26 美元，在 Dexter 上为 0.14 美元，机器人分别有 38% 和 32% 的回合时间在等待智能体。GR00T 2 在 YAM 上未使用 Sec. 4.6.1 中的加速手段（每次策略调用约 0.6 秒），在 Dexter 上则使用 TensorRT（约 0.14 秒）。

<a id="S1949"></a>
**Source:** p.106 S1949

**Original:** Detecting Step Completion. The agent’s cost and the robot’s waiting also depend on when the harness queries the agent at the end of a step. In the YAM long-horizon runs, gripper events, which need no model call,

**中文:** 检测步骤完成。智能体的成本和机器人的等待时间，还取决于调度框架在步骤结束时何时查询智能体。在 YAM 长时序运行中，夹爪事件无需模型调用，

<a id="C080"></a>
**Source:** p.107 C080 · 表 T024

![T024](assets/T024.png)

**Original (caption):** Table 24: Agent cost and latency on trash sorting. Medians over the 20 episodes per setting. Latency is the per-episode median agent-turn time, agent cost is the charge for the agent’s turns (excluding the completion checks), and waiting is the share of the episode during which the robot holds still for the agent.

**中文表注：** 表 24：垃圾分拣任务上的智能体成本与时延。中位数基于每种设置下的 20 个回合（episode）。时延为每个回合的智能体轮次时间中位数；智能体成本为智能体轮次的费用（不含完成性检查）；等待占比为回合中机器人保持静止、等待智能体的时间比例。

<a id="S1962"></a>
**Source:** p.107 S1962

**Original:** triggered 418 of the 435 step-end queries, and the 45 s limit triggered the remaining 17. The completion check is meant for steps that end without a release, such as closing a drawer, but replaying the logged requests shows that even an always-correct check would confirm a step a median of 3.9 to 6.7 s after it ends, against about 1.5 s for a gripper event. Polled throughout every step, the checks also account for 26 to 36% of the combined agent and check charge on YAM, so we keep the check as a backstop.

**中文:** 在 435 次步骤结束查询中触发了 418 次，其余 17 次由 45 秒的时限触发。完成性检查原本用于那些没有释放动作就结束的步骤，例如关闭抽屉，但重放记录的请求后可以看到，即使一个总是正确的检查，也只能在步骤结束后中位数 3.9 至 6.7 秒才确认该步骤，而夹爪事件约为 1.5 秒。若在每个步骤中全程轮询，这些检查在 YAM 上还会占智能体与检查合计费用的 26% 至 36%，因此我们保留该检查作为兜底。

<a id="S1963"></a>
**Source:** p.107 S1963

**Original:** Failure Analysis. Failures on YAM trash sorting differ in kind between the two agent-guided settings. With visual guidance, 6 of 100 items are lost, in 3 episodes, and each of these episodes contains a failed hand-over, in which the agent asked one arm to stage an item at the center of the table for the other arm. By the agent’s step-end observations, every release aimed at a bin landed in the marked bin, with one case unclear. Of the 54 items lost with language guidance, 21 were released into a wrong bin, or a different item was moved, after the agent had named the correct bin, and 20 were never attempted because the agent spent the remaining steps retrieving misplaced items. On Dexter trash sorting, visual guidance leaves 11 items in a wrong bin, against 43 with language guidance and 56 for GR00T 2, while a similar share of pick-and-place attempts ends in some bin in every setting (72%, 65%, and 71%), so the settings differ mainly in choosing the right bin.

**中文:** 故障分析。在 YAM 垃圾分拣任务中，两种智能体引导设置下的失败类型并不相同。视觉引导下，100 件物品中有 6 件丢失，分布在 3 个回合中，而且这 3 个回合都包含一次失败的交接，即智能体要求一条手臂将物品暂放到桌面中央，供另一条手臂接取。根据智能体的步骤结束观察，每次指向垃圾桶的释放都落入了标记的垃圾桶，其中一次情况不明。语言引导下丢失的 54 件物品中，有 21 件被释放到错误的垃圾桶中，或者在智能体已说出正确垃圾桶之后移动了另一件物品；另有 20 件从未被尝试，因为智能体把剩余步数花在了找回错放的物品上。在 Dexter 的垃圾分拣任务上，视觉引导使 11 件物品落入错误的垃圾桶，语言引导为 43 件，GR00T 2 为 56 件；同时，各设置中抓放尝试最终落入某个垃圾桶的比例相近（分别为 72%、65% 和 71%），因此这些设置之间的差异主要在于能否选中正确的垃圾桶。

<a id="S1964"></a>
**Source:** p.107 S1964

**Original:** Simulation Test of Steerability on LIBERO. Simulation lets us test steerability without the agent by computing the markers from the simulator state. We evaluate 45 tasks from LIBERO-PRO (Zhou et al., 2025), which perturbs the scenes and instructions of LIBERO (Liu et al., 2023), with 10 episodes per task (448 valid episodes), including spatial-instruction variants of a two-bowl scene on which an earlier language-only checkpoint failed, to test steering where language is weak. We compare a single-arm language-only checkpoint with a single-arm point-conditioned checkpoint, both mid-trained for 20k steps on RoboCasa365 (Nasiriany et al., 2026), LIBERO, and DROID (Khazatsky et al., 2024). This simulation checkpoint uses an earlier, richer form of the interface: a time-colored end-effector path with a disc at the next grasp or release point. The markers raise success from 69.6% (312 of 448) for the language-only checkpoint to 85.0% (381), while the same point-conditioned checkpoint with nothing drawn reaches 72.5% (325). On the two-bowl variants, the markers raise success from 18 of 70 for the language-only checkpoint (20 with nothing drawn) to 41 of 70. Across tasks, the marked checkpoint does better than the language-only checkpoint on 13, worse on 8, and ties on the other 24.

**中文:** LIBERO 上的引导能力仿真测试。仿真让我们无需智能体即可测试引导能力，标记可以直接从仿真器状态计算得出。我们评测了 LIBERO-PRO（Zhou et al., 2025）中的 45 个任务，该基准对 LIBERO（Liu et al., 2023）的场景和指令进行了扰动。每个任务 10 个回合（共 448 个有效回合），其中包括双碗场景的空间指令变体，一个较早的仅语言检查点在该场景上失败过，这里用来测试语言较弱时的引导能力。我们比较了单臂仅语言检查点与单臂点条件检查点，二者都在 RoboCasa365（Nasiriany et al., 2026）、LIBERO 和 DROID（Khazatsky et al., 2024）上中期训练了 20k 步。该仿真检查点使用的是接口的早期、信息更丰富的形式：一条按时间着色的末端执行器轨迹，并在下一个抓取或释放点处画一个圆盘。标记将仅语言检查点的成功率从 69.6%（448 个中的 312 个）提升到 85.0%（381），而同一点条件检查点在不画任何标记时达到 72.5%（325）。在双碗变体上，标记将仅语言检查点的成功数从 70 中的 18 个（不画任何标记时为 20 个）提升到 70 中的 41 个。跨任务来看，加标记的检查点在 13 个任务上优于仅语言检查点，在 8 个任务上更差，其余 24 个任务持平。

<a id="S1965"></a>
**Source:** p.107 S1965

**Original:** Limitations. Visual steering also has three limitations. The points specify spatial targets and the acting arm, not a manipulation strategy, which limits the gains on grasp and action references. Every step moves one arm, so coordinated two-arm motion is excluded, and a hand-over becomes two single-arm steps. On the real robots, generalization to new scenes and objects is not tested.

**中文:** 局限性。视觉引导还有三个局限。这些点指定的是空间目标和执行动作的手臂，而不是操作策略，因此限制了在抓取参考和动作参考上的收益。每个步骤只移动一条手臂，因此不包括双臂协调运动，交接也会被拆分为两个单臂步骤。在真实机器人上，尚未测试对新场景和新物体的泛化能力。

<a id="H57"></a>
### G.3. Toward Robotic Self-Improvement ｜ 迈向机器人自我改进

<a id="S1966"></a>
**Source:** p.107 S1966

**Original:** Agentic learning, execution, and steering address complementary challenges in building autonomous robotic systems. AutoResearch investigates how learning algorithms can be improved through autonomous experimentation. CaP enables structured orchestration and specialized intervention during long-horizon execution.

**中文:** 智能体化学习、执行与引导，分别针对构建自主机器人系统中的互补挑战。AutoResearch 研究如何通过自主实验改进学习算法。代码即策略（code-as-policy, CaP）支持在长时序执行过程中进行结构化编排和专门化干预。

<a id="S1967"></a>
**Source:** p.108 S1967

**Original:** Visual guidance allows a high-level reasoning model to steer the behavior of a foundation policy through richer interfaces beyond language.

**中文:** 视觉引导使高层推理模型能够通过语言之外更丰富的接口，引导基础策略的行为。

<a id="S1968"></a>
**Source:** p.108 S1968

**Original:** A promising direction for future work is to integrate these capabilities into a unified self-improvement process. During deployment, agentic execution and steering could identify difficult states, generate corrective behaviors, and collect interaction experiences that expose limitations of the current foundation policy.

**中文:** 未来工作中一个有前景的方向，是把这些能力整合进统一的自我改进流程。在部署过程中，智能体化执行与引导可以识别困难状态、生成纠正行为，并收集能够暴露当前基础策略局限性的交互经验。

<a id="S1969"></a>
**Source:** p.108 S1969

**Original:** These experiences could be incorporated into AutoResearch to discover better post-training strategies, while successful agentic behaviors could be distilled into the foundation policy to improve its generality and reduce the need for future intervention.

**中文:** 这些经验可以纳入 AutoResearch，以发现更好的后训练策略；而成功的智能体化行为则可以蒸馏到基础策略中，以提升其通用性，并减少未来对人工干预的需要。

<a id="S1970"></a>
**Source:** p.108 S1970

**Original:** Such integration would create a feedback loop in which agentic systems improve not only how robots execute tasks, but also how their underlying policies are trained and adapted.

**中文:** 这样的整合将形成一个反馈回路，使智能体化系统不仅改进机器人执行任务的方式，也改进其底层策略的训练与适配方式。

<a id="S1971"></a>
**Source:** p.108 S1971

**Original:** Although realizing this fully integrated loop remains a direction for future work, these three approaches illustrate complementary opportunities for building robotic systems that can autonomously learn, orchestrate, and adapt their behavior.

**中文:** 尽管完全整合的闭环仍是未来工作的方向，但这三种路径共同展示了构建机器人系统的互补机会，使其能够自主学习、编排并调整自身行为。

<a id="H58"></a>
### H. Humanoid Loco-Manipulation ｜ 人形机器人移动操作

<a id="S1972"></a>
**Source:** p.109 S1972

**Original:** Loco-manipulation for bipedal humanoids poses additional challenges for robot foundation models, as humanoids must achieve precise end-effector control while maintaining balance under complex whole-body dynamics. Given these stringent requirements for reactive control, we turn to GR00T 2 Turbo, the lightweight variant of GR00T 2 suitable for deployment on edge devices (e.g. NVIDIA Jetson AGX Thor (Maheshwari et al., 2025)). We extend GR00T 2’s two-level architecture with SONIC (Luo et al., 2026) to form a three-level hierarchy (Fig. 9). A reasoning model, System 2 (S2), selects the task. Conditioned on this task and the current observations, GR00T 2 Turbo, System 1 (S1), generates short-horizon whole-body motion commands in SONIC’s compact latent action space. SONIC, System 0 (S0), translates these motion commands into joint-level commands while maintaining balance. Both S1 and S0 run onboard the robot, coupling task-directed motion generation with reactive whole-body control.

**中文:** 对双足人形机器人而言，移动操作带来了额外的挑战：人形机器人必须在复杂的全身动力学下保持平衡，同时实现精确的末端执行器控制。鉴于反应式控制的这些严格要求，我们采用 GR00T 2 Turbo，它是 GR00T 2 的轻量版本，适用于边缘设备部署（例如 NVIDIA Jetson AGX Thor（Maheshwari et al., 2025））。我们用 SONIC（Luo et al., 2026）扩展 GR00T 2 的两级架构，形成三级层级结构（Fig. 9）。推理模型系统 2（S2）负责选择任务。在该任务与当前观测的条件下，GR00T 2 Turbo 即系统 1（S1）在 SONIC 的紧凑潜变量动作空间中生成短时序的全身运动指令。SONIC 即系统 0（S0），在保持平衡的同时将这些运动指令转换为关节级指令。S1 与 S0 均在机器人本体上运行，将任务导向的运动生成与反应式全身控制耦合在一起。

<a id="S1973"></a>
**Source:** p.109 S1973

**Original:** Our investigation shows that GR00T 2 Turbo achieves high success rates across four task settings that highlight complementary aspects of whole-body loco-manipulation: scooping and serving popcorn, which requires precise bimanual tool use while standing; clearing diverse objects from a table into bins, which requires long-horizon coordination of walking, reaching, grasping, and carrying; and floor-level tasks, such as wiping spills with the feet and picking up objects while squatting or kneeling, which require coordinated upper- and lower-body motion.

**中文:** 我们的考察表明，GR00T 2 Turbo 在四类任务设置上取得了较高的成功率，这些设置分别突出了全身移动操作的不同方面：舀取并盛放爆米花，需要在站立时进行精确的双臂工具使用；将桌面上的各类物品清入垃圾桶，需要长时序协调行走、伸手、抓取和搬运；地面任务，例如用脚擦拭洒落物，以及下蹲或跪地拾取物品，需要上下肢协调运动。

<a id="S1974"></a>
**Source:** p.109 S1974

**Original:** All post-training data for whole-body loco-manipulation comes from whole-body teleoperation, which is expensive to collect and hard to scale. We therefore augment it with a large amount of synthetic data from a real-to-sim pipeline: teleoperated pick-and-place motions are fitted to the S0 controller and rolled out in simulation, so the synthetic demonstrations share the action space of the real data. GR00T 2 Turbo makes better use of this simulated data than the GR00T 1.7 VLA baseline, especially on out-of-distribution tabletop pick-and-place: starting from the same 6.7% success with real data alone, co-training raises GR00T 2 Turbo to 63.3%, compared with 40.0% for GR00T 1.7 (Tab. 26).

**中文:** 全身移动操作的全部后训练数据都来自全身遥操作，采集成本高，也难以扩展。因此，我们用大量来自现实到仿真（real-to-sim）流程的合成数据对其进行扩充：遥操作得到的抓放动作被拟合到 S0 控制器上并在仿真中展开，因此合成演示与真实数据共享同一动作空间。相比 GR00T 1.7 VLA 基线，GR00T 2 Turbo 更好地利用了这些仿真数据，尤其是在分布外的桌面抓放任务上：在仅使用真实数据、同为 6.7% 的成功率基础上，联合训练将 GR00T 2 Turbo 提升至 63.3%，而 GR00T 1.7 为 40.0%（Tab. 26）。


<a id="H59"></a>
### H.1. GR00T 2 Turbo on Whole-Body Latent Actions ｜ 基于全身潜在动作的 GR00T 2 Turbo

<a id="S1975"></a>
**Source:** p.109 S1975

**Original:** The architecture of GR00T 2 Turbo is described in Sec. 2. To use GR00T 2 Turbo on a humanoid, which requires high-frequency control to remain balanced, we use the latent token interface of SONIC (Luo et al., 2026) as its action space. At a frequency of 1 Hz, GR00T 2 Turbo predicts action chunks containing the desired SONIC motion tokens and gripper width commands for the next 1.6 s. Each chunk is sampled at 50 Hz, so that at each 20 ms control step the SONIC controller receives the corresponding low-dimensional motion token together with the current robot state and outputs joint position targets for the humanoid. Gripper widths are not passed through the SONIC controller. The same token space is used for data collection, simulation, and deployment. In teleoperation, the operator’s motion is encoded into tokens and executed by SONIC, so demonstrations are recorded directly in the action space of the policy. Simulated demonstrations are generated by running the same controller in simulation.

**中文:** GR00T 2 Turbo 的架构见 Sec. 2。要在人形机器人上使用 GR00T 2 Turbo，需要高频控制才能保持平衡，因此我们采用 SONIC（Luo et al., 2026）的潜 token 接口作为其动作空间。GR00T 2 Turbo 以 1 Hz 的频率预测动作块，每个动作块包含未来 1.6 s 内期望的 SONIC 运动 token 与夹爪宽度指令。每个动作块以 50 Hz 采样，因此在每个 20 ms 控制步，SONIC 控制器会接收对应的低维运动 token 以及当前机器人状态，并为人形机器人输出关节位置目标。夹爪宽度不经过 SONIC 控制器。数据采集、仿真与部署使用同一套 token 空间。在遥操作中，操作员的动作被编码为 token 并由 SONIC 执行，因此演示数据直接记录在策略的动作空间中。仿真演示则通过在仿真中运行同一控制器生成。

<a id="H60"></a>
### H.2. Real-World Whole-Body Loco-Manipulation ｜ 真实世界全身移动操作

<a id="S1976"></a>
**Source:** p.109 S1976

**Original:** Tasks. We evaluate four task families that focus on different aspects of whole-body loco-manipulation (Fig. 57). In popcorn serving, the robot stands in front of a popcorn machine, takes a cup from a dispenser, scoops the popcorn, fills the cup, and places it for a customer. The task requires bimanual tool use and precise placement while standing. In table clean-up, objects such as bottles, food containers, fruit, and wrappers are spread over a table, and the robot picks them up one at a time and puts them into trash bins, walking between the table and the bins. This task tests walking, reaching across a table, grasping diverse objects, and carrying. The ground pick-up task asks the humanoid to pick up diverse objects from the ground by bending down. The whole-body cleaning task combines floor pick-up with cleaning a spill: the robot takes a towel from a counter, picks up a cup, drops the towel on the spill, wipes with its feet, and discards the towel and the cup into the bins. These

**中文:** 任务。我们评估了四类任务，它们分别侧重全身移动操作的不同方面（图 57）。在爆米花供应任务中，机器人站在爆米花机前，从分配器取出一个杯子，舀取爆米花，将杯子装满后放好，供顾客取用。该任务要求机器人在站立状态下完成双臂工具使用与精确放置。在桌面清理任务中，瓶子、食品盒、水果和包装纸等物品散落在桌面上，机器人逐个拾取并放入垃圾桶，过程中需要在桌面与垃圾桶之间行走。该任务考察行走、跨越桌面伸手、抓取多样物体以及搬运能力。地面拾取任务要求人形机器人弯腰从地面拾取多种物体。全身清洁任务则将地面拾取与清理溢出物结合起来：机器人从台面取下毛巾，拿起一个杯子，将毛巾铺在溢出物上，用脚擦拭，最后把毛巾和杯子丢入垃圾桶。这些

<a id="C081"></a>
**Source:** p.110 C081 · 图 F057

![F057](assets/F057.png)

**Original (caption):** Figure 57: Autonomous real-world whole-body loco-manipulation. Representative task sequences executed autonomously by post-trained GR00T 2 Turbo policies, with time progressing from left to right. From top to bottom: popcorn serving requires precise bimanual tool use to scoop, fill, and place a cup; table clean-up combines reaching and grasping with walking and carrying objects to bins; ground pick-up requires reaching to the floor and standing up with an object before carrying it away; and whole-body cleaning coordinates towel handling, foot-based wiping, and kneeling to retrieve the towel for disposal.

**中文图注：** 图 57：真实世界全身移动操作的自主执行。图中为经后训练的 GR00T 2 Turbo 策略自主执行的代表性任务序列，时间自左向右推进。自上而下依次为：爆米花供应需要精确的双臂工具使用，以舀取、装满并放置杯子；桌面清理将伸手抓取，以及行走并把物体搬运至垃圾桶相结合；地面拾取需要伸手够到地面，并在拿起物体后站起，再将其带走；全身清洁则协调毛巾操作、以脚擦拭以及屈膝拾起毛巾以便丢弃。

<a id="S2009"></a>
**Source:** p.110 S2009

**Original:** tasks require deep reaches and coordinated use of the feet and arms, and they exercise the full capabilities of a bipedal humanoid. In addition, to study real and sim co-training, we use a tabletop pick-and-place task in which the humanoid starts at different positions relative to the table and picks up one of 30 diverse objects. The objects used for the table clean-up and tabletop pick-and-place tasks are shown in Fig. 58.

**中文:** 任务需要深度伸展，以及脚与手臂的协调配合，它们充分考验双足人形机器人的全部能力。此外，为研究真实与仿真的联合训练，我们使用一项桌面抓放任务：人形机器人从相对桌子的不同位置出发，拾取 30 种多样物体中的一件。桌面清理与桌面抓放任务所用的物体见图 58。

<a id="S2010"></a>
**Source:** p.110 S2010

**Original:** Data collection. We train our policies on demonstrations collected via whole-body teleoperation and on synthetic demonstrations generated in simulation. During teleoperation, an operator wears a headset and body trackers. The operator’s motion is encoded into SONIC tokens, executed on the robot, and recorded together with the camera images. For the popcorn task, we collected 1,500 episodes for a total of 17 hours of data. Table clean-up was recorded as continuous episodes in which the operator clears several objects in a row. The robot starts facing the table at a random heading, picks up a piece of trash from the table, and then puts the object into the trash bin. For this task, we collected 3,995 episodes: 1,105 general, 375 room, and 2,515 ground episodes. For ground pick-up and tabletop pick-up, we collected 3,402 and 3,292 episodes, respectively. For the spill clean-up task, we used 292 episodes, totaling 3 hours of data. Every episode is reviewed and scored, and only episodes that pass review are used.

**中文:** 数据采集。我们的策略基于通过全身遥操作采集的演示数据以及在仿真中生成的合成演示数据进行训练。遥操作时，操作员佩戴头显和身体追踪器。操作员的动作被编码为 SONIC token，在机器人上执行，并与相机图像一同记录。对于爆米花任务，我们共采集了 1,500 个回合（episode），总计 17 小时数据。桌面清理以连续回合的形式记录，操作员在每个回合中接连清理多个物体。机器人以随机朝向面对桌子，从桌面上拾起一件垃圾，然后将其放入垃圾桶。该任务共采集 3,995 个回合：其中 1,105 个为通用回合，375 个为房间回合，2,515 个为地面回合。地面拾取与桌面拾取分别采集了 3,402 个和 3,292 个回合。对于溢出物清理任务，我们使用了 292 个回合，总计 3 小时数据。每个回合都经过审核并打分，只有通过审核的回合才会被使用。

<a id="S2011"></a>
**Source:** p.110 S2011

**Original:** Training. Popcorn and spill clean-up are post-trained as single-task policies on their own demonstrations. Pick-and-place is post-trained as a multi-task policy that mixes tabletop pick-up, ground pick-up, placing into bins, and the clean-up segments, with a crosshair indicating the target. Object targets for the crosshair are labeled once per segment with a vision-language model and propagated through the video with a point tracker. For the comparison with GR00T 1.7, 𝜋0.5, and a diffusion policy (DP), we post-train each model on the same demonstrations with the same token action space and the same cameras.

**中文:** 训练。爆米花供应与溢出物清理任务各自仅使用自身的演示数据，以单任务策略的形式进行后训练。抓放任务则以多任务策略的形式进行后训练，混合了桌面拾取、地面拾取、放入垃圾桶以及清理片段，并以十字准星（crosshair）指示目标。十字准星的目标物体位置在每个片段中用视觉语言模型（VLM）标注一次，再通过点跟踪器沿视频传播。为与 GR00T 1.7、𝜋0.5 以及扩散策略（DP）进行比较，我们在相同的演示数据、相同的 token 动作空间和相同的相机条件下，对各模型进行后训练。

<a id="C082"></a>
**Source:** p.111 C082 · 图 F058

![F058](assets/F058.png)

**Original (caption):** Figure 58: Object sets for the tabletop pick-and-place and the table clean-up tasks.

**中文图注：** 图 58：桌面抓放任务与桌面清理任务所用的物体集合。

<a id="C083"></a>
**Source:** p.111 C083 · 表 T025

![T025](assets/T025.png)

**Original (caption):** Table 25: Real-world whole-body loco-manipulation on the Unitree G1. Success rate (%) using each listed model as S1, with the SONIC controller as S0. No partial credit is given (the reported success rate is the sum of the binary scores over all trials divided by the total number of trials). All policies are post-trained on the same demonstrations per task. DP: diffusion policy on latent tokens; 𝜋0.5 (VLA); GR00T 1.7 (VLA); GR00T 2 Turbo (WAM).

**中文表注：** 表 25：Unitree G1 上的真实世界全身移动操作。以所列各模型作为 S1、以 SONIC 控制器作为 S0 时的成功率（%）。不给部分分（报告的成功率为所有试次的二元得分之和除以试次总数）。所有策略在每个任务上均使用相同的演示数据进行后训练。DP：基于潜 token 的扩散策略；𝜋0.5（VLA）；GR00T 1.7（VLA）；GR00T 2 Turbo（WAM）。

<a id="S2017"></a>
**Source:** p.111 S2017

**Original:** Evaluation and results. Popcorn serving is scored on a fixed suite of 48 runs, each requiring two full cups to be scooped and placed. The table clean-up task is scored on 30 trials; each trial involves picking up 6 diverse objects and putting all of them into the bin successfully. Failing to pick up an object or to drop it into the trash bin results in failure. Tabletop pick-and-place is scored on 30 trials with 30 household objects, 25 rigid and 5 soft, placed at ten positions on tables of three heights, with a 30 s limit per trial. Ground pick-up is scored on the same 30 household objects placed on the ground. For the spill clean-up task, we measure success over 30 trials of the full sequence: grabbing the towel, picking up the cup, wiping the spill with the feet, and dropping the towel and the cup into the bins. Tab. 25 reports the results. GR00T 2 Turbo completes 48 of 48 popcorn runs at about 41 s per two cups, while GR00T 1.7 trained on the same data completes 83% at about 48 s per two cups and is the best-performing baseline on this task. On table clean-up, GR00T 2 Turbo succeeds in 28 of 30 trials. Failures are flat objects such as a napkin or a chips bag that the gripper misses on, and objects knocked out of reach. Ground pick-up succeeds in 25 of 30 trials with the same failure modes. On the whole-body spill clean-up task, GR00T 2 Turbo succeeds in 14 of 30 trials, and GR00T 1.7 is again the second-best model with 13 of 30.

**中文:** 评测与结果。爆米花供应在一套固定的 48 次运行上进行评测，每次运行都需要舀取并放置两杯完整的爆米花。桌面清理任务基于 30 次试次进行评测，每次试次需拾取 6 件多样物体，并将它们全部成功放入垃圾桶。未能拾取物体，或未能将其投入垃圾桶，都会导致失败。桌面抓放在 30 次试次上评测，使用 30 件家用物体（其中 25 件为刚性物体，5 件为软性物体），放置在三种高度桌面上的十个位置，每次试次限时 30 s。地面拾取使用同样的 30 件家用物体，放置在地面上进行评测。对于溢出物清理任务，我们在 30 次完整流程试次上测量成功率：抓取毛巾、拾起杯子、用脚擦拭溢出物，并将毛巾和杯子丢入垃圾桶。表 25 给出了结果。GR00T 2 Turbo 完成了全部 48 次爆米花运行，每两杯约耗时 41 s；在相同数据上训练的 GR00T 1.7 完成率为 83%，每两杯约耗时 48 s，是该任务上表现最好的基线。在桌面清理任务中，GR00T 2 Turbo 在 30 次试次中成功 28 次。失败情形包括：夹爪抓空的扁平物体（如餐巾纸或薯片袋），以及被碰出可及范围的物体。地面拾取在 30 次试次中成功 25 次，失败模式相同。在全身溢出物清理任务中，GR00T 2 Turbo 在 30 次试次中成功 14 次，GR00T 1.7 再次位居第二，成功 13 次。


<a id="H61"></a>
### H.3. WAMs Consume Simulation Data Better than VLAs ｜ WAM 对仿真数据的利用优于 VLA

<a id="S2018"></a>
**Source:** p.111 S2018

**Original:** Motion-centric Real-to-Sim Demonstrations. Real-world teleoperation data is costly to collect and limited in scene and object diversity. Our key insight is to reuse the whole-body motions recorded on the G1 by finding simulated scenes in which those motions successfully perform the task. Since teleoperated episodes contain motion and camera observations but not exact table and object poses, we initialize their simulated placements from the head-camera images and refine them using CMA-ES (Hansen et al., 2003). In MuJoCo (Todorov et al., 2012) or Isaac Lab (Mittal et al., 2025), we replay each motion through the same SONIC controller used on the

**中文:** 以运动为中心的现实到仿真演示。真实世界的遥操作数据采集成本高，且场景与物体的多样性有限。我们的核心思路是复用在 G1 上记录的全身运动，为这些运动寻找能让它们成功完成任务的仿真场景。由于遥操作片段包含运动和相机观测，却不包含精确的桌面与物体位姿，我们根据头部相机图像初始化它们在仿真中的摆放位置，并使用 CMA-ES（Hansen et al., 2003）进行优化。在 MuJoCo（Todorov et al., 2012）或 Isaac Lab（Mittal et al., 2025）中，我们使用与真实机器人相同的 SONIC 控制器回放每段运动，

<a id="C084"></a>
**Source:** p.112 C084 · 图 F059

![F059](assets/F059.png)

**Original (caption):** Figure 59: Motion-centric simulation data generation. (A) We use the recorded whole-body motion of a teleoperated episode. (B) SONIC replays the motion in simulation while CMA-ES fits the table and object placement. (C) A fit is kept only if the robot lifts the object and holds it under a pull equal to its weight. (D) The same accepted fit is rendered in many generated rooms.

**中文图注：** 图 59：以运动为中心的仿真数据生成。（A）使用一段遥操作片段中记录的全身运动。（B）SONIC 在仿真中回放该运动，同时 CMA-ES 拟合桌面与物体的摆放。（C）只有当机器人抬起物体，并在相当于物体重量的拉力下保持抓握时，拟合结果才会被保留。（D）同一个被接受的拟合结果会在大量生成的房间中渲染。

<a id="C085"></a>
**Source:** p.112 C085 · 表 T026

![T026](assets/T026.png)

**Original (caption):** Table 26: WAMs consume simulation data better than VLAs. Tabletop pick-and-place success rate (%) over 30 trials on the G1 when simulated demonstrations are mixed into the same real dataset.

**中文表注：** 表 26：WAM 对仿真数据的利用优于 VLA。当仿真演示与同一真实数据集混合时，G1 上桌面抓放任务的成功率（%），统计范围为 30 次试次。

<a id="S2036"></a>
**Source:** p.112 S2036

**Original:** real robot, keeping the recorded motion fixed while optimizing the scene. The search evaluates 48 candidate scenes in parallel per generation and proceeds in two stages: fitting the table position, height, and yaw; then fitting the object type, position, and orientation on the table. A fit is accepted only if the final rollout grasps the object with both fingers, lifts it, and holds it through a 30-frame disturbance force equal to the object’s weight, followed by a 100-frame hold. We then render these fitted trajectories in procedurally generated environments with randomized lighting and camera placement, recording token sequences and rendered images in the same format as the real demonstrations. The resulting synthetic demonstrations preserve the real-data action space while expanding visual and object diversity. We use this procedure to generate 250,000 synthetic episodes totaling 1,000 hours. The generation procedure and examples are shown in Fig. 59.

**中文:** 真实机器人上运行，保持记录下来的运动不变，只优化场景。搜索过程中，每一代并行评估 48 个候选场景，分为两个阶段：先拟合桌面的位置、高度和偏航角；再拟合桌面上物体的类型、位置和朝向。只有当最终回放中物体被双指抓住、被抬起，并在相当于物体重量的 30 帧扰动力下保持住，随后再保持 100 帧时，该拟合才会被接受。随后，我们在随机化光照和相机位置的程序化生成环境中渲染这些拟合轨迹，所记录的 token 序列与渲染图像与真实演示的格式相同。由此生成的合成演示保留了真实数据的动作空间，同时扩大了视觉与物体的多样性。我们用该流程生成了 250,000 个合成片段，共计 1,000 小时。生成流程与示例见 Fig. 59。

<a id="S2037"></a>
**Source:** p.112 S2037

**Original:** Results. In Tab. 26, we test each policy in distribution, in the environment where the real data were collected, and out of distribution, in unseen scenes and locations. The synthetic data improve the pick-and-place success rate of GR00T 1.7 and GR00T 2 Turbo in both settings, while 𝜋0.5 degrades in distribution. The gain is largest out of distribution, where both GR00T 1.7 and GR00T 2 Turbo start from 6.7% with real data alone. The WAM benefits more from the simulated data in this setting: co-training removes 61% of its failures, compared with 36% for GR00T 1.7, a difference of 25 percentage points. With 30 trials per cell, however, the difference between the two co-trained models (19 against 12 successes) is suggestive rather than conclusive (two-sided Fisher exact test, 𝑝≈0.12).

**中文:** 结果。在 Tab. 26 中，我们分别在分布内（即采集真实数据的环境）和分布外（未见过的场景与地点）两种设定下测试每个策略。合成数据在两种设定下都提升了 GR00T 1.7 和 GR00T 2 Turbo 的抓放成功率，而 𝜋0.5 在分布内出现了性能下降。增益在分布外最大：仅使用真实数据时，GR00T 1.7 和 GR00T 2 Turbo 的起点都是 6.7%。在这一设定下，WAM 从仿真数据中获益更多：联合训练使其失败数减少了 61%，而 GR00T 1.7 为 36%，两者相差 25 个百分点。不过，每个单元格只有 30 次试次，两个联合训练模型之间的差异（19 次成功对比 12 次成功）属于提示性结果，而非结论性结果（双侧 Fisher 精确检验，𝑝≈0.12）。

<a id="S2038"></a>
**Source:** p.112 S2038

**Original:** Why. We hypothesize that this comes from the video prediction objective: the WAM’s more general video encoder maps rendered and camera frames into a shared latent space in which the model predicts how the scene evolves under its actions, a correspondence that is identical in simulation and reality, whereas a VLA maps appearance features tuned to real images directly to actions and treats rendered frames as out-of-distribution.

**中文:** 原因。我们推测这源于视频预测目标：WAM 更具通用性的视频编码器将渲染帧与相机帧映射到一个共享潜空间，模型在该空间中预测场景在其动作作用下如何演化，且这种对应关系在仿真与现实中是一致的。而 VLA 则将针对真实图像调校的外观特征直接映射为动作，并把渲染帧视为分布外输入。

<a id="H62"></a>
### I. Accelerating GR00T 2 ｜ 加速 GR00T 2

<a id="S2039"></a>
**Source:** p.113 S2039

**Original:** Practical deployment of a generalist robotics foundation model requires timely predictions, continuous motion, and efficient task completion across tasks and embodiments. Deployment on edge hardware also imposes compute, memory, power, and thermal limits. We address these requirements through inference acceleration, training-time real-time chunking (RTC) (Black et al., 2025), and phase-conditioned action chunk retiming. We evaluate latency, task outcomes, and motion quality together.

**中文:** 通用机器人基础模型的实际部署需要及时的预测、连续的运动，以及跨任务和跨本体的高效任务完成。在边缘硬件上部署还会受到算力、内存、功耗和热学约束的限制。我们通过推理加速、训练时实时分块（RTC）（Black et al., 2025）以及相位条件化的动作块重定时来应对这些需求。我们同时评估时延、任务结果与运动质量。

<a id="S2040"></a>
**Source:** p.113 S2040

**Original:** We first reduce inference latency within the deployment resource budget. WAMs in our setting incur higher inference latency than their VLA counterparts, motivating policy inference acceleration and system-level optimizations. Visual encoding and iterative video-action denoising contribute to model prediction latency, while observation processing and communication add delay around the model. We optimize both paths and distinguish model prediction latency from observation-to-applied-action latency. However, some delay remains even after optimization. Waiting for each prediction can interrupt execution, while naively executing predictions asynchronously can introduce discontinuities between successive action chunks. We therefore use training-time real-time chunking (RTC) to account for actions committed during inference and train the policy to produce compatible continuations.

**中文:** 我们首先在部署资源预算内降低推理时延。在我们的设定中，WAM 的推理时延高于其对应的 VLA，因此需要进行策略推理加速和系统级优化。视觉编码与迭代的视频-动作去噪会造成模型预测时延，而观测处理和通信会在模型前后引入额外延迟。我们同时优化这两条路径，并区分模型预测时延与观测到已应用动作的时延。然而，即使经过优化，仍会存在一定延迟。等待每次预测完成会打断执行，而简单地异步执行预测则会在相邻动作块之间引入不连续性。因此，我们使用训练时实时分块（RTC）来考虑推理期间已确定的动作，并训练策略生成与之兼容的后续动作。

<a id="S2041"></a>
**Source:** p.113 S2041

**Original:** Continuity must also preserve the policy’s ability to correct its behavior using new observations. In our setting, standard training-time RTC improves continuity but may degrade task performance. We address this tradeoff with noisy-prefix, action-only RTC. Perturbing the conditioning prefix is intended to reduce reliance on the previous plan while retaining context for a smooth continuation. We further find that a small-scale fine-tuning stage applied to the post-trained base model captures most of the action-continuity benefits, making RTC adaptation practical without repeating the full training pipeline.

**中文:** 连续性还必须保留策略利用新观测修正自身行为的能力。在我们的设定中，标准的训练时 RTC 提高了连续性，但可能降低任务性能。我们通过带噪前缀、仅动作的 RTC 来处理这一权衡。对条件前缀施加扰动，旨在降低对先前计划的依赖，同时保留足够的上下文以实现平滑衔接。我们还发现，对后训练基础模型进行一个小规模微调阶段，就能获得大部分动作连续性收益，从而使 RTC 适配无需重复完整训练流程即可落地。

<a id="S2042"></a>
**Source:** p.113 S2042

**Original:** Finally, continuous execution and low inference latency do not necessarily yield shorter task completion times. We introduce phase-dependent action-chunk acceleration to increase execution speed where the task permits it while retaining finer timing for precise interactions. Accelerated execution also changes the temporal relationship between successive chunks, requiring the continuity mechanism to account for the revised execution timeline. Temporal chunk alignment addresses this timing mismatch, while cross-chunk jerk optimization smooths the transition between successive commands. We evaluate the combined approach through inference latency, motion quality, task completion time, and success rate to establish whether faster execution preserves reliable task performance.

**中文:** 最后，持续执行与低推理时延并不一定意味着更短的任务完成时间。我们引入相位相关的动作块加速，在任务允许的地方提高执行速度，同时在精细交互处保留更精细的时序。加速执行也会改变相邻动作块之间的时间关系，因此连续性机制需要考虑修订后的执行时间线。时间动作块对齐用于解决这一时序失配，而跨块加加速度（jerk）优化则平滑相邻指令之间的过渡。我们通过推理时延、运动质量、任务完成时间和成功率来评估这一组合方法，以确定更快的执行是否仍能保持可靠的任务性能。

<a id="H63"></a>
### I.1. Accelerating Model Inference ｜ 加速模型推理

<a id="S2043"></a>
**Source:** p.113 S2043

**Original:** Inference uses a client-server architecture: the robot client sends observations and executes returned action chunks through its controller, while the server runs the policy (Sec. K.5).

**中文:** 推理采用客户端-服务器架构：机器人客户端发送观测，并通过其控制器执行返回的动作块，服务器则运行策略（Sec. K.5）。

<a id="S2044"></a>
**Source:** p.113 S2044

**Original:** GR00T 2 predicts action chunks by encoding camera observations, robot state, and task instructions, then iteratively denoising video and action latents. This computation adds delay to the control loop, while observation processing and communication introduce further overhead. We reduce these costs through computation reuse, optimized GPU execution, and a serving path that supports different embodiments and deployment hardware.

**中文:** GR00T 2 通过编码相机观测、机器人状态和任务指令来预测动作块，然后对视频与动作潜变量进行迭代去噪。这一计算会给控制回路增加延迟，而观测处理和通信还会带来进一步的开销。我们通过计算复用、优化的 GPU 执行，以及支持不同本体和部署硬件的服务路径来降低这些成本。

<a id="S2045"></a>
**Source:** p.113 S2045

**Original:** Timing boundaries. The environment continues to change while the policy computes, so prediction time is only part of the delay before a robot responds. We distinguish two intervals (Fig. 60). Model prediction latency covers encoding and iterative denoising performed within a prediction request. Observation-to-applied-action latency extends from observation preparation to controller application, including serialization, transport, and response handling. Streaming and prefetch can move encoding before the prediction request. We identify these configurations explicitly because their foreground prediction time excludes that encoding work.

**中文:** 时序边界。策略计算期间环境仍在变化，因此预测时间只是机器人作出响应前延迟的一部分。我们区分两段时间间隔（Fig. 60）。模型预测时延涵盖单次预测请求内部执行的编码与迭代去噪。观测到已应用动作的时延则从观测准备一直延伸到控制器应用，包括序列化、传输和响应处理。流式处理与预取可以将编码提前到预测请求之前。我们明确列出这些配置，是因为它们的前台预测时间不包含这部分编码工作。

<a id="S2046"></a>
**Source:** p.113 S2046

**Original:** Optimizing model prediction. We first remove repeated computation. The policy reuses text features while the task instruction and model remain unchanged, and refreshes visual and state representations for new observations. For a fixed checkpoint and denoising schedule, timestep-dependent conditioning values are

**中文:** 优化模型预测。我们首先去除重复计算。只要任务指令和模型保持不变，策略就复用文本特征；对于新的观测，则刷新视觉与状态表示。对于固定的检查点和去噪调度，随时间步变化的条件值，

<a id="C086"></a>
**Source:** p.114 C086 · 图 F060

![F060](assets/F060.png)

**Original (caption):** Figure 60: Timing boundaries for GR00T 2 policy inference. Model prediction covers request-time encoding and iterative denoising. Observation-to-applied-action latency additionally includes observation preparation, communication, response handling, and controller scheduling. The diagram is schematic, and stage widths do not represent measured durations.

**中文图注：** 图 60：GR00T 2 策略推理的时序边界。模型预测涵盖请求时的编码与迭代去噪。观测到已应用动作的时延还包括观测准备、通信、响应处理和控制器调度。该示意图仅为示意性质，各阶段的宽度并不代表实测时长。

<a id="S2070"></a>
**Source:** p.114 S2070

**Original:** computed in advance. Within the denoising loop, action-only updates reuse attention keys and values from the most recent video update. Persistent buffers reduce repeated cache preparation and copying.

**中文:** 可以预先计算。在去噪循环内，仅动作的更新会复用最近一次视频更新中的注意力键与值。持久缓冲区减少了重复的缓存准备与拷贝。

<a id="S2071"></a>
**Source:** p.114 S2071

**Original:** We then accelerate the remaining computation. TensorRT compiles the video VAE encoder and transformer into specialized GPU engines, and CUDA graph replay reduces CPU dispatch and kernel-launch overhead. For supported checkpoints, we calibrate the BF16-trained model on representative robot observations and apply FP8 to selected projection and feed-forward layers in the joint transformer. Normalization layers and the action-only engine retain higher precision. Supported recipes also use FP8 for VAE encoding. Reducing denoising steps provides an additional tradeoff between latency, task success, and motion smoothness, which we assess for each checkpoint and task.

**中文:** 随后，我们加速剩余的计算。TensorRT 将视频 VAE 编码器和 Transformer 编译为专用的 GPU 引擎，CUDA graph 回放则降低了 CPU 调度和核函数启动的开销。对于支持的检查点，我们使用代表性的机器人观测对 BF16 训练的模型进行校准，并对联合 Transformer 中选定的投影层和前馈层应用 FP8。归一化层与仅动作引擎则保持更高精度。受支持的配方还会对 VAE 编码使用 FP8。减少去噪步数会在时延、任务成功率和运动平滑性之间带来额外的权衡，我们针对每个检查点和任务分别进行评估。

<a id="S2072"></a>
**Source:** p.114 S2072

**Original:** Fig. 19 compares measured model-prediction latency for a GR00T 2 Turbo checkpoint deployed on G1 using RTX 5090 and Jetson Thor.

**中文:** Fig. 19 比较了 GR00T 2 Turbo 检查点部署在 G1 上、分别使用 RTX 5090 与 Jetson Thor 时实测的模型预测时延。

<a id="S2073"></a>
**Source:** p.114 S2073

**Original:** Tab. 27 reports median prediction latency for GR00T 2 and GR00T 2 Turbo across three embodiments and the evaluated hardware. Each baseline-optimized pair uses the same underlying checkpoint and input observations. The optimized configurations provide 2.94× to 7.15× speedup relative to eager BF16 execution. Each speedup applies to the complete configuration: the G1 comparison includes fewer denoising steps, while optimized Dexter and YAM use prefetched VAE representations. The timing boundaries and execution recipes are specified alongside the table.

**中文:** Tab. 27 报告了 GR00T 2 与 GR00T 2 Turbo 在三种本体及所评估硬件上的模型预测中位时延。每个基线-优化配对都使用相同的底层检查点和输入观测。相对于即时 BF16 执行，优化配置实现了 2.94× 至 7.15× 的加速。每项加速都针对完整配置而言：G1 的对比包含了更少的去噪步数，而经过优化的 Dexter 和 YAM 则使用了预取的 VAE 表示。时序边界与执行配方与该表一并给出。

<a id="S2074"></a>
**Source:** p.114 S2074

**Original:** We use one checkpoint per embodiment across hardware comparisons. All three use the 2B model configuration, with five history frames per camera at 224 × 320 pixels (height × width). Dexter uses three camera views in four model slots and a 48-action prediction horizon, YAM uses four views and a 48-action horizon, and the GR00T 2 Turbo checkpoint for G1 uses three views and an 80-action horizon. The notation 2v4a denotes two video and four action denoising steps. Dexter uses 2v2a and YAM uses 2v4a in both baseline and optimized execution. G1 changes from 2v4a to 1v2a, with the action horizon unchanged.

**中文:** 在硬件对比中，我们为每个本体使用一个检查点。三者都采用 2B 模型配置，每个相机保留五个历史帧，分辨率为 224 × 320 像素（高 × 宽）。Dexter 使用三个相机视角、四个模型槽位以及 48 个动作的预测时域；YAM 使用四个视角与 48 个动作的时域；用于 G1 的 GR00T 2 Turbo 检查点则使用三个视角与 80 个动作的时域。记号 2v4a 表示两个视频去噪步和四个动作去噪步。Dexter 在基线与优化执行中都使用 2v2a，YAM 都使用 2v4a。G1 从 2v4a 改为 1v2a，动作时域保持不变。

<a id="S2075"></a>
**Source:** p.114 S2075

**Original:** All optimized configurations use TensorRT and CUDA graphs. Dexter uses FP16-mixed transformer engines with BF16 streaming VAE and prefetch, without codec roundtrip. G1 uses FP8 mixed precision, with VAE encoding included in prediction latency. YAM uses FP8 joint-transformer and VAE engines, a BF16 action engine, and whole-window VAE prefetch with MP4V. For Dexter and YAM, eager timings include VAE encoding, while optimized timings exclude encoding completed before the request.

**中文:** 所有优化配置都使用 TensorRT 与 CUDA graph。Dexter 使用 FP16 混合精度的 Transformer 引擎，配合 BF16 流式 VAE 与预取，且不包含编解码往返。G1 使用 FP8 混合精度，并将 VAE 编码计入预测时延。YAM 使用 FP8 的联合 Transformer 与 VAE 引擎、BF16 的动作引擎，以及使用 MP4V 的整窗口 VAE 预取。对于 Dexter 和 YAM，即时执行的时间包含 VAE 编码，而优化后的时间则不包含在请求前已完成的编码。

<a id="C087"></a>
**Source:** p.115 C087 · 表 T027

![T027](assets/T027.png)

**Original (caption):** Table 27: Median model-prediction latency (p50) for GR00T 2 and GR00T 2 Turbo across embodiments and hardware. Speedup is baseline latency divided by optimized latency.

**中文表注：** 表 27：GR00T 2 与 GR00T 2 Turbo 在各本体和硬件上的模型预测中位时延（p50）。加速比为基线时延除以优化后的时延。

<a id="S2083"></a>
**Source:** p.115 S2083

**Original:** We evaluate embodiment-specific checkpoints. Each baseline-optimized pair uses the same underlying checkpoint and input profile. Baselines use unquantized BF16 PyTorch execution with checkpoint-default attention kernels. Baseline revisions are selected per checkpoint to preserve its required model behavior.

**中文:** 我们评估针对具体本体的检查点。每个基线-优化配对都使用相同的底层检查点和输入配置。基线采用未量化的 BF16 PyTorch 执行，并使用检查点默认的注意力核函数。基线版本按检查点单独选定，以保留其所需的模型行为。

<a id="S2084"></a>
**Source:** p.115 S2084

**Original:** Optimizing the serving path. Multi-camera observations must be encoded, transferred, and prepared before the model can use them. We reduce this overhead with bounded CPU worker pools for camera-history processing, faster JPEG encoding and decoding, and fewer memory copies. Where supported, incremental streaming VAE reuses cached encoder state as camera frames arrive. VAE prefetch prepares the required visual latents before the next prediction request, moving encoding off the foreground prediction path. The benefit depends on the observation format, client implementation, and hardware. Deployment-level evaluation must also account for the age of the observations and the encoding work performed before the request.

**中文:** 优化服务路径。多相机观测必须先经过编码、传输和准备，模型才能使用。我们通过以下方式降低这部分开销：为相机历史处理设置有界的 CPU 工作池，采用更快的 JPEG 编解码，并减少内存拷贝。在支持的情况下，增量流式 VAE 会在相机帧到达时复用已缓存的编码器状态。VAE 预取会在下一次预测请求之前准备所需的视觉潜变量，从而将编码工作移出前台预测路径。其收益取决于观测格式、客户端实现和硬件。部署层面的评估还必须考虑观测的时效，以及请求前已完成的编码工作。

<a id="S2085"></a>
**Source:** p.115 S2085

**Original:** Latency and action fidelity. Approximation-based inference acceleration can reduce latency at the cost of task success, our primary measure of robot policy quality. We therefore assess the effects of acceleration through numerical validation, simulation, and physical-robot evaluation. Numerical comparisons use the same checkpoint’s eager BF16 execution as a reference, holding observations, conditioning, denoising schedules, and initial noise fixed. We compute mean squared error over valid, newly generated actions, excluding padding and committed RTC prefixes, and inspect decoded errors by action group. Simulation and physical-robot tests evaluate whether accelerated execution preserves task success, alongside completion time and motion smoothness.

**中文:** 时延与动作保真度。基于近似的推理加速可以降低时延，但可能以任务成功率为代价，而任务成功率是我们衡量机器人策略质量的主要指标。因此，我们通过数值验证、仿真和实体机器人评估来考察加速的效果。数值比较以同一检查点的即时 BF16 执行作为参考，并固定观测、条件、去噪调度和初始噪声。我们计算有效的新生成动作上的均方误差，排除填充部分和已确定的 RTC 前缀，并按动作分组检查解码后的误差。仿真与实体机器人测试则评估加速执行是否保持任务成功率，同时考察完成时间与运动平滑性。

<a id="S2086"></a>
**Source:** p.115 S2086

**Original:** During the remaining prediction delay, the robot must continue executing actions. The following subsection describes how training-time RTC conditions new predictions on actions already committed for execution, supporting continuity between action chunks.

**中文:** 在剩余的预测延迟期间，机器人必须继续执行动作。下一小节说明训练时 RTC 如何将新的预测条件化于已确定用于执行的动作之上，从而支持动作块之间的连续性。


<a id="H64"></a>
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

<a id="C088"></a>
**Source:** p.116 C088 · 表 T028

![T028](assets/T028.png)

**Original (caption):** Table 28: Evaluation of a simple noisy-prefix RTC extension under simulated inference latency. Success and progress use 1,200 matched episodes per condition, while jerk uses 120 matched diagnostic layouts. Jerk changes are relative to async execution of the noisy-prefix fine-tuned checkpoint at the same delay. Negative changes indicate lower jerk. Bold values indicate the best result within each delay setting.

**中文表注：** Table 28：在仿真推理时延下对简单含噪前缀 RTC 扩展的评测。成功率与进度各使用每种条件下 1,200 个匹配回合，而加加速度（jerk）使用 120 个匹配诊断布局。jerk 的变化相对于同一延迟下含噪前缀微调检查点的异步执行计算。负值表示 jerk 更低。加粗数值表示每种延迟设置内的最佳结果。

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

<a id="H65"></a>
### I.3. Accelerating Task Throughput Beyond Demonstrations ｜ 超越演示的任务吞吐加速

<a id="S2100"></a>
**Source:** p.116 S2100

**Original:** We leverage an agentic task-throughput acceleration algorithm to enable GR00T 2 to complete tasks with higher task-completion throughput than the demonstration dataset. We decompose overall task execution into semantically meaningful phases, such as reaching, grasping, transporting, and screwing, which differ in their sensitivity to acceleration. An agent searches for a speed schedule over these phases by evaluating accelerated rollouts and refining the speed schedule based on observed failures. At deployment, a lightweight observationconditioned future subtask predictor predicts a sequence of future phases aligned with GR00T 2’s action-chunk horizon. Given the action chunk, predicted phases and a speed schedule, a trajectory transformation function produces a new action chunk for execution (see Fig 20). We train the predictor using temporally aligned phase annotations generated by an agent.

**中文:** 我们采用一种智能体化任务吞吐加速算法，使 GR00T 2 能以高于演示数据集的任务完成吞吐量完成任务。我们将整体任务执行分解为语义上有意义的阶段，例如抵达、抓取、搬运和拧螺丝，这些阶段对加速的敏感程度各不相同。智能体通过评估加速后的 rollout（轨迹采样），并根据观测到的失败修正速度调度方案，在这些阶段上搜索速度调度方案。部署时，一个轻量的、以观测为条件的未来子任务预测器会预测一串未来阶段，并与 GR00T 2 的动作块时域对齐。给定动作块、预测阶段和速度调度方案后，轨迹变换函数会生成一个新的动作块用于执行（见 Fig 20）。我们使用由智能体生成的、时间对齐的阶段标注来训练该预测器。

<a id="S2101"></a>
**Source:** p.117 S2101

**Original:** Evaluation Tasks. We showcase GR00T 2-Accelerated across three tasks on the Tianji Sharpa robot from the Dexter post-training benchmark task (see Section A.1). We report task progress scores, success rates and mean completion times of successful episodes in Table 29. Our experiments indicate that GR00T 2-Accelerated consistently decreases task completion times while preserving success rates across the evaluated long-horizon dexterous tasks.

**中文:** 评测任务。我们在 Dexter 后训练基准任务（见 Section A.1）中的 Tianji Sharpa 机器人上，展示了 GR00T 2-Accelerated 在三个任务上的表现。Table 29 报告了任务进度分数、成功率以及成功回合的平均完成时间。我们的实验表明，在所评测的长时序灵巧任务上，GR00T 2-Accelerated 持续缩短任务完成时间，同时保持成功率。

<a id="C089"></a>
**Source:** p.117 C089 · 表 T029

![T029](assets/T029.png)

**Original (caption):** Table 29: Task success rate and completion time on Dexter post-training tasks. Completion time is averaged over successful trials only.

**中文表注：** Table 29：Dexter 后训练任务上的任务成功率与完成时间。完成时间仅对成功的试次取平均。

<a id="C090"></a>
**Source:** p.118 C090 · 图 F061

![F061](assets/F061.png)

**Original (caption):** Figure 61: Subset of environments for Real-to-Sim Evaluation. Side-by-side of real-world tasks that are used to evaluate generalist capabilities of GR00T 2 and their simulation counterparts. Odd columns are the simulation environments and even columns are frames from the real-world robot workcell. Each task is evaluated five times in the real-world and ten times in simulation per checkpoint, with the results used to calculate the correlations between performance in simulation and the real-world.

**中文图注：** Figure 61：用于现实到仿真评测的环境子集。并排展示了用于评测 GR00T 2 通用能力的真实世界任务及其仿真对应物。奇数列为仿真环境，偶数列为真实机器人工作单元中的帧画面。每个任务在每个检查点上于真实世界中评测五次、于仿真中评测十次，结果用于计算仿真表现与真实世界表现之间的相关性。

<a id="H66"></a>
### J. Simulations ｜ 仿真

<a id="S2116"></a>
**Source:** p.118 S2116

**Original:** In this section, we outline how simulation contributed to GR00T 2. We developed a real-to-sim workflow that recreates high-fidelity digital twins of real-world tasks used for evaluating GR00T 2 (Sec. J.1). Policy evaluations in these high-fidelity digital twins proved to have strong correlations with real-world evaluations, allowing them to accelerate GR00T 2 development (Sec. J.2). Finally, we showcase GR00T 2’s capabilities on standardized simulation environments, establishing new state-of-the-art results on several of the latest benchmarks (Sec. J.3).

**中文:** 本节概述仿真如何服务于 GR00T 2 的研发。我们开发了一套现实到仿真（real-to-sim）工作流，用于重建 GR00T 2 评测所用真实世界任务的高保真数字孪生（Sec. J.1）。事实证明，在这些高保真数字孪生中进行的策略评测与真实世界评测之间具有很强的相关性，从而使它们能够加速 GR00T 2 的开发（Sec. J.2）。最后，我们在标准化仿真环境中展示了 GR00T 2 的能力，并在若干最新基准测试上取得了新的最优结果（Sec. J.3）。

<a id="H67"></a>
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


<a id="H68"></a>
### J.2. Accelerating GR00T 2 Development with Simulation ｜ 借助仿真加速 GR00T 2 开发

<a id="S2125"></a>
**Source:** p.119 S2125

**Original:** Once generated, the simulation environments can be used for many different applications. We first quantify the utility of our simulation suite by comparing the outcomes of GR00T 2 policy evaluations in sim and in real (Sec. J.2.1). We then highlight how these high-fidelity environments contributed to GR00T 2 development, including: optimization of GR00T 2 inference for deployment (Sec. J.2.2), faster iteration on the GR00T 2 pretraining process (Sec. J.2.3), and the development of agentic recovery skills in simulation that assist GR00T 2 during real-world deployment (Sec. J.2.4).

**中文:** 仿真环境生成之后，可以用于许多不同的应用。我们首先通过比较 GR00T 2 策略在仿真与真实环境中的评测结果，量化仿真套件的效用（Sec. J.2.1）。随后，我们说明这些高保真环境如何助力 GR00T 2 的开发，包括：面向部署的 GR00T 2 推理优化（Sec. J.2.2）、加快 GR00T 2 预训练过程的迭代（Sec. J.2.3），以及在仿真中开发智能体化恢复技能，以在真实部署中辅助 GR00T 2（Sec. J.2.4）。

<a id="C091"></a>
**Source:** p.120 C091 · 图 F062

![F062](assets/F062.png)

**Original (caption):** Figure 62: Reconstructed assembly tasks. Toy plane, Hot Wheels car, and toy tractor (left to right), shown in reset configurations (top) and assembled configurations (bottom). Camera and scale are held fixed within each column. The panels illustrate asset configurations rather than robot-policy success.

**中文图注：** Figure 62：重建的装配任务。玩具飞机、Hot Wheels 小车和玩具拖拉机（从左到右），分别展示复位配置（上排）和装配完成配置（下排）。每一列内相机与比例尺保持固定。各面板展示的是资产配置，而非机器人策略的成功率。

<a id="C092"></a>
**Source:** p.120 C092 · 图 F063

![F063](assets/F063.png)

**Original (caption):** Figure 63: From physical objects to sim-ready assets. Source photograph, input scan, reconstructed visual asset, handling collision hulls (purple), and fitting signed-distance-field (SDF) source surfaces (teal) for the same tractor body, from left to right. Circular close-ups compare the same wheel shaft: a coarse solid handling shape and the fitting bore with reconstructed thread geometry.

**中文图注：** Figure 63：从物理物体到仿真就绪资产。从左到右依次为同一拖拉机车身的原始照片、输入扫描、重建的视觉资产、用于处理的碰撞外壳（紫色），以及用于拟合的有符号距离场（SDF）源表面（青色）。圆形特写对比同一根车轮轴：左侧为粗略的实体处理形状，右侧为拟合用的孔，并带有重建的螺纹几何。

<a id="S2127"></a>
**Source:** p.120 S2127

**Original:** J.2.1. Sim and Real Policy Evaluation Correlation Analysis

**中文:** J.2.1. 仿真与真实策略评测的相关性分析

<a id="S2128"></a>
**Source:** p.120 S2128

**Original:** In order for our simulation suite to be useful, it is important for simulation to be calibrated with the real world. In this section, we gauge our simulation quality by seeing if it can be used as convincing surrogate for real world evaluation (Ranawaka et al., 2026; Jain et al., 2025). We test our policies zero-shot in simulation, without additional fine-tuning or co-training with simulation data, and find that the simulation evaluations strongly correlate with real-world results. This enables the testing of policies at a scale, cadence, and level of reproducibility that would be intractable for real-world evals.

**中文:** 要让仿真套件真正有用，仿真就必须与真实世界相互校准。本节通过判断仿真能否作为真实世界评测的可信替代手段，来衡量仿真质量（Ranawaka et al., 2026; Jain et al., 2025）。我们在仿真中以零样本方式测试策略，不做额外微调，也不与仿真数据联合训练，结果发现仿真评测与真实世界结果高度相关。这使得策略测试能够达到真实世界评测难以企及的规模、节奏和可复现性水平。

<a id="S2129"></a>
**Source:** p.120 S2129

**Original:** Setup. We evaluate 14 checkpoints in both simulation and the real world on matched setups across 25 tasks on the YAM embodiment. Additionally, we evaluate 10 tasks on the DROID (Khazatsky et al., 2024) embodiment with 5 generalist checkpoints. Each task is evaluated for 5 trials on the real robots, and 10 trials in simulation.

**中文:** 设置。我们在 YAM 本体上，以匹配的设置，在仿真与真实世界中分别评测了 14 个检查点，涵盖 25 项任务。此外，我们在 DROID（Khazatsky et al., 2024）本体上用 5 个通用检查点评测了 10 项任务。每项任务在真实机器人上评测 5 次试次，在仿真中评测 10 次试次。

<a id="S2130"></a>
**Source:** p.120 S2130

**Original:** Metrics. We measure sim and real correlation using Pearson Correlation Coefficient (r), Spearman Rank Correlation Coefficient (𝜌) and the Mean Maximum Rank Violation (MMRV) proposed by Li et al. (2024). For a simulation that perfectly reflects real-world conditions, we would observe 𝑟→1, indicating that policy performance in simulation matches that in the real world, 𝜌→1, indicating that the relative rankings of policies are maintained between simulation and the real world, and MMRV →0, indicating that the number of policy ranking violations are minimized. These correlations are calculated for task progress, success rate and the

**中文:** 指标。我们使用 Pearson 相关系数（Pearson Correlation Coefficient, r）、Spearman 秩相关系数（𝜌），以及 Li et al. (2024) 提出的平均最大秩违例（MMRV）来衡量仿真与真实世界之间的相关性。对于完全反映真实世界条件的仿真，我们应观察到 𝑟→1，表明仿真中的策略表现与真实世界一致；𝜌→1，表明策略的相对排序在仿真与真实世界之间得以保持；MMRV →0，表明策略排序违例的数量被最小化。这些相关性分别针对任务进度、成功率以及 [公式原文见 p.120]

<a id="C093"></a>
**Source:** p.121 C093 · 图 F064

![F064](assets/F064.png)

**Original (caption):** Figure 64: Robot assembly of the toy plane. Wing insertion, reorientation, and fastening with a power drill, shown from left to right during a single continuous demonstration-guided execution.

**中文图注：** Figure 64：玩具飞机的机器人装配。在一次连续的、由演示引导的执行过程中，从左到右依次展示机翼插入、调整朝向，以及使用电动钻紧固。

<a id="C094"></a>
**Source:** p.121 C094 · 图 F065

![F065](assets/F065.png)

**Original (caption):** Figure 65: Sim-real Pearson correlation per policy for three computed metrics, compared with the noise ceiling: the correlation a perfect simulator would reach given the same number of real and simulated trials.

**中文图注：** Figure 65：每个策略在三项计算指标上的仿真-现实 Pearson 相关性，并与噪声上限进行比较。噪声上限是指在真实试次数与仿真试次数相同的情况下，完美仿真器所能达到的相关性。

<a id="S2142"></a>
**Source:** p.121 S2142

**Original:** Bradley-Terry (BT) (Bradley and Terry, 1952) Elo ratings of the checkpoints. Task progress is the rubric score of a trial, a weighted sum of the completed sub-tasks between 0 and 1, and a trial is successful when the score is 1. Both are averaged within each task and then across tasks. MMRV is reported for task progress and success rate.

**中文:** 检查点的 Bradley-Terry（BT）（Bradley and Terry, 1952）Elo 评分。任务进度是某次试次的评分表（rubric）得分，即已完成子任务的加权和，取值在 0 到 1 之间；当得分为 1 时，该试次判定为成功。两者先在每项任务内取平均，再在所有任务之间取平均。MMRV 针对任务进度和成功率进行报告。

<a id="S2143"></a>
**Source:** p.121 S2143

**Original:** Bradley-Terry Elo. Real-world evaluations use blinded A/B tests: in each trial, two or three checkpoints run in randomized order from the same initial setup (based on a corresponding simulation initialization), and every pair of checkpoints in the trial forms one comparison, won by the higher score (equal scores count as a tie). We fit BT ratings to these pairwise outcomes. In simulation, every checkpoint is evaluated on the same fixed initial layouts (10 per task), so any two checkpoints can be compared layout by layout without re-running them.

**中文:** Bradley-Terry Elo。真实世界评测采用盲法 A/B 测试：在每次试次中，两个或三个检查点以随机顺序，从同一初始设置（基于对应的仿真初始化）出发运行；该试次中每一对检查点构成一次比较，得分较高者获胜（得分相同计为平局）。我们将 BT 评分拟合到这些成对结果上。在仿真中，每个检查点都在相同的固定初始布局（每项任务 10 个）上评测，因此任意两个检查点都可以逐布局比较，而无需重新运行。

<a id="S2144"></a>
**Source:** p.121 S2144

**Original:** Results on YAM embodiment. We evaluate 14 GR00T 2 variants across 25 YAM tasks in the same simulator. We completed real-world trials with the A/B evaluation procedure defined earlier. For each trial, we aligned the object initialization with the simulation using projected overlays. We find that our simulator predicts policy performance with high correlations with the real world, with a Pearson 𝑟up to 0.93 for task progress and BT Elo score. Since evaluations in both the real world and simulation can be non-deterministic, and the number of trials per task is limited, there is an effective statistical ceiling to how high these correlations can be for even a perfect simulator. Following Lage-Castellanos et al. (2019), we estimate this ceiling by assuming a perfect simulator. For checkpoint 𝑐on task 𝑡, let ˆ𝑝𝑐𝑡= 𝑠𝑐𝑡/𝑛𝑐𝑡be its real-world success rate (𝑠𝑐𝑡successes in 𝑛𝑐𝑡trials), which we treat as its true success probability. In each repetition, we generate two independent evaluations from these true values, one standing in for the real robot and one for a perfect simulator, each with 𝑛𝑐𝑡trials:

**中文:** YAM 本体上的结果。我们在同一仿真器中，于 25 项 YAM 任务上评测了 14 个 GR00T 2 变体。真实世界试次按照前文定义的 A/B 评测流程完成。对于每次试次，我们利用投影叠加图，使物体初始化与仿真保持对齐。我们发现，仿真器能够以较高相关性预测真实世界中的策略表现，任务进度与 BT Elo 评分的 Pearson 𝑟 最高可达 0.93。由于真实世界与仿真中的评测都可能是非确定性的，且每项任务的试次数有限，即使是完美的仿真器，这些相关性也存在一个有效的统计上限。沿用 Lage-Castellanos et al. (2019) 的做法，我们假设存在一个完美仿真器来估计该上限。对于任务 𝑡 上的检查点 𝑐，令 ˆ𝑝𝑐𝑡= 𝑠𝑐𝑡/𝑛𝑐𝑡 为其真实世界成功率（在 𝑛𝑐𝑡 次试次中有 𝑠𝑐𝑡 次成功），并将其视为真实成功概率。在每次重复中，我们依据这些真实值生成两组独立评测，一组代表真实机器人，另一组代表完美仿真器，每组各含 𝑛𝑐𝑡 次试次：[公式原文见 p.121]

<a id="S2158"></a>
**Source:** p.121 S2158

**Original:** where 𝑇𝑐is the number of tasks for checkpoint 𝑐and the two binomial draws are independent. This gives one real and one perfect-simulator score per checkpoint, and we compute the Pearson correlation ˜𝑟= corr(˜x, ˜y)

**中文:** 其中 𝑇𝑐 为检查点 𝑐 的任务数，两次二项抽样相互独立。由此，每个检查点各得到一个真实得分和一个完美仿真器得分，并计算 Pearson 相关系数 ˜𝑟= corr(˜x, ˜y)。[公式原文见 p.121]

<a id="C095"></a>
**Source:** p.122 C095 · 图 F066

![F066](assets/F066.png)

**Original (caption):** Figure 66: Simulated vs. real-world performance per policy on DROID. We evaluate 5 generalist checkpoints on the DROID embodiment across 10 tasks, with 5 real-world and 10 simulated trials per task, on the same layouts for every checkpoint. Panels and metrics as in Fig. 18: (a) task progress and (b) success rate averaged over tasks (dashed: 𝑦= 𝑥), and (c) Bradley-Terry Elo (dashed: least-squares fit).

**中文图注：** Figure 66：DROID 上每个策略的仿真与真实世界表现对比。我们在 DROID 本体上用 5 个通用检查点评测了 10 项任务，每项任务进行 5 次真实试次和 10 次仿真试次，且每个检查点使用相同布局。面板与指标同 Fig. 18：(a) 任务进度与 (b) 成功率（对任务取平均；虚线：𝑦= 𝑥），以及 (c) Bradley-Terry Elo（虚线：最小二乘拟合）。[公式原文见 p.122]

<a id="S2190"></a>
**Source:** p.122 S2190

**Original:** across the 14 checkpoints. Since ˜x and ˜y share the same true values, they differ only because of the limited number of trials, so the median of ˜𝑟over 1,000 repetitions is the expected correlation any simulator could achieve with this evaluation budget. As shown in Fig. 65, our simulator produces correlations that are within 95% −99% of this ceiling.

**中文:** 跨 14 个检查点。由于 ˜x 与 ˜y 具有相同的真实值，二者之间的差异仅来自有限的试次数，因此 1,000 次重复中 ˜𝑟 的中位数，就是在该评测预算下任何仿真器都可能达到的期望相关性。如 Fig. 65 所示，我们的仿真器所得相关性处于该上限的 95% −99% 之内。[公式原文见 p.122]

<a id="S2191"></a>
**Source:** p.122 S2191

**Original:** Results on DROID embodiment. Separately, we evaluate five generalist DROID checkpoints including GR00T 2 and publicly available models on environments reconstructed from real-world DROID setups. We use the same five layouts per task for each checkpoint in the real-world and the same ten layouts in simulation, to minimize variation in trial initializations. Once again, we see high Pearson r of 0.98, 0.95, 0.97 for task progress, success rate and BT Elo respectively. This demonstrates that our agentic real-to-sim reconstruction method is viable for different embodiments.

**中文:** DROID 本体上的结果。此外，我们在根据真实世界 DROID 装置重建的环境中，评测了五个通用 DROID 检查点，包括 GR00T 2 和若干公开可用模型。为尽量减少试次初始化带来的差异，每个检查点在真实世界中使用每项任务相同的五种布局，在仿真中使用相同的十种布局。我们再次观察到较高的 Pearson r：任务进度、成功率和 BT Elo 分别为 0.98、0.95 和 0.97。这表明我们的智能体化现实到仿真重建方法适用于不同本体。

<a id="S2192"></a>
**Source:** p.122 S2192

**Original:** J.2.2. GR00T 2 Inference Optimization through Simulation

**中文:** J.2.2. 借助仿真优化 GR00T 2 推理

<a id="S2193"></a>
**Source:** p.122 S2193

**Original:** Inference optimization aims to help GR00T 2 respond sooner to new observations while preserving task success and smooth motion. We optimize model execution and the processing and transfer of observations, and vary the number of steps used to refine video and action predictions (see Accelerating Model Inference). Simulation provides a repeatable setting for testing how these changes affect behavior. We can restart each trial from the same scene without repeatedly setting up a physical workcell, making it practical to screen settings before robot testing.

**中文:** 推理优化的目标，是让 GR00T 2 在保持任务成功率和动作平滑性的同时，更快地响应新的观测。我们优化模型执行，以及观测的处理与传输，并改变用于细化视频与动作预测的步数（参见 Accelerating Model Inference）。仿真为测试这些改动如何影响行为提供了可重复的环境。我们可以从同一场景重新开始每次试次，而无需反复搭建物理工作单元（workcell），因此在机器人测试之前筛选设置是切实可行的。

<a id="S2194"></a>
**Source:** p.122 S2194

**Original:** Changes that reduce prediction time can also change action predictions, so task success and motion quality must be checked together. For each checkpoint, we keep the number of actions per prediction fixed while comparing original PyTorch execution with TensorRT and CUDA Graphs and testing different numbers of refinement steps. In a YAM cube-handover pilot, several settings completed the task but differed in motion smoothness. Follow-up trials of the same checkpoint and task on a physical YAM robot also showed this distinction. In separate runtime comparisons, the optimized implementation supported more frequent updates to the action plan with comparable task progress in simulation.

**中文:** 缩短预测时间的改动也可能改变动作预测，因此必须同时检验任务成功率与动作质量。对于每个检查点，我们在保持每次预测的动作数不变的前提下，比较原始 PyTorch 执行与 TensorRT 和 CUDA Graphs，并测试不同数量的细化步数。在 YAM 方块交接（cube-handover）先导实验中，若干设置都完成了任务，但在动作平滑性上存在差异。同一检查点和任务在物理 YAM 机器人上的后续试次也显示了这一差异。在单独的运行时对比中，经过优化的实现支持更频繁地更新动作计划，同时在仿真中保持了相当的任务进度。

<a id="S2195"></a>
**Source:** p.122 S2195

**Original:** Simulation also helps us prototype real-time chunking (RTC), which connects new action predictions to actions already scheduled for execution. In separate simulation experiments (see Policy Smoothness), we compare RTC training with and without noise added to the previous action sequence. Repeated trials from matched scenes with controlled prediction delays help us assess whether smoother transitions between action sequences preserve task success, without testing every delay setting on physical robots.

**中文:** 仿真同样有助于我们原型化实时分块（RTC），它将新的动作预测与已排定执行的动作衔接起来。在单独的仿真实验中（参见 Policy Smoothness），我们比较了在先前动作序列上加入噪声与不加噪声两种情形下的 RTC 训练。来自匹配场景、且预测延迟可控的重复试次，帮助我们评估动作序列之间更平滑的过渡是否能保持任务成功率，而无需在物理机器人上测试每一种延迟设置。

<a id="S2197"></a>
**Source:** p.123 S2197

**Original:** We measure prediction latency directly on the target hardware, separately from simulated task duration. Ordinary synchronous simulation pauses while waiting for predictions, so it does not reproduce the effect of inference delay on a moving robot. The RTC experiments explicitly model this delay, but physical-robot tests remain necessary to check behavior under actual deployment timing. Simulation narrows the settings taken to these tests, where we assess task success and motion quality on the target robot.

**中文:** 我们直接在目标硬件上测量预测时延，并与仿真中的任务时长分开计算。普通的同步仿真会在等待预测期间暂停，因此无法复现推理延迟对运动中机器人的影响。RTC 实验显式地建模了这一延迟，但物理机器人测试对于检验实际部署时序下的行为仍然必不可少。仿真将进入这些测试的设置范围缩小，而这些测试用于在目标机器人上评估任务成功率与动作质量。

<a id="S2198"></a>
**Source:** p.123 S2198

**Original:** J.2.3. GR00T 2 Pretraining Acceleration with Simulation

**中文:** J.2.3. 借助仿真加速 GR00T 2 预训练

<a id="S2199"></a>
**Source:** p.123 S2199

**Original:** Simulation enabled faster iteration on GR00T 2 pretraining through many different means.

**中文:** 仿真通过多种途径，加快了 GR00T 2 预训练的迭代。

<a id="S2200"></a>
**Source:** p.123 S2200

**Original:** Monitoring of pretraining progress and checkpoint selection. Evaluating a single pretraining checkpoint across a large set of real-world tasks can take hours. Simulation provides a faster way to compare policies across a diverse task set during model development. During GR00T 2 pretraining, we evaluated intermediate checkpoints on a set of tasks from our simulation suite to inspect their closed-loop behavior and compare model capabilities as training progressed. These comparisons help us identify overfitting as we iterate on the model, and assess the relative performance of our checkpoints and external baselines without running extensive real-world evaluations for every candidate.

**中文:** 预训练进度监控与检查点选择。在大量真实世界任务上评估单个预训练检查点，可能需要数小时。仿真提供了一种更快的方式，可在模型开发过程中，于多样化的任务集上比较策略。在 GR00T 2 预训练期间，我们在仿真套件的一组任务上评估了中间检查点，以考察其闭环行为，并随训练推进比较模型能力。这些比较帮助我们在迭代模型时识别过拟合，并评估我们的检查点与外部基线的相对表现，而无需对每个候选模型都进行大规模的真实世界评测。

<a id="S2201"></a>
**Source:** p.123 S2201

**Original:** Simulation also guided checkpoint selection: we used a subset of our simulation suite (25 tasks) to determine which checkpoints showed promising closed-loop evaluation results. This provided a stable way to understand if checkpoints were worth physical robot evaluation. As a concrete example, we used this workflow to finalize our pretrained model: simulation results narrowed the candidates to three checkpoints, which we then evaluated on physical robots to select the final checkpoint. In this way, simulation was a tool to guide checkpoint analysis and development, but we still used physical-robot evaluation to validate conclusions about real-world performance.

**中文:** 仿真还指导了检查点选择：我们使用仿真套件中的一个子集（25 项任务），来判断哪些检查点在闭环评测中表现出良好前景。这为判断某个检查点是否值得进行物理机器人评测，提供了稳定的依据。作为具体例子，我们借助该流程确定了预训练模型的最终版本：仿真结果将候选检查点缩小到三个，随后我们在物理机器人上对它们进行评估，以选出最终检查点。由此，仿真是引导检查点分析与开发的工具，但我们仍以物理机器人评测来验证关于真实世界表现的结论。

<a id="S2202"></a>
**Source:** p.123 S2202

**Original:** Optimizing the data pipeline. Changes to the data loading and processing pipeline are costly to assess through full-scale pretraining. We expect a new pipeline that processes the data correctly and preserves training dynamics to produce model performance comparable to the existing pipeline. We test this expectation with small-scale training and closed-loop simulation before adopting a new pipeline for pretraining.

**中文:** 优化数据流水线。对数据加载与处理流水线的改动，若要通过全规模预训练来评估，代价高昂。我们预期，一条能够正确处理数据并保持训练动态的新流水线，将产生与现有流水线相当的模型性能。在将新流水线用于预训练之前，我们先通过小规模训练和闭环仿真对这一预期进行检验。

<a id="S2203"></a>
**Source:** p.123 S2203

**Original:** As an example, we compared five configurations that varied sequence packing, mixed-shard sampling, and text-token masking. For each configuration, we post-trained a model on real-robot teleoperation data from the YAM Scoop and Unscrew tasks, then evaluated it on simulated versions of those tasks. Simulation was used only for evaluation. The new data loading pipeline showed no observed regression in closed-loop simulation performance relative to the existing pipeline, giving us confidence to adopt it for pretraining.

**中文:** 举例来说，我们比较了五种配置，它们在序列打包（sequence packing）、混合分片采样（mixed-shard sampling）和文本 token 掩码（text-token masking）方面各有不同。对每种配置，我们都在 YAM Scoop 和 Unscrew 任务的真实机器人遥操作数据上进行后训练，随后在这些任务的仿真版本上进行评估。仿真仅用于评估。相对于现有流水线，新的数据加载流水线在闭环仿真性能上未观察到退化，这让我们有信心将其用于预训练。

<a id="S2204"></a>
**Source:** p.123 S2204

**Original:** J.2.4. Agentic Skill Development in Simulation

**中文:** J.2.4. 在仿真中开发智能体化技能

<a id="S2205"></a>
**Source:** p.123 S2205

**Original:** Simulation also helps us develop specialized manipulation skills. As described in Sec. G.1, ASPIRE learns skills that code-as-policy (CaP) can invoke alongside GR00T 2 to carry out difficult steps or recover from failures. For example, the toy plane assembly task (Fig. 64) provided a repeatable setting for developing recovery skills that transferred to physical robots. In simulation, we could test candidate behaviors, inspect failures, and refine the skills before evaluating them on the physical system.

**中文:** 仿真同样帮助我们开发专门的操作技能。如 Sec. G.1 所述，ASPIRE 学习的技能可以与 GR00T 2 一同，由代码即策略（code-as-policy, CaP）调用，用于完成困难步骤或从故障中恢复。例如，玩具飞机装配任务（Fig. 64）提供了一个可重复的环境，用于开发能够迁移到物理机器人上的恢复技能。在仿真中，我们可以测试候选行为、检查故障，并在将技能用于实体系统之前加以改进。


<a id="H69"></a>
### J.3. Simulation Benchmarking ｜ 仿真基准测试

<a id="S2206"></a>
**Source:** p.123 S2206

**Original:** We evaluate GR00T 2 on five simulation benchmarks that span single-arm mobile manipulation (RoboCasa365), bimanual manipulation (RoboDojo), zero-shot real-to-sim tabletop manipulation (RoboLab, MolmoSpaces) and humanoid loco-manipulation (G1 Factory). Unless stated otherwise, each GR00T 2 result is a single post-trained checkpoint initialized from the same pretrained GR00T 2 model, evaluated with the benchmark’s official task set, episode budget and success criterion. Among VLA and WAM policies on the public leaderboards,4 GR00T 2

**中文:** 我们在五个仿真基准上评测 GR00T 2，它们分别覆盖单臂移动操作（RoboCasa365）、双臂操作（RoboDojo）、零样本现实到仿真的桌面操作（RoboLab、MolmoSpaces）以及人形机器人移动操作（loco-manipulation，G1 Factory）。除非另有说明，每个 GR00T 2 结果都来自同一个预训练 GR00T 2 模型初始化后得到的单一后训练检查点，并按照基准官方任务集、回合预算和成功判定标准进行评测。在公开排行榜的 VLA 与 WAM 策略中，GR00T 2 [存疑：句子在此截断，原文后续内容未抽取]

<a id="S2207"></a>
**Source:** p.123 S2207

**Original:** 4Baselines are taken from the official leaderboards as of November 6, 2026 with the exception of GR00T 1.7 which we retrain and evaluate ourselves.

**中文:** 4 基线取自截至 2026 年 11 月 6 日的官方排行榜，GR00T 1.7 除外，该模型由我们自行重新训练和评测。

<a id="C096"></a>
**Source:** p.124 C096 · 表 T030

![T030](assets/T030.png)

**Original (caption):** Table 30: Results on the RoboCasa365 benchmark. We report success rate (%). The best and second-best results are highlighted in bold and underline, respectively.

**中文表注：** RoboCasa365 基准测试结果。报告成功率（%）。最优与次优结果分别以粗体和下划线标出。

<a id="S2209"></a>
**Source:** p.124 S2209

**Original:** 𝜋0.5 (Physical Intelligence et al., 2025) 16.9 39.6 7.1 1.2 GR00T 1.7 (NVIDIA, 2026a) 22.1 41.7 17.7 4.4 Paimon-0 58.1 79.3 55.8 36.7 Axiom-0 (Shu et al., 2026) 61.6 86.5 59.4 35.8 Awomo-0.5V (Awomo-WAM Team, 2026) 62.5 85.0 60.4 39.4 minionx 62.6 81.8 60.0 43.6 Awomo-0.5I (Awomo-WAM Team, 2026) 64.4 86.5 58.8 45.2

**中文:** [存疑：表 30 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] 𝜋0.5 (Physical Intelligence et al., 2025) 16.9 39.6 7.1 1.2 GR00T 1.7 (NVIDIA, 2026a) 22.1 41.7 17.7 4.4 Paimon-0 58.1 79.3 55.8 36.7 Axiom-0 (Shu et al., 2026) 61.6 86.5 59.4 35.8 Awomo-0.5V (Awomo-WAM Team, 2026) 62.5 85.0 60.4 39.4 minionx 62.6 81.8 60.0 43.6 Awomo-0.5I (Awomo-WAM Team, 2026) 64.4 86.5 58.8 45.2

<a id="C097"></a>
**Source:** p.124 C097 · 表 T031

![T031](assets/T031.png)

**Original (caption):** Table 31: Results on the RoboDojo benchmark. Dimension columns report success rate (%), while the last two columns report the average score and success rate (%). GR00T 2 is evaluated on all three layout banks. Tab. 19 reports layout bank 0 only, for all four GR00T 2 configurations including RL and agentic execution. The best and second-best results are highlighted in bold and underline, respectively.

**中文表注：** RoboDojo 基准测试结果。各维度列报告成功率（%），最后两列分别报告平均得分和成功率（%）。GR00T 2 在全部三个布局库（layout bank）上评测。Tab. 19 仅报告布局库 0 的结果，涵盖 GR00T 2 的全部四种配置，包括强化学习（RL）和智能体化执行的配置。最优与次优结果分别以粗体和下划线标出。

<a id="S2214"></a>
**Source:** p.124 S2214

**Original:** GR00T 1.7 (NVIDIA, 2026a) 4.1 1.1 11.8 2.6 1.4 7.65 4.20 𝜋0.5 (Physical Intelligence et al., 2025) 8.2 5.5 14.7 4.7 1.7 11.44 6.93 Rex-M1 Preview 26.1 23.8 33.0 48.2 6.1 33.79 27.44 Simate-beta 28.0 26.9 43.4 33.0 8.5 33.95 27.96 Awomo-0.5 (Awomo-WAM Team, 2026) 23.8 33.5 26.8 41.2 22.9 35.34 29.64 VPP2 (Guo et al., 2026) 29.5 35.2 37.0 55.6 4.1 39.26 32.26 WALL-OSS-1.0-lite 37.9 29.1 32.3 56.0 19.6 42.59 34.97

**中文:** [存疑：表 31 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] GR00T 1.7 (NVIDIA, 2026a) 4.1 1.1 11.8 2.6 1.4 7.65 4.20 𝜋0.5 (Physical Intelligence et al., 2025) 8.2 5.5 14.7 4.7 1.7 11.44 6.93 Rex-M1 Preview 26.1 23.8 33.0 48.2 6.1 33.79 27.44 Simate-beta 28.0 26.9 43.4 33.0 8.5 33.95 27.96 Awomo-0.5 (Awomo-WAM Team, 2026) 23.8 33.5 26.8 41.2 22.9 35.34 29.64 VPP2 (Guo et al., 2026) 29.5 35.2 37.0 55.6 4.1 39.26 32.26 WALL-OSS-1.0-lite 37.9 29.1 32.3 56.0 19.6 42.59 34.97

<a id="S2217"></a>
**Source:** p.124 S2217

**Original:** RoboCasa365. RoboCasa365 (Nasiriany et al., 2026) is a large-scale household simulation benchmark with 365 tasks across 2,500 procedurally generated kitchens, in which a mobile manipulator acts from three RGB cameras. Following the official multi-task protocol, we train on the Human300 pretraining mixture and evaluate on 50 target tasks split into 18 Atomic-Seen, 16 Composite-Seen and 16 Composite-Unseen tasks. The last split is absent from training and therefore tests zero-shot composition of learned skills. The overall score is the mean of the 50 per-task success rates. Results are shown in Tab. 30.

**中文:** RoboCasa365（Nasiriany et al., 2026）是一个大规模家庭仿真基准，包含 365 个任务，分布在 2,500 个程序化生成的厨房中，移动操作机器人的动作决策依据三台 RGB 相机的图像。遵循官方多任务协议，我们在 Human300 预训练数据配比上训练，并在 50 个目标任务上评测。这些目标任务分为 18 个 Atomic-Seen、16 个 Composite-Seen 和 16 个 Composite-Unseen 任务。最后一个划分从未出现在训练中，因此用于检验已学技能的零样本组合能力。总分为 50 个任务各自成功率的平均值。结果见 Tab. 30。

<a id="S2218"></a>
**Source:** p.124 S2218

**Original:** GR00T 2 reaches 67.2% average success, 2.8 percentage points above the best prior entry, and it leads on the Atomic-Seen and Composite-Seen splits. Notably, its largest margin is on the Composite-Seen tasks, multi-step activities that chain several learned skills, where it reaches 73.6%, 13.2 points above the next entry (Awomo-0.5V, 60.4%).

**中文:** GR00T 2 的平均成功率达到 67.2%，比此前最优条目高 2.8 个百分点，并且在 Atomic-Seen 和 Composite-Seen 两个划分上领先。最显著的优势出现在 Composite-Seen 任务上，这类多步活动会串接多个已学技能。在这一划分上，GR00T 2 达到 73.6%，比次优条目（Awomo-0.5V，60.4%）高 13.2 个百分点。

<a id="S2219"></a>
**Source:** p.124 S2219

**Original:** RoboDojo. RoboDojo (Chen et al., 2026a) is a bimanual benchmark in Isaac Sim (NVIDIA, 2025) on the 14-DoF ARX-X5 platform, with 42 tasks grouped into five capability dimensions: Generalization (standard and randomized layouts), Precision, Long-Horizon (up to 1,900 control steps), Memory and Open (open-vocabulary instructions with no training demonstrations). Following the official protocol, we run the evaluation over all 42 tasks (54 task configurations) on three layout banks (6,300 episodes) and report the partial-progress score and success rate. Results are shown in Tab. 31.

**中文:** RoboDojo（Chen et al., 2026a）是一个在 Isaac Sim（NVIDIA，2025）中构建的双臂基准，运行在 14 自由度（DoF）的 ARX-X5 平台上，包含 42 个任务，分为五个能力维度：泛化（标准布局与随机布局）、精度、长时序（最多 1,900 个控制步）、记忆，以及开放（使用开放词汇指令且没有训练演示）。遵循官方协议，我们在三个布局库（共 6,300 个回合）上运行全部 42 个任务（共 54 种任务配置），并报告部分任务进度得分和成功率。结果见 Tab. 31。

<a id="C098"></a>
**Source:** p.125 C098 · 表 T032

![T032](assets/T032.png)

**Original (caption):** Table 32: Results on the RoboLab benchmark. We report success rate (%) overall and per difficulty tier. The best and second-best results are highlighted in bold and underline, respectively.

**中文表注：** RoboLab 基准测试结果。报告总体成功率（%）以及各难度等级的成功率。最优与次优结果分别以粗体和下划线标出。

<a id="S2222"></a>
**Source:** p.125 S2222

**Original:** GR00T 1.7 (NVIDIA, 2026a) 18.9 22.8 15.9 10.9 𝜋0.5 (Physical Intelligence et al., 2025) 28.0 29.7 31.5 13.5 Atomic-WAM (Shi et al., 2026) 39.6 44.4 40.5 19.4 HiDream-O1-Embodied 39.9 43.1 37.7 32.9 FLUX 3 Action (Black Forest Labs, 2026) 42.9 49.1 39.2 28.2 BiMind v0.5 49.2 51.6 52.6 32.4 Lakeside 51.0 57.6 44.1 42.4

**中文:** [存疑：表 32 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] GR00T 1.7 (NVIDIA, 2026a) 18.9 22.8 15.9 10.9 𝜋0.5 (Physical Intelligence et al., 2025) 28.0 29.7 31.5 13.5 Atomic-WAM (Shi et al., 2026) 39.6 44.4 40.5 19.4 HiDream-O1-Embodied 39.9 43.1 37.7 32.9 FLUX 3 Action (Black Forest Labs, 2026) 42.9 49.1 39.2 28.2 BiMind v0.5 49.2 51.6 52.6 32.4 Lakeside 51.0 57.6 44.1 42.4

<a id="C099"></a>
**Source:** p.125 C099 · 表 T033

![T033](assets/T033.png)

**Original (caption):** Table 33: Results on the MolmoSpaces benchmark. We report success rate (%). The best and second-best results are highlighted in bold and underline, respectively. Baselines: 𝜋0.5-DROID (Physical Intelligence et al., 2025), GR00T 1.7 (NVIDIA, 2026a), MolmoAct2 DROID (Fang et al., 2026), PRTS-Droid (Zhang et al., 2026), WALL-OSS-0.5 (Yu et al., 2026b), and Cosmos3-Nano-Policy (NVIDIA Cosmos Team, 2026).

**中文表注：** MolmoSpaces 基准测试结果。报告成功率（%）。最优与次优结果分别以粗体和下划线标出。基线包括：𝜋0.5-DROID (Physical Intelligence et al., 2025)、GR00T 1.7 (NVIDIA, 2026a)、MolmoAct2 DROID (Fang et al., 2026)、PRTS-Droid (Zhang et al., 2026)、WALL-OSS-0.5 (Yu et al., 2026b) 和 Cosmos3-Nano-Policy (NVIDIA Cosmos Team, 2026)。

<a id="S2228"></a>
**Source:** p.125 S2228

**Original:** 𝜋0.5-DROID 22.7 65.1 18.1 6.4 7.0 8.0 12.0 10.2 10.4 17.77 GR00T 1.7 11.9 68.0 35.3 11.7 12.5 7.8 9.4 12.9 11.6 20.12 MolmoAct2 DROID 11.7 71.3 43.4 20.5 21.9 11.1 15.6 18.5 19.3 25.92 PRTS-Droid 12.0 76.3 47.5 18.1 20.5 21.6 17.4 19.0 18.2 27.84 WALL-OSS-0.5 16.8 78.5 78.4 47.9 47.2 30.1 13.8 15.9 18.3 38.55 Cosmos3-Nano-Policy 32.0 79.1 66.5 32.3 32.2 25.7 26.0 22.9 34.3 39.00 ZoeInside-VLA 36.6 85.7 74.8 51.8 55.9 45.5 37.8 21.2 36.2 49.50

**中文:** [存疑：表 33 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] 𝜋0.5-DROID 22.7 65.1 18.1 6.4 7.0 8.0 12.0 10.2 10.4 17.77 GR00T 1.7 11.9 68.0 35.3 11.7 12.5 7.8 9.4 12.9 11.6 20.12 MolmoAct2 DROID 11.7 71.3 43.4 20.5 21.9 11.1 15.6 18.5 19.3 25.92 PRTS-Droid 12.0 76.3 47.5 18.1 20.5 21.6 17.4 19.0 18.2 27.84 WALL-OSS-0.5 16.8 78.5 78.4 47.9 47.2 30.1 13.8 15.9 18.3 38.55 Cosmos3-Nano-Policy 32.0 79.1 66.5 32.3 32.2 25.7 26.0 22.9 34.3 39.00 ZoeInside-VLA 36.6 85.7 74.8 51.8 55.9 45.5 37.8 21.2 36.2 49.50

<a id="S2229"></a>
**Source:** p.125 S2229

**Original:** GR00T 2 (Ours) 20.7 79.0 71.9 42.0 42.9 20.3 44.2 37.5 47.6 45.12 manipulation to coordinated bimanual control. On Precision it leads the strongest prior entry by 4.8 points in success rate (40.0% vs. 35.2%) and reaches the highest partial-progress score (47.7 vs. 43.0), meaning it advances further through fine-grained manipulation even when an episode does not finish.

**中文:** GR00T 2（Ours）20.7 79.0 71.9 42.0 42.9 20.3 44.2 37.5 47.6 45.12 [存疑：句首为 “manipulation to coordinated bimanual control.” 的片段，与前文断开，对应中文应为“……从单臂操作到协同双臂控制”，抽取未保留前文] 在 Precision 维度上，GR00T 2 的成功率比最强的既有条目高 4.8 个百分点（40.0% 对 35.2%），并达到最高的部分任务进度得分（47.7 对 43.0）。这说明即使某个回合没有完成，GR00T 2 也能在精细操作中推进得更远。

<a id="S2231"></a>
**Source:** p.125 S2231

**Original:** RoboLab. RoboLab (Yang et al., 2026) is a high-fidelity Isaac Lab benchmark of 120 tabletop tasks on the DROID (Khazatsky et al., 2024) Franka setup, grouped into 64 simple, 39 moderate and 17 complex tasks. Following the official protocol, we run 10 episodes per task (1,200 episodes) with the default instructions and report binary success rate. Our policy is post-trained only on real DROID data, so this evaluation is zero-shot real-to-sim transfer. Results are shown in Tab. 32.

**中文:** RoboLab（Yang et al., 2026）是一个高保真的 Isaac Lab 基准，包含 120 个桌面任务，基于 DROID（Khazatsky et al., 2024）的 Franka 平台设置，任务分为 64 个简单任务、39 个中等任务和 17 个复杂任务。遵循官方协议，我们每个任务运行 10 个回合（共 1,200 个回合），使用默认指令，并报告二值成功率。我们的策略仅在真实 DROID 数据上进行后训练，因此该评测属于零样本的现实到仿真迁移。结果见 Tab. 32。

<a id="S2232"></a>
**Source:** p.125 S2232

**Original:** GR00T 2 reaches 47.4% success, placing in the top three among non-agentic entries on the leaderboard. Since GR00T 2 is post-trained only on real-world DROID data, this result indicates GR00T 2’s robust zero-shot transfer to unseen simulated scenes and tasks.

**中文:** GR00T 2 达到 47.4% 的成功率，在排行榜的非智能体化条目中位列前三。由于 GR00T 2 仅在真实世界 DROID 数据上进行后训练，这一结果表明 GR00T 2 能够稳健地零样本迁移到未见过的仿真场景和任务。

<a id="S2233"></a>
**Source:** p.125 S2233

**Original:** MolmoSpaces. MolmoSpaces (Kim et al., 2026) evaluates a Franka DROID policy in procedurally generated MuJoCo houses populated with Objaverse (Deitke et al., 2023) objects. Following the leaderboard’s default view, we report success rate on nine suites: articulated Open and Close, four pick suites (Pick-v1.5 and Pick-v2 under the classic renderer, the filament renderer and randomized cameras) and three pick-and-place suites (plain, next-to and color-referred), 8,915 episodes in total. The overall score is the unweighted mean over the nine suites, with unsubmitted suites counted as zero. As with RoboLab, we evaluate the same real-DROID post-trained checkpoint zero-shot. Results are shown in Tab. 33.

**中文:** MolmoSpaces（Kim et al., 2026）在程序化生成的 MuJoCo 房屋中评测 Franka DROID 策略，房屋内放置了 Objaverse（Deitke et al., 2023）物体。遵循排行榜的默认视图，我们报告九个子套件上的成功率：可动关节的 Open 与 Close 子套件、四个抓取（pick）子套件（Pick-v1.5 和 Pick-v2 分别在经典渲染器、Filament 渲染器和随机相机条件下的测试），以及三个抓放（pick-and-place）子套件（普通型、近邻型和颜色指代型），共计 8,915 个回合。总分为九个子套件的未加权平均值，未提交结果的子套件按零计。与 RoboLab 相同，我们对同一个真实 DROID 后训练检查点进行零样本评测。结果见 Tab. 33。

<a id="S2235"></a>
**Source:** p.125 S2235

**Original:** GR00T 2 scores 45.12%, second only to ZoeInside-VLA (49.50%), and it has the best score on all three

**中文:** GR00T 2 得分为 45.12%，仅次于 ZoeInside-VLA（49.50%），并且在全部三个 [存疑：句子在此截断，原文后续内容未抽取]

<a id="C100"></a>
**Source:** p.126 C100 · 表 T034

![T034](assets/T034.png)

**Original (caption):** Table 34: Results on G1 Factory. We report success rate (%) over 100 episodes per task. The best results are highlighted in bold. Baseline: GR00T 1.7 (NVIDIA, 2026a).

**中文表注：** G1 Factory 结果。报告每个任务 100 个回合上的成功率（%）。最优结果以粗体标出。基线：GR00T 1.7 (NVIDIA, 2026a)。

<a id="S2243"></a>
**Source:** p.126 S2243

**Original:** pick-and-place suites (44.2%, 37.5% and 47.6% on v2, NextTo and Color). Notably, it leads the spatially referred NextTo suite by 14.6 points (37.5% vs. 22.9% for Cosmos3-Nano-Policy), indicating strong grounding of spatial language. Its weakest suite is Pick-v2 with randomized cameras (20.3%), indicating sensitivity to camera viewpoint.

**中文:** 抓放（pick-and-place）子套件（v2、NextTo 和 Color 上分别为 44.2%、37.5% 和 47.6%）。值得注意的是，它在空间指代的 NextTo 子套件上领先 14.6 个百分点（37.5% 对 22.9%，后者为 Cosmos3-Nano-Policy），表明它对空间语言的落地（grounding）能力较强。其最弱的子套件是随机相机条件下的 Pick-v2（20.3%），说明它对相机视角较为敏感。

<a id="S2244"></a>
**Source:** p.126 S2244

**Original:** G1 Factory. G1 Factory (NVIDIA, 2026c) adapts the nine Unitree G1 loco-manipulation tasks introduced in HumanoidMimicGen (Lin et al., 2026) to NVIDIA Isaac Lab-Arena. The tasks involve lifting and shelving boxes, retrieving and transferring drills, pressing buttons, and pushing a shelving cart with a 43-DoF G1 humanoid. The policy commands the arms, hands, and waist together with base-height and navigation commands that are executed by a lower-body controller. We train on 100 demonstrations per task from the released G1 Factory dataset and evaluate each policy over 100 episodes per task (900 episodes in total). We compare against GR00T 1.7 and report overall success rates in Tab. 34.

**中文:** G1 Factory（NVIDIA，2026c）将 HumanoidMimicGen（Lin et al., 2026）中引入的九个 Unitree G1 移动操作任务适配到 NVIDIA Isaac Lab-Arena 中。任务包括搬运与上架箱子、取出并转移钻头、按压按钮，以及推动置物架推车，所用机器人为 43 自由度（DoF）的 G1 人形机器人。策略同时指令手臂、手部和腰部，并配合基座高度和导航指令，由下肢控制器负责执行。我们使用已发布的 G1 Factory 数据集，每个任务用 100 个演示进行训练，并在每个任务的 100 个回合上评测每个策略（共 900 个回合）。我们与 GR00T 1.7 进行比较，总体成功率见 Tab. 34。

<a id="S2245"></a>
**Source:** p.126 S2245

**Original:** GR00T 2 achieves an overall success rate of 84.7%, outperforming GR00T 1.7 (69.4%) by 15.3 percentage points. It improves success rates on all nine tasks and achieves 100% success on box lifting from both the table and the floor. Remaining failures are concentrated in contact-rich tasks that require precise end-effector placement while the robot maintains balance: drill retrieval from the holder, shelf pushing, and button pressing.

**中文:** GR00T 2 的总体成功率为 84.7%，比 GR00T 1.7（69.4%）高 15.3 个百分点。它在全部九个任务上都提高了成功率，并且在箱子分别位于桌面和地面时的搬运任务上均达到 100% 成功率。剩余的失败主要集中在富接触任务上，这类任务要求机器人在保持平衡的同时精确放置末端执行器，包括从支架上取出钻头、推动置物架和按压按钮。


<a id="H70"></a>
### K. Infrastructure ｜ K. 基础设施

<a id="S2246"></a>
**Source:** p.127 S2246

**Original:** This section describes the compute, data, and research infrastructure used to develop GR00T 2.

**中文:** 本节介绍用于开发 GR00T 2 的计算、数据与研究基础设施。

<a id="H71"></a>
### K.1. Overall Software and Hardware Stack ｜ K.1. 整体软硬件栈

<a id="S2247"></a>
**Source:** p.127 S2247

**Original:** Training a robotics foundation model like GR00T involves: (1) the ingestion and conversion of large volumes of multimodal recordings, such as video, motion, and language annotations, into training-ready datasets, (2) pretraining and post-training at scale on GPU clusters, and (3) the deployment and evaluation of the resulting policies in simulation and on robots. This section describes the infrastructure we built for these workloads and used to develop GR00T 2. At each layer of the stack we build on widely used open-source software, such as PyTorch, Ray, SkyPilot, and Kubernetes, improving it where needed and adding robotics-specific components on top. We describe the overall stack first and each component separately below.

**中文:** 训练 GR00T 这类机器人基础模型，需要完成三项工作：(1) 将大量多模态记录（如视频、动作和语言标注）摄取并转换为可用于训练的数据集；(2) 在 GPU 集群上大规模地进行预训练与后训练；(3) 在仿真环境和真实机器人上部署并评测所得的策略。本节介绍我们为这些工作负载构建、并用于开发 GR00T 2 的基础设施。软件栈的每一层都建立在 PyTorch、Ray、SkyPilot 和 Kubernetes 等广泛使用的开源软件之上，必要时对其加以改进，并在其上增加面向机器人的专用组件。下文先概述整个软件栈，再分别介绍各个组件。

<a id="C101"></a>
**Source:** p.127 C101 · 图 F067

![F067](assets/F067.png)

**Original (caption):** Figure 67: Overall software and hardware stack of GR00T 2.

**中文图注：** 图 67：GR00T 2 的整体软硬件栈。

<a id="S2248"></a>
**Source:** p.127 S2248

**Original:** Fig. 67 shows the stack from the hardware up. Each workload runs on the NVIDIA platform suited to it: GB300 for training, RTX PRO 6000 for data processing, L40 and L40S for simulation and evaluation, and Jetson Thor for inference on the robot. Kubernetes manages the GPU clusters, with NVIDIA NVSentinel monitoring node health and services such as GPU Operator and DCGM alongside it. SkyPilot (Yang et al., 2023) provisions clusters and schedules and manages jobs across them. Ray (Moritz et al., 2018) distributes work within a job, for training workers and for data ingestion alike, and PyTorch is the deep learning framework.

**中文:** Fig. 67 自硬件向上展示了整个软硬件栈。每类工作负载都运行在与之匹配的 NVIDIA 平台上：训练使用 GB300，数据处理使用 RTX PRO 6000，仿真与评测使用 L40 和 L40S，机器人上的推理使用 Jetson Thor。Kubernetes 管理 GPU 集群，NVIDIA NVSentinel 负责节点健康监控，并与 GPU Operator、DCGM 等服务协同工作。SkyPilot（Yang et al., 2023）负责为集群供给资源，并在集群之间调度和管理作业。Ray（Moritz et al., 2018）在作业内部分发工作，既用于训练 worker，也用于数据摄取；PyTorch 则是深度学习框架。

<a id="S2249"></a>
**Source:** p.127 S2249

**Original:** The following subsections describe the hardware, cluster and job management, distributed training, inference, and data infrastructure. Reinforcement-learning post-training runs on the same stack, and its infrastructure is described in Sec. F.3.

**中文:** 以下各小节依次介绍硬件、集群与作业管理、分布式训练、推理和数据基础设施。强化学习后训练运行在同一套软件栈上，其基础设施见 Sec. F.3。

<a id="H72"></a>
### K.2. Hardware ｜ K.2. 硬件

<a id="S2250"></a>
**Source:** p.127 S2250

**Original:** GR00T 2 has many workloads that span large-scale foundation-model pretraining, simulation and policy evaluation, online post-training, and latency-sensitive robot deployment. These stages place different demands on accelerator memory, interconnect bandwidth, storage throughput, scheduling, and end-to-end latency. As a result, each stage has different hardware and system requirements that need to be accounted for.

**中文:** GR00T 2 涉及多种工作负载，涵盖大规模基础模型预训练、仿真与策略评测、在线后训练，以及对时延敏感的机器人部署。这些阶段对加速器显存、互连带宽、存储吞吐、调度和端到端时延提出了不同的要求。因此，每个阶段都有各自需要考虑的硬件与系统需求。

<a id="S2252"></a>
**Source:** p.128 S2252

**Original:** K.2.1. Pretraining

**中文:** K.2.1. 预训练

<a id="S2253"></a>
**Source:** p.128 S2253

**Original:** GR00T 2 pretraining ran on NVIDIA GB300 NVL72 systems because the workload placed a premium on GPU memory capacity, Tensor Core throughput, and networking/collective communication acceleration. Each Blackwell Ultra GPU provides up to 288 GB of HBM3e with 8 TB/s of memory bandwidth and approximately 2.5 PFLOPS of dense BF16/FP16 Tensor Core compute. Because the GR00T 2 model was small enough to fit without pipeline parallelism, this memory capacity allowed the model parameters, each rank’s optimizer state, and activations for a per-device batch of 16 to remain in GPU memory. The larger per-device batch provided more matrix-multiplication work for the Tensor Cores and amortized kernel-launch overhead, improving compute utilization (Aubrey and Stam, 2025).

**中文:** GR00T 2 的预训练运行在 NVIDIA GB300 NVL72 系统上，因为该工作负载对 GPU 显存容量、Tensor Core 吞吐，以及网络与集合通信加速有很高要求。每块 Blackwell Ultra GPU 提供最高 288 GB 的 HBM3e 显存，显存带宽为 8 TB/s，稠密 BF16/FP16 Tensor Core 算力约为 2.5 PFLOPS。由于 GR00T 2 模型足够小，无需流水线并行即可放下，因此这一显存容量使模型参数、每个 rank 的优化器状态，以及单设备批量为 16 时的激活值都能留在 GPU 显存中。更大的单设备批量为 Tensor Core 提供了更多矩阵乘法运算量，并分摊了 kernel 启动开销，从而提高了计算利用率（Aubrey and Stam, 2025）。

<a id="S2254"></a>
**Source:** p.128 S2254

**Original:** For networking, each GB300 NVL72 rack contains 18 compute trays and 72 GPUs connected as one NVLink domain. Fifth-generation NVLink provides 1.8 TB/s of bidirectional bandwidth per GPU. Within each NVLink domain, NVLink SHARP (NVLS) offloaded reductions to the NVSwitch. East/West communication used the RoCE scale-out fabric, with one 800 Gb/s ConnectX-8 SuperNIC per GPU (NVIDIA, n.d.a,n).

**中文:** 在网络方面，每个 GB300 NVL72 机架包含 18 个计算托盘和 72 块 GPU，它们连接成一个 NVLink 域。第五代 NVLink 为每块 GPU 提供 1.8 TB/s 的双向带宽。在每个 NVLink 域内，NVLink SHARP（NVLS）将归约操作卸载到 NVSwitch 上完成。东西向通信使用 RoCE 横向扩展（scale-out）网络结构，每块 GPU 配备一块 800 Gb/s 的 ConnectX-8 SuperNIC（NVIDIA, n.d.a,n）。

<a id="S2255"></a>
**Source:** p.128 S2255

**Original:** The full cluster contained 2,016 GPUs across 28 GB300 NVL72 racks. The GR00T 2 main pretraining run used 1,024 GPUs, while the remaining cluster capacity supported other training experiments concurrently.

**中文:** 整个集群共有 2,016 块 GPU，分布在 28 个 GB300 NVL72 机架中。GR00T 2 的主预训练运行使用了 1,024 块 GPU，其余集群容量则同时支持其他训练实验。

<a id="S2256"></a>
**Source:** p.128 S2256

**Original:** K.2.2. Simulation and Policy Evaluation

**中文:** K.2.2. 仿真与策略评测

<a id="S2257"></a>
**Source:** p.128 S2257

**Original:** Simulation and policy evaluation ran on NVIDIA L40 and L40S clusters because these workloads required graphics, simulation compute, and policy inference on the same accelerator. Both GPUs use the Ada Lovelace architecture and provide 48 GB of GDDR6 memory with 864 GB/s of memory bandwidth, 142 third-generation RT Cores, and 568 fourth-generation Tensor Cores. The RT Cores accelerate hardware ray tracing for rendered observations, while the Tensor Cores accelerate low-precision policy inference. The L40S retains the L40’s memory capacity and graphics resources while providing approximately twice its peak low-precision Tensor Core throughput, allowing more inference work to accompany simulation (NVIDIA, 2023, n.d.c).

**中文:** 仿真与策略评测运行在 NVIDIA L40 和 L40S 集群上，因为这些工作负载需要在同一加速器上同时完成图形渲染、仿真计算和策略推理。两款 GPU 均采用 Ada Lovelace 架构，各配备 48 GB GDDR6 显存，显存带宽为 864 GB/s，并具有 142 个第三代 RT Core 和 568 个第四代 Tensor Core。RT Core 为渲染观测提供硬件光线追踪加速，Tensor Core 则加速低精度策略推理。L40S 保留了 L40 的显存容量和图形资源，同时其峰值低精度 Tensor Core 吞吐约为 L40 的两倍，从而能够在运行仿真的同时承载更多推理工作（NVIDIA, 2023, n.d.c）。

<a id="S2258"></a>
**Source:** p.128 S2258

**Original:** The 48 GB memory capacity provides headroom to keep the policy checkpoint, simulator state, and rendering buffers resident while processing multiple environments, although achievable concurrency depends on the simulator and task. Unlike GB300 NVL72 systems, L40 and L40S are PCIe Gen4 GPUs without NVLink (NVIDIA, 2023, n.d.c). Evaluation therefore scales primarily by distributing independent environment, checkpoint, and random-seed shards across workers rather than through frequent cross-GPU collectives. Network and storage throughput remain important for staging checkpoints and collecting rollout artifacts, but the primary capacity metrics are environments per GPU, rollout throughput, and checkpoint-evaluation turnaround time.

**中文:** 48 GB 的显存容量为同时处理多个环境时保留策略检查点、仿真器状态和渲染缓冲区提供了余量，不过可实现的并发度取决于仿真器和任务。与 GB300 NVL72 系统不同，L40 和 L40S 是不带 NVLink 的 PCIe Gen4 GPU（NVIDIA, 2023, n.d.c）。因此，评测主要通过将独立的环境、检查点和随机种子分片分配给各个 worker 来扩展，而不是依赖频繁的跨 GPU 集合通信。网络和存储吞吐对于暂存检查点、收集 rollout（轨迹采样）产物依然重要，但主要的容量指标是每块 GPU 的环境数、rollout 吞吐量以及检查点评测的周转时间。

<a id="S2259"></a>
**Source:** p.128 S2259

**Original:** K.2.3. Online Post-Training

**中文:** K.2.3. 在线后训练

<a id="S2260"></a>
**Source:** p.128 S2260

**Original:** Online post-training ran across heterogeneous H100, GB300, and L40/L40S pools because no single accelerator could satisfy every stage of the workflow. H100 and GB300 systems supported distributed policy optimization. L40 and L40S systems supported simulation-based collection and evaluation, where graphics capabilities were needed. Capacity was allocated independently to each stage and adjusted as workload bottlenecks shifted.

**中文:** 在线后训练运行在异构的 H100、GB300 以及 L40/L40S 资源池上，因为没有任何单一加速器能满足工作流中的每个阶段。H100 和 GB300 系统支持分布式策略优化。L40 和 L40S 系统支持基于仿真的数据收集与评测，这类工作需要图形能力。各阶段的资源容量独立分配，并随工作负载瓶颈的转移而调整。

<a id="H73"></a>
### K.3. Cluster and Job Management ｜ K.3. 集群与作业管理

<a id="S2261"></a>
**Source:** p.128 S2261

**Original:** K.3.1. Kubernetes

**中文:** K.3.1. Kubernetes

<a id="S2262"></a>
**Source:** p.128 S2262

**Original:** Kubernetes provides the AI factory execution layer for GR00T 2, with the cluster software stack deployed through NVIDIA AI Cluster Runtime (AICR) (NVIDIA, n.d.d). This integrates NVIDIA DSX OS components for GPU enablement, high-performance networking, and infrastructure resilience. NVIDIA GPU Operator and Network Operator manage the GPU and networking software stacks, while KAI Scheduler and Kueue provide workload scheduling and admission control, priorities, resource quotas, and topology-aware placement for multi-node workloads.

**中文:** Kubernetes 为 GR00T 2 提供 AI 工厂的执行层，集群软件栈通过 NVIDIA AI Cluster Runtime（AICR）部署（NVIDIA, n.d.d）。它集成了 NVIDIA DSX OS 组件，用于 GPU 启用、高性能网络和基础设施韧性。NVIDIA GPU Operator 和 Network Operator 负责管理 GPU 与网络软件栈；KAI Scheduler 和 Kueue 则为多节点工作负载提供调度与准入控制、优先级、资源配额，以及拓扑感知的放置。

<a id="S2263"></a>
**Source:** p.129 S2263

**Original:** On GB300 NVL72 systems, NVIDIA’s Dynamic Resource Allocation (DRA) driver manages ComputeDomains, enabling secure multi-node NVLink access for workload pods. NCCL uses this fabric for collective communication within each NVLink domain and RoCE for communication across racks.

**中文:** 在 GB300 NVL72 系统上，NVIDIA 的动态资源分配（DRA）驱动程序负责管理 ComputeDomains，为工作负载 Pod 提供安全的多节点 NVLink 访问。NCCL 在每个 NVLink 域内使用该互连进行集合通信，并通过 RoCE 实现跨机架通信。

<a id="S2264"></a>
**Source:** p.129 S2264

**Original:** NVSentinel, also part of NVIDIA DSX OS, monitors GPU and node health and supports policy-driven isolation and remediation of faulty nodes. Together with SkyPilot’s job recovery and the training runtime’s checkpoint-resume mechanisms, these components support reliable operation of the GR00T 2 AI factory.

**中文:** NVSentinel 同样是 NVIDIA DSX OS 的组成部分，负责监控 GPU 与节点健康，并支持基于策略对故障节点进行隔离与修复。结合 SkyPilot 的作业恢复机制以及训练运行时的检查点续训机制，这些组件共同保障了 GR00T 2 AI 工厂的可靠运行。

<a id="S2265"></a>
**Source:** p.129 S2265

**Original:** K.3.2. SkyPilot

**中文:** K.3.2. SkyPilot

<a id="S2266"></a>
**Source:** p.129 S2266

**Original:** GR00T 2 training uses SkyPilot (Yang et al., 2023) as the infrastructure orchestration layer for distributed GPU workloads. A shared SkyPilot API control plane provides a common interface for submitting experiments, provisioning workload clusters, monitoring execution, and managing cluster lifecycles. The platform connects this control plane to GPU infrastructure through configured Kubernetes contexts and workspace access controls. Infrastructure configuration and administrative policies are maintained separately from model code, allowing researchers to specify training requirements while platform operators manage credentials, storage integration, and infrastructure access.

**中文:** GR00T 2 训练使用 SkyPilot（Yang et al., 2023）作为分布式 GPU 工作负载的基础设施编排层。共享的 SkyPilot API 控制平面提供统一接口，用于提交实验、供给工作负载集群、监控执行过程以及管理集群生命周期。平台通过已配置的 Kubernetes 上下文和工作区访问控制，将该控制平面与 GPU 基础设施相连。基础设施配置与管理策略独立于模型代码维护，使研究人员能够描述训练需求，而平台运维人员负责管理凭据、存储集成和基础设施访问。

<a id="S2267"></a>
**Source:** p.129 S2267

**Original:** Each experiment runs as a SkyPilot managed job. Once resources are available, the workload containers form a Ray cluster, and the training driver creates a distributed worker for each GPU. SkyPilot manages infrastructure execution, Ray places training workers, and PyTorch, NCCL, and the optimizer implementation perform distributed model training.

**中文:** 每个实验都作为一个 SkyPilot 托管作业运行。资源就绪后，工作负载容器组成一个 Ray 集群，训练驱动程序为每块 GPU 创建一个分布式 worker。SkyPilot 负责基础设施执行，Ray 负责放置训练 worker，PyTorch、NCCL 以及优化器实现则共同完成分布式模型训练。

<a id="S2268"></a>
**Source:** p.129 S2268

**Original:** The infrastructure accounts for the communication and data-access requirements of large-scale joint videoand-action training. Kubernetes and Kueue coordinate admission of multi-node workloads using GPU topology information, while the OCI workload configuration requests RDMA network attachments and placement within GPU clique topology domains. The training runtime additionally orders distributed ranks according to physical topology. Shared Lustre storage supplies datasets, pretrained assets, and persistent checkpoints, while node-local scratch supports temporary runtime files. These components connect resource allocation to the communication and storage requirements of the GR00T 2 training workload.

**中文:** 该基础设施考虑了大规模视频-动作联合训练（[存疑：原文抽取为 videoand-action，疑为 video-and-action]）在通信与数据访问方面的需求。Kubernetes 与 Kueue 利用 GPU 拓扑信息协调多节点工作负载的准入，而 OCI 工作负载配置则请求 RDMA 网络附件，并将 Pod 放置在 GPU clique 拓扑域内。训练运行时还会根据物理拓扑对分布式 rank 进行排序。共享的 Lustre 存储提供数据集、预训练资产和持久化检查点，节点本地的 scratch 存储则用于临时运行时文件。这些组件将资源分配与 GR00T 2 训练工作负载的通信和存储需求联系起来。

<a id="S2269"></a>
**Source:** p.129 S2269

**Original:** Launch-time administrative policies validate infrastructure selections, preserve backend-specific placement settings, and configure centralized log forwarding. Workspace access controls govern access to the available compute environments. The platform also supports policies that derive queue assignments and scheduling priorities from administrator-managed workspace configuration. SkyPilot managed-job recovery works together with bounded retries and checkpoint resume in the training stack. This separation enables infrastructure recovery while retaining training state in persistent storage.

**中文:** 启动时的管理策略会校验基础设施选择、保留特定后端的放置设置，并配置集中式日志转发。工作区访问控制用于管理对可用计算环境的访问。平台还支持根据管理员维护的工作区配置推导队列分配和调度优先级的策略。SkyPilot 托管作业的恢复机制与训练栈中有上限次数的重试和检查点续训协同工作。这种分工使基础设施能够恢复，同时训练状态保存在持久存储中。


<a id="H74"></a>
### K.4. Distributed Training ｜ 分布式训练

<a id="S2270"></a>
**Source:** p.129 S2270

**Original:** Distributed training of GR00T 2 requires coordinating multimodal input preparation with synchronous model updates. We design the runtime to reduce memory use, limit waiting between training stages, and preserve progress across interruptions.

**中文:** GR00T 2 的分布式训练需要让多模态输入准备与同步的模型更新相互协调。我们设计该运行时，以降低内存占用、限制各训练阶段之间的等待时间，并在训练中断后保留训练进度。

<a id="S2271"></a>
**Source:** p.129 S2271

**Original:** K.4.1. Parallelism and Memory Management

**中文:** K.4.1. 并行与内存管理

<a id="S2272"></a>
**Source:** p.129 S2272

**Original:** We use synchronous data parallelism with DeepSpeed ZeRO-2. Model weights are replicated on each GPU, while gradients and optimizer state are partitioned across ranks to reduce per-device memory use. BF16 gradient synchronization overlaps with model computation to reduce exposed communication time.

**中文:** 我们使用同步的数据并行（data parallelism）并结合 DeepSpeed ZeRO-2。模型权重在每块 GPU 上各保存一份副本，而梯度和优化器状态则在各 rank（分布式进程）之间切分，以降低单设备的内存占用。BF16 梯度同步与模型计算重叠进行，以减少暴露在外的通信时间。

<a id="S2273"></a>
**Source:** p.129 S2273

**Original:** K.4.2. Efficient Multimodal Computation

**中文:** K.4.2. 高效的多模态计算

<a id="S2274"></a>
**Source:** p.129 S2274

**Original:** Multimodal training requires computation in both frozen feature encoders and the trainable model. Depending on the recipe, the runtime supports TensorRT video encoding, fused text-encoder operations, efficient attention kernels, and PyTorch compilation.

**中文:** 多模态训练既需要在冻结的特征编码器中进行计算，也需要在可训练模型中进行计算。根据训练配方的不同，运行时支持 TensorRT 视频编码、融合的文本编码器算子、高效的注意力算子（kernel），以及 PyTorch 编译。

<a id="S2275"></a>
**Source:** p.129 S2275

**Original:** Activation recomputation reduces memory use at the cost of additional computation. Attention optimizations

**中文:** 激活重计算以额外计算为代价降低内存占用。注意力优化 [存疑：原文抽取在此截断]

<a id="C102"></a>
**Source:** p.130 C102 · 图 F068

![F068](assets/F068.png)

**Original (caption):** Figure 68: Data delivery during multi-view pretraining on 1,024 NVIDIA GB300 GPUs over 100 consecutive steadystate steps. (a) Delivered sample-window throughput. (b) Exposed batch-retrieval wait, showing the mean and maximum across ranks.

**中文图注：** 图 68：在 1,024 块 NVIDIA GB300 GPU 上、连续 100 个稳态步内的多视角预训练数据交付情况。(a) 已交付的样本窗口吞吐量。(b) 暴露的批次取回等待时间，显示各 rank 上的均值与最大值。

<a id="S2279"></a>
**Source:** p.130 S2279

**Original:** GR00T 2’s data loader combines versioned multimodal storage, offline quality filtering, and asynchronous batch preparation. Training recipes specify the data snapshots to read and how samples are selected and interpreted across embodiments. The training mixture used for the measurements below comprises 25 versioned dataset stores, totaling 15.6 million episode records and 46.2 billion recorded time steps before applying the run’s sampling views. These totals aggregate the selected stores without deduplicating recording content across stores.

**中文:** GR00T 2 的数据加载器结合了带版本的多模态存储、离线质量过滤和异步批次准备。训练配方规定了要读取的数据快照，以及样本如何在不同本体（embodiment）之间被选取和解释。下文测量所用的训练混合数据由 25 个带版本的数据集存储组成，在应用本次运行的采样视图之前，共计 1560 万条片段（episode）记录和 462 亿个记录的时间步。这些总数是对所选存储的汇总，未对各存储之间的记录内容去重。

<a id="S2280"></a>
**Source:** p.130 S2280

**Original:** Versioned storage and schema. We store training data in LanceDS, built on the Lance columnar format (Pace et al., 2025; Lance Contributors, 2026). Each dataset contains a step table for state, action, annotations, and quality-control (QC) signals, an episode table, and a media table holding the original videos. Lance’s versioning preserves earlier snapshots when episodes are added or annotations or QC signals change, and new QC columns can be added without rewriting existing columns. A per-dataset commit record ties each snapshot’s table versions to its normalization statistics and metadata. A training run pins one snapshot per dataset, so data, statistics, and metadata are reproduced together. Snapshots are replicated to the object store and to training clusters in commit order, with the commit record copied last, so a replica serves a pinned snapshot completely or not at all.

**中文:** 版本化存储与模式（schema）。我们将训练数据存储在 LanceDS 中，它构建于 Lance 列式格式之上（Pace et al., 2025; Lance Contributors, 2026）。每个数据集包含一张用于存放状态、动作、标注和质量控制（QC）信号的步表（step table）、一张片段表（episode table），以及一张存放原始视频的媒体表（media table）。当新增片段，或标注、QC 信号发生变化时，Lance 的版本机制会保留较早的快照；新的 QC 列可以直接添加，无需重写已有列。每个数据集的提交记录（commit record）将每个快照的表版本与其归一化统计量和元数据关联起来。一次训练运行会为每个数据集固定一个快照，因此数据、统计量和元数据能够被一并复现。快照按提交顺序复制到对象存储和训练集群，提交记录最后复制，因此副本要么完整地提供固定的快照，要么完全不提供。

<a id="S2281"></a>
**Source:** p.130 S2281

**Original:** Datasets share a schema in which state and action groups are packed into one state column and one action column. Group names and offsets are recorded in schema metadata, allowing the loader to select fields by name despite differences in their stored order. At read time, the recipe’s embodiment tag selects groups, cameras, annotations, normalization statistics pooled across datasets of that embodiment, and, for dexterous hands, fingertip force signals and deformation video. The same tag determines the model’s embodiment-specific projection layers. Datasets of the same embodiment can be merged with a common group order.

**中文:** 各数据集共享同一模式：状态组和动作组分别打包进一个状态列和一个动作列。组名和偏移量记录在模式元数据中，使加载器即便字段在存储中的顺序不同，仍能按名称选取字段。读取时，配方中的本体标签会选定组、相机、标注，以及在该本体所有数据集上汇总的归一化统计量；对于灵巧手，还会选定指尖力信号和形变视频。同一标签还决定了模型中本体相关的投影层。同一本体的数据集可以按统一的组顺序合并。

<a id="S2282"></a>
**Source:** p.130 S2282

**Original:** Steps within each episode are stored contiguously, and the loader fetches episode ranges through batched reads. Step-table reads bypass filesystem readahead, which amplified per-shard step-table I/O by 28× to 60× in an earlier production benchmark.

**中文:** 每个片段内的步按连续方式存储，加载器通过批量读取获取片段范围。步表读取会绕过文件系统的预读（readahead），在早前的一次生产基准测试中，预读使每个分片的步表 I/O 放大了 28× 至 60×。

<a id="S2283"></a>
**Source:** p.131 S2283

**Original:** Window-aware QC views. A view records the steps eligible to serve as training-sample starts. User-defined Python filters evaluate an episode’s columns over the temporal window consumed by each sample, so eligibility accounts for the observations and action targets that training will read. Filters can also select whole episodes by metadata such as task family, collection date, or data origin. Views are computed offline and stored as runs of consecutive eligible steps per episode. Training samples directly from these runs without evaluating the filters in the loading path.

**中文:** 感知窗口的 QC 视图（view）。一个视图记录可以作为训练样本起点的步。用户自定义的 Python 过滤器会在每个样本所消耗的时间窗口上计算片段的各列，因此资格判定会考虑训练将读取的观测和动作目标。过滤器还可以依据任务族、采集日期或数据来源等元数据，选取整段片段。视图离线计算，并以每个片段内连续合格步的游程形式存储。训练直接从这些游程中采样，加载路径中不再计算过滤器。

<a id="S2284"></a>
**Source:** p.131 S2284

**Original:** Each view is identified by a hash of the dataset, filter code and arguments, and sample window. Cosmetic edits to a filter keep its hash. Views are tagged with the table versions they serve and can be shared by identifier across runs. A view is reused at a new version when the dataset’s rows and the columns its filters read are unchanged. Views are rebuilt automatically: each new snapshot triggers a build of every registered view in the same job that writes the snapshot, and the snapshot and its views are published together, so recipes can pin new snapshots without a manual build step.

**中文:** 每个视图由数据集、过滤器代码及参数和样本窗口的哈希值共同标识。对过滤器的外观性修改不会改变其哈希值。视图会标注其所服务的表版本，并可在不同运行之间通过标识符共享。当数据集的行以及过滤器所读取的列均未变化时，视图可在新版本下复用。视图会自动重建：每个新快照都会在写入该快照的同一作业中触发所有已注册视图的构建，快照与其视图同时发布，因此配方无需手动构建步骤即可固定到新快照。

<a id="S2285"></a>
**Source:** p.131 S2285

**Original:** Views also carry normalization statistics (mean, standard deviation, minimum, maximum, and 1st and 99th percentiles) computed over the samples they keep. Each statistics entry is keyed to the training configuration it was computed under: the snapshot, embodiment, action horizon, and which actions are trained relative to state.

**中文:** 视图还携带归一化统计量（均值、标准差、最小值、最大值，以及第 1 和第 99 百分位数），这些统计量基于视图所保留的样本计算。每条统计量记录都与其计算时所处的训练配置相关联：快照、本体、动作时域，以及哪些动作是相对于状态进行训练的。

<a id="S2286"></a>
**Source:** p.131 S2286

**Original:** For human demonstrations, QC filters check head and wrist motion, hand-pose plausibility, and keypoint visibility, excluding tracking failures such as frozen head poses and abrupt fingertip jumps. For robot demonstrations, filters exclude task-irrelevant motion, idle time, and annotated mistakes or failures. Storing these signals as step-table columns allows curation rules to evolve alongside the versioned dataset.

**中文:** 对于人类演示，QC 过滤器会检查头部和腕部运动、手部姿态的合理性以及关键点可见性，并剔除跟踪失效的片段，例如头部姿态冻结和指尖突然跳变。对于机器人演示，过滤器会剔除与任务无关的运动、空闲时间，以及已标注的错误或失败。将这些信号存储为步表的列，使数据筛选规则能够随带版本的数据集一同演进。

<a id="S2287"></a>
**Source:** p.131 S2287

**Original:** Sampling and batch delivery. Sampling choices are generated on demand from deterministic per-rank step seeds, avoiding a precomputed sampling sequence. Samples are mixed across shards to target the recipe’s dataset proportions in each global step. Sampling without replacement accommodates datasets of different lengths without requiring aligned epoch boundaries.

**中文:** 采样与批次交付。采样选择按需由各 rank 上确定性的步级随机种子生成，无需预先计算采样序列。样本在各分片之间混合，使每个全局步中的数据集比例符合配方的设定。无放回采样可以适应长度不同的数据集，而无需对齐 epoch 边界。

<a id="S2288"></a>
**Source:** p.131 S2288

**Original:** Batch preparation uses three asynchronous stages. The I/O stage prefetches video shards from shared storage into node-local NVMe. The decoding stage reads cached shards, decodes frames, and prepares trajectory metadata. In a representative three-view shard benchmark, decoding was estimated to account for about 90% of preparation time. A separate sequential-decoding microbenchmark measured approximately 7,000 frames/s with one decoding thread at 320×240. The loader stage applies augmentations (random crops retaining 95% of each spatial dimension, resizing to 224×320, and codec augmentation), collates samples, and prepares asynchronous transfers from pinned host memory to the GPU. Keeping prefetched video shards on NVMe reduces the host RAM required for buffering and allows a deeper prefetch window. Dedicated worker pools, SIMD-vectorized decoding, and C++ augmentation implementations reduce CPU processing overhead.

**中文:** 批次准备包含三个异步阶段。I/O 阶段将视频分片从共享存储预取到节点本地 NVMe。解码阶段读取已缓存的分片、解码帧并准备轨迹元数据。在一个具有代表性的三视角分片基准测试中，估计解码约占准备时间的 90%。另有一项单独的顺序解码微基准测试，在 320×240 分辨率、单解码线程下测得约 7,000 帧/秒（frames/s）。加载器阶段应用数据增广（随机裁剪保留每个空间维度的 95%、缩放至 224×320，以及编解码器增广），整理（collate）样本，并准备从锁页主机内存到 GPU 的异步传输。将预取的视频分片保存在 NVMe 上，可以减少缓冲所需的主机内存，并允许更深的预取窗口。专用的 worker 池、SIMD 向量化解码以及 C++ 增广实现，降低了 CPU 处理开销。

<a id="S2289"></a>
**Source:** p.131 S2289

**Original:** On clusters with limited shared-storage capacity, the I/O stage instead stages upcoming shards’ source files on node-local NVMe through a cluster-lifetime object store. Each file is read from the data source once per cluster and forwarded between nodes, so source traffic does not grow with node count. A preloaded interposer serves data-loader reads from local NVMe at the files’ original paths, and a file that cannot be delivered is an error rather than a skipped episode.

**中文:** 在共享存储容量有限的集群上，I/O 阶段改为通过集群生命周期的对象存储，将即将使用的分片源文件预先暂存到节点本地 NVMe 上。每个文件在每个集群中只从数据源读取一次，并在节点之间转发，因此源端流量不会随节点数量增长。预加载的拦截层（interposer）以文件的原始路径，从本地 NVMe 为数据加载器的读取提供服务；无法交付的文件被视为错误，而不是被跳过的片段。

<a id="S2290"></a>
**Source:** p.131 S2290

**Original:** Variable-length token packing reduces padding when samples differ in camera configuration or sequence length. In the measured training run, packed sequences occupied 94.5% of the available positions in 32,768-token rows.

**中文:** 当样本在相机配置或序列长度上有所不同时，变长 token 打包可以减少填充。在实测的训练运行中，打包后的序列占据了 32,768 token 行中 94.5% 的可用位置。

<a id="S2291"></a>
**Source:** p.131 S2291

**Original:** Reproducibility and diagnostics. The loader controls random seeds for sampling and spatiotemporal augmentation. Training checkpoints record loader progress (including active shard offsets, sample indices, and worker state) together with the configuration, including each dataset’s pinned snapshot. The supported sharded pipeline restores sample-sequence progress when resuming with the same data configuration and rank/worker topology. Each sample carries a composite identifier comprising dataset ID, trajectory ID, and frame index, linking the training input to its source.

**中文:** 可复现性与诊断。加载器控制采样和时空增广所用的随机种子。训练检查点会与配置（包括每个数据集所固定的快照）一同记录加载器进度（包括活跃的分片偏移、样本索引和 worker 状态）。在数据配置及 rank/worker 拓扑保持一致的情况下续训时，所支持的分片流水线会恢复样本序列进度。每个样本都带有一个复合标识符，由数据集 ID、轨迹 ID 和帧索引组成，从而将训练输入与其来源相连。

<a id="S2293"></a>
**Source:** p.132 S2293

**Original:** Structured events from each worker and distributed rank trace the batch-loading lifecycle. Correlating these events with sample identifiers helps investigate storage delays, worker starvation, and loss anomalies. A CPU-only benchmark harness uses Gloo and identity model stubs to profile the loading pipeline before GPU runs. Fig. 68 and Tab. 35 report the measured input-delivery performance.

**中文:** 来自每个 worker 和分布式 rank 的结构化事件，记录了批次加载的完整生命周期。将这些事件与样本标识符关联起来，有助于排查存储延迟、worker 饥饿和 loss 异常。一个仅使用 CPU 的基准测试框架，在 GPU 运行之前，使用 Gloo 和恒等模型桩（identity model stub）对加载流水线进行剖析。Fig. 68 和 Tab. 35 报告了实测的输入交付性能。

<a id="S2294"></a>
**Source:** p.132 S2294

**Original:** K.4.4. Straggler Control and Communication

**中文:** K.4.4. 掉队者控制与通信

<a id="S2295"></a>
**Source:** p.132 S2295

**Original:** A rank delayed by input preparation or a CPU pause can hold up collective operations across the training job. We profile CPU activity, GPU execution, and collective timing together to distinguish late-arriving ranks from slow communication.

**中文:** 因输入准备或 CPU 停顿而延迟的 rank（掉队者，straggler），可能会阻塞整个训练作业中的集合通信操作。我们同时剖析 CPU 活动、GPU 执行和集合通信时序，以区分到达较晚的 rank 与通信缓慢。

<a id="S2296"></a>
**Source:** p.132 S2296

**Original:** Depending on the configuration, the runtime coordinates garbage collection, controls CPU thread placement, balances loader concurrency, and reports metrics asynchronously to limit host delays that interrupt GPU work and synchronization.

**中文:** 根据配置不同，运行时会协调垃圾回收、控制 CPU 线程放置、平衡加载器并发度，并异步上报指标，以限制会打断 GPU 工作与同步的主机端延迟。

<a id="S2297"></a>
**Source:** p.132 S2297

**Original:** K.4.5. Checkpointing and Recovery

**中文:** K.4.5. 检查点保存与恢复

<a id="S2298"></a>
**Source:** p.132 S2298

**Original:** Checkpointing coordinates a consistent foreground snapshot of training state, followed by background serialization and writes. Asynchronous saving reduces exposed I/O, and a checkpoint becomes available for continuation once all required writes complete.

**中文:** 检查点保存先协调一个一致的训练状态前台快照，随后进行后台序列化与写入。异步保存减少了暴露的 I/O；所有必需的写入完成后，检查点即可用于续训。

<a id="S2299"></a>
**Source:** p.132 S2299

**Original:** Model artifacts provide weights for evaluation and downstream initialization. Continuation checkpoints additionally retain optimizer partitions, scheduler history, random-number-generator state, and supported loader progress. Restoring training requires compatibility between the saved state and the resumed runtime.

**中文:** 模型产物提供用于评测和下游初始化的权重。续训检查点还额外保存优化器分区、调度器历史、随机数生成器状态以及受支持的加载器进度。恢复训练要求所保存的状态与恢复时的运行时相互兼容。

<a id="S2300"></a>
**Source:** p.132 S2300

**Original:** K.4.6. Training Efficiency

**中文:** K.4.6. 训练效率

<a id="S2301"></a>
**Source:** p.132 S2301

**Original:** We assess training efficiency across input retrieval, frozen feature encoding, model computation, gradient synchronization, and optimizer updates. Step time is interpreted alongside model quality, accounting for differences in active modalities, trainable components, and input shapes.

**中文:** 我们从输入读取、冻结特征编码、模型计算、梯度同步和优化器更新等方面评估训练效率。单步耗时需结合模型质量加以解读，并考虑活跃模态、可训练组件和输入形状的差异。

<a id="S2302"></a>
**Source:** p.132 S2302

**Original:** Tab. 35 reports input-delivery performance over 100 steady-state pretraining steps on 1,024 NVIDIA GB300 GPUs. These measurements characterize the data pipeline. They do not measure whole-model FLOP utilization.

**中文:** Tab. 35 报告了在 1,024 块 NVIDIA GB300 GPU 上、连续 100 个稳态预训练步中的输入交付性能。这些测量刻画的是数据流水线，并不测量整模型的 FLOP 利用率。

<a id="C103"></a>
**Source:** p.132 C103 · 表 T035

![T035](assets/T035.png)

**Original (caption):** Table 35: Measured training-input delivery over 100 steady-state steps on 1,024 NVIDIA GB300 GPUs. The wait-time share is relative to aggregate measured rank-step time.

**中文表注：** 表 35：在 1,024 块 NVIDIA GB300 GPU 上、100 个稳态步内实测的训练输入交付情况。等待时间占比相对于实测的 rank 步总耗时计算。

<a id="S2304"></a>
**Source:** p.132 S2304

**Original:** Aggregate sample-window throughput ∼12,000 windows/s Per-GPU sample-window throughput 11.7 windows/s Mean exposed data-loader wait 0.37 ms 99th-percentile exposed data-loader wait 0.61 ms Exposed wait / aggregate measured rank-step time 0.049%

**中文:** 总体样本窗口吞吐量约为 12,000 windows/s；单 GPU 样本窗口吞吐量为 11.7 windows/s；平均暴露的数据加载器等待时间为 0.37 ms；第 99 百分位的暴露数据加载器等待时间为 0.61 ms；暴露等待时间占实测 rank 步总耗时的比例为 0.049%。[存疑：原文为表格的扁平抽取，行列结构已丢失]

<a id="S2305"></a>
**Source:** p.132 S2305

**Original:** We monitor Overall FLOP Utilization (OFU), a hardware-counter-based complement to application-level Model FLOPs Utilization (MFU), alongside step time and task-level evaluation (Pedersen et al., 2026). DCGM provides GPU telemetry (NVIDIA, n.d.e), and Weights & Biases records step time. Utilization helps diagnose accelerator use, while elapsed time and model quality determine whether a change is useful. An optimization can reduce step time without changing the utilization signal. Assessment of a full training run also accounts for startup, compilation, checkpoint pauses, interruptions, and replayed work.

**中文:** 我们监控整体 FLOP 利用率（Overall FLOP Utilization, OFU）。它基于硬件计数器，是应用层模型 FLOP 利用率（MFU）的补充，与单步耗时和任务级评测一并使用（Pedersen et al., 2026）。DCGM 提供 GPU 遥测数据（NVIDIA, n.d.e），Weights & Biases 记录单步耗时。利用率有助于诊断加速器的使用情况，而耗时和模型质量则决定某项改动是否有用。一项优化可能在不改变利用率信号的情况下降低单步耗时。对完整训练运行的评估还需考虑启动、编译、检查点暂停、中断以及重放的工作。


<a id="H75"></a>
### K.5. Inference Infrastructure ｜ 推理基础设施

<a id="S2306"></a>
**Source:** p.132 S2306

**Original:** We use a client-server architecture to deploy GR00T 2 across embodiments and execution backends. The server handles policy inference, while robot clients connect it to embodiment-specific sensing and control.

**中文:** 我们采用客户端-服务器架构，在不同的本体（embodiment）与执行后端上部署 GR00T 2。服务器负责策略推理，机器人客户端则把服务器与各本体特定的感知和控制连接起来。

<a id="S2307"></a>
**Source:** p.133 S2307

**Original:** K.5.1. Policy Serving

**中文:** K.5.1. 策略服务

<a id="S2308"></a>
**Source:** p.133 S2308

**Original:** The robot client sends camera history, robot state, and task instructions through a shared request-reply interface. The server prepares inputs for the loaded model and returns predicted action chunks, which the client maps to the robot’s command format. Checkpoint configuration specifies the required history and embodiment-specific input and action representations. The interface supports PyTorch and optimized runtimes, with client and server running on the same host or separate hosts.

**中文:** 机器人客户端通过共享的请求-应答接口发送相机历史、机器人状态和任务指令。服务器为已加载的模型准备输入，并返回预测的动作块，客户端再将其映射为机器人的指令格式。检查点配置规定了所需的历史信息，以及各本体特定的输入和动作表示。该接口同时支持 PyTorch 与优化运行时，客户端与服务器既可以运行在同一台主机上，也可以分别运行在不同的主机上。

<a id="S2309"></a>
**Source:** p.133 S2309

**Original:** For streaming or prefetched observations, the server verifies that prepared visual inputs match the camera history in the prediction request.

**中文:** 对于流式或预取的观测，服务器会核对已准备好的视觉输入是否与预测请求中的相机历史一致。

<a id="S2310"></a>
**Source:** p.133 S2310

**Original:** K.5.2. Compatibility and Readiness

**中文:** K.5.2. 兼容性与就绪状态

<a id="S2311"></a>
**Source:** p.133 S2311

**Original:** Compiled runtime artifacts are specific to the checkpoint and execution environment. The server checks checkpoint identity, input shapes, numerical precision, software versions, and GPU target before use, rejecting incompatible artifacts. Backends that require warmup initialize execution with a representative observation from the client. Readiness indicates that the required checks and initialization have completed.

**中文:** 编译后的运行时产物与检查点及执行环境相绑定。服务器在使用前会检查检查点身份、输入形状、数值精度、软件版本和 GPU 目标，并拒绝不兼容的产物。需要预热的后端会用客户端提供的一个代表性观测来初始化执行。就绪状态表示所需的检查与初始化均已完成。

<a id="S2312"></a>
**Source:** p.133 S2312

**Original:** On devices with limited GPU memory, the server can offload text-encoder weights to CPU memory, leaving more accelerator memory for policy execution.

**中文:** 在 GPU 显存有限的设备上，服务器可以把文本编码器权重卸载到 CPU 内存中，从而为策略执行留出更多加速器内存。

<a id="S2313"></a>
**Source:** p.133 S2313

**Original:** K.5.3. Action Delivery

**中文:** K.5.3. 动作下发

<a id="S2314"></a>
**Source:** p.133 S2314

**Original:** The client buffers action chunks and schedules commands at the controller’s execution rate. With asynchronous prediction enabled, it requests the next chunk while the controller executes the current one. Clients using timestamped waypoints discard expired targets before sending commands to the controller. Inference acceleration and policy-quality validation are described in Sec. I.1. RTC and action-timing methods are described in Sec. I.2 and I.3.

**中文:** 客户端会缓存动作块，并按控制器的执行频率调度指令。启用异步预测后，客户端会在控制器执行当前动作块的同时请求下一个动作块。使用带时间戳路点的客户端，会在把指令发送给控制器之前丢弃已过期的目标。推理加速与策略质量验证见 Sec. I.1，实时分块（RTC）与动作时序方法见 Sec. I.2 和 Sec. I.3。

<a id="H76"></a>
### K.6. Scalable Multi-Modal Data Processing ｜ 可扩展的多模态数据处理

<a id="S2315"></a>
**Source:** p.133 S2315

**Original:** Scaling GR00T 2 across tasks and environments requires turning increasingly large and diverse collections of human demonstrations into training-ready data. Our infrastructure processes petabyte-scale monthly input volumes, with individual production jobs using nearly 10,000 vCPUs. At this scale, preparation must sustain both massive data movement and heterogeneous computation: multi-camera video must be retrieved, decoded, and resized. Motion records must be transformed and, where needed, retargeted to the training hand representation, and observations, actions, and annotations must be aligned in time. Recording duration, resolution, encoding, and retargeting requirements vary across sources, so equal numbers of episodes can impose very different I/O and compute demands. The output is a consistent set of indexed multimodal episodes, packaged into training-ready shards (Fig. 69).

**中文:** 要让 GR00T 2 跨任务、跨环境扩展，就必须把规模日益庞大、类型日益多样的人类演示集合转化为可直接用于训练的数据。我们的基础设施每月处理的输入数据量达到 PB 级，单个生产作业使用的 vCPU 接近 10,000 个。在这一规模下，数据准备必须同时承受海量数据搬运与异构计算：多相机视频需要被检索、解码并缩放；运动记录需要被变换，并在需要时重定向到训练所用的手部表示；观测、动作与标注则需要在时间上对齐。录制时长、分辨率、编码方式和重定向需求在不同来源之间差异很大，因此数量相同的片段（episode）可能带来截然不同的 I/O 与算力需求。最终输出是一组一致的、带索引的多模态片段，并被打包成训练就绪分片（shard）（Fig. 69）。

<a id="S2316"></a>
**Source:** p.133 S2316

**Original:** The central challenge is that these conversions share data and compete for limited working storage. A long video can contain many episodes, while one episode can depend on several camera files and separately stored motion records. Staging a shared file once avoids repeated downloads, but its slowest consumer determines when that storage can be reclaimed. A slow conversion or output upload can therefore retain local files, block retrieval of unrelated inputs, and leave compute workers idle. Interruptions compound the problem by adding repeated transfers and expensive recomputation. Sustained throughput requires coordinating data lifetime with execution progress across the entire pipeline.

**中文:** 核心挑战在于，这些转换既共享数据，又争夺有限的工作存储。一段长视频可以包含许多片段，而一个片段又可能依赖多个相机文件和单独存储的运动记录。把共享文件只暂存一次可以避免重复下载，但最慢的消费者决定了该存储何时可以被回收。因此，转换或输出上传变慢，可能导致本地文件被长期保留、阻塞无关输入的检索，并使计算工作节点空闲。中断会带来重复传输和高昂的重新计算，进一步加重这一问题。要维持持续的吞吐量，就需要在整个流水线中协调数据生命周期与执行进度。

<a id="S2317"></a>
**Source:** p.133 S2317

**Original:** The ingestion pipeline coordinates execution with the lifetime of its shared inputs: new work is admitted according to committed storage, dispatched where its inputs reside, and releases capacity only after its outputs are safely uploaded. Active files move directly from object storage to processing nodes, allowing conversion to begin before the entire selected collection has been retrieved. This removes intermediate staging on a shared filesystem while making input placement, retention, and reconstruction explicit responsibilities. Fig. 70 shows the mechanisms supporting this lifecycle.

**中文:** 摄取流水线让执行与其共享输入的生命周期相协调：新工作会依据已承诺（committed）的存储进行准入，派发到其输入所在的位置，并且只有在输出被安全上传之后才释放容量。活跃文件直接从对象存储移动到处理节点，使转换可以在所选集合全部取回之前开始。这样就去掉了共享文件系统上的中间暂存，同时把输入的放置、保留与重建明确为各自的职责。Fig. 70 展示了支撑这一生命周期的机制。

<a id="C104"></a>
**Source:** p.134 C104 · 图 F069

![F069](assets/F069.png)

**Original (caption):** Figure 69: Transformation of human demonstration recordings into aligned multimodal episodes and training-ready dataset shards.

**中文图注：** 图 69：将人类演示录制数据转换为对齐的多模态片段与可直接用于训练的数据集分片的过程。

<a id="S2318"></a>
**Source:** p.134 S2318

**Original:** Admit and place work (Fig. 70, panels B and C). Equal episode counts can imply very different file footprints and sharing patterns, so task limits alone cannot control storage demand. Before downloading an input group, admission accounts for resident files, pending transfers, and output headroom against the node’s budget. Required inputs must be ready before episode dispatch, and consumers execute on the node holding those inputs. Separate Ray worker pools (Moritz et al., 2018) give loading, conversion, and publication independent concurrency. Bounded queues limit outstanding work while storage admission limits the capacity committed to it.

**中文:** 准入并放置工作（Fig. 70，面板 B 与 C）。数量相同的片段可能对应截然不同的文件占用量和共享模式，因此仅靠任务数量限制无法控制存储需求。在下载某个输入组之前，准入会根据节点的预算核算驻留文件、待完成的传输以及输出余量。所需输入必须在片段派发之前就绪，消费者则在持有这些输入的节点上执行。独立的 Ray 工作进程池（Moritz et al., 2018）使加载、转换与发布各自拥有独立的并发度。有界队列限制未完成工作的数量，存储准入则限制分配给这些工作的容量。

<a id="S2319"></a>
**Source:** p.134 S2319

**Original:** Retain inputs through completion, then release capacity (Fig. 70, panels A to C). A downloaded video may serve several episodes, including consumers still waiting for execution. The loader establishes their claims before handing off work, protecting shared inputs across queueing, conversion, and upload. An episode releases its claims only after its intermediate results have been uploaded and temporary outputs cleaned up, while other consumers continue to protect the same files. Once the last claim is released, cleanup can reclaim those files and make room for the next input group. Consumer completion thus governs admission of subsequent inputs. Retrieval, conversion, and shard publication advance asynchronously around this dependency: they overlap across workers without allowing prefetch to grow independently of the storage that unfinished consumers still hold.

**中文:** 在完成前保留输入，然后释放容量（Fig. 70，面板 A 至 C）。一个已下载的视频可能服务于多个片段，其中包括仍在等待执行的消费者。加载器在移交工作之前先为它们建立占用（claim），从而在排队、转换和上传的全过程中保护共享输入。一个片段只有在其中间结果已上传、临时输出已清理之后才释放自己的占用，而其他消费者仍会继续保护同一批文件。一旦最后一个占用被释放，清理程序即可回收这些文件，为下一个输入组腾出空间。因此，消费者的完成情况决定了后续输入的准入。检索、转换与分片发布围绕这一依赖关系异步推进：它们在各工作节点之间相互重叠，但预取不会脱离未完成消费者仍占用的存储而独自增长。

<a id="S2320"></a>
**Source:** p.134 S2320

**Original:** Recover within the same capacity budget (Fig. 70, panel D). Recovery preserves this connection between execution and storage. Stopped attempts release obsolete claims, while lost inputs are reconstructed on an available node through the same admission path before affected episodes retry. Durable conversion-group and publication checkpoints separately identify completed results that job resumption can reuse. Input release after upload and cleanup, and checkpoint-based reuse after restart, are distinct boundaries: an uploaded artifact without recorded completion may still require repeated processing. These rules keep retries within the working-storage budget while preserving reusable progress.

**中文:** 在同一容量预算内恢复（Fig. 70，面板 D）。恢复过程保留了执行与存储之间的这一联系。被中止的尝试会释放已过时的占用，丢失的输入则会通过同一条准入路径在可用节点上重建，之后再重试受影响的片段。持久化的转换组检查点与发布检查点分别标识已完成的结果，作业恢复时可以复用这些结果。上传与清理之后的输入释放，以及重启之后基于检查点的复用，是两个不同的边界：已上传但未记录完成状态的产物，仍可能需要重复处理。这些规则使重试始终处于工作存储预算之内，同时保留可复用的进度。

<a id="S2321"></a>
**Source:** p.134 S2321

**Original:** This coordination of shared-input lifetime, admission, and recovery complements prior work on video analysis, multimodal processing, and prefetching (Poms et al., 2018; Chen et al., 2025; Luan et al., 2026; Dryden et al., 2021).

**中文:** 这种对共享输入生命周期、准入与恢复的协调，与此前关于视频分析、多模态处理和预取的工作形成互补（Poms et al., 2018; Chen et al., 2025; Luan et al., 2026; Dryden et al., 2021）。

<a id="S2322"></a>
**Source:** p.134 S2322

**Original:** Production evaluation. Tab. 36 summarizes throughput and resource use across three production jobs and recovery across five interrupted jobs. Each job uses 100 nodes with 96 vCPUs and 768 GiB of memory per node. The throughput workload covers 1.30 million episodes and about 18,700 demonstration-hours, with three camera views per episode.

**中文:** 生产环境评测。Tab. 36 汇总了三个生产作业的吞吐量与资源使用情况，以及五个被中断作业的恢复情况。每个作业使用 100 个节点，每个节点配备 96 个 vCPU 和 768 GiB 内存。吞吐量测试负载涵盖约 130 万个片段和约 18,700 演示小时，每个片段包含三个相机视角。

<a id="S2323"></a>
**Source:** p.134 S2323

**Original:** Completed-conversion time efficiency is the share of completed conversion time spent on work that did not need to be repeated after interruption.

**中文:** 已完成转换时间的效率，指在已完成的转换时间中，用于中断后无需重复的工作所占的比例。

<a id="C105"></a>
**Source:** p.135 C105 · 图 F070

![F070](assets/F070.png)

**Original (caption):** Figure 70: Multimodal data ingestion: (A) asynchronous overlap, (B) processing stages and the feedback from input release to admission, (C) storage tiers, and (D) recovery. Numbers identify shards, and timings are illustrative. Compute/upload overlap occurs across workers.

**中文图注：** 图 70：多模态数据摄取：(A) 异步重叠，(B) 处理阶段，以及从输入释放到准入的反馈，(C) 存储层级，(D) 恢复。数字用于标识分片，时间数值仅为示意。计算与上传的重叠发生在各工作节点之间。

<a id="C106"></a>
**Source:** p.135 C106 · 表 T036

![T036](assets/T036.png)

**Original (caption):** Table 36: Production evaluation of the data ingestion system. Ranges span jobs. Memory and disk use are per-node means.

**中文表注：** 表 36：数据摄取系统的生产环境评测。范围取值跨作业统计。内存与磁盘使用量为各节点的均值。

<a id="S2326"></a>
**Source:** p.135 S2326

**Original:** Published demonstration duration per job ∼6,240 h Execution time per job 8.0–8.6 h End-to-end throughput 722–780 demonstration-hours/h Time to first training-ready shard ≤28 min Mean worker assignment at 10–80% conversion completion

**中文:** [存疑：表格内容被抽取为单行文本，行列对应关系不明，且最后一项缺少数值，请对照 p.135 核实] 每个作业发布的演示时长 ∼6,240 h；每个作业的执行时间 8.0–8.6 h；端到端吞吐量 722–780 演示小时/小时；首个训练就绪分片的耗时 ≤28 min；转换完成 10–80% 时的平均工作进程分配。


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
