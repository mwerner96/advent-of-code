from itertools import product
from collections import Counter
from functools import cache

TOP_SCORE = 21


def roll_results():
    return Counter((sum(rolls) for rolls in product(range(1, 4), repeat=3))).items()


@cache
def simulate(pos, score=(0, 0)):
    if score[0] >= TOP_SCORE:
        return 1, 0
    if score[1] >= TOP_SCORE:
        return 0, 1

    wins = [0, 0]
    for roll, count in roll_results():
        newpos = (pos[0] + roll) % 10
        newscore = score[0] + newpos + 1
        b, a = simulate((pos[1], newpos), (score[1], newscore))
        wins[0] += a * count
        wins[1] += b * count

    return wins


with open('input') as f:
    pos = [int(l.strip().split()[-1]) - 1 for l in f.readlines()]


print(max(simulate(tuple(pos))))
