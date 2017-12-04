def step(idx):
    x, y = 0, 0
    dx, dy = 1, 0

    tick, steps, left = False, 1, 1

    for i in xrange(idx):
        x += dx
        y += dy
        left -= 1

        if left > 0:
            continue

        tick ^= True
        if not tick:
            steps += 1

        dx, dy = -dy, dx
        left = steps

    return x, y

mp = [[0] * 9 for _ in xrange(9)]

for i in xrange(82):
    x, y = step(i-1)
    mp[4-y][4+x] = i

# for r in mp:
    # print " ".join("%3d" % s for s in r)

sample = 368078
rx, ry = step(sample - 1)
print abs(rx) + abs(ry)

cache = { (0, 0): 1 }

idx = 1
while True:
    x, y = step(idx)
    idx += 1

    cres = long(0)
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            cres += cache.get((x+dx, y+dy), 0)

    cache[x, y] = cres
    print x, y, cres

    if cres > sample:
        break
