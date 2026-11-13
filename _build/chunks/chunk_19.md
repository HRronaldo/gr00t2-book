### E.2. UMI Direct ｜ UMI 直接部署

<a id="S1394"></a>
**Source:** p.74 S1394

**Original:** UMI direct means deploying a UMI-trained policy on the corresponding UMI robot gripper, the robot counterpart of the handheld: the same sensors (the same camera board with its fisheye wrist camera and trigger camera), the same gripper kinematics (two soft-fingered carriages driven symmetrically along a rail), and the same gripper fingers. Observations and actions therefore carry over without translation: the policy sees the scene through the cameras it was trained on and commands the finger width the handheld measured, so the camera and gripper gaps are removed by construction (Sec. E.1). The robot side exchanges poses in the handheld’s wrist frame, which a per-robot hand-eye calibration maps onto the robot, and gripper widths in millimetres, the quantity the handheld measured. A policy trained on grasp-point poses and normalized widths (Sec. B.2) is wrapped so that its outputs are converted back to these quantities. On the deployment robot, the policy

**中文:** UMI 直接部署是指将基于 UMI 训练的策略部署到对应的 UMI 机器人夹爪上，该夹爪是手持设备的机器人版本：传感器相同（同一块相机板，包括鱼眼腕部相机和触发相机），夹爪运动学相同（两个软指滑块沿导轨对称驱动），夹爪手指也相同。因此，观测和动作无需转换即可直接迁移：策略通过训练时所用的相机观察场景，并下达手持设备所测得的手指宽度指令，所以相机和夹爪方面的差距在构造上即已消除（Sec. E.1）。机器人一侧以手持设备的腕部坐标系交换位姿，再经由每台机器人各自的手眼标定映射到机器人上；夹爪宽度以毫米为单位，即手持设备所测量的量。基于抓取点位姿和归一化宽度训练的策略（Sec. B.2）会被包装，使其输出换算回这些量。在部署机器人上，该策略

![F040](assets/F040.png)

<a id="C054"></a>
**Source:** p.75 C054 · 图 F040

**Original (caption):** Figure 40: Pre-strain and motion of the flexure linkage. (a) Relaxed (printed) shape (dashed) and its pose at the open stop (solid). The 22.858 mm difference per side pre-strains the TPU joints. (b) Shadows of the linkage closing from the open stop to the closed pose: the finger mounts slide inward along the rail and the bottom joint moves along the symmetry plane.

**中文（图注）：** 柔性铰链机构的预应变与运动。(a) 松弛（打印）形状（虚线）及其在张开限位处的姿态（实线）。每侧 22.858 mm 的差值会对 TPU 关节施加预应变。(b) 连杆从张开限位闭合到闭合姿态的阴影图：手指安装座沿导轨向内滑动，底部关节沿对称平面移动。

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

### E.3. UMI →YAM Transfer: Embodiment Gaps and Ablations ｜ UMI→YAM 迁移：本体差距与消融实验

<a id="S1405"></a>
**Source:** p.75 S1405

**Original:** As described in Sec. 3.2 and Sec. B.2, GR00T 2 can be adapted to a bimanual gripper robot from handheld Gripper UMI demonstrations alone, with no teleoperation of the target robot. In this section, we present the details behind that result: how co-training lets the model absorb the appearance difference on its own (Fig. 14),

**中文:** 如 Sec. 3.2 和 Sec. B.2 所述，GR00T 2 仅凭手持 Gripper UMI 演示即可适配到双臂夹爪机器人，无需对目标机器人进行遥操作。本节给出该结果背后的细节：联合训练如何让模型自行吸收外观差异（Fig. 14），

![F041](assets/F041.png)

<a id="C055"></a>
**Source:** p.76 C055 · 图 F041

**Original (caption):** Figure 41: UMI direct rollouts. Each row shows one task with its instruction and six keyframes of a GR00T 2 policy post-trained on Gripper UMI demonstrations alone and deployed on the UMI robot gripper, numbered by stage: Toy Dumptruck Assembly, Toy Plane Assembly, Bluey Car Assembly, and Monster Truck Assembly. Each task requires placing parts, driving screws, and reorienting the body of the toy.

**中文（图注）：** UMI 直接部署的 rollout。每行展示一项任务，包括其指令以及一个 GR00T 2 策略的六个关键帧。该策略仅在 Gripper UMI 演示上进行后训练，并部署在 UMI 机器人夹爪上，关键帧按阶段编号。任务包括 Toy Dumptruck Assembly、Toy Plane Assembly、Bluey Car Assembly 和 Monster Truck Assembly。每项任务都需要放置零件、拧入螺钉，并调整玩具主体的朝向。

