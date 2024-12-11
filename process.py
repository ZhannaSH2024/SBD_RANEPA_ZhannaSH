x = 1
processes = [x for x in range(3)]
print(processes)

print([x for x in filter(lambda p: p!=2, processes)])