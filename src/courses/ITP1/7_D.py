n, m, l = map(int, input().split())
A: list[list[int]] = []
B: list[list[int]] = []
for i in range(0, n):
    A.append(list(map(int, input().split())))
for i in range(0, m):
    B.append(list(map(int, input().split())))
for i in range(0, n):
    for j in range(0, l):
        el = 0
        for k in range(0, m):
            el += A[i][k] * B[k][j]
        if j == l - 1:
            print(el, end="")
        else:
            print(el, end=" ")
    print()
