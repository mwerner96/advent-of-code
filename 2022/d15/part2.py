sens_beac = []

for line in open("input").read().splitlines():
    tokens = line.replace(",", " ").replace("=", " ").replace(":", " ").split()
    sens_beac.append(
        ((int(tokens[3]), int(tokens[5])), (int(tokens[-3]), int(tokens[-1])))
    )


for idx, line in enumerate(range(0, 4000001)):
    not_covered = [(0, 4000000)]
    for (x_s, y_s), (x_b, y_b) in sens_beac:
        manhattan = abs(x_s - x_b) + abs(y_s - y_b)
        rest = manhattan - abs(y_s - line)
        if rest >= 0:
            line_max = x_s + rest
            line_min = x_s - rest
            not_covered_new = []
            for nc in not_covered:
                # outside
                if line_min > nc[1] or line_max < nc[0]:
                    not_covered_new.append(nc)
                # overlap full
                elif line_min <= nc[0] and line_max >= nc[1]:
                    pass
                # lower overlap
                elif line_min <= nc[0] and line_max < nc[1]:
                    not_covered_new.append((line_max + 1, nc[1]))
                # upper overlap
                elif line_max >= nc[1] and line_min > nc[0]:
                    not_covered_new.append((nc[0], line_min - 1))
                # inside
                elif line_min > nc[0] and line_max < nc[1]:
                    not_covered_new.append((nc[0], line_min - 1))
                    not_covered_new.append((line_max + 1, nc[1]))
                # error
                else:
                    raise

            not_covered = not_covered_new

    if len(not_covered) > 0:
        print(not_covered[0][0] * 4000000 + idx)
        exit()
