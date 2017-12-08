data = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

from star_8_input import data

lines = data.strip().split('\n')

ops = {
    '>': lambda a, ca: a > ca,
    '<': lambda a, ca: a < ca,
    '=>': lambda a, ca: a >= ca,
    '>=': lambda a, ca: a >= ca,
    '<=': lambda a, ca: a <= ca,
    '==': lambda a, ca: a == ca,
    '!=': lambda a, ca: a != ca
}

print data[:10]

prog = []
for line in lines:
    name, op, am_s, if_s, cond_name, op_s, cond_arg_s = line.split()
    am = int(am_s)
    if op == 'inc':
        delta = am
    elif op == 'dec':
        delta = -am
    else:
        raise

    cond_arg = int(cond_arg_s)

    prog.append((name, delta, cond_name, ops[op_s], cond_arg))
    # print name, op, am_s, if_s, cond_name, op_s, cond_arg

reg = {}
ever = float('-inf')
for name, delta, cond_name, lam, ca in prog:
    if not lam(reg.get(cond_name, 0), ca):
        continue

    reg[name] = reg.get(name, 0) + delta
    ever = max(ever, float(reg[name]))

print max(reg.values()), ever
