from collections import defaultdict
from itertools import product

lines = open("input").read().splitlines()

pwd = []
tree = {}

for l in lines:
    if l.startswith("$"):
        cmd = l.split()
        if cmd[1] == "cd":
            if cmd[2] == "..":
                pwd.pop()
            else:
                pwd.append(cmd[2])
    else:
        first, second = l.split()
        path = "/".join(pwd)
        if path not in tree:
            # this cannot be replaced by defaultdict
            # we would miss directories with no files but with subdirectories
            # which still count towards the total score
            tree[path] = 0
        if first != "dir":
            tree[path] += int(first)

recsize = defaultdict(int)
for dir, other in product(tree.keys(), tree.keys()):
    if dir in other:
        recsize[dir] += tree[other]

print(sum(size for size in recsize.values() if size < 100000))
