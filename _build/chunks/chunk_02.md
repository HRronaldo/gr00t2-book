### 2. GR00T 2 Overview ｜ 2. GR00T 2 概览

<a id="S058"></a>
**Source:** p.5 S058

**Original:** GR00T 2 is a world-action model (WAM): a single model that, given the robot’s visual and proprioceptive input and a user instruction, predicts both how the scene will unfold and the robot’s actions. One pretrained checkpoint covers parallel-gripper arms, dexterous hands, and a humanoid, and learns diverse source data sources including human egocentric videos, handheld UMI gripper data, and robot teleopration data. (Sec. 4.2).

**中文:** GR00T 2 是一种世界-动作模型（WAM）：给定机器人的视觉与本体感知输入以及用户指令，由同一个模型同时预测场景将如何演化，以及机器人的动作。一个预训练检查点即可覆盖平行夹爪机械臂、灵巧手和人形机器人，并从多样的数据来源中学习，包括人类第一人称视角（egocentric）视频、手持式 UMI 夹爪数据以及机器人遥操作数据。(Sec. 4.2).

<a id="S059"></a>
**Source:** p.5 S059

**Original:** Inputs and outputs. At every control step, GR00T 2 receives (i) a 0.8s history of 224 × 320 images from up to four cameras at 5 fps, typically a head camera and one camera on each wrist, (ii) the robot’s proprioceptive state, and (iii) a natural-language instruction. It returns a chunk of future actions together with the predicted future frames of every camera. The robot executes the chunk through its own controller while the next chunk is computed (Sec. K.5).

**中文:** 输入与输出。在每个控制步，GR00T 2 接收 (i) 来自至多四台相机的 0.8 秒历史图像（224 × 320，5 fps，通常为一台头部相机加上每个腕部各一台）、(ii) 机器人的本体感知状态，以及 (iii) 一条自然语言指令。它返回一段未来动作块，以及每台相机的预测未来帧。机器人通过自身控制器执行该动作块，同时下一个动作块正在计算（Sec. K.5）。

<a id="S060"></a>
**Source:** p.5 S060

**Original:** Architecture. GR00T 2 is built on Cosmos-Predict2.5-2B, a video diffusion transformer pretrained for world simulation (NVIDIA et al., 2025a). Video, state, and action inputs become tokens in one sequence that a single 2B-parameter transformer processes (Fig. 1):

**中文:** 架构。GR00T 2 构建于 Cosmos-Predict2.5-2B 之上，后者是一个为世界仿真而预训练的视频扩散 Transformer（NVIDIA et al., 2025a）。视频、状态和动作输入被转换为同一序列中的 token，由单个 2B 参数的 Transformer 统一处理（Fig. 1）：

<a id="S061"></a>
**Source:** p.5 S061

**Original:** • Video. A frozen Wan 2.1 video VAE (Wan Team et al., 2025) compresses each camera stream 4× in time and 8× in each spatial dimension. The latents are split into patches, giving 280 tokens per latent frame and camera at 224 × 320. A learned view embedding tells the model which camera each token comes from. Past frames enter as context, and future frames are generated. • Language. A frozen Cosmos-Reason1 vision-language model (NVIDIA et al., 2025b) encodes the instruction, and the transformer reads it through cross-attention. • State and actions. Small embodiment-specific MLPs map the robot state and the noisy action chunk into the transformer’s width, and an embodiment-specific decoder maps the output tokens back to actions.

**中文:** • 视频。一个冻结的 Wan 2.1 视频 VAE（Wan Team et al., 2025）将每路相机流在时间维度上压缩 4×、在每个空间维度上压缩 8×。潜变量被切分为图块（patch），在 224 × 320 分辨率下，每个潜变量帧、每路相机对应 280 个 token。一个可学习的视角嵌入（view embedding）告诉模型每个 token 来自哪台相机。过去的帧作为上下文输入，未来的帧则由模型生成。• 语言。一个冻结的 Cosmos-Reason1 视觉语言模型（NVIDIA et al., 2025b）对指令进行编码，Transformer 通过交叉注意力读取该编码。• 状态与动作。小型的本体专用 MLP 将机器人状态和带噪动作块映射到 Transformer 的宽度，本体专用解码器再将输出 token 映射回动作。

<a id="S062"></a>
**Source:** p.5 S062

