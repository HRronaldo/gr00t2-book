### H.3. WAMs Consume Simulation Data Better than VLAs ｜ WAM 对仿真数据的利用优于 VLA

<a id="S2018"></a>
**Source:** p.111 S2018

**Original:** Motion-centric Real-to-Sim Demonstrations. Real-world teleoperation data is costly to collect and limited in scene and object diversity. Our key insight is to reuse the whole-body motions recorded on the G1 by finding simulated scenes in which those motions successfully perform the task. Since teleoperated episodes contain motion and camera observations but not exact table and object poses, we initialize their simulated placements from the head-camera images and refine them using CMA-ES (Hansen et al., 2003). In MuJoCo (Todorov et al., 2012) or Isaac Lab (Mittal et al., 2025), we replay each motion through the same SONIC controller used on the

**中文:** 以运动为中心的现实到仿真演示。真实世界的遥操作数据采集成本高，且场景与物体的多样性有限。我们的核心思路是复用在 G1 上记录的全身运动，为这些运动寻找能让它们成功完成任务的仿真场景。由于遥操作片段包含运动和相机观测，却不包含精确的桌面与物体位姿，我们根据头部相机图像初始化它们在仿真中的摆放位置，并使用 CMA-ES（Hansen et al., 2003）进行优化。在 MuJoCo（Todorov et al., 2012）或 Isaac Lab（Mittal et al., 2025）中，我们使用与真实机器人相同的 SONIC 控制器回放每段运动，

![F059](assets/F059.png)

<a id="C084"></a>
**Source:** p.112 C084 · 图 F059

**Original (caption):** Figure 59: Motion-centric simulation data generation. (A) We use the recorded whole-body motion of a teleoperated episode. (B) SONIC replays the motion in simulation while CMA-ES fits the table and object placement. (C) A fit is kept only if the robot lifts the object and holds it under a pull equal to its weight. (D) The same accepted fit is rendered in many generated rooms.

**中文（图注）：** 图 59：以运动为中心的仿真数据生成。（A）使用一段遥操作片段中记录的全身运动。（B）SONIC 在仿真中回放该运动，同时 CMA-ES 拟合桌面与物体的摆放。（C）只有当机器人抬起物体，并在相当于物体重量的拉力下保持抓握时，拟合结果才会被保留。（D）同一个被接受的拟合结果会在大量生成的房间中渲染。

![T026](assets/T026.png)

<a id="C085"></a>
**Source:** p.112 C085 · 表 T026

**Original (caption):** Table 26: WAMs consume simulation data better than VLAs. Tabletop pick-and-place success rate (%) over 30 trials on the G1 when simulated demonstrations are mixed into the same real dataset.

**中文（表注）：** 表 26：WAM 对仿真数据的利用优于 VLA。当仿真演示与同一真实数据集混合时，G1 上桌面抓放任务的成功率（%），统计范围为 30 次试次。

<a id="S2036"></a>
**Source:** p.112 S2036

**Original:** real robot, keeping the recorded motion fixed while optimizing the scene. The search evaluates 48 candidate scenes in parallel per generation and proceeds in two stages: fitting the table position, height, and yaw; then fitting the object type, position, and orientation on the table. A fit is accepted only if the final rollout grasps the object with both fingers, lifts it, and holds it through a 30-frame disturbance force equal to the object’s weight, followed by a 100-frame hold. We then render these fitted trajectories in procedurally generated environments with randomized lighting and camera placement, recording token sequences and rendered images in the same format as the real demonstrations. The resulting synthetic demonstrations preserve the real-data action space while expanding visual and object diversity. We use this procedure to generate 250,000 synthetic episodes totaling 1,000 hours. The generation procedure and examples are shown in Fig. 59.

**中文:** 真实机器人上运行，保持记录下来的运动不变，只优化场景。搜索过程中，每一代并行评估 48 个候选场景，分为两个阶段：先拟合桌面的位置、高度和偏航角；再拟合桌面上物体的类型、位置和朝向。只有当最终回放中物体被双指抓住、被抬起，并在相当于物体重量的 30 帧扰动力下保持住，随后再保持 100 帧时，该拟合才会被接受。随后，我们在随机化光照和相机位置的程序化生成环境中渲染这些拟合轨迹，所记录的 token 序列与渲染图像与真实演示的格式相同。由此生成的合成演示保留了真实数据的动作空间，同时扩大了视觉与物体的多样性。我们用该流程生成了 250,000 个合成片段，共计 1,000 小时。生成流程与示例见 Fig. 59。

