# 高性能计算机示例

## PVP

### Cray 系列

- Cray XMP
  - 年代：1982
  - 最高配置的峰值效率：`0.235 GFlop` x 4
- Cray YMP
  - 年代：1988
  - 最高配置的峰值效率：`0.333 GFlop` x 8
- Cray C90
  - 年代：1991
  - 最高配置的峰值效率：`1 GFlop` x 16
- Cray T90
  - 年代：1995
  - 最高配置的峰值效率：`1.8 GFlop` x 32

### 其他 PVP

- 银河一号
  - 年代：1983
  - 峰值效率：不低于 `0.1GHz`(每秒一亿次计算)

- NEC SX-3/44
  - 年代：1992
  - 峰值效率： `22 GFLOPS` (Top500 1993-06)

## Cluster

- Top500 中有很多
- 天河二号：
  - 年代：2013
  - 峰值效率：`54.9 PFLOPS`
- NVIDIA DGX SuperPOD
  - 年代：2019
  - 峰值效率：`55.81 PFLOPS`
- 微软 Azure Eagle：
  - 年代：2023
  - 性能：`561.2 PFLOPS`

## MPP（我觉得包含 SMP 和 CC-NUMA）

- Cray T3E-900（NCC-NUMA）
  - 年代：1996
  - 峰值效率：`900 MFLOPS`
- IBM Blue Gene/P （SMP）
  - 年代：2007
  - 峰值效率：`1.02 PFLOPS`
- Fujitsu K Computer（Tofu 互连）
  - 年代：2011
  - 峰值效率：`10.5 PFLOPS`
- Fugaku（CC-NUMA）
  - 年代：2021
  - 峰值效率：`537 PFLOPS`
- Summit（结合了 SMP 和 CC-NUMA）
  - 年代：2018
  - 峰值效率：`200 PFLOPS`
- 神威太湖之光（CC-NUMA）
  - 年代：2016
  - 峰值效率：`93 PFLOPS`
- 天河一号（MPP）
  - 年代：2009
  - 峰值效率：`1.87 PFLOPS`

## SIMD 指令集示例

- Intel AVX 指令集
  - 年代：2011
  - 提供了 256 位向量运算寄存器
  - 性能提升假设：不超过 8 倍
- Intel AVX-512 指令集
  - 年代：2013
  - 提供了 512 位的 SIMD 寄存器
  - 性能提升假设：不超过 16 倍
  - 现实案例：Intel® Xeon Phi™ Processor 7210
    - 年代：2016
    - 主频：`1.30 GHz`
- ARM Neon 指令集
  - 年代：2008
  - 出现自 ARMv7
  - 提供了 128 位向量运算寄存器
  - 性能提升假设：不超过 4 倍
  - 现实案例：Cortex-A7
    - 年代：2011
    - 主频：`1.2GHz~1.6GHz`
- CUDA 与 OpenCL 等编程模型
  - 年代：2006
  - 现实案例：NVIDIA Tesla K80
    - 年代：2014
    - 峰值性能：`8.74 TFLOPS`

