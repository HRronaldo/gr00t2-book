### J.3. Simulation Benchmarking ｜ 仿真基准测试

<a id="S2206"></a>
**Source:** p.123 S2206

**Original:** We evaluate GR00T 2 on five simulation benchmarks that span single-arm mobile manipulation (RoboCasa365), bimanual manipulation (RoboDojo), zero-shot real-to-sim tabletop manipulation (RoboLab, MolmoSpaces) and humanoid loco-manipulation (G1 Factory). Unless stated otherwise, each GR00T 2 result is a single post-trained checkpoint initialized from the same pretrained GR00T 2 model, evaluated with the benchmark’s official task set, episode budget and success criterion. Among VLA and WAM policies on the public leaderboards,4 GR00T 2

**中文:** 我们在五个仿真基准上评测 GR00T 2，它们分别覆盖单臂移动操作（RoboCasa365）、双臂操作（RoboDojo）、零样本现实到仿真的桌面操作（RoboLab、MolmoSpaces）以及人形机器人移动操作（loco-manipulation，G1 Factory）。除非另有说明，每个 GR00T 2 结果都来自同一个预训练 GR00T 2 模型初始化后得到的单一后训练检查点，并按照基准官方任务集、回合预算和成功判定标准进行评测。在公开排行榜的 VLA 与 WAM 策略中，GR00T 2 [存疑：句子在此截断，原文后续内容未抽取]

<a id="S2207"></a>
**Source:** p.123 S2207

**Original:** 4Baselines are taken from the official leaderboards as of November 6, 2026 with the exception of GR00T 1.7 which we retrain and evaluate ourselves.

**中文:** 4 基线取自截至 2026 年 11 月 6 日的官方排行榜，GR00T 1.7 除外，该模型由我们自行重新训练和评测。

![T030](assets/T030.png)

<a id="C096"></a>
**Source:** p.124 C096 · 表 T030

**Original (caption):** Table 30: Results on the RoboCasa365 benchmark. We report success rate (%). The best and second-best results are highlighted in bold and underline, respectively.

**中文（表注）：** RoboCasa365 基准测试结果。报告成功率（%）。最优与次优结果分别以粗体和下划线标出。

<a id="S2209"></a>
**Source:** p.124 S2209

**Original:** 𝜋0.5 (Physical Intelligence et al., 2025) 16.9 39.6 7.1 1.2 GR00T 1.7 (NVIDIA, 2026a) 22.1 41.7 17.7 4.4 Paimon-0 58.1 79.3 55.8 36.7 Axiom-0 (Shu et al., 2026) 61.6 86.5 59.4 35.8 Awomo-0.5V (Awomo-WAM Team, 2026) 62.5 85.0 60.4 39.4 minionx 62.6 81.8 60.0 43.6 Awomo-0.5I (Awomo-WAM Team, 2026) 64.4 86.5 58.8 45.2

**中文:** [存疑：表 30 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] 𝜋0.5 (Physical Intelligence et al., 2025) 16.9 39.6 7.1 1.2 GR00T 1.7 (NVIDIA, 2026a) 22.1 41.7 17.7 4.4 Paimon-0 58.1 79.3 55.8 36.7 Axiom-0 (Shu et al., 2026) 61.6 86.5 59.4 35.8 Awomo-0.5V (Awomo-WAM Team, 2026) 62.5 85.0 60.4 39.4 minionx 62.6 81.8 60.0 43.6 Awomo-0.5I (Awomo-WAM Team, 2026) 64.4 86.5 58.8 45.2

![T031](assets/T031.png)

<a id="C097"></a>
**Source:** p.124 C097 · 表 T031

**Original (caption):** Table 31: Results on the RoboDojo benchmark. Dimension columns report success rate (%), while the last two columns report the average score and success rate (%). GR00T 2 is evaluated on all three layout banks. Tab. 19 reports layout bank 0 only, for all four GR00T 2 configurations including RL and agentic execution. The best and second-best results are highlighted in bold and underline, respectively.

**中文（表注）：** RoboDojo 基准测试结果。各维度列报告成功率（%），最后两列分别报告平均得分和成功率（%）。GR00T 2 在全部三个布局库（layout bank）上评测。Tab. 19 仅报告布局库 0 的结果，涵盖 GR00T 2 的全部四种配置，包括强化学习（RL）和智能体化执行的配置。最优与次优结果分别以粗体和下划线标出。

<a id="S2214"></a>
**Source:** p.124 S2214

