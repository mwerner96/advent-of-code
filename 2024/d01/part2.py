with open("input") as f:
    lines = f.read().splitlines()

left, right = list(zip(*(l.split("   ") for l in lines)))

left = sorted(int(x) for x in left)
right = sorted(int(x) for x in right)

howmany = {i: right.count(i) for i in set(left)}

print(sum(x * howmany[x] for x in left))
