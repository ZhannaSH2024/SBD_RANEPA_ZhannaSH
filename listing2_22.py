import asyncio
def call_later():
    print("Меня вызовут в ближайшем будущем!")

async def delay (delay_second: int) -> int:
#async нужен, потому что task относится к библиотеке async
#какой тип переменной возвращает функция, лучше всегда указывать
    print (f'засыпаю на {delay_second} секунд')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} cек закончился')
    return delay_second

async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)
asyncio.run(main(), debug=True)