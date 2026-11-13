### B.5. Human →Simulation →Tianji + Sharpa ｜ B.5. 人类 →仿真 →Tianji + Sharpa

<a id="S996"></a>
**Source:** p.53 S996

**Original:** Despite their broad capabilities, WAMs still struggle with contact-rich dexterous manipulation, such as in-hand object reorientation. Reinforcement learning (RL) in simulation offers a complementary source of skills, including forceful tool use, precise contact interactions, and recovery behaviors that are difficult to demonstrate

**中文:** 尽管 WAM 能力广泛，它们在富接触的灵巧操作上仍然吃力，例如手内物体重定向。强化学习（RL）在仿真中可以提供另一类互补的技能，包括用力的工具使用、精确的接触交互，以及一些难以演示的恢复行为。

![T006](assets/T006.png)

<a id="C036"></a>
**Source:** p.54 C036 · 表 T006

**Original (caption):** Table 6: DexUMI →Tianji + Sharpa results. Fraction of real-robot trials that complete the whole task, over 20 trials per task. No training data contain a robot trajectory of either task.

**中文（表注）：** 表 6：DexUMI →Tianji + Sharpa 的结果。表中为每个任务在 20 次试次中，真机完整完成任务的比例。训练数据中没有任何一项任务的机器人轨迹。

<a id="S999"></a>
**Source:** p.54 S999

**Original:** reliably through teleoperation or kinematic retargeting. We introduce a human-to-sim-to-real pipeline that enables GR00T 2 to acquire these skills from a single human demonstration video per task.

**中文:** 这些行为很难通过遥操作或运动学重定向可靠地演示出来。我们提出一条人类到仿真再到现实（human-to-sim-to-real）的流程，使 GR00T 2 只需每个任务一段人类演示视频，就能习得这些技能。

<a id="S1000"></a>
**Source:** p.54 S1000

**Original:** Building on NVIDIA’s Video to Data (V2D) (NVIDIA, 2026b) pipeline, we reconstruct 3D object assets, hand– object motion, and contacts from stereo video, then train a state-based RL expert using CHORD (Zhu et al., 2026). We collect expert demonstrations with native simulation rendering, physical and visual randomization, and state perturbations that broaden state coverage and elicit recovery behaviors beyond nominal trajectories. Fig. 16 illustrates the full pipeline.

**中文:** 基于 NVIDIA 的 Video to Data（V2D）（NVIDIA, 2026b）流程，我们从立体视频中重建三维物体资产、手-物体运动和接触，然后使用 CHORD（Zhu et al., 2026）训练一个基于状态的 RL 专家。我们借助原生仿真渲染、物理与视觉随机化，以及状态扰动来采集专家演示。这些状态扰动扩大了状态覆盖范围，并引发超出标称轨迹的恢复行为。Fig. 16 展示了完整流程。

<a id="S1001"></a>
**Source:** p.54 S1001

**Original:** We fine-tune GR00T 2’s diffusion transformer (DiT) on 1.5K simulation episodes, incorporating training-time Real-Time Chunking (RTC) for continuous execution. The resulting policy is deployed zero-shot using RGB observations, robot state, and task instructions, without additional real-world robot data or scene-specific reconstruction or alignment. By expanding one human demonstration into diverse robot rollouts, this approach provides a scalable source of dexterous manipulation data. We hypothesize that GR00T 2’s pretrained priors support compositional generalization: fine-tuning combines simulation-learned contact-rich skills with the perceptual and behavioral knowledge acquired during large-scale pretraining.

**中文:** 我们在 1.5K 个仿真回合（episode）上微调 GR00T 2 的扩散 Transformer（DiT），并引入训练时实时分块（RTC）以实现连续执行。得到的策略以 RGB 观测、机器人状态和任务指令进行零样本部署，无需额外的真实机器人数据，也无需针对具体场景的重建或对齐。通过把一段人类演示扩展为多样的机器人 rollout（轨迹采样），该方法提供了一个可扩展的灵巧操作数据来源。我们假设 GR00T 2 的预训练先验支持组合泛化：微调把仿真中习得的富接触技能，与大规模预训练期间获得的感知和行为知识结合起来。

