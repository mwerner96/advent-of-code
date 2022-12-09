cmd = {
    "U": (1, 0),
    "D": (-1, 0),
    "R": (0, 1),
    "L": (0, -1),
}

moves = (
    (direction, int(amount))
    for direction, amount in (l.split() for l in open("input").read().splitlines())
)

rope = [(0, 0) for _ in range(10)]

visited = {rope[-1]}


for move in moves:
    for _ in range(move[1]):
        rope[0] = (rope[0][0] + cmd[move[0]][0], rope[0][1] + cmd[move[0]][1])

        for idx in range(len(rope) - 1):
            if abs(rope[idx][0] - rope[idx + 1][0]) > 1:
                rope[idx + 1] = (
                    rope[idx + 1][0] + (1 if rope[idx][0] > rope[idx + 1][0] else -1),
                    rope[idx + 1][1],
                )
                if abs(rope[idx][1] - rope[idx + 1][1]) > 0:
                    rope[idx + 1] = (
                        rope[idx + 1][0],
                        rope[idx + 1][1]
                        + (1 if rope[idx][1] > rope[idx + 1][1] else -1),
                    )

            if abs(rope[idx][1] - rope[idx + 1][1]) > 1:
                rope[idx + 1] = (
                    rope[idx + 1][0],
                    rope[idx + 1][1] + (1 if rope[idx][1] > rope[idx + 1][1] else -1),
                )
                if abs(rope[idx][0] - rope[idx + 1][0]) > 0:
                    rope[idx + 1] = (
                        rope[idx + 1][0]
                        + (1 if rope[idx][0] > rope[idx + 1][0] else -1),
                        rope[idx + 1][1],
                    )

        visited.add(rope[-1])

print(len(visited))
