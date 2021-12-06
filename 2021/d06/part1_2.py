def simulate(population):
    population = population[1:] + population[:1]
    population[6] += population[-1]
    return population


with open('input') as f:
    fish = list(map(int, f.readline().strip().split(',')))
    fish = [fish.count(i) for i in range(0, 9)]

for _ in range(0, 80):
    fish = simulate(fish)
print(sum(fish))

for _ in range(80, 256):
    fish = simulate(fish)
print(sum(fish))