<a id="S2037"></a>
**Source:** p.112 S2037

**Original:** Results. In Tab. 26, we test each policy in distribution, in the environment where the real data were collected, and out of distribution, in unseen scenes and locations. The synthetic data improve the pick-and-place success rate of GR00T 1.7 and GR00T 2 Turbo in both settings, while 𝜋0.5 degrades in distribution. The gain is largest out of distribution, where both GR00T 1.7 and GR00T 2 Turbo start from 6.7% with real data alone. The WAM benefits more from the simulated data in this setting: co-training removes 61% of its failures, compared with 36% for GR00T 1.7, a difference of 25 percentage points. With 30 trials per cell, however, the difference between the two co-trained models (19 against 12 successes) is suggestive rather than conclusive (two-sided Fisher exact test, 𝑝≈0.12).

**中文:** 结果。在 Tab. 26 中，我们分别在分布内（即采集真实数据的环境）和分布外（未见过的场景与地点）两种设定下测试每个策略。合成数据在两种设定下都提升了 GR00T 1.7 和 GR00T 2 Turbo 的抓放成功率，而 𝜋0.5 在分布内出现了性能下降。增益在分布外最大：仅使用真实数据时，GR00T 1.7 和 GR00T 2 Turbo 的起点都是 6.7%。在这一设定下，WAM 从仿真数据中获益更多：联合训练使其失败数减少了 61%，而 GR00T 1.7 为 36%，两者相差 25 个百分点。不过，每个单元格只有 30 次试次，两个联合训练模型之间的差异（19 次成功对比 12 次成功）属于提示性结果，而非结论性结果（双侧 Fisher 精确检验，𝑝≈0.12）。

<a id="S2038"></a>
**Source:** p.112 S2038

**Original:** Why. We hypothesize that this comes from the video prediction objective: the WAM’s more general video encoder maps rendered and camera frames into a shared latent space in which the model predicts how the scene evolves under its actions, a correspondence that is identical in simulation and reality, whereas a VLA maps appearance features tuned to real images directly to actions and treats rendered frames as out-of-distribution.

**中文:** 原因。我们推测这源于视频预测目标：WAM 更具通用性的视频编码器将渲染帧与相机帧映射到一个共享潜空间，模型在该空间中预测场景在其动作作用下如何演化，且这种对应关系在仿真与现实中是一致的。而 VLA 则将针对真实图像调校的外观特征直接映射为动作，并把渲染帧视为分布外输入。

### I. Accelerating GR00T 2 ｜ 加速 GR00T 2

<a id="S2039"></a>
**Source:** p.113 S2039

**Original:** Practical deployment of a generalist robotics foundation model requires timely predictions, continuous motion, and efficient task completion across tasks and embodiments. Deployment on edge hardware also imposes compute, memory, power, and thermal limits. We address these requirements through inference acceleration, training-time real-time chunking (RTC) (Black et al., 2025), and phase-conditioned action chunk retiming. We evaluate latency, task outcomes, and motion quality together.

**中文:** 通用机器人基础模型的实际部署需要及时的预测、连续的运动，以及跨任务和跨本体的高效任务完成。在边缘硬件上部署还会受到算力、内存、功耗和热学约束的限制。我们通过推理加速、训练时实时分块（RTC）（Black et al., 2025）以及相位条件化的动作块重定时来应对这些需求。我们同时评估时延、任务结果与运动质量。

<a id="S2040"></a>
**Source:** p.113 S2040

