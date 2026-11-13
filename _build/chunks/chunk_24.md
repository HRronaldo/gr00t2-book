### F.4. Precision Manipulation through RL Post-Training ｜ 通过 RL 后训练实现精密操作

<a id="S1675"></a>
**Source:** p.91 S1675

**Original:** We evaluate three complementary post-training approaches on four real-world contact-rich manipulation tasks, demonstrating how GR00T 2 improves through RL-based learning and targeted policy adaptation.

**中文:** 我们在四个真实世界的富接触操作任务上评估了三种互补的后训练方法，展示 GR00T 2 如何通过基于强化学习（RL）的学习和有针对性的策略适配获得提升。

<a id="S1676"></a>
**Source:** p.91 S1676

**Original:** Tasks. Our evaluation includes four precision manipulation tasks (Fig. 49). In fixed-pipe fittings, the robot grasps a threaded tee fitting, aligns it with a horizontally mounted pipe, engages the threads, and completes one full turn. This is the Fixed-Pipe Fittings task of Tab. 1a, but each RL trial starts from a fitting pose that the post-trained policy struggles with. In finger placement, the robot inserts two 3 mm pins on a gripper finger into matching holes on a fixed base, requiring accurate position and yaw alignment.

**中文:** 任务。我们的评估包含四个精密操作任务（Fig. 49）。在固定管件（fixed-pipe fittings）任务中，机器人抓取一个带螺纹的三通管件，将其与水平安装的管道对齐，咬合螺纹，并完整旋转一圈。这就是 Tab. 1a 中的 Fixed-Pipe Fittings 任务，但每次 RL 试次都从一个后训练策略难以应对的管件位姿开始。在手指放置（finger placement）任务中，机器人需要把夹爪手指上的两根 3 mm 销钉插入固定底座上对应的孔中，这要求准确的位置对齐和偏航（yaw）对齐。

<a id="S1677"></a>
**Source:** p.91 S1677

**Original:** In cable insertion, the robot inserts an Ethernet connector into a designated network-switch port, with success determined by network-link connectivity. In charger insertion, the robot inserts a two-prong charger into a specified outlet within a 2 × 6 grid. These tasks involve tight geometric tolerances, partial occlusion, and contact-sensitive execution.

**中文:** 在线缆插入（cable insertion）任务中，机器人将以太网接头插入指定的网络交换机端口，成功与否以网络链路是否连通为准。在充电器插入（charger insertion）任务中，机器人需要把两极插头的充电器插入 2 × 6 网格中指定的插座。这些任务涉及严格的几何公差、部分遮挡以及对接触敏感的执行过程。

<a id="S1678"></a>
**Source:** p.91 S1678

**Original:** Evaluation Protocol. All evaluated methods build on the same SFT-initialized GR00T 2 checkpoint, either as an initialization or as a frozen base. GRPO directly updates GR00T 2 using both successful and failed trajectories. Self-imitation reuses successful GRPO rollouts without additional collection. Residual RL instead learns a separate controller on top of the frozen base, using human-assisted training experience.

**中文:** 评估协议。所有被评估的方法都以同一个经监督微调（SFT）初始化的 GR00T 2 检查点为基础，它要么作为初始化，要么作为冻结的基座。GRPO 直接使用成功和失败的轨迹来更新 GR00T 2。自模仿（self-imitation）复用成功的 GRPO rollout，不需要额外采集。残差强化学习（Residual RL）则相反，它在冻结的基座之上学习一个独立的控制器，并使用人工辅助的训练经验。

<a id="S1680"></a>
**Source:** p.92 S1680

**Original:** For each task, evaluations use the same target distribution, reset conditions, and time limits, with no human intervention during evaluation. Trials are independent of training rollouts, and we report per-task success rates. An episode is considered a failure if misalignment prevents the policy from recovering or if the insertion exceeds the time limit.

**中文:** 对每个任务，评估都使用相同的目标分布、重置条件和时间限制，评估期间不进行人工干预。试次与训练 rollout 相互独立，我们报告各任务的成功率。若错位使策略无法恢复，或插入过程超过时间限制，则该回合记为失败。

<a id="S1681"></a>
**Source:** p.92 S1681

