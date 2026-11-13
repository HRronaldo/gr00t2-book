### E.4. DexUMI Exoskeleton Hardware ｜ E.4. DexUMI 外骨骼硬件

<a id="S1468"></a>
**Source:** p.81 S1468

**Original:** The GEAR DexUMI exoskeleton (NVIDIA GEAR Team, 2026) replicates the kinematics of the target robot hand (XHAND1 Pro-U) joint for joint and reproduces its fingertip and palm contact surfaces, which keeps the visual and physical gap to the robot small for policy training. It is also designed for wearability, so that operators can comfortably collect high-quality data across long, dexterous tasks. Compared with the original DexUMI, it offers the following improvements:

**中文:** GEAR DexUMI 外骨骼（NVIDIA GEAR Team, 2026）逐关节复刻了目标机器人手（XHAND1 Pro-U）的运动学，并还原了其指尖与手掌的接触表面，使策略训练时人手采集环境与机器人之间的视觉和物理差距保持较小。该外骨骼还考虑了穿戴性，使操作员能够舒适地在长时序、灵巧的任务中采集高质量数据。与原始 DexUMI 相比，它有以下改进：

<a id="S1470"></a>
**Source:** p.81 S1470

**Original:** • More degrees of freedom. The exoskeleton captures 16 degrees of freedom, using 20 joints of which four pairs are coupled. • Higher precision and durability. Machined parts give higher precision and durability. • No over-constraint, better tracking and wearability. Removing non-essential contact surfaces and adopting a remote-center-of-motion (RCM) linkage resolves the over-constraint of the original structure. The structure flexes less, which improves tracking precision and wearability. • Daisy-chained encoders. The joint encoders are daisy-chained, which simplifies cable management. • Left and right hands. Both left- and right-hand versions are available, enabling bimanual tasks.

**中文:** • 更多自由度。该外骨骼可采集 16 个自由度，使用 20 个关节，其中四对关节存在耦合。• 更高的精度与耐久性。机加工零件带来更高的精度与耐久性。• 消除过约束，跟踪与穿戴性更好。去除非必要的接触表面，并采用远程运动中心（RCM）连杆机构，解决了原结构的过约束问题。结构形变更小，从而提升了跟踪精度与穿戴性。• 编码器串联。各关节编码器采用串联连接，简化了线缆管理。• 左手与右手版本。左右手版本均可提供，支持双臂任务。

<a id="S1471"></a>
**Source:** p.81 S1471

**Original:** Remote-center-of-motion joints. Matching the robot hand’s abduction/adduction (AB/AD) and flexion joints is a packaging problem, since those joint centers lie where the operator’s finger is. We replicate them with an RCM linkage that creates a virtual joint at the robot hand’s joint center without placing hardware in the operator’s workspace (Fig. 44a). The RCM is a parallel four-bar linkage. To avoid over-constraining it, only two of the four holes at the top joint are used. Leaving the other two unused reduces binding from manufacturing tolerances and keeps motion smooth.

**中文:** 远程运动中心关节。要匹配机器人手的外展/内收（AB/AD）关节与屈曲关节，是一个封装问题，因为这些关节中心恰好位于操作员手指所在的位置。我们用 RCM 连杆机构来复刻它们：该机构在机器人手的关节中心处形成一个虚拟关节，同时不在操作员的工作空间内放置硬件（Fig. 44a）。RCM 是一个平行四连杆机构。为避免对它造成过约束，顶部关节的四个孔中只使用其中两个。保留另外两个孔不用，可以减少制造公差造成的卡滞，并使运动更顺滑。

<a id="S1472"></a>
**Source:** p.81 S1472

**Original:** Thumb. The thumb linkages use a “kicked-out” geometry that preserves the robot hand’s thumb kinematics while clearing space for the operator’s own thumb, so its range of motion is unobstructed during dexterous manipulation (Fig. 44b).

**中文:** 拇指。拇指连杆采用“外撇式”几何结构，在保留机器人手拇指运动学的同时，为操作员自己的拇指留出空间，使其在灵巧操作过程中的运动范围不受阻碍（Fig. 44b）。

<a id="S1473"></a>
**Source:** p.81 S1473

**Original:** Rigid, compact joints. Every joint is supported on both sides to prevent deflection and improve measurement precision. Custom pins keep joint bulk low while forming secure connections, and a variant with a direct keying interface mates to the joint encoders, reducing backlash and improving sensor accuracy (Fig. 45a).

