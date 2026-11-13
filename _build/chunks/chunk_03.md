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

![F005](assets/F005.png)

<a id="C006"></a>
**Source:** p.10 C006 · 图 F005

**Original (caption):** Figure 5: Real-robot post-training on four contact-rich manipulation tasks. Labels report success rates, and whiskers are 95% Wilson intervals over 50 trials per bar. Bold marks each task’s best method. GRPO and GRPO-induced self-imitation update GR00T 2 directly, whereas residual RL learns a correction policy on top of a frozen GR00T 2. GRPO-induced self-imitation trains on successful GRPO rollouts. *Evaluated with CPS sampling noise.

**中文（图注）：** 图 5：四项富接触操作任务上的真机后训练。标签为成功率，误差线为每个柱体基于 50 次试次计算的 95% Wilson 区间。加粗表示各任务的最佳方法。GRPO 与 GRPO 诱导的自模仿直接更新 GR00T 2，而残差 RL 在冻结的 GR00T 2 之上学习修正策略。GRPO 诱导的自模仿在成功的 GRPO rollout 上训练。*使用保系数采样（CPS）的采样噪声进行评测。

![F006](assets/F006.png)

<a id="C007"></a>
**Source:** p.10 C007 · 图 F006

**Original (caption):** Figure 6: Agentic runtime architecture. System 2 monitors execution and invokes GR00T 2 and CaP tools through an observe-reason-act-verify loop. GR00T 2 or ASPIRE-generated program serves as execution backends with shared execution environment interface.

**中文（图注）：** 图 6：智能体化运行时架构。系统 2（S2）通过“观察-推理-行动-验证”循环监控执行，并调用 GR00T 2 与代码即策略（code-as-policy, CaP）工具。GR00T 2 或 ASPIRE 生成的程序均可作为执行后端，共享同一执行环境接口。

<a id="S190"></a>
**Source:** p.10 S190

**Original:** on contact-rich manipulation. The resulting skills can be integrated into agentic execution for more complex, long-horizon tasks (Sec. 3.4), as we will introduce next.

**中文:** [存疑：文本从句中开始，句首缺失] 在接触密集型操作上。所得技能可以整合进智能体化执行，用于更复杂的长时序任务（Sec. 3.4），下文将对此作介绍。

### 3.4. Agentic GR00T 2 ｜ 3.4. 智能体化 GR00T 2

<a id="S191"></a>
**Source:** p.10 S191

