n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
ans = 0


def is_satisfied(index: int, target: int) -> bool:
    if S[index] >= target:
        return True
    return False


def binary_search(target: int) -> int:
    index_ng = -1
    index_ok = len(S)

    while abs(index_ok - index_ng) > 1:
        mid = (index_ok + index_ng) // 2
        if is_satisfied(mid, target):
            index_ok = mid
        else:
            index_ng = mid
    return index_ok


for t in T:
    if S[binary_search(t)] == t:
        ans += 1
print(ans)
