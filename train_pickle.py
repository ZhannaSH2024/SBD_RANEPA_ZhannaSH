import time
from functools import wraps
from sklearn.ensemble import RandomForestClassifier
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

# Обучение модели
X = [[2, 2, 1], [1, 1, 1], [1, 1, 2], [1, 2, 2]]
Y = ["b", "a", "a", "b"]

@timethis
def train_model(X, Y):
    clf = RandomForestClassifier(n_estimators=10)
    return clf.fit(X, Y)

clf = train_model(X, Y)

# Сохранение модели
@timethis
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

save_model(clf, "rf_model.pkl")  # Сохраняем модель с расширением .pkl
