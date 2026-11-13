### K.5. Inference Infrastructure ｜ 推理基础设施

<a id="S2306"></a>
**Source:** p.132 S2306

**Original:** We use a client-server architecture to deploy GR00T 2 across embodiments and execution backends. The server handles policy inference, while robot clients connect it to embodiment-specific sensing and control.

**中文:** 我们采用客户端-服务器架构，在不同的本体（embodiment）与执行后端上部署 GR00T 2。服务器负责策略推理，机器人客户端则把服务器与各本体特定的感知和控制连接起来。

<a id="S2307"></a>
**Source:** p.133 S2307

**Original:** K.5.1. Policy Serving

**中文:** K.5.1. 策略服务

<a id="S2308"></a>
**Source:** p.133 S2308

**Original:** The robot client sends camera history, robot state, and task instructions through a shared request-reply interface. The server prepares inputs for the loaded model and returns predicted action chunks, which the client maps to the robot’s command format. Checkpoint configuration specifies the required history and embodiment-specific input and action representations. The interface supports PyTorch and optimized runtimes, with client and server running on the same host or separate hosts.

**中文:** 机器人客户端通过共享的请求-应答接口发送相机历史、机器人状态和任务指令。服务器为已加载的模型准备输入，并返回预测的动作块，客户端再将其映射为机器人的指令格式。检查点配置规定了所需的历史信息，以及各本体特定的输入和动作表示。该接口同时支持 PyTorch 与优化运行时，客户端与服务器既可以运行在同一台主机上，也可以分别运行在不同的主机上。

<a id="S2309"></a>
**Source:** p.133 S2309

**Original:** For streaming or prefetched observations, the server verifies that prepared visual inputs match the camera history in the prediction request.

**中文:** 对于流式或预取的观测，服务器会核对已准备好的视觉输入是否与预测请求中的相机历史一致。

<a id="S2310"></a>
**Source:** p.133 S2310

**Original:** K.5.2. Compatibility and Readiness

**中文:** K.5.2. 兼容性与就绪状态

<a id="S2311"></a>
**Source:** p.133 S2311

**Original:** Compiled runtime artifacts are specific to the checkpoint and execution environment. The server checks checkpoint identity, input shapes, numerical precision, software versions, and GPU target before use, rejecting incompatible artifacts. Backends that require warmup initialize execution with a representative observation from the client. Readiness indicates that the required checks and initialization have completed.

**中文:** 编译后的运行时产物与检查点及执行环境相绑定。服务器在使用前会检查检查点身份、输入形状、数值精度、软件版本和 GPU 目标，并拒绝不兼容的产物。需要预热的后端会用客户端提供的一个代表性观测来初始化执行。就绪状态表示所需的检查与初始化均已完成。

<a id="S2312"></a>
**Source:** p.133 S2312

**Original:** On devices with limited GPU memory, the server can offload text-encoder weights to CPU memory, leaving more accelerator memory for policy execution.

**中文:** 在 GPU 显存有限的设备上，服务器可以把文本编码器权重卸载到 CPU 内存中，从而为策略执行留出更多加速器内存。

<a id="S2313"></a>
**Source:** p.133 S2313

**Original:** K.5.3. Action Delivery

**中文:** K.5.3. 动作下发

<a id="S2314"></a>
**Source:** p.133 S2314

**Original:** The client buffers action chunks and schedules commands at the controller’s execution rate. With asynchronous prediction enabled, it requests the next chunk while the controller executes the current one. Clients using timestamped waypoints discard expired targets before sending commands to the controller. Inference acceleration and policy-quality validation are described in Sec. I.1. RTC and action-timing methods are described in Sec. I.2 and I.3.

**中文:** 客户端会缓存动作块，并按控制器的执行频率调度指令。启用异步预测后，客户端会在控制器执行当前动作块的同时请求下一个动作块。使用带时间戳路点的客户端，会在把指令发送给控制器之前丢弃已过期的目标。推理加速与策略质量验证见 Sec. I.1，实时分块（RTC）与动作时序方法见 Sec. I.2 和 Sec. I.3。

