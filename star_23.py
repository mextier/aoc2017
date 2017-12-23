with open("star_23.txt") as f:
    source = f.read()

lines = source.strip().split('\n')

def regidx(s):
    assert 'a' <= s <= 'h'
    return ord(s)-ord('a')

def val(reg, s):
    return reg[regidx(s)] if 'a' <= s <= 'h' else int(s)

program = []
for line in lines:
    op, x, y = line.split()
    program.append((op, x, y))

regs, ip = [0] * 8, 0

mulinv = 0
while 0 <= ip < len(program):
    op, x, y = program[ip]

    if op == 'set':
        regs[regidx(x)] = val(regs, y)
        ip += 1
    elif op == 'sub':
        regs[regidx(x)] -= val(regs, y)
        ip += 1
    elif op == 'mul':
        mulinv += 1
        regs[regidx(x)] *= val(regs, y)
        ip += 1
    elif op == 'jnz':
        ip += 1 if val(regs, x) == 0 else val(regs, y)
    else:
        raise

print 'mulinv', mulinv

b, c = 108100, 125100

prime = [1] * (c+1)

for i in xrange(2, c+1):
    if not prime[i]:
        continue
    for j in xrange(2*i, c+1, i):
        prime[j] = 0

h = 0
for cb in range(b, c+1, 17):
    h += 1-prime[cb]

print h
