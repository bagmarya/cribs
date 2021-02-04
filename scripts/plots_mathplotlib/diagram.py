#столбчатая диаграмма bar() - вертикальная; barh() - горизонтальная.

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

labels = [f'P{i}' for i in range(7)]

x = np.arange(len(labels))
counts = np.random.randint(3, 10, len(labels))

ax.bar(x, counts)
ax.set_xticks(x)
ax.set_xticklabels(labels)

plt.show()

