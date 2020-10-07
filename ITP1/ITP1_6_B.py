suite = ['S', 'H', 'C', 'D']
card = {}

n = int(input())
for i in range(n):
  card[input()] = True

for s in suite:
  for num in range(1, 14):
    key = s + ' ' + str(num)
    if key not in card:
      print(key)

