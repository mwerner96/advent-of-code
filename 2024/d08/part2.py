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

        # initialize starting antinode
        ax, ay = a[0], a[1]

        # antinodes in positive direction
        while True:
            if ax >= 0 and ay >= 0 and ax < LEN_X and ay < LEN_Y:
                antinodes[ay][ax] = "#"
            else:
                break

            ax += x_dist
            ay += y_dist

        # initialize starting antinode
        ax, ay = a[0], a[1]

        # antinodes in negative direction
        while True:
            if ax >= 0 and ay >= 0 and ax < LEN_X and ay < LEN_Y:
                antinodes[ay][ax] = "#"
            else:
                break

            ax -= x_dist
            ay -= y_dist

print(sum(line.count("#") for line in antinodes))
