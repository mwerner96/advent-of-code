import pprint
import re

rules = []
strings = []
with open('input') as f:
    while (line := f.readline()) != '\n':
        rules.append(line)
    while line := f.readline():
        strings.append(line.strip())

rulez = {}
for rule in rules:
    key, rule = rule.split(':')
    key = int(key)
    rule = rule.split()
    if '"a"' in rule or '"b"' in rule:
        rule = rule[0][1]
    else:
        subrule = 0
        r = [[]]
        for c in rule:
            if c != '|':
                r[subrule].append(int(c))
            else:
                r.append([])
                subrule += 1
        rule = r
    rulez[key] = rule


def build_regex(idx=0):
    rule = rulez[idx]
    if rule == 'a' or rule == 'b':
        return rule
    regex = '(' if len(rule) > 1 else ''
    for i, sub in enumerate(rule):
        for idx_sub in sub:
            regex += (build_regex(idx_sub))
        if i+1 < len(rule):
            regex += ('|')
    regex += ')' if len(rule) > 1 else ''
    return regex


matcher = re.compile(build_regex())
matches = 0
for string in strings:
    if matcher.fullmatch(string):
        matches += 1

print(matches)
