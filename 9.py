for a in range(1, 333):
    for b in range(a, 666):
        for c in range(b, 999):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                break