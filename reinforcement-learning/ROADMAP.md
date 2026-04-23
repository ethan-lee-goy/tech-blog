# 强化学习学习路线图

## 第一部分：基础理论（已完成）

### 第 1 章 强化学习入门
- 1.1 什么是强化学习
- 1.2 强化学习的基本要素
- 1.3 强化学习与其他机器学习范式的区别
- 1.4 强化学习的应用场景
- 1.5 强化学习的挑战

### 第 2 章 马尔可夫决策过程（MDP）
- 2.1 马尔可夫性质
- 2.2 马尔可夫决策过程的定义
- 2.3 回报与价值函数
- 2.4 贝尔曼方程
- 2.5 最优策略与最优价值函数

### 第 3 章 有模型与无模型强化学习
- 3.1 有模型强化学习（动态规划）
  - 策略迭代
  - 价值迭代
- 3.2 无模型强化学习
  - 蒙特卡洛方法
  - 时序差分方法（SARSA, Q-Learning）
  - 同策略与异策略
  - 多步时序差分与 TD(λ)

---

## 第二部分：函数近似与深度强化学习基础

### 第 4 章 函数近似
- 4.1 从表格方法到函数近似
- 4.2 线性函数近似
- 4.3 非线性函数近似
  - 神经网络基础
  - 深度学习在 RL 中的应用
- 4.4 函数近似的挑战
  - 致命三角（Deadly Triad）
  - 发散问题

### 第 5 章 深度 Q 网络（DQN）
- 5.1 从 Q-Learning 到 DQN
- 5.2 DQN 的核心技术
  - 经验回放（Experience Replay）
  - 目标网络（Target Network）
- 5.3 DQN 的改进算法
  - Double DQN
  - Dueling DQN
  - Prioritized Experience Replay
  - Rainbow DQN
- 5.4 DQN 的实现与调试技巧

---

## 第三部分：策略梯度方法

### 第 6 章 策略梯度基础
- 6.1 策略梯度定理
- 6.2 REINFORCE 算法
- 6.3 基线函数（Baseline）
- 6.4 策略梯度的方差问题

### 第 7 章 Actor-Critic 方法
- 7.1 Actor-Critic 架构
- 7.2 优势函数（Advantage Function）
- 7.3 A2C（Advantage Actor-Critic）
- 7.4 A3C（Asynchronous Advantage Actor-Critic）
- 7.5 GAE（Generalized Advantage Estimation）

### 第 8 章 信赖域与自然梯度方法
- 8.1 策略优化的挑战
- 8.2 TRPO（Trust Region Policy Optimization）
  - KL 散度约束
  - 共轭梯度法
- 8.3 自然策略梯度（Natural Policy Gradient）
- 8.4 PPO（Proximal Policy Optimization）
  - PPO-Clip
  - PPO-Penalty
  - PPO 的实现技巧

---

## 第四部分：连续控制

### 第 9 章 确定性策略梯度
- 9.1 DPG（Deterministic Policy Gradient）
- 9.2 DDPG（Deep Deterministic Policy Gradient）
  - Actor-Critic 架构
  - Ornstein-Uhlenbeck 噪声
- 9.3 TD3（Twin Delayed DDPG）
  - Clipped Double Q-Learning
  - 延迟策略更新
  - 目标策略平滑

### 第 10 章 最大熵强化学习
- 10.1 熵正则化
- 10.2 Soft Q-Learning
- 10.3 SAC（Soft Actor-Critic）
  - 自动温度调节
  - 重参数化技巧
- 10.4 SAC 的应用与调优

---

## 第五部分：模型基础强化学习

### 第 11 章 模型学习
- 11.1 世界模型（World Models）
- 11.2 Dyna 架构
  - Dyna-Q
  - Dyna-2
- 11.3 模型预测控制（MPC）
- 11.4 想象增强智能体（I2A）

### 第 12 章 现代模型基础方法
- 12.1 MBPO（Model-Based Policy Optimization）
- 12.2 PETS（Probabilistic Ensembles with Trajectory Sampling）
- 12.3 Dreamer 系列
  - Dreamer v1
  - Dreamer v2
  - Dreamer v3
- 12.4 MuZero
  - 学习隐式模型
  - MCTS 与神经网络结合

---

## 第六部分：前沿主题

### 第 13 章 离线强化学习（Offline RL）
- 13.1 离线 RL 的动机与挑战
- 13.2 分布偏移问题
- 13.3 保守 Q-Learning（CQL）
- 13.4 行为克隆与 RL 的结合
  - BCQ（Batch-Constrained Q-Learning）
  - BEAR
- 13.5 Decision Transformer
  - 序列建模视角
  - Trajectory Transformer

### 第 14 章 多智能体强化学习（MARL）
- 14.1 多智能体系统基础
- 14.2 独立学习 vs 联合学习
- 14.3 QMIX 与 VDN
- 14.4 MADDPG
- 14.5 通信与协作机制

