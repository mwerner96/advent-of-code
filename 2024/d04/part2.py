# M S
#  A
# M S

# all possible rotations of the above,
# read from top left to bottom right:
WORDS = {"MSAMS", "MMASS", "SMASM", "SSAMM"}


with open("input") as f:
    lines = [line + "  " for line in f.read().splitlines()]
    lines.append(" " * len(lines[0]))
    lines.append(" " * len(lines[0]))

sum = 0
for y in range(len(lines) - 2):
    for x in range(len(lines[0]) - 2):
        word = lines[y][x]
        word += lines[y][x + 2]
        word += lines[y + 1][x + 1]
        word += lines[y + 2][x]
        word += lines[y + 2][x + 2]

        sum += 1 if word in WORDS else 0

print(sum)
