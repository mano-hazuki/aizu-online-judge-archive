while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(0, H):
        for j in range(0, W):
            print("#" if i == 0 or j == 0 or i == H - 1 or j == W - 1 else ".", end="")
        print()
    print()
