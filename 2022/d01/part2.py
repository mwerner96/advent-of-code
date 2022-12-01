print(
    sum(
        sorted(
            sum(int(food) for food in bag.splitlines())
            for bag in open("input").read().split("\n\n")
        )[-3:]
    )
)
