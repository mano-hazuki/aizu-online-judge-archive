while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for _ in range(0, H):
        for _ in range(0, W):
            print("#", end="")
        print()
    print()
