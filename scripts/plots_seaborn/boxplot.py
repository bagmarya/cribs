#https://seaborn.pydata.org/tutorial.html
import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset('iris')
print(iris.head())

sns.boxplot(x='species', y='sepal_length', data=iris)
plt.show()