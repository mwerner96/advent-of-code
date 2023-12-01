lut = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

with open("input") as f:
    lines = f.read().splitlines()

numbers = []
for line in lines:
    nums = []
    for idx in range(len(line)):
        for key, value in lut.items():
            if line[idx:].startswith(key):
                nums.append(value)
    numbers.append(nums)

print(sum(10 * n[0] + n[-1] for n in numbers))