**Original:** GR00T 1.7 (NVIDIA, 2026a) 4.1 1.1 11.8 2.6 1.4 7.65 4.20 𝜋0.5 (Physical Intelligence et al., 2025) 8.2 5.5 14.7 4.7 1.7 11.44 6.93 Rex-M1 Preview 26.1 23.8 33.0 48.2 6.1 33.79 27.44 Simate-beta 28.0 26.9 43.4 33.0 8.5 33.95 27.96 Awomo-0.5 (Awomo-WAM Team, 2026) 23.8 33.5 26.8 41.2 22.9 35.34 29.64 VPP2 (Guo et al., 2026) 29.5 35.2 37.0 55.6 4.1 39.26 32.26 WALL-OSS-1.0-lite 37.9 29.1 32.3 56.0 19.6 42.59 34.97

**中文:** [存疑：表 31 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] GR00T 1.7 (NVIDIA, 2026a) 4.1 1.1 11.8 2.6 1.4 7.65 4.20 𝜋0.5 (Physical Intelligence et al., 2025) 8.2 5.5 14.7 4.7 1.7 11.44 6.93 Rex-M1 Preview 26.1 23.8 33.0 48.2 6.1 33.79 27.44 Simate-beta 28.0 26.9 43.4 33.0 8.5 33.95 27.96 Awomo-0.5 (Awomo-WAM Team, 2026) 23.8 33.5 26.8 41.2 22.9 35.34 29.64 VPP2 (Guo et al., 2026) 29.5 35.2 37.0 55.6 4.1 39.26 32.26 WALL-OSS-1.0-lite 37.9 29.1 32.3 56.0 19.6 42.59 34.97

<a id="S2217"></a>
**Source:** p.124 S2217

**Original:** RoboCasa365. RoboCasa365 (Nasiriany et al., 2026) is a large-scale household simulation benchmark with 365 tasks across 2,500 procedurally generated kitchens, in which a mobile manipulator acts from three RGB cameras. Following the official multi-task protocol, we train on the Human300 pretraining mixture and evaluate on 50 target tasks split into 18 Atomic-Seen, 16 Composite-Seen and 16 Composite-Unseen tasks. The last split is absent from training and therefore tests zero-shot composition of learned skills. The overall score is the mean of the 50 per-task success rates. Results are shown in Tab. 30.

**中文:** RoboCasa365（Nasiriany et al., 2026）是一个大规模家庭仿真基准，包含 365 个任务，分布在 2,500 个程序化生成的厨房中，移动操作机器人的动作决策依据三台 RGB 相机的图像。遵循官方多任务协议，我们在 Human300 预训练数据配比上训练，并在 50 个目标任务上评测。这些目标任务分为 18 个 Atomic-Seen、16 个 Composite-Seen 和 16 个 Composite-Unseen 任务。最后一个划分从未出现在训练中，因此用于检验已学技能的零样本组合能力。总分为 50 个任务各自成功率的平均值。结果见 Tab. 30。

<a id="S2218"></a>
**Source:** p.124 S2218

**Original:** GR00T 2 reaches 67.2% average success, 2.8 percentage points above the best prior entry, and it leads on the Atomic-Seen and Composite-Seen splits. Notably, its largest margin is on the Composite-Seen tasks, multi-step activities that chain several learned skills, where it reaches 73.6%, 13.2 points above the next entry (Awomo-0.5V, 60.4%).

**中文:** GR00T 2 的平均成功率达到 67.2%，比此前最优条目高 2.8 个百分点，并且在 Atomic-Seen 和 Composite-Seen 两个划分上领先。最显著的优势出现在 Composite-Seen 任务上，这类多步活动会串接多个已学技能。在这一划分上，GR00T 2 达到 73.6%，比次优条目（Awomo-0.5V，60.4%）高 13.2 个百分点。

<a id="S2219"></a>
**Source:** p.124 S2219

**Original:** RoboDojo. RoboDojo (Chen et al., 2026a) is a bimanual benchmark in Isaac Sim (NVIDIA, 2025) on the 14-DoF ARX-X5 platform, with 42 tasks grouped into five capability dimensions: Generalization (standard and randomized layouts), Precision, Long-Horizon (up to 1,900 control steps), Memory and Open (open-vocabulary instructions with no training demonstrations). Following the official protocol, we run the evaluation over all 42 tasks (54 task configurations) on three layout banks (6,300 episodes) and report the partial-progress score and success rate. Results are shown in Tab. 31.

**中文:** RoboDojo（Chen et al., 2026a）是一个在 Isaac Sim（NVIDIA，2025）中构建的双臂基准，运行在 14 自由度（DoF）的 ARX-X5 平台上，包含 42 个任务，分为五个能力维度：泛化（标准布局与随机布局）、精度、长时序（最多 1,900 个控制步）、记忆，以及开放（使用开放词汇指令且没有训练演示）。遵循官方协议，我们在三个布局库（共 6,300 个回合）上运行全部 42 个任务（共 54 种任务配置），并报告部分任务进度得分和成功率。结果见 Tab. 31。

