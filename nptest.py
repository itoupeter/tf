import numpy as np

a = [1, 2, 3]
at = np.transpose(a)
b = np.random.rand(3, 3)

print(a @ b)
print(at @ b)

a = np.transpose(at)

print(a)
