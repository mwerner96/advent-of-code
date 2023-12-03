MAXVALS = {"red": 12, "green": 13, "blue": 14}

with open("input") as f:
    games = [l[l.find(": ") + 2 :] for l in f.read().splitlines()]

games = [g.split("; ") for g in games]

good_games = 0

for idx, game in enumerate(games, start=1):
    possible = True
    for round in game:
        pulls = [pull.split() for pull in round.split(", ")]
        for pull in pulls:
            if int(pull[0]) > MAXVALS[pull[1]]:
                possible = False
    if possible:
        good_games += idx

print(good_games)