**Original:** Real-World Results. Direct RL on GR00T 2 improves precision manipulation. GRPO increases success rates on all four tasks (Fig. 5), raising fixed-pipe fittings from 66% to 86%, finger placement from 58% to 72%, cable insertion from 76% to 92%, and charger insertion from 40% to 94%. With 50 trials per task, the gains on charger insertion and fixed-pipe fittings are significant at the 5% level (two-sided Fisher exact test), whereas those on cable insertion (38 to 46 successes) and finger placement (29 to 36) are not conclusive at this sample size.

**中文:** 真实世界结果。对 GR00T 2 直接进行 RL 可以提升精密操作能力。GRPO 在全部四个任务上都提高了成功率（Fig. 5），固定管件从 66% 提高到 86%，手指放置从 58% 提高到 72%，线缆插入从 76% 提高到 92%，充电器插入从 40% 提高到 94%。每个任务进行 50 次试次时，充电器插入和固定管件的提升在双侧 Fisher 精确检验下达到 5% 显著性水平；而线缆插入（成功次数从 38 增至 46）和手指放置（从 29 增至 36）的提升在此样本量下尚无定论。

<a id="S1682"></a>
**Source:** p.92 S1682

**Original:** Self-imitation consolidates successful RL exploration. Self-imitation reaches 88% on fixed-pipe fittings, 98% on finger placement, 94% on cable insertion, and 96% on charger insertion, matching or exceeding GRPO on all four tasks. The gain is most pronounced on finger placement, where success rises from 72% to 98%.

**中文:** 自模仿巩固了成功的 RL 探索。自模仿在固定管件上达到 88%，在手指放置上达到 98%，在线缆插入上达到 94%，在充电器插入上达到 96%，在全部四个任务上都与 GRPO 持平或超过 GRPO。提升最明显的是手指放置任务，其成功率从 72% 升至 98%。

<a id="S1683"></a>
**Source:** p.92 S1683

**Original:** These results highlight the potential of combining RL exploration with supervised policy optimization. RL discovers successful behaviors through interaction, while self-imitation consolidates them under a stable supervised objective. This offers a complementary route to improving GR00T 2 beyond direct policy-gradient optimization.

**中文:** 这些结果凸显了将 RL 探索与监督式策略优化相结合的潜力。RL 通过交互发现成功的行为，而自模仿则在稳定的监督目标下巩固这些行为。这为改进 GR00T 2 提供了一条补充途径，超越了直接的策略梯度优化。

<a id="S1684"></a>
**Source:** p.92 S1684

**Original:** Residual RL enables targeted adaptation without updating GR00T 2. Residual RL reaches 76% on fixed-pipe fittings, 84% on finger placement, 82% on cable insertion, and 70% on charger insertion, with clear gains over supervised post-training on finger placement and charger insertion. These results show that lightweight corrective controllers can improve precision execution while leaving the pretrained GR00T 2 intact.

**中文:** 残差 RL 无需更新 GR00T 2 即可实现有针对性的适配。残差 RL 在固定管件上达到 76%，在手指放置上达到 84%，在线缆插入上达到 82%，在充电器插入上达到 70%，并且在手指放置和充电器插入上相对监督后训练有明显提升。这些结果表明，轻量级的纠正性控制器可以在保持预训练 GR00T 2 完整不变的同时，提升精密执行能力。

<a id="S1685"></a>
**Source:** p.92 S1685

**Original:** These experiments show that direct RL, self-imitation, and residual RL can improve GR00T 2’s precision manipulation through complementary forms of post-training.

**中文:** 这些实验表明，直接 RL、自模仿和残差 RL 都能通过各自互补的后训练形式，提升 GR00T 2 的精密操作能力。

<a id="S1686"></a>
**Source:** p.92 S1686

**Original:** The preceding experiments improve policies through physical interaction. We next investigate a complementary source of training experience: interaction with a learned environment constructed from recorded policy rollouts.

**中文:** 前面的实验是通过物理交互来改进策略的。接下来，我们研究另一种互补的训练经验来源：与一个由已录制的策略 rollout 构建而成的学习环境进行交互。

### F.5. Reinforcement Learning with Neural Simulation ｜ 基于神经仿真的强化学习

