data = """
4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3
"""

# data = """
# 0 2 7 0
# """

banks = tuple(map(int, data.strip().split()))
n = len(banks)

vis, steps = {}, 0
while banks not in vis:
    vis[banks] = steps
    steps += 1

    amount, nidx = max((v, -i) for v, i in zip(banks, range(n)))

    # print banks, amount, -nidx, fv, loopsize, steps, vis

    nbanks = list(banks)
    nbanks[-nidx] = 0
    for i in xrange(1, amount+1):
        nbanks[(i-nidx)%n] += 1

    banks = tuple(nbanks)

print steps, steps-vis[banks]
