f = sorted([int(line) for line in open('input','r').readlines()])

joltdiff = [0, 0, 1]
prev = 0
for adapter in f:
    joltdiff[adapter - prev - 1] += 1
    prev = adapter

print(joltdiff[0] * joltdiff[2])
