#https://seaborn.pydata.org/tutorial.html
import seaborn as sns
import matplotlib.pyplot as plt
#sns.get_dataset_names() # вернет список встроенных датасетов
mpg = sns.load_dataset('mpg') # загрузим датасет по автомобилям
print(type(mpg))
print(mpg.head())

sns.relplot(x='horsepower',     #по оси обсцисс - лошадинные силы
            y='acceleration',   #по оси ординат - ускорение
            size='cylinders',   #размер точки зависит от количества циллиндров
            kind='scatter',     # строим точечную диаграмму
            data=mpg)           # ...по датасету mpg

plt.show()
