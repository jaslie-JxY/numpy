import numpy as np

# data reading
file_path = "D:/pycharm/big_data/xor_dataset.csv"

data = np.loadtxt(fname=file_path, delimiter=",", dtype="float16")
print(data)  # np.loadtxt不直接支持读取指定的行
data_1 = data[:10]
data_2 = data[10:17]
print(data_1, "\n", data_2)

# 创建标签数组
label_1 = np.ones((data_1.shape[0], 1))
label_2 = np.zeros((data_2.shape[0], 1)) + 2

# horizontal splicing
data_1 = np.hstack((label_1, data_1))
data_2 = np.hstack((label_2, data_2))

# vertical splicing
data_1_2 = np.vstack((data_1, data_2))
print("\n", data_1_2)
