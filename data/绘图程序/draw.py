import matplotlib.pyplot as plt

PVP        = 'red'
MPP_SMPH   = 'orange'
MPP_NUMA   = 'yellow'
CLUSTER    = 'green'

# 示例数据
year_list   = [      1982,       1988,       1991,       1991,          1991]
gflops_list = [   0.235*4,    0.333*8,       1*16,     1.8*32,            22]
colors_list = [       PVP,        PVP,        PVP,        PVP,           PVP]
labels_list = ["Cray XMP", "Cray YMP", "Cray C90", "Cray T90", "NEC SX-3/44"]

year_list   += [           2009,            2018,             2023,            2024]
gflops_list += [563.1 * (10**3), 61.44 * (10**6), 121.40 * (10**6), 561.2 * (10**6)]
colors_list += [        CLUSTER,         CLUSTER,          CLUSTER,         CLUSTER]
labels_list += [     "Tianhe-1",     "Tianhe-2A",       "SuperPOD",         "Eagle"]

year_list   += [          1996,              2008,           2011,             2020,          2018,            2016]
gflops_list += [           0.9,   23.86 * (10**3), 10.5 * (10**6), 422.01 * (10**6), 200 * (10**6), 93.01 * (10**6)]
colors_list += [      MPP_NUMA,          MPP_SMPH,       MPP_NUMA,         MPP_NUMA,      MPP_NUMA,        MPP_NUMA]
labels_list += ["Cray T3E-900", "IBM Blue Gene/P",    "Fujitsu K",         "Fugaku",      "Summit",        "Sunway"]

# 创建散点图
plt.figure(figsize=(8, 6))
for i in range(len(year_list)):
    plt.scatter(year_list[i], gflops_list[i], color=colors_list[i])
    plt.text(year_list[i], gflops_list[i], labels_list[i], fontsize=9)

color_uniq = [  PVP,  MPP_SMPH,  MPP_NUMA,    CLUSTER]
name_uniq  = ["PVP", "MPP/UMA", "MPP/NUMA", "Cluster"]

# 添加图例，唯一标签
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color_uniq[i], markersize=10) for i in range(len(color_uniq))]
plt.legend(handles, name_uniq)

# 设置纵坐标为对数坐标
plt.yscale('log')

# 添加图例
plt.title('')
plt.xlabel('Year')
plt.ylabel('Rmax*/GFLOPS (log scale)')
plt.xlim(1980, 2030)
plt.grid()

# 显示图形
plt.show()