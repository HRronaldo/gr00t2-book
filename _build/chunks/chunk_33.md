### K. Infrastructure ｜ K. 基础设施

<a id="S2246"></a>
**Source:** p.127 S2246

**Original:** This section describes the compute, data, and research infrastructure used to develop GR00T 2.

**中文:** 本节介绍用于开发 GR00T 2 的计算、数据与研究基础设施。

### K.1. Overall Software and Hardware Stack ｜ K.1. 整体软硬件栈

<a id="S2247"></a>
**Source:** p.127 S2247

**Original:** Training a robotics foundation model like GR00T involves: (1) the ingestion and conversion of large volumes of multimodal recordings, such as video, motion, and language annotations, into training-ready datasets, (2) pretraining and post-training at scale on GPU clusters, and (3) the deployment and evaluation of the resulting policies in simulation and on robots. This section describes the infrastructure we built for these workloads and used to develop GR00T 2. At each layer of the stack we build on widely used open-source software, such as PyTorch, Ray, SkyPilot, and Kubernetes, improving it where needed and adding robotics-specific components on top. We describe the overall stack first and each component separately below.

**中文:** 训练 GR00T 这类机器人基础模型，需要完成三项工作：(1) 将大量多模态记录（如视频、动作和语言标注）摄取并转换为可用于训练的数据集；(2) 在 GPU 集群上大规模地进行预训练与后训练；(3) 在仿真环境和真实机器人上部署并评测所得的策略。本节介绍我们为这些工作负载构建、并用于开发 GR00T 2 的基础设施。软件栈的每一层都建立在 PyTorch、Ray、SkyPilot 和 Kubernetes 等广泛使用的开源软件之上，必要时对其加以改进，并在其上增加面向机器人的专用组件。下文先概述整个软件栈，再分别介绍各个组件。

![F067](assets/F067.png)

<a id="C101"></a>
**Source:** p.127 C101 · 图 F067

**Original (caption):** Figure 67: Overall software and hardware stack of GR00T 2.

**中文（图注）：** 图 67：GR00T 2 的整体软硬件栈。

<a id="S2248"></a>
**Source:** p.127 S2248

**Original:** Fig. 67 shows the stack from the hardware up. Each workload runs on the NVIDIA platform suited to it: GB300 for training, RTX PRO 6000 for data processing, L40 and L40S for simulation and evaluation, and Jetson Thor for inference on the robot. Kubernetes manages the GPU clusters, with NVIDIA NVSentinel monitoring node health and services such as GPU Operator and DCGM alongside it. SkyPilot (Yang et al., 2023) provisions clusters and schedules and manages jobs across them. Ray (Moritz et al., 2018) distributes work within a job, for training workers and for data ingestion alike, and PyTorch is the deep learning framework.

**中文:** Fig. 67 自硬件向上展示了整个软硬件栈。每类工作负载都运行在与之匹配的 NVIDIA 平台上：训练使用 GB300，数据处理使用 RTX PRO 6000，仿真与评测使用 L40 和 L40S，机器人上的推理使用 Jetson Thor。Kubernetes 管理 GPU 集群，NVIDIA NVSentinel 负责节点健康监控，并与 GPU Operator、DCGM 等服务协同工作。SkyPilot（Yang et al., 2023）负责为集群供给资源，并在集群之间调度和管理作业。Ray（Moritz et al., 2018）在作业内部分发工作，既用于训练 worker，也用于数据摄取；PyTorch 则是深度学习框架。

<a id="S2249"></a>
**Source:** p.127 S2249

**Original:** The following subsections describe the hardware, cluster and job management, distributed training, inference, and data infrastructure. Reinforcement-learning post-training runs on the same stack, and its infrastructure is described in Sec. F.3.

**中文:** 以下各小节依次介绍硬件、集群与作业管理、分布式训练、推理和数据基础设施。强化学习后训练运行在同一套软件栈上，其基础设施见 Sec. F.3。

### K.2. Hardware ｜ K.2. 硬件

<a id="S2250"></a>
**Source:** p.127 S2250

**Original:** GR00T 2 has many workloads that span large-scale foundation-model pretraining, simulation and policy evaluation, online post-training, and latency-sensitive robot deployment. These stages place different demands on accelerator memory, interconnect bandwidth, storage throughput, scheduling, and end-to-end latency. As a result, each stage has different hardware and system requirements that need to be accounted for.

**中文:** GR00T 2 涉及多种工作负载，涵盖大规模基础模型预训练、仿真与策略评测、在线后训练，以及对时延敏感的机器人部署。这些阶段对加速器显存、互连带宽、存储吞吐、调度和端到端时延提出了不同的要求。因此，每个阶段都有各自需要考虑的硬件与系统需求。

<a id="S2252"></a>
**Source:** p.128 S2252

**Original:** K.2.1. Pretraining

