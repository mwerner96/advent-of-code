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


max_score = 0

for x, y in product(range(len(visible)), range(len(visible[0]))):
    score = 1
    for direction_x, direction_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        distance = 0
        cur_x = x
        cur_y = y
        while True:
            cur_x += direction_x
            cur_y += direction_y
            if (
                cur_x < 0
                or cur_x >= len(visible)
                or cur_y < 0
                or cur_y >= len(visible[0])
            ):
                break
            distance += 1
            if trees[cur_x][cur_y] >= trees[x][y]:
                break
        score *= distance
    max_score = max(score, max_score)

print(max_score)
