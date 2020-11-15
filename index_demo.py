import numpy as np

# 索引和切片
# 索引会降维（每索引一次，降维一次），切片不会降维
x = np.arange(24).reshape([2, 3, 4])
print(x)
print(x[0])
print(x[0:1])
print(x[1, 1])  # 按照轴的顺序连续取值
print(x[1][1])  # 取完当前轴之后，再在这个基础上取
print(x[1:2, 1:2])
print(x[:, 1])
print(x[0, 1, 2])
print("------")
print(x[1:, 1])
print(x[:, 1:])
print(x[:, :3])


# 花式索引
a1 = np.array([1, 2, 3, 4, 5, 6])
print(np.array([a1[0], a1[1], a1[2]]))
print(np.array([1, 3, 5]))
print(a1[[0, 2, 4]])

a2 = np.array([[3, 5, 9], [4, 2, 1], [6, 3, 7]])
print(a2[[2, 0, 1], [1, 2, 0]])  # 第0轴的索引，第一轴的索引
print(a2[[0, 1, 2], [2, 1, 2]])  # [9 2 7]

print(a2[:1, 1], a2[:1, 2:], a2[1:2, :1])
print([a2[0, 0], a2[0, 2], a2[1, 0]])
print(np.array([a2[0, 0], a2[0, 2], a2[1, 0]]))

print("=======")
a3 = np.array([[3, 5, 9], [4, 2, 1], [6, 3, 7]])
print(a3[[[2, 0], [1, 1]], [[1, 2], [0, 2]]])  # 第0轴的索引，第1轴的索引


a4 = np.arange(12).reshape([3, 2, 2])
print(a4)
print(a4[:, :, :1])  # 取得第一列
print(a4[..., :1])


a5 = np.arange(12).reshape([3, 2, 2])
print(a5)
print(a5[:2, 1:, :1])


# 小数操作
a6 = np.floor(3.5)  # 向下
b = np.ceil(3.5)
c = np.int(3.6)
d = np.pi
e = np.round(d, 3)  # 四舍五入
f = np.around(d, 3)  # 四舍五入
g1 = np.rint(3.4)
g2 = np.rint(3.5)
h1, h2 = np.modf(3.5)  # 分割成小数和整数

print(a6)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g1)
print(g2)
print(h1, h2)


j = np.arange(9)
q = np.split(j, 3)  # 平均分割成三组
w = np.split(j, [3, 5, 8])  # 按照指定元素的位置分割数组

print(j)
print(q)
print(w)