**中文:** K.2.1. 预训练

<a id="S2253"></a>
**Source:** p.128 S2253

**Original:** GR00T 2 pretraining ran on NVIDIA GB300 NVL72 systems because the workload placed a premium on GPU memory capacity, Tensor Core throughput, and networking/collective communication acceleration. Each Blackwell Ultra GPU provides up to 288 GB of HBM3e with 8 TB/s of memory bandwidth and approximately 2.5 PFLOPS of dense BF16/FP16 Tensor Core compute. Because the GR00T 2 model was small enough to fit without pipeline parallelism, this memory capacity allowed the model parameters, each rank’s optimizer state, and activations for a per-device batch of 16 to remain in GPU memory. The larger per-device batch provided more matrix-multiplication work for the Tensor Cores and amortized kernel-launch overhead, improving compute utilization (Aubrey and Stam, 2025).

**中文:** GR00T 2 的预训练运行在 NVIDIA GB300 NVL72 系统上，因为该工作负载对 GPU 显存容量、Tensor Core 吞吐，以及网络与集合通信加速有很高要求。每块 Blackwell Ultra GPU 提供最高 288 GB 的 HBM3e 显存，显存带宽为 8 TB/s，稠密 BF16/FP16 Tensor Core 算力约为 2.5 PFLOPS。由于 GR00T 2 模型足够小，无需流水线并行即可放下，因此这一显存容量使模型参数、每个 rank 的优化器状态，以及单设备批量为 16 时的激活值都能留在 GPU 显存中。更大的单设备批量为 Tensor Core 提供了更多矩阵乘法运算量，并分摊了 kernel 启动开销，从而提高了计算利用率（Aubrey and Stam, 2025）。

<a id="S2254"></a>
**Source:** p.128 S2254

**Original:** For networking, each GB300 NVL72 rack contains 18 compute trays and 72 GPUs connected as one NVLink domain. Fifth-generation NVLink provides 1.8 TB/s of bidirectional bandwidth per GPU. Within each NVLink domain, NVLink SHARP (NVLS) offloaded reductions to the NVSwitch. East/West communication used the RoCE scale-out fabric, with one 800 Gb/s ConnectX-8 SuperNIC per GPU (NVIDIA, n.d.a,n).

**中文:** 在网络方面，每个 GB300 NVL72 机架包含 18 个计算托盘和 72 块 GPU，它们连接成一个 NVLink 域。第五代 NVLink 为每块 GPU 提供 1.8 TB/s 的双向带宽。在每个 NVLink 域内，NVLink SHARP（NVLS）将归约操作卸载到 NVSwitch 上完成。东西向通信使用 RoCE 横向扩展（scale-out）网络结构，每块 GPU 配备一块 800 Gb/s 的 ConnectX-8 SuperNIC（NVIDIA, n.d.a,n）。

<a id="S2255"></a>
**Source:** p.128 S2255

**Original:** The full cluster contained 2,016 GPUs across 28 GB300 NVL72 racks. The GR00T 2 main pretraining run used 1,024 GPUs, while the remaining cluster capacity supported other training experiments concurrently.

**中文:** 整个集群共有 2,016 块 GPU，分布在 28 个 GB300 NVL72 机架中。GR00T 2 的主预训练运行使用了 1,024 块 GPU，其余集群容量则同时支持其他训练实验。

<a id="S2256"></a>
**Source:** p.128 S2256

**Original:** K.2.2. Simulation and Policy Evaluation

**中文:** K.2.2. 仿真与策略评测

<a id="S2257"></a>
**Source:** p.128 S2257

**Original:** Simulation and policy evaluation ran on NVIDIA L40 and L40S clusters because these workloads required graphics, simulation compute, and policy inference on the same accelerator. Both GPUs use the Ada Lovelace architecture and provide 48 GB of GDDR6 memory with 864 GB/s of memory bandwidth, 142 third-generation RT Cores, and 568 fourth-generation Tensor Cores. The RT Cores accelerate hardware ray tracing for rendered observations, while the Tensor Cores accelerate low-precision policy inference. The L40S retains the L40’s memory capacity and graphics resources while providing approximately twice its peak low-precision Tensor Core throughput, allowing more inference work to accompany simulation (NVIDIA, 2023, n.d.c).

**中文:** 仿真与策略评测运行在 NVIDIA L40 和 L40S 集群上，因为这些工作负载需要在同一加速器上同时完成图形渲染、仿真计算和策略推理。两款 GPU 均采用 Ada Lovelace 架构，各配备 48 GB GDDR6 显存，显存带宽为 864 GB/s，并具有 142 个第三代 RT Core 和 568 个第四代 Tensor Core。RT Core 为渲染观测提供硬件光线追踪加速，Tensor Core 则加速低精度策略推理。L40S 保留了 L40 的显存容量和图形资源，同时其峰值低精度 Tensor Core 吞吐约为 L40 的两倍，从而能够在运行仿真的同时承载更多推理工作（NVIDIA, 2023, n.d.c）。