**中文:** 刚性紧凑的关节。每个关节两侧均有支撑，以防止形变并提高测量精度。定制销钉在形成可靠连接的同时保持关节体积较小；另一种带有直接键连接接口的版本与关节编码器配合，可以减小回差并提高传感器精度（Fig. 45a）。

![F044](assets/F044.png)

<a id="C061"></a>
**Source:** p.82 C061 · 图 F044

**Original (caption):** Figure 44: GEAR DexUMI kinematic design. (a) A remote-center-of-motion linkage places a virtual joint at the robot hand’s AB/AD and flexion joint centers. (b) The kicked-out thumb linkage keeps the robot hand’s thumb kinematics while clearing the operator’s thumb.

**中文（图注）：** 图 44：GEAR DexUMI 运动学设计。(a) 远程运动中心连杆机构在机器人手的 AB/AD 关节与屈曲关节中心处设置虚拟关节。(b) 外撇式拇指连杆在保留机器人手拇指运动学的同时，为操作员的拇指留出空间。

<a id="S1476"></a>
**Source:** p.82 S1476

**Original:** Contact surfaces and camera. The fingertip and palm tactile-sensor contact surfaces match the robot hand’s, and the fingertip geometry is reproduced on the exoskeleton to reduce the visual gap between human collection and robot execution (Fig. 45b). Non-essential contact surfaces are removed to improve wearability. The camera mounting angle and alignment are carried over to the robot hand’s mount, so the collected images match the deployed field of view (Fig. 45c). Finally, the chassis is anodized green so that a color threshold can segment it for the masked-video augmentation (Sec. E.6).

**中文:** 接触表面与相机。指尖与手掌的触觉传感器接触表面与机器人手保持一致，外骨骼上还原了指尖几何形状，以减小人工采集与机器人执行之间的视觉差距（Fig. 45b）。为提高穿戴性，去除了非必要的接触表面。相机的安装角度与对准方式沿用到机器人手的安装座上，因此采集的图像与部署时的视场一致（Fig. 45c）。最后，外壳采用阳极氧化的绿色，使颜色阈值能够将其分割出来，用于掩码视频增广（Sec. E.6）。

<a id="S1477"></a>
**Source:** p.82 S1477

**Original:** Sensing. The exoskeleton fingertips report force in the robot hand’s own tactile format: five fingertip sensors with two pads and three force axes each, 30 channels per hand. Per hand, an iPhone tracks a wrist frame 12.6 cm from its lens, which a per-arm hand-eye calibration maps onto the robot, and the same 640 × 400, 45 fps wrist and head cameras serve collection and deployment.

**中文:** 传感。外骨骼指尖以机器人手自身的触觉格式回传力信息：每个指尖配有五个传感器，每个传感器包含两个触点和三个力分量，每只手共 30 个通道。每只手通过一部 iPhone 跟踪腕部坐标系，该坐标系位于其镜头前方 12.6 cm 处，并由每条手臂的手眼标定映射到机器人上。同一套 640 × 400、45 fps 的腕部相机与头部相机同时用于采集与部署。

### E.5. DexUMI Post-Training Recipe ｜ DexUMI 后训练方案

<a id="S1478"></a>
**Source:** p.82 S1478

**Original:** For the DexUMI results of Sec. B.3, we post-train the 2B GR00T 2 model from the GR00T 2 pretraining checkpoint for 60,000 steps at a learning rate of 3 × 10−5, with 224 × 320 images from the wrist cameras and, optionally, the head camera. The policy predicts 40-step action chunks at stride 2 on the 45 fps data: relative end-effector poses for each arm and, for each hand, either absolute joint positions with joint torques or offset joint positions in their place (Eqs. (1) and (3)).

**中文:** 对于 Sec. B.3 中的 DexUMI 结果，我们从 GR00T 2 预训练检查点出发，对 2B 的 GR00T 2 模型进行后训练，训练 60,000 步，学习率为 3 × 10−5，输入为腕部相机的 224 × 320 图像，并可选地加入头部相机图像。策略在 45 fps 数据上以步长 2 预测 40 步动作块：各手臂的相对末端执行器位姿，以及各只手的一组量，二者择一，即绝对关节位置加关节力矩，或以偏移关节位置代替之（Eqs. (1) and (3)）。

