from itertools import product

with open("star_21.txt", "rt") as f:
    data = f.read()

rules = {}
for rule_raw in data.strip().split('\n'):
    left, right = rule_raw.split('=>')
    leftb = [c == '#' for c in left if c in '.#']
    rightb = [c == '#' for c in right if c in '.#']

    side = 2 if len(leftb) == 4 else 3

    for h, v, d in product([False, True], repeat=3):
        cleft = list(leftb)
        if h:
            cleft = [cleft[(side-i-1)*side+j] for i in xrange(side) for j in xrange(side)]
        if v:
            cleft = [cleft[i*side + side-j-1] for i in xrange(side) for j in xrange(side)]
        if d:
            cleft = [cleft[j*side + i] for i in xrange(side) for j in xrange(side)]

        rules[tuple(cleft)] = tuple(rightb)

start_state = (0, 1, 0, 0, 0, 1, 1, 1, 1)

def iter_from_3(iters, orig_state3):
    cside, cstate = 3, map(bool, orig_state3)

    for itern in xrange(iters):
        nmside = 3 if cside % 2 == 0 else 4
        nside = nmside * (cside / (nmside - 1))
        nstate = [False] * (nside ** 2)
        for i, j in product(xrange(cside / (nmside-1)), repeat=2):
            cright = rules[tuple(cstate[(i*(nmside-1)+di)*cside + (j*(nmside-1)+dj)] for di, dj in product(xrange(nmside-1), repeat=2))]
            for di, dj in product(xrange(nmside), repeat=2):
                nstate[(i*nmside+di)*nside + (j*nmside+dj)] = cright[di*nmside+dj]

        cside, cstate = nside, nstate

    return cstate

print sum(iter_from_3(5, start_state))

step3_res = {}
step3_sum = {}

for state in product((False, True), repeat=9):
    end_state = iter_from_3(3, state)
    step3_sum[tuple(state)] = sum(end_state)

    step3_res[tuple(state)] = res = {}
    for i, j in product(xrange(3), repeat=2):
        substate = [None] * 9
        for di, dj in product(xrange(3), repeat=2):
            substate[di*3+dj] = end_state[(i*3+di)*9 + j*3+dj]

        res[tuple(substate)] = res.get(tuple(substate), 0) + 1

counts = {tuple(map(bool, start_state)): 1}
powers = 6
for powern in xrange(powers):
    new_counts = {}

    if powern < powers-1:
        for state, count in counts.iteritems():
            for estate, ecount in step3_res[state].iteritems():
                new_counts[estate] = new_counts.get(estate, 0) + count * ecount

        counts = new_counts

    else:
        res = 0
        for state, count in counts.iteritems():
            res += step3_sum[state] * count

        print res