<a id="S1687"></a>
**Source:** p.92 S1687

**Original:** In neural-simulation RL, the policy interacts with a learned world model in place of the physical environment. This changes how training experience is generated while retaining reward-based optimization of the pretrained world-action policy.

**中文:** 在神经仿真 RL 中，策略与一个学习得到的世界模型交互，以代替物理环境。这改变了训练经验的生成方式，同时保留了对预训练世界-动作策略进行基于奖励的优化。

<a id="S1688"></a>
**Source:** p.92 S1688

**Original:** We use DreamDojo (Gao et al., 2026), initialized from pretrained video priors, to turn recorded robot interactions into a learning environment. Successful and failed attempts provide supervision for task-specific adaptation. A pretrained GR00T 2 policy can then collect further training experience through interaction with the adapted model. Task rollouts are still required to construct this environment, while subsequent policy-learning rollouts are generated in neural simulation.

**中文:** 我们使用 DreamDojo（Gao et al., 2026），以预训练的视频先验进行初始化，将已录制的机器人交互转化为学习环境。成功和失败的尝试为面向具体任务的适配提供监督。随后，预训练的 GR00T 2 策略可以通过与适配后的模型交互，收集更多训练经验。构建该环境仍然需要任务 rollout，而之后的策略学习 rollout 则在神经仿真中生成。

<a id="S1689"></a>
**Source:** p.92 S1689

**Original:** To support policy learning, the model’s predictions must provide usable inputs to GR00T 2 throughout an episode. We provide multi-view camera predictions, align them with executed action chunks, and approximate proprioceptive inputs using action targets. We also maintain visual history across successive world-model calls. We first describe world-model construction and the closed-loop policy interface, including support for long-horizon interaction. We then present the experimental setup, reward modeling and policy optimization, and results in RoboLab and on real-world tasks.

**中文:** 为支持策略学习，模型的预测在整个回合中都必须能为 GR00T 2 提供可用的输入。我们提供多视角相机预测，将其与已执行的动作块对齐，并使用动作目标近似本体感知输入。我们还在连续的世界模型调用之间维持视觉历史。我们首先介绍世界模型的构建以及闭环策略接口，包括对长时序交互的支持。随后介绍实验设置、奖励建模与策略优化，以及在 RoboLab 和真实世界任务上的结果。

<a id="S1690"></a>
**Source:** p.92 S1690

**Original:** Training Data and Task Adaptation. We first mid-train DreamDojo on multi-view episodes, then adapt the resulting model to downstream tasks. The bimanual YAM corpus contains 8,310 four-view episodes from policy rollouts and DAgger collection, including failed attempts and recovery. These episodes total approximately 226.8 hours at 30 Hz. The DROID source corpus contains 57,773 episodes, approximately 273 hours at 15 Hz, with three synchronized camera views and recorded joint and gripper actions.

**中文:** 训练数据与任务适配。我们先在多视角回合上对 DreamDojo 进行中段训练（mid-training），然后将得到的模型适配到下游任务。双臂 YAM 数据集包含 8,310 个四视角回合，来自策略 rollout 和 DAgger 采集，其中包括失败尝试和恢复过程。这些回合合计约 226.8 小时，采样频率为 30 Hz。DROID 源数据集包含 57,773 个回合，约 273 小时，采样频率为 15 Hz，具有三个同步的相机视角，并记录了关节动作和夹爪动作。

<a id="S1692"></a>
**Source:** p.93 S1692

**Original:** We tile synchronized camera views into one video canvas so that the model predicts them jointly using DreamDojo’s existing video backbone and causal variational autoencoder (VAE). YAM uses a 2 × 2 layout at 480 × 640 pixels. DROID concatenates three 180 × 320 views horizontally and pads the canvas vertically to 192 × 960 pixels.

**中文:** 我们把同步的相机视角平铺拼接成一张视频画布，使模型能够利用 DreamDojo 现有的视频主干网络和因果变分自编码器（VAE）对它们进行联合预测。YAM 采用 480 × 640 像素的 2 × 2 布局。DROID 将三个 180 × 320 的视角水平拼接，并在垂直方向上将画布填充至 192 × 960 像素。