### K.6. Scalable Multi-Modal Data Processing ｜ 可扩展的多模态数据处理

<a id="S2315"></a>
**Source:** p.133 S2315

**Original:** Scaling GR00T 2 across tasks and environments requires turning increasingly large and diverse collections of human demonstrations into training-ready data. Our infrastructure processes petabyte-scale monthly input volumes, with individual production jobs using nearly 10,000 vCPUs. At this scale, preparation must sustain both massive data movement and heterogeneous computation: multi-camera video must be retrieved, decoded, and resized. Motion records must be transformed and, where needed, retargeted to the training hand representation, and observations, actions, and annotations must be aligned in time. Recording duration, resolution, encoding, and retargeting requirements vary across sources, so equal numbers of episodes can impose very different I/O and compute demands. The output is a consistent set of indexed multimodal episodes, packaged into training-ready shards (Fig. 69).

**中文:** 要让 GR00T 2 跨任务、跨环境扩展，就必须把规模日益庞大、类型日益多样的人类演示集合转化为可直接用于训练的数据。我们的基础设施每月处理的输入数据量达到 PB 级，单个生产作业使用的 vCPU 接近 10,000 个。在这一规模下，数据准备必须同时承受海量数据搬运与异构计算：多相机视频需要被检索、解码并缩放；运动记录需要被变换，并在需要时重定向到训练所用的手部表示；观测、动作与标注则需要在时间上对齐。录制时长、分辨率、编码方式和重定向需求在不同来源之间差异很大，因此数量相同的片段（episode）可能带来截然不同的 I/O 与算力需求。最终输出是一组一致的、带索引的多模态片段，并被打包成训练就绪分片（shard）（Fig. 69）。

<a id="S2316"></a>
**Source:** p.133 S2316

**Original:** The central challenge is that these conversions share data and compete for limited working storage. A long video can contain many episodes, while one episode can depend on several camera files and separately stored motion records. Staging a shared file once avoids repeated downloads, but its slowest consumer determines when that storage can be reclaimed. A slow conversion or output upload can therefore retain local files, block retrieval of unrelated inputs, and leave compute workers idle. Interruptions compound the problem by adding repeated transfers and expensive recomputation. Sustained throughput requires coordinating data lifetime with execution progress across the entire pipeline.

**中文:** 核心挑战在于，这些转换既共享数据，又争夺有限的工作存储。一段长视频可以包含许多片段，而一个片段又可能依赖多个相机文件和单独存储的运动记录。把共享文件只暂存一次可以避免重复下载，但最慢的消费者决定了该存储何时可以被回收。因此，转换或输出上传变慢，可能导致本地文件被长期保留、阻塞无关输入的检索，并使计算工作节点空闲。中断会带来重复传输和高昂的重新计算，进一步加重这一问题。要维持持续的吞吐量，就需要在整个流水线中协调数据生命周期与执行进度。

<a id="S2317"></a>
**Source:** p.133 S2317

**Original:** The ingestion pipeline coordinates execution with the lifetime of its shared inputs: new work is admitted according to committed storage, dispatched where its inputs reside, and releases capacity only after its outputs are safely uploaded. Active files move directly from object storage to processing nodes, allowing conversion to begin before the entire selected collection has been retrieved. This removes intermediate staging on a shared filesystem while making input placement, retention, and reconstruction explicit responsibilities. Fig. 70 shows the mechanisms supporting this lifecycle.

**中文:** 摄取流水线让执行与其共享输入的生命周期相协调：新工作会依据已承诺（committed）的存储进行准入，派发到其输入所在的位置，并且只有在输出被安全上传之后才释放容量。活跃文件直接从对象存储移动到处理节点，使转换可以在所选集合全部取回之前开始。这样就去掉了共享文件系统上的中间暂存，同时把输入的放置、保留与重建明确为各自的职责。Fig. 70 展示了支撑这一生命周期的机制。

