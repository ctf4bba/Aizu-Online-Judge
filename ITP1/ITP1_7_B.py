while True:
    n, x = map(int, input().split())
    c = 0
    if n == 0 and x == 0:
        break
    for i in range(1, n-1):
        for j in range(i+1, n):
            k = x - (i + j)
            if j < k and k <= n:
                c += 1
    print(c)
