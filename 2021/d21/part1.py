from itertools import cycle

TOP_SCORE = 1000


def deterministic_dice():
    dice = cycle(range(1, 101))
    rolls = 0
    while True:
        rolls += 3
        yield next(dice) + next(dice) + next(dice), rolls


with open('input') as f:
    pos = [int(l.strip().split()[-1]) - 1 for l in f.readlines()]

active = 0
next_player = [1, 0]
score = [0, 0]
sum_rolls = 0
for res, rolls in deterministic_dice():
    pos[active] += res
    pos[active] %= 10
    score[active] += pos[active] + 1
    if score[active] >= TOP_SCORE:
        sum_rolls = rolls
        break
    active = next_player[active]

print(sum_rolls * score[next_player[active]])
