### D.7. Limitations ｜ 局限性

<a id="S1342"></a>
**Source:** p.71 S1342

**Original:** • Relative, suite-specific ratings. Elo measures skill relative to the other checkpoints on the same suite. Ratings from different suites are not comparable, and adding a checkpoint shifts all ratings of a suite by a common constant. • Few independent units. Independent replication comes from distinct tasks, not trials: the first suite has 16 tasks with A/B comparisons, the current one 38. Intervals are correspondingly wide (median 93 Elo on V2, 128 on V1), and some checkpoints with few tasks have none. On V1, one checkpoint’s point estimate (Elo 840) lies outside its own bootstrap interval [853, 995]. We make no claims about it.

**中文:** • 相对性的、按套件区分的评分。Elo 衡量的是某个检查点相对于同一套件中其他检查点的技能。不同套件的评分不可直接比较，而且新增一个检查点会使该套件的所有评分整体平移同一个常数。• 独立单元较少。独立的重复来自不同的任务，而不是试次：第一个套件有 16 个包含 A/B 比较的任务，当前套件有 38 个。置信区间相应地较宽（V2 上的中位数为 93 Elo，V1 上为 128 Elo），而一些任务较少的检查点甚至没有区间。在 V1 上，某个检查点的点估计（Elo 840）落在其自身自助法（bootstrap）区间 [853, 995] 之外。我们不对该结果作任何结论。

![F038](assets/F038.png)

<a id="C052"></a>
**Source:** p.72 C052 · 图 F038

**Original (caption):** Figure 38: Skill versus inference speed on YAM V2. Elo against policy inferences per second (log scale), measured as server-side compute per inference during the same A/B episodes. Bars are 90% Elo intervals, shown for the labelled checkpoints (all intervals are in Fig. 36). Inference-rate intervals are narrower than the markers. Colour is the model family and marker shape the serving stack. Dashed: frontier of point estimates across stacks. Ringed: the checkpoint that dominates all others served by the GR00T 2 policy server.

**中文（图注）：** 图 38：YAM V2 上的技能与推理速度对比。纵轴为 Elo，横轴为每秒策略推理次数（对数刻度），按同一 A/B 回合期间每次推理的服务端计算量测得。柱体为 90% Elo 区间，仅显示带标签的检查点（所有区间见图 36）。推理速率的区间比标记更窄。颜色表示模型系列，标记形状表示服务栈。虚线：跨服务栈的点估计前沿。圈出的检查点：支配由 GR00T 2 策略服务器提供的所有其他检查点的那一个。

<a id="S1366"></a>
**Source:** p.72 S1366

**Original:** • Ties and grading. Ties are 30 to 35% of matches. Rankings come from human operators, and the rubric bounds but does not remove their judgment. • Confounds across campaigns. A/B trials remove drift within a campaign. Differences between stations and operators across campaigns are absorbed only through shared opponents, and the reference-first pairing policy keeps most checkpoints connected to the same opponents. • Live evidence. Graded trials of campaigns still in progress count immediately. Four V2 campaigns were paused at the snapshot, and the comparisons of GR00T 1.7 and 𝜋0.5 rest on campaigns from the last week before it. • Curated metadata. Model-family labels, checkpoint dates (storage timestamps), and serving stacks are recorded or inferred outside the A/B record itself. Embodiment tags and serving settings, such as 𝜋0.5’s separate embodiment tag or video-codec settings, are admission criteria but are not part of the rating.

**中文:** • 平局与评分。平局占全部比赛的 30% 至 35%。排名来自人类操作员，评分细则约束了他们的判断，但并未消除这些判断。• 跨评测批次的混杂因素。A/B 试次消除了同一评测批次（campaign）内的漂移。不同批次之间工位与操作员的差异，只能通过共同对手来吸收；参照优先的配对策略使大多数检查点仍与相同的对手相连。• 实时证据。仍在进行中的评测批次，其已评分的试次会被立即计入。快照时有四个 V2 评测批次处于暂停状态，而 GR00T 1.7 与 π0.5 的比较依赖于其之前最后一周的评测批次。• 人工整理的元数据。模型系列标签、检查点日期（存储时间戳）和服务栈，是在 A/B 记录之外记录或推断的。本体标签与服务设置（例如 π0.5 单独的本体标签或视频编解码器设置）属于准入标准，但不计入评分。

