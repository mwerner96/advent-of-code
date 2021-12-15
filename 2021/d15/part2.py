import networkx as nx
from itertools import product

with open('input') as f:
    lines = list(f.read().splitlines())

area = nx.DiGraph()
max_pos = (len(lines[0]), len(lines))
for y, line in enumerate(lines):
    for x, depth in enumerate(map(int, line.strip())):
        for coord, increase in (
            ((x + n*max_pos[0], y + m*max_pos[1]), n+m)
            for n, m
            in product(range(5), repeat=2)
        ):
            area.add_node(coord)
            new_depth = depth + increase
            area.nodes[coord]['weight'] = new_depth if new_depth < 10 else new_depth - 9

max_pos = (max_pos[0] * 5, max_pos[1] * 5)

for x, y in product(range(max_pos[0]), range(max_pos[1])):
    if x > 0:
        area.add_edge((x, y), (x-1, y), weight=area.nodes[(x-1, y)]['weight'])
        area.add_edge((x-1, y), (x, y), weight=area.nodes[(x, y)]['weight'])
    if y > 0:
        area.add_edge((x, y), (x, y-1), weight=area.nodes[(x, y-1)]['weight'])
        area.add_edge((x, y-1), (x, y), weight=area.nodes[(x, y)]['weight'])

print(nx.algorithms.shortest_paths.astar.astar_path_length(area, (0, 0), (max_pos[0] - 1, max_pos[1] - 1), weight='weight'))
