import numpy as np

a = np.arange(12).reshape([2, 2, 3])
print(a.ndim)  # 维度

print(a.size)  # 元素个数
print(a.dtype)
print(a.itemsize)  # 字节大小（一个字节8个位）

print(a.data)  # 数据的内存地址