**Original:** We first reduce inference latency within the deployment resource budget. WAMs in our setting incur higher inference latency than their VLA counterparts, motivating policy inference acceleration and system-level optimizations. Visual encoding and iterative video-action denoising contribute to model prediction latency, while observation processing and communication add delay around the model. We optimize both paths and distinguish model prediction latency from observation-to-applied-action latency. However, some delay remains even after optimization. Waiting for each prediction can interrupt execution, while naively executing predictions asynchronously can introduce discontinuities between successive action chunks. We therefore use training-time real-time chunking (RTC) to account for actions committed during inference and train the policy to produce compatible continuations.

**中文:** 我们首先在部署资源预算内降低推理时延。在我们的设定中，WAM 的推理时延高于其对应的 VLA，因此需要进行策略推理加速和系统级优化。视觉编码与迭代的视频-动作去噪会造成模型预测时延，而观测处理和通信会在模型前后引入额外延迟。我们同时优化这两条路径，并区分模型预测时延与观测到已应用动作的时延。然而，即使经过优化，仍会存在一定延迟。等待每次预测完成会打断执行，而简单地异步执行预测则会在相邻动作块之间引入不连续性。因此，我们使用训练时实时分块（RTC）来考虑推理期间已确定的动作，并训练策略生成与之兼容的后续动作。

<a id="S2041"></a>
**Source:** p.113 S2041

**Original:** Continuity must also preserve the policy’s ability to correct its behavior using new observations. In our setting, standard training-time RTC improves continuity but may degrade task performance. We address this tradeoff with noisy-prefix, action-only RTC. Perturbing the conditioning prefix is intended to reduce reliance on the previous plan while retaining context for a smooth continuation. We further find that a small-scale fine-tuning stage applied to the post-trained base model captures most of the action-continuity benefits, making RTC adaptation practical without repeating the full training pipeline.

**中文:** 连续性还必须保留策略利用新观测修正自身行为的能力。在我们的设定中，标准的训练时 RTC 提高了连续性，但可能降低任务性能。我们通过带噪前缀、仅动作的 RTC 来处理这一权衡。对条件前缀施加扰动，旨在降低对先前计划的依赖，同时保留足够的上下文以实现平滑衔接。我们还发现，对后训练基础模型进行一个小规模微调阶段，就能获得大部分动作连续性收益，从而使 RTC 适配无需重复完整训练流程即可落地。

<a id="S2042"></a>
**Source:** p.113 S2042

**Original:** Finally, continuous execution and low inference latency do not necessarily yield shorter task completion times. We introduce phase-dependent action-chunk acceleration to increase execution speed where the task permits it while retaining finer timing for precise interactions. Accelerated execution also changes the temporal relationship between successive chunks, requiring the continuity mechanism to account for the revised execution timeline. Temporal chunk alignment addresses this timing mismatch, while cross-chunk jerk optimization smooths the transition between successive commands. We evaluate the combined approach through inference latency, motion quality, task completion time, and success rate to establish whether faster execution preserves reliable task performance.

**中文:** 最后，持续执行与低推理时延并不一定意味着更短的任务完成时间。我们引入相位相关的动作块加速，在任务允许的地方提高执行速度，同时在精细交互处保留更精细的时序。加速执行也会改变相邻动作块之间的时间关系，因此连续性机制需要考虑修订后的执行时间线。时间动作块对齐用于解决这一时序失配，而跨块加加速度（jerk）优化则平滑相邻指令之间的过渡。我们通过推理时延、运动质量、任务完成时间和成功率来评估这一组合方法，以确定更快的执行是否仍能保持可靠的任务性能。

### I.1. Accelerating Model Inference ｜ 加速模型推理

<a id="S2043"></a>
**Source:** p.113 S2043

**Original:** Inference uses a client-server architecture: the robot client sends observations and executes returned action chunks through its controller, while the server runs the policy (Sec. K.5).

**中文:** 推理采用客户端-服务器架构：机器人客户端发送观测，并通过其控制器执行返回的动作块，服务器则运行策略（Sec. K.5）。

<a id="S2044"></a>
**Source:** p.113 S2044

**Original:** GR00T 2 predicts action chunks by encoding camera observations, robot state, and task instructions, then iteratively denoising video and action latents. This computation adds delay to the control loop, while observation processing and communication introduce further overhead. We reduce these costs through computation reuse, optimized GPU execution, and a serving path that supports different embodiments and deployment hardware.

