sens_beac = []

for line in open("input").read().splitlines():
    tokens = line.replace(",", " ").replace("=", " ").replace(":", " ").split()
    sens_beac.append(
        ((int(tokens[3]), int(tokens[5])), (int(tokens[-3]), int(tokens[-1])))
    )

LINE = 2000000
line_target = {}
for (x_s, y_s), (x_b, y_b) in sens_beac:
    if y_b == LINE:
        line_target[x_b] = "B"
    manhattan = abs(x_s - x_b) + abs(y_s - y_b)
    rest = manhattan - abs(y_s - LINE)
    if rest >= 0:
        line_max = x_s + rest
        line_min = x_s - rest
        for idx in range(line_min, line_max + 1):
            if idx not in line_target:
                line_target[idx] = "#"

print(sum(1 for _, tok in line_target.items() if tok == "#"))
