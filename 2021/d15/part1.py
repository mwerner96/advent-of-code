import networkx as nx

with open('input') as f:
    area = nx.DiGraph()
    max_pos = (0, 0)
    for y, line in enumerate(f.readlines()):
        for x, depth in enumerate(map(int, line.strip())):
            area.add_node((x, y))
            area.nodes[(x, y)]['weight'] = depth
            if x > 0:
                area.add_edge((x, y), (x-1, y), weight=area.nodes[(x-1, y)]['weight'])
                area.add_edge((x-1, y), (x, y), weight=depth)
            if y > 0:
                area.add_edge((x, y), (x, y-1), weight=area.nodes[(x, y-1)]['weight'])
                area.add_edge((x, y-1), (x, y), weight=depth)
            if x > max_pos[0] and y > max_pos[1]:
                max_pos = (x, y)

print(nx.algorithms.shortest_paths.astar.astar_path_length(area, (0, 0), max_pos, weight='weight'))
