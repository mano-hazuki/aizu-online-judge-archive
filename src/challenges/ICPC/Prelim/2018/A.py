while True:
    n = int(input())
    if n == 0:
        break
    A = list(map(int, input().split()))
    ave = sum(A) / len(A)
    ans = 0
    for a in A:
        if a <= ave:
            ans += 1
    print(ans)
