n = int(input())
s1 = s2 = 0
for i in range(n):
    a, b = input().split()
    if len(a) < len(b):
        tmp = a
    else:
        tmp = b
    for j in range(len(tmp)):
        if a[j] > b[j]:
            s1 += 3
            break
        elif a[j] < b[j]:
            s2 += 3
            break
        else:
            pass
    else:
        if len(a) > len(b):
            s1 += 3
        elif len(a) < len(b):
            s2 += 3
        else:
            s1 += 1
            s2 += 1
print(s1, s2)