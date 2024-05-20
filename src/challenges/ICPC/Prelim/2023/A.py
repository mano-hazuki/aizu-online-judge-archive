while True:
    n = int(input())
    if n == 0:
        break
    A = list(map(int, input().split()))
    ans = -1
    diff_min = int(10E4)
    for i in range(0, n):
        diff = abs(A[i] - 2023)
        if diff < diff_min:
            ans = i
            diff_min = diff
    print(ans + 1)
