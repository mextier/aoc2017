with open("star_11.txt", 'rt') as f:
    path_s = f.readline()

dirs = {
    'n' : (0, 1),
    's' : (0, -1),

    'ne' : (1, 0),
    'sw' : (-1, 0),

    'se' : (1, -1),
    'nw' : (-1, 1)
}

# path_s = "ne,ne,sw,sw"
path = path_s.strip().split(',')

temps = set([(0, 0)])

tx, ty = 0, 0
for dir_s in path:
    dx, dy = dirs[dir_s]

    tx += dx; ty += dy
    temps.add((tx, ty))

from collections import deque
q = deque([((0, 0), 0)])
vis = set([(0, 0)])

furthest = 0

while len(temps) > 0:
    cp, clen = q.popleft()
    cx, cy = cp
    if cx == tx and cy == ty:
        print 'final', clen

    if cp in temps:
        temps.discard(cp)
        furthest = max(furthest, clen)

    for dx, dy in dirs.itervalues():
        np = (cx + dx, cy + dy)
        if np not in vis:
            vis.add(np)
            q.append((np, clen+1))

print 'furthest', furthest
