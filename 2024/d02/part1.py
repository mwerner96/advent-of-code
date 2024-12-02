with open("input") as f:
    lines = (list(int(x) for x in line.split()) for line in f.read().splitlines())

safe = 0

for line in lines:
    if line[0] > line[-1]:
        line = list(reversed(line))

    distances = set(y - x for x, y in zip(line, line[1:]))
    disallowed = distances.difference({1, 2, 3})
    if len(disallowed) == 0:
        safe += 1

print(safe)
