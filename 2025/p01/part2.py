with open("input") as f:
    lines = f.read().splitlines()

ops = (int(l[1:]) if l[0] == "R" else -int(l[1:]) for l in lines)

pos = 50
at_0 = 0
for op in ops:
    old_pos = pos
    pos += op

    if pos == 0:
        at_0 += 1

    if pos < 0:
        if old_pos != 0:
            at_0 += 1

    at_0 += abs(pos) // 100

    pos %= 100


print(at_0)
