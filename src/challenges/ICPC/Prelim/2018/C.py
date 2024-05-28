import math

while True:
    B = int(input())
    if B == 0:
        break
    f = -1
    n = -1
    for q in range(1, 100001):
        p = B / q - (q - 1) / 2
        if p >= 1 and p == math.floor(p):
            f = int(p)
            n = q
    print(f, n)
