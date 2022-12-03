bags = [set(bag) for bag in open("input").read().splitlines()]
print(
    sum(
        ord(l) - ord("A") + 27 if ord(l) < ord("a") else ord(l) - ord("a") + 1
        for l in (
            (a & b & c).pop() for a, b, c in zip(bags[0::3], bags[1::3], bags[2::3])
        )
    )
)
