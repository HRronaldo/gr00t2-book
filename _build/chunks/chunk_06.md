### 4.4. Learning without Teleoperation: Devices and Pipelines ｜ 无遥操作学习：设备与流程

<a id="S320"></a>
**Source:** p.17 S320

**Original:** GR00T 2 learns a skill on a robot from demonstrations recorded without that robot (Sec. 3.2). In all four sources below, the demonstrations specify the task. For human motion capture and the Gripper UMI, whose devices differ from the robot, task-agnostic data from the target robot specify the embodiment, and cross-embodiment pretraining connects the two. The DexUMI exoskeleton replicates the robot hand it is built for, so on that hand its demonstrations need no robot play data (Sec. 4.4.3). Capture and conversion remove what can be removed before training, namely differences in camera geometry (Sec. C.1.3), kinematics, and action semantics

**中文:** GR00T 2 从未操作该机器人时录制的演示中学习技能（见第 3.2 节）。下列四种来源中，演示都指明了任务。对于人体动作捕捉和 Gripper UMI 这两种与机器人设备不同的来源，目标机器人的任务无关数据用于指定本体（embodiment），跨本体预训练则把两者连接起来。DexUMI 外骨骼复刻了其所适配的机器人手，因此在该手上，其演示无需机器人自由操作数据（robot play data）（见第 4.4.3 节）。采集与转换环节会在训练前尽量消除可消除的差异，即相机几何（见第 C.1.3 节）、运动学以及动作语义上的差异。

![F012](assets/F012.png)

<a id="C013"></a>
**Source:** p.18 C013 · 图 F012

**Original (caption):** Figure 12: GR00T 2 learns new robot tasks from human demonstrations. (1) A person performs the task wearing GMSL head and wrist cameras at robot-matched poses, PICO controllers that track 6-DoF wrist poses, and Manus gloves that track finger joints. (2) Retargeting maps each wrist pose to the 7-DoF arm and each hand pose to the 22-DoF hand, and the video stays unmodified. (3) GR00T 2 co-trains on the retargeted human demonstrations and on robot data of other tasks: videos supervise video prediction, and human and robot actions train one shared action head. (4) On the robot, GR00T 2 takes the observation and the instruction, predicts a sequence of future frames, and outputs the actions the robot executes. No teleoperated demonstration of the new task enters training.

**中文（图注）：** 图 12：GR00T 2 从人类演示中学习新的机器人任务。(1) 人员佩戴与机器人姿态匹配的 GMSL 头部与腕部相机，同时手持追踪 6-DoF 腕部位姿的 PICO 控制器，并戴上追踪手指关节的 Manus 手套来完成任务。(2) 重定向把每个腕部位姿映射到 7-DoF 手臂，把每个手部位姿映射到 22-DoF 手，视频保持不修改。(3) GR00T 2 在重定向后的人类演示与其他任务的机器人数据上联合训练：视频用于监督视频预测，人类动作与机器人动作共同训练同一个动作头。(4) 在机器人上，GR00T 2 接收观测与指令，预测未来若干帧的序列，并输出机器人执行的动作。训练中不包含新任务的任何遥操作演示。

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

**中文（图注）：** 图 13：人类演示与 GR00T 2 预测。两个仅由人类演示过的任务。给定一帧机器人起始画面与指令，GR00T 2 预测机器人的第一人称视角。时间以起始帧为起点计算。人类演示（上方各行）仅出现在训练中。全部四个任务见图 28。

![F013](assets/F013.png)

<a id="C015"></a>
**Source:** p.19 C015 · 图 F014

**Original (caption):** Figure 14: GR00T 2-generated future frames on YAM, without and with YAM co-training. Both models observe the same YAM top-camera frame (left) and predict eight future steps of Toy Dumptruck Assembly, a task demonstrated only with Gripper UMI. Trained on UMI data alone (top), GR00T 2 renders human arms and the blue UMI fingers entering the scene. Co-trained with task-agnostic YAM data (bottom), it renders YAM’s own arms. The co-training data supply the robot’s appearance as well as its action statistics.

**中文（图注）：** 图 14：GR00T 2 在 YAM 上生成的未来帧，分别为未经 YAM 联合训练与经过 YAM 联合训练的结果。两个模型观测到相同的 YAM 顶部相机画面（左），并预测 Toy Dumptruck Assembly 任务的八个未来步。该任务仅用 Gripper UMI 演示。仅用 UMI 数据训练时（上方），GR00T 2 渲染出人手与蓝色 UMI 手指进入画面。与任务无关的 YAM 数据联合训练后（下方），它渲染出的是 YAM 自身的手臂。联合训练数据既提供了机器人的外观，也提供了其动作统计特性。

![F014](assets/F014.png)

<a id="C016"></a>
**Source:** p.19 C016 · 图 F015

**Original (caption):** Figure 15: DexUMI demonstration and GR00T 2 rollout. Prepare Banana Yogurt, with keyframes numbered by subtask: a person demonstrating the task with the DexUMI exoskeletons (top) and a GR00T 2 rollout on a Tianji robot with XHAND1 Pro-U hands (bottom). The task is demonstrated only with DexUMI. All three DexUMI tasks are shown in Fig. 30.

**中文（图注）：** 图 15：DexUMI 演示与 GR00T 2 的 rollout（轨迹采样）。Prepare Banana Yogurt 任务，关键帧按子任务编号：上方为人员佩戴 DexUMI 外骨骼演示该任务，下方为 GR00T 2 在搭配 XHAND1 Pro-U 手的 Tianji 机器人上的 rollout。该任务仅用 DexUMI 演示。全部三个 DexUMI 任务见图 30。

![F015](assets/F015.png)

<a id="S346"></a>
**Source:** p.19 S346

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

**中文（图注）：** 图 16：GR00T 2 的人类到仿真再到现实的迁移（Human-to-sim-to-real）。(1) 人到仿真环节从一次人类演示中重建资产与运动。(2) 强化学习在仿真中训练基于状态的操作策略。(3) 在扰动下采集数据，扩展状态覆盖范围并捕获恢复行为。(4) GR00T 2 仅在仿真数据上微调，并以零样本方式部署到真实世界。

![F016](assets/F016.png)

<a id="S372"></a>
**Source:** p.20 S372

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
