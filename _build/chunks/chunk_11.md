<a id="S895"></a>
**Source:** p.46 S895

**Original:** Learning without teleoperation. Without a single teleoperated demonstration, GR00T 2 succeeds in 65%, 30%, 10%, and 50% of trials on Filter Paper Setup, Dropper-to-Beaker Dispensing, Microscope Slide Dabbing, and Conveyor Package Tossing (Fig. 27). Both baselines fail every chemistry-lab trial in the same setting and succeed only on tossing, with 20% without cross-embodiment pretraining and 5% for GR00T 1.7. The human demonstrations carry the task: without them, the same GR00T 2 recipe succeeds in 0% of trials on every task. Tossing shows that this transfer extends beyond teleoperation: GR00T 2 learns the throw entirely from humans.

**中文:** 无需遥操作的学习。在没有任何一条遥操作演示的情况下，GR00T 2 在 Filter Paper Setup、Dropper-to-Beaker Dispensing、Microscope Slide Dabbing 和 Conveyor Package Tossing 四项任务上的试次成功率分别为 65%、30%、10% 和 50%（Fig. 27）。两个基线在同一设置下的每个化学实验室试次中均告失败，仅在抛掷任务上取得成功：不做跨本体预训练的基线成功率为 20%，GR00T 1.7 为 5%。承担任务的是人类演示：去掉它们后，同一套 GR00T 2 配方在每项任务上的成功率均为 0%。抛掷任务表明，这种迁移并不局限于遥操作：GR00T 2 完全从人类那里学会了抛掷动作。

<a id="S896"></a>
**Source:** p.46 S896

**Original:** Teleoperation adds to human data. Teleoperated demonstrations refine the task that human demonstrations teach rather than replace them. With 10 demonstrations, GR00T 2 succeeds in 95%, 70%, and 50% of chemistry-lab trials, compared with 45%, 40%, and 30% without cross-embodiment pretraining and 0% for GR00T 1.7. On Filter Paper Setup, GR00T 2 without teleoperation already outperforms the baseline trained with 10 teleoperated demonstrations.

**中文:** 遥操作对人类数据起补充作用。遥操作演示细化的是人类演示所教授的任务，而不是取代它们。使用 10 条演示时，GR00T 2 在化学实验室试次上的成功率分别为 95%、70% 和 50%；不做跨本体预训练时分别为 45%、40% 和 30%，GR00T 1.7 为 0%。在 Filter Paper Setup 上，不使用遥操作的 GR00T 2 已经超过使用 10 条遥操作演示训练的基线。

![F028](assets/F028.png)

<a id="C031"></a>
**Source:** p.47 C031 · 图 F028

**Original (caption):** Figure 28: Predicted futures for tasks that only humans demonstrated. Given one robot start frame and the instruction, GR00T 2 predicts the robot’s ego view autoregressively. Each GR00T 2 row comes from a single rollout that starts at the first frame of an evaluation episode, and times are measured from that frame. Human demonstrations (top rows) appear only in training.

**中文（图注）：** 图 28：仅由人类演示的任务的预测未来画面。给定一个机器人起始帧和指令，GR00T 2 以自回归方式预测机器人的第一人称视角画面。每一行 GR00T 2 结果都来自一次 rollout（轨迹采样），其起点为某个评测片段的第一帧，时间自该帧起算。人类演示（顶部几行）仅出现在训练中。

<a id="S939"></a>
**Source:** p.47 S939

**Original:** B.1.5. Why GR00T 2 Learns without Teleoperation

**中文:** B.1.5. 为什么 GR00T 2 无需遥操作也能学习

<a id="S940"></a>
**Source:** p.47 S940

**Original:** Two baselines test the two properties that let GR00T 2 learn without teleoperation (Fig. 27). Each replaces one component of GR00T 2, the model formulation or the pretraining data, and keeps the post-training data, sampling weights, step budget, and evaluation protocol fixed.

**中文:** 两个基线分别检验让 GR00T 2 无需遥操作即可学习的两项特性（Fig. 27）。每个基线替换 GR00T 2 的一个组件，即模型形式或预训练数据，同时保持后训练数据、采样权重、步数预算和评测协议不变。

