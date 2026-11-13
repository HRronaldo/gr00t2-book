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

![F054](assets/F054.png)

<a id="C074"></a>
**Source:** p.102 C074 · 图 F054

**Original (caption):** Figure 54: Why SFT + Agent episodes fail. Primary cause of manually reviewed failed SFT + Agent episodes: 87 on RoboCasa365 and 80 on RoboDojo.

**中文（图注）：** 图 54：SFT + Agent 回合失败的原因。人工复核的失败 SFT + Agent 回合的主要原因：RoboCasa365 上 87 次，RoboDojo 上 80 次。

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

### G.2. Agentic Steering with Visual Guidance ｜ 智能体化视觉引导

<a id="S1887"></a>
**Source:** p.102 S1887

**Original:** Agentic skill composition and recovery (Sec. G.1) integrates GR00T 2 with external CaP programs and skills, whereas agentic steering keeps GR00T 2 as the only controller and lets the agent shape its behavior through the WAM API. We first describe the three parts of visual steering, in which the agent adds visual guidance to its language instructions: the interface, the agent loop, and the mid-training of GR00T 2. We then evaluate visual steering on short- and long-horizon benchmarks on YAM and Dexter.

**中文:** 智能体化技能组合与恢复（见 Sec. G.1）将 GR00T 2 与外部 CaP 程序和技能相结合，而智能体化引导（agentic steering）则让 GR00T 2 仍作为唯一控制器，由智能体通过 WAM API 塑造其行为。我们首先描述视觉引导的三个组成部分：智能体在语言指令之上叠加视觉引导的交互界面、智能体循环，以及 GR00T 2 的中期训练（mid-training）。随后，我们在 YAM 和 Dexter 上，分别于短时序与长时序基准中评估视觉引导。

<a id="S1888"></a>
**Source:** p.102 S1888

**Original:** Visual Guidance Interface. The interface separates what and where from how. For each step, the agent names the acting arm and gives a grasp point and a release point as pixel coordinates in the image of one scene camera (Tab. 21), while GR00T 2 determines the grasp pose, the approach, and all motion in between. We observed that GR00T 2 conditions strongly on fine visual details in its conditioning frames, so we pass the points by drawing them as markers directly on the conditioning frame rather than through a separate input: a filled disc for the grasp point and a plus-shaped cross for the release point, in the acting arm’s color (magenta for the left arm, cyan for the right), as in Fig. 8a. Only the acting arm is marked, and only on the current frame of the scene camera. Alongside the markers, GR00T 2 receives the agent’s per-step instruction, which names the

**中文:** 视觉引导接口。该接口将“做什么、在哪里做”与“怎么做”分开。对于每一步，智能体指定执行动作的手臂，并以某一场景相机图像（Tab. 21）中的像素坐标给出抓取点和释放点，而 GR00T 2 负责决定抓取位姿、接近方式以及其间的全部运动。我们观察到，GR00T 2 对其条件帧中的精细视觉细节高度敏感，因此我们不通过单独的输入传递这些点，而是把它们直接画在条件帧上作为标记：抓取点用实心圆盘表示，释放点用加号形十字表示，颜色取执行动作手臂的颜色（左臂为品红色，右臂为青色），如图 8a 所示。只标记执行动作的手臂，并且只标记场景相机的当前帧。除标记外，GR00T 2 还接收智能体的逐步指令，该指令指明

![F055](assets/F055.png)

<a id="C075"></a>
**Source:** p.103 C075 · 图 F055

**Original (caption):** Figure 55: Real-world tasks. (A) Toy Plane assembly: dump the parts, attach and fasten the bottom wing, turn the airplane over, and fasten the top wing. (B) Toy Tractor assembly: dump the parts, fasten the wheels on one side, turn the body over, and complete the other side. (C) Hot Wheels assembly: dump the parts, mount and fasten four wheels, and install and fasten the hood. (D) Multi-cable insertion: plug five Ethernet cables into a network switch. (E) Multi-charger insertion: plug five chargers into a power strip.

**中文（图注）：** 图 55：真实世界任务。（A）玩具飞机装配：倒出零件，安装并拧紧下机翼，将飞机翻转，再拧紧上机翼。（B）玩具拖拉机装配：倒出零件，拧紧一侧的车轮，将车身翻转，并完成另一侧。（C）Hot Wheels 装配：倒出零件，安装并拧紧四个车轮，再安装并拧紧引擎盖。（D）多线缆插接：将五根以太网线缆插入网络交换机。（E）多充电器插接：将五个充电器插入排插。

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

![T021](assets/T021.png)

<a id="C076"></a>
**Source:** p.104 C076 · 表 T021

**Original (caption):** Table 21: Embodiment-specific choices for visual steering. Everything not listed follows the shared rules in the text. The Dexter column describes the joint YAM and Dexter recipe used for Dexter trash sorting.

**中文（表注）：** 表 21：视觉引导的本体专用设置。未列出的内容均遵循正文中的共享规则。Dexter 一列描述的是用于 Dexter 垃圾分类的 YAM 与 Dexter 联合配方。

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

![F056](assets/F056.png)

