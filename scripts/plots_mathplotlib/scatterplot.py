#точечный график

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10.5, 0.5)
y = np.cos(x)

fig, ax = plt.subplots()

ax.scatter(x, y)
plt.show()