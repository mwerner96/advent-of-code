import re

with open("input") as f:
    input = f.read()

pattern = r"mul\([0-9]+,[0-9]+\)"
muls = [tuple(mul[4:-1].split(",")) for mul in re.findall(pattern, input)]

print(sum(int(a) * int(b) for a, b in muls))
