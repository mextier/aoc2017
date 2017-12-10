lst = range(256)
lengths = (199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192)

# lst = range(5)
# lengths = (3, 4, 1, 5)

def one_round(lengths):
    global lst, cur, skip
    for l in lengths:
        lst = lst[cur:] + lst[:cur]
        lst = list(reversed(lst[:l])) + lst[l:]
        lst = lst[-cur:] + lst[:-cur]

        cur = (cur + l + skip) % len(lst)
        skip += 1

cur, skip = 0, 0
one_round(lengths)

# print lst
print lst[0]*lst[1]

p2lengths = map(ord, filter(lambda c: c not in ' ()', str(lengths))) + [17, 31, 73, 47, 23]
lst = range(256)

cur, skip = 0, 0
for rn in xrange(64):
    one_round(p2lengths)

dense = []
for i in xrange(0, len(lst), 16):
    dense.append(reduce(lambda c, a: c^a, lst[i:i+16]))

print "".join(map(lambda c: "%02x" % c, dense))