**Original:** Inside the transformer, video tokens attend to one another across time and cameras, and action tokens attend to all video tokens, including the future frames being generated. Actions can therefore follow the future the model imagines. GR00T 2 is trained with flow matching (Lipman et al., 2023) on future video latents and actions together, with one loss for each. At inference, a few denoising steps suffice: one or two for video and two to four for actions in our deployments (Sec. I.1).

**中文:** 在 Transformer 内部，视频 token 在时间和相机之间相互注意，动作 token 则关注所有视频 token，包括正在生成的未来帧。因此，动作可以依循模型所想象的未来来展开。GR00T 2 使用流匹配（Lipman et al., 2023）在未来视频潜变量与动作上联合训练，二者各对应一项损失。推理时，几个去噪步即可满足需要：在我们的部署中，视频用一到两步，动作用两到四步（Sec. I.1）。

<a id="S063"></a>
**Source:** p.5 S063

**Original:** GR00T 2 Turbo: Efficient World-Action Modeling. While GR00T 2 already runs in real time when served from a workstation GPU (a median of 153 ms to predict an action chunk for Dexter from three camera views on a GeForce RTX 5090, Tab. 27), humanoid whole-body loco-manipulation sets a much stricter budget. The policy must react quickly to keep the whole body coordinated as the robot moves, and it must run onboard on

**中文:** GR00T 2 Turbo：高效的世界-动作建模。虽然 GR00T 2 在工作站 GPU 上部署时已能实时运行（在 GeForce RTX 5090 上，利用三路相机视图为 Dexter 预测一个动作块的中位时延为 153 ms，见 Tab. 27），但人形机器人全身移动操作对时延预算的要求要严格得多。策略必须快速响应，才能在机器人运动时保持全身协调，并且它必须在机载端运行，

![F002](assets/F002.png)

<a id="C002"></a>
**Source:** p.6 C002 · 图 F002

**Original (caption):** Figure 2: Cross-embodiment transfer to Dexter with 0, 1, and 5 Dexter episodes. Results on the Dexter-50 tasks, which have no Dexter training data but appear in YAM teleoperation data, human video, or both. Zero-shot runs the pretrained model directly, while 1-shot and 5-shot fine-tune it with LoRA on 1 or 5 Dexter episodes. Left: average success rate over the 50 tasks. Right: number of tasks in each success-rate range. The tasks are those the model learns with five episodes (at least 80% success). Per-task results are in Fig. 24.

**中文（图注）：** 图 2：使用 0、1 和 5 个 Dexter episode 的跨本体迁移至 Dexter 的结果。结果基于 Dexter-50 任务集，这些任务在 Dexter 训练数据中没有出现，但出现在 YAM 遥操作数据、人类视频或二者之中。Zero-shot 直接运行预训练模型，而 1-shot 与 5-shot 则使用 LoRA 在 1 个或 5 个 Dexter episode 上进行微调。左图：50 个任务的平均成功率。右图：各成功率区间内的任务数量。这些任务是模型用五个 episode 即可学会的任务（成功率至少为 80%）。逐任务结果见 Fig. 24。

<a id="S078"></a>
**Source:** p.6 S078

**Original:** an edge GPU such as the NVIDIA Jetson AGX Thor, which has far less compute. We therefore design GR00T 2 Turbo to make the world-modeling objective itself even cheaper. Most of the tokens GR00T 2 predicts are future video, and video is highly redundant. Turbo keeps the 2B transformer that models video and actions jointly but encodes video with a higher-compression VAE, so it still predicts future observations and actions together, with far fewer visual tokens. This makes both training and inference faster. Turbo predicts in 124 ms on the onboard Jetson Thor of the Unitree G1, where it plans whole-body motion for the SONIC controller (Sec. 3.5 and 4.6.1). Turbo trails GR00T 2 on dexterous tasks but remains well above the baselines on bimanual and dexterous manipulation, and offers a favorable tradeoff between task performance and inference latency (Sec. 3.1 and Fig. 23).

**中文:** 例如 NVIDIA Jetson AGX Thor 这样的边缘 GPU，其算力要少得多。因此，我们设计了 GR00T 2 Turbo，使世界建模目标本身的开销进一步降低。GR00T 2 预测的大部分 token 是未来视频，而视频具有高度冗余性。Turbo 保留了联合建模视频与动作的 2B Transformer，但使用压缩率更高的 VAE 编码视频，因此它仍然同时预测未来观测与动作，只是视觉 token 数量少得多。这使训练与推理都更快。Turbo 在 Unitree G1 的机载 Jetson Thor 上以 124 ms 完成预测，并在此基础上为 SONIC 控制器规划全身运动（Sec. 3.5 and 4.6.1）。Turbo 在灵巧任务上落后于 GR00T 2，但在双臂与灵巧操作上仍远高于基线，并在任务性能与推理时延之间提供了有利的权衡（Sec. 3.1 and Fig. 23）。

