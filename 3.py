from math import sqrt, floor


div = 2
m_div = 0
n = 600851475143
while div <= floor(sqrt(n)):
    if n % div == 0:
        n //= div
        if m_div < div:
            m_div = div
    else:
        div += 1
print(m_div)