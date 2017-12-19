data = """
     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
"""

with open("star_19.txt", "rt") as f:
    data = f.read()

lines = filter(lambda v: len(v.strip()) > 0, data.split('\n'))
maxl = max(map(len, lines))

bmp = [[None] * maxl for _ in xrange(len(lines))]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != ' ':
            bmp[i][j] = c

sj = None
for j in xrange(maxl):
    if bmp[0][j] is not None:
        sj = j

dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
dirsym = "||--"

def is_letter(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

route = ""

def walk(i, j, cdir):
    global route

    steps = 0
    while 0 <= i < len(lines) and 0 <= j < maxl:
        cc = bmp[i][j]
        steps += 1

        if is_letter(cc):
            route += cc

        if cc == '+':
            cnds = []
            for ndir in (2, 3) if cdir in (0, 1) else (0, 1):
                di, dj = dirs[ndir]
                ni, nj = i+di, j+dj
                if 0 <= ni < len(lines) and 0 <= nj < maxl and bmp[ni][nj] is not None:
                    i, j, cdir = ni, nj, ndir
                    break

        elif cc is not None:
            di, dj = dirs[cdir]
            i, j = i+di, j+dj

        else:
            break

    return steps

print walk(0, sj, 0) - 1
print route