**中文:** GR00T 2 通过编码相机观测、机器人状态和任务指令来预测动作块，然后对视频与动作潜变量进行迭代去噪。这一计算会给控制回路增加延迟，而观测处理和通信还会带来进一步的开销。我们通过计算复用、优化的 GPU 执行，以及支持不同本体和部署硬件的服务路径来降低这些成本。

<a id="S2045"></a>
**Source:** p.113 S2045

**Original:** Timing boundaries. The environment continues to change while the policy computes, so prediction time is only part of the delay before a robot responds. We distinguish two intervals (Fig. 60). Model prediction latency covers encoding and iterative denoising performed within a prediction request. Observation-to-applied-action latency extends from observation preparation to controller application, including serialization, transport, and response handling. Streaming and prefetch can move encoding before the prediction request. We identify these configurations explicitly because their foreground prediction time excludes that encoding work.

**中文:** 时序边界。策略计算期间环境仍在变化，因此预测时间只是机器人作出响应前延迟的一部分。我们区分两段时间间隔（Fig. 60）。模型预测时延涵盖单次预测请求内部执行的编码与迭代去噪。观测到已应用动作的时延则从观测准备一直延伸到控制器应用，包括序列化、传输和响应处理。流式处理与预取可以将编码提前到预测请求之前。我们明确列出这些配置，是因为它们的前台预测时间不包含这部分编码工作。

<a id="S2046"></a>
**Source:** p.113 S2046

**Original:** Optimizing model prediction. We first remove repeated computation. The policy reuses text features while the task instruction and model remain unchanged, and refreshes visual and state representations for new observations. For a fixed checkpoint and denoising schedule, timestep-dependent conditioning values are

**中文:** 优化模型预测。我们首先去除重复计算。只要任务指令和模型保持不变，策略就复用文本特征；对于新的观测，则刷新视觉与状态表示。对于固定的检查点和去噪调度，随时间步变化的条件值，

![F060](assets/F060.png)

<a id="C086"></a>
**Source:** p.114 C086 · 图 F060

**Original (caption):** Figure 60: Timing boundaries for GR00T 2 policy inference. Model prediction covers request-time encoding and iterative denoising. Observation-to-applied-action latency additionally includes observation preparation, communication, response handling, and controller scheduling. The diagram is schematic, and stage widths do not represent measured durations.

**中文（图注）：** 图 60：GR00T 2 策略推理的时序边界。模型预测涵盖请求时的编码与迭代去噪。观测到已应用动作的时延还包括观测准备、通信、响应处理和控制器调度。该示意图仅为示意性质，各阶段的宽度并不代表实测时长。

<a id="S2070"></a>
**Source:** p.114 S2070

**Original:** computed in advance. Within the denoising loop, action-only updates reuse attention keys and values from the most recent video update. Persistent buffers reduce repeated cache preparation and copying.

**中文:** 可以预先计算。在去噪循环内，仅动作的更新会复用最近一次视频更新中的注意力键与值。持久缓冲区减少了重复的缓存准备与拷贝。

<a id="S2071"></a>
**Source:** p.114 S2071

**Original:** We then accelerate the remaining computation. TensorRT compiles the video VAE encoder and transformer into specialized GPU engines, and CUDA graph replay reduces CPU dispatch and kernel-launch overhead. For supported checkpoints, we calibrate the BF16-trained model on representative robot observations and apply FP8 to selected projection and feed-forward layers in the joint transformer. Normalization layers and the action-only engine retain higher precision. Supported recipes also use FP8 for VAE encoding. Reducing denoising steps provides an additional tradeoff between latency, task success, and motion smoothness, which we assess for each checkpoint and task.

**中文:** 随后，我们加速剩余的计算。TensorRT 将视频 VAE 编码器和 Transformer 编译为专用的 GPU 引擎，CUDA graph 回放则降低了 CPU 调度和核函数启动的开销。对于支持的检查点，我们使用代表性的机器人观测对 BF16 训练的模型进行校准，并对联合 Transformer 中选定的投影层和前馈层应用 FP8。归一化层与仅动作引擎则保持更高精度。受支持的配方还会对 VAE 编码使用 FP8。减少去噪步数会在时延、任务成功率和运动平滑性之间带来额外的权衡，我们针对每个检查点和任务分别进行评估。

