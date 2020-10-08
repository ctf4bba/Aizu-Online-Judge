while True:
    d = list(map(int, input().split()))
    if d[0] == -1 and d[1] == -1 and d[2] == -1:
        break
    elif d[0] == -1 or d[1] == -1:
        print('F')
    elif d[0] + d[1] >= 80:
        print('A')
    elif d[0] + d[1] >= 65:
        print('B')
    elif d[0] + d[1] >= 50 or (d[0] + d[1] >= 30 and d[2] >= 50):
        print('C')
    elif d[0] + d[1] >= 30:
        print('D')
    else:
        print('F')

