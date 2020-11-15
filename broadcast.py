import numpy as np

a = np.arange(48).reshape([3, 4, 4])
b = np.arange(12).reshape([3, 4, 1])
# b = np.arange(4)

# print(a)
# print(b)
# print(a+b)

a1 = np.arange(24).reshape([2, 3, 4])
b1 = np.arange(12).reshape([3, 4])
c1 = np.arange(4)

# print(a1+b1)
# print(a1+c1)

a2 = np.arange(12).reshape([3, 4, 1])
b2 = np.arange(3, 4)  # [3]
c2 = np.arange(12).reshape([3, 4])

print(a2)
print(b2)
print(a2+b2)



