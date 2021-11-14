with open('input') as f:
    pos = (0, 0)
    moves = {
        '<': (-1, 0),
        '^': (0, 1),
        '>': (1, 0),
        'v': (0, -1),
    }

    def update(pos, move):
        move = moves[move]
        return (
            pos[0] + move[0],
            pos[1] + move[1]
        )

    houses = {pos}
    while c := f.read(1):
        pos = update(pos, c)
        houses.add(pos)

    print(len(houses))
