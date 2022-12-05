file = open("input").read().splitlines()

layout = [l for l in file if not l.startswith("move") and l != ""]
commands = [
    (int(c[1]), int(c[3]), int(c[5]))
    for c in (l.split() for l in file if l.startswith("move"))
]

stacks_width = int(layout[-1].split()[-1])
stacks = [[] for _ in range(stacks_width)]

for l in list(reversed(layout))[1:]:
    for i in range(stacks_width):
        idx = 1 + i * 4
        if l[idx] != " ":
            stacks[i].append(l[idx])

for cmd in commands:
    stacks[cmd[2] - 1].extend(stacks[cmd[1] - 1][-cmd[0] :])
    stacks[cmd[1] - 1] = stacks[cmd[1] - 1][: -cmd[0]]

print("".join(s[-1] for s in stacks))