<a id="S080"></a>
**Source:** p.6 S080

**Original:** Specifically, Turbo replaces the video VAE with the Wan 2.2 VAE (Wan Team et al., 2025), increasing spatial compression from 8× to 16× per dimension and producing a 4× smaller spatial latent grid. The latent input and output projections are adapted to the new VAE, while the action horizon remains unchanged.

**中文:** 具体而言，Turbo 将视频 VAE 替换为 Wan 2.2 VAE（Wan Team et al., 2025），将每个维度的空间压缩率从 8× 提高到 16×，使空间潜变量网格缩小 4×。潜变量的输入与输出投影层已适配新的 VAE，而动作时域（action horizon）保持不变。

<a id="S081"></a>
**Source:** p.6 S081

**Original:** Using GR00T 2 on a new robot. To bring up a robot, a practitioner maps its cameras to the head and wrist views, expresses its actions in a supported action space (or adds a new one), and post-trains GR00T 2 on demonstrations of the target tasks. Sec. 3 shows how few demonstrations this takes, and how to replace teleoperation with human or UMI demonstrations altogether.

**中文:** 在新机器人上使用 GR00T 2。要让一台机器人运行起来，实践者需要把它的相机映射到头部与腕部视角，将其动作表示为受支持的动作空间（或新增一个动作空间），然后在目标任务的演示数据上对 GR00T 2 进行后训练。第 3 节说明只需多少演示即可完成这一过程，以及如何完全用人类演示或 UMI 演示替代遥操作。

### 3. GR00T 2 Capabilities ｜ 3. GR00T 2 能力

<a id="S082"></a>
**Source:** p.6 S082

**Original:** We now present the capabilities of GR00T 2. Sec. 3.1 shows zero-shot deployment and few-shot adaptation on new tasks and post-training on long-horizon tasks that demand precision and dexterity, and Sec. 3.2 studies cross-embodiment transfer, in which GR00T 2 learns a skill on a robot without teleoperated demonstrations of that skill. Sec. 3.3 shows that reinforcement learning improves GR00T 2 beyond its demonstrations, Sec. 3.4 pairs GR00T 2 with a frontier agent for long-horizon tasks, and Sec. 3.5 extends GR00T 2 to whole-body humanoid loco-manipulation. We report the main results here and defer the full evaluations to the appendix.

**中文:** 下面介绍 GR00T 2 的能力。第 3.1 节展示其在新任务上的零样本部署与少样本适配，以及在要求精确与灵巧的长时序任务上的后训练；第 3.2 节研究跨本体迁移，即 GR00T 2 在某台机器人上学会一项技能，而无需该技能的遥操作演示。第 3.3 节表明，强化学习能使 GR00T 2 超越其演示数据；第 3.4 节将 GR00T 2 与前沿智能体配对，用于长时序任务；第 3.5 节将 GR00T 2 扩展到全身人形机器人移动操作。这里只报告主要结果，完整评测留待附录。

### 3.1. Fast Adaptation: Zero-Shot Generalization and Few-Shot Mastery ｜ 3.1. 快速适配：零样本泛化与少样本精通

<a id="S083"></a>
**Source:** p.6 S083

**Original:** Zero-shot deployment on new tasks. Pretraining on teleoperation data from many robots and on Human-1M human video (Sec. 4.2) gives GR00T 2 an emergent ability to perform tasks it has never seen on the target robot. We test this on Dexter (Tianji robot + Sharpa hands), a bimanual robot with two 22-DoF dexterous hands, with 50 tasks that are absent from Dexter’s own data and appear only in YAM gripper data, human video, or both. Deployed out of the box and conditioned only on the language instruction, GR00T 2 succeeds in 40% of trials and completes 40 of the 50 tasks at least once (Fig. 2). Most failures come from a single step

**中文:** 在新任务上的零样本部署。在许多机器人的遥操作数据以及 Human-1M 人类视频上进行预训练（Sec. 4.2），使 GR00T 2 获得了一种涌现能力，能够在目标机器人上完成它从未见过的任务。我们在 Dexter（Tianji 机器人 + Sharpa 手）上检验这一能力。Dexter 是一台双臂机器人，配备两只 22-DoF 灵巧手。测试包含 50 个任务，这些任务不在 Dexter 自身的数据中，只出现在 YAM 夹爪数据、人类视频或二者之中。GR00T 2 开箱即用，仅以语言指令为条件，在 40% 的试次中成功，并且 50 个任务中至少完成一次的有 40 个（Fig. 2）。大多数失败来自一个步骤

