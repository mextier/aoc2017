data = "amgozmfv"
# data = "flqrgnkx"

def one_round(lengths, lst, cur, skip):
    for l in lengths:
        lst = lst[cur:] + lst[:cur]
        lst = list(reversed(lst[:l])) + lst[l:]
        lst = lst[-cur:] + lst[:-cur]

        cur = (cur + l + skip) % len(lst)
        skip += 1

    return (lst, cur, skip)

def knot_hash(s):
    p2lengths = map(ord, s) + [17, 31, 73, 47, 23]
    lst = range(256)

    cur, skip = 0, 0
    for rn in xrange(64):
        lst, cur, skip = one_round(p2lengths, lst, cur, skip)

    dense = []
    for i in xrange(0, len(lst), 16):
        dense.append(reduce(lambda c, a: c^a, lst[i:i+16]))

    return dense

def bins(dh):
    res = []
    for c in dh:
        for i in xrange(7, -1, -1):
            res.append(bool((1 << i) & c))

    return res

def tos(bv):
    return "".join(map(lambda f: ".#"[f], bv))

n = 128

res = 0
table = []
for i in xrange(n):
    bv = bins(knot_hash("%s-%d" % (data, i)))
    table.append(bv)
    res += sum(bv)

print res

vis = [[False] * n for _ in xrange(n)]

def dfs(i, j):
    global vis
    vis[i][j] = True

    for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and table[ni][nj] and not vis[ni][nj]:
            dfs(ni, nj)

regions = 0
for i in xrange(n):
    for j in xrange(n):
        if table[i][j] and not vis[i][j]:
            regions += 1
            dfs(i, j)

print regions