<a id="S941"></a>
**Source:** p.47 S941

**Original:** World-action model. GR00T 2 learns from human-only task data because it is a world-action model. Unlike a VLA that must learn task and embodiment in one observation-to-action map, from human-hand observations paired with retargeted actions, GR00T 2 factorizes the problem into two parts. Future-video prediction learns what should happen to the scene, a change that human and robot largely share, while action prediction learns how this robot produces that change, from robot play data. To test the formulation, we compare GR00T 2 with GR00T 1.7, a VLA pretrained on the same data and post-trained with the same recipe. The two models also differ in backbone and initialization, so the comparison tests the WAM design as a whole rather than the prediction target alone. GR00T 1.7 fails every chemistry-lab trial, even with 10 teleoperated demonstrations: under the same data and step budget, the VLA learns these precise tasks neither from human demonstrations nor from a few robot demonstrations. The factorization also makes a direct prediction: for a task that only humans demonstrated, GR00T 2 should predict robot hands rather than human hands. Conditioned on one robot start frame, GR00T 2 predicts the robot’s own hands reaching each milestone of all four tasks (Fig. 28).

**中文:** 世界-动作模型（WAM）。GR00T 2 仅从人类任务数据中学习，是因为它是一个世界-动作模型。与视觉-语言-动作（VLA）模型不同，后者必须在一个观测到动作的映射中同时学习任务和本体，而该映射的训练数据是人手观测与重定向动作的配对；GR00T 2 则把问题分解为两部分。未来视频预测学习场景应当如何变化，这一变化在人类与机器人之间大体相同；动作预测则从机器人自由操作数据中学习该机器人如何产生这种变化。为检验这一形式，我们将 GR00T 2 与 GR00T 1.7 进行比较。GR00T 1.7 是一个在同样数据上预训练、并用相同配方后训练的 VLA。两个模型在主干网络和初始化上也有差异，因此该比较检验的是 WAM 设计的整体，而不仅是预测目标。即使使用 10 条遥操作演示，GR00T 1.7 在每个化学实验室试次上仍告失败：在相同的数据和步数预算下，该 VLA 既无法从人类演示中学会这些精细任务，也无法从少量机器人演示中学会。这种分解还带来一个直接预测：对于只由人类演示过的任务，GR00T 2 应当预测机器人的手，而不是人手。给定一个机器人起始帧，GR00T 2 预测的是机器人自身的手在四项任务的每个里程碑处伸出的画面（Fig. 28）。

<a id="S942"></a>
**Source:** p.47 S942

**Original:** Cross-embodiment pretraining. GR00T 2 transfers task knowledge from the human hand to the robot hand because it pretrains across embodiments. Unlike target-only pretraining that ties task knowledge to one body, cross-embodiment pretraining teaches GR00T 2 to express one task through many bodies. To test this property, we fix the GR00T 2 model and its post-training and replace the full pretraining mixture with target-robot data alone, at a matched pretraining budget. The full mixture adds robot embodiments, human data, and scale at once, so this comparison measures the value of the GR00T 2 mixture as a whole. Without cross-embodiment pretraining, GR00T 2 fails every chemistry-lab trial without teleoperation and trails the full model at every number of teleoperated demonstrations, 45%, 40%, and 30% against 95%, 70%, and 50% at 10.

**中文:** 跨本体预训练。GR00T 2 能把任务知识从人手迁移到机器人手上，是因为它在多种本体上进行预训练。与只针对目标本体预训练、把任务知识绑定到单一身体上的做法不同，跨本体预训练让 GR00T 2 能够通过多种身体表达同一项任务。为检验这一特性，我们固定 GR00T 2 模型及其后训练，仅把完整预训练混合数据替换为目标机器人数据，且预训练预算保持一致。完整混合数据同时增加了机器人本体、人类数据和数据规模，因此该比较衡量的是 GR00T 2 数据混合的整体价值。去掉跨本体预训练后，GR00T 2 在不使用遥操作时的每个化学实验室试次中均告失败，并且在每一种遥操作演示数量下都落后于完整模型：分别为 45%、40% 和 30%，完整模型则为 95%、70% 和 50%（最后一组对应 10 条演示）。

