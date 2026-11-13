### J.2. Accelerating GR00T 2 Development with Simulation ｜ 借助仿真加速 GR00T 2 开发

<a id="S2125"></a>
**Source:** p.119 S2125

**Original:** Once generated, the simulation environments can be used for many different applications. We first quantify the utility of our simulation suite by comparing the outcomes of GR00T 2 policy evaluations in sim and in real (Sec. J.2.1). We then highlight how these high-fidelity environments contributed to GR00T 2 development, including: optimization of GR00T 2 inference for deployment (Sec. J.2.2), faster iteration on the GR00T 2 pretraining process (Sec. J.2.3), and the development of agentic recovery skills in simulation that assist GR00T 2 during real-world deployment (Sec. J.2.4).

**中文:** 仿真环境生成之后，可以用于许多不同的应用。我们首先通过比较 GR00T 2 策略在仿真与真实环境中的评测结果，量化仿真套件的效用（Sec. J.2.1）。随后，我们说明这些高保真环境如何助力 GR00T 2 的开发，包括：面向部署的 GR00T 2 推理优化（Sec. J.2.2）、加快 GR00T 2 预训练过程的迭代（Sec. J.2.3），以及在仿真中开发智能体化恢复技能，以在真实部署中辅助 GR00T 2（Sec. J.2.4）。

![F062](assets/F062.png)

<a id="C091"></a>
**Source:** p.120 C091 · 图 F062

**Original (caption):** Figure 62: Reconstructed assembly tasks. Toy plane, Hot Wheels car, and toy tractor (left to right), shown in reset configurations (top) and assembled configurations (bottom). Camera and scale are held fixed within each column. The panels illustrate asset configurations rather than robot-policy success.

**中文（图注）：** Figure 62：重建的装配任务。玩具飞机、Hot Wheels 小车和玩具拖拉机（从左到右），分别展示复位配置（上排）和装配完成配置（下排）。每一列内相机与比例尺保持固定。各面板展示的是资产配置，而非机器人策略的成功率。

![F063](assets/F063.png)

<a id="C092"></a>
**Source:** p.120 C092 · 图 F063

**Original (caption):** Figure 63: From physical objects to sim-ready assets. Source photograph, input scan, reconstructed visual asset, handling collision hulls (purple), and fitting signed-distance-field (SDF) source surfaces (teal) for the same tractor body, from left to right. Circular close-ups compare the same wheel shaft: a coarse solid handling shape and the fitting bore with reconstructed thread geometry.

**中文（图注）：** Figure 63：从物理物体到仿真就绪资产。从左到右依次为同一拖拉机车身的原始照片、输入扫描、重建的视觉资产、用于处理的碰撞外壳（紫色），以及用于拟合的有符号距离场（SDF）源表面（青色）。圆形特写对比同一根车轮轴：左侧为粗略的实体处理形状，右侧为拟合用的孔，并带有重建的螺纹几何。

<a id="S2127"></a>
**Source:** p.120 S2127

**Original:** J.2.1. Sim and Real Policy Evaluation Correlation Analysis

**中文:** J.2.1. 仿真与真实策略评测的相关性分析

<a id="S2128"></a>
**Source:** p.120 S2128

**Original:** In order for our simulation suite to be useful, it is important for simulation to be calibrated with the real world. In this section, we gauge our simulation quality by seeing if it can be used as convincing surrogate for real world evaluation (Ranawaka et al., 2026; Jain et al., 2025). We test our policies zero-shot in simulation, without additional fine-tuning or co-training with simulation data, and find that the simulation evaluations strongly correlate with real-world results. This enables the testing of policies at a scale, cadence, and level of reproducibility that would be intractable for real-world evals.

**中文:** 要让仿真套件真正有用，仿真就必须与真实世界相互校准。本节通过判断仿真能否作为真实世界评测的可信替代手段，来衡量仿真质量（Ranawaka et al., 2026; Jain et al., 2025）。我们在仿真中以零样本方式测试策略，不做额外微调，也不与仿真数据联合训练，结果发现仿真评测与真实世界结果高度相关。这使得策略测试能够达到真实世界评测难以企及的规模、节奏和可复现性水平。

