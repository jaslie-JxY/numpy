import numpy as np
import random

# 使用numpy生成数组---ndarray数据结构
a = np.array([1, 2, 3, 4, 5])
b = np.array(range(1, 6))
c = np.arange(1, 6, 2)

print(a, b, c)
print(type(a), type(b), type(c))
print(c.dtype)  # ndarray属性-数组中元素的数据类型

print("*"*35)

# 设定函数的dtype参数,指定ndarray的dtype属性
a1 = np.array([1.1, 3.3, 5.5, 7.7, 9.9], dtype="float16")
print(a1, a1.dtype)
b1 = np.array(range(1, 8, 1), dtype="int8")
print(b1, b1.dtype)
c1 = np.arange(1, 9, 3, dtype="i1")
print(c1, c1.dtype)
d1 = np.array([1, 0, 0, 1, 1], dtype="bool")
print(d1, d1.dtype)

print("*"*35)

# 利用astype方法调整dtype属性
a2 = a1.astype("int8")
print(a2, a2.dtype)

print("*"*35)

# ndarray中的小数
a3 = np.array([random.random() for i in range(6)])
print(a3, a3.dtype)
b3 = np.round(a3, 2)  # 四舍五入
print(b3, b3.dtype)  # 显示浮点数时会默认省略末尾的0
