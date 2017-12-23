area = """
#.##.###.#.#.##.###.##.##
.##.#.#.#..####.###.....#
...##.....#..###.#..#.##.
##.###.#...###.#.##..##.#
###.#.###..#.#.##.#.###.#
.###..#.#.####..##..#..##
..###.##..###.#..#...###.
........##..##..###......
######...###...###...#...
.######.##.###.#.#...###.
###.##.###..##..#..##.##.
.#.....#.#.#.#.##........
#..#..#.#...##......#.###
#######.#...#..###..#..##
#..#.###...#.#.#.#.#....#
#.#####...#.##.##..###.##
..#..#..#.....#...#.#...#
###.###.#...###.#.##.####
.....###.#..##.##.#.###.#
#..#...######.....##.##.#
###.#.#.#.#.###.##..###.#
..####.###.##.#.###..#.##
#.#....###....##...#.##.#
###..##.##.#.#.##..##...#
#.####.###.#...#.#.....##
"""

# area = """
# ..#
# #..
# ...
# """

from copy import copy
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

lines = area.strip().split('\n')
assert len(lines) % 2 == 1

state = {}

cc = len(lines) / 2

for i, line in enumerate(lines):
    assert len(line) == len(lines)
    for j, c in enumerate(line):
        if c == '#':
            state[(i-cc, j-cc)] = -1

def simulate(deltas, final_cell, iters):
    cstate = copy(state)

    final_count = 0

    cx, cy, cdir = 0, 0, 0
    for burstn in xrange(iters):
        cp = (cx, cy)
        cell = cstate.get(cp, 0)
        if cell == -1:
            cell = final_cell

        cdir = (cdir + deltas[cell]) % 4
        cstate[cp] = cell = (cell+1) % len(deltas)
        if cell == final_cell:
            final_count += 1

        dx, dy = dirs[cdir]

        cx += dx
        cy += dy

    return final_count

print simulate((-1,1), 1, 10000)
print simulate((-1,0,1,2), 2, 10000000)
