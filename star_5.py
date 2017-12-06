from star_5_input import data

# data = """
# 0
# 3
# 0
# 1
# -3
# """

jumps = map(int, data.strip().split('\n'))

steps, j = 0, 0
while 0 <= j < len(jumps):
    steps += 1
    before = jumps[j]
    jumps[j] += 1 if before < 3 else -1
    j += before

print steps
# print j
# print jumps
