import time
from dask.distributed import Client

# Создаем клиентское соединение с Scheduler
client = Client('tcp://127.0.0.1:8786')

# Функция, имитирующая длительную задачу
def long_running_task(seconds):
    print(f"Starting task for {seconds} seconds...")
    time.sleep(seconds)
    print("Task completed!")
    return f"Task took {seconds} seconds to complete."

# Отправляем задачу на выполнение
future = client.submit(long_running_task, 10) 
# задача будет выполняться в распределенной среде Dask, и она будет "спать" 10 секунд. 

# Периодическая проверка статуса выполнения задачи
# Этот цикл будет выполняться до тех пор, пока задача, представленная объектом Future 
# (в данном случае future), не будет завершена.
while not future.done():
    status = future.status
    print(f"Current status: {status}")
    time.sleep(2)

# Получаем результат после завершения задачи
result = future.result()
print(result)