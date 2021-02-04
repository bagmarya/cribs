import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'  # для векторного отображения графиков
# fig, axes = plt.subplots(1, 3) # метод возращает объект figure с тремя встроенными объектами axes
# plt.plot(x, y) - создает график без явного создания объектов полотна для графиков
# но лучше создавать их явно для возможности более тонкой настройки.


fig = plt.figure()
ax = fig.add_subplot()
fig.set(facecolor='grey')

x = np.linspace(0, 30, 10)
y1 = x
y2 = [i ** 2 for i in x]

ax.plot(x, y1, color = 'red', linestyle = '--', label='lineal')
ax.plot(x, y2, color = 'grey', linestyle = '-', label='sqwere')
ax.legend()
ax.grid()
ax.set(title = 'Graph_1', xlabel='ось X', ylabel = 'ось Y')
plt.show()
