while True:
    n, x = map(int, input().split())
    ans = 0
    if n == 0 and x == 0:
        break
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i + j + k == x - 3:
                    ans += 1
    print(ans)
