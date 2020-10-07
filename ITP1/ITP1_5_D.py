n = int(input())
a = ''

for i in range(1, n + 1):
  if i % 3 == 0:
    a += ' ' + str(i)
  elif '3' in str(i):
    a += ' ' + str(i)

print(a)
