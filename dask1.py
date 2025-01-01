from dask.distributed import Client

client = Client('tcp://127.0.0.1:8786') # для подключения к к Dask-серверу

def inc(x):
    return x + 1

future = client.submit(inc, 10) # отправляет функцию inc с аргументом 10 
#на выполнение в распределенной системе Dask

result = future.result()
print(result)  # Выведет 11