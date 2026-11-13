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

![F030](assets/F030.png)

<a id="C035"></a>
**Source:** p.51 C035 · 图 F030

**Original (caption):** Figure 30: DexUMI tasks. Each block shows one task with six keyframes, numbered by subtask as in Tab. 5: a person demonstrating the task with the DexUMI exoskeletons (top) and a GR00T 2 rollout on a Tianji robot with XHAND1 Pro-U hands (bottom). Prepare Banana Yogurt and Scoop Granola are the two halves of one continuous make-breakfast demonstration and rollout, and every task is demonstrated only with DexUMI.

**中文（图注）：** Figure 30：DexUMI 任务。每个区块展示一项任务的六个关键帧，按 Tab. 5 中的子任务编号排列：上排为人使用 DexUMI 外骨骼演示该任务，下排为 GR00T 2 在配备 XHAND1 Pro-U 手的 Tianji 机器人上的 rollout（轨迹采样）。准备香蕉酸奶与舀取格兰诺拉麦片是一段连续“做早餐”演示与 rollout 的两半，且每项任务都只用 DexUMI 演示。

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

![E001](assets/equations/E001.png)

<a id="E001"></a>
**Source:** p.52 E001

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