<a id="S2258"></a>
**Source:** p.128 S2258

**Original:** The 48 GB memory capacity provides headroom to keep the policy checkpoint, simulator state, and rendering buffers resident while processing multiple environments, although achievable concurrency depends on the simulator and task. Unlike GB300 NVL72 systems, L40 and L40S are PCIe Gen4 GPUs without NVLink (NVIDIA, 2023, n.d.c). Evaluation therefore scales primarily by distributing independent environment, checkpoint, and random-seed shards across workers rather than through frequent cross-GPU collectives. Network and storage throughput remain important for staging checkpoints and collecting rollout artifacts, but the primary capacity metrics are environments per GPU, rollout throughput, and checkpoint-evaluation turnaround time.

**中文:** 48 GB 的显存容量为同时处理多个环境时保留策略检查点、仿真器状态和渲染缓冲区提供了余量，不过可实现的并发度取决于仿真器和任务。与 GB300 NVL72 系统不同，L40 和 L40S 是不带 NVLink 的 PCIe Gen4 GPU（NVIDIA, 2023, n.d.c）。因此，评测主要通过将独立的环境、检查点和随机种子分片分配给各个 worker 来扩展，而不是依赖频繁的跨 GPU 集合通信。网络和存储吞吐对于暂存检查点、收集 rollout（轨迹采样）产物依然重要，但主要的容量指标是每块 GPU 的环境数、rollout 吞吐量以及检查点评测的周转时间。

<a id="S2259"></a>
**Source:** p.128 S2259

**Original:** K.2.3. Online Post-Training

**中文:** K.2.3. 在线后训练

<a id="S2260"></a>
**Source:** p.128 S2260

**Original:** Online post-training ran across heterogeneous H100, GB300, and L40/L40S pools because no single accelerator could satisfy every stage of the workflow. H100 and GB300 systems supported distributed policy optimization. L40 and L40S systems supported simulation-based collection and evaluation, where graphics capabilities were needed. Capacity was allocated independently to each stage and adjusted as workload bottlenecks shifted.

**中文:** 在线后训练运行在异构的 H100、GB300 以及 L40/L40S 资源池上，因为没有任何单一加速器能满足工作流中的每个阶段。H100 和 GB300 系统支持分布式策略优化。L40 和 L40S 系统支持基于仿真的数据收集与评测，这类工作需要图形能力。各阶段的资源容量独立分配，并随工作负载瓶颈的转移而调整。

### K.3. Cluster and Job Management ｜ K.3. 集群与作业管理

<a id="S2261"></a>
**Source:** p.128 S2261

**Original:** K.3.1. Kubernetes

**中文:** K.3.1. Kubernetes

<a id="S2262"></a>
**Source:** p.128 S2262

**Original:** Kubernetes provides the AI factory execution layer for GR00T 2, with the cluster software stack deployed through NVIDIA AI Cluster Runtime (AICR) (NVIDIA, n.d.d). This integrates NVIDIA DSX OS components for GPU enablement, high-performance networking, and infrastructure resilience. NVIDIA GPU Operator and Network Operator manage the GPU and networking software stacks, while KAI Scheduler and Kueue provide workload scheduling and admission control, priorities, resource quotas, and topology-aware placement for multi-node workloads.

**中文:** Kubernetes 为 GR00T 2 提供 AI 工厂的执行层，集群软件栈通过 NVIDIA AI Cluster Runtime（AICR）部署（NVIDIA, n.d.d）。它集成了 NVIDIA DSX OS 组件，用于 GPU 启用、高性能网络和基础设施韧性。NVIDIA GPU Operator 和 Network Operator 负责管理 GPU 与网络软件栈；KAI Scheduler 和 Kueue 则为多节点工作负载提供调度与准入控制、优先级、资源配额，以及拓扑感知的放置。

<a id="S2263"></a>
**Source:** p.129 S2263

**Original:** On GB300 NVL72 systems, NVIDIA’s Dynamic Resource Allocation (DRA) driver manages ComputeDomains, enabling secure multi-node NVLink access for workload pods. NCCL uses this fabric for collective communication within each NVLink domain and RoCE for communication across racks.

**中文:** 在 GB300 NVL72 系统上，NVIDIA 的动态资源分配（DRA）驱动程序负责管理 ComputeDomains，为工作负载 Pod 提供安全的多节点 NVLink 访问。NCCL 在每个 NVLink 域内使用该互连进行集合通信，并通过 RoCE 实现跨机架通信。

<a id="S2264"></a>
**Source:** p.129 S2264

