import time
from functools import wraps
import pickle

# Декоратор, который выводит время выполнения
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнен за {end - start:.8f} секунд")
        return result
    return wrapper

@timethis
def load_model(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Загрузка модели
rf1 = load_model("rf_model.pkl")

# Прогноз
input_data = [[1, 2, 2]]
prediction = rf1.predict(input_data)
print(f"Прогноз для {input_data}: {prediction}")
