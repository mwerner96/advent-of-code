def check_pairs(line):
    while len(line) > 4:
        pair = line[:2]
        check = line[2:]
        if pair in check:
            return True
        line = line[1:]
    return False


def check_skip(line):
    for a, b in zip(line[:-2], line[2:]):
        if a == b:
            return True
    return False


with open('input') as f:
    lines = f.readlines()

lines = [line for line in lines if check_pairs(line)]
lines = [line for line in lines if check_skip(line)]

print(len(lines))
