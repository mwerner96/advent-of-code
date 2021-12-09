import networkx as nx
import math

with open('input') as f:
    area = nx.Graph()
    for y, line in enumerate(f.readlines()):
        for x, depth in enumerate(line.strip()):
            area.add_node((x, y))
            if x > 0:
                area.add_edge((x, y), (x-1, y))
            if y > 0:
                area.add_edge((x, y), (x, y-1))
            area.nodes[(x, y)]['depth'] = depth

for x, y in area.nodes:
    if area.nodes[(x, y)]['depth'] == '9':
        area.remove_edges_from([
            ((x, y), (x-1, y)),
            ((x, y), (x+1, y)),
            ((x, y), (x, y-1)),
            ((x, y), (x, y+1))
        ])

component_sizes = [len(c) for c in sorted(nx.connected_components(area), key=len, reverse=True)]

print(math.prod(component_sizes[:3]))
