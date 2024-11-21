​	

# 如何完成 HPC 课程报告

## -1. TL;DR



## 0. 老师给出的内容大纲

> - 主题 2 高性能计算机体系结构模型
>   - 2.1. 分类/总体架构
>   - 2.2. 单指令多数据流 SIMD
>     - 2.2.1. Vector Pipelined 向量流水计算机
>     - 2.2.2. Processor Array SIMD 阵列机
>   - 2.3. 多指令多数据流 MIMD
>     - 2.3.1. 共享存储型（SMP、CC-NUMA）
>     - 2.3.2. 分布式存储（并行向量处理机 Vector、大规模并行处理机 MPP、机群 Cluster）
>   - 2.4. 参考文献

## 1. 如何合作

1. **个人列举了一些分工相关的内容，可能不科学，欢迎各位批评建议，仅供参考。**
2. 所有组员参与文献收集，你收集了那部分对应的文献，最后就把你的工作量写到哪栏（**换言之我们不会提到这章内容具体是谁写的**）。
3. 欢迎大家自愿参与报告编写与 PPT 制作，纯自愿，不会算到最终工作量里，助力大家轻松划水。
   1. 最终报告的参加也是纯自愿，想来参加的我们就讨论下报告时的分工。

## 2. 需要确定的信息

1. 各种处理机架构的**提出时间**、**代表性论文**、**现实世界中哪些机器隶属于这个架构**（例子）、以及它们各自**大概的结构图**、**大概的运算效率**如何（FLOPS 或者 MIPS）。
2. 在找现实世界中的机器时优先找 Top 500 中的相关例子，例子多多益善，给不出结构图没关系，有相关的介绍性文献即可。
3. 分析各类计算机结构目前常用的领域、分析 Top500 计算机中给类计算机的占比、尽可能分析这种现象产生的历史原因。（这个写报告时候考虑即可，应该会很难考虑）。

### 3. 任务划分

关于资料收集：

1. 资料收集：收集 SIMD：Vector Pipelined 与 Processor Array SIMD 的相关资料。
2. 资料收集：收集 SMP 与 CC-NUMA 的相关资料。
3. 资料收集：收集 MIMD：并行向量处理机 Vector 的相关资料。
4. 资料收集：收集 MIMD：大规模并行处理机 MPP、机群 Cluster 的相关资料。
5. 制作 PPT 以及用于提交的汇报文档。（自愿参与）

## 4. 报告中计划要有哪些内容

### 1. 分类与总体架构

- 这里最好能给出**多个常见的分类维度**，具体还得再想想。
- 对比 SIMD 和 MIMD 的架构设计，放点结构图。评论一下各自的优劣。最好引用一下弗林分类法的原始论文。
  - 弗林分类法：[very-high-speed-computing-systems-flynn.pdf](./doc/very-high-speed-computing-systems-flynn.pdf)
- 抄谁：
  - 【知乎】计算机体系结构：SIMD：https://zhuanlan.zhihu.com/p/651044595
  - 【CSDN】SIMD、SIMD、SIMT、MISD、MIMD详解与比较：https://blog.csdn.net/tabactivity/article/details/90236460

### 2. SIMD

- 抄谁：
  - Computer Architecture: SIMD/Vector/GPU：https://course.ece.cmu.edu/~ece740/f13/lib/exe/fetch.php%3Fmedia=seth-740-fall13-module5.1-simd-vector-gpu.pdf
  - Array Processor in Computer Architecture：https://binaryterms.com/array-processor-in-computer-architecture.html

### 3.MIMD

- 抄谁：
  - ~~MIMD 是什么？：https://zhuanlan.zhihu.com/p/645392338~~（不符合主旨）
  - 关于共享存储模型：UMA/NUMA/COMA/CC-NUMA/NORMA：https://pop0726.github.io/bxjs/text/ch02/se01/r2_1_5.htm
  - 并行多核体系结构概述：https://zhuanlan.zhihu.com/p/586274438
  - 未完待续

### 4. 历史性评述

- 这个看看到时候能编成啥样，在各个章节中应该最好都放点穿插。

