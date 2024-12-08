import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

grid = np.array([list(line.strip()) for line in lines])

# ------------------------------
# Part 1
# ------------------------------
flatten = lambda l: [item for sl in l for item in sl]


def within_bounds(pos):
    x, y = pos
    return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]


frequenices = set(flatten(grid)) - set(".")
antinodes = set()

for f in frequenices:
    antennas = np.argwhere(grid == f)
    an = [[a0 + (a0 - a1) for a1 in antennas if not np.array_equal(a1, a0)] for a0 in antennas]
    antinodes.update(map(tuple, filter(within_bounds, flatten(an))))

len(antinodes)

# ------------------------------
# Part 2
# ------------------------------

antinodes = set()
stupid_big_number = 50

for f in frequenices:
    antennas = np.argwhere(grid == f)
    an = [flatten([
            [a0 + i*(a0 - a1) for i in range(stupid_big_number)]
            for a1 in antennas if not np.array_equal(a1, a0)
        ])
        for a0 in antennas]
    antinodes.update(map(tuple, filter(within_bounds, flatten(an))))

len(antinodes)
