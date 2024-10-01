import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Данные об ирисе Фишера
iris = sns.load_dataset('iris')

# Гистограмма для длины чашелистика
plt.figure(figsize=(10, 6))
sns.histplot(iris['sepal_length'], bins=20, kde=True)
plt.title('Гистограмма длины чашелистика ириса Фишера')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