<a id="S1693"></a>
**Source:** p.93 S1693

**Original:** Video and action sampling are aligned separately. For YAM, we downsample video from 30 to 15 Hz while retaining fourteen-dimensional actions at 30 Hz. Each window contains five conditioning frames and twelve future frames, paired with 24 future actions. DROID video and eight-dimensional actions both remain at 15 Hz, and each window contains five conditioning frames and sixteen future frames. We precompute and cache VAE latents, which are the compressed video representations used by the world model. We sample temporally aligned training windows from this cache, avoiding repeated encoding of the same recorded videos.

**中文:** 视频采样与动作采样分别对齐。对于 YAM，我们将视频从 30 Hz 降采样到 15 Hz，同时保留 30 Hz 的十四维动作。每个窗口包含五个条件帧和十二个未来帧，并与 24 个未来动作配对。DROID 的视频和八维动作均保持在 15 Hz，每个窗口包含五个条件帧和十六个未来帧。我们预先计算并缓存 VAE 潜变量，它们是世界模型所使用的压缩视频表示。我们从该缓存中采样时间对齐的训练窗口，避免对相同的已录制视频重复编码。

<a id="S1694"></a>
**Source:** p.93 S1694

**Original:** Task adaptation. We adapt the mid-trained world model to the scenes and action distributions encountered by the target policy. Successful and failed rollouts provide supervision on the states reached during execution, allowing the model to learn task-relevant visual changes and action effects. We fine-tune the model on these rollouts using the multi-view representation and temporal alignment used during policy interaction. Recorded robot actions and world-model inputs use consistent action coordinates and normalization.

**中文:** 任务适配。我们将中段训练后的世界模型适配到目标策略所遇到的场景和动作分布。成功和失败的 rollout 为执行过程中到达的状态提供监督，使模型能够学习与任务相关的视觉变化和动作效果。我们在策略交互时所用的多视角表示和时间对齐方式下，利用这些 rollout 对模型进行微调。已录制的机器人动作与世界模型输入使用一致的动作坐标和归一化方式。

<a id="S1695"></a>
**Source:** p.93 S1695

**Original:** Closed-Loop Simulation Interface. To collect experience for policy optimization, we alternate GR00T 2 action prediction with world-model prediction throughout a task episode. A rollout starts from recorded multi-view observations. GR00T 2 predicts an action sequence, and the world model predicts the camera observations resulting from its executed prefix. These predicted images become the policy’s next visual input, allowing GR00T 2 to respond to the consequences of its own actions. Repeating this interaction produces a trajectory for reward evaluation and policy learning.

**中文:** 闭环仿真接口。为了收集策略优化所需的经验，我们在整个任务回合中交替进行 GR00T 2 的动作预测与世界模型预测。rollout 从已录制的多视角观测开始。GR00T 2 预测一段动作序列，世界模型则预测其已执行前缀所导致的相机观测。这些预测图像成为策略的下一个视觉输入，使 GR00T 2 能够对自身动作的后果作出响应。重复这一交互过程，即可得到用于奖励评估和策略学习的轨迹。

<a id="S1696"></a>
**Source:** p.93 S1696

**Original:** At interaction round 𝑟, GR00T 2 samples an action plan from the current observation and task instruction. Let 𝐴𝑟denote its executed prefix of 𝐻actions and 𝐶𝑟the world model’s conditioning latents. Initially, 𝐶0 is obtained by encoding five recorded video frames into two latent frames. The mapping 𝑔converts actions into the world model’s action coordinates and normalization. Future latents and the next conditioning history are then given by

**中文:** 在第 𝑟 轮交互中，GR00T 2 从当前观测和任务指令中采样一个动作计划。记 𝐴𝑟 为其已执行的 𝐻 个动作前缀，𝐶𝑟 为世界模型的条件潜变量。初始时，𝐶0 通过将五个已录制视频帧编码为两个潜变量帧得到。映射 𝑔 将动作转换为世界模型的动作坐标和归一化方式。未来潜变量及下一个条件历史由下式给出：[存疑：抽取结果中缺少该公式] [公式原文见 p.93]

<a id="S1700"></a>
**Source:** p.93 S1700

