s = 0
for i in range(1, 101):
    s += i * i

print(sum([i for i in range(1, 101)]) ** 2 - s)