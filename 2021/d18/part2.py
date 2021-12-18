import json
from math import floor, ceil
from itertools import permutations


def add(a, b):
    sum = [a, b]
    while True:
        exp = explode(sum)
        if exp != sum:
            sum = exp
            continue
        spl = split(sum)
        if spl != sum:
            sum = spl
            continue
        break
    return sum


def make_linear(a):
    if isinstance(a, list):
        linear = ['[']
        linear.extend(make_linear(a[0]))
        linear.append(',')
        linear.extend(make_linear(a[1]))
        linear.append(']')
    else:
        linear = [a]
    return linear


def explode(a, nesting=0):
    a_lin = make_linear(a)
    nesting = 0
    exp_idx = None
    left_idx = None
    # find explosion
    for i, c in enumerate(a_lin):
        if c == '[':
            nesting += 1
        elif c == ']':
            nesting -= 1
        elif c == ',':
            pass
        else:
            left_idx = i
        if nesting == 5:
            exp_idx = i
            break

    if exp_idx == None:
        return a

    # find right
    right_idx = None
    for i in range(exp_idx+5, len(a_lin)):
        if isinstance(a_lin[i], int):
            right_idx = i
            break

    l = a_lin[exp_idx+1]
    r = a_lin[exp_idx+3]

    if left_idx:
        a_lin[left_idx] += l
    if right_idx:
        a_lin[right_idx] += r

    new_a = ''.join((str(c) if isinstance(c, int) else c for c in a_lin[:exp_idx]))
    new_a += '0'
    new_a += ''.join((str(c) if isinstance(c, int) else c for c in a_lin[exp_idx+5:]))
    return json.loads(new_a)


def split(a_in):
    a = a_in.copy()
    for i in range(2):
        if isinstance(a[i], int):
            if a[i] > 9:
                a[i] = [floor(a[i] / 2), ceil(a[i] / 2)]
                return a
        else:
            new_a_i = split(a[i])
            if new_a_i != a[i]:
                a[i] = new_a_i
                return a
    return a


def magnitude(a):
    if isinstance(a, int):
        return a
    return magnitude(a[0]) * 3 + magnitude(a[1]) * 2


with open('input') as f:
    homework = [json.loads(l) for l in f.readlines()]

largest = 0
for a, b in permutations(homework, 2):
    mag = magnitude(add(a, b))
    if mag > largest:
        largest = mag

print(largest)
