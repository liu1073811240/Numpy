import numpy as np

x = np.random.randint(0, 10, 100)  # 随机生成0-10之间的100个整数
# 从“半开”间隔[ 低，高 ]中指定dtype的“离散均匀”分布返回随机整数
print(x)
print(x.sum())

x = np.random.random(100).reshape(2, 50)  # #随机生成0到1之间的指定个数的小数
# 结果来自所述间隔的“连续均匀”分布。
print(x)

x = np.random.rand(10)  #随机生成0到1之间的指定个数的小数,
# 创建给定形状的数组，并使用来自均匀分布的随机样本填充它。[0, 1)
print(x)

x = np.random.rand(2, 2, 2, 2)  # 指定形状
print(x)

x = np.random.rand(8).reshape(2, 4)  # 变换形状
print(x)

x = np.random.randn(10, 10)  # 随机生成指定个数的标准正态分布数据
print(x)

x = np.random.randn(100).reshape(10, 10)
#从标准正态分布中返回一个或多个样本值。
print(x)

x = np.random.ranf(10)  #随机生成0到1之间的指定个数的小数,
# 结果来自所述间隔的“连续均匀”分布
print(x)

x = np.random.random_sample(10)  # 随机生成0到1之间的指定个数的小数,
# 结果来自所述间隔的“连续均匀”分布
print(x)

x = np.random.uniform(-1, 1, 100)  # 随机生成-1到1之间的指定个数的小数
# 结果来自所述间隔的“连续均匀”分布
print(x)

