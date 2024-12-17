import time
import numpy as np
from multiprocessing import Pool

def calculate_row_sum(matrix, row_index):
    """Вычисляет сумму элементов одной строки матрицы."""
    return matrix[row_index].sum()

def calculate_col_sum(matrix, col_index):
    """Вычисляет сумму элементов одного столбца матрицы."""
    return matrix[:, col_index].sum()

    # Генерация большой случайной матрицы размером 1000x1000
matrix = np.random.randint(0, 10, size=(100, 100))
print(matrix.shape[0])    
    # Использование пула процессов для параллельного вычисления суммы строк
with Pool(processes=4) as pool:
    row_sums = pool.starmap(calculate_row_sum, ((matrix, i) for i in range(matrix.shape[0])))
    
    # Использование пула процессов для параллельного вычисления суммы столбцов
start_time = time.time()
with Pool(processes=4) as pool:
    col_sums = pool.starmap(calculate_col_sum, ((matrix, i) for i in range(matrix.shape[1])))
  
end_time = time.time()
elapsed_time_for = end_time - start_time
print(elapsed_time_for)
    # Вывод результатов
print("Суммы строк:", row_sums[:5])  # Показываем первые 5 сумм строк
print("Суммы столбцов:", col_sums[:5])  # Показываем первые 5 сумм столбцов