<a id="S2129"></a>
**Source:** p.120 S2129

**Original:** Setup. We evaluate 14 checkpoints in both simulation and the real world on matched setups across 25 tasks on the YAM embodiment. Additionally, we evaluate 10 tasks on the DROID (Khazatsky et al., 2024) embodiment with 5 generalist checkpoints. Each task is evaluated for 5 trials on the real robots, and 10 trials in simulation.

**中文:** 设置。我们在 YAM 本体上，以匹配的设置，在仿真与真实世界中分别评测了 14 个检查点，涵盖 25 项任务。此外，我们在 DROID（Khazatsky et al., 2024）本体上用 5 个通用检查点评测了 10 项任务。每项任务在真实机器人上评测 5 次试次，在仿真中评测 10 次试次。

<a id="S2130"></a>
**Source:** p.120 S2130

**Original:** Metrics. We measure sim and real correlation using Pearson Correlation Coefficient (r), Spearman Rank Correlation Coefficient (𝜌) and the Mean Maximum Rank Violation (MMRV) proposed by Li et al. (2024). For a simulation that perfectly reflects real-world conditions, we would observe 𝑟→1, indicating that policy performance in simulation matches that in the real world, 𝜌→1, indicating that the relative rankings of policies are maintained between simulation and the real world, and MMRV →0, indicating that the number of policy ranking violations are minimized. These correlations are calculated for task progress, success rate and the

**中文:** 指标。我们使用 Pearson 相关系数（Pearson Correlation Coefficient, r）、Spearman 秩相关系数（𝜌），以及 Li et al. (2024) 提出的平均最大秩违例（MMRV）来衡量仿真与真实世界之间的相关性。对于完全反映真实世界条件的仿真，我们应观察到 𝑟→1，表明仿真中的策略表现与真实世界一致；𝜌→1，表明策略的相对排序在仿真与真实世界之间得以保持；MMRV →0，表明策略排序违例的数量被最小化。这些相关性分别针对任务进度、成功率以及 [公式原文见 p.120]

![F064](assets/F064.png)

<a id="C093"></a>
**Source:** p.121 C093 · 图 F064

**Original (caption):** Figure 64: Robot assembly of the toy plane. Wing insertion, reorientation, and fastening with a power drill, shown from left to right during a single continuous demonstration-guided execution.

**中文（图注）：** Figure 64：玩具飞机的机器人装配。在一次连续的、由演示引导的执行过程中，从左到右依次展示机翼插入、调整朝向，以及使用电动钻紧固。

![F065](assets/F065.png)

<a id="C094"></a>
**Source:** p.121 C094 · 图 F065

**Original (caption):** Figure 65: Sim-real Pearson correlation per policy for three computed metrics, compared with the noise ceiling: the correlation a perfect simulator would reach given the same number of real and simulated trials.

**中文（图注）：** Figure 65：每个策略在三项计算指标上的仿真-现实 Pearson 相关性，并与噪声上限进行比较。噪声上限是指在真实试次数与仿真试次数相同的情况下，完美仿真器所能达到的相关性。

<a id="S2142"></a>
**Source:** p.121 S2142

**Original:** Bradley-Terry (BT) (Bradley and Terry, 1952) Elo ratings of the checkpoints. Task progress is the rubric score of a trial, a weighted sum of the completed sub-tasks between 0 and 1, and a trial is successful when the score is 1. Both are averaged within each task and then across tasks. MMRV is reported for task progress and success rate.

**中文:** 检查点的 Bradley-Terry（BT）（Bradley and Terry, 1952）Elo 评分。任务进度是某次试次的评分表（rubric）得分，即已完成子任务的加权和，取值在 0 到 1 之间；当得分为 1 时，该试次判定为成功。两者先在每项任务内取平均，再在所有任务之间取平均。MMRV 针对任务进度和成功率进行报告。

<a id="S2143"></a>
**Source:** p.121 S2143

**Original:** Bradley-Terry Elo. Real-world evaluations use blinded A/B tests: in each trial, two or three checkpoints run in randomized order from the same initial setup (based on a corresponding simulation initialization), and every pair of checkpoints in the trial forms one comparison, won by the higher score (equal scores count as a tie). We fit BT ratings to these pairwise outcomes. In simulation, every checkpoint is evaluated on the same fixed initial layouts (10 per task), so any two checkpoints can be compared layout by layout without re-running them.

