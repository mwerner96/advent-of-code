from itertools import product


with open("input") as f:
    eqns = []
    for line in f.read().splitlines():
        result, eqn = line.split(": ")
        result = int(result)
        eqn = [int(x) for x in eqn.split()]
        eqns.append((result, eqn))

sum = 0
for result, eqn in eqns:
    for operations in product(
        [lambda a, b: a + b, lambda a, b: a * b, lambda a, b: int(str(a) + str(b))],
        repeat=len(eqn) - 1,
    ):
        calc = eqn[0]
        for idx, (operation, val) in enumerate(tuple(zip(operations, eqn[1:]))):
            calc = operation(calc, val)
        if calc == result:
            sum += result
            break

print(sum)