<a id="S1002"></a>
**Source:** p.54 S1002

**Original:** We evaluate nail hammering, flask handover, and table sweeping, comparing GR00T 2 against GR00T 1.7 and 𝜋0.5. GR00T 2 demonstrates successful transfer of dexterous manipulation skills from simulation to the real world. Although 𝜋0.5 performs well in simulation, its real-world execution is limited to grasping and lifting, with no successful completion of the full tasks, which require subsequent reorientation and object interactions.

**中文:** 我们评测了钉钉子、递交烧瓶和桌面清扫三项任务，并将 GR00T 2 与 GR00T 1.7 和 π0.5 进行比较。GR00T 2 展示了灵巧操作技能从仿真到真实世界的成功迁移。尽管 π0.5 在仿真中表现良好，但其真机执行仅限于抓取和提起，没有一项能完整完成任务，而完整任务还需要后续的重定向和物体交互。

<a id="S1003"></a>
**Source:** p.54 S1003

**Original:** Human and Object Reconstruction. Stable simulation and policy training require accurate, geometrically consistent reconstructions of hand motion, object trajectories, and their contacts. Independent estimates of hands and objects can be inconsistent, particularly when the supplied object mesh differs from the object observed in the video. We use V2D’s agentic pipeline for 4D hand-object reconstruction, coordinating tools such as SAM3 (Carion et al., 2025), FoundationPose (Wen et al., 2024), and GATOR (Wu et al., 2026) for segmentation, object tracking, and hand tracking. To resolve geometric inconsistencies, the reconstructed hands are refined against the supplied object mesh while keeping the mesh and reference object motion fixed. Contact-wrench objectives and geometric checks guide alignment, followed by penetration correction and finger repair. This formulation adapts hand configurations and contact locations to the supplied geometry while targeting the interaction’s mechanical effect on the object. These anchors provide persistent references for downstream robotic grounding. Evaluated on 15 stereo trajectories from SHOW3D (Rim et al., 2026), a dataset of hand-object interactions captured in the wild with annotated 3D hand and object poses, the reconstruction pipeline achieves an average hand reconstruction error of 17.5 mm and an object Chamfer distance of 3.0 mm.

**中文:** 人与物体重建。稳定的仿真与策略训练需要对手部运动、物体轨迹及其接触进行准确且几何一致的重建。手和物体的独立估计可能彼此不一致，尤其是在所给的物体网格与视频中观察到的物体不同时。我们使用 V2D 的智能体化（agentic）流程进行四维（4D）手-物体重建，协调 SAM3（Carion et al., 2025）、FoundationPose（Wen et al., 2024）和 GATOR（Wu et al., 2026）等工具，分别完成分割、物体跟踪和手部跟踪。为解决几何不一致问题，重建得到的手部在保持网格和参考物体运动固定的前提下，相对于所给物体网格进行细化。接触力旋量目标和几何检查引导对齐，随后进行穿透修正和手指修复。该公式使手部构型和接触位置适应所给几何，同时以交互对物体产生的力学效果为目标。这些锚点为下游机器人落地提供持续的参照。在 SHOW3D（Rim et al., 2026）的 15 条立体轨迹上评估（该数据集为真实场景中采集的手-物体交互，带有标注的三维手部与物体位姿），重建流程的平均手部重建误差为 17.5 mm，物体 Chamfer 距离为 3.0 mm。

<a id="S1004"></a>
**Source:** p.54 S1004

**Original:** RL in Simulation. Using the reconstructed object assets and trajectories, we train a state-based RL expert to perform dexterous manipulation in simulation. The policy observes privileged robot and object states and outputs arm and hand joint targets. Training follows CHORD, with a warm-up procedure following SimToolReal (Kedia et al., 2026).

