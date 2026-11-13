<a id="S1948"></a>
**Source:** p.106 S1948

**Original:** Agent Cost and Latency. Steering adds the agent’s cost and latency to every episode, which we measure on trash sorting on both robots (Tab. 24). With visual guidance, an episode takes a median of 9 agent turns and costs $0.26 on YAM and $0.14 on Dexter, and the robot waits for the agent during 38% and 32% of the episode. GR00T 2 was served without the accelerations of Sec. 4.6.1 on YAM (about 0.6 s per policy call) and with TensorRT on Dexter (about 0.14 s).

**中文:** 智能体成本与时延。引导会为每个回合（episode）增加智能体的成本和时延，我们在两台机器人上对垃圾分拣任务进行了测量（Tab. 24）。加入视觉引导后，一个回合的中位数为 9 次智能体轮次，智能体成本在 YAM 上为 0.26 美元，在 Dexter 上为 0.14 美元，机器人分别有 38% 和 32% 的回合时间在等待智能体。GR00T 2 在 YAM 上未使用 Sec. 4.6.1 中的加速手段（每次策略调用约 0.6 秒），在 Dexter 上则使用 TensorRT（约 0.14 秒）。

<a id="S1949"></a>
**Source:** p.106 S1949

**Original:** Detecting Step Completion. The agent’s cost and the robot’s waiting also depend on when the harness queries the agent at the end of a step. In the YAM long-horizon runs, gripper events, which need no model call,

**中文:** 检测步骤完成。智能体的成本和机器人的等待时间，还取决于调度框架在步骤结束时何时查询智能体。在 YAM 长时序运行中，夹爪事件无需模型调用，

![T024](assets/T024.png)

<a id="C080"></a>
**Source:** p.107 C080 · 表 T024

**Original (caption):** Table 24: Agent cost and latency on trash sorting. Medians over the 20 episodes per setting. Latency is the per-episode median agent-turn time, agent cost is the charge for the agent’s turns (excluding the completion checks), and waiting is the share of the episode during which the robot holds still for the agent.

**中文（表注）：** 表 24：垃圾分拣任务上的智能体成本与时延。中位数基于每种设置下的 20 个回合（episode）。时延为每个回合的智能体轮次时间中位数；智能体成本为智能体轮次的费用（不含完成性检查）；等待占比为回合中机器人保持静止、等待智能体的时间比例。

<a id="S1962"></a>
**Source:** p.107 S1962

**Original:** triggered 418 of the 435 step-end queries, and the 45 s limit triggered the remaining 17. The completion check is meant for steps that end without a release, such as closing a drawer, but replaying the logged requests shows that even an always-correct check would confirm a step a median of 3.9 to 6.7 s after it ends, against about 1.5 s for a gripper event. Polled throughout every step, the checks also account for 26 to 36% of the combined agent and check charge on YAM, so we keep the check as a backstop.

**中文:** 在 435 次步骤结束查询中触发了 418 次，其余 17 次由 45 秒的时限触发。完成性检查原本用于那些没有释放动作就结束的步骤，例如关闭抽屉，但重放记录的请求后可以看到，即使一个总是正确的检查，也只能在步骤结束后中位数 3.9 至 6.7 秒才确认该步骤，而夹爪事件约为 1.5 秒。若在每个步骤中全程轮询，这些检查在 YAM 上还会占智能体与检查合计费用的 26% 至 36%，因此我们保留该检查作为兜底。

<a id="S1963"></a>
**Source:** p.107 S1963

**Original:** Failure Analysis. Failures on YAM trash sorting differ in kind between the two agent-guided settings. With visual guidance, 6 of 100 items are lost, in 3 episodes, and each of these episodes contains a failed hand-over, in which the agent asked one arm to stage an item at the center of the table for the other arm. By the agent’s step-end observations, every release aimed at a bin landed in the marked bin, with one case unclear. Of the 54 items lost with language guidance, 21 were released into a wrong bin, or a different item was moved, after the agent had named the correct bin, and 20 were never attempted because the agent spent the remaining steps retrieving misplaced items. On Dexter trash sorting, visual guidance leaves 11 items in a wrong bin, against 43 with language guidance and 56 for GR00T 2, while a similar share of pick-and-place attempts ends in some bin in every setting (72%, 65%, and 71%), so the settings differ mainly in choosing the right bin.