**Original:** A frontier multimodal agent and GR00T 2 address complementary parts of a task. The agent determines what to do: it decomposes long tasks, monitors progress, and writes code. GR00T 2 determines how to do it, performing the contact-rich manipulation that is difficult to script. The agent serves as System 2 and calls GR00T 2 as a tool alongside camera, state, and CaP tools (Fig. 6). It supports GR00T 2 in four ways. Augment: for tasks that need memory or explicit reasoning, the agent runs a task-level program that calls GR00T 2 for each manipulation step. Together with RL post-training, this puts GR00T 2 first on both the RoboCasa365 (Nasiriany et al., 2026) and RoboDojo (Chen et al., 2026a) leaderboards (Tab. 19). Assist: on real robots, the agent watches GR00T 2 and, when it sees a dropped part or stalled progress, repairs the state with a CaP skill and hands control back, lifting a post-trained GR00T 2 to near-perfect success on three cluttered assembly tasks (Fig. 7). Guide: beyond language, the agent can steer GR00T 2 with visual targets through the WAM API, described below. Improve: an autonomous research agent discovered the basis of the RL recipe we use to post-train GR00T 2 (Sec. 4.1

**中文:** 一个前沿多模态智能体与 GR00T 2 分别负责任务的互补部分。智能体决定做什么：它分解长任务、监控进展并编写代码。GR00T 2 决定怎样做，执行那些难以脚本化的富接触操作。智能体作为系统 2（S2），与相机、状态和 CaP 工具一并，将 GR00T 2 当作工具来调用（Fig. 6）。它以四种方式支持 GR00T 2。增强（Augment）：对于需要记忆或显式推理的任务，智能体运行一个任务级程序，为每个操作步骤调用 GR00T 2。结合 RL 后训练，这使 GR00T 2 在 RoboCasa365（Nasiriany et al., 2026）和 RoboDojo（Chen et al., 2026a）两个排行榜上均居首位（Tab. 19）。辅助（Assist）：在真实机器人上，智能体观察 GR00T 2 的执行过程，当其发现零件掉落或进展停滞时，用 CaP 技能修复状态并将控制权交还，使经过后训练的 GR00T 2 在三项杂乱装配任务上接近完美的成功率（Fig. 7）。引导（Guide）：除语言之外，智能体还可以通过 WAM API 用视觉目标引导 GR00T 2，下文将介绍。改进（Improve）：一个自主研究智能体发现了我们用于 GR00T 2 后训练的 RL 方案的基础（Sec. 4.1 [存疑：文本在此截断]

![F007](assets/F007.png)

<a id="C008"></a>
**Source:** p.11 C008 · 图 F007

**Original (caption):** Figure 7: Agentic assistance on real robots. (a) Successful trials out of 100 per method on three long-horizon assembly tasks on YAM. Before every trial a person randomly dumps all parts onto the table, a cluttered starting configuration never seen in post-training and much harder than the arranged layouts of Tab. 1a. A trial that needed human help counts as a failure. The agent lifts GR00T 2 after SFT + DAgger to at least 97% on all three tasks. (b) Full-task success over 20 repeated-insertion episodes with SFT and RL-post-trained GR00T 2 in the same agentic framework. RL post-training raises success from 60% to 95% on multi-cable and from 10% to 100% on multi-charger insertion.

**中文（图注）：** 图 7：真实机器人上的智能体辅助。(a) 在 YAM 上完成三项长时序装配任务时，每种方法 100 次试次中的成功次数。每次试次前，由人工随机将所有零件倒在桌面上，形成从未在后训练中出现过的杂乱起始配置，难度远高于 Tab. 1a 中整齐排列的布局。需要人工帮助的试次计为失败。经 SFT + DAgger 后的 GR00T 2 在智能体辅助下，三项任务均至少达到 97%。(b) 在同一智能体化框架中，使用 SFT 与经 RL 后训练的 GR00T 2，对 20 个重复插入回合的整任务成功率。RL 后训练将多线缆插入的成功率从 60% 提升至 95%，将多充电器插入的成功率从 10% 提升至 100%。

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

**中文（图注）：** 图 8：在两个评测层级上，采用视觉引导（visual steering）均取得更高的平均成功率。(a) 左手与右手的引导示例。圆圈标记抓取目标，叉号标记释放目标，颜色标识执行动作的手臂。(b, c) 为基准成功率的等权平均值，而非汇总后的试次成功率。短时序结果取两个基准的平均值（每种配置分别为 144 和 64 次试次；Dexter 基准采用模型的早期实现获得）；长时序结果则平均三种机器人-任务组合：两台机器人上的垃圾分拣（各 20 个回合），以及仅在 YAM 上进行的板件拆卸压力测试（10 个回合）。各机器人的具体协议与结果见 Sec. G.2。

<a id="S218"></a>
**Source:** p.12 S218

**Original:** We evaluate this approach on two embodiments, YAM and Dexter, in two tiers: short-horizon benchmarks test only a few steps instruction following, while long-horizon benchmarks require completing an entire trash-sorting task on both robots, plus board disassembly on YAM as a stress test. Short-horizon instructions are organized by reference type to assess distinct grounding requirements (nominal, spatial, ordinal, cardinal, arm, and object-exclusion references) and execution requirements (action and grasp references). Sec. G.2 details this taxonomy together with the evaluation protocols, individual benchmarks, and instruction-category breakdowns. We compare three settings: GR00T 2 given the original task instruction, GR00T 2 given the agent’s language guidance, and the point-conditioned GR00T 2 given the agent’s language guidance and visual markers. Visual steering achieves the highest average success in both tiers: benchmark-mean success of 76.8% on short-horizon tasks and mean full-task success of 53.3% on long-horizon tasks, compared with 44.2% and 1.7% using the agent’s language guidance alone (Fig. 8).

**中文:** 我们在两种本体（embodiment）YAM 和 Dexter 上、以两个层级评测该方法：短时序基准仅测试少量步骤的指令遵循能力，而长时序基准要求在两台机器人上完成整个垃圾分拣任务，并在 YAM 上加测板件拆卸作为压力测试。短时序指令按指代类型组织，以评估不同的定位需求（名义、空间、序数、基数、手臂和排除物体指代），以及执行需求（动作指代与抓取指代）。Sec. G.2 详细介绍了该分类体系，以及评测协议、各个基准和指令类别的细分结果。我们比较了三种设置：给定原始任务指令的 GR00T 2、给定智能体语言指导的 GR00T 2，以及同时给定智能体语言指导与视觉标记、以点为条件的 GR00T 2。视觉引导在两个层级上均取得最高平均成功率：短时序任务的基准平均成功率为 76.8%，长时序任务的平均整任务成功率为 53.3%；而仅使用智能体语言指导时，分别为 44.2% 和 1.7%（Fig. 8）。

<a id="S219"></a>
**Source:** p.12 S219

**Original:** Despite these gains, grasp and release points cannot convey every task requirement. The markers specify spatial

**中文:** 尽管有这些收益，抓取点与释放点仍无法传达每一项任务要求。这些标记指定的是空间 [存疑：文本在此截断]

![F009](assets/F009.png)

<a id="C010"></a>
**Source:** p.13 C010 · 图 F009

**Original (caption):** Figure 9: Three-level stack for whole-body loco-manipulation. An optional reasoning model (S2) picks the task and the prompt. GR00T 2 Turbo (S1) reads RGB images and proprioception and predicts 1.6 s chunks of SONIC whole-body motion tokens at about 1 Hz. SONIC (S0) decodes the tokens into joint position targets at 50 Hz, which the robot’s PD controller tracks at 1000 Hz. S1 runs onboard on an NVIDIA Jetson AGX Thor, and S0 runs onboard on an NVIDIA Jetson Orin NX.

**中文（图注）：** 图 9：用于全身移动操作的三层堆栈。一个可选的推理模型（S2）负责选择任务与提示。GR00T 2 Turbo（S1）读取 RGB 图像与本体感知状态，并以约 1 Hz 的频率预测 1.6 秒长的 SONIC 全身运动 token 块。SONIC（S0）将这些 token 解码为 50 Hz 的关节位置目标，再由机器人的 PD 控制器以 1000 Hz 进行跟踪。S1 运行在机载的 NVIDIA Jetson AGX Thor 上，S0 运行在机载的 NVIDIA Jetson Orin NX 上。

<a id="S262"></a>
**Source:** p.13 S262

**Original:** targets, not a complete manipulation strategy: requirements such as placing an object on its side, pouring, or scooping still depend on language and GR00T 2’s learned skills. Richer guidance, including target 6D object poses, goal images, or affordance-based marking, could extend this interface.

**中文:** [存疑：文本从句中开始，句首缺失] 目标，而不是完整的操作策略：诸如将物体侧放、倾倒或舀取等要求，仍然依赖语言以及 GR00T 2 习得的技能。更丰富的指导，包括目标 6D 物体位姿、目标图像或基于可供性（affordance）的标记，可以扩展这一接口。
