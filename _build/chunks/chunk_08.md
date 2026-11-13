### 4.6. Deployment and Real-Time Inference ｜ 4.6. 部署与实时推理

<a id="S417"></a>
**Source:** p.22 S417

**Original:** Deployment requires timely predictions, continuous motion, and efficient task completion, both on workstation GPUs and on edge hardware with limited compute, memory, and power. Compared with VLA policies, these requirements are more difficult to meet for a world-action model: GR00T 2 encodes multi-camera video and

**中文:** 部署需要及时的预测、连续的运动以及高效的任务完成，无论是在工作站 GPU 上，还是在算力、内存与功耗都有限的边缘硬件上。与 VLA 策略相比，这些要求对世界-动作模型而言更难满足：GR00T 2 对多相机视频和

![F019](assets/F019.png)

<a id="C020"></a>
**Source:** p.23 C020 · 图 F019

**Original (caption):** Figure 19: Model-prediction latency for GR00T 2 Turbo on G1 using (a) a GeForce RTX 5090 and (b) Jetson Thor in 120 W mode. Bars show medians of 500 predictions after 20 warmup requests, using the same checkpoint weights and input observations. The panels use independent horizontal scales. Denoising-step tuning changes 2v4a to 1v2a.

**中文（图注）：** 图 19：GR00T 2 Turbo 在 G1 上的模型预测时延，分别使用 (a) GeForce RTX 5090 和 (b) 处于 120 W 模式的 Jetson Thor。柱状图为 500 次预测的中位数，预测前先进行 20 次预热请求，所用检查点权重与输入观测相同。两个子图使用各自独立的水平刻度。去噪步数调优会将 2v4a 改为 1v2a。

<a id="S440"></a>
**Source:** p.23 S440

**Original:** iteratively denoises video and action latents, and in our setting it incurs higher inference latency. We address them with accelerated inference (Sec. 4.6.1), training-time real-time chunking for smooth execution under the remaining delay (Sec. 4.6.2), and phase-conditioned action chunk transforms that enables faster than demonstration task completion throughput (Sec. 4.6.3).

**中文:** 迭代地对视频与动作潜变量进行去噪，在我们的设定中，这会带来更高的推理时延。我们通过加速推理（Sec. 4.6.1）、在剩余时延下实现平滑执行的训练时实时分块（Sec. 4.6.2），以及能够实现快于演示的任务完成吞吐量的阶段条件化动作块变换（Sec. 4.6.3）来应对这些问题。

<a id="S441"></a>
**Source:** p.23 S441

**Original:** 4.6.1. Policy Serving and Accelerated Inference

**中文:** 4.6.1. 策略服务与加速推理

<a id="S442"></a>
**Source:** p.23 S442

**Original:** GR00T 2 is served through a client-server interface: a robot client sends the camera history, robot state, and instruction, and the server returns an action chunk, which the client buffers and executes at the controller’s rate while it requests the next one (Sec. K.5). The server first removes repeated computation. It reuses the text features while the instruction is unchanged, precomputes the timestep conditioning, and lets action-only denoising steps reuse the attention keys and values of the latest video step. It then compiles the video encoder and the transformer into TensorRT engines replayed with CUDA graphs, for supported checkpoints applies FP8 to selected projection and feed-forward layers after calibration on robot observations, and reduces the number of denoising steps where task success and smoothness allow. On the serving path, streaming and prefetching move video encoding ahead of the prediction request. For GR00T 2 Turbo on the G1, TensorRT compilation gives the largest single reduction on both GPUs (Fig. 19). Together, these optimizations reduce median prediction latency by 2.9× to 7.2× relative to eager BF16 execution of the same checkpoint (Tab. 27). On a DGX Station GB300, GR00T 2 predicts in 48 ms on Dexter and 54 ms on YAM, with video encoding prefetched. For the Unitree G1, GR00T 2 Turbo predicts in 38 ms on a GeForce RTX 5090 and in 124 ms on the robot’s onboard Jetson Thor, where it plans 1.6 s chunks of whole-body motion tokens about once per second for the SONIC controller to execute at 50 Hz (Fig. 9). Numerical comparisons with eager BF16 execution help identify changes in predicted actions, but prediction error alone does not establish task success in closed-loop control. We make deployment decisions to screen inference changes and make deployment decisions through evaluation on the physical robot, considering task success, completion time, and motion quality together (Sec. I.1).

