from itertools import product

paths = [
    [tuple(int(n) for n in coord.split(",")) for coord in line.split(" -> ")]
    for line in open("input").read().splitlines()
]

min_x = 10000
max_x = 0
min_y = 10000
max_y = 0

for path in paths:
    for x, y in path:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = 0
        max_y = max(max_y, y)

max_x += max_y
min_x -= max_y
max_y += 2

cave = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
cave[-1] = ["#" for _ in range(len(cave[-1]))]

paths = [[(x - min_x, y - min_y) for x, y in path] for path in paths]

for path in paths:
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        for x, y in product(
            range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1)
        ):
            cave[y][x] = "#"


spawn_real = (500, 0)
spawn = (spawn_real[0] - min_x, 0)


resting = 0
while True:
    x, y = spawn
    while True:
        if cave[y + 1][x] == ".":
            y += 1
        elif cave[y + 1][x - 1] == ".":
            y += 1
            x -= 1
        elif cave[y + 1][x + 1] == ".":
            y += 1
            x += 1
        else:
            cave[y][x] = "o"
            resting += 1
            if (x, y) == spawn:
                print(resting)
                exit()
            break
