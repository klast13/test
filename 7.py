from math import sqrt

c = 0
n = 2
arr = [2]
while c != 10000:
    n += 1
    if n > 10:
        if n % 2 == 0 or n % 10 == 5:
            continue
    for i in arr:
        if i > int((sqrt(n)) + 1):
            arr.append(n)
            c += 1
            break
        if n % i == 0:
            break
    else:
        arr.append(n)
        c += 1
print(n)