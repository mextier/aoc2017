import re
import operator
from itertools import product, izip
from math import sqrt

eps = 1e-5

with open("star_20.txt", "r") as f:
    lines = filter(bool, f.read().split('\n'))

# lines = filter(bool, """
# p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
# p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
# p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
# p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>
# """.split('\n'))

regex = re.compile('^p=<([-0-9]+),([-0-9]+),([-0-9]+)>, '
                   'v=<([-0-9]+),([-0-9]+),([-0-9]+)>, '
                   'a=<([-0-9]+),([-0-9]+),([-0-9]+)>')

dist = 1000000L
bestdist = (dist**8, None)

particles = []
for index, line in enumerate(lines):
    ints = map(long, regex.match(line).groups())
    p, v, a = ints[0:3], ints[3:6], ints[6:9]

    # p+vT+aT^2/2

    e = map(lambda pc, vc, ac: pc + vc*dist + ac*dist*dist/2, p, v, a)
    md = sum(map(abs, e))

    particles.append((p, v, a))

    bestdist = min(bestdist, (md, index))

print bestdist

# tried to code the quadratic solver first, but simulation suffices here
for steps in xrange(1000):
    pset = {}
    for i in xrange(len(particles)-1, -1, -1):
        p, v, a = particles[i]
        for j in xrange(3):
            v[j] += a[j]
            p[j] += v[j]
        pt = tuple(p)
        if pt in pset:
            removed = True
            if pset[pt] is not None:
                del particles[pset[pt]]
                pset[pt] = None
            del particles[i]
        else:
            pset[pt] = i

    print len(particles)
