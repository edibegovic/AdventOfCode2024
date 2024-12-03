with open("input.txt") as f:
    lines = f.readlines()
    input = "".join(lines)

# ------------------------------
# Part 1
# ------------------------------
import re

regex = "mul\((\d{1,3}),(\d{1,3})\)"
pairs = re.findall(regex, input)

sum([int(x) * int(y) for x, y in pairs])

# ------------------------------
# Part 2
# ------------------------------
regex = "mul\((\d{1,3}),(\d{1,3})\)|(don't\(\)|do\(\))"
matches = re.findall(regex, input)

sum = 0
state = 1

for a, b, s in matches:
    if s == "do()":
        state = 1
    elif s == "don't()":
        state = 0
    else:
        sum += int(a) * int(b) * state
