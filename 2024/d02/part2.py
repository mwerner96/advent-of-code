def checksafe(line):
    distances = set(y - x for x, y in zip(line, line[1:]))
    disallowed = distances.difference({1, 2, 3})
    return len(disallowed) == 0


with open("input") as f:
    lines = (list(int(x) for x in line.split()) for line in f.read().splitlines())

safe = 0

for line in lines:
    if line[0] > line[-1]:
        line = list(reversed(line))

    if checksafe(line):
        safe += 1
    else:
        for idx in range(len(line)):
            if checksafe(line[:idx] + line[idx + 1 :]):
                safe += 1
                break


print(safe)