![T015](assets/T015.png)

<a id="C056"></a>
**Source:** p.76 C056 · 表 T015

**Original (caption):** Table 15: UMI direct. Prog. is the average substage score and SR the end-to-end success rate on the UMI robot gripper, both on a 0 to 100 scale, of GR00T 2 post-trained on Gripper UMI demonstrations alone. GR00T 2 w/o UMI pretraining starts from an earlier pretraining checkpoint whose mixture contains no UMI-10K data, while GR00T 2 starts from the default checkpoint, whose pretraining mixture includes UMI-10K. Each task uses 10 trials, and the last row averages the four tasks. Bold marks the best Prog. and SR in each row.

**中文（表注）：** UMI 直接部署。任务进度（Prog.）为各子阶段分数的平均值，成功率（SR）为 UMI 机器人夹爪上的端到端成功率，两者均为 0 到 100 的刻度，对象是仅在 Gripper UMI 演示上后训练的 GR00T 2。GR00T 2 w/o UMI pretraining 从一个更早的预训练检查点出发，其数据配比不含 UMI-10K；GR00T 2 则从默认检查点出发，其预训练数据配比包含 UMI-10K。每项任务使用 10 次试次，最后一行为四项任务的平均值。每行中最优的 Prog. 和 SR 以粗体标出。

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

![T016](assets/T016.png)

<a id="C057"></a>
**Source:** p.77 C057 · 表 T016

**Original (caption):** Table 16: Gripper UMI versus YAM. YAM differs from the handheld gripper in its cameras, its gripper interface, and its control frame.

**中文（表注）：** Gripper UMI 与 YAM 的对比。YAM 在相机、夹爪接口和控制坐标系上与手持夹爪不同。

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

**Original (caption):** Figure 42: Gripper UMI versus YAM, same task, same camera slots. Top: a Gripper UMI demonstration of Toy Dumptruck Assembly seen through its wide-FOV head camera and two fisheye wrist cameras, recorded in the wild. Bottom: the YAM robot performing the task in its cell, seen through the standard-FOV top camera and two wrist RealSense cameras that fill the same observation slots. Right: the handheld UMI gripper and the YAM gripper, each with its wrist camera. The lines mark the full opening between the fingertips (85.55 mm and 96 mm). Both frames show the same step: the left gripper holds the truck while the right gripper brings the second wheel to the axle.

**中文（图注）：** Gripper UMI 与 YAM 对比，同一任务，同样的相机槽位。上方：Gripper UMI 演示 Toy Dumptruck Assembly，通过宽视场头部相机和两路鱼眼腕部相机在野外采集。下方：YAM 机器人在其工作单元中执行同一任务，通过标准视场顶部相机和两路 RealSense 腕部相机观察，这些相机占据相同的观测槽位。右侧：手持 UMI 夹爪与 YAM 夹爪，各自带有腕部相机。线条标出指尖之间的完整开口（85.55 mm 和 96 mm）。两帧展示的是同一步骤：左侧夹爪夹住卡车，右侧夹爪将第二个车轮送到车轴上。

![F043](assets/F043.png)

<a id="C059"></a>
**Source:** p.78 C059 · 图 F043

**Original (caption):** Figure 43: Wrist views for UMI →YAM transfer. The same UMI wrist frame as (a) the raw fisheye, (b) the stereographic view used in pretraining, and (c) the YAM-aligned re-render that imitates YAM’s wrist camera. (d) The real YAM wrist camera at the same step.

**中文（图注）：** UMI→YAM 迁移的腕部视图。同一 UMI 腕部画面的 (a) 原始鱼眼图像、(b) 预训练中使用的立体投影视图，以及 (c) 模仿 YAM 腕部相机的 YAM 对齐重渲染。(d) 同一步骤下真实的 YAM 腕部相机画面。

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

![T017](assets/T017.png)

<a id="C060"></a>
**Source:** p.79 C060 · 表 T017

**Original (caption):** Table 17: UMI →YAM ablations. Prog. is the average substage score and SR the end-to-end success rate on YAM, both on a 0 to 100 scale, as in Tab. 4. The shaded row in each block is the default configuration (shared action head, YAM-aligned wrist-view warping, all UMI episodes, pretraining with UMI-10K data), and the other rows change that one choice. For Conveyor Belt Sorting and Tossing, SR is the share of 50 items sorted, and there is no separate progress score. Bold marks the best value in each block.

