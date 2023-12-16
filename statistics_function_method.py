import numpy as np

a = np.arange(0, 24, dtype="float16").reshape(4, 6)
print(a, type(a))
a[2] = 0
a[[0, 1, 1, 2], [1, 2, 4, 4]] = np.nan
print(a, a.dtype)

print("*"*35)

# statistical functions/methods
sum_all = np.sum(a)
sum_0 = np.sum(a, axis=0)
sum_1 = a.sum(axis=1)  # 指定axis,否则统计整个数组
print(sum_all, "\n", sum_0, "\n", sum_1)

print("*"*35)  # nan和任何值计算都为nan

a_max = a.max()
a_min_0 = a.min(axis=0)
a_median_0 = np.median(a, axis=0)
a_ptp_0 = np.ptp(a, axis=0)  # 跨行求极差
a_mean_1 = a.mean(axis=1)  # 跨列求均值
print(a_max, a_min_0, a_median_0, a_ptp_0, a_mean_1)