**中文:** GR00T 2 通过客户端-服务器接口提供服务：机器人客户端发送相机历史、机器人状态和指令，服务器返回一个动作块，客户端将其缓存并以控制器的频率执行，同时请求下一个动作块（Sec. K.5）。服务器首先消除重复计算：指令不变时复用文本特征，预先计算时间步条件，并让仅动作的去噪步复用最新视频步的注意力 key 与 value。随后，它将视频编码器和 Transformer 编译为 TensorRT 引擎，并通过 CUDA graph 回放；对于支持的检查点，在使用机器人观测完成校准后，对选定的投影层和前馈层应用 FP8；并在任务成功率与运动平滑性允许的情况下减少去噪步数。在服务路径上，流式传输与预取会把视频编码提前到预测请求之前完成。对于 G1 上的 GR00T 2 Turbo，TensorRT 编译在两种 GPU 上都带来了最大的单项降幅（图 19）。综合这些优化，相较于同一检查点的 eager BF16 执行，中位预测时延降低了 2.9× 至 7.2×（表 27）。在 DGX Station GB300 上，GR00T 2 在 Dexter 上的预测耗时为 48 ms，在 YAM 上为 54 ms（视频编码已预取）。对于 Unitree G1，GR00T 2 Turbo 在 GeForce RTX 5090 上的预测耗时为 38 ms，在机器人自带的 Jetson Thor 上为 124 ms；后者约每秒规划一次 1.6 s 的全身运动 token 块，由 SONIC 控制器以 50 Hz 执行（图 9）。与 eager BF16 执行的数值比较有助于识别预测动作的变化，但在闭环控制中，仅凭预测误差无法证明任务成功。我们借助数值比较来筛查推理变更，并通过实体机器人上的评测做出部署决策，同时综合考虑任务成功率、完成时间与运动质量（Sec. I.1）。

<a id="S443"></a>
**Source:** p.23 S443

**Original:** 4.6.2. Smooth Execution with Real-Time Chunking

**中文:** 4.6.2. 借助实时分块实现平滑执行

<a id="S444"></a>
**Source:** p.23 S444

**Original:** Some delay remains after acceleration, and the robot must keep moving while the next chunk is computed. Waiting for each prediction interrupts the motion, and executing predictions asynchronously without accounting for the delay creates discontinuities between successive chunks. Training-time real-time chunking (RTC) (Black et al., 2025) conditions each prediction on the prefix of actions already committed for execution. In our setting, conditioning on a clean prefix improves continuity but lowers task success at the shorter delay. We therefore use noisy-prefix RTC: during fine-tuning, the conditioning prefix is perturbed with Gaussian noise, which is intended to reduce reliance on the previous plan while retaining the context needed for a smooth continuation,

**中文:** 加速之后仍存在一定时延，而机器人必须在计算下一个动作块的同时持续运动。等待每次预测会打断运动，而在不考虑时延的情况下异步执行预测，则会使相邻动作块之间出现不连续。训练时实时分块（RTC）（Black et al., 2025）让每次预测以已确定用于执行的动作前缀为条件。在我们的设定中，以干净前缀为条件可以改善连续性，但在较短时延下会降低任务成功率。因此，我们采用带噪前缀实时分块（noisy-prefix RTC）：在微调期间，条件前缀被施加高斯噪声扰动，目的是在保留平滑衔接所需上下文的同时，降低对先前规划的依赖，

![F020](assets/F020.png)

<a id="C021"></a>
**Source:** p.24 C021 · 图 F020

**Original (caption):** Figure 20: Phase-conditioned task-completion throughput acceleration of GR00T 2. GR00T 2 predicts a future action chunk, while a subtask predictor identifies its task phases. Using a phase-specific speed schedule, we transform the original action chunk to accelerate execution and boost task-completion throughput while preserving success rates.

**中文（图注）：** 图 20：GR00T 2 的阶段条件化任务完成吞吐量加速。GR00T 2 预测未来的一个动作块，同时子任务预测器识别其所处的任务阶段。借助阶段特定的速度调度，我们对原始动作块进行变换，在保持成功率的同时加快执行并提升任务完成吞吐量。

<a id="S456"></a>
**Source:** p.24 S456