<a id="S2072"></a>
**Source:** p.114 S2072

**Original:** Fig. 19 compares measured model-prediction latency for a GR00T 2 Turbo checkpoint deployed on G1 using RTX 5090 and Jetson Thor.

**中文:** Fig. 19 比较了 GR00T 2 Turbo 检查点部署在 G1 上、分别使用 RTX 5090 与 Jetson Thor 时实测的模型预测时延。

<a id="S2073"></a>
**Source:** p.114 S2073

**Original:** Tab. 27 reports median prediction latency for GR00T 2 and GR00T 2 Turbo across three embodiments and the evaluated hardware. Each baseline-optimized pair uses the same underlying checkpoint and input observations. The optimized configurations provide 2.94× to 7.15× speedup relative to eager BF16 execution. Each speedup applies to the complete configuration: the G1 comparison includes fewer denoising steps, while optimized Dexter and YAM use prefetched VAE representations. The timing boundaries and execution recipes are specified alongside the table.

**中文:** Tab. 27 报告了 GR00T 2 与 GR00T 2 Turbo 在三种本体及所评估硬件上的模型预测中位时延。每个基线-优化配对都使用相同的底层检查点和输入观测。相对于即时 BF16 执行，优化配置实现了 2.94× 至 7.15× 的加速。每项加速都针对完整配置而言：G1 的对比包含了更少的去噪步数，而经过优化的 Dexter 和 YAM 则使用了预取的 VAE 表示。时序边界与执行配方与该表一并给出。

<a id="S2074"></a>
**Source:** p.114 S2074

**Original:** We use one checkpoint per embodiment across hardware comparisons. All three use the 2B model configuration, with five history frames per camera at 224 × 320 pixels (height × width). Dexter uses three camera views in four model slots and a 48-action prediction horizon, YAM uses four views and a 48-action horizon, and the GR00T 2 Turbo checkpoint for G1 uses three views and an 80-action horizon. The notation 2v4a denotes two video and four action denoising steps. Dexter uses 2v2a and YAM uses 2v4a in both baseline and optimized execution. G1 changes from 2v4a to 1v2a, with the action horizon unchanged.

**中文:** 在硬件对比中，我们为每个本体使用一个检查点。三者都采用 2B 模型配置，每个相机保留五个历史帧，分辨率为 224 × 320 像素（高 × 宽）。Dexter 使用三个相机视角、四个模型槽位以及 48 个动作的预测时域；YAM 使用四个视角与 48 个动作的时域；用于 G1 的 GR00T 2 Turbo 检查点则使用三个视角与 80 个动作的时域。记号 2v4a 表示两个视频去噪步和四个动作去噪步。Dexter 在基线与优化执行中都使用 2v2a，YAM 都使用 2v4a。G1 从 2v4a 改为 1v2a，动作时域保持不变。

<a id="S2075"></a>
**Source:** p.114 S2075

**Original:** All optimized configurations use TensorRT and CUDA graphs. Dexter uses FP16-mixed transformer engines with BF16 streaming VAE and prefetch, without codec roundtrip. G1 uses FP8 mixed precision, with VAE encoding included in prediction latency. YAM uses FP8 joint-transformer and VAE engines, a BF16 action engine, and whole-window VAE prefetch with MP4V. For Dexter and YAM, eager timings include VAE encoding, while optimized timings exclude encoding completed before the request.

**中文:** 所有优化配置都使用 TensorRT 与 CUDA graph。Dexter 使用 FP16 混合精度的 Transformer 引擎，配合 BF16 流式 VAE 与预取，且不包含编解码往返。G1 使用 FP8 混合精度，并将 VAE 编码计入预测时延。YAM 使用 FP8 的联合 Transformer 与 VAE 引擎、BF16 的动作引擎，以及使用 MP4V 的整窗口 VAE 预取。对于 Dexter 和 YAM，即时执行的时间包含 VAE 编码，而优化后的时间则不包含在请求前已完成的编码。

