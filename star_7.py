data = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

from star_7_input import data

lines = data.strip().split('\n')

adjd, wgtd, incd = {}, {}, {}

for line in lines:
    if '->' in line:
        before, after = line.split('->')
        after_l = after.strip().split(', ')
    else:
        before, after_l = line, []

    # print before.strip().split(' ')
    from_s, wgt_s = before.strip().split(' ')
    wgt = int(wgt_s[1:-1])

    # print from_s, wgt, after_l

    adjd[from_s] = after_l
    wgtd[from_s] = wgt

    for after in after_l:
        incd[after] = incd.get(after, 0) + 1

root = None
for from_s in adjd.iterkeys():
    if from_s not in incd:
        root = from_s
        print from_s
        break

wgtr = {}

def rec(node):
    children = []
    wgtr[node] = wgtd[node]
    for adj in adjd.get(node, ()):
        stwgt = rec(adj)
        if stwgt is None:
            return None

        children.append(stwgt)
        wgtr[node] += stwgt

    if children:
        avg = sorted(children)[len(children)/2]
        for i, w in enumerate(children):
            if w != avg:
                adj = adjd[node][i]
                print node, '->', adj, wgtd[adj]-w+avg
                return None

    return wgtr[node]

rec(root)
