from collections import Counter

from aoc.utils import get_lines

lines = get_lines(1)
l1, l2 = [], []
for line in lines:
    a, b = line.split()
    l1.append(int(a))
    l2.append(int(b))

l1 = sorted(l1)
l2 = sorted(l2)

diff = 0

for a, b in zip(l1, l2):
    diff += abs(a - b)

print(diff)

l2_count = Counter(l2)

sim = 0

for a in list(set(l1)):
    sim += a * l2_count.get(a, 0)

print(sim)