![T001](assets/T001.png)

<a id="C003"></a>
**Source:** p.7 C003 · 表 T001

**Original (caption):** Table 1: Post-training benchmarks. For each model, Prog. is the average task progress score across all trials and SR is the success rate, both on a scale from 0 to 100. Bold marks the best Prog. and SR in each row, and the last row of each table averages its tasks. Each YAM result is based on up to 20 trials. On Truck Assembly, GR00T 2 and GR00T 2 Turbo were evaluated on a revised, easier set of start scenes, and on the original scenes GR00T 2 succeeds in 7 of 20 trials with a progress score of 94.0. Baselines: 𝜋0.5 (Physical Intelligence et al., 2025), GR00T 1.7 (NVIDIA, 2026a), FastWAM (Yuan et al., 2026), MolmoAct2 (Fang et al., 2026), and FLUX 3 Action (Black Forest Labs, 2026).

**中文（表注）：** 表 1：后训练基准测试。对每个模型，Prog. 为所有试次的平均任务进度得分，SR 为成功率，二者均取 0 到 100 的刻度。每行中最佳的 Prog. 与 SR 加粗标出，每个表的最后一行对其所有任务取平均。每个 YAM 结果基于至多 20 次试验。在 Truck Assembly 上，GR00T 2 与 GR00T 2 Turbo 是在修订后、更容易的一组起始场景上评测的；在原始场景上，GR00T 2 在 20 次试验中成功 7 次，进度得分为 94.0。基线：𝜋0.5（Physical Intelligence et al., 2025）、GR00T 1.7（NVIDIA, 2026a）、FastWAM（Yuan et al., 2026）、MolmoAct2（Fang et al., 2026）以及 FLUX 3 Action（Black Forest Labs, 2026）。

<a id="S088"></a>
**Source:** p.7 S088

**Original:** Hot Wheels Assembly 95.4 85.0 68.6 50.0 13.1 0.0 19.5 0.0 0.8 0.0 1.5 0.0 0.5 0.0 Toy Tractor Assembly 63.8 45.0 54.5 40.0 8.4 0.0 3.6 0.0 1.9 0.0 1.1 0.0 2.4 0.0 Toy Plane Assembly 71.0 70.0 63.5 55.0 24.0 10.0 11.0 0.0 10.0 0.0 13.5 0.0 10.0 0.0 iPhone into Box 89.0 65.0 91.0 55.0 67.5 5.0 49.5 15.0 17.0 0.0 38.0 0.0 19.5 0.0 Fixed-Pipe Fittings 70.0 70.0 90.0 90.0 30.0 30.0 35.0 35.0 45.0 45.0 35.0 35.0 0.0 0.0 Wire into Breaker 98.5 95.0 100.0 100.0 30.0 30.0 17.0 0.0 18.5 5.0 10.0 10.0 8.0 0.0

**中文:** [存疑：抽取文本为表格行的扁平化结果，列结构丢失，无法确定各数值所属的列，以下按原始顺序保留。] 任务行依次为：Hot Wheels Assembly（Hot Wheels 组装）95.4 85.0 68.6 50.0 13.1 0.0 19.5 0.0 0.8 0.0 1.5 0.0 0.5 0.0；Toy Tractor Assembly（玩具拖拉机组装）63.8 45.0 54.5 40.0 8.4 0.0 3.6 0.0 1.9 0.0 1.1 0.0 2.4 0.0；Toy Plane Assembly（玩具飞机组装）71.0 70.0 63.5 55.0 24.0 10.0 11.0 0.0 10.0 0.0 13.5 0.0 10.0 0.0；iPhone into Box（将 iPhone 放入盒中）89.0 65.0 91.0 55.0 67.5 5.0 49.5 15.0 17.0 0.0 38.0 0.0 19.5 0.0；Fixed-Pipe Fittings（固定管路接头）70.0 70.0 90.0 90.0 30.0 30.0 35.0 35.0 45.0 45.0 35.0 35.0 0.0 0.0；Wire into Breaker（将线缆接入断路器）98.5 95.0 100.0 100.0 30.0 30.0 17.0 0.0 18.5 5.0 10.0 10.0 8.0 0.0。

