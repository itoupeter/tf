import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]], float)

print(A)
print(np.linalg.norm(A, 2))
print(np.linalg.svd(A))
