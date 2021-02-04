# графики изображаются друг над другом
# и каждый следующий - сумма предыдущего и заданного
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 2, 5, 7, 9]

fig, ax = plt.subplots()

ax.stackplot(x, y1, y2, y3, labels=['y1', 'y2', 'y3'])
ax.legend(loc='upper left') # здесь указываем расположение в левом верхнем углу


plt.show()