**中文（表注）：** UMI→YAM 消融实验。任务进度（Prog.）为 YAM 上各子阶段分数的平均值，成功率（SR）为端到端成功率，两者均为 0 到 100 的刻度，与 Tab. 4 相同。每个区块中的阴影行为默认配置（共享动作头、YAM 对齐的腕部视图扭曲、全部 UMI 片段、包含 UMI-10K 数据的预训练），其他行则只改变其中一项选择。对于 Conveyor Belt Sorting and Tossing，SR 为 50 件物品中被分拣的占比，没有单独的进度分数。每个区块中的最佳值以粗体标出。

<a id="S1460"></a>
**Source:** p.79 S1460

**Original:** Ablation 1: shared versus separate action head. GR00T 2 shares its diffusion transformer across embodiments but keeps one row of action-encoder, state-encoder, and action-decoder weights per embodiment. The sharedhead arm re-expresses UMI in YAM’s semantics and places it on YAM’s row: grasp-site poses, absolute widths normalized by the 85.55 mm full opening, the first 20 of YAM’s 32 action dimensions, and YAM’s normalization statistics. The separate-head arm keeps UMI on the row it was pretrained on, with wrist-frame relative poses, relative widths in millimetres, and its own statistics. The separate arm therefore changes the action representation as well as the head, so the comparison is not a single-variable change. The two arms trade embodiment grounding against skill coverage, and the results in Tab. 17 split along that line. The shared head is clearly stronger on Toy Dumptruck Assembly (60% versus 10%) and Conveyor Belt Sorting and Tossing (86% versus 64%), whereas the separate head is slightly better on NIST Board Disassembly (60% versus 50%, progress 93 versus 86). The NIST margin is concentrated in the hex-nut subtask, which the separate head completes in 7 of 10 trials and the shared head in 5 of 10. This is also the subtask on which the demonstrations are most specific: the UMI demonstrators slide the nut off its post without rotating the wrist, and the YAM co-training data do not contain this way of removing a nut. With the shared head, UMI actions are decoded by the same weights as the YAM data, so the decoder’s prior follows YAM’s motion statistics, and a strategy that appears only in the demonstrations is reproduced less reliably. The separate head keeps UMI on the row it was pretrained on and preserves the demonstrators’ strategy. The same mechanism explains the reverse outcome on the other two tasks: where the demonstrated motions are ones the YAM data already perform, placing UMI on YAM’s row grounds the task evidence directly in YAM’s action statistics and controller, whereas the separate head must rely on the transformer to map YAM observations onto a row it has never seen paired with them. The shared head is therefore the better default, while the separate head helps only where the demonstrations rely on a motion strategy that the co-training data do not share.

**中文:** 消融实验 1：共享动作头与独立动作头。GR00T 2 在各本体之间共享其扩散 Transformer，但为每个本体保留一组动作编码器、状态编码器和动作解码器权重。共享头方案[存疑：原文 "sharedhead" 疑为漏空格]将 UMI 重新表达为 YAM 的语义，并放在 YAM 的动作行上：抓取点位姿、以 85.55 mm 全开口归一化的绝对宽度、YAM 32 个动作维度中的前 20 维，以及 YAM 的归一化统计量。独立头方案则让 UMI 保留在其预训练时所在的行上，使用腕部坐标系下的相对位姿、以毫米为单位的相对宽度以及其自身的统计量。因此，独立方案同时改变了动作表示和动作头，两者的对比并非单变量改变。两种方案是在本体锚定与技能覆盖之间做取舍，Tab. 17 中的结果恰好沿此方向分化。共享头在 Toy Dumptruck Assembly（60% 对 10%）和 Conveyor Belt Sorting and Tossing（86% 对 64%）上明显更强，而独立头在 NIST Board Disassembly（60% 对 50%，进度 93 对 86）上略胜一筹。NIST 上的优势集中在六角螺母子任务上：独立头在 10 次试次中完成了 7 次，共享头则完成了 5 次。这也是演示最具特殊性的子任务：UMI 演示者不转动手腕，而是将螺母从其柱子上滑下来，而 YAM 联合训练数据中不包含这种取出螺母的方式。使用共享头时，UMI 动作由与 YAM 数据相同的权重解码，因此解码器的先验遵循 YAM 的运动统计，而仅出现在演示中的策略则被复现得不够可靠。独立头使 UMI 保留在其预训练所在的行上，从而保留了演示者的策略。同样的机制也解释了另外两项任务上的相反结果：当演示的运动正是 YAM 数据已经执行过的动作时，把 UMI 放在 YAM 的行上可以将任务证据直接锚定到 YAM 的动作统计量和控制器上，而独立头则必须依靠 Transformer 将 YAM 观测映射到一个从未与之配对过的行上。因此，共享头是更好的默认选择，而独立头只在演示依赖于联合训练数据并不共享的运动策略时才有帮助。
