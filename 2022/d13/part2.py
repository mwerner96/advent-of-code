import ast
import functools


def compare_lists(l, r):
    if len(l) == 0 and len(r) == 0:
        return 0
    if len(l) == 0:
        return 1
    elif len(r) == 0:
        return -1
    elif isinstance(l[0], int) and isinstance(r[0], int):
        if l[0] < r[0]:
            return 1
        elif l[0] > r[0]:
            return -1
        elif len(l) > 1 or len(r) > 1:
            return compare_lists(l[1:], r[1:])
        else:
            return 0
    elif isinstance(l[0], list) and isinstance(r[0], list):
        comp = compare_lists(l[0], r[0])
        if comp == 0:
            return compare_lists(l[1:], r[1:])
        return comp
    elif isinstance(l[0], int):
        return compare_lists([[l[0]], *l[1:]], r)
    else:
        return compare_lists(l, [[r[0]], *r[1:]])


DIV_1 = [[2]]
DIV_2 = [[6]]


messages = [
    ast.literal_eval(msg) for msg in open("input").read().splitlines() if msg != ""
]
messages.append(DIV_1)
messages.append(DIV_2)


messages.sort(key=functools.cmp_to_key(compare_lists), reverse=True)

print((messages.index(DIV_1) + 1) * (messages.index(DIV_2) + 1))
