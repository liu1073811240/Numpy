import numpy as np

a = np.arange(6).reshape(2, 3)
b = a.T
print(a)
# print(b)

for i in np.nditer(a, flags=['external_loop'], order='F'):
    print(i)
    exit()




