import numpy as np

# 交换轴
a = np.arange(24).reshape([2, 3, 4])
b = a.T
c = np.transpose(a, [2, 1, 0])
d = a.transpose(1, 0, 2)
e = np.swapaxes(a, 0, 2)
f = a.swapaxes(0, 1)

# print(a.shape)
# print(b.shape)
# print(c.shape)
# print(d.shape)
# print(e.shape)
# print(f.shape)

# print(np.add(a, a))

a1 = np.arange(12).reshape([3, 2, 2])
# print(a1)
# 每个轴对应元素求和
# print(np.sum(a1, axis=2))
# print(np.mean(a1, axis=2))

a2 = np.array([[1, 10], [5, 9]])
b2 = np.array([[8, 3], [6, 7]])
print(a2)
print(b2)
# 取最大值
# print(np.max(a2, 0))
# print(np.max(a2, 1))
# 取最大值的索引
# print(np.argmax(a2, 0))

# 两个数组对应元素取最大、最小的，组成新的数组
print(np.maximum(a2, b2))
print(np.minimum(a2, b2))

print("-----------")

m = np.array([1, 2, 3, 5, 6, 2, 56, 9, 6, ])
n = np.where(m > 3)
print(n)

# 表示合格的使用一个数代替，不合格的使用另一个数代替， 用来分类
p = np.where(m > 3, 1, 0)
print(p)

# 求精度
print(np.sum(p) / len(m))