<a id="S943"></a>
**Source:** p.47 S943

**Original:** Human-level motion beyond teleoperation. GR00T 2 achieves human-level motion agility, because learning directly from human demonstrations removes the speed ceiling that teleoperation imposes on robot data. A teleoperator perceives the scene through delayed video, feels no contact, and acts through a mismatched impedance, so teleoperated demonstrations are inherently slower and more conservative than natural human motion, and policies trained on them inherit this limit. Conveyor Package Tossing tests this directly: it is a targeted throw, not a simple toss. The robot must identify each package, grasp it from the moving belt, and release it at the correct phase of a fast arm swing so that it lands in the bin assigned to that package, a skill that is impractical to teleoperate. The demonstrator performs the task at natural speed in the capture rig, and GR00T 2 learns it from the converted demonstrations and robot play data alone, with no task-specific robot data, succeeding in 50% of trials. Removing the teleoperator thus does more than lower collection cost: it expands the set of behaviors a robot can learn to those that require human-level speed.

**中文:** 超越遥操作的人类水平动作。GR00T 2 实现了人类水平的动作敏捷性，因为直接从人类演示中学习，消除了遥操作施加在机器人数据上的速度上限。遥操作者通过有延迟的视频感知场景，无法感受接触，并以不匹配的阻抗进行操作，因此遥操作演示天生比自然的人类动作更慢、更保守，而在其上训练的策略也继承了这一限制。Conveyor Package Tossing 对此做了直接检验：它是一次有目标的抛掷，而不是简单的扔。机器人必须识别每个包裹，从移动的传送带上抓起它，并在手臂快速摆动的正确阶段松开，使包裹落入分配给它的箱子中，这种技能很难通过遥操作完成。示范者在采集装置中以自然速度完成该任务，GR00T 2 仅从转换后的演示和机器人自由操作数据中学习，没有任何任务专用的机器人数据，成功率达到 50%。因此，去掉遥操作者不只是降低了采集成本，还扩展了机器人可以学会的行为范围，使其包括那些需要人类水平速度的行为。

### B.2. UMI →YAM ｜ B.2 节：从 UMI 到 YAM 的迁移

<a id="S945"></a>
**Source:** p.48 S945

**Original:** Suppose a bimanual gripper robot must learn to take apart an electronics assembly on a factory bench it has never seen: unscrew a nut, lift out a gear and two housings, unplug the connectors and cables, and place every part in a tray. No teleoperation data exist for this robot, and collecting them would tie up the robot, a station, and an operator for the full campaign. With GR00T 2 the task can instead be demonstrated with Gripper UMI, a handheld parallel gripper in the lineage of the Universal Manipulation Interface (UMI, Chi et al., 2024 and Sec. E.2): a person holding the device performs the job with natural motions at natural speed, while robot-style wrist cameras and a width encoder record the demonstration in robot coordinates, with no robot in the loop (Sec. E.1). The difficulty is that the handheld device and the robot are different embodiments. Whereas prior

**中文:** 设想一台双臂夹爪机器人需要在一张从未见过的工厂工作台上拆解电子组件：拧下螺母，取出一个齿轮和两个外壳，拔下连接器和线缆，并把每个零件放进托盘。这台机器人没有遥操作数据，而采集这些数据会让一台机器人、一个工位和一名操作员在整个评测批次中都被占用。借助 GR00T 2，这项任务可以改用 Gripper UMI 来演示。Gripper UMI 是一款手持平行夹爪，属于 Universal Manipulation Interface（UMI，Chi et al., 2024 and Sec. E.2）的技术谱系：持设备的人以自然动作、自然速度完成工作，同时类机器人的腕部相机和宽度编码器以机器人坐标记录演示，全程无需机器人参与（Sec. E.1）。难点在于，手持设备与机器人是不同的本体。而此前的 [存疑：句子在第 48 页截断，续句见 S946]

