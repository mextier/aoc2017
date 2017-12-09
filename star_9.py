data = """
{{<!!>},{<!!>},{<!!>},{<!!>}}
"""

data = """{{<a!>},{<a!>},{<a!>},{<ab>}}"""
data = """{{{},{},{{}}}}"""

with open("star_9_input.txt", "rt") as f:
    data = f.read()

from copy import copy

data = data.strip()
s = copy(data)

def eat():
    global s
    c = s[0]
    s = s[1:]
    return c

def peek():
    return s[0]

score, removed = 0, 0

def ignore():
    assert peek() == '!'
    eat()
    eat()

def garbage():
    assert eat() == '<'
    global removed

    while peek() != '>':
        if peek() == '!':
            ignore()
        else:
            removed += 1
            eat()

    assert eat() == '>'

def group(d):
    assert eat() == '{'

    global score
    score += d

    while peek() != '}':
        if peek() == '!':
            ignore()
        elif peek() == '<':
            garbage()
        elif peek() == '{':
            group(d+1)
        else:
            eat()

    assert eat() == '}'

group(1)
print score, removed, ' ->', s
