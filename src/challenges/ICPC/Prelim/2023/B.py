N, M, P, Q = map(int, input().split())
X = list(map(int, input().split()))
K = [[0 for _ in range(0, N)] for _ in range(0, M * 2 + 3)]


def init():
    for y in range(0, len(K)):
        for x in range(0, len(K[y])):
            K[y][x] = 0
    y = 0
    for i in range(0, len(X)):
        y += 2
        K[y][X[i] - 1] = 1
        K[y][X[i]] = 1


def check():
    x = P - 1
    y = 0
    while y >= len(K) - 1:
        if K[y][x] == 1:
            if x > 0 and K[y][x - 1] == 1:
                x -= 1
            if x < len(K[y]) - 1 and K[y][x + 1] == 1:
                x += 1
        y += 1
    return x == (Q - 1)


if __name__ == "__main__":
    ok = False
    count = 0
    new_x = -1
    new_y = -1
    while True:
        init()

        if new_x != -1 and new_y != -1:
            K[new_y][new_x] = 1
            K[new_y][new_x + 1] = 1

        if check():
            ok = True
            break

        if new_x == -1 and new_y == -1:
            new_x = 0
            new_y = 1
        else:
            if new_x == len(K[new_y]) - 2:
                new_x = 0
                new_y += 2
            else:
                new_x += 1
        if new_y >= len(K) - 1:
            break
        count += 1

    if ok:
        if count == 0:
            print("OK")
        else:
            print(new_x + 1, new_y + 1)
    else:
        print("NG")