**中文:** 故障分析。在 YAM 垃圾分拣任务中，两种智能体引导设置下的失败类型并不相同。视觉引导下，100 件物品中有 6 件丢失，分布在 3 个回合中，而且这 3 个回合都包含一次失败的交接，即智能体要求一条手臂将物品暂放到桌面中央，供另一条手臂接取。根据智能体的步骤结束观察，每次指向垃圾桶的释放都落入了标记的垃圾桶，其中一次情况不明。语言引导下丢失的 54 件物品中，有 21 件被释放到错误的垃圾桶中，或者在智能体已说出正确垃圾桶之后移动了另一件物品；另有 20 件从未被尝试，因为智能体把剩余步数花在了找回错放的物品上。在 Dexter 的垃圾分拣任务上，视觉引导使 11 件物品落入错误的垃圾桶，语言引导为 43 件，GR00T 2 为 56 件；同时，各设置中抓放尝试最终落入某个垃圾桶的比例相近（分别为 72%、65% 和 71%），因此这些设置之间的差异主要在于能否选中正确的垃圾桶。

<a id="S1964"></a>
**Source:** p.107 S1964

**Original:** Simulation Test of Steerability on LIBERO. Simulation lets us test steerability without the agent by computing the markers from the simulator state. We evaluate 45 tasks from LIBERO-PRO (Zhou et al., 2025), which perturbs the scenes and instructions of LIBERO (Liu et al., 2023), with 10 episodes per task (448 valid episodes), including spatial-instruction variants of a two-bowl scene on which an earlier language-only checkpoint failed, to test steering where language is weak. We compare a single-arm language-only checkpoint with a single-arm point-conditioned checkpoint, both mid-trained for 20k steps on RoboCasa365 (Nasiriany et al., 2026), LIBERO, and DROID (Khazatsky et al., 2024). This simulation checkpoint uses an earlier, richer form of the interface: a time-colored end-effector path with a disc at the next grasp or release point. The markers raise success from 69.6% (312 of 448) for the language-only checkpoint to 85.0% (381), while the same point-conditioned checkpoint with nothing drawn reaches 72.5% (325). On the two-bowl variants, the markers raise success from 18 of 70 for the language-only checkpoint (20 with nothing drawn) to 41 of 70. Across tasks, the marked checkpoint does better than the language-only checkpoint on 13, worse on 8, and ties on the other 24.

**中文:** LIBERO 上的引导能力仿真测试。仿真让我们无需智能体即可测试引导能力，标记可以直接从仿真器状态计算得出。我们评测了 LIBERO-PRO（Zhou et al., 2025）中的 45 个任务，该基准对 LIBERO（Liu et al., 2023）的场景和指令进行了扰动。每个任务 10 个回合（共 448 个有效回合），其中包括双碗场景的空间指令变体，一个较早的仅语言检查点在该场景上失败过，这里用来测试语言较弱时的引导能力。我们比较了单臂仅语言检查点与单臂点条件检查点，二者都在 RoboCasa365（Nasiriany et al., 2026）、LIBERO 和 DROID（Khazatsky et al., 2024）上中期训练了 20k 步。该仿真检查点使用的是接口的早期、信息更丰富的形式：一条按时间着色的末端执行器轨迹，并在下一个抓取或释放点处画一个圆盘。标记将仅语言检查点的成功率从 69.6%（448 个中的 312 个）提升到 85.0%（381），而同一点条件检查点在不画任何标记时达到 72.5%（325）。在双碗变体上，标记将仅语言检查点的成功数从 70 中的 18 个（不画任何标记时为 20 个）提升到 70 中的 41 个。跨任务来看，加标记的检查点在 13 个任务上优于仅语言检查点，在 8 个任务上更差，其余 24 个任务持平。

