s = 0
for i in range(1901, 2002):
    if i % 4 == 0 and i % 400 != 0:
        s += 366
    else:
        s += 365
print(s // 7)