### E. UMIverse for GR00T 2 ｜ GR00T 2 的 UMIverse

<a id="S1367"></a>
**Source:** p.73 S1367

**Original:** UMIverse is our family of robot-free interfaces that record human demonstrations in a robot’s own sensory and action space. Gripper UMI is a handheld parallel gripper in the lineage of the Universal Manipulation Interface (Chi et al., 2024): it carries the robot’s wrist cameras and measures the gripper width that the robot later commands. DexUMI (Xu et al., 2025) is a wearable hand exoskeleton that replicates the kinematics, contact surfaces, and camera mount of a dexterous robot hand, so that every recorded finger joint, fingertip force, and camera view has a robot counterpart. Our GEAR DexUMI (NVIDIA GEAR Team, 2026) replicates the XHAND1 Pro-U (Sec. E.4). Unlike teleoperation, neither interface needs a robot during collection. Unlike human video, both record actions in robot coordinates and observations through robot cameras.

**中文:** UMIverse 是我们的一族无需机器人的接口，用于在机器人自身的感知空间与动作空间中记录人类演示。Gripper UMI 是一款手持式平行夹爪，属于通用操作接口（Universal Manipulation Interface）（Chi et al., 2024）的谱系：它搭载机器人的腕部相机，并测量机器人随后要下达指令的夹爪宽度。DexUMI（Xu et al., 2025）是一种可穿戴的手部外骨骼，复现了灵巧机器人手的运动学、接触面与相机安装位置，因此每一个被记录的手指关节、指尖力与相机视角，在机器人侧都有对应量。我们的 GEAR DexUMI（NVIDIA GEAR Team, 2026）复现的是 XHAND1 Pro-U（Sec. E.4）。与遥操作不同，这两种接口在采集过程中都不需要机器人。与人类视频也不同，两者都以机器人坐标记录动作，并通过机器人相机记录观测。

<a id="S1368"></a>
**Source:** p.73 S1368

**Original:** The two interfaces play complementary roles in GR00T 2. Gripper UMI provides scale: collection stations in three regions supply thousands of hours of bimanual pretraining demonstrations, and the resulting policies deploy directly onto a matching robot (Sec. E.2) or transfer across an embodiment gap to YAM (Sec. B.2), a test of the cross-embodiment imagination that GR00T 2 is built for. DexUMI provides depth: post-training data for complex, long-horizon, and dynamic dexterous tasks (Sec. B.3), which GR00T 2 learns with compliance labels derived from fingertip force (Eqs. (1) and (3)). For DexUMI, the visual gap between the exoskeleton and the robot hand is addressed inside the world-action model rather than by editing video (Sec. E.6). DexUMI demonstrations can also be retargeted to a hand that the exoskeleton does not replicate, such as the Sharpa hand (Sec. B.4). The UMI →YAM transfer and the DexUMI post-training results are presented in Sec. B.2 and B.3. This appendix describes the hardware of both interfaces (Sec. E.1 and E.4), UMI direct (Sec. E.2), the embodiment gaps and ablations of the UMI →YAM transfer (Sec. E.3), and DexUMI’s post-training recipe and WAM-native inpainting (Sec. E.5 and E.6).

**中文:** 这两种接口在 GR00T 2 中扮演互补的角色。Gripper UMI 提供规模：三个地区的采集工位提供了数千小时的双臂预训练演示，所得策略既可以直接部署到匹配的机器人上（Sec. E.2），也可以跨越本体差距迁移到 YAM 上（Sec. B.2），这是对 GR00T 2 所要实现的跨本体想象力（cross-embodiment imagination）的一项检验。DexUMI 提供深度：为复杂、长时序且动态的灵巧任务提供后训练数据（Sec. B.3），GR00T 2 利用由指尖力推导出的柔顺性标签（Eqs. (1) and (3)）学习这些数据。对于 DexUMI，外骨骼与机器人手之间的视觉差异是在世界-动作模型内部处理的，而不是通过编辑视频来解决（Sec. E.6）。DexUMI 的演示也可以重定向到外骨骼并未复现的手上，例如 Sharpa 手（Sec. B.4）。UMI →YAM 迁移与 DexUMI 后训练结果分别见 Sec. B.2 和 B.3。本附录描述两种接口的硬件（Sec. E.1 和 E.4）、UMI direct（Sec. E.2）、UMI →YAM 迁移的本体差距与消融实验（Sec. E.3），以及 DexUMI 的后训练方案与 WAM 原生补全（inpainting）（Sec. E.5 和 E.6）。