**中文:** 仿真中的强化学习（RL）。利用重建得到的物体资产和轨迹，我们在仿真中训练一个基于状态的 RL 专家来完成灵巧操作。该策略观测特权的机器人与物体状态，输出手臂和手部的关节目标。训练遵循 CHORD，并采用 SimToolReal（Kedia et al., 2026）的预热（warm-up）流程。

<a id="S1005"></a>
**Source:** p.54 S1005

**Original:** We calibrate the simulated robot’s joint dynamics through system identification of stiffness, damping, armature, friction, and delay. To improve robustness to physical variation, we randomize robot dynamics, object properties, and scene geometry during training. We also vary initial robot and object configurations, fixture geometry, and table dimensions, while ensuring valid, collision-free initialization.

**中文:** 我们通过对刚度、阻尼、转子惯量（armature）、摩擦和延迟进行系统辨识，来标定仿真机器人的关节动力学。为提高对物理变化的鲁棒性，训练期间我们随机化机器人动力学、物体属性和场景几何。我们还改变机器人与物体的初始构型、夹具几何和桌面尺寸，同时保证初始化有效且无碰撞。

![F031](assets/F031.png)

<a id="C037"></a>
**Source:** p.55 C037 · 图 F031

**Original (caption):** Figure 31: GR00T 2 learns dexterous manipulation through human-to-sim-to-real transfer. Starting from a single human demonstration per task captured with an egocentric stereo camera, the Video-to-Data pipeline generates simulation data for SFT of GR00T 2. The resulting policies transfer zero-shot to the real world on Hammer Nail, Handover Flask, and Brushing Trash, demonstrating dexterous in-hand object reorientation, handover, tool use, and bimanual coordination.

**中文（图注）：** GR00T 2 通过人类到仿真再到现实的迁移学习灵巧操作。每个任务从一段用第一人称视角立体相机（egocentric stereo camera）采集的人类演示出发，Video-to-Data 流程为 GR00T 2 的 SFT 生成仿真数据。所得策略以零样本方式迁移到真实世界，完成敲钉（Hammer Nail）、递交烧瓶（Handover Flask）和扫纸屑（Brushing Trash）三项任务，展示了灵巧的手内物体重定向、递交、工具使用以及双臂协调。

<a id="S1006"></a>
**Source:** p.55 S1006

**Original:** The reward follows CHORD (Zhu et al., 2026) and combines task execution, motion regularization, and contact quality to encourage reliable, human-like tool interactions. Task rewards include keypoint-based tracking of the demonstrated object trajectory, subgoal completion, task progress, and terminal success. Joint-speed penalties regularize motion. Contact rewards use contact wrenches to encourage human-like grasps, improve grasp quality, and sustain object holding. We optimize the policy using a PPO-based SAPG (Singla et al., 2024).

**中文:** 奖励遵循 CHORD（Zhu et al., 2026），综合任务执行、运动正则化和接触质量，以鼓励可靠、类人的工具交互。任务奖励包括基于关键点跟踪演示物体轨迹的奖励、子目标完成、任务进度以及终止时的成功。关节速度惩罚用于正则化运动。接触奖励使用接触力旋量，以鼓励类人的抓取、提高抓取质量并维持对物体的持握。我们使用基于 PPO 的 SAPG（Singla et al., 2024）优化策略。

<a id="S1007"></a>
**Source:** p.55 S1007

**Original:** Harvest Dexterity from Simulation. We convert the RL expert’s skills into demonstrations for supervised fine-tuning (SFT). Each rollout records RGB observations, robot states, expert actions, and task instructions. The privileged tool and goal keypoints available to the RL expert are excluded from GR00T 2’s inputs. We continue to randomize physical properties and scene configurations during collection to capture expert behavior across diverse conditions.

**中文:** 从仿真中获取灵巧性。我们把 RL 专家的技能转化为用于监督微调（SFT）的演示。每条 rollout（轨迹采样）记录 RGB 观测、机器人状态、专家动作和任务指令。RL 专家可用的特权工具关键点与目标关键点不纳入 GR00T 2 的输入。采集过程中，我们持续随机化物理属性和场景配置，以捕获专家在多样条件下的行为。

<a id="S1008"></a>
**Source:** p.55 S1008

