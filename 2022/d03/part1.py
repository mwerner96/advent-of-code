print(
    sum(
        ord(l) - ord("A") + 27 if ord(l) < ord("a") else ord(l) - ord("a") + 1
        for l in (
            (a & b).pop()
            for a, b in (
                (set(bag[: len(bag) >> 1]), set(bag[len(bag) >> 1 :]))
                for bag in open("input").read().splitlines()
            )
        )
    )
)