**Original:** Here, Tail2 retains the final two latent frames of the concatenated conditioning and predicted sequence. After decoding, we remove the overlapping conditioning prefix and append the newly predicted images to the policy’s visual history. The views and historical frames required by GR00T 2 form its next observation, closing the interaction loop.

**中文:** 这里，Tail2 保留拼接后的条件序列与预测序列中的最后两个潜变量帧。解码之后，我们去掉重叠的条件前缀，并将新预测的图像追加到策略的视觉历史中。GR00T 2 所需的视角和历史帧构成其下一步观测，从而闭合交互回路。

<a id="S1701"></a>
**Source:** p.93 S1701

**Original:** The rollout preserves the video-action alignment used during training. For YAM, the world model predicts twelve new video frames at 15 Hz for 24 native actions at 30 Hz. For DROID/RoboLab, it predicts sixteen frames for sixteen actions, both at 15 Hz. We query the policy again after executing this action prefix and truncate the final round at the task horizon.

**中文:** rollout 保持了训练时使用的视频-动作对齐方式。对于 YAM，世界模型以 15 Hz 预测 12 个新视频帧，对应 30 Hz 下的 24 个原生动作。对于 DROID/RoboLab，它预测 16 帧，对应 16 个动作，两者均以 15 Hz 运行。执行完该动作前缀后，我们会再次查询策略，并在任务时限处截断最后一轮。

<a id="S1702"></a>
**Source:** p.93 S1702

**Original:** We exclude the five-frame conditioning prefix from the images returned to the policy. RoboLab decodes the complete latent window at each round. YAM retains the causal decoder cache and decodes only new latents after the first round. This decoder cache is separate from the latent history passed to the world model. For policies requiring proprioception, we initialize the state input from the recorded reset state. At each later policy query, we use the last executed action target as an approximation of the current robot state.

**中文:** 返回给策略的图像不包含五帧条件前缀。RoboLab 在每一轮都解码完整的潜变量窗口。YAM 则保留因果解码器缓存，仅在第一轮之后解码新的潜变量。该解码器缓存与传入世界模型的潜变量历史是分开的。对于需要本体感知的策略，我们从已录制的重置状态初始化状态输入。在之后的每次策略查询中，我们使用上一次已执行的动作目标作为当前机器人状态的近似。

<a id="S1703"></a>
**Source:** p.94 S1703

**Original:** Long-Horizon Prediction. Policy learning requires multiple rounds of interaction, whereas the world model is trained on short video windows. We therefore generate successive segments autoregressively. After the first segment, the model conditions on its own predictions rather than recorded observations. Errors in this history can affect subsequent predictions and policy decisions.

**中文:** 长时序预测。策略学习需要多轮交互，而世界模型是在短视频窗口上训练的。因此，我们以自回归方式生成连续片段。在第一个片段之后，模型以自身的预测而非已录制的观测作为条件。该历史中的误差可能影响后续的预测和策略决策。

<a id="S1704"></a>
**Source:** p.94 S1704

**Original:** For the DROID-derived model used in RoboLab, we perturb recorded conditioning latents during training to expose the model to imperfect visual histories, while keeping recorded future latents as prediction targets. For a clean conditioning tensor 𝐶, we use

**中文:** 对于 RoboLab 所用的 DROID 衍生模型，我们在训练时扰动已录制的条件潜变量，使模型接触到不完美的视觉历史，同时保留已录制的未来潜变量作为预测目标。对于干净的条件张量 𝐶，我们采用下式：

![E007](assets/equations/E007.png)

<a id="E007"></a>
**Source:** p.94 E007

**Original:** 𝐶= (1 −𝜎)𝐶+ 𝜎𝜖, 𝜖∼𝒩(0, 𝐼). (20)

**中文:** 该式描述对条件张量加噪的方式：以噪声强度 𝜎 将 𝐶 与标准高斯噪声 𝜖 混合，式中原样保留为 $$𝐶= (1 −𝜎)𝐶+ 𝜎𝜖, 𝜖∼𝒩(0, 𝐼). (20)$$ [公式原文见 p.94] [存疑：左侧 𝐶 与右侧 𝐶 可能是不同符号，抽取未保留其区别]