<a id="S946"></a>
**Source:** p.48 S946

**Original:** UMI deployments avoid this by construction, with a robot end-effector that reproduces the handheld device’s cameras and fingers (Chi et al., 2024), the target robot here, YAM, shares none of these components, and the two embodiments differ in all three respects at once: in sensing because YAM’s wrist cameras share neither the lens nor the viewpoint of the handheld device, in actuation because YAM’s arm, gripper, and control space have no counterpart in handheld data, and in environment because the demonstrations are collected in the wild and the policy runs in a robot cell the demonstrations never show (Fig. 42).

**中文:** 以往的 UMI 部署通过构造规避了这一问题，即采用一个复现手持设备相机和手指的机器人末端执行器（Chi et al., 2024）。而这里的目标机器人 YAM 不与手持设备共享这些组件，两种本体在三个方面同时存在差异：在感知上，YAM 的腕部相机与手持设备既不共用镜头，也不共用视点；在驱动上，YAM 的机械臂、夹爪和控制空间在手持数据中没有对应项；在环境上，演示是在野外采集的，而策略运行于演示中从未出现过的机器人工作单元（robot cell）中（Fig. 42）。

<a id="S947"></a>
**Source:** p.48 S947

**Original:** Closing this gap decouples data collection from the deployment platform, and the decoupling pays off along three axes. The first is generality: the same handheld demonstrations transfer to off-the-shelf robots with their own cameras, grippers, and controllers, so a task collected once need not be re-collected for each platform. The second is capability: the handheld device records motion at human speed with natural contact feedback, so dynamic skills such as tossing, which teleoperation renders slow and conservative, become learnable. The third is efficiency: adding a task requires no robot, no instrumented cell, and no operator training. Demonstrations are recorded in the wild after a few dozen minutes of setup, whereas teleoperation ties up a robot, a station, and a trained operator for the entire collection. The demonstration budget itself is small: with roughly 20 handheld episodes, the policy still completes Toy Dumptruck Assembly end to end (10% success, 81 progress) and still sorts 84% of the conveyor items on Conveyor Belt Sorting and Tossing, and even 10 episodes sort 70% (Tab. 17).

**中文:** 弥合这一差距使数据采集与部署平台解耦，而解耦的收益体现在三个方面。第一是通用性：同一套手持演示可以迁移到带有自身相机、夹爪和控制器的现成机器人上，因此一项任务只需采集一次，无需为每个平台重新采集。第二是能力：手持设备以人类速度记录动作，并保留自然的接触反馈，因此抛掷这类动态技能变得可以学习，而遥操作会使其变得缓慢而保守。第三是效率：增加一项任务不需要机器人、带仪器的工作单元，也不需要培训操作员。演示可以在几十分钟的准备之后，在野外录制；而遥操作会在整个采集过程中占用一台机器人、一个工位和一名受过训练的操作员。演示预算本身也很小：仅用约 20 个手持片段，策略仍能端到端完成 Toy Dumptruck Assembly（成功率 10%，进度 81），仍能分拣 Conveyor Belt Sorting and Tossing 中 84% 的传送带物品，即使只有 10 个片段也能分拣 70%（Tab. 17）。

<a id="S948"></a>
**Source:** p.48 S948

**Original:** What makes the transfer work. Three design choices carry the transfer, each closing one gap, and Sec. E.3 ablates all of them.

**中文:** 使迁移成功的关键。三项设计选择承担了迁移，每一项弥合一种差距，Sec. E.3 对它们逐一做了消融。

<a id="S949"></a>
**Source:** p.48 S949

**Original:** • Co-training with task-agnostic robot data closes the embodiment and scene gap. GR00T 2 is post-trained on the UMI demonstrations together with YAM teleoperation data from four general in-lab corpora that contain no episode of the target tasks, typically at a 0.6 : 0.4 ratio: the YAM data supply the embodiment and the scene, the UMI data supply the task. The effect is visible in the model’s own predictions, which render YAM’s arms rather than the demonstrator’s once YAM data are present (Fig. 14). • Aligning the wrist view closes the geometric part of the sensing gap. We re-render the UMI fisheye as a virtual pinhole camera that imitates YAM’s wrist view, fitted in Isaac Sim on 112 paired renders (Fig. 43). The alignment is only approximate, yet without it end-to-end success falls to 0% on both long-horizon tasks. • Sharing the action head grounds the task in the robot’s own action space. UMI actions are re-expressed in YAM’s semantics and decoded by YAM’s weights, so the task evidence lands directly in the statistics

