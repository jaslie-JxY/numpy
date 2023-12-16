import numpy as np

# np.nan != np.nan
a = np.array(range(0, 20), dtype="float16").reshape(4, 5)
print(a, type(a))
a[(a < 7) | (a > 17)] = np.nan  # 应用逻辑或|而非or,type(nan)=float
print(a, type(np.nan))
a[:, 0] = 0
print(a)
num_nonzero = np.count_nonzero(a)  # 非0元素个数
print("num_nonzero=", num_nonzero)
num_nan = np.count_nonzero(a != a)  # nan个数
print("num_non=", num_nan)
num_nan = np.count_nonzero(np.isnan(a))
print(np.isnan(a), "\n", "num_nan=", num_nan)

print("*" * 35)


# replace nan with the mean
# 按列处理 定义函数
def nan_replace(array):
    for i in range(array.shape[1]):
        temp_col = array[:, i]
        num = np.count_nonzero(temp_col != temp_col)  # 求解列中nan元素个数
        if num != 0:
            temp_col[np.isnan(temp_col)] = temp_col[temp_col == temp_col].mean()
        # array[:, i] = temp_col  # temp_col是array的一个视图(view),而不是副本(copy)
    return array


b = np.arange(0, 30).reshape(5, 6).astype("float16")
b[2, :3] = np.nan
b[3, 4:] = np.nan
print(b, type(b))
b = nan_replace(b)
print(b)