### E.6. DexUMI WAM-Native Inpainting ｜ DexUMI 的 WAM 原生补全（inpainting）

<a id="S1479"></a>
**Source:** p.82 S1479

**Original:** GR00T 2 addresses the visual gap between the exoskeleton and the robot hand inside training rather than by editing video: it corrupts the exoskeleton region so that the model cannot rely on exoskeleton-specific appearance. By WAM-native inpainting we mean this in-model treatment, in place of offline video editing. Our earlier pipeline, following the original DexUMI (Xu et al., 2025), filmed each demonstration replayed on a real robot hand, segmented the exoskeleton from manually picked keypoints, inpainted it with ProPainter, and composited the robot hand back in, at the cost of robot time, manual input, and GPU-heavy segmentation and inpainting.

**中文:** GR00T 2 在训练过程中处理外骨骼与机器人手之间的视觉差距，而不是通过编辑视频来解决。它会对外骨骼区域施加扰动，使模型无法依赖外骨骼特有的外观。这里的“WAM 原生补全”指的正是这种模型内部的处理方式，用以替代离线视频编辑。我们早期的流程沿用原始 DexUMI（Xu et al., 2025）：每段演示在真实机器人手上回放并拍摄，然后根据人工选取的关键点分割出外骨骼，用 ProPainter 进行补全，再把机器人手合成回画面中。这一流程需要付出机器人时间、人工输入，以及计算开销较大的分割与补全工作。

<a id="S1480"></a>
**Source:** p.82 S1480

**Original:** Exoskeleton masks. We segment the green regions in every camera video with HSV color bands, morphological cleanup, and a ±2-frame temporal majority vote, and store each mask as a lossless binary video beside its RGB stream.

**中文:** 外骨骼掩码。我们对每个相机视频中的绿色区域进行分割：先用 HSV 颜色阈值，再做形态学清理，并结合 ±2 帧的时间多数投票。每个掩码以无损二值视频的形式，与其 RGB 视频流一同存储。

![F045](assets/F045.png)

<a id="C062"></a>
**Source:** p.83 C062 · 图 F045

**Original (caption):** Figure 45: GEAR DexUMI joints, contact surfaces, and camera. (a) Double-sided joint support and a custom pin with a direct keying interface to the joint encoder. (b) Fingertip and palm contact surfaces replicate the robot hand’s tactile sensors. (c) The camera mount matches the robot hand’s mounting angle and alignment.

**中文（图注）：** 图 45：GEAR DexUMI 的关节、接触表面与相机。(a) 双面关节支撑，以及带有直接键连接接口、与关节编码器相连的定制销钉。(b) 指尖与手掌的接触表面复现了机器人手的触觉传感器。(c) 相机支架的安装角度与对准方式与机器人手一致。

<a id="S1484"></a>
**Source:** p.83 S1484

**Original:** Masked-video augmentation. During training only, GR00T 2 corrupts the masked region before cropping and resizing, with one draw of corruption parameters per sample shared across frames and views, blended in through a feathered mask:

**中文:** 掩码视频增广。仅在训练时，GR00T 2 会在裁剪和缩放之前对掩码区域施加扰动。每个样本只抽取一次扰动参数，并在所有帧与所有视角之间共享，再通过羽化掩码混合回原图：

<a id="E004"></a>
**Source:** p.83 E004

**Original:** , 𝛼= 𝐺𝜎* 𝑚, (9)

**中文:** 该式定义混合权重 α：先对二值掩码 𝑚 施加高斯模糊 𝐺𝜎，得到随掩码边界平滑衰减的权重。式中 (9) 为公式编号。$$, 𝛼= 𝐺𝜎* 𝑚, (9)$$ [公式原文见 p.83]

<a id="S1489"></a>
**Source:** p.83 S1489

**Original:** where 𝑚is the binary mask and 𝐺𝜎a Gaussian blur with 𝜎= 6 px at 640 px width, so the corruption fades out over a narrow band around the mask and pixels farther from it stay bit-identical. The default corruption 𝑐rotates hue over the full color wheel, scales saturation by 𝑈[0.1, 1.2] and value by 𝑈[0.2, 1.15], and adds luminance noise. The saturation and value ranges deliberately reach dark, desaturated colors because the deployed robot hand is largely black. Masks are dropped from the deployed model’s inputs, so a checkpoint needs only RGB and inference frames pass through unchanged.

