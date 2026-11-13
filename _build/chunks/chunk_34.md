### K.4. Distributed Training ｜ 分布式训练

<a id="S2270"></a>
**Source:** p.129 S2270

**Original:** Distributed training of GR00T 2 requires coordinating multimodal input preparation with synchronous model updates. We design the runtime to reduce memory use, limit waiting between training stages, and preserve progress across interruptions.

**中文:** GR00T 2 的分布式训练需要让多模态输入准备与同步的模型更新相互协调。我们设计该运行时，以降低内存占用、限制各训练阶段之间的等待时间，并在训练中断后保留训练进度。

<a id="S2271"></a>
**Source:** p.129 S2271

**Original:** K.4.1. Parallelism and Memory Management

**中文:** K.4.1. 并行与内存管理

<a id="S2272"></a>
**Source:** p.129 S2272

**Original:** We use synchronous data parallelism with DeepSpeed ZeRO-2. Model weights are replicated on each GPU, while gradients and optimizer state are partitioned across ranks to reduce per-device memory use. BF16 gradient synchronization overlaps with model computation to reduce exposed communication time.

**中文:** 我们使用同步的数据并行（data parallelism）并结合 DeepSpeed ZeRO-2。模型权重在每块 GPU 上各保存一份副本，而梯度和优化器状态则在各 rank（分布式进程）之间切分，以降低单设备的内存占用。BF16 梯度同步与模型计算重叠进行，以减少暴露在外的通信时间。

<a id="S2273"></a>
**Source:** p.129 S2273

**Original:** K.4.2. Efficient Multimodal Computation

**中文:** K.4.2. 高效的多模态计算

<a id="S2274"></a>
**Source:** p.129 S2274

**Original:** Multimodal training requires computation in both frozen feature encoders and the trainable model. Depending on the recipe, the runtime supports TensorRT video encoding, fused text-encoder operations, efficient attention kernels, and PyTorch compilation.

**中文:** 多模态训练既需要在冻结的特征编码器中进行计算，也需要在可训练模型中进行计算。根据训练配方的不同，运行时支持 TensorRT 视频编码、融合的文本编码器算子、高效的注意力算子（kernel），以及 PyTorch 编译。

<a id="S2275"></a>
**Source:** p.129 S2275

**Original:** Activation recomputation reduces memory use at the cost of additional computation. Attention optimizations

**中文:** 激活重计算以额外计算为代价降低内存占用。注意力优化 [存疑：原文抽取在此截断]

![F068](assets/F068.png)

<a id="C102"></a>
**Source:** p.130 C102 · 图 F068

**Original (caption):** Figure 68: Data delivery during multi-view pretraining on 1,024 NVIDIA GB300 GPUs over 100 consecutive steadystate steps. (a) Delivered sample-window throughput. (b) Exposed batch-retrieval wait, showing the mean and maximum across ranks.

**中文（图注）：** 图 68：在 1,024 块 NVIDIA GB300 GPU 上、连续 100 个稳态步内的多视角预训练数据交付情况。(a) 已交付的样本窗口吞吐量。(b) 暴露的批次取回等待时间，显示各 rank 上的均值与最大值。

<a id="S2279"></a>
**Source:** p.130 S2279

**Original:** GR00T 2’s data loader combines versioned multimodal storage, offline quality filtering, and asynchronous batch preparation. Training recipes specify the data snapshots to read and how samples are selected and interpreted across embodiments. The training mixture used for the measurements below comprises 25 versioned dataset stores, totaling 15.6 million episode records and 46.2 billion recorded time steps before applying the run’s sampling views. These totals aggregate the selected stores without deduplicating recording content across stores.

**中文:** GR00T 2 的数据加载器结合了带版本的多模态存储、离线质量过滤和异步批次准备。训练配方规定了要读取的数据快照，以及样本如何在不同本体（embodiment）之间被选取和解释。下文测量所用的训练混合数据由 25 个带版本的数据集存储组成，在应用本次运行的采样视图之前，共计 1560 万条片段（episode）记录和 462 亿个记录的时间步。这些总数是对所选存储的汇总，未对各存储之间的记录内容去重。

<a id="S2280"></a>
**Source:** p.130 S2280

