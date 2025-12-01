with open("input") as f:
    lines = f.read().splitlines()

ops = (int(l[1:]) if l[0] == "R" else -int(l[1:]) for l in lines)

pos = 50
at_0 = 0
for op in ops:
    pos += op
    if (pos % 100) == 0:
        at_0 += 1

print(at_0)
