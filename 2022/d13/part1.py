import ast


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


message_pairs = (
    tuple(ast.literal_eval(msg) for msg in pair)
    for pair in (
        messages.splitlines() for messages in open("input").read().split("\n\n")
    )
)


print(
    sum(
        idx
        for idx, (l, r) in enumerate(message_pairs, start=1)
        if compare_lists(l, r) == 1
    )
)
