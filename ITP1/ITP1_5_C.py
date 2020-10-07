l = '#.'*600

while True:
  h, w = map(int, input().split())
  if h == 0 and w == 0:
    break
  
  for i in range(h):
    print(l[i:i+w])
  else:
    print('')
