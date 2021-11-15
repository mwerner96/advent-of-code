def check_vowels(line):
    cnt = 0
    for c in line:
        if c in 'aeiou':
            cnt += 1
    return cnt >= 3


def check_pairs(line):
    for a, b in zip(line[:-1], line[1:]):
        if a == b:
            return True
    return False


def check_bad(line):
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in line:
            return False
    return True


with open('input') as f:
    lines = f.readlines()

lines = [line for line in lines if check_vowels(line)]
lines = [line for line in lines if check_pairs(line)]
lines = [line for line in lines if check_bad(line)]

print(len(lines))
