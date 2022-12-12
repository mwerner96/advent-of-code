import networkx as nx

from itertools import product

lines = open("input").read().splitlines()

grid = []
start = None
top = None
for x, line in enumerate(lines):
    grid.append([])
    for y, letter in enumerate(line):
        if letter == "S":
            grid[x].append(ord("a"))
            start = (x, y)
        elif letter == "E":
            grid[x].append(ord("z"))
            top = (x, y)
        else:
            grid[x].append(ord(letter))

g = nx.DiGraph()

for x, y in product(range(len(grid)), range(len(grid[0]))):
    for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x_n, y_n = (x + dir_x, y + dir_y)
        if not (0 <= x_n < len(grid) and 0 <= y_n < len(grid[0])):
            continue
        if grid[x_n][y_n] - grid[x][y] <= 1:
            g.add_edge((x, y), (x_n, y_n))

print(nx.shortest_path_length(g, start, top))
