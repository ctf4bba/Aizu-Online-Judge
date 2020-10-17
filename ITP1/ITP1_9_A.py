import sys

w = input()
t = ''
for l in sys.stdin:
    t += l

tl = t.lower().replace('END_OF_TEXT', '').strip().split()
c = 0
for tli in tl:
    if tli == w:
        c += 1

print(c)