**Original:** and at inference the policy conditions on the clean committed actions. A short fine-tuning stage of 5k steps on a post-trained policy captures most of the continuity benefit, so RTC does not require repeating the full training pipeline. On eight RoboDojo precision tasks with simulated inference delays, noisy-prefix RTC raises success over asynchronous execution of the same weights from 32.8% to 34.8% at a 160 ms delay and from 15.0% to 21.4% at 320 ms. It reduces peak commanded jerk by 69% at 160 ms and the 95th-percentile cross-chunk jerk by 87% at 320 ms, whereas clean-prefix RTC lowers success at 160 ms to 30.7% (Sec. I.2).

**中文:** 而在推理时，策略以干净的已提交动作为条件。在经过后训练的策略上进行 5k 步的短程微调，即可获得大部分连续性收益，因此 RTC 无需重复完整的训练流程。在八个带模拟推理时延的 RoboDojo 精细任务上，相较于使用同一权重的异步执行，带噪前缀 RTC 将 160 ms 时延下的成功率从 32.8% 提升至 34.8%，将 320 ms 时延下的成功率从 15.0% 提升至 21.4%。在 160 ms 时延下，它使峰值指令加加速度（jerk）降低 69%；在 320 ms 时延下，它使跨块加加速度的第 95 百分位数降低 87%。相比之下，干净前缀 RTC 在 160 ms 时延下的成功率降至 30.7%（Sec. I.2）。

<a id="S457"></a>
**Source:** p.24 S457

**Original:** 4.6.3. Accelerating Task Throughput Beyond Demonstrations

**中文:** 4.6.3. 超越演示的任务吞吐量加速

<a id="S458"></a>
**Source:** p.24 S458

**Original:** Continuous execution and low latency do not by themselves boost task completion throughput, which remains bound to the pace of the demonstrations. We therefore retime GR00T 2’s action chunks by task phase. A task is decomposed into semantically meaningful phases, such as reaching, grasping, transporting, and screwing, which tolerate different degrees of acceleration. An agent searches for a per-phase speed schedule by evaluating accelerated rollouts and refining the schedule after observed failures. At deployment, a lightweight subtask predictor, trained on phase annotations generated by an agent, predicts from the current observation the phases spanned by each action chunk, and the chunk is retimed according to the schedule (Fig. 20). Because retiming changes the timing between successive chunks, temporal chunk alignment and cross-chunk jerk smoothing keep the execution continuous (Sec. I.3).

**中文:** 连续执行与低时延本身并不能提升任务完成吞吐量，后者仍受限于演示的节奏。因此，我们按任务阶段对 GR00T 2 的动作块进行时间重标定。任务被分解为若干语义上有意义的阶段，例如接近、抓取、搬运和拧螺丝，这些阶段能够容忍不同程度的加速。智能体通过评估加速后的 rollout（轨迹采样），并在观察到失败后细化调度，为每个阶段搜索逐阶段的速度调度。部署时，一个轻量级子任务预测器根据当前观测预测每个动作块所覆盖的阶段；该预测器基于由智能体生成的阶段标注训练。随后，动作块按照调度进行重标定（图 20）。由于重标定会改变相邻块之间的时间关系，时间块对齐与跨块加加速度平滑可以保证执行的连续性（Sec. I.3）。

### 4.7. Infrastructure ｜ 4.7. 基础设施

<a id="S459"></a>
**Source:** p.24 S459

**Original:** Training GR00T 2 runs a joint video-action model over multi-camera video from human, UMI, and robot sources. Its infrastructure must provide the memory and compute for this model at scale, deliver decoded video windows to every GPU without stalling synchronous training, and turn raw recordings into training-ready data at the scale of the pretraining corpus. We describe the pretraining compute and distributed training runtime (Sec. 4.7.1), the training data loader (Sec. 4.7.2), and the multimodal data processing pipeline (Sec. 4.7.3).

**中文:** GR00T 2 的训练运行一个联合视频-动作模型，其输入来自人类、UMI 与机器人等多个来源的多相机视频。其基础设施必须为这一规模的模型提供所需的内存与算力，将解码后的视频窗口送达每个 GPU 而不阻塞同步训练，并将原始录制数据转换为可直接用于训练的数据，且规模要与预训练语料相当。我们依次介绍预训练算力与分布式训练运行时（Sec. 4.7.1）、训练数据加载器（Sec. 4.7.2）以及多模态数据处理流水线（Sec. 4.7.3）。

