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

![F026](assets/F026.png)

<a id="C029"></a>
**Source:** p.45 C029 · 图 F026

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

![F027](assets/F027.png)

<a id="C030"></a>
**Source:** p.46 C030 · 图 F027

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
