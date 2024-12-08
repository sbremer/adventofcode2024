import re

from aoc.utils import get_lines

lines = get_lines(3)
line = "".join(lines)

mul_pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

mul_operations = mul_pattern.findall(line)
mul_sum = sum([int(a) * int(b) for a, b in mul_operations])
print(mul_sum)

mul_sum_2 = 0
start = 0
while True:
    end = line[start:].find("don't()")
    if end == -1:
        line_part = line[start:]
    else:
        line_part = line[start : start + end + len("don't()")]
    mul_operations = mul_pattern.findall(line_part)
    mul_sum_2 += sum([int(a) * int(b) for a, b in mul_operations])

    start += end + len("don't()")
    delta_new_do = line[start:].find("do()")
    if delta_new_do == -1:
        break
    else:
        start += delta_new_do


print(mul_sum_2)
