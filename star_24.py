data = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""

with open("star_24.txt", "rt") as f:
    data = f.read()

ports = []
for line in data.strip().split():
    l, r = map(int, line.split('/'))
    ports.append((l, r))

vis = [False] * len(ports)

def backtrack(pins, first_part):
    global vis

    best = (0, ()) if first_part else (0, 0)
    for i in xrange(len(ports)):
        if vis[i]:
            continue

        l, r = ports[i]
        if l == pins:
            out = r
        elif r == pins:
            out = l
        else:
            continue

        vis[i] = True
        res = backtrack(out, first_part)
        vis[i] = False

        if first_part:
            strength, tail = res
            value = (strength + l + r, ((l,r),) + tail)
        else:
            length, strength = res
            value = (length + 1, strength + l + r)

        best = max(best, value)

    return best

print backtrack(0, True)
print backtrack(0, False)