<a id="S1705"></a>
**Source:** p.94 S1705

**Original:** The noise strength 𝜎is sampled from 0, 0.0245, 0.0480, and 0.0925 with probabilities 0.2, 0.2, 0.4, and 0.2, respectively. We also explored replacing recorded history with a model-generated preceding segment, with gradients stopped through that history. These preliminary trials showed no clear additional benefit over noise augmentation, which we retain in the final training recipe.

**中文:** 噪声强度 𝜎 从 0、0.0245、0.0480 和 0.0925 中采样，对应概率分别为 0.2、0.2、0.4 和 0.2。我们也尝试过用模型生成的前序片段替代已录制的历史，并让梯度在该历史处截断。这些初步试验表明，它相对于噪声增广（noise augmentation）并没有明显的额外收益，因此我们在最终训练配方中保留了噪声增广。

<a id="S1706"></a>
**Source:** p.94 S1706

**Original:** At rollout time, we pass the final two predicted latent frames to the next world-model segment as its conditioning history. This avoids decoding and re-encoding images to construct that history. We still decode predicted latents into images for GR00T 2: the world model carries its history in latent space, while the policy receives camera observations in pixel space.

**中文:** 在 rollout 时，我们将最后两个预测潜变量帧作为下一个世界模型片段的条件历史传入。这样就无需先解码再重新编码图像来构建该历史。不过，我们仍会将预测的潜变量解码为图像供 GR00T 2 使用：世界模型在潜空间中保存其历史，而策略则在像素空间中接收相机观测。

<a id="S1707"></a>
**Source:** p.94 S1707

**Original:** Experimental Setup. Starting from SFT, GRPO updates GR00T 2 through interaction with the learned environment, while the world model and learned success detector remain fixed. Native RoboLab evaluation and real-world execution test whether these updates improve behavior outside the learned environment.

**中文:** 实验设置。以 SFT 为起点，GRPO 通过与学习得到的环境交互来更新 GR00T 2，同时世界模型和学习得到的成功检测器保持固定。原生 RoboLab 评测与真实世界执行用于检验这些更新能否在学习得到的环境之外改善行为。

<a id="S1708"></a>
**Source:** p.94 S1708

**Original:** We collect rollouts from the initial GR00T 2 policy, retaining successful and failed attempts for world-model adaptation and reward supervision. The study covers ten RoboLab tasks and four families of physical manipulation: peg insertion, test-tube insertion into a specified rack hole, bun placement on yellow and white cups, and hardware sorting with nine instructions. Hardware sorting tests whether the policy selects the requested target object and destination from three target object categories and three colored trays in the presence of distractors. Fig. 52 illustrates the physical task setups.

**中文:** 我们从初始的 GR00T 2 策略采集 rollout，保留成功和失败的尝试，用于世界模型适配和奖励监督。该研究涵盖十个 RoboLab 任务，以及四类物理操作：插销插入（peg insertion）、将试管插入指定的试管架孔位、将小圆面包放置到黄色和白色杯子上，以及根据九条指令进行硬件分拣。硬件分拣用于检验策略在存在干扰物时，能否从三类目标物体和三个彩色托盘中选出所要求的目标物体与目的地。Fig. 52 展示了物理任务的设置。

<a id="S1709"></a>
**Source:** p.94 S1709

**Original:** World-model adaptation uses 300 physical rollouts for each insertion task and each of the two bun-placement tasks, and approximately 300 rollouts in total for hardware sorting. The insertion and hardware tasks share a jointly adapted world model, while a separate model is adapted for bun placement. For RoboLab, we adapt one shared world model using 450 training trajectories per task across 64 tasks, with 50 trajectories per task held out. Joint policy RL uses ten tasks from this collection. Each RL run starts from its SFT baseline and keeps the world model and reward model fixed. RoboLab reward supervision uses 450 training and 50 validation trajectories per task. The test-tube success detector uses a separate set of 600 training and 120 validation videos labeled for insertion and release in the designated rack hole.

