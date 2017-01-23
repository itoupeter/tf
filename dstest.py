import matplotlib.pyplot as plt
import numpy as np
import csv

x1 = []
x2 = []
y1 = []
y2 = []

with open('dstest.csv', 'r') as csvfile:
	data = csv.reader(csvfile)
	for line in data:
		if line[0] == 'Admit':
			continue
		if line[1] == 'Male':
			if line[0] == 'Admitted':
				x1 += [int(line[3])]
			else:
				x2 += [int(line[3])]
		else:
			if line[0] == 'Admitted':
				y1 += [int(line[3])]
			else:
				y2 += [int(line[3])]

x1 = np.array(x1)
x2 = np.array(x2)
y1 = np.array(y1)
y2 = np.array(y2)

width = 0.25
index = np.arange(len(x1))
opacity = 0.4

plt.figure(1)
plt.bar(index, x1, width, color = 'r', alpha = opacity)
plt.bar(index + width, x2, width, color = 'b', alpha = opacity)
plt.bar(index + width * 2, x1 / x2 * 100, width, color = 'g', alpha = opacity)

plt.figure(2)
plt.bar(index, y1, width, color = 'r', alpha = opacity)
plt.bar(index + width, y2, width, color = 'b', alpha = opacity)
plt.bar(index + width * 2, y1 / y2 * 100, width, color = 'g', alpha = opacity)

plt.show()
