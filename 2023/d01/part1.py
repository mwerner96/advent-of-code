with open("input") as f:
    lines = f.read().splitlines()

tens = [int(next(d for d in s if d.isdigit())) for s in lines]
ones = [int(next(d for d in reversed(s) if d.isdigit())) for s in lines]

print(sum(tens) * 10 + sum(ones))
# 55538
