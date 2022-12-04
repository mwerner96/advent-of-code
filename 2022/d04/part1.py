def is_inside(a, b):
    return a[0] >= b[0] and a[1] <= b[1]


print(
    sum(
        1 if is_inside(a, b) or is_inside(b, a) else 0
        for a, b in (
            ((int(a1), int(a2)), (int(b1), int(b2)))
            for a1, a2, b1, b2 in (
                l.replace("-", ",").split(",")
                for l in open("input").read().splitlines()
            )
        )
    )
)