<a id="S094"></a>
**Source:** p.7 S094

**Original:** Make Shipping Label 78.0 60.0 73.0 60.0 41.0 5.0 16.0 0.0 Flashlight Battery Replacement 86.0 55.0 49.0 15.0 34.0 0.0 41.0 0.0 GB300 Memory 96.0 85.0 81.0 50.0 43.0 0.0 55.0 0.0 Truck Assembly 98.0 65.0 43.0 5.0 0.0 0.0 0.0 0.0 Crude Salt Filtering 98.0 85.0 88.0 65.0 17.0 0.0 14.0 0.0 Vitamin C Test 86.0 75.0 67.0 25.0 9.0 0.0 14.0 0.0 Microscope 64.0 55.0 33.0 20.0 10.0 0.0 9.0 0.0

**中文:** [存疑：抽取文本为表格行的扁平化结果，列结构丢失，无法确定各数值所属的列，以下按原始顺序保留。] 任务行依次为：Make Shipping Label（制作运输标签）78.0 60.0 73.0 60.0 41.0 5.0 16.0 0.0；Flashlight Battery Replacement（更换手电筒电池）86.0 55.0 49.0 15.0 34.0 0.0 41.0 0.0；GB300 Memory（GB300 内存模块）96.0 85.0 81.0 50.0 43.0 0.0 55.0 0.0；Truck Assembly（卡车组装）98.0 65.0 43.0 5.0 0.0 0.0 0.0 0.0；Crude Salt Filtering（粗盐过滤）98.0 85.0 88.0 65.0 17.0 0.0 14.0 0.0；Vitamin C Test（维生素 C 检测）86.0 75.0 67.0 25.0 9.0 0.0 14.0 0.0；Microscope（显微镜操作）64.0 55.0 33.0 20.0 10.0 0.0 9.0 0.0。

![F003](assets/F003.png)

<a id="C004"></a>
**Source:** p.7 C004 · 图 F003

**Original (caption):** Figure 3: Representative tasks from the two post-training benchmarks. Hot Wheels Assembly on YAM (top) and Make Shipping Label on Dexter (bottom).

**中文（图注）：** 图 3：两个后训练基准测试中的代表性任务。YAM 上的 Hot Wheels Assembly（上）与 Dexter 上的 Make Shipping Label（下）。

<a id="S096"></a>
**Source:** p.7 S096

**Original:** that falls short on precision within an otherwise correct execution. The ability grows with data, and zero-shot success on new Dexter tasks more than doubles as the amount of human video in pretraining increases (Fig. 10). On broader zero-shot suites for YAM and Dexter, GR00T 2 also leads the VLA baselines in success rate (Tabs. 2 and 3).

**中文:** 该步骤在精度上不足，而其余执行本身是正确的。这种能力随数据增长：随着预训练中人类视频数量的增加，Dexter 新任务上的零样本成功率增长超过一倍（Fig. 10）。在 YAM 与 Dexter 更广泛的零样本测试集上，GR00T 2 的成功率同样领先于 VLA 基线（Tabs. 2 and 3）。

<a id="S097"></a>
**Source:** p.7 S097

**Original:** Few-shot mastery with minutes of robot data. Because the pretrained model already knows how to approach

**中文:** 仅用几分钟机器人数据实现少样本精通。由于预训练模型已经知道如何接近

![F004](assets/F004.png)

<a id="C005"></a>
**Source:** p.8 C005 · 图 F004

**Original (caption):** Figure 4: Learning new tasks without teleoperation. Each column is one way to demonstrate a task without the target robot. It shows a demonstration, a GR00T 2 rollout on the robot, and the real-robot success rate per task. Best baseline is the highest success among the other models evaluated on that task (GR00T 1.7 (NVIDIA, 2026a), 𝜋0.5 (Physical Intelligence et al., 2025), LingBot-VA (Li et al., 2026)). *For Conveyor Sorting, the bars show the share of the 50 conveyor items sorted, not the share of successful trials. Full results are in Fig. 27 and Tabs. 4, 5 and 7.

**中文（图注）：** 图 4：不依赖遥操作学习新任务。每一列对应一种无需目标机器人即可演示任务的方式，展示了演示、GR00T 2 在机器人上的一次 rollout（轨迹采样），以及每个任务的真机成功率。Best baseline 指在该任务上其他被评测模型中的最高成功率（GR00T 1.7（NVIDIA, 2026a）、𝜋0.5（Physical Intelligence et al., 2025）、LingBot-VA（Li et al., 2026））。*对于 Conveyor Sorting，柱状图表示所分拣的 50 件传送带物品所占的比例，而非成功试次的比例。完整结果见 Fig. 27 和 Tabs. 4, 5 and 7。

