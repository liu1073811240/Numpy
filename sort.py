import numpy as np

a = np.array([2, 3, 5, 2, 3, 5])
print(a)

b = np.sort(a)
print(b)

c = -np.sort(-a)
print(c)

d = a[::-1]  # 倒着输出，一次输出一个
print(d)


a1 = np.array([[8, 3, 4], [5, 6, 2]])
print(a1)
b1 = np.sort(a1)  # 默认以最后一轴从小到大排序
b2 = np.sort(a1, 0)
print(b1)
print(b2)

c1 = -np.sort(-a1)  # 元素从大到小排序
print(c1)
d1 = a1[::-1]
print(d1)
