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

head = (0, 0)
tail = (0, 0)

visited = {tail}

for move in moves:
    for _ in range(move[1]):
        head = (head[0] + cmd[move[0]][0], head[1] + cmd[move[0]][1])

        if abs(head[0] - tail[0]) > 1:
            tail = (tail[0] + (1 if head[0] > tail[0] else -1), tail[1])
            if abs(head[1] - tail[1]) > 0:
                tail = (tail[0], tail[1] + (1 if head[1] > tail[1] else -1))

        if abs(head[1] - tail[1]) > 1:
            tail = (tail[0], tail[1] + (1 if head[1] > tail[1] else -1))
            if abs(head[0] - tail[0]) > 0:
                tail = (tail[0] + (1 if head[0] > tail[0] else -1), tail[1])

        visited.add(tail)

print(len(visited))