<a id="S1965"></a>
**Source:** p.107 S1965

**Original:** Limitations. Visual steering also has three limitations. The points specify spatial targets and the acting arm, not a manipulation strategy, which limits the gains on grasp and action references. Every step moves one arm, so coordinated two-arm motion is excluded, and a hand-over becomes two single-arm steps. On the real robots, generalization to new scenes and objects is not tested.

**中文:** 局限性。视觉引导还有三个局限。这些点指定的是空间目标和执行动作的手臂，而不是操作策略，因此限制了在抓取参考和动作参考上的收益。每个步骤只移动一条手臂，因此不包括双臂协调运动，交接也会被拆分为两个单臂步骤。在真实机器人上，尚未测试对新场景和新物体的泛化能力。

### G.3. Toward Robotic Self-Improvement ｜ 迈向机器人自我改进

<a id="S1966"></a>
**Source:** p.107 S1966

**Original:** Agentic learning, execution, and steering address complementary challenges in building autonomous robotic systems. AutoResearch investigates how learning algorithms can be improved through autonomous experimentation. CaP enables structured orchestration and specialized intervention during long-horizon execution.

**中文:** 智能体化学习、执行与引导，分别针对构建自主机器人系统中的互补挑战。AutoResearch 研究如何通过自主实验改进学习算法。代码即策略（code-as-policy, CaP）支持在长时序执行过程中进行结构化编排和专门化干预。

<a id="S1967"></a>
**Source:** p.108 S1967

**Original:** Visual guidance allows a high-level reasoning model to steer the behavior of a foundation policy through richer interfaces beyond language.

**中文:** 视觉引导使高层推理模型能够通过语言之外更丰富的接口，引导基础策略的行为。

<a id="S1968"></a>
**Source:** p.108 S1968

**Original:** A promising direction for future work is to integrate these capabilities into a unified self-improvement process. During deployment, agentic execution and steering could identify difficult states, generate corrective behaviors, and collect interaction experiences that expose limitations of the current foundation policy.

**中文:** 未来工作中一个有前景的方向，是把这些能力整合进统一的自我改进流程。在部署过程中，智能体化执行与引导可以识别困难状态、生成纠正行为，并收集能够暴露当前基础策略局限性的交互经验。

<a id="S1969"></a>
**Source:** p.108 S1969

**Original:** These experiences could be incorporated into AutoResearch to discover better post-training strategies, while successful agentic behaviors could be distilled into the foundation policy to improve its generality and reduce the need for future intervention.

**中文:** 这些经验可以纳入 AutoResearch，以发现更好的后训练策略；而成功的智能体化行为则可以蒸馏到基础策略中，以提升其通用性，并减少未来对人工干预的需要。

<a id="S1970"></a>
**Source:** p.108 S1970

**Original:** Such integration would create a feedback loop in which agentic systems improve not only how robots execute tasks, but also how their underlying policies are trained and adapted.

**中文:** 这样的整合将形成一个反馈回路，使智能体化系统不仅改进机器人执行任务的方式，也改进其底层策略的训练与适配方式。

<a id="S1971"></a>
**Source:** p.108 S1971

**Original:** Although realizing this fully integrated loop remains a direction for future work, these three approaches illustrate complementary opportunities for building robotic systems that can autonomously learn, orchestrate, and adapt their behavior.

**中文:** 尽管完全整合的闭环仍是未来工作的方向，但这三种路径共同展示了构建机器人系统的互补机会，使其能够自主学习、编排并调整自身行为。

### H. Humanoid Loco-Manipulation ｜ 人形机器人移动操作

<a id="S1972"></a>
**Source:** p.109 S1972