**Original:** Versioned storage and schema. We store training data in LanceDS, built on the Lance columnar format (Pace et al., 2025; Lance Contributors, 2026). Each dataset contains a step table for state, action, annotations, and quality-control (QC) signals, an episode table, and a media table holding the original videos. Lance’s versioning preserves earlier snapshots when episodes are added or annotations or QC signals change, and new QC columns can be added without rewriting existing columns. A per-dataset commit record ties each snapshot’s table versions to its normalization statistics and metadata. A training run pins one snapshot per dataset, so data, statistics, and metadata are reproduced together. Snapshots are replicated to the object store and to training clusters in commit order, with the commit record copied last, so a replica serves a pinned snapshot completely or not at all.

**中文:** 版本化存储与模式（schema）。我们将训练数据存储在 LanceDS 中，它构建于 Lance 列式格式之上（Pace et al., 2025; Lance Contributors, 2026）。每个数据集包含一张用于存放状态、动作、标注和质量控制（QC）信号的步表（step table）、一张片段表（episode table），以及一张存放原始视频的媒体表（media table）。当新增片段，或标注、QC 信号发生变化时，Lance 的版本机制会保留较早的快照；新的 QC 列可以直接添加，无需重写已有列。每个数据集的提交记录（commit record）将每个快照的表版本与其归一化统计量和元数据关联起来。一次训练运行会为每个数据集固定一个快照，因此数据、统计量和元数据能够被一并复现。快照按提交顺序复制到对象存储和训练集群，提交记录最后复制，因此副本要么完整地提供固定的快照，要么完全不提供。

<a id="S2281"></a>
**Source:** p.130 S2281

**Original:** Datasets share a schema in which state and action groups are packed into one state column and one action column. Group names and offsets are recorded in schema metadata, allowing the loader to select fields by name despite differences in their stored order. At read time, the recipe’s embodiment tag selects groups, cameras, annotations, normalization statistics pooled across datasets of that embodiment, and, for dexterous hands, fingertip force signals and deformation video. The same tag determines the model’s embodiment-specific projection layers. Datasets of the same embodiment can be merged with a common group order.

**中文:** 各数据集共享同一模式：状态组和动作组分别打包进一个状态列和一个动作列。组名和偏移量记录在模式元数据中，使加载器即便字段在存储中的顺序不同，仍能按名称选取字段。读取时，配方中的本体标签会选定组、相机、标注，以及在该本体所有数据集上汇总的归一化统计量；对于灵巧手，还会选定指尖力信号和形变视频。同一标签还决定了模型中本体相关的投影层。同一本体的数据集可以按统一的组顺序合并。

<a id="S2282"></a>
**Source:** p.130 S2282

**Original:** Steps within each episode are stored contiguously, and the loader fetches episode ranges through batched reads. Step-table reads bypass filesystem readahead, which amplified per-shard step-table I/O by 28× to 60× in an earlier production benchmark.

**中文:** 每个片段内的步按连续方式存储，加载器通过批量读取获取片段范围。步表读取会绕过文件系统的预读（readahead），在早前的一次生产基准测试中，预读使每个分片的步表 I/O 放大了 28× 至 60×。

<a id="S2283"></a>
**Source:** p.131 S2283

**Original:** Window-aware QC views. A view records the steps eligible to serve as training-sample starts. User-defined Python filters evaluate an episode’s columns over the temporal window consumed by each sample, so eligibility accounts for the observations and action targets that training will read. Filters can also select whole episodes by metadata such as task family, collection date, or data origin. Views are computed offline and stored as runs of consecutive eligible steps per episode. Training samples directly from these runs without evaluating the filters in the loading path.

**中文:** 感知窗口的 QC 视图（view）。一个视图记录可以作为训练样本起点的步。用户自定义的 Python 过滤器会在每个样本所消耗的时间窗口上计算片段的各列，因此资格判定会考虑训练将读取的观测和动作目标。过滤器还可以依据任务族、采集日期或数据来源等元数据，选取整段片段。视图离线计算，并以每个片段内连续合格步的游程形式存储。训练直接从这些游程中采样，加载路径中不再计算过滤器。

<a id="S2284"></a>
**Source:** p.131 S2284

**Original:** Each view is identified by a hash of the dataset, filter code and arguments, and sample window. Cosmetic edits to a filter keep its hash. Views are tagged with the table versions they serve and can be shared by identifier across runs. A view is reused at a new version when the dataset’s rows and the columns its filters read are unchanged. Views are rebuilt automatically: each new snapshot triggers a build of every registered view in the same job that writes the snapshot, and the snapshot and its views are published together, so recipes can pin new snapshots without a manual build step.

