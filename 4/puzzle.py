with open("input.txt") as f:
    lines = f.readlines()

# lines = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX""".split(
#     "\n"
# )

# ------------------------------
# Part 1
# ------------------------------
import numpy as np
from functools import reduce
import re

grid = np.array([list(line.strip()) for line in lines])
size = grid.shape[0]


sets = [
    grid,  # rows
    grid.T,  # columns
    [np.diag(grid, k=i) for i in range(-size + 1, size)],  # diag: /
    [np.diag(np.rot90(grid), k=i) for i in range(-size + 1, size)],  # diag: \
]

lr_slices = [slice for s in sets for slice in s]
rl_slices = [slice[::-1] for slice in lr_slices]
slices = ["".join(l) for l in lr_slices + rl_slices]

count = reduce(lambda acc, slice: acc + len(re.findall("XMAS", slice)), slices, 0)
count

# ------------------------------
# Part 2
# ------------------------------
grid = np.array([list(line.strip()) for line in lines])

p_grid = np.pad(grid, 1, "constant", constant_values=".")
size = p_grid.shape[0]


def is_mas(grid, pos):
    i, j = pos
    diags = [
        [grid[i - 1, j - 1], grid[i + 1, j + 1]] in [["M", "S"], ["S", "M"]],
        [grid[i - 1, j + 1], grid[i + 1, j - 1]] in [["M", "S"], ["S", "M"]],
    ]
    return sum(diags) == 2


count = 0
for i in range(size):
    for j in range(size):
        if p_grid[i, j] == "A" and is_mas(p_grid, (i, j)):
            count += 1

count
