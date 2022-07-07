totalfuel = 0

for fuel in (int(l) // 3 - 2 for l in open("input").readlines()):
    fuelfuels = [fuel]
    while fuelfuels[-1] != 0:
        thisfuel = fuelfuels[-1] // 3 - 2
        fuelfuels.append(thisfuel if thisfuel >= 0 else 0)
    totalfuel += sum(fuelfuels)

print(totalfuel)