**中文:** 每个视图由数据集、过滤器代码及参数和样本窗口的哈希值共同标识。对过滤器的外观性修改不会改变其哈希值。视图会标注其所服务的表版本，并可在不同运行之间通过标识符共享。当数据集的行以及过滤器所读取的列均未变化时，视图可在新版本下复用。视图会自动重建：每个新快照都会在写入该快照的同一作业中触发所有已注册视图的构建，快照与其视图同时发布，因此配方无需手动构建步骤即可固定到新快照。

<a id="S2285"></a>
**Source:** p.131 S2285

**Original:** Views also carry normalization statistics (mean, standard deviation, minimum, maximum, and 1st and 99th percentiles) computed over the samples they keep. Each statistics entry is keyed to the training configuration it was computed under: the snapshot, embodiment, action horizon, and which actions are trained relative to state.

**中文:** 视图还携带归一化统计量（均值、标准差、最小值、最大值，以及第 1 和第 99 百分位数），这些统计量基于视图所保留的样本计算。每条统计量记录都与其计算时所处的训练配置相关联：快照、本体、动作时域，以及哪些动作是相对于状态进行训练的。

<a id="S2286"></a>
**Source:** p.131 S2286

**Original:** For human demonstrations, QC filters check head and wrist motion, hand-pose plausibility, and keypoint visibility, excluding tracking failures such as frozen head poses and abrupt fingertip jumps. For robot demonstrations, filters exclude task-irrelevant motion, idle time, and annotated mistakes or failures. Storing these signals as step-table columns allows curation rules to evolve alongside the versioned dataset.

**中文:** 对于人类演示，QC 过滤器会检查头部和腕部运动、手部姿态的合理性以及关键点可见性，并剔除跟踪失效的片段，例如头部姿态冻结和指尖突然跳变。对于机器人演示，过滤器会剔除与任务无关的运动、空闲时间，以及已标注的错误或失败。将这些信号存储为步表的列，使数据筛选规则能够随带版本的数据集一同演进。

<a id="S2287"></a>
**Source:** p.131 S2287

**Original:** Sampling and batch delivery. Sampling choices are generated on demand from deterministic per-rank step seeds, avoiding a precomputed sampling sequence. Samples are mixed across shards to target the recipe’s dataset proportions in each global step. Sampling without replacement accommodates datasets of different lengths without requiring aligned epoch boundaries.

**中文:** 采样与批次交付。采样选择按需由各 rank 上确定性的步级随机种子生成，无需预先计算采样序列。样本在各分片之间混合，使每个全局步中的数据集比例符合配方的设定。无放回采样可以适应长度不同的数据集，而无需对齐 epoch 边界。

<a id="S2288"></a>
**Source:** p.131 S2288

**Original:** Batch preparation uses three asynchronous stages. The I/O stage prefetches video shards from shared storage into node-local NVMe. The decoding stage reads cached shards, decodes frames, and prepares trajectory metadata. In a representative three-view shard benchmark, decoding was estimated to account for about 90% of preparation time. A separate sequential-decoding microbenchmark measured approximately 7,000 frames/s with one decoding thread at 320×240. The loader stage applies augmentations (random crops retaining 95% of each spatial dimension, resizing to 224×320, and codec augmentation), collates samples, and prepares asynchronous transfers from pinned host memory to the GPU. Keeping prefetched video shards on NVMe reduces the host RAM required for buffering and allows a deeper prefetch window. Dedicated worker pools, SIMD-vectorized decoding, and C++ augmentation implementations reduce CPU processing overhead.

**中文:** 批次准备包含三个异步阶段。I/O 阶段将视频分片从共享存储预取到节点本地 NVMe。解码阶段读取已缓存的分片、解码帧并准备轨迹元数据。在一个具有代表性的三视角分片基准测试中，估计解码约占准备时间的 90%。另有一项单独的顺序解码微基准测试，在 320×240 分辨率、单解码线程下测得约 7,000 帧/秒（frames/s）。加载器阶段应用数据增广（随机裁剪保留每个空间维度的 95%、缩放至 224×320，以及编解码器增广），整理（collate）样本，并准备从锁页主机内存到 GPU 的异步传输。将预取的视频分片保存在 NVMe 上，可以减少缓冲所需的主机内存，并允许更深的预取窗口。专用的 worker 池、SIMD 向量化解码以及 C++ 增广实现，降低了 CPU 处理开销。

<a id="S2289"></a>
**Source:** p.131 S2289

**Original:** On clusters with limited shared-storage capacity, the I/O stage instead stages upcoming shards’ source files on node-local NVMe through a cluster-lifetime object store. Each file is read from the data source once per cluster and forwarded between nodes, so source traffic does not grow with node count. A preloaded interposer serves data-loader reads from local NVMe at the files’ original paths, and a file that cannot be delivered is an error rather than a skipped episode.

