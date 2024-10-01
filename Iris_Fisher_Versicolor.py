import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = sns.load_dataset('iris')

# Данные для сорта Iris versicolor
iris_versicolor = iris[iris['species'] == 'versicolor']

# Гистограмма для длины чашелистика
plt.figure(figsize=(10, 6))
sns.histplot(iris_versicolor['sepal_length'], bins=20, kde=True)
plt.title('Гистограмма длины чашелистика для Iris versicolor')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
