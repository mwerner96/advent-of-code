WORDS = ["XMAS", "SAMX"]

with open("input") as f:
    lines = f.read().splitlines()

tr_lines = ["".join(s) for s in zip(*lines)]

count = 0

# horizontal
for line in lines:
    for word in WORDS:
        count += line.count(word)

# vertical
for line in tr_lines:
    for word in WORDS:
        count += line.count(word)

# diagonal 1
padded = [
    " " * idx + line + " " * (len(line) - idx - 1) for idx, line in enumerate(lines)
]
tr_padded = ["".join(s) for s in zip(*padded)]
for line in tr_padded:
    for word in WORDS:
        count += line.count(word)


# diagonal 2
padded = [
    " " * (len(line) - idx - 1) + line + " " * idx for idx, line in enumerate(lines)
]
tr_padded = ["".join(s) for s in zip(*padded)]
for line in tr_padded:
    for word in WORDS:
        count += line.count(word)


print(count)
