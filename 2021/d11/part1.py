import networkx as nx

EDGE = 10
ITERATIONS = 100

with open('input') as f:
    area = nx.Graph()
    for y, line in enumerate(f.readlines()):
        for x, energy in enumerate(line.strip()):
            area.add_node((x, y))
            if x > 0:
                area.add_edge((x, y), (x-1, y))
                if y > 0:
                    area.add_edge((x, y), (x-1, y-1))
            if y > 0:
                area.add_edge((x, y), (x, y-1))
                if x < (EDGE-1):
                    area.add_edge((x, y), (x+1, y-1))
            area.nodes[(x, y)]['energy'] = int(energy)

flash = 0
for _ in range(0, ITERATIONS):
    for octopus in area.nodes:
        area.nodes[octopus]['energy'] += 1

    flashed = set()
    while True:
        for octopus in area.nodes:
            if area.nodes[octopus]['energy'] > 9 and octopus not in flashed:
                flash += 1
                flashed.add(octopus)
                for neighbour in area[octopus]:
                    area.nodes[neighbour]['energy'] += 1
                break
        else:
            break

    for octopus in area.nodes:
        if area.nodes[octopus]['energy'] > 9:
            area.nodes[octopus]['energy'] = 0

print(flash)
