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

### 4. How We Made GR00T 2 ｜ 我们如何构建 GR00T 2

<a id="S266"></a>
**Source:** p.14 S266

**Original:** This section describes the methods behind GR00T 2, focusing on the key design decisions, while the appendix provides the full details. Sec. 4.1 presents the training recipe, from pretraining to RL post-training, and Sec. 4.2 the training data. Sec. 4.3 describes how we benchmark checkpoints against each other on real robots. Sec. 4.4 describes the capture devices and pipelines for learning without teleoperation, Sec. 4.5 the simulation and evaluation framework, Sec. 4.6 real-time deployment, and Sec. 4.7 the training and data infrastructure.

**中文:** 本节介绍 GR00T 2 背后的方法，重点讨论关键设计决策，完整细节见附录。Sec. 4.1 介绍从预训练到 RL 后训练的训练方案，Sec. 4.2 介绍训练数据。Sec. 4.3 描述如何在真实机器人上对检查点进行相互基准测试。Sec. 4.4 描述无需遥操作即可学习时所用的采集设备与流水线，Sec. 4.5 介绍仿真与评测框架，Sec. 4.6 介绍实时部署，Sec. 4.7 介绍训练与数据基础设施。

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

**中文（图注）：** 预训练中的人类视频规模扩展。在 Human-1M 数据上以 0%、1%、10% 或 100% 的比例进行预训练，再使用 Dexter 遥操作数据进行后训练，并在 72 个任务上评估。真实机器人：每个任务 3 个轨迹采样回合。由操作员判定二元成功，由视觉语言模型给出任务进度评分。视频轨迹采样：对每个任务，从 3 个记录的初始配置出发，每个配置使用 10 个生成种子进行自回归视频生成。由视觉语言模型判断成功并给出任务进度评分。我们报告任务进度（%）与成功率，误差线为 ±1 SEM。

<a id="S287"></a>
**Source:** p.15 S287

**Original:** completion detector as the reward (Sec. F.5). An online infrastructure coordinates robot interaction, training, and evaluation, and retains experience across interruptions (Sec. F.3).

**中文:** 完成检测器（completion detector）作为奖励（Sec. F.5）。一套在线基础设施负责协调机器人交互、训练与评测，并在中断之后保留经验（Sec. F.3）。