**Original:** To broaden state coverage and capture recovery behavior, we introduce random-action bursts, object teleports, and robot-joint teleports during data collection. These perturbations move the system away from nominal trajectories and elicit corrective behavior from the expert. The resulting demonstrations cover states that GR00T 2 may encounter when its own actions deviate, helping mitigate the narrow state coverage and compounding errors observed with naive expert-rollout collection.

**中文:** 为扩大状态覆盖并捕获恢复行为，我们在数据采集时引入随机动作脉冲、物体瞬移和机器人关节瞬移。这些扰动使系统偏离标称轨迹，并引发专家的纠正行为。由此得到的演示覆盖了 GR00T 2 自身动作发生偏差时可能遇到的状态，有助于缓解朴素专家 rollout 采集中观察到的状态覆盖面窄和误差累积问题。

<a id="S1009"></a>
**Source:** p.55 S1009

**Original:** We also randomize visual appearance using native Isaac Lab (Mittal et al., 2025) rendering, without visual inpainting or style transfer models. Randomization covers object and scene colors, textures, material properties, illumination, environment lighting, and camera calibration. Small perturbations to camera poses and intrinsics model calibration uncertainty, while image noise models sensor variation.

**中文:** 我们还使用原生 Isaac Lab（Mittal et al., 2025）渲染对视觉外观进行随机化，未使用视觉补全（inpainting）或风格迁移模型。随机化涵盖物体与场景的颜色、纹理、材质属性、光照、环境照明和相机标定。相机位姿与内参的微小扰动用于模拟标定不确定性，图像噪声则用于模拟传感器差异。

<a id="S1010"></a>
**Source:** p.55 S1010

**Original:** SFT with Simulation Data. We fine-tune GR00T 2 for each task using 1.5k simulation episodes, sourced from one human demonstration video. During SFT, we update the DiT, retain the pretrained action normalization statistics, and freeze the action decoder and video output projection. The fine-tuned policy is deployed zero-shot in the real world using RGB observations, robot state, and a task instruction, with no additional real-world robot data. To support continuous real-time execution of action chunks, we incorporate training-time Real-Time Chunking (RTC).

**中文:** 基于仿真数据的 SFT。我们为每个任务使用 1.5k 个仿真回合微调 GR00T 2，这些回合源自一段人类演示视频。SFT 期间，我们更新 DiT，保留预训练的动作归一化统计量，并冻结动作解码器和视频输出投影。微调后的策略以 RGB 观测、机器人状态和任务指令进行零样本的真实世界部署，不使用额外的真实机器人数据。为支持动作块的连续实时执行，我们引入了训练时实时分块（RTC）。

![T007](assets/T007.png)

<a id="C038"></a>
**Source:** p.56 C038 · 表 T007

**Original (caption):** Table 7: GR00T 2 learns dexterous manipulation skills from simulation demonstrations generated from human videos and transfers these skills zero-shot to the real world. Fine-tuned models are evaluated in simulation (s) and the real world (r).

**中文（表注）：** 表 7：GR00T 2 从人类视频生成的仿真演示中学习灵巧操作技能，并将这些技能零样本迁移到真实世界。微调后的模型分别在仿真（s）和真实世界（r）中评估。

<a id="S1014"></a>
**Source:** p.56 S1014

**Original:** Learning Tasks with Human-to-Sim-to-Real. We evaluate GR00T 2 on three tasks requiring dexterous manipulation, with success defined as follows:

**中文:** 借助人类到仿真再到现实完成任务学习。我们在三项需要灵巧操作的任务上评估 GR00T 2，成功的定义如下：

<a id="S1015"></a>
**Source:** p.56 S1015

**Original:** • Hammer Nail: The nail is driven into the fixture until its head contacts the fixture’s top surface. • Handover Flask: The flask is lifted off the table, handed over, and tilted to a pouring angle without being dropped. • Brushing Trash: Paper waste is swept into the red dustpan using the brush.

