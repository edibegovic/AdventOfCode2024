from collections import defaultdict
from itertools import groupby
from functools import cmp_to_key
from math import ceil

with open("input.txt") as f:
    lines = f.readlines()

split_idx = lines.index("\n")

rules = [x.strip().split("|") for x in lines[:split_idx]]
updates = [x.strip().split(",") for x in lines[split_idx + 1 :]]


# ------------------------------
# Part 1
# ------------------------------
def is_valid(update):
    return not any(
        [any([[pn, x] in rules for x in update[:i]]) for i, pn in enumerate(update)]
    )


valid_updates = filter(is_valid, updates)

# Resulst
sum([int(update[len(update) // 2]) for update in valid_updates])

# ------------------------------
# Part 2
# ------------------------------
invalid_updates = filter(lambda x: not is_valid(x), updates)


def cmp(x, y):
    if [x, y] in rules:
        return -1
    if [y, x] in rules:
        return 1
    return 0


fixed_updates = [sorted(update, key=cmp_to_key(cmp)) for update in invalid_updates]

# Result
sum([int(update[len(update) // 2]) for update in fixed_updates])
