from collections import defaultdict


with open('input') as f:
    polymer = f.readline().strip()
    pairs = defaultdict(int)
    for a, b in zip(polymer, polymer[1:]):
        pairs[a+b] += 1
    elements = defaultdict(int)
    for e in polymer:
        elements[e] += 1
    f.readline()
    rules = {
        pair: element
        for pair, element
        in (
            l.strip().split(' -> ')
            for l
            in f.readlines()
        )
    }

for _ in range(40):
    new_pairs = defaultdict(int)
    for pair in pairs:
        if pair in rules:
            new_pairs[pair[0]+rules[pair]] += pairs[pair]
            new_pairs[rules[pair]+pair[1]] += pairs[pair]
            elements[rules[pair]] += pairs[pair]
        else:
            print('else')
            new_pairs[pair] += pairs[pair]
    pairs = new_pairs

print(max(elements.values()) - min(elements.values()))
