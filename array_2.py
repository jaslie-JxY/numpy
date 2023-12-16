import numpy as np

# 数组的形状,ndarray的shape属性
a = np.array(range(6))
print(a, a.shape)  # 一维 axis-0
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b, b.shape)  # 二维 axis-0,1
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c, c.shape)  # 三维 axis-0,1,2

print("*" * 35)

# reshape方法修改数组形状
a1 = a.reshape(2, 3)
print(a, a1, type(a1))  # reshape方法有return返回值
b1 = np.array(range(24)).reshape(2, 3, 4)  # 2块(层)3行4列
print(b1, b1.dtype)

print("*" * 35)

# 数组展开为一维
a2 = a1.reshape((a1.shape[0] * a1.shape[1]),)  # 行*列
print(a1, a2)
a3 = a1.reshape(-1,)  # 酱紫也行
print(a3)
b2 = b1.flatten()
print(b1, b2)
b3 = b1.reshape(-1,)
print(b3)

# 数组与数计算,广播原则
a + 1
a - 1
a * 3
a / 3
print(a / 0)  # nan and inf

# 数组与数组计算,对应计算
b + c

# 数组转置
array = np.array(range(0, 8)).reshape(2, 4)
print(array, "\n******\n", array.transpose(), "\n*******\n", array.T)
