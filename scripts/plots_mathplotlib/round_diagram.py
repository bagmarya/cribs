import matplotlib.pyplot as plt
import numpy as np

vals = [24, 17, 53, 29]
labels = [f'P{i}' for i in range(4)]

fig, ax = plt.subplots()

ax.pie(vals, labels=labels)

plt.show()