![T032](assets/T032.png)

<a id="C098"></a>
**Source:** p.125 C098 · 表 T032

**Original (caption):** Table 32: Results on the RoboLab benchmark. We report success rate (%) overall and per difficulty tier. The best and second-best results are highlighted in bold and underline, respectively.

**中文（表注）：** RoboLab 基准测试结果。报告总体成功率（%）以及各难度等级的成功率。最优与次优结果分别以粗体和下划线标出。

<a id="S2222"></a>
**Source:** p.125 S2222

**Original:** GR00T 1.7 (NVIDIA, 2026a) 18.9 22.8 15.9 10.9 𝜋0.5 (Physical Intelligence et al., 2025) 28.0 29.7 31.5 13.5 Atomic-WAM (Shi et al., 2026) 39.6 44.4 40.5 19.4 HiDream-O1-Embodied 39.9 43.1 37.7 32.9 FLUX 3 Action (Black Forest Labs, 2026) 42.9 49.1 39.2 28.2 BiMind v0.5 49.2 51.6 52.6 32.4 Lakeside 51.0 57.6 44.1 42.4

**中文:** [存疑：表 32 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] GR00T 1.7 (NVIDIA, 2026a) 18.9 22.8 15.9 10.9 𝜋0.5 (Physical Intelligence et al., 2025) 28.0 29.7 31.5 13.5 Atomic-WAM (Shi et al., 2026) 39.6 44.4 40.5 19.4 HiDream-O1-Embodied 39.9 43.1 37.7 32.9 FLUX 3 Action (Black Forest Labs, 2026) 42.9 49.1 39.2 28.2 BiMind v0.5 49.2 51.6 52.6 32.4 Lakeside 51.0 57.6 44.1 42.4

![T033](assets/T033.png)

<a id="C099"></a>
**Source:** p.125 C099 · 表 T033

**Original (caption):** Table 33: Results on the MolmoSpaces benchmark. We report success rate (%). The best and second-best results are highlighted in bold and underline, respectively. Baselines: 𝜋0.5-DROID (Physical Intelligence et al., 2025), GR00T 1.7 (NVIDIA, 2026a), MolmoAct2 DROID (Fang et al., 2026), PRTS-Droid (Zhang et al., 2026), WALL-OSS-0.5 (Yu et al., 2026b), and Cosmos3-Nano-Policy (NVIDIA Cosmos Team, 2026).

**中文（表注）：** MolmoSpaces 基准测试结果。报告成功率（%）。最优与次优结果分别以粗体和下划线标出。基线包括：𝜋0.5-DROID (Physical Intelligence et al., 2025)、GR00T 1.7 (NVIDIA, 2026a)、MolmoAct2 DROID (Fang et al., 2026)、PRTS-Droid (Zhang et al., 2026)、WALL-OSS-0.5 (Yu et al., 2026b) 和 Cosmos3-Nano-Policy (NVIDIA Cosmos Team, 2026)。

<a id="S2228"></a>
**Source:** p.125 S2228

**Original:** 𝜋0.5-DROID 22.7 65.1 18.1 6.4 7.0 8.0 12.0 10.2 10.4 17.77 GR00T 1.7 11.9 68.0 35.3 11.7 12.5 7.8 9.4 12.9 11.6 20.12 MolmoAct2 DROID 11.7 71.3 43.4 20.5 21.9 11.1 15.6 18.5 19.3 25.92 PRTS-Droid 12.0 76.3 47.5 18.1 20.5 21.6 17.4 19.0 18.2 27.84 WALL-OSS-0.5 16.8 78.5 78.4 47.9 47.2 30.1 13.8 15.9 18.3 38.55 Cosmos3-Nano-Policy 32.0 79.1 66.5 32.3 32.2 25.7 26.0 22.9 34.3 39.00 ZoeInside-VLA 36.6 85.7 74.8 51.8 55.9 45.5 37.8 21.2 36.2 49.50

