# 从零构建大模型
本仓库是记录了学习斯坦福大学CS336的学习笔记

课程主页https://cs336.stanford.edu/spring2025/

## 学习目标
本课程主要是讲解如何从0构建一个大模型

相比较我之前看的那本Build a large language model from scratch,这个课程看起来更加的全面，包括说像GPU、分布式运算、moe架构等等，并且作业的代码量也很多

因此，本课程对于我来说，主要是想学习大模型的底层原理，以及对应的代码实现。因为学习的原则（凡事不能动手搓出来的，就说明还没有理解透彻）。

此外，出于面试的角度考虑，对于大模型算法岗的一些面试要求，比如手写moe，手写一些loss，以及手写mha等等，在这门课如此大的作业量下，如果高质量完成后，相信足以应对这些面试中设计到模型本身的手撕了

## 课程大纲
**Basics (基础)**

Tokenization (分词)

Architecture (架构)

Loss function (损失函数)

Optimizer (优化器)

Learning rate (学习率)

**Systems (系统)**

Kernels (内核)

Parallelism (并行)

Quantization (量化)

Activation checkpointing (激活检查点)

CPU offloading (CPU 卸载)

Inference (推理)

**Scaling laws (缩放定律)**

Scaling sequence (缩放序列)

Model complexity (模型复杂度)

Loss metric (损失度量)

Parametric form (参数形式)

**Data (数据)**

Evaluation (评估)

Curation (策展/筛选)

Transformation (转换)

Filtering (过滤)

Deduplication (去重)

Mixing (混合)

**Alignment (对齐)**

Supervised fine-tuning (监督微调)

Reinforcement learning (强化学习)

Preference data (偏好数据)

Synthetic data (合成数据)

Verifiers (验证器)


一共有5个部分，一共部分一个作业
