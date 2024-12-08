from itertools import combinations


with open("input") as f:
    rules = {}
    while True:
        line = f.readline().strip()
        if len(line) == 0:
            break

        rule = tuple(int(s) for s in line.split("|"))

        rules[min(rule), max(rule)] = rule

    jobs = [[int(s) for s in line.split(",")] for line in f.read().splitlines()]


sum = 0
for job in jobs:
    rule_ok = True
    for pair in combinations(job, 2):
        rule = rules[(min(pair), max(pair))]
        if rule != pair:
            rule_ok = False
            break
    if rule_ok:
        sum += job[int((len(job) - 1) / 2)]


print(sum)