### 第 15 章 分层强化学习（HRL）
- 15.1 Options 框架
- 15.2 封建强化学习（Feudal RL）
- 15.3 HAC（Hierarchical Actor-Critic）
- 15.4 HIRO（Data Efficient Hierarchical RL）

### 第 16 章 元强化学习与迁移学习
- 16.1 元学习基础
- 16.2 MAML（Model-Agnostic Meta-Learning）
- 16.3 RL²（Fast RL via Slow RL）
- 16.4 领域随机化
- 16.5 迁移学习策略

### 第 17 章 逆强化学习与模仿学习
- 17.1 逆强化学习（IRL）
  - 最大熵 IRL
  - 最大边际 IRL
- 17.2 模仿学习
  - 行为克隆（BC）
  - DAgger
- 17.3 GAIL（Generative Adversarial Imitation Learning）
- 17.4 从人类反馈中学习（RLHF）
  - Reward Modeling
  - PPO-RLHF（ChatGPT 背后的技术）

---

## 第七部分：探索与奖励设计

### 第 18 章 探索策略
- 18.1 探索-利用权衡
- 18.2 ε-贪心与 Softmax
- 18.3 UCB（Upper Confidence Bound）
- 18.4 Thompson 采样
- 18.5 内在动机
  - 好奇心驱动（Curiosity-Driven）
  - ICM（Intrinsic Curiosity Module）
  - RND（Random Network Distillation）
- 18.6 Count-Based 探索

### 第 19 章 奖励塑形与课程学习
- 19.1 奖励塑形（Reward Shaping）
- 19.2 稀疏奖励问题
- 19.3 HER（Hindsight Experience Replay）
- 19.4 课程学习（Curriculum Learning）
- 19.5 自动课程生成

---

## 第八部分：实践与应用

### 第 20 章 RL 工程实践
- 20.1 超参数调优
- 20.2 调试技巧
- 20.3 可复现性
- 20.4 常用 RL 库
  - Stable-Baselines3
  - RLlib
  - CleanRL
- 20.5 分布式训练

### 第 21 章 应用案例
- 21.1 游戏 AI
  - Atari 游戏
  - AlphaGo / AlphaZero
  - Dota 2 / StarCraft II
- 21.2 机器人控制
  - 机械臂操作
  - 四足机器人
- 21.3 自动驾驶
- 21.4 推荐系统
- 21.5 资源调度与优化
- 21.6 金融交易

---

## 第九部分：理论基础（选修）

### 第 22 章 RL 理论
- 22.1 遗憾界（Regret Bounds）
- 22.2 样本复杂度
- 22.3 PAC-MDP 框架
- 22.4 收敛性分析
- 22.5 策略梯度的收敛性

### 第 23 章 安全强化学习
- 23.1 约束 MDP
- 23.2 安全探索
- 23.3 鲁棒性
- 23.4 可解释性

---

## 第十部分：2024-2025 年最新进展 🔥

### 第 22 章 基础模型时代的强化学习

#### 22.1 大语言模型与 RL 的深度融合
- **LLM as Agent**
  - ReAct（Reasoning + Acting）
  - Reflexion（自我反思机制）
  - AutoGPT 与 Agent 框架
  
- **LLM for Reward Modeling**
  - 使用 LLM 作为奖励函数
  - Constitutional AI（Anthropic）
  - RLAIF（RL from AI Feedback）
  
- **In-Context Reinforcement Learning**
  - Transformer 的上下文学习能力
  - Algorithm Distillation
  - Prompt-based RL

#### 22.2 超越 RLHF 的对齐方法
- **DPO（Direct Preference Optimization）** ⭐
  - 无需显式奖励模型
  - 直接从偏好数据优化策略
  - 比 PPO-RLHF 更简单高效
  
- **IPO（Identity Preference Optimization）**
  - 改进 DPO 的正则化
  - 更好的理论保证
  
- **KTO（Kahneman-Tversky Optimization）**
  - 基于前景理论
  - 只需要二元反馈（好/坏）
  
- **ORPO（Odds Ratio Preference Optimization）**
  - 单阶段对齐
  - 无需 SFT 预训练

#### 22.3 多模态决策模型
- **Vision-Language-Action Models**
  - RT-1（Robotics Transformer 1）
  - RT-2（结合 VLM 的机器人控制）
  - RT-X（跨机器人泛化）
  
- **PaLM-E**
  - 具身多模态语言模型
  - 视觉-语言-动作统一建模
  
- **Octo**
  - 开源的通用机器人策略
  - 大规模机器人数据预训练

### 第 23 章 扩散模型在 RL 中的应用

#### 23.1 扩散策略（Diffusion Policy）
- **基本原理**
  - 将动作生成建模为扩散过程
  - 多模态动作分布
  - 避免模式崩溃
  
