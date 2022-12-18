import networkx as nx
from itertools import product

cubes = {tuple(int(coord) for coord in line.split(",")) for line in open("input").read().splitlines()}

neighbours = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

max_x = 0
min_x = 100
max_y = 0
min_y = 100
max_z = 0
min_z = 100

for x, y, z in cubes:
    max_x = max(max_x, x+2)
    min_x = min(min_x, x-2)
    max_y = max(max_y, y+2)
    min_y = min(min_y, y-2)
    max_z = max(max_z, z+2)
    min_z = min(min_z, z-2)

negated_cubes = {coord for coord in product(range(min_x, max_x), range(min_y, max_y), range(min_z, max_z)) if coord not in cubes}

negated_graph = nx.Graph()
for x, y, z in negated_cubes:
    for a, b, c in neighbours:
        neighbour = (x+a, y+b, z+c)
        if neighbour in negated_cubes:
            negated_graph.add_edge((x, y, z), neighbour)

largest_negated = max(nx.connected_components(negated_graph), key=len)

cubes = {coord for coord in product(range(min_x, max_x), range(min_y, max_y), range(min_z, max_z)) if coord not in largest_negated}

empty_sides = 0
for x, y, z in cubes:
    empty_sides += 6 - sum(1 for side in ((x+a, y+b, z+c) for a, b, c in neighbours) if side in cubes)

print(empty_sides)
