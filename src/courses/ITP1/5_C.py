while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(0, H):
        for j in range(0, W):
            print("#" if j % 2 == i % 2 else ".", end="")
        print()
    print()