**中文:** 在共享存储容量有限的集群上，I/O 阶段改为通过集群生命周期的对象存储，将即将使用的分片源文件预先暂存到节点本地 NVMe 上。每个文件在每个集群中只从数据源读取一次，并在节点之间转发，因此源端流量不会随节点数量增长。预加载的拦截层（interposer）以文件的原始路径，从本地 NVMe 为数据加载器的读取提供服务；无法交付的文件被视为错误，而不是被跳过的片段。

<a id="S2290"></a>
**Source:** p.131 S2290

**Original:** Variable-length token packing reduces padding when samples differ in camera configuration or sequence length. In the measured training run, packed sequences occupied 94.5% of the available positions in 32,768-token rows.

**中文:** 当样本在相机配置或序列长度上有所不同时，变长 token 打包可以减少填充。在实测的训练运行中，打包后的序列占据了 32,768 token 行中 94.5% 的可用位置。

<a id="S2291"></a>
**Source:** p.131 S2291

**Original:** Reproducibility and diagnostics. The loader controls random seeds for sampling and spatiotemporal augmentation. Training checkpoints record loader progress (including active shard offsets, sample indices, and worker state) together with the configuration, including each dataset’s pinned snapshot. The supported sharded pipeline restores sample-sequence progress when resuming with the same data configuration and rank/worker topology. Each sample carries a composite identifier comprising dataset ID, trajectory ID, and frame index, linking the training input to its source.

**中文:** 可复现性与诊断。加载器控制采样和时空增广所用的随机种子。训练检查点会与配置（包括每个数据集所固定的快照）一同记录加载器进度（包括活跃的分片偏移、样本索引和 worker 状态）。在数据配置及 rank/worker 拓扑保持一致的情况下续训时，所支持的分片流水线会恢复样本序列进度。每个样本都带有一个复合标识符，由数据集 ID、轨迹 ID 和帧索引组成，从而将训练输入与其来源相连。

<a id="S2293"></a>
**Source:** p.132 S2293

**Original:** Structured events from each worker and distributed rank trace the batch-loading lifecycle. Correlating these events with sample identifiers helps investigate storage delays, worker starvation, and loss anomalies. A CPU-only benchmark harness uses Gloo and identity model stubs to profile the loading pipeline before GPU runs. Fig. 68 and Tab. 35 report the measured input-delivery performance.

**中文:** 来自每个 worker 和分布式 rank 的结构化事件，记录了批次加载的完整生命周期。将这些事件与样本标识符关联起来，有助于排查存储延迟、worker 饥饿和 loss 异常。一个仅使用 CPU 的基准测试框架，在 GPU 运行之前，使用 Gloo 和恒等模型桩（identity model stub）对加载流水线进行剖析。Fig. 68 和 Tab. 35 报告了实测的输入交付性能。

<a id="S2294"></a>
**Source:** p.132 S2294

**Original:** K.4.4. Straggler Control and Communication

**中文:** K.4.4. 掉队者控制与通信

<a id="S2295"></a>
**Source:** p.132 S2295

**Original:** A rank delayed by input preparation or a CPU pause can hold up collective operations across the training job. We profile CPU activity, GPU execution, and collective timing together to distinguish late-arriving ranks from slow communication.

**中文:** 因输入准备或 CPU 停顿而延迟的 rank（掉队者，straggler），可能会阻塞整个训练作业中的集合通信操作。我们同时剖析 CPU 活动、GPU 执行和集合通信时序，以区分到达较晚的 rank 与通信缓慢。

<a id="S2296"></a>
**Source:** p.132 S2296

**Original:** Depending on the configuration, the runtime coordinates garbage collection, controls CPU thread placement, balances loader concurrency, and reports metrics asynchronously to limit host delays that interrupt GPU work and synchronization.

**中文:** 根据配置不同，运行时会协调垃圾回收、控制 CPU 线程放置、平衡加载器并发度，并异步上报指标，以限制会打断 GPU 工作与同步的主机端延迟。

<a id="S2297"></a>
**Source:** p.132 S2297

**Original:** K.4.5. Checkpointing and Recovery

**中文:** K.4.5. 检查点保存与恢复

<a id="S2298"></a>
**Source:** p.132 S2298

**Original:** Checkpointing coordinates a consistent foreground snapshot of training state, followed by background serialization and writes. Asynchronous saving reduces exposed I/O, and a checkpoint becomes available for continuation once all required writes complete.

