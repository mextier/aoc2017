data = """
0: 3
1: 2
4: 4
6: 4
"""

from star_13_input import data

fw = []
for line in data.strip().split('\n'):
    d_s, r_s = line.split(': ')
    d, r = int(d_s), int(r_s)
    fw.append((d, r))

max_d = max(fw)[0]
ranges = [None] * (max_d + 1)
for d, r in fw:
    ranges[d] = r

# read before coding next time
def wraparound(c, r):
    mc = c % (2*r-2)
    return mc if mc < r else 2*(r-1)-mc

sev = 0
for c in range(max_d+1):
    if ranges[c] is not None:
        cp = wraparound(c, ranges[c])
        if cp == 0:
            sev += c*ranges[c]

print sev

safe = 0
while True:
    caught = False
    for c in range(max_d+1):
        if ranges[c] is not None:
            cp = wraparound(c+safe, ranges[c])
            if cp == 0:
                caught = True
                break

    if not caught:
        print safe
        break

    safe += 1
