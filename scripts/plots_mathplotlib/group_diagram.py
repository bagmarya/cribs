#столбчатая диаграмма bar() - вертикальная; barh() - горизонтальная.

import matplotlib.pyplot as plt
import numpy as np

labels = [f'P{i}' for i in range(5)]
g1 = [10, 21, 34, 12, 27]
g2 = [17, 15, 25, 21, 26]
width = 0.3
x = np.arange(len(labels))

fig, ax = plt.subplots()

ax.bar(x, g1, width, label='g1')
ax.bar(x + width/2, g2, width, label='g2')

# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# эти строки заменим одной
ax.set(title='групповая диаграмма', xticks=x, xticklabels=labels)
ax.legend()

plt.show()

