N = int(input())
A = list(map(int, input().split()))

for i in range(1, N - 1):
    for j in range(0, i + 1):
        if A[i] < A[j]:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
        print(A)
print(A)
