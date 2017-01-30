import numpy as np
import matplotlib.pyplot as plt

a = np.random.rand(4, 4)
b = np.random.rand(4, 1)

r1 = np.dot(np.transpose(b), a)
r1 = np.dot(r1, b)
print(r1)

a = np.transpose(a)
r1 = np.dot(np.transpose(b), a)
r1 = np.dot(r1, b)
print(r1)
