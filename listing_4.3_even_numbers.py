def frange(start, stop, increment):
    x = start
    while x < stop:
        if x % 2 == 0:
            yield x
        x += increment    # x увеличивается на величину increment

for n in frange(0, 10, 0.5):
    print(n)

list(frange(0, 10, 0.5))