- **Diffusion-QL**
  - 离线 RL + 扩散模型
  - 更好的行为克隆
  
- **Decision Diffuser**
  - 轨迹级别的扩散
  - 规划与生成的统一

#### 23.2 扩散世界模型
- **GENIE（Generative Interactive Environments）**
  - 从视频学习可交互世界模型
  - 无监督学习动作空间
  
- **Video Diffusion for Planning**
  - 使用视频生成模型进行规划
  - 想象未来轨迹

### 第 24 章 新一代世界模型

#### 24.1 Transformer-based 世界模型
- **IRIS（Imagine, Reason, and Interact in Symbolic Space）**
  - 离散符号空间的世界模型
  - 更高效的推理
  
- **TWM（Transformer World Models）**
  - 纯 Transformer 架构
  - 长期依赖建模

#### 24.2 视频生成模型用于决策
- **Sora 与决策**
  - 视频生成模型的决策潜力
  - 物理世界的模拟器
  
- **UniSim**
  - 统一的世界模拟器
  - 多任务泛化

### 第 25 章 开源生态与工具链的演进

#### 25.1 新一代 RL 库
- **Gymnasium（OpenAI Gym 的继任者）**
  - 更好的 API 设计
  - 更多标准环境
  
- **Stable-Baselines3 v2.x**
  - 支持最新算法
  - 更好的文档和示例
  
- **CleanRL 2.0**
  - 单文件实现
  - 易于理解和修改
  
- **TorchRL（Meta）**
  - PyTorch 原生 RL 库
  - 模块化设计

#### 25.2 大规模训练基础设施
- **Ray RLlib 2.x**
  - 分布式训练
  - 支持大规模实验
  
- **Acme（DeepMind）**
  - 研究级 RL 框架
  - 高质量实现
  
- **Sample Factory 2.0**
  - 超高吞吐量训练
  - 适合大规模实验

#### 25.3 新的基准测试环境
- **ManiSkill2**
  - 机器人操作基准
  - 物理仿真
  
- **Isaac Gym / Isaac Lab**
  - GPU 加速的物理仿真
  - 大规模并行训练
  
- **NetHack Learning Environment**
  - 复杂的程序生成环境
  - 长期规划挑战

### 第 26 章 RL 在实际应用中的突破

#### 26.1 大规模语言模型对齐
- **ChatGPT / GPT-4**
  - RLHF 的成功应用
  - 人类偏好学习
  
- **Claude（Constitutional AI）**
  - 基于原则的对齐
  - 减少人工标注
  
- **Llama 2 / Llama 3**
  - 开源 RLHF 实践
  - 社区驱动改进

#### 26.2 具身智能与机器人
- **Figure 01 + OpenAI**
  - 人形机器人 + VLM
  - 自然语言控制
  
- **Tesla Optimus**
  - 端到端学习
  - 大规模数据收集
  
- **1X Technologies**
  - 通用机器人平台
  - 远程操作 + RL

#### 26.3 科学发现
- **AlphaFold 3**
  - 蛋白质结构预测
  - RL 辅助优化
  
- **GNoME（Graph Networks for Materials Exploration）**
  - 材料发现
  - 220 万新材料预测
  
- **FunSearch（DeepMind）**
  - 使用 LLM 发现数学定理
  - 进化算法 + LLM

#### 26.4 游戏 AI 的新里程碑
- **Cicero（Meta）**
  - 外交游戏（Diplomacy）
  - 自然语言谈判 + 战略规划
  
- **Player of Games**
  - 统一的游戏 AI
  - 完美信息 + 不完美信息游戏

---

## 2024-2025 年关键趋势总结

### 🔥 五大核心趋势

1. **基础模型 + RL 的深度融合**
   - LLM 不再只是工具，而是 RL 的核心组件
   - 从 RLHF 到 DPO，对齐方法持续演进
   - In-context RL 展现出惊人潜力

2. **扩散模型进入 RL 领域**
   - 扩散策略解决多模态动作问题
   - 扩散世界模型用于规划
   - 视频生成模型成为通用模拟器

3. **具身智能的爆发**
   - 机器人学习迎来黄金时代
   - 多模态模型（VLA）成为标配
   - 大规模数据收集与预训练

4. **从 RLHF 到更简单的对齐方法**
   - DPO 系列算法简化训练流程
   - 无需显式奖励模型
   - 更好的理论理解

5. **开源生态的繁荣**
   - Gymnasium 取代 Gym
   - 更多高质量开源实现
   - 社区驱动的算法改进

### 📊 算法演进时间线

```
2023 年：
- DPO 提出（简化 RLHF）
- RT-2（VLM + 机器人）
- Diffusion Policy

2024 年：
- GENIE（可交互世界模型）
- Sora（视频生成）
- Constitutional AI
- KTO, IPO（对齐方法）

2025 年：
- 更多 VLA 模型
- 扩散模型在 RL 中的广泛应用
- 具身智能商业化
```
---