![F069](assets/F069.png)

<a id="C104"></a>
**Source:** p.134 C104 · 图 F069

**Original (caption):** Figure 69: Transformation of human demonstration recordings into aligned multimodal episodes and training-ready dataset shards.

**中文（图注）：** 图 69：将人类演示录制数据转换为对齐的多模态片段与可直接用于训练的数据集分片的过程。

<a id="S2318"></a>
**Source:** p.134 S2318

**Original:** Admit and place work (Fig. 70, panels B and C). Equal episode counts can imply very different file footprints and sharing patterns, so task limits alone cannot control storage demand. Before downloading an input group, admission accounts for resident files, pending transfers, and output headroom against the node’s budget. Required inputs must be ready before episode dispatch, and consumers execute on the node holding those inputs. Separate Ray worker pools (Moritz et al., 2018) give loading, conversion, and publication independent concurrency. Bounded queues limit outstanding work while storage admission limits the capacity committed to it.

**中文:** 准入并放置工作（Fig. 70，面板 B 与 C）。数量相同的片段可能对应截然不同的文件占用量和共享模式，因此仅靠任务数量限制无法控制存储需求。在下载某个输入组之前，准入会根据节点的预算核算驻留文件、待完成的传输以及输出余量。所需输入必须在片段派发之前就绪，消费者则在持有这些输入的节点上执行。独立的 Ray 工作进程池（Moritz et al., 2018）使加载、转换与发布各自拥有独立的并发度。有界队列限制未完成工作的数量，存储准入则限制分配给这些工作的容量。

<a id="S2319"></a>
**Source:** p.134 S2319

**Original:** Retain inputs through completion, then release capacity (Fig. 70, panels A to C). A downloaded video may serve several episodes, including consumers still waiting for execution. The loader establishes their claims before handing off work, protecting shared inputs across queueing, conversion, and upload. An episode releases its claims only after its intermediate results have been uploaded and temporary outputs cleaned up, while other consumers continue to protect the same files. Once the last claim is released, cleanup can reclaim those files and make room for the next input group. Consumer completion thus governs admission of subsequent inputs. Retrieval, conversion, and shard publication advance asynchronously around this dependency: they overlap across workers without allowing prefetch to grow independently of the storage that unfinished consumers still hold.

**中文:** 在完成前保留输入，然后释放容量（Fig. 70，面板 A 至 C）。一个已下载的视频可能服务于多个片段，其中包括仍在等待执行的消费者。加载器在移交工作之前先为它们建立占用（claim），从而在排队、转换和上传的全过程中保护共享输入。一个片段只有在其中间结果已上传、临时输出已清理之后才释放自己的占用，而其他消费者仍会继续保护同一批文件。一旦最后一个占用被释放，清理程序即可回收这些文件，为下一个输入组腾出空间。因此，消费者的完成情况决定了后续输入的准入。检索、转换与分片发布围绕这一依赖关系异步推进：它们在各工作节点之间相互重叠，但预取不会脱离未完成消费者仍占用的存储而独自增长。

<a id="S2320"></a>
**Source:** p.134 S2320

**Original:** Recover within the same capacity budget (Fig. 70, panel D). Recovery preserves this connection between execution and storage. Stopped attempts release obsolete claims, while lost inputs are reconstructed on an available node through the same admission path before affected episodes retry. Durable conversion-group and publication checkpoints separately identify completed results that job resumption can reuse. Input release after upload and cleanup, and checkpoint-based reuse after restart, are distinct boundaries: an uploaded artifact without recorded completion may still require repeated processing. These rules keep retries within the working-storage budget while preserving reusable progress.