**Original:** NVSentinel, also part of NVIDIA DSX OS, monitors GPU and node health and supports policy-driven isolation and remediation of faulty nodes. Together with SkyPilot’s job recovery and the training runtime’s checkpoint-resume mechanisms, these components support reliable operation of the GR00T 2 AI factory.

**中文:** NVSentinel 同样是 NVIDIA DSX OS 的组成部分，负责监控 GPU 与节点健康，并支持基于策略对故障节点进行隔离与修复。结合 SkyPilot 的作业恢复机制以及训练运行时的检查点续训机制，这些组件共同保障了 GR00T 2 AI 工厂的可靠运行。

<a id="S2265"></a>
**Source:** p.129 S2265

**Original:** K.3.2. SkyPilot

**中文:** K.3.2. SkyPilot

<a id="S2266"></a>
**Source:** p.129 S2266

**Original:** GR00T 2 training uses SkyPilot (Yang et al., 2023) as the infrastructure orchestration layer for distributed GPU workloads. A shared SkyPilot API control plane provides a common interface for submitting experiments, provisioning workload clusters, monitoring execution, and managing cluster lifecycles. The platform connects this control plane to GPU infrastructure through configured Kubernetes contexts and workspace access controls. Infrastructure configuration and administrative policies are maintained separately from model code, allowing researchers to specify training requirements while platform operators manage credentials, storage integration, and infrastructure access.

**中文:** GR00T 2 训练使用 SkyPilot（Yang et al., 2023）作为分布式 GPU 工作负载的基础设施编排层。共享的 SkyPilot API 控制平面提供统一接口，用于提交实验、供给工作负载集群、监控执行过程以及管理集群生命周期。平台通过已配置的 Kubernetes 上下文和工作区访问控制，将该控制平面与 GPU 基础设施相连。基础设施配置与管理策略独立于模型代码维护，使研究人员能够描述训练需求，而平台运维人员负责管理凭据、存储集成和基础设施访问。

<a id="S2267"></a>
**Source:** p.129 S2267

**Original:** Each experiment runs as a SkyPilot managed job. Once resources are available, the workload containers form a Ray cluster, and the training driver creates a distributed worker for each GPU. SkyPilot manages infrastructure execution, Ray places training workers, and PyTorch, NCCL, and the optimizer implementation perform distributed model training.

**中文:** 每个实验都作为一个 SkyPilot 托管作业运行。资源就绪后，工作负载容器组成一个 Ray 集群，训练驱动程序为每块 GPU 创建一个分布式 worker。SkyPilot 负责基础设施执行，Ray 负责放置训练 worker，PyTorch、NCCL 以及优化器实现则共同完成分布式模型训练。

<a id="S2268"></a>
**Source:** p.129 S2268

**Original:** The infrastructure accounts for the communication and data-access requirements of large-scale joint videoand-action training. Kubernetes and Kueue coordinate admission of multi-node workloads using GPU topology information, while the OCI workload configuration requests RDMA network attachments and placement within GPU clique topology domains. The training runtime additionally orders distributed ranks according to physical topology. Shared Lustre storage supplies datasets, pretrained assets, and persistent checkpoints, while node-local scratch supports temporary runtime files. These components connect resource allocation to the communication and storage requirements of the GR00T 2 training workload.

**中文:** 该基础设施考虑了大规模视频-动作联合训练（[存疑：原文抽取为 videoand-action，疑为 video-and-action]）在通信与数据访问方面的需求。Kubernetes 与 Kueue 利用 GPU 拓扑信息协调多节点工作负载的准入，而 OCI 工作负载配置则请求 RDMA 网络附件，并将 Pod 放置在 GPU clique 拓扑域内。训练运行时还会根据物理拓扑对分布式 rank 进行排序。共享的 Lustre 存储提供数据集、预训练资产和持久化检查点，节点本地的 scratch 存储则用于临时运行时文件。这些组件将资源分配与 GR00T 2 训练工作负载的通信和存储需求联系起来。

<a id="S2269"></a>
**Source:** p.129 S2269

**Original:** Launch-time administrative policies validate infrastructure selections, preserve backend-specific placement settings, and configure centralized log forwarding. Workspace access controls govern access to the available compute environments. The platform also supports policies that derive queue assignments and scheduling priorities from administrator-managed workspace configuration. SkyPilot managed-job recovery works together with bounded retries and checkpoint resume in the training stack. This separation enables infrastructure recovery while retaining training state in persistent storage.

**中文:** 启动时的管理策略会校验基础设施选择、保留特定后端的放置设置，并配置集中式日志转发。工作区访问控制用于管理对可用计算环境的访问。平台还支持根据管理员维护的工作区配置推导队列分配和调度优先级的策略。SkyPilot 托管作业的恢复机制与训练栈中有上限次数的重试和检查点续训协同工作。这种分工使基础设施能够恢复，同时训练状态保存在持久存储中。
