from itertools import product

trees = [[int(c) for c in line] for line in open("input").read().splitlines()]

visible = [[False for _ in range(len(trees[0]))] for _ in range(len(trees))]

highest_l = -1
highest_r = -1
for line, column in product(range(len(trees)), range(len(trees[0]))):
    if column == 0:
        highest_l = -1
        highest_r = -1
    if trees[line][column] > highest_l:
        visible[line][column] = True
    if trees[line][-(column + 1)] > highest_r:
        visible[line][-(column + 1)] = True
    highest_l = max(highest_l, trees[line][column])
    highest_r = max(highest_r, trees[line][-(column + 1)])

highest_t = -1
highest_b = -1
for column, line in product(range(len(trees[0])), range(len(trees))):
    if line == 0:
        highest_t = -1
        highest_b = -1
    if trees[line][column] > highest_t:
        highest_t = trees[line][column]
        visible[line][column] = True
    if trees[-(line + 1)][column] > highest_b:
        highest_b = trees[-(line + 1)][column]
        visible[-(line + 1)][column] = True


print(sum(sum(1 for val in vals if val) for vals in visible))
