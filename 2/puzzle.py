# ------------------------------
# Part 1
# ------------------------------

with open("input.txt") as f:
    lines = f.readlines()

levels = [line.strip().split() for line in lines]

level_diffs = [[int(a) - int(b) for a, b in zip(level[1::], level)] for level in levels]

same_sign = lambda l: (all(x < 0 for x in l) or all(x > 0 for x in l))
within_range = lambda l: all(1 <= abs(x) <= 3 for x in l)
safe = lambda l: 1 if (same_sign(l) and within_range(l)) else 0

# Result
sum([safe(level) for level in level_diffs])

# ------------------------------
# Part 2
# ------------------------------

# eh fuck it
safe_count = 0
for level in levels:
    for idx in range(-1, len(level)):
        level_mod = [x for i, x in enumerate(level) if i != idx]
        level_diff = [int(a) - int(b) for a, b in zip(level_mod[1::], level_mod)]
        if safe(level_diff):
            safe_count += 1
            break
