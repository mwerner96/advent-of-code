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
            tree[path] = []
        if first != "dir":
            tree[path].append((int(first), second))

dirsize = {}
for dir, files in tree.items():
    dirsize[dir] = sum(size for size, _ in files)

recsize = {}
for dir in tree.keys():
    recsize[dir] = 0
    for other in tree.keys():
        if dir in other:
            recsize[dir] += dirsize[other]

print(sum(size for size in recsize.values() if size < 100000))