**Original:** Loco-manipulation for bipedal humanoids poses additional challenges for robot foundation models, as humanoids must achieve precise end-effector control while maintaining balance under complex whole-body dynamics. Given these stringent requirements for reactive control, we turn to GR00T 2 Turbo, the lightweight variant of GR00T 2 suitable for deployment on edge devices (e.g. NVIDIA Jetson AGX Thor (Maheshwari et al., 2025)). We extend GR00T 2’s two-level architecture with SONIC (Luo et al., 2026) to form a three-level hierarchy (Fig. 9). A reasoning model, System 2 (S2), selects the task. Conditioned on this task and the current observations, GR00T 2 Turbo, System 1 (S1), generates short-horizon whole-body motion commands in SONIC’s compact latent action space. SONIC, System 0 (S0), translates these motion commands into joint-level commands while maintaining balance. Both S1 and S0 run onboard the robot, coupling task-directed motion generation with reactive whole-body control.

**中文:** 对双足人形机器人而言，移动操作带来了额外的挑战：人形机器人必须在复杂的全身动力学下保持平衡，同时实现精确的末端执行器控制。鉴于反应式控制的这些严格要求，我们采用 GR00T 2 Turbo，它是 GR00T 2 的轻量版本，适用于边缘设备部署（例如 NVIDIA Jetson AGX Thor（Maheshwari et al., 2025））。我们用 SONIC（Luo et al., 2026）扩展 GR00T 2 的两级架构，形成三级层级结构（Fig. 9）。推理模型系统 2（S2）负责选择任务。在该任务与当前观测的条件下，GR00T 2 Turbo 即系统 1（S1）在 SONIC 的紧凑潜变量动作空间中生成短时序的全身运动指令。SONIC 即系统 0（S0），在保持平衡的同时将这些运动指令转换为关节级指令。S1 与 S0 均在机器人本体上运行，将任务导向的运动生成与反应式全身控制耦合在一起。

<a id="S1973"></a>
**Source:** p.109 S1973

**Original:** Our investigation shows that GR00T 2 Turbo achieves high success rates across four task settings that highlight complementary aspects of whole-body loco-manipulation: scooping and serving popcorn, which requires precise bimanual tool use while standing; clearing diverse objects from a table into bins, which requires long-horizon coordination of walking, reaching, grasping, and carrying; and floor-level tasks, such as wiping spills with the feet and picking up objects while squatting or kneeling, which require coordinated upper- and lower-body motion.

**中文:** 我们的考察表明，GR00T 2 Turbo 在四类任务设置上取得了较高的成功率，这些设置分别突出了全身移动操作的不同方面：舀取并盛放爆米花，需要在站立时进行精确的双臂工具使用；将桌面上的各类物品清入垃圾桶，需要长时序协调行走、伸手、抓取和搬运；地面任务，例如用脚擦拭洒落物，以及下蹲或跪地拾取物品，需要上下肢协调运动。

<a id="S1974"></a>
**Source:** p.109 S1974

**Original:** All post-training data for whole-body loco-manipulation comes from whole-body teleoperation, which is expensive to collect and hard to scale. We therefore augment it with a large amount of synthetic data from a real-to-sim pipeline: teleoperated pick-and-place motions are fitted to the S0 controller and rolled out in simulation, so the synthetic demonstrations share the action space of the real data. GR00T 2 Turbo makes better use of this simulated data than the GR00T 1.7 VLA baseline, especially on out-of-distribution tabletop pick-and-place: starting from the same 6.7% success with real data alone, co-training raises GR00T 2 Turbo to 63.3%, compared with 40.0% for GR00T 1.7 (Tab. 26).

**中文:** 全身移动操作的全部后训练数据都来自全身遥操作，采集成本高，也难以扩展。因此，我们用大量来自现实到仿真（real-to-sim）流程的合成数据对其进行扩充：遥操作得到的抓放动作被拟合到 S0 控制器上并在仿真中展开，因此合成演示与真实数据共享同一动作空间。相比 GR00T 1.7 VLA 基线，GR00T 2 Turbo 更好地利用了这些仿真数据，尤其是在分布外的桌面抓放任务上：在仅使用真实数据、同为 6.7% 的成功率基础上，联合训练将 GR00T 2 Turbo 提升至 63.3%，而 GR00T 1.7 为 40.0%（Tab. 26）。
