import numpy as np
from scipy import ndimage

iterations = 50

with open('input') as f:
    filter = [c == '#' for c in f.readline().strip()]
    f.readline()
    image = np.pad(np.genfromtxt(f.readlines(), dtype=str, delimiter=1, comments=None) == '#', iterations)

for _ in range(iterations):
    image = ndimage.generic_filter(image, lambda a: filter[int(''.join(['1' if b else '0' for b in a.flatten()]), 2)], size=3, mode='nearest')

print(np.count_nonzero(image))
