import math

a, b, C = map(float, input().split())

sinC = math.sin(math.radians(C))
print(a * b * math.sin(math.radians(C)) / 2)
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C))) + a + b)
print(b * math.sin(math.radians(C)))