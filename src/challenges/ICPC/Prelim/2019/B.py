while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    keyboard = []
    for _ in range(0, h):
        keys = input()
        keyboard.append(keys)
    sentence = input()

    # steps = [[j + i for j in range(1, w + 1)] for i in range(0, h)]
    lastPos = (-1, -1)
    ans = 0

    for s in sentence:
        for y in range(0, h):
            for x in range(0, w):
                if s != keyboard[y][x]:
                    continue
                if lastPos == (-1, -1):
                    ans += y + x + 1
                else:
                    ans += abs(y - lastPos[0]) + abs(x - lastPos[1]) + 1
                lastPos = (y, x)
    print(ans)
