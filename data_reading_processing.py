import numpy as np

file_path = "D:/pycharm/big_data/xor_dataset.csv"

# data reading
data1 = np.loadtxt(fname=file_path, dtype="float16", delimiter=",", unpack=False)
    # loadtxt读取数据,fname-文件位置,dtype-数据类型,delimiter-分隔符
    # skiprows,usecols,unpack-是否转置(布尔值)

data2 = np.loadtxt(fname=file_path, dtype="float32", delimiter=",", unpack=True)

print(data1)
print(data2)

print("*"*35)

# data slicing
a1 = data1[2]  # 一行
a2 = data1[2:]  # 连续多行
a3 = data1[[2, 4, 6]]  # 不连续多行
print(a1, "\n", a2, "\n", a3)

print("*"*35)

b1 = data2[:, 0]  # 第一列
b2 = data2[:, 1:]  # 连续多列
b3 = data2[:, [0, 2, 7]]  # 不连续多列
print(b1, "\n", b2, "\n", b3)

print("*"*35)

c1 = data1[0, 1]  # 第一行第二列
c2 = data2[1:, 0:3]  # 多行多列
c3 = data2[[0, 1, 2], [1, 3, 7]]  # 多个不相邻的点
print(c1, type(c1), "\n", c2, type(c2), "\n", c3)
print(c2.shape[0], c2.shape[1])

# data modifying
c2[1, 2] = 0  # 索引后直接重新赋值修改
print(c2)
c2[c2 == 0] = 1  # 布尔索引
print(c2)

print("*"*35)

d = np.arange(0, 20).reshape(4, 5)
print(d)
d1 = np.where(d > 10, 1, 0)  # 三元运算符
d2 = np.clip(d, 7, 9)  # clip裁剪，等号取不取无所谓
print(d1)
print(d2)
