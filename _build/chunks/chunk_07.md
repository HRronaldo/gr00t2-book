### 4.5. Simulation and Evaluation ｜ 4.5 仿真与评测

<a id="S376"></a>
**Source:** p.20 S376

**Original:** Simulation serves GR00T 2 in two roles. Physics simulation of digital twins of our real-world tasks provides a fast, repeatable, and calibrated proxy for real-robot evaluation, which we use throughout development (Sec. 4.5.1 and 4.5.2). Neural simulation with a learned world model, adapted from recorded rollouts, provides an environment for reinforcement learning (Sec. 4.5.3). We also evaluate GR00T 2 on five public simulation benchmarks (Sec. 4.5.4).

**中文:** 仿真在 GR00T 2 的研发中承担两种角色。针对真实任务构建的数字孪生（digital twin）物理仿真，为真机评测提供了快速、可重复且经过校准的代理，我们在整个开发过程中都在使用它（见 Sec. 4.5.1 和 4.5.2）。基于学习得到的世界模型、并利用录制的轨迹采样（rollout）数据加以适配的神经仿真，为强化学习提供了环境（见 Sec. 4.5.3）。我们还在五个公开仿真基准测试上评估了 GR00T 2（见 Sec. 4.5.4）。

![F017](assets/F017.png)

<a id="C018"></a>
**Source:** p.21 C018 · 图 F017

**Original (caption):** Figure 17: Real-world tasks and their simulated counterparts. Each pair shows the real workcell’s top camera (Real) and the same moment when the recorded robot commands are replayed in simulation (Sim), for five general manipulation tasks and one stage of the multi-stage airplane assembly. More tasks are shown in Fig. 61.

**中文（图注）：** 真实任务及其仿真对应物。每组图像展示真实工作单元（workcell）的顶部相机画面（Real），以及同一时刻将录制的机器人指令在仿真中回放的画面（Sim），涵盖五项通用操作任务，以及多阶段飞机装配中的一个阶段。更多任务见 Fig. 61。

![F018](assets/F018.png)

<a id="C019"></a>
**Source:** p.21 C019 · 图 F018

**Original (caption):** Figure 18: Simulated vs. real-world performance per policy. (a) Task progress (mean rubric score) and (b) success rate, averaged over 25 tasks (dashed: y = x). (c) Bradley-Terry Elo ratings fitted separately to pairwise outcomes in simulation and in real-world A/B evaluations (dashed: least-squares fit, since the two Elo scales differ). r: Pearson, 𝜌: Spearman, MMRV: mean maximum rank violation. Each point is a generalist checkpoint of GR00T 2 trained for the YAM embodiment.

**中文（图注）：** 按策略划分的仿真与真实世界表现对比。(a) 任务进度（平均评分标准得分，mean rubric score）与 (b) 成功率，均在 25 项任务上取平均（虚线：y = x）。(c) 分别依据仿真中与真实世界 A/B 评测中的成对结果拟合的 Bradley-Terry Elo 评分（虚线：最小二乘拟合，因为两套 Elo 尺度不同）。r：Pearson 相关系数，𝜌：Spearman 秩相关系数，MMRV：平均最大秩违例（mean maximum rank violation）。每个点都是针对 YAM 本体训练的 GR00T 2 通用检查点。

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
