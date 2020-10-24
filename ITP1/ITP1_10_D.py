n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
xy_d = [abs(xi - yi) for xi, yi in zip(x, y)]
d = [sum(xy_di ** p for xy_di in xy_d) ** (1 / p) for p in range(1, 4)]
d.append(max(xy_d))
print(*d, sep='\n')