![T027](assets/T027.png)

<a id="C087"></a>
**Source:** p.115 C087 · 表 T027

**Original (caption):** Table 27: Median model-prediction latency (p50) for GR00T 2 and GR00T 2 Turbo across embodiments and hardware. Speedup is baseline latency divided by optimized latency.

**中文（表注）：** 表 27：GR00T 2 与 GR00T 2 Turbo 在各本体和硬件上的模型预测中位时延（p50）。加速比为基线时延除以优化后的时延。

<a id="S2083"></a>
**Source:** p.115 S2083

**Original:** We evaluate embodiment-specific checkpoints. Each baseline-optimized pair uses the same underlying checkpoint and input profile. Baselines use unquantized BF16 PyTorch execution with checkpoint-default attention kernels. Baseline revisions are selected per checkpoint to preserve its required model behavior.

**中文:** 我们评估针对具体本体的检查点。每个基线-优化配对都使用相同的底层检查点和输入配置。基线采用未量化的 BF16 PyTorch 执行，并使用检查点默认的注意力核函数。基线版本按检查点单独选定，以保留其所需的模型行为。

<a id="S2084"></a>
**Source:** p.115 S2084

**Original:** Optimizing the serving path. Multi-camera observations must be encoded, transferred, and prepared before the model can use them. We reduce this overhead with bounded CPU worker pools for camera-history processing, faster JPEG encoding and decoding, and fewer memory copies. Where supported, incremental streaming VAE reuses cached encoder state as camera frames arrive. VAE prefetch prepares the required visual latents before the next prediction request, moving encoding off the foreground prediction path. The benefit depends on the observation format, client implementation, and hardware. Deployment-level evaluation must also account for the age of the observations and the encoding work performed before the request.

**中文:** 优化服务路径。多相机观测必须先经过编码、传输和准备，模型才能使用。我们通过以下方式降低这部分开销：为相机历史处理设置有界的 CPU 工作池，采用更快的 JPEG 编解码，并减少内存拷贝。在支持的情况下，增量流式 VAE 会在相机帧到达时复用已缓存的编码器状态。VAE 预取会在下一次预测请求之前准备所需的视觉潜变量，从而将编码工作移出前台预测路径。其收益取决于观测格式、客户端实现和硬件。部署层面的评估还必须考虑观测的时效，以及请求前已完成的编码工作。

<a id="S2085"></a>
**Source:** p.115 S2085

**Original:** Latency and action fidelity. Approximation-based inference acceleration can reduce latency at the cost of task success, our primary measure of robot policy quality. We therefore assess the effects of acceleration through numerical validation, simulation, and physical-robot evaluation. Numerical comparisons use the same checkpoint’s eager BF16 execution as a reference, holding observations, conditioning, denoising schedules, and initial noise fixed. We compute mean squared error over valid, newly generated actions, excluding padding and committed RTC prefixes, and inspect decoded errors by action group. Simulation and physical-robot tests evaluate whether accelerated execution preserves task success, alongside completion time and motion smoothness.

**中文:** 时延与动作保真度。基于近似的推理加速可以降低时延，但可能以任务成功率为代价，而任务成功率是我们衡量机器人策略质量的主要指标。因此，我们通过数值验证、仿真和实体机器人评估来考察加速的效果。数值比较以同一检查点的即时 BF16 执行作为参考，并固定观测、条件、去噪调度和初始噪声。我们计算有效的新生成动作上的均方误差，排除填充部分和已确定的 RTC 前缀，并按动作分组检查解码后的误差。仿真与实体机器人测试则评估加速执行是否保持任务成功率，同时考察完成时间与运动平滑性。

<a id="S2086"></a>
**Source:** p.115 S2086

**Original:** During the remaining prediction delay, the robot must continue executing actions. The following subsection describes how training-time RTC conditions new predictions on actions already committed for execution, supporting continuity between action chunks.

**中文:** 在剩余的预测延迟期间，机器人必须继续执行动作。下一小节说明训练时 RTC 如何将新的预测条件化于已确定用于执行的动作之上，从而支持动作块之间的连续性。