**中文:** • 与任务无关的机器人数据的联合训练弥合了本体与场景差距。GR00T 2 在 UMI 演示之外，还与 YAM 遥操作数据一同进行后训练；这些数据来自四个通用的实验室内语料库，不包含任何目标任务片段，通常按 0.6 : 0.4 的比例混合：YAM 数据提供本体与场景，UMI 数据提供任务。这一效果可以从模型自身的预测中看出：一旦加入 YAM 数据，模型渲染出的是 YAM 的机械臂，而非演示者的手臂（Fig. 14）。• 对齐腕部视角弥合了感知差距中的几何部分。我们把 UMI 鱼眼图像重新渲染为一台模拟 YAM 腕部视角的虚拟针孔相机，并在 Isaac Sim 中利用 112 组成对渲染图进行拟合（Fig. 43）。这一对齐只是近似的，但若没有它，两项长时序任务的端到端成功率都会降至 0%。• 共享动作头使任务落在机器人自身的动作空间中。UMI 动作被重新表达为 YAM 的语义，并由 YAM 的权重解码，因此任务证据直接落入

<a id="C032"></a>
**Source:** p.49 C032 · 图 F029

**Original (caption):** Figure 29: Zero-teleop transfer from UMI to YAM. Each row shows one task with the language instruction GR00T 2 receives and six keyframes of a YAM rollout, numbered by stage: Toy Dumptruck Assembly, NIST Board Disassembly, and Conveyor Belt Sorting and Tossing. Every task is demonstrated only with the handheld Gripper UMI, and YAM has no teleoperation data of these tasks.

**中文（图注）：** 图 29：从 UMI 到 YAM 的零遥操作迁移。每一行展示一项任务，包括 GR00T 2 接收到的语言指令，以及一次 YAM rollout（轨迹采样）中按阶段编号的六个关键帧，任务依次为 Toy Dumptruck Assembly、NIST Board Disassembly，以及 Conveyor Belt Sorting and Tossing。每项任务都只通过手持 Gripper UMI 演示，而 YAM 没有这些任务的遥操作数据。

![F029](assets/F029.png)

<a id="S950"></a>
**Source:** p.49 S950

**Original:** the controller executes.

**中文:** 控制器执行。 [存疑：抽取断句，为 S949 的续句]

<a id="S951"></a>
**Source:** p.49 S951

**Original:** Tasks and protocol. We evaluate on three tasks (Fig. 29): Toy Dumptruck Assembly and NIST Board Disassembly, two long-horizon tasks, an assembly and a disassembly, that chain unscrewing, part removal, flipping, and drilling, and Conveyor Belt Sorting and Tossing, a dynamic task paced by the belt. Each task is demonstrated with 41 to 75 handheld episodes and co-trained with YAM teleoperation data that contain no episode of the target tasks. All models share the post-training recipe and step budget, and the policy predicts 48-step action chunks, of which 30 are executed.

**中文:** 任务与协议。我们在三项任务上进行评测（Fig. 29）：Toy Dumptruck Assembly 与 NIST Board Disassembly 是两项长时序任务，分别为装配与拆解，串联了拧螺丝、取出零件、翻转和钻孔；Conveyor Belt Sorting and Tossing 则是由传送带节奏限定的动态任务。每项任务使用 41 至 75 条手持片段进行演示，并与不包含任何目标任务片段的 YAM 遥操作数据联合训练。所有模型共享相同的后训练配方与步数预算，策略预测 48 步的动作块，其中 30 步被执行。

<a id="C033"></a>
**Source:** p.49 C033 · 表 T004

