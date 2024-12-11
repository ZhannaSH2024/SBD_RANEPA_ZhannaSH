import threading

semaphore = threading.Semaphore(3)  # Создаем семафор с начальным значением 3

def worker():
    semaphore.acquire()  # Захватываем семафор
    try:
        # Выполняем некоторую работу с общим ресурсом
        for i in range(100_000_000):
            a=1+i
        print(f"{threading.current_thread().getName()} is working")
    finally:
        semaphore.release()  # Освобождаем семафор

threads = []
for i in range(10):
    thread = threading.Thread(target=worker, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()