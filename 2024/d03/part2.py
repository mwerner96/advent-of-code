import re

with open("input") as f:
    input = f.read()

pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
instructions = re.findall(pattern, input)

sum = 0
enabled = True
for instruction in instructions:
    if instruction.startswith("mul"):
        if enabled:
            a, b = instruction[4:-1].split(",")
            sum += int(a) * int(b)
    elif instruction.startswith("don't"):
        enabled = False
    else:
        enabled = True

print(sum)
