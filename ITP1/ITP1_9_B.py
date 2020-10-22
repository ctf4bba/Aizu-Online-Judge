for s in iter(input, '-'):
    cnt = int(input())
    for i in range(cnt):
        h = int(input())
        s = s[h:] + s[:h]
    else:
        print(s)