**中文:** Bradley-Terry Elo。真实世界评测采用盲法 A/B 测试：在每次试次中，两个或三个检查点以随机顺序，从同一初始设置（基于对应的仿真初始化）出发运行；该试次中每一对检查点构成一次比较，得分较高者获胜（得分相同计为平局）。我们将 BT 评分拟合到这些成对结果上。在仿真中，每个检查点都在相同的固定初始布局（每项任务 10 个）上评测，因此任意两个检查点都可以逐布局比较，而无需重新运行。

<a id="S2144"></a>
**Source:** p.121 S2144

**Original:** Results on YAM embodiment. We evaluate 14 GR00T 2 variants across 25 YAM tasks in the same simulator. We completed real-world trials with the A/B evaluation procedure defined earlier. For each trial, we aligned the object initialization with the simulation using projected overlays. We find that our simulator predicts policy performance with high correlations with the real world, with a Pearson 𝑟up to 0.93 for task progress and BT Elo score. Since evaluations in both the real world and simulation can be non-deterministic, and the number of trials per task is limited, there is an effective statistical ceiling to how high these correlations can be for even a perfect simulator. Following Lage-Castellanos et al. (2019), we estimate this ceiling by assuming a perfect simulator. For checkpoint 𝑐on task 𝑡, let ˆ𝑝𝑐𝑡= 𝑠𝑐𝑡/𝑛𝑐𝑡be its real-world success rate (𝑠𝑐𝑡successes in 𝑛𝑐𝑡trials), which we treat as its true success probability. In each repetition, we generate two independent evaluations from these true values, one standing in for the real robot and one for a perfect simulator, each with 𝑛𝑐𝑡trials:

**中文:** YAM 本体上的结果。我们在同一仿真器中，于 25 项 YAM 任务上评测了 14 个 GR00T 2 变体。真实世界试次按照前文定义的 A/B 评测流程完成。对于每次试次，我们利用投影叠加图，使物体初始化与仿真保持对齐。我们发现，仿真器能够以较高相关性预测真实世界中的策略表现，任务进度与 BT Elo 评分的 Pearson 𝑟 最高可达 0.93。由于真实世界与仿真中的评测都可能是非确定性的，且每项任务的试次数有限，即使是完美的仿真器，这些相关性也存在一个有效的统计上限。沿用 Lage-Castellanos et al. (2019) 的做法，我们假设存在一个完美仿真器来估计该上限。对于任务 𝑡 上的检查点 𝑐，令 ˆ𝑝𝑐𝑡= 𝑠𝑐𝑡/𝑛𝑐𝑡 为其真实世界成功率（在 𝑛𝑐𝑡 次试次中有 𝑠𝑐𝑡 次成功），并将其视为真实成功概率。在每次重复中，我们依据这些真实值生成两组独立评测，一组代表真实机器人，另一组代表完美仿真器，每组各含 𝑛𝑐𝑡 次试次：[公式原文见 p.121]

<a id="S2158"></a>
**Source:** p.121 S2158

**Original:** where 𝑇𝑐is the number of tasks for checkpoint 𝑐and the two binomial draws are independent. This gives one real and one perfect-simulator score per checkpoint, and we compute the Pearson correlation ˜𝑟= corr(˜x, ˜y)

**中文:** 其中 𝑇𝑐 为检查点 𝑐 的任务数，两次二项抽样相互独立。由此，每个检查点各得到一个真实得分和一个完美仿真器得分，并计算 Pearson 相关系数 ˜𝑟= corr(˜x, ˜y)。[公式原文见 p.121]

![F066](assets/F066.png)

<a id="C095"></a>
**Source:** p.122 C095 · 图 F066

**Original (caption):** Figure 66: Simulated vs. real-world performance per policy on DROID. We evaluate 5 generalist checkpoints on the DROID embodiment across 10 tasks, with 5 real-world and 10 simulated trials per task, on the same layouts for every checkpoint. Panels and metrics as in Fig. 18: (a) task progress and (b) success rate averaged over tasks (dashed: 𝑦= 𝑥), and (c) Bradley-Terry Elo (dashed: least-squares fit).