**中文:** [存疑：表 33 的数据行，抽取为连续文本，列结构未保留，数值按原文顺序列出] 𝜋0.5-DROID 22.7 65.1 18.1 6.4 7.0 8.0 12.0 10.2 10.4 17.77 GR00T 1.7 11.9 68.0 35.3 11.7 12.5 7.8 9.4 12.9 11.6 20.12 MolmoAct2 DROID 11.7 71.3 43.4 20.5 21.9 11.1 15.6 18.5 19.3 25.92 PRTS-Droid 12.0 76.3 47.5 18.1 20.5 21.6 17.4 19.0 18.2 27.84 WALL-OSS-0.5 16.8 78.5 78.4 47.9 47.2 30.1 13.8 15.9 18.3 38.55 Cosmos3-Nano-Policy 32.0 79.1 66.5 32.3 32.2 25.7 26.0 22.9 34.3 39.00 ZoeInside-VLA 36.6 85.7 74.8 51.8 55.9 45.5 37.8 21.2 36.2 49.50

<a id="S2229"></a>
**Source:** p.125 S2229

**Original:** GR00T 2 (Ours) 20.7 79.0 71.9 42.0 42.9 20.3 44.2 37.5 47.6 45.12 manipulation to coordinated bimanual control. On Precision it leads the strongest prior entry by 4.8 points in success rate (40.0% vs. 35.2%) and reaches the highest partial-progress score (47.7 vs. 43.0), meaning it advances further through fine-grained manipulation even when an episode does not finish.

**中文:** GR00T 2（Ours）20.7 79.0 71.9 42.0 42.9 20.3 44.2 37.5 47.6 45.12 [存疑：句首为 “manipulation to coordinated bimanual control.” 的片段，与前文断开，对应中文应为“……从单臂操作到协同双臂控制”，抽取未保留前文] 在 Precision 维度上，GR00T 2 的成功率比最强的既有条目高 4.8 个百分点（40.0% 对 35.2%），并达到最高的部分任务进度得分（47.7 对 43.0）。这说明即使某个回合没有完成，GR00T 2 也能在精细操作中推进得更远。

<a id="S2231"></a>
**Source:** p.125 S2231

**Original:** RoboLab. RoboLab (Yang et al., 2026) is a high-fidelity Isaac Lab benchmark of 120 tabletop tasks on the DROID (Khazatsky et al., 2024) Franka setup, grouped into 64 simple, 39 moderate and 17 complex tasks. Following the official protocol, we run 10 episodes per task (1,200 episodes) with the default instructions and report binary success rate. Our policy is post-trained only on real DROID data, so this evaluation is zero-shot real-to-sim transfer. Results are shown in Tab. 32.

**中文:** RoboLab（Yang et al., 2026）是一个高保真的 Isaac Lab 基准，包含 120 个桌面任务，基于 DROID（Khazatsky et al., 2024）的 Franka 平台设置，任务分为 64 个简单任务、39 个中等任务和 17 个复杂任务。遵循官方协议，我们每个任务运行 10 个回合（共 1,200 个回合），使用默认指令，并报告二值成功率。我们的策略仅在真实 DROID 数据上进行后训练，因此该评测属于零样本的现实到仿真迁移。结果见 Tab. 32。

<a id="S2232"></a>
**Source:** p.125 S2232

**Original:** GR00T 2 reaches 47.4% success, placing in the top three among non-agentic entries on the leaderboard. Since GR00T 2 is post-trained only on real-world DROID data, this result indicates GR00T 2’s robust zero-shot transfer to unseen simulated scenes and tasks.

**中文:** GR00T 2 达到 47.4% 的成功率，在排行榜的非智能体化条目中位列前三。由于 GR00T 2 仅在真实世界 DROID 数据上进行后训练，这一结果表明 GR00T 2 能够稳健地零样本迁移到未见过的仿真场景和任务。

<a id="S2233"></a>
**Source:** p.125 S2233

**Original:** MolmoSpaces. MolmoSpaces (Kim et al., 2026) evaluates a Franka DROID policy in procedurally generated MuJoCo houses populated with Objaverse (Deitke et al., 2023) objects. Following the leaderboard’s default view, we report success rate on nine suites: articulated Open and Close, four pick suites (Pick-v1.5 and Pick-v2 under the classic renderer, the filament renderer and randomized cameras) and three pick-and-place suites (plain, next-to and color-referred), 8,915 episodes in total. The overall score is the unweighted mean over the nine suites, with unsubmitted suites counted as zero. As with RoboLab, we evaluate the same real-DROID post-trained checkpoint zero-shot. Results are shown in Tab. 33.

**中文:** MolmoSpaces（Kim et al., 2026）在程序化生成的 MuJoCo 房屋中评测 Franka DROID 策略，房屋内放置了 Objaverse（Deitke et al., 2023）物体。遵循排行榜的默认视图，我们报告九个子套件上的成功率：可动关节的 Open 与 Close 子套件、四个抓取（pick）子套件（Pick-v1.5 和 Pick-v2 分别在经典渲染器、Filament 渲染器和随机相机条件下的测试），以及三个抓放（pick-and-place）子套件（普通型、近邻型和颜色指代型），共计 8,915 个回合。总分为九个子套件的未加权平均值，未提交结果的子套件按零计。与 RoboLab 相同，我们对同一个真实 DROID 后训练检查点进行零样本评测。结果见 Tab. 33。

