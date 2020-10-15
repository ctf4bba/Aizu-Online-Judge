import string
import sys

d = {}
for i in range(97, 123):
    d[chr(i)] = 0

s = ''
for l in sys.stdin:
  s += l

for c in s.lower():
    if c in string.ascii_letters:
        d[c] += 1

for di in d:
    print("{} : {}".format(di, d[di]))