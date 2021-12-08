with open('input') as f:
    patterns = [(line.split()[:10], line.split()[-4:]) for line in f.readlines()]

total = 0
for _, pattern in patterns:
    for p in pattern:
        if len(p) in [2, 3, 4, 7]:
            total += 1

print(total)
