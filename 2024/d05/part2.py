from itertools import combinations
from functools import cmp_to_key


with open("input") as f:
    rules = {}
    while True:
        line = f.readline().strip()
        if len(line) == 0:
            break

        rule = tuple(int(s) for s in line.split("|"))
        rules[min(rule), max(rule)] = rule

    jobs = [[int(s) for s in line.split(",")] for line in f.read().splitlines()]


broken_jobs = []
for job in jobs:
    for pair in combinations(job, 2):
        rule = rules[(min(pair), max(pair))]
        if rule != pair:
            broken_jobs.append(job)
            break


sum = 0
for job in broken_jobs:
    sorted_job = sorted(
        job,
        key=cmp_to_key(lambda a, b: -1 if a == rules[(min(a, b), max(a, b))][0] else 1),
    )
    sum += sorted_job[int((len(sorted_job) - 1) / 2)]


print(sum)
