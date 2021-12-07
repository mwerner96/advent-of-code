def total_fuel(positions, target):
    def triangular(n):
        return int((n * (n+1)) / 2)
    return sum([triangular(abs(pos - target)) for pos in positions])


with open('input') as f:
    positions = list(map(int, f.readline().strip().split(',')))

best = None
for target in range(0, max(positions)):
    fuel = total_fuel(positions, target)
    if not best:
        best = (fuel, target)
    if best[0] > fuel:
        best = (fuel, target)

print(best[0])
