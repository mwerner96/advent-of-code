NEXT_DIR = {
    (0, -1): (1, 0),  # up to right
    (1, 0): (0, 1),  # right to down
    (0, 1): (-1, 0),  # down to left
    (-1, 0): (0, -1),  # left to up
}


with open("input") as f:
    area = [list(line) for line in f.read().splitlines()]

STARTING_POS = None  # to be initialized
STARTING_DIR = (0, -1)

pos = (0, 0)  # to be initialized
dir = STARTING_DIR  # upwards in y-direction, we assume "^" as the starting move

LEN_Y = len(area)
LEN_X = len(area[0])

# find the starting position
for y, line in enumerate(area):
    try:
        x = line.index("^")
        pos = (x, y)
        STARTING_POS = pos
        break
    except:
        pass

# find the natural path
natural_path = set()
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
    pos = next_pos
    if pos != STARTING_POS:
        natural_path.add(pos)

loops = 0
for x, y in natural_path:
    try_area = [[c for c in l] for l in area]
    try_area[y][x] = "#"

    been_there = set()
    pos = STARTING_POS
    dir = STARTING_DIR

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
        if try_area[next_pos[1]][next_pos[0]] == "#":
            dir = NEXT_DIR[dir]
            continue

        # business as usual
        pos = next_pos

        move = (pos, dir)
        if move in been_there:
            # already been here! circle!
            loops += 1
            break
        been_there.add(move)

print(loops)
