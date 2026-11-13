### C. Data for GR00T 2 ｜ 附录 C：GR00T 2 的数据

<a id="S1018"></a>
**Source:** p.57 S1018

**Original:** This appendix details the sources and roles of data for GR00T 2 summarized in Sec. 4.2.

**中文:** 本附录详述 Sec. 4.2 概述的 GR00T 2 各数据来源及其作用。

### C.1. Human Data for GR00T 2 ｜ C.1 GR00T 2 的人类数据

<a id="S1019"></a>
**Source:** p.57 S1019

**Original:** Prior work in scaling data for robot learning has showcased emergent transfer and generalization through scaling egocentric data (Kareer et al., 2025; Punamiya et al., 2026; Zheng et al., 2026).

**中文:** 在机器人学习的数据规模化方面，既有工作已经展示了通过扩展第一人称数据而出现的迁移与泛化能力（Kareer et al., 2025; Punamiya et al., 2026; Zheng et al., 2026）。

<a id="S1020"></a>
**Source:** p.57 S1020

**Original:** Human-1M is a large and diverse egocentric dataset curated by NVIDIA, which supplies the large scale human experience data in GR00T 2’s cross embodiment training mixture. Human-1M contains approximately 1 million hours of proficient human labor sensorized with egocentric cameras, dense language annotation, SLAM and hand pose estimation which are filtered down. The collection spans different environments and sensing configurations, including monocular and stereo head cameras and additional wrist views. We additionally incorporate capture setups that bring human observations closer to those of dexterous robots to examine the transfer of human data at various hierarchies.

**中文:** Human-1M 是 NVIDIA 整理的一个大规模、多样化的第一人称数据集，为 GR00T 2 的跨本体训练配比提供大规模人类经验数据。Human-1M 包含约 100 万小时的熟练人类劳动，用第一人称相机做传感器化记录，并配有密集语言标注、SLAM 与手部位姿估计，随后经过过滤。采集覆盖不同环境与传感配置，包括单目与立体头戴相机，以及额外的腕部视角。我们还引入了使人类观测更接近灵巧机器人观测的采集装置，以考察人类数据在不同层级上的迁移。

<a id="S1021"></a>
**Source:** p.57 S1021

**Original:** C.1.1. Dataset Composition

**中文:** C.1.1 数据集构成

<a id="S1022"></a>
**Source:** p.57 S1022

**Original:** The Human-1M inventory used within GR00T 2 contains 402,730 hours across approximately 13.75 million episodes, spanning over 51,500 unique collectors and 123,000 scenes.

**中文:** GR00T 2 中实际使用的 Human-1M 库存包含 402,730 小时、约 1,375 万条 episode，覆盖 51,500 名以上不重复的采集者与 123,000 个场景。

<a id="S1023"></a>
**Source:** p.57 S1023

**Original:** Collection Settings. We collect demonstrations in both natural “in-the-wild” and controlled studio environments. In-the-wild collection captures proficient laborers in economically valuable scenarios across households, industry workplaces, agriculture, commercial kitchens, service, retail, and logistics. Studio collection concentrates on tabletop manipulation under standardized protocols, resembling demonstration style robotics datasets. Studio data comprises of assembly tasks that involve assembling various kits, curated tasks selected to cover target robot skills and task distributions. Within studio data, “in-lab” collection follows a stricter protocol where demonstrators keep both hands in view, avoid idle periods, and perform motions at speeds chosen to match the robot. Approximately 80,000 hours of the total mixture is studio data. These settings serve complementary purposes. Natural environments broaden the range of interactions observed during pretraining for the world-action model, while controlled collection makes it possible to target particular skills and capture them under more consistent conditions for better transfer to the downstream robot embodiments.

**中文:** 采集设置。我们在自然的"野外"环境与受控的影棚环境中都采集演示。野外采集记录熟练劳动者在具有经济价值的场景中的作业，涵盖家庭、工业工作场所、农业、商业厨房、服务业、零售与物流。影棚采集聚焦标准化协议下的桌面操作，形态类似演示风格的机器人数据集。影棚数据由装配任务构成，涉及组装各类套件，以及为覆盖目标机器人技能与任务分布而挑选的定制任务。在影棚数据中，"实验室内"（in-lab）采集遵循更严格的协议：演示者保持双手在视野内、避免空转时段，并以与机器人匹配的速度完成动作。整个配比中约 80,000 小时为影棚数据。这些设置互为补充：自然环境拓宽了世界-动作模型预训练时观察到的交互范围；受控采集则使针对特定技能、在更一致条件下采集成为可能，从而更好地迁移到下游机器人本体。