**中文:** 在同一容量预算内恢复（Fig. 70，面板 D）。恢复过程保留了执行与存储之间的这一联系。被中止的尝试会释放已过时的占用，丢失的输入则会通过同一条准入路径在可用节点上重建，之后再重试受影响的片段。持久化的转换组检查点与发布检查点分别标识已完成的结果，作业恢复时可以复用这些结果。上传与清理之后的输入释放，以及重启之后基于检查点的复用，是两个不同的边界：已上传但未记录完成状态的产物，仍可能需要重复处理。这些规则使重试始终处于工作存储预算之内，同时保留可复用的进度。

<a id="S2321"></a>
**Source:** p.134 S2321

**Original:** This coordination of shared-input lifetime, admission, and recovery complements prior work on video analysis, multimodal processing, and prefetching (Poms et al., 2018; Chen et al., 2025; Luan et al., 2026; Dryden et al., 2021).

**中文:** 这种对共享输入生命周期、准入与恢复的协调，与此前关于视频分析、多模态处理和预取的工作形成互补（Poms et al., 2018; Chen et al., 2025; Luan et al., 2026; Dryden et al., 2021）。

<a id="S2322"></a>
**Source:** p.134 S2322

**Original:** Production evaluation. Tab. 36 summarizes throughput and resource use across three production jobs and recovery across five interrupted jobs. Each job uses 100 nodes with 96 vCPUs and 768 GiB of memory per node. The throughput workload covers 1.30 million episodes and about 18,700 demonstration-hours, with three camera views per episode.

**中文:** 生产环境评测。Tab. 36 汇总了三个生产作业的吞吐量与资源使用情况，以及五个被中断作业的恢复情况。每个作业使用 100 个节点，每个节点配备 96 个 vCPU 和 768 GiB 内存。吞吐量测试负载涵盖约 130 万个片段和约 18,700 演示小时，每个片段包含三个相机视角。

<a id="S2323"></a>
**Source:** p.134 S2323

**Original:** Completed-conversion time efficiency is the share of completed conversion time spent on work that did not need to be repeated after interruption.

**中文:** 已完成转换时间的效率，指在已完成的转换时间中，用于中断后无需重复的工作所占的比例。

![F070](assets/F070.png)

<a id="C105"></a>
**Source:** p.135 C105 · 图 F070

**Original (caption):** Figure 70: Multimodal data ingestion: (A) asynchronous overlap, (B) processing stages and the feedback from input release to admission, (C) storage tiers, and (D) recovery. Numbers identify shards, and timings are illustrative. Compute/upload overlap occurs across workers.

**中文（图注）：** 图 70：多模态数据摄取：(A) 异步重叠，(B) 处理阶段，以及从输入释放到准入的反馈，(C) 存储层级，(D) 恢复。数字用于标识分片，时间数值仅为示意。计算与上传的重叠发生在各工作节点之间。

![T036](assets/T036.png)

<a id="C106"></a>
**Source:** p.135 C106 · 表 T036

**Original (caption):** Table 36: Production evaluation of the data ingestion system. Ranges span jobs. Memory and disk use are per-node means.

**中文（表注）：** 表 36：数据摄取系统的生产环境评测。范围取值跨作业统计。内存与磁盘使用量为各节点的均值。

<a id="S2326"></a>
**Source:** p.135 S2326

**Original:** Published demonstration duration per job ∼6,240 h Execution time per job 8.0–8.6 h End-to-end throughput 722–780 demonstration-hours/h Time to first training-ready shard ≤28 min Mean worker assignment at 10–80% conversion completion

**中文:** [存疑：表格内容被抽取为单行文本，行列对应关系不明，且最后一项缺少数值，请对照 p.135 核实] 每个作业发布的演示时长 ∼6,240 h；每个作业的执行时间 8.0–8.6 h；端到端吞吐量 722–780 演示小时/小时；首个训练就绪分片的耗时 ≤28 min；转换完成 10–80% 时的平均工作进程分配。
