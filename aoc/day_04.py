import re

import numpy as np

from aoc.utils import get_lines

lines = get_lines(4)

to_find = "XMAS"

data = np.array([list(line) for line in lines])

data_all = []

for i in range(data.shape[0]):
    data_all.append(data[i, :])

for i in range(data.shape[1]):
    data_all.append(data[:, i])

shape_max = max(*data.shape)
for i in range(len(to_find) - shape_max, shape_max - len(to_find)):
    data_all.append(np.diagonal(data, offset=i))

data_t = np.fliplr(data)

for i in range(len(to_find) - shape_max, shape_max - len(to_find)):
    data_all.append(np.diagonal(data_t, offset=i))

data_all = ["".join(line) for line in data_all]

pattern = re.compile(to_find)
pattern_r = re.compile(to_find[::-1])

n_xmas = 0

for line in data_all:
    n_xmas += len(pattern.findall(line))
    n_xmas += len(pattern_r.findall(line))

print(n_xmas)

n_mas_x = 0
to_find_2 = ("MAS", "SAM")

for x in range(1, data.shape[0] - 1):
    for y in range(1, data.shape[1] - 1):
        data_small = data[x - 1 : x + 2, y - 1 : y + 2]
        diag_1 = "".join(np.diagonal(data_small))
        diag_2 = "".join(np.diagonal(np.fliplr(data_small)))
        if diag_1 in to_find_2 and diag_2 in to_find_2:
            n_mas_x += 1

print(n_mas_x)
