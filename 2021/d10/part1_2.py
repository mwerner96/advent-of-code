import statistics

with open('input') as f:
    lines = [line.strip() for line in f.readlines()]

matching = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

errors = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

scores = []
error = 0
for line in lines:
    # build stack for part 1
    broken = False
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            opening = stack.pop()
            if opening != matching[c]:
                error += errors[c]
                broken = True
                break

    if broken:
        continue

    # build score for part 2
    score = 0
    for c in reversed(stack):
        score *= 5
        score += autocomplete[c]

    scores.append(score)

# part 1
print(error)

# part 2
print(statistics.median(scores))
