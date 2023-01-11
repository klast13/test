def is_pal(n):
    n = str(n)
    return n == n[::-1]


max_pal = 0
for i in range(999, 9, -1):
    for j in range(999, 9, -1):
        if is_pal(i * j):
            max_pal = max(max_pal, i * j)
print(max_pal)