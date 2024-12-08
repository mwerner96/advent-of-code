from collections import defaultdict
from itertools import combinations


with open("input") as f:
    area = [list(line) for line in f.read().splitlines()]
    antinodes = [["." for _ in line] for line in area]

LEN_Y = len(area)
LEN_X = len(area[0])


antennae = defaultdict(set)

for y, line in enumerate(area):
    for x, pos in enumerate(line):
        if pos == ".":
            continue

        antennae[pos].add((x, y))


for antenna_type_positions in antennae.values():
    for a, b in combinations(antenna_type_positions, r=2):
        x_dist = a[0] - b[0]
        y_dist = a[1] - b[1]

        a1x, a1y = (a[0] + x_dist, a[1] + y_dist)
        a2x, a2y = (b[0] - x_dist, b[1] - y_dist)

        if a1x >= 0 and a1y >= 0 and a1x < LEN_X and a1y < LEN_Y:
            antinodes[a1y][a1x] = "#"

        if a2x >= 0 and a2y >= 0 and a2x < LEN_X and a2y < LEN_Y:
            antinodes[a2y][a2x] = "#"

print(sum(line.count("#") for line in antinodes))
