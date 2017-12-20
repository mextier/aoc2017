import re

with open("star_20.txt", "r") as f:
    lines = filter(bool, f.read().split('\n'))

regex = re.compile('^p=<([-0-9]+),([-0-9]+),([-0-9]+)>, '
                   'v=<([-0-9]+),([-0-9]+),([-0-9]+)>, '
                   'a=<([-0-9]+),([-0-9]+),([-0-9]+)>')

dist = 1000000L
bestdist = (dist**8, None)

particles = []
for index, line in enumerate(lines):
    ints = map(long, regex.match(line).groups())
    p, v, a = tuple(ints[0:3]), tuple(ints[3:6]), tuple(ints[6:9])

    # p+vT+aT^2/2

    e = map(lambda pc, vc, ac: pc + vc*dist + ac*dist*dist/2, p, v, a)
    md = sum(map(abs, e))

    particles.append((p, v, a))

    bestdist = min(bestdist, (md, index))

print bestdist

while True:
    print len(particles)
    removed = False

    k = 0
    for i in xrange(len(particles)):
        for j in xrange(i+1, len(particles)):
            p1, v1, a1 = particles[i]
            p2, v2, a2 = particles[j]

            k += 1
            if k > 10:
                break

            # (p1-p2) + (v1-v2)T + (a1^2-a2^2)*T^2/2
            #

            ds = map(
                lambda pc1, vc1, ac1, pc2, vc2, ac2:
                (vc1-vc2)**2 - 2*(ac1 - ac2)*(ac1 + ac2)*(pc1-pc2),
                *(particles[i] + particles[j])
            )

            print ds


    if not removed:
        break
