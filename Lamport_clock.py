class LamportClock:
    def __init__(self):
        self.clock = 0

    def get_time(self):
        return self.clock

    def increment(self):
        self.clock += 1

    def update(self, other_clock):
        self.clock = max(self.clock, other_clock)

# Пример использования
node_a = LamportClock()
node_b = LamportClock()

print("Initial time for node A:", node_a.get_time())
print("Initial time for node B:", node_b.get_time())

# Node A increments its clock
node_a.increment()
node_a.increment()
node_a.increment()
print("Node A increments its clock to:", node_a.get_time())

# Node B sends a message with timestamp 10 to Node A
message_timestamp = 2
node_a.update(message_timestamp)
print("Node A updates its clock after receiving message from Node B:", node_a.get_time())