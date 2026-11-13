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

![T011](assets/T011.png)

<a id="C043"></a>
**Source:** p.62 C043 · 表 T011

**Original (caption):** Table 11: Robot teleoperation data in the GR00T 2 pretraining mixture. Share is the fraction of robot-data samples drawn from each source.

**中文（表注）：** 表 11：GR00T 2 预训练数据配比中的机器人遥操作数据。Share 为从各数据源抽取的机器人数据样本所占的比例。

<a id="S1120"></a>
**Source:** p.62 S1120

**Original:** with objects from an object inventory into task templates, which are linted, deduplicated against every existing task. A human then inspects each task and manually accepts or rejects it. Each template is instantiated into concrete tasks by sampling different object, count, color, and position, which yields counterfactual pairs that share a scene but differ in one attribute of the instruction, and each generation round under-samples skills that are already common. The result is broad compositional coverage: 2,798 distinct skill-object pairs, with 70% of the top-24-skill by top-30-object grid populated.

**中文:** 将物体清单中的物体填入任务模板，这些模板经过规范检查，并与所有已有任务做去重。随后由人工逐条检查任务，并手动接受或拒绝。每个模板通过采样不同的物体、数量、颜色和位置被实例化为具体任务，由此得到的反事实对共享同一场景，但指令中只有一个属性不同；每一轮生成也会对已经常见的技能进行欠采样。最终形成了广泛的组合覆盖：共 2,798 种不同的技能-物体对，在由前 24 项技能与前 30 个物体构成的网格中，有 70% 的格子被填充。

<a id="S1121"></a>
**Source:** p.62 S1121

**Original:** Quality control. Every episode passes a three-stage quality pipeline before it enters the corpus. First, an autonomous station-side check rejects recordings with uneven frame timing, dropped frames, or tracking and gripper faults at the point of capture. Second, an agentic QC pipeline reviews each remaining episode from its videos and instruction and scores four aspects: task completion (every step of the instruction is carried out on the objects, counts, and targets the instruction names, and the result is left in the specified state), motion quality (no micro-adjustments, jerky or abrupt movements, or idle hesitation), scene validity (a clean workspace without distracting or occluding objects or people), and view quality (both grippers and the task area visible in every camera); an episode is rejected on any critical failure or on a low aspect score. Third, human reviewers audit the agent’s verdicts on sampled and disputed episodes against a golden set, and their corrections feed back into the judge. Together these stages filter out roughly a quarter of recorded episodes (about 11% at the station and 16% at the agentic gate), so the corpus contains only clean, instruction-faithful demonstrations whose motion reflects natural human manipulation: the 95th-percentile gripper speed within an episode is 0.28 m/s on each arm, and peak speeds exceed 0.68 m/s in a tenth of the episodes.

**中文:** 质量控制。每条片段在进入语料前都要经过三阶段质量流水线。第一，工位端的自动检查会在采集时直接剔除帧时间不均匀、丢帧，或跟踪与夹爪故障的录制。第二，智能体化的 QC 流水线根据视频和指令审查每条剩余片段，并对四个方面打分：任务完成度（指令中的每一步都在指令所指定的物体、数量和目标上执行，且结果保持在指定状态）、动作质量（没有微调、抖动或突兀动作，也没有空闲迟疑）、场景有效性（工作区整洁，没有分散注意力或遮挡的物体或人员），以及视角质量（每个相机中都能看到两个夹爪和任务区域）。只要出现任何关键失败或某一方面得分过低，片段即被剔除。第三，人工审核员针对抽检和有争议的片段，对照黄金集（golden set）审核智能体的判定，其修正结果会反馈给判定器（judge）。这些阶段合计过滤掉约四分之一的录制片段（工位端约 11%，智能体关卡约 16%），因此语料中只保留干净、与指令一致的演示，其动作体现了人类自然的操作方式：片段内夹爪速度的第 95 百分位在每条手臂上为 0.28 m/s，十分之一的片段峰值速度超过 0.68 m/s。

### C.3. Teleoperation Data for GR00T 2 ｜ 面向 GR00T 2 的遥操作数据

<a id="S1123"></a>
**Source:** p.62 S1123

**Original:** GR00T 2 pretrains on about 23.5k hours and 1.16M episodes of teleoperation from six sources. They span bimanual parallel-gripper arms, bimanual arms with dexterous hands, a humanoid, and a single-arm manipulator (Tab. 11).

**中文:** GR00T 2 在来自六个数据源的约 23.5k 小时、1.16M 条遥操作片段上进行预训练。这些数据涵盖双臂平行夹爪机械臂、带灵巧手的双臂机械臂、一台人形机器人，以及一台单臂操作器（Tab. 11）。

<a id="S1124"></a>
**Source:** p.62 S1124

**Original:** Embodiments and sources. Bimanual parallel-gripper data come from YAM arms and make up the largest block: 18.7k hours covering a broad range of household and tabletop tasks, including 3.6k hours from ABC- 130k (XDOF, 2026). Dexterous data come from bimanual arms with multi-fingered hands. The Sharpa data (22-DoF Sharpa hands) cover 2.9k hours, and Wuji (20-DoF Wuji hands on 7-DoF Tianji arms) adds 1.3k hours. Humanoid data come from the Unitree G1 (App. H), and DROID (Khazatsky et al., 2024) contributes single-arm Franka data from 564 scenes. Every bimanual platform records a head or top-down view and two wrist views.

**中文:** 本体与数据来源。双臂平行夹爪数据来自 YAM 机械臂，是占比最大的部分：18.7k 小时，覆盖广泛的家庭与桌面任务，其中包括来自 ABC-130k（XDOF, 2026）的 3.6k 小时。灵巧数据来自配备多指手的双臂机械臂。Sharpa 数据（22-DoF Sharpa 手）覆盖 2.9k 小时，Wuji（7-DoF Tianji 机械臂上装配的 20-DoF Wuji 手）增加了 1.3k 小时。人形机器人数据来自 Unitree G1（App. H），DROID（Khazatsky et al., 2024）则提供来自 564 个场景的单臂 Franka 数据。每个双臂平台都记录一路头部或俯视视角，以及两路腕部视角。

![F033](assets/F033.png)

<a id="C044"></a>
**Source:** p.63 C044 · 图 F033

**Original (caption):** Figure 33: Teleoperation system for Tianji + Sharpa. (A) Teleoperation pipeline from operator devices to the robot. The retargeter is the solver used for human-data conversion. (B) Robot platform: Tianji arms, Sharpa hands, and the GEAR Neck. (C) Key upgrades: hardware, numbered at their location in (B), and software.

**中文（图注）：** 图 33：Tianji + Sharpa 的遥操作系统。（A）从操作员设备到机器人的遥操作流水线。重定向器（retargeter）是用于人类数据转换的求解器。（B）机器人平台：Tianji 机械臂、Sharpa 手和 GEAR Neck。（C）关键升级：硬件（编号位置对应（B）中的位置）和软件。

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
