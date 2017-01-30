import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

np.set_printoptions(precision = 3, suppress = True)

A = np.array([ \
[8, 11, 3, -2], \
[3, 2, 2, -1], \
[-1, 7, -3, 1], \
[-11, 1, -12, 5]], float)

r0 = np.array(A[0,])
r3 = np.array(A[3,])
A[3,] = r0
A[0,] = r3

M1 = np.array([ \
[1, 0, 0, 0],
[3./11., 1, 0, 0],
[-1./11., 0, 1, 0],
[8./11., 0, 0, 1]], float)

A1 = np.dot(M1, A)

r1 = np.array(A1[1],)
r3 = np.array(A1[3],)
A1[3,] = r1
A1[1,] = r3
t2 = -A1[2, 1] / A1[1, 1]
t3 = -A1[3, 1] / A1[1, 1]

M2 = np.array([ \
[1, 0, 0, 0],
[0, 1, 0, 0],
[0, t2, 1, 0],
[0, t3, 0, 1]], float)

A2 = np.dot(M2, A1)

t3 = -A2[3, 3] / A2[2, 3]

M3 = np.array([ \
[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, 1, 0],
[0, 0, t3, 1]], float)

A3 = np.dot(M3, A2)

M = M3 @ M2 @ M1