<a id="S130"></a>
**Source:** p.8 S130

**Original:** these tasks, very little robot data closes the gap. One teleoperated episode per task lifts success to 71%, and five episodes, under three minutes of robot data, lift it to 95%, with 37 of the 50 tasks succeeding in every trial. The 50 tasks were chosen among those the model learns with five episodes (at least 80% success), so the five-episode rate is high partly by construction. Each adaptation is a LoRA fine-tune of about 30 minutes on a single RTX 5090, and merging the adapter into the weights means the adapted model is served exactly like the pretrained one (Sec. A.3).

**中文:** 这些任务上，极少量的机器人数据即可弥合差距。每个任务一个遥操作 episode 即可将成功率提升至 71%；五个 episode（不足三分钟的机器人数据）则将其提升至 95%，其中 50 个任务中有 37 个在每次试验中都成功。这 50 个任务是从模型用五个 episode 即可学会（成功率至少为 80%）的任务中挑选出来的，因此五个 episode 的成功率在一定程度上由挑选方式决定。每次适配都是在单张 RTX 5090 上约 30 分钟的 LoRA 微调；将适配器合并进权重后，适配后的模型与预训练模型的部署方式完全相同（Sec. A.3）。

<a id="S131"></a>
**Source:** p.8 S131

**Original:** Long-horizon tasks that demand precision and dexterity. The same pretraining pays off when GR00T 2 is post-trained on long-horizon tasks that chain many precise steps. On six YAM tasks, from assembling a toy car end to end in 24 stages to inserting a wire into a breaker, GR00T 2 reaches 71.7% average success, compared with at most 12.5% for the VLA and WAM baselines (Tab. 1a and Fig. 3). On seven dexterous-hand tasks, such as filtering crude salt, testing for vitamin C, and swapping a GB300 memory module, GR00T 2 reaches 68.6% average success, compared with at most 0.7% for GR00T 1.7 and 𝜋0.5 (Tab. 1b). Completing such tasks end to end, with dexterous hands and tight tolerances at every step, is a new capability for a generalist robot model. All tasks of both benchmarks are shown in Sec. A.1.

**中文:** 需要精确与灵巧的长时序任务。当 GR00T 2 在串联多个精细步骤的长时序任务上进行后训练时，同样的预训练也带来了收益。在六个 YAM 任务上（从分 24 个阶段端到端组装玩具汽车，到将线缆插入断路器），GR00T 2 的平均成功率达到 71.7%，而 VLA 与 WAM 基线至多为 12.5%（Tab. 1a and Fig. 3）。在七个灵巧手任务上（例如过滤粗盐、维生素 C 检测，以及更换 GB300 内存模块），GR00T 2 的平均成功率达到 68.6%，而 GR00T 1.7 与 𝜋0.5 至多为 0.7%（Tab. 1b）。在每一步都要求灵巧手与严苛公差的前提下端到端完成此类任务，对通用机器人模型而言是一项新能力。两个基准测试的全部任务均展示于 Sec. A.1。

<a id="S132"></a>
**Source:** p.8 S132

**Original:** GR00T 2 Turbo. Although Turbo is designed primarily for onboard deployment on edge devices (Sec. 2), it still retains much of GR00T 2 capability. In zero-shot evaluation, it stays close to GR00T 2 on YAM and ranks second among the evaluated models on Dexter (Tabs. 2 and 3). After post-training it gives up some success, reaching 65.0% on the YAM tasks and 34.3% on the dexterous-hand tasks, still well above the baselines. Fig. 23 shows the resulting trade-off between task progress and inference latency.

**中文:** GR00T 2 Turbo。尽管 Turbo 主要为边缘设备上的机载部署而设计（Sec. 2），它仍保留了 GR00T 2 的大部分能力。在零样本评测中，它在 YAM 上与 GR00T 2 接近，在 Dexter 上在所评测模型中排名第二（Tabs. 2 and 3）。经过后训练后，它损失了一部分成功率：在 YAM 任务上达到 65.0%，在灵巧手任务上达到 34.3%，仍远高于基线。Fig. 23 展示了任务进度与推理时延之间由此产生的权衡。
