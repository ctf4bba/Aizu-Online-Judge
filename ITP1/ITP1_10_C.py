import math

while True:
    n = int(input())
    if n == 0:
        break
    else:
        s = list(map(int, input().split()))
        avg = sum(s) / len(s)
        tmp = 0
        for si in s:
            tmp += (si - avg) ** 2
        else:
            std = math.sqrt(tmp / len(s))
            print(f'{std:.08f}')