<a id="S460"></a>
**Source:** p.24 S460

**Original:** Policy serving is described with deployment (Sec. 4.6.1), and the online RL infrastructure with RL post-training (Sec. 4.1).

**中文:** 策略服务在部署部分中说明（Sec. 4.6.1），在线 RL 基础设施则在 RL 后训练部分中说明（Sec. 4.1）。

<a id="S461"></a>
**Source:** p.24 S461

**Original:** 4.7.1. Pretraining Compute and Distributed Training

**中文:** 4.7.1. 预训练算力与分布式训练

<a id="S462"></a>
**Source:** p.24 S462

**Original:** GR00T 2 is pretrained on NVIDIA GB300 NVL72 systems, chosen for GPU memory capacity, Tensor Core throughput, and acceleration of collective communication. Each Blackwell Ultra GPU provides up to 288 GB of HBM3e with 8 TB/s of bandwidth and about 2.5 PFLOPS of dense BF16/FP16 Tensor Core compute. A rack connects 72 GPUs into one NVLink domain with 1.8 TB/s of bidirectional bandwidth per GPU, in which NVLink SHARP offloads reductions to the switches, and racks communicate over a RoCE fabric with one 800 Gb/s ConnectX-8 SuperNIC per GPU. The cluster has 2,016 GPUs in 28 racks, and the main pretraining run used 1,024 of them, while the rest ran other training experiments concurrently (Sec. K.2.1).

**中文:** GR00T 2 在 NVIDIA GB300 NVL72 系统上进行预训练，选择该平台是因为其 GPU 显存容量、Tensor Core 吞吐量以及对集合通信的加速能力。每块 Blackwell Ultra GPU 提供最高 288 GB 的 HBM3e 显存，带宽为 8 TB/s，并具有约 2.5 PFLOPS 的稠密 BF16/FP16 Tensor Core 算力。一个机架将 72 块 GPU 连接为一个 NVLink 域，每块 GPU 的双向带宽为 1.8 TB/s，其中 NVLink SHARP 将归约操作卸载到交换机上；机架之间则通过 RoCE 网络互连，每块 GPU 配备一块 800 Gb/s 的 ConnectX-8 SuperNIC。集群共有 2,016 块 GPU，分布在 28 个机架中，主预训练运行使用其中 1,024 块，其余 GPU 同时运行其他训练实验（Sec. K.2.1）。

<a id="S463"></a>
**Source:** p.25 S463

**Original:** Training uses synchronous data parallelism with DeepSpeed ZeRO-2: every GPU holds the full weights, gradients and optimizer state are partitioned across ranks, and BF16 gradient synchronization overlaps with computation. Because the model fits without pipeline parallelism, the GPU memory keeps the parameters, each rank’s optimizer partition, and the activations of a per-device batch of 16 resident, and the large per-device batch gives the Tensor Cores more matrix-multiplication work and amortizes kernel-launch overhead. Part of each step runs in frozen feature encoders rather than the trainable model. Depending on the recipe, the runtime uses TensorRT for video encoding, fused text-encoder operations, efficient attention kernels that keep the model’s masking rules, PyTorch compilation, and activation recomputation, and it can encode the next batch’s features while the current batch synchronizes gradients and updates the optimizer. We judge efficiency across the whole step, from input retrieval and feature encoding to gradient synchronization and the optimizer update. A hardware-counter-based utilization metric, Overall FLOP Utilization (Pedersen et al., 2026), is monitored alongside step time, but elapsed time and model quality decide whether a change is kept, since an optimization can shorten the step without moving the utilization signal (Sec. K.4).

**中文:** 训练采用同步数据并行与 DeepSpeed ZeRO-2：每块 GPU 持有完整权重，梯度与优化器状态在各 rank 之间分片，BF16 梯度同步与计算重叠进行。由于模型无需流水线并行即可装下，GPU 显存中常驻的内容包括参数、每个 rank 的优化器分片，以及每设备批量为 16 的激活值。这种较大的每设备批量能为 Tensor Core 提供更多矩阵乘法工作，并摊销内核启动开销。每一步的一部分计算在冻结的特征编码器中完成，而非在可训练模型中进行。根据训练配方的不同，运行时会使用 TensorRT 进行视频编码、融合文本编码器运算、保留模型掩码规则的高效注意力内核、PyTorch 编译以及激活重计算，并且可以在当前批次同步梯度、更新优化器的同时，对下一批次的特征进行编码。我们从整体上衡量每一步的效率，涵盖从输入读取、特征编码到梯度同步和优化器更新的全过程。我们同时监控一个基于硬件计数器的利用率指标，即整体 FLOP 利用率（Overall FLOP Utilization）（Pedersen et al., 2026），并与单步耗时一同观察；但是否保留某项改动，取决于实际耗时与模型质量，因为一项优化可能缩短单步耗时，却不会改变该利用率信号（Sec. K.4）。