**中文（图注）：** Figure 66：DROID 上每个策略的仿真与真实世界表现对比。我们在 DROID 本体上用 5 个通用检查点评测了 10 项任务，每项任务进行 5 次真实试次和 10 次仿真试次，且每个检查点使用相同布局。面板与指标同 Fig. 18：(a) 任务进度与 (b) 成功率（对任务取平均；虚线：𝑦= 𝑥），以及 (c) Bradley-Terry Elo（虚线：最小二乘拟合）。[公式原文见 p.122]

<a id="S2190"></a>
**Source:** p.122 S2190

**Original:** across the 14 checkpoints. Since ˜x and ˜y share the same true values, they differ only because of the limited number of trials, so the median of ˜𝑟over 1,000 repetitions is the expected correlation any simulator could achieve with this evaluation budget. As shown in Fig. 65, our simulator produces correlations that are within 95% −99% of this ceiling.

**中文:** 跨 14 个检查点。由于 ˜x 与 ˜y 具有相同的真实值，二者之间的差异仅来自有限的试次数，因此 1,000 次重复中 ˜𝑟 的中位数，就是在该评测预算下任何仿真器都可能达到的期望相关性。如 Fig. 65 所示，我们的仿真器所得相关性处于该上限的 95% −99% 之内。[公式原文见 p.122]

<a id="S2191"></a>
**Source:** p.122 S2191

**Original:** Results on DROID embodiment. Separately, we evaluate five generalist DROID checkpoints including GR00T 2 and publicly available models on environments reconstructed from real-world DROID setups. We use the same five layouts per task for each checkpoint in the real-world and the same ten layouts in simulation, to minimize variation in trial initializations. Once again, we see high Pearson r of 0.98, 0.95, 0.97 for task progress, success rate and BT Elo respectively. This demonstrates that our agentic real-to-sim reconstruction method is viable for different embodiments.

**中文:** DROID 本体上的结果。此外，我们在根据真实世界 DROID 装置重建的环境中，评测了五个通用 DROID 检查点，包括 GR00T 2 和若干公开可用模型。为尽量减少试次初始化带来的差异，每个检查点在真实世界中使用每项任务相同的五种布局，在仿真中使用相同的十种布局。我们再次观察到较高的 Pearson r：任务进度、成功率和 BT Elo 分别为 0.98、0.95 和 0.97。这表明我们的智能体化现实到仿真重建方法适用于不同本体。

<a id="S2192"></a>
**Source:** p.122 S2192

**Original:** J.2.2. GR00T 2 Inference Optimization through Simulation

**中文:** J.2.2. 借助仿真优化 GR00T 2 推理

<a id="S2193"></a>
**Source:** p.122 S2193

**Original:** Inference optimization aims to help GR00T 2 respond sooner to new observations while preserving task success and smooth motion. We optimize model execution and the processing and transfer of observations, and vary the number of steps used to refine video and action predictions (see Accelerating Model Inference). Simulation provides a repeatable setting for testing how these changes affect behavior. We can restart each trial from the same scene without repeatedly setting up a physical workcell, making it practical to screen settings before robot testing.

**中文:** 推理优化的目标，是让 GR00T 2 在保持任务成功率和动作平滑性的同时，更快地响应新的观测。我们优化模型执行，以及观测的处理与传输，并改变用于细化视频与动作预测的步数（参见 Accelerating Model Inference）。仿真为测试这些改动如何影响行为提供了可重复的环境。我们可以从同一场景重新开始每次试次，而无需反复搭建物理工作单元（workcell），因此在机器人测试之前筛选设置是切实可行的。

<a id="S2194"></a>
**Source:** p.122 S2194

**Original:** Changes that reduce prediction time can also change action predictions, so task success and motion quality must be checked together. For each checkpoint, we keep the number of actions per prediction fixed while comparing original PyTorch execution with TensorRT and CUDA Graphs and testing different numbers of refinement steps. In a YAM cube-handover pilot, several settings completed the task but differed in motion smoothness. Follow-up trials of the same checkpoint and task on a physical YAM robot also showed this distinction. In separate runtime comparisons, the optimized implementation supported more frequent updates to the action plan with comparable task progress in simulation.

