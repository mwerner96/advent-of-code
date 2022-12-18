cubes = {tuple(int(coord) for coord in line.split(",")) for line in open("input").read().splitlines()}

neighbours = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

empty_sides = 0
for x, y, z in cubes:
    empty_sides += 6 - sum(1 for side in ((x+a, y+b, z+c) for a, b, c in neighbours) if side in cubes)

print(empty_sides)
