f1 = 1
f2 = 2
f3 = 0
s = 2  # 0 + f2
while f3 < 4000000:
    f3 = f1 + f2
    if f3 < 4000000 and f3 % 2 == 0:
        s += f3
    f1 = f2
    f2 = f3
print(s)