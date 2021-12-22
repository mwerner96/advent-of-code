from itertools import product

with open('input') as f:
    steps = [
        (
            step[0] == 'on',
            *[
                (int(step[i]), int(step[i+1])+1)
                for i
                in range(2, 10, 3)
            ]
        )
        for step
        in (
            l.replace('=', ' ').replace('..', ' ').replace(',', ' ').split()
            for l
            in f.readlines()
        )
    ]

cubes_on = set()
for step in steps:
    coords = [*step[1], *step[2], *step[3]]
    if max(coords) > 51 or min(coords) < -50:
        continue
    for coord in product(*[range(*step[i]) for i in range(1, 4)]):
        if step[0]:
            cubes_on.add(coord)
        else:
            cubes_on.discard(coord)

print(len(cubes_on))
