from collections import Counter
from itertools import permutations


with open('input') as f:
    polymer = f.readline().strip()
    pairs = Counter(zip(polymer, polymer[1:]))
    f.readline()
    rules = {
        tuple(pair): element
        for pair, element
        in (
            l.strip().split(' -> ')
            for l
            in f.readlines()
        )
    }

assert(set(rules) == set(permutations([*rules.values(), *polymer], 2)))

for _ in range(40):
    new_pairs = Counter()
    for pair, count in pairs.items():
        new_pairs[(pair[0], rules[pair])] += count
        new_pairs[(rules[pair], pair[1])] += count
    pairs = new_pairs

elements = Counter({polymer[0]: 1})
for (_, b), count in pairs.items():
    elements[b] += count

print(max(elements.values()) - min(elements.values()))
