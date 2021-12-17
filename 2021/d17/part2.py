def is_inside(coord):
    return (
        coord[0] >= x_min and
        coord[0] <= x_max and
        coord[1] >= y_min and
        coord[1] <= y_max
    )


def sequence(v_x, v_y):
    x, y = (0, 0)
    while True:
        x += v_x
        y += v_y
        v_x -= 1 if v_x > 0 else 0
        v_y -= 1
        if (y < y_min or x > x_max):
            break
        yield (x, y)


with open('input') as f:
    inp = f.readline().strip('target area: x=').strip().split(', y=')
    x_in = list(map(int, inp[0].split('..')))
    x_min, x_max = (min(x_in), max(x_in))
    y_in = list(map(int, inp[1].split('..')))
    y_min, y_max = (min(y_in), max(y_in))

count = 0
for v_x in range(1, x_max+1):
    for v_y in range(y_min, abs(y_min)+1):
        for x, y in sequence(v_x, v_y):
            if is_inside((x, y)):
                count += 1
                break

print(count)