### E.1. Gripper UMI Hardware ｜ E.1. Gripper UMI 硬件

<a id="S1369"></a>
**Source:** p.73 S1369

**Original:** The handheld gripper mirrors its robot counterpart. Relative to the original UMI gripper (Chi et al., 2024), the main mechanical change is that the pin joints, bearings, and return springs of the finger-trigger linkage are replaced by a single compliant flexure linkage (Fig. 39) that is printed entirely on a desktop printer. This yields the following improvements over the previous design:

**中文:** 手持夹爪在结构上与其机器人版本保持一致。相较于原始的 UMI 夹爪（Chi et al., 2024），主要的机械改动在于：手指扳机连杆中原有的销轴关节、轴承与回位弹簧，被替换为一个完整的柔顺柔性铰链连杆（flexure linkage）（图 39），并且整体可直接用桌面打印机打印。相较于此前的设计，这带来以下改进：

<a id="S1370"></a>
**Source:** p.73 S1370

**Original:** • Constant force scaling. The finger-to-jaw force scaling is constant over the gripper’s entire range of motion. In the original UMI gripper, the scaling is large when the gripper is fully open but varies nonlinearly with opening, and when the gripper is fully closed the fingertip force falls to roughly 20% of the force applied at the trigger. The constant scaling of the new design instead delivers substantially higher fingertip force at small openings, which is better suited to fine-grained dexterous manipulation. • Fewer parts and faster assembly. The flexure joints are printed directly into the links, so the linkage needs no pins, bearings, or return springs and only a few fasteners, which greatly reduces part count and assembly time. • Simpler linkage and less backlash. The complex multi-part linkage is replaced by a single compliant mechanism with no discrete sliding or pivoting interfaces, which significantly reduces backlash. • Encoder-based width sensing. An encoder measures the gripper opening directly, which avoids the visual occlusion that can affect a camera-and-marker approach to width sensing.

**中文:** • 恒定的力放大比。在夹爪的整个运动范围内，从手指到钳口的力放大比都是恒定的。在原始 UMI 夹爪中，夹爪完全张开时放大比很大，并且会随开合度非线性变化；夹爪完全闭合时，指尖力降至扳机处所施力的约 20%。新设计的恒定放大比则在小开合度下提供明显更大的指尖力，更适合精细的灵巧操作。• 更少的零件与更快的装配。柔性铰链直接打印在连杆之中，因此连杆无需销轴、轴承或回位弹簧，只需少量紧固件，这大幅减少了零件数量和装配时间。• 更简单的连杆与更小的回差（backlash）。复杂的多零件连杆被替换为单一的柔顺机构，不存在离散的滑动或枢转界面，从而显著降低了回差。• 基于编码器的宽度感知。编码器直接测量夹爪开合度，避免了基于相机与标记的宽度感知方法可能受到的视觉遮挡。

<a id="S1371"></a>
**Source:** p.73 S1371

**Original:** Flexure linkage. The linkage is mirror-symmetric and rides on a 150 mm linear rail (MGN9). Rigid links and finger mounts are printed in PLA, and four TPU 90A flexure joints are printed directly into them. Each joint is a short, thin strip with a T-shaped head embedded in a pocket of the PLA part, so load transfers without additional fasteners. The operator’s finger pinch acts on the long links, and the bottom joint is guided along the symmetry plane, so pinch maps to jaw motion through a fixed lever ratio: the jaws move about 2.9× as far as the fingertips and, ideally, carry about 0.35× the finger force. Because the rigid links meet the flexures directly, the operator’s input reaches the jaws through a short, stiff load path with little lost motion.

**中文:** 柔性铰链连杆。连杆呈镜像对称，安装在一条 150 mm 直线导轨（MGN9）上。刚性连杆与手指安装件采用 PLA 打印，四个 TPU 90A 柔性铰链直接打印在其中。每个铰链是一段短而薄的条带，其一端带有 T 形头部，嵌入 PLA 零件的凹槽中，因此载荷传递无需额外紧固件。操作员的手指捏合作用于长连杆，底部铰链沿对称面导向，因此捏合动作通过固定的杠杆比转换为钳口运动：钳口的移动距离约为指尖的 2.9 倍，理想情况下所承受的手指力约为手指力的 0.35 倍。由于刚性连杆直接与柔性铰链相接，操作员的输入经由一条短而刚的载荷路径传递到钳口，几乎没有运动损耗。

