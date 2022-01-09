def step(z, num, cmds):
    x = (z % 26) + cmds[1]
    z //= cmds[0]

    if x != num:
        z *= 26
        z += cmds[2] + num
    return z


with open('input') as f:
    commands = [l.split()[-1] for l in f.readlines()]
    commands = [
        [
            int(c)
            for c
            in [commands[i + 4], commands[i+5], commands[i+15]]
        ]
        for i
        in range(0, 252, 18)
    ]

z_vals = {0: 0}

for idx, cmds in enumerate(commands):
    z_vals_new = {}
    ceil = 26 ** (14-idx)
    for z0, num in z_vals.items():
        for pos in range(1, 10):
            candidate = num * 10 + pos
            z = step(z0, pos, cmds)
            if z > ceil:
                continue
            if z in z_vals_new:
                candidate = max(candidate, z_vals_new[z])
            z_vals_new[z] = candidate
    z_vals = z_vals_new

print(z_vals[0])
