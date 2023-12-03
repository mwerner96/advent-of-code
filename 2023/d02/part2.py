from math import prod

MAXVALS = {"red": 12, "green": 13, "blue": 14}

with open("input") as f:
    games = [l[l.find(": ") + 2 :] for l in f.read().splitlines()]

games = [g.split("; ") for g in games]

powers = 0

for idx, game in enumerate(games, start=1):
    MAXVALS = {"red": 0, "green": 0, "blue": 0}
    power = 1
    for round in game:
        pulls = [pull.split() for pull in round.split(", ")]
        for pull in pulls:
            if int(pull[0]) > MAXVALS[pull[1]]:
                MAXVALS[pull[1]] = int(pull[0])
    powers += prod(MAXVALS.values())

print(powers)
