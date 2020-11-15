import numpy as np

a = np.array([1, 2, 5, 4, 3, 6, 7])
b = np.array([True, False, False, True, False, True, False])

# 0，1可以做布尔值，也可以做索引，使用的时候一定要指明
# b = np.array([1, 0, 0, 1, 0, 1, 0])
print(a[b])  # 拿b数组里面的布尔值去选择a数组中的元素
print(a[b == True])
print(a[b == False])


a1 = np.array([1, 2, 3, 4, 5, 6])
# 输出符合条件的布尔值
print(a1 > 3)  # 符合条件的输出True, 否则输出False
print(a1[a1 > 3])  # 拿布尔值选择数组里面的元素
print((a==3) | (a==5))  # 或运算 (输出符合条件的布尔值)
print((a==3) & (a==5))  # 并运算


# 布尔值是可以运算的
a = np.array([True, False, True, True, False])
print(a+1)