<a id="S2235"></a>
**Source:** p.125 S2235

**Original:** GR00T 2 scores 45.12%, second only to ZoeInside-VLA (49.50%), and it has the best score on all three

**中文:** GR00T 2 得分为 45.12%，仅次于 ZoeInside-VLA（49.50%），并且在全部三个 [存疑：句子在此截断，原文后续内容未抽取]

![T034](assets/T034.png)

<a id="C100"></a>
**Source:** p.126 C100 · 表 T034

**Original (caption):** Table 34: Results on G1 Factory. We report success rate (%) over 100 episodes per task. The best results are highlighted in bold. Baseline: GR00T 1.7 (NVIDIA, 2026a).

**中文（表注）：** G1 Factory 结果。报告每个任务 100 个回合上的成功率（%）。最优结果以粗体标出。基线：GR00T 1.7 (NVIDIA, 2026a)。

<a id="S2243"></a>
**Source:** p.126 S2243

**Original:** pick-and-place suites (44.2%, 37.5% and 47.6% on v2, NextTo and Color). Notably, it leads the spatially referred NextTo suite by 14.6 points (37.5% vs. 22.9% for Cosmos3-Nano-Policy), indicating strong grounding of spatial language. Its weakest suite is Pick-v2 with randomized cameras (20.3%), indicating sensitivity to camera viewpoint.

**中文:** 抓放（pick-and-place）子套件（v2、NextTo 和 Color 上分别为 44.2%、37.5% 和 47.6%）。值得注意的是，它在空间指代的 NextTo 子套件上领先 14.6 个百分点（37.5% 对 22.9%，后者为 Cosmos3-Nano-Policy），表明它对空间语言的落地（grounding）能力较强。其最弱的子套件是随机相机条件下的 Pick-v2（20.3%），说明它对相机视角较为敏感。

<a id="S2244"></a>
**Source:** p.126 S2244

**Original:** G1 Factory. G1 Factory (NVIDIA, 2026c) adapts the nine Unitree G1 loco-manipulation tasks introduced in HumanoidMimicGen (Lin et al., 2026) to NVIDIA Isaac Lab-Arena. The tasks involve lifting and shelving boxes, retrieving and transferring drills, pressing buttons, and pushing a shelving cart with a 43-DoF G1 humanoid. The policy commands the arms, hands, and waist together with base-height and navigation commands that are executed by a lower-body controller. We train on 100 demonstrations per task from the released G1 Factory dataset and evaluate each policy over 100 episodes per task (900 episodes in total). We compare against GR00T 1.7 and report overall success rates in Tab. 34.

**中文:** G1 Factory（NVIDIA，2026c）将 HumanoidMimicGen（Lin et al., 2026）中引入的九个 Unitree G1 移动操作任务适配到 NVIDIA Isaac Lab-Arena 中。任务包括搬运与上架箱子、取出并转移钻头、按压按钮，以及推动置物架推车，所用机器人为 43 自由度（DoF）的 G1 人形机器人。策略同时指令手臂、手部和腰部，并配合基座高度和导航指令，由下肢控制器负责执行。我们使用已发布的 G1 Factory 数据集，每个任务用 100 个演示进行训练，并在每个任务的 100 个回合上评测每个策略（共 900 个回合）。我们与 GR00T 1.7 进行比较，总体成功率见 Tab. 34。

<a id="S2245"></a>
**Source:** p.126 S2245

**Original:** GR00T 2 achieves an overall success rate of 84.7%, outperforming GR00T 1.7 (69.4%) by 15.3 percentage points. It improves success rates on all nine tasks and achieves 100% success on box lifting from both the table and the floor. Remaining failures are concentrated in contact-rich tasks that require precise end-effector placement while the robot maintains balance: drill retrieval from the holder, shelf pushing, and button pressing.

**中文:** GR00T 2 的总体成功率为 84.7%，比 GR00T 1.7（69.4%）高 15.3 个百分点。它在全部九个任务上都提高了成功率，并且在箱子分别位于桌面和地面时的搬运任务上均达到 100% 成功率。剩余的失败主要集中在富接触任务上，这类任务要求机器人在保持平衡的同时精确放置末端执行器，包括从支架上取出钻头、推动置物架和按压按钮。
