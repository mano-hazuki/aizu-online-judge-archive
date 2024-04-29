time = int(input())
hour = time // (60 * 60)
minute = (time - hour * 60 * 60) // 60
second = (time - hour * 60 * 60) % 60
print(f'{hour}:{minute}:{second}')