**中文:** 世界模型适配使用的物理 rollout 数量为：每个插入任务以及两个小圆面包放置任务各 300 条，硬件分拣总计约 300 条。插入任务与硬件分拣任务共享一个联合适配的世界模型，而小圆面包放置则单独适配一个模型。对于 RoboLab，我们使用 64 个任务、每个任务 450 条训练轨迹适配一个共享的世界模型，并且每个任务另留出 50 条轨迹。联合策略 RL 使用该集合中的十个任务。每次 RL 运行都从其 SFT 基线开始，并保持世界模型和奖励模型固定。RoboLab 奖励监督使用每个任务 450 条训练轨迹和 50 条验证轨迹。试管成功检测器使用另外一组 600 段训练视频和 120 段验证视频，这些视频标注了在指定试管架孔位中的插入与释放。

<a id="S1710"></a>
**Source:** p.94 S1710

**Original:** Reward Modeling and Policy Optimization. Sparse rewards. Dense progress rewards are difficult to obtain consistently across manipulation tasks and expensive to annotate. They can also introduce reward hacking when a policy increases a proxy score without completing the requested goal. We therefore use sparse task-completion rewards, learning a binary success detector rather than a continuous progress score.

**中文:** 奖励建模与策略优化。稀疏奖励。稠密的进度奖励难以在各类操作任务中稳定获得，且标注成本高昂。当策略提升了代理分数却没有完成所要求的目标时，它们还可能引入奖励投机（reward hacking）。因此，我们采用稀疏的任务完成奖励，即学习一个二值成功检测器，而不是连续的进度分数。

<a id="S1711"></a>
**Source:** p.94 S1711

**Original:** We train compact success detectors based on VideoMAE (Tong et al., 2022) to provide rewards during RL. For physical videos, a vision-language model (VLM) proposes outcome labels and supporting visual evidence, and targeted human review resolves ambiguous cases. These offline labels supervise the compact detectors, avoiding VLM queries during policy learning. For hardware sorting only, annotated world-model rollouts augment the recorded videos to cover observations encountered in neural simulation. The other reward models use recorded task data.

**中文:** 我们基于 VideoMAE（Tong et al., 2022）训练紧凑的成功检测器，在 RL 过程中提供奖励。对于物理视频，视觉语言模型（VLM）提出结果标签及支撑性的视觉证据，有针对性的人工复核则解决有歧义的情况。这些离线标签用于监督紧凑检测器，从而避免在策略学习过程中调用 VLM。仅针对硬件分拣，已标注的世界模型 rollout 会对已录制的视频进行增广，以覆盖神经仿真中遇到的观测。其他奖励模型使用已录制的任务数据。

<a id="S1712"></a>
**Source:** p.94 S1712

**Original:** Success is defined by the requested instruction: choosing the wrong object or destination is a negative outcome.

**中文:** 成功由所请求的指令定义：选错物体或目的地属于负面结果。

<a id="S1713"></a>
**Source:** p.95 S1713

**Original:** We use task-specific detectors, including instruction-specific outputs for joint hardware sorting. RoboLab provides native success labels, while physical-task labels use recorded outcomes and reviewed visual evidence. The detector and its task-specific decision rule remain fixed during RL. Final policy evaluation uses native RoboLab outcomes and physical execution, independently of the learned reward model.

**中文:** 我们使用面向具体任务的检测器，其中包括用于联合硬件分拣的指令特定输出。RoboLab 提供原生成功标签，物理任务的标签则使用已录制的结果及经复核的视觉证据。在 RL 过程中，检测器及其面向具体任务的判定规则保持固定。最终的策略评测使用 RoboLab 原生结果和物理执行结果，且与学习得到的奖励模型相互独立。

<a id="S1714"></a>
**Source:** p.95 S1714

**Original:** Policy optimization. We apply the clipped transition-level policy optimization principle of Sec. F.1.1 to interaction with a fixed learned environment. We collect groups of attempts from the same recorded reset context and score them with the learned success detector. The neural-simulation experiments use Flow-SDE (Liu et al., 2025) for stochastic action denoising, while the physical-RL recipe uses CPS. Both provide tractable transition densities for likelihood-ratio updates.

