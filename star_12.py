data = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""

from star_12_input import data

adj = {}
for line in data.strip().split('\n'):
    f_s, l_s = line.split('<->')
    f = int(f_s)
    l = map(int, l_s.strip().split(', '))

    for na in l:
        adj.setdefault(f, []).append(na)
        adj.setdefault(na, []).append(f)

def dfs(vis, n):
    for na in adj[n]:
        if na not in vis:
            vis.add(na)
            dfs(vis, na)

mark = set()
dfs(mark, 0)
print len(mark)

allv = set(adj.keys())
groups = 0
while allv:
    groups += 1
    sn = allv.pop()
    mark = set()
    dfs(mark, sn)
    allv -= mark

print '!', groups
