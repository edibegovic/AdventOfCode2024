# ------------------------------
# Part 1
# ------------------------------

with open("input.txt") as f:
    lines = f.readlines()

pairs = [line.strip().split() for line in lines]

left = sorted([int(pair[0]) for pair in pairs])
right = sorted([int(pair[1]) for pair in pairs])

sorted_pairs = list(zip(left, right))

sum([abs(pair[0] - pair[1]) for pair in sorted_pairs])


# ------------------------------
# Part 2
# ------------------------------
from collections import Counter, defaultdict

right_count = defaultdict(int, Counter(right))

sum([right_count[id] * id for id in left])