**中文:** 缩短预测时间的改动也可能改变动作预测，因此必须同时检验任务成功率与动作质量。对于每个检查点，我们在保持每次预测的动作数不变的前提下，比较原始 PyTorch 执行与 TensorRT 和 CUDA Graphs，并测试不同数量的细化步数。在 YAM 方块交接（cube-handover）先导实验中，若干设置都完成了任务，但在动作平滑性上存在差异。同一检查点和任务在物理 YAM 机器人上的后续试次也显示了这一差异。在单独的运行时对比中，经过优化的实现支持更频繁地更新动作计划，同时在仿真中保持了相当的任务进度。

<a id="S2195"></a>
**Source:** p.122 S2195

**Original:** Simulation also helps us prototype real-time chunking (RTC), which connects new action predictions to actions already scheduled for execution. In separate simulation experiments (see Policy Smoothness), we compare RTC training with and without noise added to the previous action sequence. Repeated trials from matched scenes with controlled prediction delays help us assess whether smoother transitions between action sequences preserve task success, without testing every delay setting on physical robots.

**中文:** 仿真同样有助于我们原型化实时分块（RTC），它将新的动作预测与已排定执行的动作衔接起来。在单独的仿真实验中（参见 Policy Smoothness），我们比较了在先前动作序列上加入噪声与不加噪声两种情形下的 RTC 训练。来自匹配场景、且预测延迟可控的重复试次，帮助我们评估动作序列之间更平滑的过渡是否能保持任务成功率，而无需在物理机器人上测试每一种延迟设置。

<a id="S2197"></a>
**Source:** p.123 S2197

**Original:** We measure prediction latency directly on the target hardware, separately from simulated task duration. Ordinary synchronous simulation pauses while waiting for predictions, so it does not reproduce the effect of inference delay on a moving robot. The RTC experiments explicitly model this delay, but physical-robot tests remain necessary to check behavior under actual deployment timing. Simulation narrows the settings taken to these tests, where we assess task success and motion quality on the target robot.

**中文:** 我们直接在目标硬件上测量预测时延，并与仿真中的任务时长分开计算。普通的同步仿真会在等待预测期间暂停，因此无法复现推理延迟对运动中机器人的影响。RTC 实验显式地建模了这一延迟，但物理机器人测试对于检验实际部署时序下的行为仍然必不可少。仿真将进入这些测试的设置范围缩小，而这些测试用于在目标机器人上评估任务成功率与动作质量。

<a id="S2198"></a>
**Source:** p.123 S2198

**Original:** J.2.3. GR00T 2 Pretraining Acceleration with Simulation

**中文:** J.2.3. 借助仿真加速 GR00T 2 预训练

<a id="S2199"></a>
**Source:** p.123 S2199

**Original:** Simulation enabled faster iteration on GR00T 2 pretraining through many different means.

**中文:** 仿真通过多种途径，加快了 GR00T 2 预训练的迭代。

<a id="S2200"></a>
**Source:** p.123 S2200

**Original:** Monitoring of pretraining progress and checkpoint selection. Evaluating a single pretraining checkpoint across a large set of real-world tasks can take hours. Simulation provides a faster way to compare policies across a diverse task set during model development. During GR00T 2 pretraining, we evaluated intermediate checkpoints on a set of tasks from our simulation suite to inspect their closed-loop behavior and compare model capabilities as training progressed. These comparisons help us identify overfitting as we iterate on the model, and assess the relative performance of our checkpoints and external baselines without running extensive real-world evaluations for every candidate.

**中文:** 预训练进度监控与检查点选择。在大量真实世界任务上评估单个预训练检查点，可能需要数小时。仿真提供了一种更快的方式，可在模型开发过程中，于多样化的任务集上比较策略。在 GR00T 2 预训练期间，我们在仿真套件的一组任务上评估了中间检查点，以考察其闭环行为，并随训练推进比较模型能力。这些比较帮助我们在迭代模型时识别过拟合，并评估我们的检查点与外部基线的相对表现，而无需对每个候选模型都进行大规模的真实世界评测。

