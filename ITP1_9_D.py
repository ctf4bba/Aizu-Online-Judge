s = input()
q = int(input())
for i in range(q):
    l = input().split()
    n1 = int(l[1])
    n2 = int(l[2])
    if l[0] == 'replace':
        s = s[:n1] + l[3] + s[n2+1:]
    elif l[0] == 'reverse':
        s = s[:n1] + s[n2:n1:-1] + s[n1] + s[n2+1:]
    elif l[0] == 'print':
        print(s[n1:n2+1])
    else:
        pass

