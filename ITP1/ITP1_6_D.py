n, m = map(int, input().split())
a = []
b = []

for ni in range(n):
    a.append(list(map(int, input().split())))

for mi in range(m):
    b.append(int(input()))

for ai in a:
    num = 0
    for aij, bj in zip(ai, b):
        num += aij * bj
    print(num)
