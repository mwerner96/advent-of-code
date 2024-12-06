NEXT_DIR = {
    (0, -1): (1, 0),  # up to right
    (1, 0): (0, 1),  # right to down
    (0, 1): (-1, 0),  # down to left
    (-1, 0): (0, -1),  # left to up
}

with open("input") as f:
    area = [list(line) for line in f.read().splitlines()]

pos = (0, 0)  # to be initialized
dir = (0, -1)  # upwards in y-direction, we assume "^" as the starting move

LEN_Y = len(area)
LEN_X = len(area[0])

# find the starting position
for y, line in enumerate(area):
    try:
        x = line.index("^")
        pos = (x, y)
        area[y][x] = "X"
        break
    except:
        pass

while True:
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])

    # leaving the area
    if (
        next_pos[0] < 0
        or next_pos[1] < 0
        or next_pos[0] >= LEN_X
        or next_pos[1] >= LEN_Y
    ):
        break

    # hitting a wall
    if area[next_pos[1]][next_pos[0]] == "#":
        dir = NEXT_DIR[dir]
        continue

    # business as usual
    area[next_pos[1]][next_pos[0]] = "X"
    pos = next_pos

print(sum(line.count("X") for line in area))
