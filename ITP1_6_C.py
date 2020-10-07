l = [[[0] * 10 for i in range(3)] for j in range(4)]

l_inp = []
n = int(input())
for ni in range(n):
    l_inp.append(list(map(int, input().split())))

for i in range(len(l_inp)):
    l[l_inp[i][0]-1][l_inp[i][1]-1][l_inp[i][2]-1] += l_inp[i][3]

for i, li in enumerate(l):
    for lj in li:
        print(' ' + ' '.join(map(str, lj)))
    if i < len(l) - 1:
        print('#'*20)
