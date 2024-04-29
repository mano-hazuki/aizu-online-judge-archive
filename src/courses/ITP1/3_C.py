while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    a = min(x, y)
    b = max(x, y)
    print(f"{a} {b}")
