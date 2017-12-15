s = [277, 349]
f = (16807, 48271)
m = (4, 8)
modulo = 2147483647

res = 0
for _ in xrange(40000000):
    for i in (0, 1):
        s[i] = (s[i] * f[i]) % modulo

    if (s[0] & 0xffff) == (s[1] & 0xffff):
        res += 1

print res

res2 = 0
for _ in xrange(5000000):
    for i in (0, 1):
        while True:
            s[i] = (s[i] * f[i]) % modulo
            if s[i] % m[i] == 0:
                break

    if (s[0] & 0xffff) == (s[1] & 0xffff):
        res2 += 1

print res2
