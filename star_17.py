n, s = 2017, 366

c, d = 0, [0]

for v in xrange(1, n+1):
    c = (c + s) % len(d) + 1
    d = d[:c] + [v] + d[c:]

print d[c:c+2]

n = 50*1000*1000
c = 0

last = None
for v in xrange(1, n+1):
    c = (c + s) % v + 1
    if c == 1:
        last = v

print last
