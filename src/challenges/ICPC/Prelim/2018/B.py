def show_holes(holes: list[list[int]]):
    print()
    for i in range(0, len(holes)):
        for j in range(0, len(holes[i])):
            print(holes[i][j], end="")
        print()


while True:
    #  Read input values
    N, M, T, P = map(int, input().split())
    if N == M == T == P == 0:
        break
    D_C: list[list[int]] = []
    X_Y: list[list[int]] = []
    for _ in range(0, T):
        D, C = map(int, input().split())
        D_C.append([D, C])
    for _ in range(0, P):
        X, Y = map(int, input().split())
        X_Y.append([X, Y])

    #  Prepare initial hole state
    W_MAX = N * len(D_C) * 2
    H_MAX = M * len(D_C) * 2
    H = [[0 for _ in range(0, W_MAX)] for _ in range(0, H_MAX)]
    for y in range(len(H) - M, len(H)):
        for x in range(0, N):
            H[y][x] = 1

    #  For debugging
    # show_holes(H)

    # Calculate hole count
    offset_x = 0
    offset_y = 0
    for i in range(0, len(D_C)):
        d = D_C[i][0]
        c = D_C[i][1]

        # show_holes(H)

        # Update hole count for left-to-right folding
        if d == 1:
            for y in range(0, len(H)):
                for r in range(0, c):
                    from_x = offset_x + (c - 1) - r
                    to_x = offset_x + (c - 1) + r + 1
                    H[y][to_x] += H[y][from_x]
                    H[y][from_x] = 0

            # Update offset
            offset_x += c
            continue

        # Update hole count for bottom-to-top folding
        if d == 2:
            for x in range(0, W_MAX):
                for r in range(0, c):
                    from_y = len(H) - 1 - offset_y - (c - 1) + r
                    to_y = len(H) - 1 - offset_y - (c - 1) - 1 - r
                    H[to_y][x] += H[from_y][x]
                    H[from_y][x] = 0

            # Update offset
            offset_y += c
            continue

    # Print results
    for i in range(0, len(X_Y)):
        x, y = map(int, X_Y[i])
        print(H[len(H) - 1 - offset_y - y][offset_x + x])
