import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

equations = [line.strip().split(":") for line in lines]

numbers = [[int(x) for x in eq[1].strip().split()] for eq in equations]
values = [int(eq[0]) for eq in equations]

# ------------------------------
# mint solution
# ------------------------------
from operator import add, mul

naive_add = lambda x, y: int(str(x) + str(y))
flatten = lambda l: [item for sl in l for item in sl]

def potential_solutions(values, operations):
    if len(values) == 2:
        return [op(values[0], values[1]) for op in operations]

    return flatten(
        [
            [op(v, values[-1]) for op in operations]
            for v in potential_solutions(values[:-1], operations)
        ]
    )


# ------------------------------
# Part 1
# ------------------------------
sum([v for v, nums in zip(values, numbers) if v in potential_solutions(nums, [add, mul])])

# ------------------------------
# Part 2
# ------------------------------
sum([v for v, nums in zip(values, numbers) if v in potential_solutions(nums, [add, mul, naive_add])])