<a id="S464"></a>
**Source:** p.25 S464

**Original:** 4.7.2. Training Data Loading

**中文:** 4.7.2. 训练数据加载

<a id="S465"></a>
**Source:** p.25 S465

**Original:** Training data are stored in LanceDS, built on the Lance columnar format (Pace et al., 2025; Lance Contributors, 2026). Each dataset holds a step table with state, actions, annotations, and quality-control (QC) signals, an episode table, and a media table with the original videos. Lance versioning preserves earlier snapshots when episodes are added or annotations and QC signals change, and new QC columns are added without rewriting existing ones. A training run pins one snapshot per dataset, so its data, normalization statistics, and metadata are reproduced together. All datasets share one schema, and the recipe’s embodiment tag selects at read time the state and action groups, cameras, annotations, and normalization statistics of that embodiment, as well as the model’s embodiment-specific projection layers. QC rules are not applied in the loading path: they are evaluated offline over the temporal window that each training sample reads, its observations and its action targets, and stored as views of the eligible sample starts. The views are rebuilt with every new snapshot and carry normalization statistics computed over the samples they keep. Sampling is drawn on demand from deterministic per-rank seeds and mixes shards so that each global step follows the recipe’s dataset proportions. Batch preparation runs in three asynchronous stages: video shards are prefetched from shared storage to node-local NVMe, frames are decoded (about 90% of preparation time in a three-view shard benchmark), and samples are augmented, collated, and copied to the GPU from pinned memory. Variable-length token packing reduces padding. Over 100 steady-state pretraining steps on 1,024 GB300 GPUs, reading 25 dataset stores with 15.6 million episode records and 46.2 billion time steps, the loader delivered about 12,000 sample windows per second, and the mean exposed wait for input was 0.37 ms (0.61 ms at the 99th percentile), or 0.049% of the measured step time (Tab. 35). These numbers characterize input delivery, not the model’s FLOP utilization. In the measured run, packing filled 94.5% of the positions in 32,768-token rows. Loader changes are validated in closed-loop simulation before adoption (Sec. 4.5.2), and Sec. K.4.3 details the loader.

**中文:** 训练数据存储在 LanceDS 中，它构建于 Lance 列式格式之上（Pace et al., 2025；Lance Contributors, 2026）。每个数据集包含一张 step 表（记录状态、动作、标注以及质量控制（QC）信号）、一张 episode 表，以及一张保存原始视频的 media 表。当新增 episode，或标注与 QC 信号发生变化时，Lance 版本管理会保留更早的快照；新增的 QC 列无需重写已有列。一次训练运行会为每个数据集固定一个快照，因此其数据、归一化统计量与元数据能够被一并复现。所有数据集共享同一套 schema，配方中的本体标签（embodiment tag）会在读取时选定该本体对应的状态与动作组、相机、标注和归一化统计量，以及模型中特定于本体的投影层。QC 规则不在加载路径中应用：它们以离线方式在每个训练样本所读取的时间窗口（即其观测与动作目标）上评估，并存储为合格样本起点的视图。每当生成新快照时，这些视图都会被重建，并携带基于其所保留样本计算的归一化统计量。采样按需从确定性的逐 rank 随机种子中抽取，并混合各分片，使每个全局步都遵循配方规定的数据集比例。批次准备分为三个异步阶段：视频分片从共享存储预取到节点本地 NVMe，帧被解码（在三视角分片基准测试中，解码约占准备时间的 90%），样本经过数据增广、整理（collate）后，从锁页内存复制到 GPU。变长 token 打包减少了填充。在 1,024 块 GB300 GPU 上进行的 100 个稳态预训练步中，加载器读取了 25 个数据集存储，共包含 1,560 万条 episode 记录和 462 亿个时间步，平均每秒交付约 12,000 个样本窗口；输入等待的平均暴露时间为 0.37 ms（第 99 百分位为 0.61 ms），占实测单步耗时的 0.049%（Tab. 35）。这些数字刻画的是输入交付的情况，而非模型的 FLOP 利用率。在实测运行中，打包使 32,768 token 行中 94.5% 的位置被填充。加载器的改动会先经闭环仿真验证再被采用（Sec. 4.5.2），Sec. K.4.3 则详细介绍了加载器。

