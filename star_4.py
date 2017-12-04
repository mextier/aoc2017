from star_4_input import data

valid_count, valid_count_2 = 0, 0
for passphrase in data.strip().split('\n'):
    words = passphrase.split()
    valid = bool(len(set(words)) == len(words))

    slist = map(lambda w: tuple(sorted(w)), words)
    slist.sort()

    valid_count += valid
    valid_count_2 += bool(len(set(slist)) == len(slist))

print valid_count, valid_count_2
