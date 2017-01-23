import numpy as np
import matplotlib.pyplot as plt

a = np.random.randn(100)
noise = np.random.randn(100) * 0.01
b = a * 0.33 + 0.2 + noise

plt.plot(a, b, 'o')
plt.show()