**中文:** 检查点保存先协调一个一致的训练状态前台快照，随后进行后台序列化与写入。异步保存减少了暴露的 I/O；所有必需的写入完成后，检查点即可用于续训。

<a id="S2299"></a>
**Source:** p.132 S2299

**Original:** Model artifacts provide weights for evaluation and downstream initialization. Continuation checkpoints additionally retain optimizer partitions, scheduler history, random-number-generator state, and supported loader progress. Restoring training requires compatibility between the saved state and the resumed runtime.

**中文:** 模型产物提供用于评测和下游初始化的权重。续训检查点还额外保存优化器分区、调度器历史、随机数生成器状态以及受支持的加载器进度。恢复训练要求所保存的状态与恢复时的运行时相互兼容。

<a id="S2300"></a>
**Source:** p.132 S2300

**Original:** K.4.6. Training Efficiency

**中文:** K.4.6. 训练效率

<a id="S2301"></a>
**Source:** p.132 S2301

**Original:** We assess training efficiency across input retrieval, frozen feature encoding, model computation, gradient synchronization, and optimizer updates. Step time is interpreted alongside model quality, accounting for differences in active modalities, trainable components, and input shapes.

**中文:** 我们从输入读取、冻结特征编码、模型计算、梯度同步和优化器更新等方面评估训练效率。单步耗时需结合模型质量加以解读，并考虑活跃模态、可训练组件和输入形状的差异。

<a id="S2302"></a>
**Source:** p.132 S2302

**Original:** Tab. 35 reports input-delivery performance over 100 steady-state pretraining steps on 1,024 NVIDIA GB300 GPUs. These measurements characterize the data pipeline. They do not measure whole-model FLOP utilization.

**中文:** Tab. 35 报告了在 1,024 块 NVIDIA GB300 GPU 上、连续 100 个稳态预训练步中的输入交付性能。这些测量刻画的是数据流水线，并不测量整模型的 FLOP 利用率。

![T035](assets/T035.png)

<a id="C103"></a>
**Source:** p.132 C103 · 表 T035

**Original (caption):** Table 35: Measured training-input delivery over 100 steady-state steps on 1,024 NVIDIA GB300 GPUs. The wait-time share is relative to aggregate measured rank-step time.

**中文（表注）：** 表 35：在 1,024 块 NVIDIA GB300 GPU 上、100 个稳态步内实测的训练输入交付情况。等待时间占比相对于实测的 rank 步总耗时计算。

<a id="S2304"></a>
**Source:** p.132 S2304

**Original:** Aggregate sample-window throughput ∼12,000 windows/s Per-GPU sample-window throughput 11.7 windows/s Mean exposed data-loader wait 0.37 ms 99th-percentile exposed data-loader wait 0.61 ms Exposed wait / aggregate measured rank-step time 0.049%

**中文:** 总体样本窗口吞吐量约为 12,000 windows/s；单 GPU 样本窗口吞吐量为 11.7 windows/s；平均暴露的数据加载器等待时间为 0.37 ms；第 99 百分位的暴露数据加载器等待时间为 0.61 ms；暴露等待时间占实测 rank 步总耗时的比例为 0.049%。[存疑：原文为表格的扁平抽取，行列结构已丢失]

<a id="S2305"></a>
**Source:** p.132 S2305

**Original:** We monitor Overall FLOP Utilization (OFU), a hardware-counter-based complement to application-level Model FLOPs Utilization (MFU), alongside step time and task-level evaluation (Pedersen et al., 2026). DCGM provides GPU telemetry (NVIDIA, n.d.e), and Weights & Biases records step time. Utilization helps diagnose accelerator use, while elapsed time and model quality determine whether a change is useful. An optimization can reduce step time without changing the utilization signal. Assessment of a full training run also accounts for startup, compilation, checkpoint pauses, interruptions, and replayed work.

**中文:** 我们监控整体 FLOP 利用率（Overall FLOP Utilization, OFU）。它基于硬件计数器，是应用层模型 FLOP 利用率（MFU）的补充，与单步耗时和任务级评测一并使用（Pedersen et al., 2026）。DCGM 提供 GPU 遥测数据（NVIDIA, n.d.e），Weights & Biases 记录单步耗时。利用率有助于诊断加速器的使用情况，而耗时和模型质量则决定某项改动是否有用。一项优化可能在不改变利用率信号的情况下降低单步耗时。对完整训练运行的评估还需考虑启动、编译、检查点暂停、中断以及重放的工作。
