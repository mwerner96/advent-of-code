with open("input") as f:
    lines = f.read().splitlines()

left, right = list(zip(*(l.split("   ") for l in lines)))

left = sorted(int(x) for x in left)
right = sorted(int(x) for x in right)

print(sum(abs(l - r) for l, r in zip(left, right)))