<a id="S1024"></a>
**Source:** p.57 S1024

**Original:** Egocentric Cameras. The dataset includes monocular and stereo egocentric recordings. Monocular setups use a single head-mounted RGB camera. Stereo setups provide synchronized two camera RGB head views with optional additional multi-view cameras for better hand pose estimation.

**中文:** 第一人称相机。数据集包含单目与立体第一人称录制。单目配置使用单个头戴 RGB 相机。立体配置提供同步的双相机 RGB 头部视角，并可选用额外的多视角相机以改善手部位姿估计。

<a id="S1025"></a>
**Source:** p.57 S1025

**Original:** Wrist Cameras. Approximately 90,000 hours of the collection also includes wrist cameras, which provide close-up views of manipulation and hand-object interactions to reduce partial observability during fine-grained manipulation. Additionally, a portion of the studio data contains robot-aligned wrist viewpoints to address the visual alignment gap.

**中文:** 腕部相机。约 90,000 小时的采集还包含腕部相机，提供操作与手-物交互的近景视角，以减少细粒度操作中的部分可观测性。此外，一部分影棚数据包含与机器人对齐的腕部视角，用以解决视觉对齐差距。

<a id="S1026"></a>
**Source:** p.57 S1026

**Original:** Even when humans and robots perform the same grasp, wrist-camera placement can change the apparent size and orientation of the hand and object, as well as the visibility of their interaction. We studied this alignment process with the Sharpa platform. We screened 13 initial mount designs and conducted a controlled comparison of four mounts across four operators. The human and robot perform the same four thumb-finger grasps and their viewpoints are compared in a 640x480 image frame. The evaluation measured hand-object overlap, object scale, camera-to-object distance, and camera orientation. We further optimized image rotation and scaling for visual alignment, and used ChArUco (Garrido-Jurado et al., 2014) calibration together with directional motions to optimize angular alignment.

**中文:** 即使人与机器人执行同一个抓取，腕部相机的安装位置也会改变手与物体的表观尺寸和朝向，以及二者交互的可见程度。我们用 Sharpa 平台研究了这一对齐过程。我们筛选了 13 种初始安装设计，并在四名操作员上对四种安装座做了受控比较。人与机器人执行同样的四种拇指-手指抓取，并在 640×480 的图像帧中比较二者的视角。评测测量手-物重叠度、物体尺度、相机到物体的距离以及相机朝向。我们进一步优化图像旋转与缩放以实现视觉对齐，并使用 ChArUco（Garrido-Jurado et al., 2014）标定配合定向运动来优化角度对齐。

<a id="S1027"></a>
**Source:** p.57 S1027

**Original:** Annotations. Each egocentric episode contains language annotations along with frame-aligned estimations of hand and head motion following prior work on learning from egocentric human experience (Kareer et al., 2025; Punamiya et al., 2026).

**中文:** 标注。每条第一人称 episode 都包含语言标注，以及与视频帧对齐的手部与头部运动估计，做法沿用从第一人称人类经验中学习的既有工作（Kareer et al., 2025; Punamiya et al., 2026）。

<a id="S1028"></a>
**Source:** p.58 S1028

**Original:** Hand and Camera Pose. Hand motion is represented by 21 three-dimensional keypoints per hand: the wrist and four landmarks along each finger, including the fingertips. Keypoint positions are expressed in meters in the reference head-camera coordinate frame and aligned with the corresponding video frames. Head motion is represented by the six-degree-of-freedom pose of the head-mounted reference camera, estimated using simultaneous localization and mapping (SLAM) in a canonical per episode world frame.

**中文:** 手部与相机位姿。手部运动由每只手 21 个三维关键点表示：腕部，以及每根手指上的四个标志点（含指尖）。关键点位置以米为单位、在参考头戴相机坐标系中表达，并与对应视频帧对齐。头部运动由头戴参考相机的六自由度位姿表示，用同步定位与建图（SLAM）在每条 episode 各自的标准世界坐标系中估计。

