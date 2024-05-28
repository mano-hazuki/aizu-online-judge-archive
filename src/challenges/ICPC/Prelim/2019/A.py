while True:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    scores = [0 for _ in range(0, N)]
    for i in range(0, M):
        P = list(map(int, input().split()))
        for j in range(0, N):
            scores[j] += P[j]

    print(max(scores))
