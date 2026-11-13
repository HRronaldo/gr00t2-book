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

![T009](assets/T009.png)

<a id="C040"></a>
**Source:** p.59 C040 · 表 T009

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

![T010](assets/T010.png)

<a id="C041"></a>
**Source:** p.61 C041 · 表 T010

**Original (caption):** Table 10: UMI-10K for GR00T 2. Gripper UMI episodes in the pretraining corpus.

**中文表注：** 表 10：供 GR00T 2 使用的 UMI-10K。预训练语料中的夹爪 UMI episode。

![F032](assets/F032.png)

<a id="C042"></a>
**Source:** p.61 C042 · 图 F032

**Original (caption):** Figure 32: Skill distribution of the Gripper UMI corpus. Episodes per skill on a logarithmic scale, colored by skill group. An episode counts toward every skill its instruction exercises. Pick-and-place is the most common skill, but 88% of episodes also exercise at least one other skill.

**中文图注：** 图 32：夹爪 UMI 语料的技能分布。每项技能的 episode 数（对数刻度），按技能组着色。一条 episode 计入其指令所涉及的每一项技能。抓取-放置是最常见的技能，但 88% 的 episode 还涉及至少一项其他技能。
