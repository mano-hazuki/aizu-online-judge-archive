def print_arr(arr: list[int]):
    for i in range(0, len(arr)):
        print(arr[i], "" if i == len(arr) - 1 else " ", end="")
    print()


def insertion_sort(a: list[int], n: int):
    for i in range(1, n):
        print_arr(a)
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v


N = int(input())
A = list(map(int, input().split()))

insertion_sort(A, N)