**中文:** • 敲钉（Hammer Nail）：钉子被敲入夹具，直至钉头接触夹具的顶面。• 递交烧瓶（Handover Flask）：烧瓶被从桌面提起、递交，并倾斜至倾倒角度，且不能掉落。• 扫纸屑（Brushing Trash）：使用刷子将纸质废弃物扫入红色簸箕。

<a id="S1016"></a>
**Source:** p.56 S1016

**Original:** GR00T 2 is deployed with 2 action 1 video denoising steps during inference with RTC enabled at 20 Hz. 𝜋0.5 is deployed with the settings recommended in the official implementation: each inference integrates the flow-matching action expert for 10 steps, and the robot executes the first 8 actions of each predicted 30-step chunk (0.4 s at 20 Hz) before synchronously querying the policy again, with 𝜋0.5 observing only the most recent frame of each camera view.

**中文:** 推理时，GR00T 2 以 2 个动作去噪步和 1 个视频去噪步进行部署，并以 20 Hz 启用 RTC。π0.5 按照官方实现推荐的设置进行部署：每次推理对流匹配动作专家积分 10 步，机器人执行每个预测的 30 步动作块中的前 8 个动作（在 20 Hz 下为 0.4 s），然后同步地再次查询策略；π0.5 仅观测每个相机视角的最新一帧。

<a id="S1017"></a>
**Source:** p.56 S1017

**Original:** We compare against GR00T 1.7 and 𝜋0.5 in both simulation and the real world. Figure 31 shows execution rollouts for each task. Tab. 7 reports the number of successful episodes for each method. With simulation-only post-training, GR00T 2 achieves 20/20, 13/20, and 19/20 full-task successes in simulation on nail hammering, flask handover, and trash sweeping, respectively (Table 7). In real-world evaluation, it completes nail hammering in 9/10 trials and trash sweeping in 8/10 trials, demonstrating zero-shot transfer on both tasks. Both GR00T 1.7 and 𝜋0.5 achieve 0/10 full-task successes on every real-world task despite making intermediate progress. On nail hammering, GR00T 1.7 lifts the hammer in 10/10 trials and completes in-hand reorientation in 6/10 trials, but never drives the nail to the required depth. On trash sweeping, it lifts the brush in 7/10 trials but never completes the sweep. Similarly, 𝜋0.5 lifts the hammer, flask, and brush in 6/10, 4/10, and 9/10 trials, respectively, but completes none of the full tasks. These results distinguish successful grasp acquisition from full task execution, which requires subsequent reorientation and contact interactions. For the Handover Flask task, the high-frequency specialist policy succeeds in the real world. However, the handover requires precise spatiotemporal coordination and contact control, making it particularly sensitive to observation and inference delays.

**中文:** 我们在仿真和真实世界中都将 GR00T 2 与 GR00T 1.7 及 π0.5 进行比较。图 31 展示了每项任务的执行 rollout（轨迹采样）。Tab. 7 报告了每种方法成功的回合数。仅经过仿真后训练时，GR00T 2 在仿真中完成完整任务的成功次数分别为：敲钉 20/20、递交烧瓶 13/20、扫纸屑 19/20（Table 7）。在真实世界评估中，它完成敲钉的试次为 9/10，完成扫纸屑的试次为 8/10，证明了两项任务上的零样本迁移。尽管取得了中间进展，GR00T 1.7 和 π0.5 在每项真实世界任务上的完整任务成功率都是 0/10。在敲钉任务上，GR00T 1.7 在 10/10 次试次中举起了锤子，并在 6/10 次中完成了手内重定向，但从未将钉子敲到所需深度。在扫纸屑任务上，它在 7/10 次中举起了刷子，但从未完成清扫。类似地，π0.5 分别在 6/10、4/10 和 9/10 次试次中举起了锤子、烧瓶和刷子，但没有完成任何一项完整任务。这些结果区分了成功抓取与完整执行任务：后者还需要后续的重定向和接触交互。对于递交烧瓶任务，高频专用策略在真实世界中取得了成功。然而，递交需要精确的时空协调和接触控制，因此对观测和推理延迟尤为敏感。