**Original (caption):** Table 4: Zero-teleop transfer from UMI to YAM. For each model, Prog. is the average substage score and SR the end-to-end success rate on YAM, both on a 0 to 100 scale. Every task is demonstrated only with Gripper UMI (41 to 75 episodes) and co-trained with task-agnostic YAM teleoperation data. All models share the post-training recipe and step budget. GR00T 2 w/o UMI pretraining starts from an earlier GR00T 2 pretraining checkpoint whose mixture contains no UMI data (Sec. E.2). Toy Dumptruck Assembly and NIST Board Disassembly use 10 trials. Conveyor Belt Sorting and Tossing scores each of 50 items as sorted or missed, so its SR is the share of items sorted and it has no separate progress score. The last row averages SR over the three tasks and therefore mixes this per-item rate with the per-trial success rates of the two long-horizon tasks. Bold marks the best Prog. and SR in each row.

**中文（表注）：** 表 4：从 UMI 到 YAM 的零遥操作迁移。对每个模型，任务进度（Prog.）为其在 YAM 上的平均子阶段得分，成功率（SR）为 YAM 上的端到端成功率，两者均采用 0 至 100 的标度。每项任务仅用 Gripper UMI 演示（41 至 75 条片段），并与不针对任务的 YAM 遥操作数据联合训练。所有模型共享相同的后训练配方与步数预算。GR00T 2 w/o UMI pretraining 从较早的 GR00T 2 预训练检查点开始，其混合数据不含 UMI 数据（Sec. E.2）。Toy Dumptruck Assembly 与 NIST Board Disassembly 使用 10 次试次。Conveyor Belt Sorting and Tossing 将 50 个物品各自计为已分拣或已遗漏，因此其成功率为已分拣物品的比例，且没有单独的任务进度得分。最后一行对三项任务的成功率取平均，因此把该任务的逐物品比例与两项长时序任务的逐试次成功率混在了一起。每行中最佳的任务进度与成功率以粗体标出。

![T004](assets/T004.png)

<a id="S956"></a>
**Source:** p.49 S956

**Original:** Results. With 41 to 75 handheld episodes per task, GR00T 2 reaches 60% and 50% end-to-end success on the two long-horizon tasks, with progress scores of 96 and 86, and sorts 86% of the 50 conveyor items, on a robot never teleoperated for any of these tasks, whereas the baselines 𝜋0.5, LingBot-VA, and GR00T 1.7 complete neither long-horizon task and sort at most 28% of the conveyor items (Tab. 4). The decisive ingredient lies upstream of the recipe: starting from a pretraining checkpoint without UMI data, with identical post-training data, drops success to 20% and 0% on the long-horizon tasks and the share of conveyor items sorted to 34%. A few dozen handheld demonstrations therefore suffice because the embodiments were aligned before post-training began. Sec. E.3 quantifies the three gaps and ablates each component of the recipe.

**中文:** 结果。每项任务使用 41 至 75 条手持片段，GR00T 2 在两项长时序任务上分别达到 60% 和 50% 的端到端成功率，进度得分分别为 96 与 86，并在 50 个传送带物品中分拣出 86%。这台机器人从未针对这些任务接受过遥操作。相比之下，基线 𝜋0.5、LingBot-VA 和 GR00T 1.7 在两项长时序任务上均未完成，分拣的传送带物品至多为 28%（Tab. 4）。决定性因素位于配方的上游：若从不含 UMI 数据的预训练检查点开始，并使用完全相同的后训练数据，则长时序任务的成功率降至 20% 和 0%，分拣比例降至 34%。因此，几十条手持演示就已足够，原因在于各本体在后训练开始之前已经对齐。Sec. E.3 量化了三类差距，并对配方的每个组件做了消融。

<a id="C034"></a>
**Source:** p.50 C034 · 表 T005

**Original (caption):** Table 5: DexUMI post-training results. Fraction of real-robot trials that reach the end of each subtask. Overall is the fraction that completes the whole task.

**中文（表注）：** 表 5：DexUMI 后训练结果。表示真实机器人试次中到达每个子任务终点的比例。Overall 表示完成整个任务的比例。

![T005](assets/T005.png)
