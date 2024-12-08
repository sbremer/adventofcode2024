import numpy as np

from aoc.utils import get_lines


def is_safe(levels: np.array) -> bool:
    diff = levels[:-1] - levels[1:]
    all_same_sign = np.unique(np.sign(diff)).shape[0] == 1
    all_in_delta = np.all((1 <= np.abs(diff)) & (np.abs(diff) <= 3))
    return all_same_sign and all_in_delta


lines = get_lines(2)

reports = []

for line in lines:
    levels = list(map(int, line.split()))
    reports.append(np.array(levels))

n_safe = 0

for levels in reports:
    if is_safe(levels):
        n_safe += 1

print(n_safe)

n_safe_2 = 0

for levels in reports:
    if is_safe(levels):
        n_safe_2 += 1
    else:
        for i in range(len(levels)):
            levels_ = np.concatenate([levels[:i], levels[i + 1 :]])
            if is_safe(levels_):
                n_safe_2 += 1
                break

print(n_safe_2)