<a id="C077"></a>
**Source:** p.105 C077 · 图 F056

**Original (caption):** Figure 56: Short-horizon instruction following benchmark on YAM. Eight reference categories, each illustrated by a shared starting scene and two contrasting instructions. Blue and orange text denote the alternatives, and all remaining wording is identical. The panel labeled Constraint shows an exclusion reference.

**中文（图注）：** 图 56：YAM 上的短时序指令遵循基准。八个参考类别各由一个共享的起始场景和两条对比指令加以说明。蓝色与橙色文字表示两种备选，其余措辞完全相同。标为 Constraint 的面板展示的是排除参考。

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

![T022](assets/T022.png)

<a id="C078"></a>
**Source:** p.106 C078 · 表 T022

**Original (caption):** Table 22: Visual steering results on every benchmark. Short horizon: success rate (%), with successful trials in parentheses (pass@1 on YAM). Long horizon: full-task successes over episodes, with the mean rubric score (0 to 1) in parentheses. 𝑛counts trials (short horizon) or episodes (long horizon). The success rates and full-task counts are the components averaged in Fig. 8. †Obtained with an earlier implementation of the model.

**中文（表注）：** 表 22：每个基准上的视觉引导结果。短时序：成功率（%），括号内为成功试验数（YAM 为 pass@1）。长时序：按回合计的全任务成功数，括号内为平均评分细则分数（0 至 1）。𝑛 表示试验数（短时序）或回合数（长时序）。成功率和全任务成功数即图 8 中取平均所用的组成部分。†由该模型的早期实现获得。

![T023](assets/T023.png)

<a id="C079"></a>
**Source:** p.106 C079 · 表 T023

**Original (caption):** Table 23: YAM short-horizon pass@1 (%) by reference category. Each category has six instructions and 18 scored trials per setting.

**中文（表注）：** 表 23：YAM 短时序 pass@1（%），按参考类别划分。每个类别包含六条指令，每种设置下计分的试验为 18 次。

<a id="S1945"></a>
**Source:** p.106 S1945

**Original:** (8.3 points), where GR00T 2 already reaches 75.0%.

**中文:** （8.3 个百分点），其中 GR00T 2 已达到 75.0%。

<a id="S1946"></a>
**Source:** p.106 S1946

**Original:** Guidance Following. Success rates alone do not show that GR00T 2 follows the guidance, because a steerable policy should change its behavior when only the guidance changes (Chen et al., 2026d). The counterfactual pairs of the YAM short-horizon benchmark are designed to test a system-level version of this: within a pair, the scene is fixed and only the requested behavior changes. Counting a pair as solved if both of its instructions succeed in at least two of three trials, GR00T 2 solves 4 of the 24 pairs (16.7%), language guidance 10 (41.7%), and visual guidance 19 (79.2%). Conversely, 24 of the 60 successful trials of GR00T 2 (40.0%) come from instructions whose counterpart fails all three trials, as expected from a policy that repeats one behavior regardless of the instruction. This share falls to 12.5% (10 of 80) with language guidance and 5.8% (7 of 120) with visual guidance. On YAM trash sorting, GR00T 2 also follows the arm assignment: with visual guidance, the marked (and named) arm made 169 of 172 gripper closures (98.3%), against 164 of 181 (90.6%) for the named arm with language guidance, so wrong-arm closures fall from 9.4% to 1.7%. Its releases also follow the markers: with visual guidance, every release aimed at a bin landed in the marked bin, with one case unclear, whereas with language guidance, 21 items went into a wrong bin, or a different item was moved, after the agent had named the correct bin (see Failure Analysis).

**中文:** 指引遵循。仅看成功率并不能说明 GR00T 2 是否遵循了指引，因为一个可引导的策略应当在且仅在指引改变时改变其行为（Chen et al., 2026d）。YAM 短时序基准的反事实对正是为了从系统层面检验这一点而设计：在同一对中，场景固定，只有所要求的行为发生变化。若一对中的两条指令在三次试验中各自至少成功两次，则该对视为已解决。按此标准，GR00T 2 解决了 24 对中的 4 对（16.7%），语言引导解决了 10 对（41.7%），视觉引导解决了 19 对（79.2%）。反过来，GR00T 2 的 60 次成功试验中，有 24 次（40.0%）来自其对应指令三次试验全部失败的指令，这与一个无论指令如何都重复同一行为的策略的预期一致。语言引导下这一比例降至 12.5%（80 次中的 10 次），视觉引导下则降至 5.8%（120 次中的 7 次）。在 YAM 垃圾分类中，GR00T 2 也遵循了手臂分配：使用视觉引导时，被标记（并被命名）的手臂完成了 172 次夹爪闭合中的 169 次（98.3%），而语言引导下被命名手臂则为 181 次中的 164 次（90.6%），因此错误手臂的闭合率从 9.4% 降至 1.7%。它的释放也遵循标记：使用视觉引导时，每一次指向容器的释放都落入被标记的容器，仅有一例不明确；而使用语言引导时，在智能体已命名正确容器之后，仍有 21 件物品落入错误容器，或移动了另一件物品（见失败分析）。
