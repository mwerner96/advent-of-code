print(
    sum(
        (
            {
                "A": {"X": 4, "Y": 8, "Z": 3},
                "B": {"X": 1, "Y": 5, "Z": 9},
                "C": {"X": 7, "Y": 2, "Z": 6},
            }[s[0]][s[2]]
            for s in open("input").read().splitlines()
        )
    )
)
