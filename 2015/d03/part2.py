with open('input') as f:
    santa = (0, 0)
    robos = (0, 0)
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

    houses = {santa}
    who = True
    while c := f.read(1):
        if who:
            santa = update(santa, c)
            houses.add(santa)
        else:
            robos = update(robos, c)
            houses.add(robos)
        who = not who

    print(len(houses))
