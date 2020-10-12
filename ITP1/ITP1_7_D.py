n, m, l = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    tl = ''
    for j in range(l):
        tmp = 0
        for k in range(m):
            tmp += a[i][k] * b[k][j]
        tl += ' ' + str(tmp)
    print(tl.strip())
