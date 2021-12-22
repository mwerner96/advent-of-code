from math import prod
from dataclasses import dataclass


@dataclass(frozen=True)
class Cube:
    coord_pairs: tuple

    def overlaps(self, other):
        return all((
            not (pair[0][0] > pair[1][1] or pair[0][1] < pair[1][0])
            for pair
            in zip(self.coord_pairs, other.coord_pairs)
        ))

    @property
    def volume(self):
        return prod((a[1] - a[0] + 1 for a in self.coord_pairs))

    @property
    def x(self):
        return self.coord_pairs[0]

    @property
    def y(self):
        return self.coord_pairs[1]

    @property
    def z(self):
        return self.coord_pairs[2]

    def cut(self, other):
        if not self.overlaps(other):
            return [self]

        pieces = []
        if self.x[0] < other.x[0]:
            pieces.append(Cube((
                (self.x[0], other.x[0]-1),
                self.y,
                self.z
            )))
        if self.x[1] > other.x[1]:
            pieces.append(Cube((
                (other.x[1]+1, self.x[1]),
                self.y,
                self.z
            )))
        if self.y[0] < other.y[0]:
            pieces.append(Cube((
                (max(self.x[0], other.x[0]), min(self.x[1], other.x[1])),
                (self.y[0], other.y[0]-1),
                self.z
            )))
        if self.y[1] > other.y[1]:
            pieces.append(Cube((
                (max(self.x[0], other.x[0]), min(self.x[1], other.x[1])),
                (other.y[1]+1, self.y[1]),
                self.z
            )))
        if self.z[0] < other.z[0]:
            pieces.append(Cube((
                (max(self.x[0], other.x[0]), min(self.x[1], other.x[1])),
                (max(self.y[0], other.y[0]), min(self.y[1], other.y[1])),
                (self.z[0], other.z[0]-1),
            )))
        if self.z[1] > other.z[1]:
            pieces.append(Cube((
                (max(self.x[0], other.x[0]), min(self.x[1], other.x[1])),
                (max(self.y[0], other.y[0]), min(self.y[1], other.y[1])),
                (other.z[1]+1, self.z[1]),
            )))

        return pieces


with open('input') as f:
    steps = [
        (
            step[0] == 'on',
            Cube(
                tuple((
                    (int(step[i]), int(step[i+1]))
                    for i
                    in range(2, 10, 3)
                ))
            )
        )
        for step
        in (
            l.replace('=', ' ').replace('..', ' ').replace(',', ' ').split()
            for l
            in f.readlines()
        )
    ]

cubes = []
for keep, cube in steps:
    new_cubes = []
    for other in cubes:
        new_cubes.extend(other.cut(cube))
    if keep:
        new_cubes.append(cube)
    cubes = new_cubes

print(sum(c.volume for c in cubes))
