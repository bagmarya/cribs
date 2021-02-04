#https://seaborn.pydata.org/tutorial.html
import seaborn as sns
import matplotlib.pyplot as plt


flights = sns.load_dataset('flights')
print(flights.head())

sns.relplot(x='year', y='passengers', kind='line', data=flights, ci=None)
# ci=None - отключает отображение доверительного интервала
plt.show()
