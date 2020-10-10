r, c = map(int, input().split())
l = []
for ri in range(r):
    lt = list(map(int, input().split()))
    lt.append(sum(lt))
    l.append(lt)
    print(' '.join(map(str, lt)))

lt2 = []
for i in range(len(l[0])):
    n = 0
    for li in l:
        n += li[i]
    lt2.append(n)
print(' '.join(map(str, lt2)))