import time
import tracemalloc
from multiprocessing import Pool

def check_combination(args):
    D, O, DONALD, GERALD, ROBERT = args
    digits = [i for i in range(10) if i != D]  # Доступные цифры (0-9 без D)
    digits_zero = [i for i in digits if i != 0]  # Без нуля для первых букв слова, потому что 6-значные числа
    results = []
    unique_letters = set(DONALD + GERALD + ROBERT)  # Извлекаем уникальные буквы

    # Проверяем, что количество уникальных букв не превышает 10, иначе нет решения
    if len(unique_letters) > 10:
        return results

    # Генерируем все возможные комбинации для оставшихся букв
    for N in digits:
        if N in (D, O): #Если N уже равно D или O, то пропускаем итерацию, так как буквы должны быть уникальными
            continue
        for A in digits:
            if A in (D, O, N):
                continue
            for L in digits:
                if L in (D, O, N, A):
                    continue
                for G in digits_zero:  # G не может быть 0
                    if G in (D, O, N, A, L):
                        continue
                    for E in digits:
                        if E in (D, O, N, A, L, G):
                            continue
                        for R in digits_zero:  # R не может быть 0
                            if R in (D, O, N, A, L, G, E):
                                continue
                            for B in digits:
                                if B in (D, O, N, A, L, G, E, R):
                                    continue
                                for T in digits:
                                    if T in (D, O, N, A, L, G, E, R, B):
                                        continue
                                    # Вычисляем значения для DONALD, GERALD и ROBERT
                                    DONALD_value = D * 100000 + O * 10000 + N * 1000 + A * 100 + L * 10 + D
                                    GERALD_value = G * 100000 + E * 10000 + R * 1000 + A * 100 + L * 10 + D
                                    ROBERT_value = R * 100000 + O * 10000 + B * 1000 + E * 100 + R * 10 + T

                                    # Проверяем, выполняется ли уравнение
                                    if DONALD_value + GERALD_value == ROBERT_value:
                                        results.append((DONALD_value, GERALD_value, ROBERT_value, O, G, E, R, B, T, A, L, N))
                                        # Выводим результат
                                        print(f"Решение найдено: DONALD = {DONALD_value}, GERALD = {GERALD_value}, ROBERT = {ROBERT_value}")
                                        print(f"Сопоставление: D={D}, O={O}, N={N}, A={A}, L={L}, G={G}, E={E}, R={R}, B={B}, T={T}")

    return results

def solve_ford(DONALD="DONALD", GERALD="GERALD", ROBERT="ROBERT", D=5):  # Задаем слова и фиксированное значение для D
    # Запускаем отслеживание памяти
    tracemalloc.start()

    # Время начала выполнения
    start_time = time.time()

    digits = [i for i in range(10) if i != D]  # Доступные цифры (0-9 без D)

    # Создаем пул процессов
    with Pool(processes=2) as pool:
        results = pool.map(check_combination, [(D, O, DONALD, GERALD, ROBERT) for O in digits if O != D])

    # Записываем время окончания выполнения
    end_time = time.time()

    # Получаем объем задействованной памяти
    current, peak = tracemalloc.get_traced_memory()

    # Останавливаем отслеживание памяти
    tracemalloc.stop()
    
    # Выводим время выполнения и объем памяти
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
    print(f"Текущий объем памяти: {current / (1024 * 1024):.2f} МБ; Пиковый объем памяти: {peak / (1024 * 1024):.2f} МБ")

solve_ford()
