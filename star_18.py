# fuck this, never solve AoC @ 2 AM

data = """
set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 316
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
"""

# Data = """
# set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2
# """

# data = """
# snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d
# """

insn = map(lambda l: l.strip().split(), data.strip().split('\n'))

def make_regs():
    return dict((chr(ord('a') + i), 0) for i in xrange(26))

def run(regs, c, rcvif):

    def val(s):
        try:
            v = int(s)
            return v
        except:
            return regs.get(s)

    while 0 <= c < len(insn):
        cmd, args = insn[c][0], insn[c][1:]

        if cmd == 'set':
            regs[args[0]] = val(args[1])
            c += 1

        elif cmd == 'snd':
            snd = val(args[0])
            return (c+1, 'snd', snd)

        elif cmd == 'add':
            regs[args[0]] += val(args[1])
            c += 1

        elif cmd == 'mul':
            regs[args[0]] *= val(args[1])
            c += 1

        elif cmd == 'mod':
            regs[args[0]] %= val(args[1])
            c += 1

        elif cmd == 'rcv':
            if rcvif:
                if val(args[0]) != 0:
                    return (c+1, 'rcv')
                else:
                    c += 1
            else:
                assert 'a' <= args[0] <= 'z'
                return (c+1, 'rcv', args[0])

        elif cmd == 'jgz':
            c += val(args[1]) if val(args[0]) > 0 else 1
            # if args[0] == 'f':
                # print 'jgz', c, val(args[0]), args[1]

        else:
            raise

    return (-1, 'exit')

c, snd, p1regs = 0, None, make_regs()

while True:
    res = run(p1regs, c, rcvif = True)
    if res[1] == 'snd':
        c, _, snd = res
    elif res[1] == 'rcv':
        print 'recover', snd
        break
    elif res[1] == 'exit':
        break

from collections import deque

st = [[0, make_regs(), deque()] for i in (0, 1)]
st[1][1]['p'] = 1

numsend = 0

def pregs(r):
    return str([(k, v) for k, v in r.iteritems() if v])

while st[0][2] or st[1][2] or numsend == 0:
    for i in (0,1):
        print '---', i
        print st[0][0], pregs(st[0][1]), len(st[0][2]), st[0][2]
        print st[1][0], pregs(st[1][1]), len(st[1][2]), st[1][2]

        while True:
            cc, cregs, cq = st[i]
            res = run(cregs, cc, rcvif = False)
            # print 'run', i, st[i][0], pregs(st[i][1]), res

            if res[1] == 'snd':
                nc, _, val = res
                st[1-i][2].append(val)
                st[i][0] = nc

                if i == 1:
                    numsend += 1

            elif res[1] == 'rcv':
                nc, _, reg = res
                if cq:
                    st[i][0] = nc
                    cregs[reg] = cq.popleft()
                else:
                    st[i][0] = nc-1
                    break

            elif res[1] == 'exit':
                st[i][0] == -1
                break

print numsend