## 附录

### 附录 A：数学基础
- A.1 概率论与统计
- A.2 线性代数
- A.3 优化理论
- A.4 信息论

### 附录 B：深度学习基础
- B.1 神经网络
- B.2 卷积神经网络
- B.3 循环神经网络
- B.4 Transformer

### 附录 C：经典论文列表
- 按主题分类的必读论文

### 附录 D：实验环境
- D.1 Gym / Gymnasium
- D.2 MuJoCo
- D.3 PyBullet
- D.4 Unity ML-Agents
- D.5 Isaac Gym

---

## 学习建议

### 初学者路径（3-6 个月）
1. 第 1-3 章：基础理论
2. 第 4-5 章：DQN
3. 第 6-7 章：策略梯度基础
4. 第 8 章：PPO
5. 第 20 章：实践

### 进阶路径（6-12 个月）
1. 完成初学者路径
2. 第 9-10 章：连续控制
3. 第 11-12 章：模型基础方法
4. 第 13 章：离线 RL
5. 第 17 章：模仿学习与 RLHF
6. 第 21 章：应用案例

### 研究者路径（12+ 个月）
1. 完成进阶路径
2. 第 14-16 章：前沿主题
3. 第 18-19 章：探索与奖励
4. 第 22-23 章：理论基础
5. 阅读最新论文，复现 SOTA 算法

---

## 参考资源

### 经典教材
- Sutton & Barto: Reinforcement Learning: An Introduction (2nd Edition)
- Csaba Szepesvári: Algorithms for Reinforcement Learning
- Dimitri Bertsekas: Dynamic Programming and Optimal Control

### 在线课程
- David Silver's RL Course (DeepMind)
- CS285: Deep Reinforcement Learning (UC Berkeley)
- Spinning Up in Deep RL (OpenAI)

### 论文资源
- arXiv.org (cs.LG, cs.AI)
- NeurIPS, ICML, ICLR 会议论文
- JMLR, TMLR 期刊

### 代码资源
- Stable-Baselines3: https://github.com/DLR-RM/stable-baselines3
- CleanRL: https://github.com/vwxyzjn/cleanrl
- RLlib: https://docs.ray.io/en/latest/rllib/

---

### 🎯 学习建议更新

#### 如果你是初学者（2024-2025 版）
1. 第 1-3 章：经典基础（必学）
2. 第 4-8 章：深度 RL 核心（DQN, PPO）
3. **第 17 章：RLHF 与 DPO**（新增重点）⭐
4. **第 22 章：LLM + RL**（了解前沿）
5. 第 20 章：工程实践

#### 如果你想从事 LLM 对齐
1. 掌握基础 RL（第 1-3 章）
2. 策略梯度方法（第 6-8 章，重点 PPO）
3. **RLHF 完整流程**（第 17 章）
4. **DPO 及其变体**（第 22 章）⭐
5. 实践：微调开源 LLM

#### 如果你想从事机器人学习
1. 基础 RL + 连续控制（第 1-10 章）
2. 模仿学习（第 17 章）
3. **多模态模型**（第 22 章）⭐
4. **扩散策略**（第 23 章）⭐
5. 实践：ManiSkill2, Isaac Gym

#### 如果你是研究者
- 关注第 22-24 章的最新进展
- 阅读 2024-2025 年顶会论文（NeurIPS, ICML, ICLR, CoRL）
- 复现 SOTA 算法
- 探索未解决的问题

---

## 重要论文列表（2024-2025）

### 对齐方法
- **DPO**: Direct Preference Optimization (NeurIPS 2023)
- **IPO**: A General Theoretical Paradigm to Understand Learning from Human Preferences (2024)
- **KTO**: Model Alignment as Prospect Theoretic Optimization (2024)
- **ORPO**: Monolithic Preference Optimization without Reference Model (2024)

### 多模态与具身智能
- **RT-2**: Vision-Language-Action Models (2023)
- **PaLM-E**: An Embodied Multimodal Language Model (2023)
- **Octo**: An Open-Source Generalist Robot Policy (2024)

### 扩散模型
- **Diffusion Policy**: Visuomotor Policy Learning via Action Diffusion (2023)
- **GENIE**: Generative Interactive Environments (2024)
- **Decision Diffuser**: Diffusion Models for Offline RL (2023)

### 世界模型
- **IRIS**: Transformers are Sample-Efficient World Models (2023)
- **TWM**: Transformer World Models (2024)

### 应用突破
- **Cicero**: Human-Level Play in Diplomacy (2022)
- **AlphaFold 3**: Accurate Structure Prediction (2024)
- **GNoME**: Discovering New Materials (2023)

---
