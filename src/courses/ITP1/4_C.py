while True:
    a, op, b = map(str, input().split())
    a = int(a)
    b = int(b)
    if op == "?":
        break
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    else:
        print(a // b)
