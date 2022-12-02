print(
    sum(
        (
            {
                "A": {"X": 3, "Y": 4, "Z": 8},
                "B": {"X": 1, "Y": 5, "Z": 9},
                "C": {"X": 2, "Y": 6, "Z": 7},
            }[s[0]][s[2]]
            for s in open("input").read().splitlines()
        )
    )
)
