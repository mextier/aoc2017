with open('star_16.txt', 'rt') as f:
    data = f.read().strip()

m = 16
order = map(lambda c: chr(ord('a') + c), xrange(m))
moves = data.split(',')

# m = 5
# order = list('abcde')
# moves = ['s1', 'x3/4', 'pe/b']

parsed = []
cur = range(m)

def flush():
    global cur
    if cur != range(m):
        parsed.append(tuple(cur))
        cur = range(m)

for move in moves:
    if move[0] == 's':
        n = int(move[1:])
        cur = [(c + n) % m for c in cur]

    elif move[0] == 'x':
        i, j = map(int, move[1:].split('/'))
        xi, xj = cur.index(i), cur.index(j)
        cur[xi], cur[xj] = j, i

    elif move[0] == 'p':
        flush()

        ni, nj = move[1:].split('/')
        parsed.append(('io', ni, nj))

flush()

def perform(order):
    for p in parsed:
        if p[0] == 'io':
            _, ni, nj = p
            order = list(order)
            i, j = order.index(ni), order.index(nj)
            order[i], order[j] = order[j], order[i]
        else:
            ns = [None] * m
            for i, c in zip(p, order):
                ns[i] = c
            order = ns

    return order

print "".join(perform(list(order)))

n = 1000000000

seen = {}
i, co = 0, list(order)
while True:
    key = "".join(co)
    if key not in seen:
        seen[key] = i
    else:
        print 'loop', seen[key], i
        n = seen[key] + (n - seen[key]) % (i - seen[key])
        break

    i += 1
    co = perform(co)

for _ in xrange(n):
    order = perform(order)

print "".join(order)
