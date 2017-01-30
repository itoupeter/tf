import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

b = np.transpose(a)
print(b)

ab = np.dot(a, b)
print(ab)

u, s, v = np.linalg.svd(ab)
print(u)
print(s)
print(v)
print("-----------------------")

ba = np.dot(b, a)
print(ba)

u, s, v = np.linalg.svd(ba)
print(u)
print(s)
print(v)
