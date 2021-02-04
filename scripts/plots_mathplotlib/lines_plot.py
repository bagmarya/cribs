import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(2, 2) # в данном случае axes - это двухмерный массив 2 х 2

x = np.linspace(0, 30, 10)
y1 = x
y2 = [i ** 2 for i in x]
y3 = [-i ** 2 for i in x]
y4 = [np.sin(i) for i in x]

# можно построить графики обращаесь  к сабплотам по индексам
# axes[0, 0].plot(x, y1)
# axes[0, 1].plot(x, y2)
# axes[1, 0].plot(x, y3)
# axes[1, 1].plot(x, y4)

# но можно и вот так. flattern() - переводит массив в одномерный

for ax, y in zip(axes.flatten(), [y1, y2, y3, y4]):
    ax.plot(x, y)

plt.show()
