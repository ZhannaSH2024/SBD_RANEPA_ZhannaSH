import threading
import random

class LamportClock:
    def __init__(self):
        self.clock = 0

    def get_time(self):
        return self.clock

    def increment(self):
        self.clock += 1

    def update(self, other_clock):
        self.clock = max(self.clock, other_clock)

class Process:
    def __init__(self, id):
        self.id = id
        self.clock = LamportClock()
        self.messages_sent = []
        self.messages_recieved = []
        self.lock = threading.Lock()

    def send_message(self, recipient, event_type="message"):
            with self.lock: # блокируем текущий объект класса Process
                self.clock.increment()
                message = (event_type, self.id, self.clock.get_time())
                self.messages_sent.append(message) # записали в отосланные
                recipient.receive_message(message) # принимаем сообщение

    
    def receive_message(self, message):
            with self.lock:
                event_type, sender_id, sender_clock = message
                self.clock.update(sender_clock) # это и есть other_clock
                self.messages_recieved.append(message)

    def run(self):
        for _ in range(3): # создает 3 симметричных процесса
            recipients = list(filter(lambda p: p.id != self.id, processes)) # посылаем всем, кроме себя (!= self.id) из 3
            if recipients:
                recipient = recipients[random.randint(0, len(recipients)-1)]  # формирует случайного реципиента 
                self.send_message(recipient)   # отправляет ему message 

processes = [Process(id=i) for i in range(3)] # синтаксический сахар,  (2 получателя и я)

threads = [threading.Thread(target=p.run) for p in processes]
for t in threads:
    t.start()

# Вывод результатов
for p in processes:
    print(f"Процесс {p.id}:")
    print("\tОтправленные сообщения:", p.messages_sent)
    print("\tПолученные сообщения:", p.messages_recieved)