**中文:** 其中 𝑚 为二值掩码，𝐺𝜎 为高斯模糊，𝜎 = 6 px（以 640 px 宽度计），因此扰动会在掩码周围的一条窄带内逐渐衰减，远离掩码的像素保持逐位一致。默认扰动 𝑐 在整个色轮上旋转色相，按 𝑈[0.1, 1.2] 缩放饱和度，按 𝑈[0.2, 1.15] 缩放明度，并加入亮度噪声。饱和度与明度的取值范围特意覆盖暗色与低饱和度颜色，因为部署的机器人手大部分是黑色的。掩码不进入已部署模型的输入，因此检查点只需要 RGB 输入，推理帧则原样通过。[公式原文见 p.83]

### F. RL Post-Training ｜ 强化学习后训练

<a id="S1490"></a>
**Source:** p.84 S1490

**Original:** Pretraining equips GR00T 2 with broad visual and motor priors, but reliable real-world manipulation often requires adaptation to precise alignment, contact dynamics, and physical interaction. Reinforcement learning (RL) provides a complementary approach to supervised fine-tuning (SFT), enabling policies to improve through robot experience and task-level feedback.

**中文:** 预训练为 GR00T 2 提供了广泛的视觉与运动先验，但可靠的真实世界操作往往还需要适应精确对齐、接触动力学和物理交互。强化学习（RL）是监督微调（SFT）的一种补充方法，使策略能够借助机器人经验和任务层面的反馈不断改进。

<a id="S1492"></a>
**Source:** p.84 S1492

**Original:** Applying RL to GR00T 2 introduces unique challenges. Unlike action-only policies, GR00T 2 jointly generates actions and predicted visual futures through iterative denoising. Policy optimization must therefore accommodate joint video-action computation while enabling effective exploration. Furthermore, physical interaction is expensive, requiring efficient algorithms and infrastructure to make iterative post-training practical.

**中文:** 将 RL 应用于 GR00T 2 带来了独特的挑战。与仅输出动作的策略不同，GR00T 2 通过迭代去噪同时生成动作与预测的视觉未来。因此，策略优化必须既能适应视频-动作的联合计算，又能支持有效的探索。此外，物理交互代价高昂，需要高效的算法与基础设施，才能使迭代式后训练切实可行。

<a id="S1493"></a>
**Source:** p.84 S1493

**Original:** We address these challenges through three complementary components. First, we develop direct GR00T 2 posttraining methods, including GRPO-based optimization (Shao et al., 2024) and self-imitation from successful RL exploration, alongside residual RL for localized corrections (Sec. F.1). Second, we leverage AutoRL, an autonomous research system that discovers and improves RL post-training algorithms through closed-loop experimentation in simulation (Sec. F.2). Third, we develop scalable infrastructure that coordinates robot interaction, training, and evaluation while preserving experience and minimizing iteration overhead (Sec. F.3). We demonstrate these capabilities on four real-world precision manipulation tasks (Sec. F.4). We also investigate RL post-training through interaction with a learned neural simulator. We adapt DreamDojo (Gao et al., 2026) to recorded policy rollouts, then demonstrate that GR00T 2 can improve through world-model-based RL (Sec. F.5).

**中文:** 我们通过三个互补的部分应对这些挑战。第一，我们开发直接的 GR00T 2 后训练方法，包括基于 GRPO 的优化（Shao et al., 2024）、来自成功 RL 探索的自模仿（self-imitation），以及用于局部修正的残差强化学习（residual RL）（Sec. F.1）。第二，我们利用 AutoRL，这是一个自主研究系统，通过仿真中的闭环实验发现并改进 RL 后训练算法（Sec. F.2）。第三，我们开发了可扩展的基础设施，用于协调机器人交互、训练与评测，同时保存经验并尽量减少迭代开销（Sec. F.3）。我们在四项真实世界的精确操作任务上展示了这些能力（Sec. F.4）。我们还通过与一个学习得到的神经仿真器交互，研究 RL 后训练。我们将 DreamDojo（Gao et al., 2026）适配到录制的策略 rollout（轨迹采样）上，然后证明 GR00T 2 可以通过基于世界模型的强化学习（world-model-based RL）得到改进（Sec. F.5）。