<a id="S1029"></a>
**Source:** p.58 S1029

**Original:** Language Annotation. Language describes demonstrations at two levels. Tier 1 (T1) annotations provide a one- to two-sentence episode summary identifying the primary goal, major actions, and key objects. Tier 2 (T2) annotations describe individual actions in contiguous, timestamped segments of 1-10 seconds. Each description is self-contained and specifies the relevant hand, action, and objects. These annotations support language-conditioned learning and task-based data curation. The language annotations are validated by human quality control checks. The highest quality annotations are used for the training mixture of Flora pipeline described in Sec. C.4. The Flora pipeline is then used to further enrich or provide T2 language annotations across the dataset.

**中文:** 语言标注。语言在两个层级上描述演示。第 1 层（T1）标注提供一到两句话的 episode 摘要，指明主要目标、主要动作与关键物体。第 2 层（T2）标注以 1–10 秒的连续、带时间戳的片段描述单个动作。每条描述自包含，并指明相关的手、动作与物体。这些标注支撑语言条件学习与基于任务的数据整理。语言标注经人工质量控制检查验证。质量最高的标注用于 Sec. C.4 所述 Flora 流程的训练配比。随后再用 Flora 流程在整个数据集上进一步丰富或补足 T2 语言标注。

<a id="S1030"></a>
**Source:** p.58 S1030

**Original:** C.1.2. Data Filtering and Quality Control

**中文:** C.1.2 数据过滤与质量控制

<a id="S1031"></a>
**Source:** p.58 S1031

**Original:** The usefulness of a human demonstration for tabletop manipulation settings depends on both the interaction it contains and the reliability of its recorded motion. We therefore apply quality control at two levels. Batch-level review checks the content and annotations of a delivery, while quantitative filtering selects timesteps with sufficiently stable observations and hand trajectories. Additional details about the quality control are in the accompanying Human-1M dataset release.

**中文:** 一条人类演示对桌面操作场景是否有用，既取决于它包含的交互，也取决于其记录运动的可靠性。因此我们在两个层级上做质量控制。批次级审核检查一次交付的内容与标注；定量过滤则挑选观测与手部轨迹足够稳定的时间步。关于质量控制的更多细节见随 Human-1M 数据集发布的说明。

<a id="S1032"></a>
**Source:** p.58 S1032

**Original:** Human review. Human auditors check language-annotation validity, task quality and idle time as per our collection specs at a 95% per episode pass rate. These criteria screen deliveries before individual training timesteps are selected by the quantitative filters.

**中文:** 人工审核。人工审核员按我们的采集规范检查语言标注有效性、任务质量与空转时间，要求每条 episode 通过率 95%。这些准则在定量过滤器挑选单个训练时间步之前，先对交付批次做筛选。

<a id="S1033"></a>
**Source:** p.58 S1033

**Original:** Quantitative Filtering. At each candidate training timestep, we evaluate a window extending 24 frames into the past and 48 frames into the future. We retain the timestep only if all quality criteria pass over this window. The checks constrain head rotation and translation, hand visibility, consistency of reconstructed bone lengths, and wrist speed (Tab. 8). The bone-length error of a hand in a frame is the median absolute deviation of its 20 finger-bone lengths from their per-episode medians, divided by the mean of those medians, so the threshold of 0.05 corresponds to 5% of the mean bone length.

**中文:** 定量过滤。对每个候选训练时间步，我们评估一个向前 24 帧、向后 48 帧的窗口。只有当全部质量准则在该窗口上都通过时，我们才保留该时间步。检查项约束头部旋转与平移、手部可见性、重建骨长的一致性以及腕部速度（Tab. 8）。某帧中某只手的骨长误差定义为：20 根手指骨长相对其本 episode 中位数的中位绝对偏差，除以这些中位数的均值；因此阈值 0.05 对应平均骨长的 5%。

![T008](assets/T008.png)

<a id="C039"></a>
**Source:** p.58 C039 · 表 T008

**Original (caption):** Table 8: Quantitative criteria for selecting training timesteps.

**中文表注：** 表 8：用于挑选训练时间步的定量准则。