<a id="S1372"></a>
**Source:** p.73 S1372

**Original:** Design rules from rapid prototyping.

**中文:** 快速原型制作中的设计规则。

<a id="C053"></a>
**Source:** p.74 C053 · 图 F039

![F039](assets/F039.png)

**Original (caption):** Figure 39: Flexure linkage of the handheld gripper. (a) Cut view at the symmetry plane with main dimensions in mm: black parts are PLA, blue parts are TPU 90A, the gray shape is the operator’s finger contour, and the four TPU joints are numbered 1 to 4 (top, mid, static, bottom). (b) Section views of joints 1 to 4: T-shaped TPU anchors sit in pockets of the PLA parts, and the short exposed strip between them forms the flexure (strip thickness 𝑡and out-of-plane width 𝑤in mm).

**中文（图注）：** 图 39：手持夹爪的柔性铰链连杆。(a) 对称面处的剖视图，主要尺寸单位为 mm：黑色零件为 PLA，蓝色零件为 TPU 90A，灰色轮廓为操作员手指的轮廓，四个 TPU 铰链编号为 1 至 4（顶部、中部、静态、底部）。(b) 铰链 1 至 4 的截面视图：T 形 TPU 锚固件嵌在 PLA 零件的凹槽中，二者之间裸露的短条带构成柔性铰链（条带厚度 𝑡and、面外宽度 𝑤in，单位为 mm）[公式原文见 p.74]。

<a id="S1391"></a>
**Source:** p.74 S1391

**Original:** • Thin strips: strip thickness is set by print accuracy, 1.8 mm (2.3 mm at the top joint), about four extrusion lines, so it prints reliably yet still bends. • Short necks: each exposed neck is kept short so the flexure behaves like a rotary joint, with bending concentrated at one location instead of along a long leaf spring. • Width: links and joints are 23 mm wide out of plane (16 mm for the short link and inner joints). Narrower variants twisted under side loads, while wider ones needed a firm grip to close. • Compliance: the finite compliance of TPU absorbs small mismatches between rail, mounts, and link lengths that a rigid pin-jointed version would not tolerate.

**中文:** • 薄条带：条带厚度由打印精度决定，为 1.8 mm（顶部铰链为 2.3 mm），约等于四条挤出线，因此既能可靠打印，又仍然能够弯曲。• 短颈部：每个裸露的颈部都保持较短，使柔性铰链表现得像一个转动关节，弯曲集中在一处，而不是沿着长片簧分布。• 宽度：连杆与铰链的面外宽度为 23 mm（短连杆与内侧铰链为 16 mm）。较窄的变体在侧向载荷下会扭转，而较宽的变体需要用力抓握才能闭合。• 柔顺性：TPU 有限的柔顺性能够吸收导轨、安装件与连杆长度之间的微小失配，而刚性销接版本无法承受这些失配。

<a id="S1392"></a>
**Source:** p.74 S1392

**Original:** Pre-strained open state. The linkage is printed wider than the rail allows (163.8 mm relaxed pivot span versus 118.1 mm at the rail stops), so the TPU joints are pre-strained at the open stop (Fig. 40). This provides a passive restoring force that returns the gripper to its open state and replaces separate return springs.

**中文:** 预应变张开状态。连杆的打印宽度大于导轨所允许的范围（松弛状态下的枢转跨距为 163.8 mm，而在导轨限位处为 118.1 mm），因此 TPU 铰链在张开限位处处于预应变状态（图 40）。这提供了一个被动的恢复力，使夹爪回到张开状态，并取代了单独的回位弹簧。

<a id="S1393"></a>
**Source:** p.74 S1393

**Original:** End effector. Apart from the added width encoder, sensor placement is kept consistent with the existing UMI configuration, which preserves compatibility with established data-collection pipelines. Further end-effector details, including sensing and assembly, are available in our open-source documentation (NVIDIA GEAR Team, 2026).

**中文:** 末端执行器。除新增的宽度编码器外，传感器布置与现有 UMI 配置保持一致，从而保留了与既有数据采集流程的兼容性。关于末端执行器的更多细节（包括传感与装配），请参阅我们的开源文档（NVIDIA GEAR Team, 2026）。