<a id="S2201"></a>
**Source:** p.123 S2201

**Original:** Simulation also guided checkpoint selection: we used a subset of our simulation suite (25 tasks) to determine which checkpoints showed promising closed-loop evaluation results. This provided a stable way to understand if checkpoints were worth physical robot evaluation. As a concrete example, we used this workflow to finalize our pretrained model: simulation results narrowed the candidates to three checkpoints, which we then evaluated on physical robots to select the final checkpoint. In this way, simulation was a tool to guide checkpoint analysis and development, but we still used physical-robot evaluation to validate conclusions about real-world performance.

**中文:** 仿真还指导了检查点选择：我们使用仿真套件中的一个子集（25 项任务），来判断哪些检查点在闭环评测中表现出良好前景。这为判断某个检查点是否值得进行物理机器人评测，提供了稳定的依据。作为具体例子，我们借助该流程确定了预训练模型的最终版本：仿真结果将候选检查点缩小到三个，随后我们在物理机器人上对它们进行评估，以选出最终检查点。由此，仿真是引导检查点分析与开发的工具，但我们仍以物理机器人评测来验证关于真实世界表现的结论。

<a id="S2202"></a>
**Source:** p.123 S2202

**Original:** Optimizing the data pipeline. Changes to the data loading and processing pipeline are costly to assess through full-scale pretraining. We expect a new pipeline that processes the data correctly and preserves training dynamics to produce model performance comparable to the existing pipeline. We test this expectation with small-scale training and closed-loop simulation before adopting a new pipeline for pretraining.

**中文:** 优化数据流水线。对数据加载与处理流水线的改动，若要通过全规模预训练来评估，代价高昂。我们预期，一条能够正确处理数据并保持训练动态的新流水线，将产生与现有流水线相当的模型性能。在将新流水线用于预训练之前，我们先通过小规模训练和闭环仿真对这一预期进行检验。

<a id="S2203"></a>
**Source:** p.123 S2203

**Original:** As an example, we compared five configurations that varied sequence packing, mixed-shard sampling, and text-token masking. For each configuration, we post-trained a model on real-robot teleoperation data from the YAM Scoop and Unscrew tasks, then evaluated it on simulated versions of those tasks. Simulation was used only for evaluation. The new data loading pipeline showed no observed regression in closed-loop simulation performance relative to the existing pipeline, giving us confidence to adopt it for pretraining.

**中文:** 举例来说，我们比较了五种配置，它们在序列打包（sequence packing）、混合分片采样（mixed-shard sampling）和文本 token 掩码（text-token masking）方面各有不同。对每种配置，我们都在 YAM Scoop 和 Unscrew 任务的真实机器人遥操作数据上进行后训练，随后在这些任务的仿真版本上进行评估。仿真仅用于评估。相对于现有流水线，新的数据加载流水线在闭环仿真性能上未观察到退化，这让我们有信心将其用于预训练。

<a id="S2204"></a>
**Source:** p.123 S2204

**Original:** J.2.4. Agentic Skill Development in Simulation

**中文:** J.2.4. 在仿真中开发智能体化技能

<a id="S2205"></a>
**Source:** p.123 S2205

**Original:** Simulation also helps us develop specialized manipulation skills. As described in Sec. G.1, ASPIRE learns skills that code-as-policy (CaP) can invoke alongside GR00T 2 to carry out difficult steps or recover from failures. For example, the toy plane assembly task (Fig. 64) provided a repeatable setting for developing recovery skills that transferred to physical robots. In simulation, we could test candidate behaviors, inspect failures, and refine the skills before evaluating them on the physical system.

**中文:** 仿真同样帮助我们开发专门的操作技能。如 Sec. G.1 所述，ASPIRE 学习的技能可以与 GR00T 2 一同，由代码即策略（code-as-policy, CaP）调用，用于完成困难步骤或从故障中恢复。例如，玩具飞机装配任务（Fig. 64）提供了一个可重复的环境，用于开发能够迁移到物理机器人上的恢复技能。在仿真中，我们可以测试候选行为、检查故障，并在将技能用于实体系统之前加以改进。