<a id="S466"></a>
**Source:** p.25 S466

**Original:** 4.7.3. Multi-Modal Data Processing

**中文:** 4.7.3. 多模态数据处理

<a id="S467"></a>
**Source:** p.25 S467

**Original:** Before they can be loaded, raw human demonstration recordings are converted into training-ready data. Multi-camera video is retrieved, decoded, and resized. Motion records are transformed and, where needed, retargeted to the training hand representation. Observations, actions, and annotations are then aligned in time and packaged as indexed episodes in training-ready shards. The pipeline processes petabyte-scale input each month, with individual production jobs using nearly 10,000 vCPUs. The central difficulty is that these conversions share inputs and compete for limited working storage. A long video can contain many episodes, and one episode can depend on several camera files and separately stored motion records, so a shared input can be reclaimed only after its slowest consumer finishes, and a slow conversion or upload can block the retrieval of unrelated inputs and leave workers idle. The pipeline therefore ties the lifetime of each input to execution progress. Files stream from object storage directly to the processing nodes, without staging on a shared filesystem, so conversion starts before a collection has been fully retrieved. New inputs are admitted against each node’s storage budget, counting resident files, pending transfers, and output headroom, and work is dispatched to the node that holds its inputs. An episode releases its claim on an input only after its outputs are uploaded, so the completion of consumers, rather than prefetching, governs when new inputs enter. After an interruption, lost inputs are rebuilt through the same admission path, and durable checkpoints let the resumed job reuse completed conversions and published shards. In three production jobs on 100 nodes with 96 vCPUs each, the pipeline processed 722 to 780 demonstration-hours of recordings per hour, published the first training-ready shard within 28 minutes, and averaged 97.8% CPU utilization during conversion. Across five interrupted jobs, 92.4% of the completed conversion time went to work that did not have to be repeated, and publication resumed 2.4 to 5.3 minutes after a restart (Sec. K.6 and Tab. 36).

**中文:** 原始人类演示录制数据需先转换为可用于训练的数据，才能被加载。多相机视频被读取、解码并缩放。运动记录被变换，并在需要时重定向到训练所用的手部表示。随后，观测、动作与标注在时间上对齐，并作为带索引的 episode 打包成训练就绪的分片。该流水线每月处理 PB 级输入，单个生产作业使用接近 10,000 个 vCPU。核心难点在于，这些转换会共享输入，并争用有限的工作存储。一段长视频可能包含许多 episode，而一个 episode 可能依赖多个相机文件以及单独存储的运动记录，因此共享输入只有在其最慢的消费者完成后才能被回收；转换或上传缓慢还会阻塞无关输入的读取，使工作节点空转。为此，该流水线将每个输入的生命周期与执行进度绑定。文件直接从对象存储流式传输到处理节点，无需在共享文件系统上暂存，因此转换可以在一次采集完全读取之前就开始。新输入的准入需对照每个节点的存储预算进行判断，预算计入常驻文件、待处理传输以及输出余量；工作则被分派到持有其输入的节点。一个 episode 只有在其输出上传完成后才释放对某个输入的占用，因此新输入何时进入，取决于消费者的完成情况，而非预取。中断之后，丢失的输入会通过同一准入路径重新构建；持久化检查点则让恢复后的作业能够复用已完成的转换与已发布的分片。在 100 个节点（每节点 96 个 vCPU）上的三个生产作业中，该流水线每小时处理 722 至 780 个演示小时的录制数据，在 28 分钟内发布了第一个训练就绪分片，转换期间的 CPU 平均利用率为 97.8%。在五次中断的作业中，已完成的转换时间中有 92.4% 用于不必重复的工作，重启后发布恢复耗时 2.4 至 5.3 分钟（Sec. K.6 与 Tab. 36）。