**中文:** 策略优化。我们将 Sec. F.1.1 中的截断式转移级策略优化原则，应用于与固定学习环境的交互。我们从同一条已录制的重置上下文中采集多组尝试，并用学习得到的成功检测器对其打分。神经仿真实验使用 Flow-SDE（Liu et al., 2025）进行随机动作去噪，而物理 RL 配方使用保系数采样（CPS）。两者都为似然比更新提供了可计算的转移密度。

<a id="S1715"></a>
**Source:** p.95 S1715

**Original:** We optimize a clipped likelihood-ratio objective on selected action-denoising transitions. For each selected transition, we store the sampled latent input and output, denoising index, conditioning inputs, and behaviorpolicy probability. During optimization, we replay the same transition and recompute its probability under the current parameters with gradients enabled. The sampled transition and noise schedule remain fixed, so the likelihood ratio compares the two policies on the same sampled event.

**中文:** 我们在选定的动作去噪转移上优化一个截断似然比目标。对于每个选定的转移，我们存储采样得到的潜变量输入与输出、去噪索引、条件输入以及行为策略概率。在优化过程中，我们重放同一转移，并在开启梯度的情况下，用当前参数重新计算其概率。采样得到的转移与噪声调度保持固定，因此似然比是在同一个采样事件上比较两个策略。

<a id="S1716"></a>
**Source:** p.95 S1716

**Original:** Consistent replay is necessary because numerical differences can produce an apparent policy change before any update. We disable dropout, preserve positional-encoding precision, and check rollout and replay logprobabilities under unchanged weights before the first optimizer update. Activation checkpointing reduces memory use during backpropagation through the joint world-action model described in Sec. F.1.1. The likelihood ratio scores the selected action transition, with no separate video-likelihood objective or learned critic. In the physical-task recipe, we compute the actor loss using actions up to and including the first chunk in which success is confirmed. Later actions are excluded.

**中文:** 保持重放一致是必要的，因为数值差异可能在任何更新之前就产生看似存在的策略变化。我们关闭随机丢弃（dropout），保留位置编码的精度，并在第一次优化器更新之前，在权重不变的情况下检查 rollout 与重放的对数概率。激活值检查点（activation checkpointing）降低了在 Sec. F.1.1 中所述的联合世界-动作模型上进行反向传播时的内存占用。似然比只对所选的动作转移进行评分，不使用单独的视频似然目标，也不使用学习得到的评论者（critic）。在物理任务配方中，我们使用直到并包含首个确认成功的动作块为止的动作来计算 actor 损失，之后的动作则被排除在外。

<a id="S1717"></a>
**Source:** p.95 S1717

**Original:** Policy Improvement in RoboLab. We evaluate task success using native RoboLab outcomes, independently of the learned world model and reward model. Fig. 50 compares the SFT policy with the policy obtained by joint RL from that initialization. Each policy is evaluated for 500 episodes per task, or 5,000 episodes in total, using matched observation and action settings and full task horizons. Mean success increases from 51.32% to 70.88%, a gain of 19.56 percentage points.

**中文:** RoboLab 中的策略改进。我们使用 RoboLab 原生结果评估任务成功情况，且与学习得到的世界模型和奖励模型相互独立。Fig. 50 比较了 SFT 策略与从同一初始化出发经联合 RL 得到的策略。每个策略在每个任务上评估 500 个回合，总计 5,000 个回合，观测与动作设置一致，并使用完整的任务时限。平均成功率从 51.32% 提高到 70.88%，提升 19.56 个百分点。

<a id="S1718"></a>
**Source:** p.95 S1718

**Original:** Batch and group size. Sparse rewards connect exploration to optimization: a larger group can reveal a return difference that a smaller group misses. In RoboLab, we compare (𝐵, 𝐺) = (512, 8) and (1536, 24), where 𝐵is the number of trajectories collected per round and 𝐺the number of attempts per reset group. Both recipes collect 64 groups and perform four optimizer updates per round.

**中文:** 批量与分组大小。稀疏奖励将探索与优化联系在一起：较大的分组可能揭示较小分组会遗漏的回报差异。在 RoboLab 中，我们比较了 (𝐵, 𝐺) = (512, 8) 与 (1536, 24)，其中 𝐵 为每轮采集的轨迹数，𝐺 为每个重置分组中的尝试次数。两种配方都采集 64 个分组，并在每轮执行四次优化器更新。
