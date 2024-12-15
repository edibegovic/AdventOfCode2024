import numpy as np
from functools import lru_cache
from itertools import groupby

with open("input.txt") as f:
    lines = f.readlines()

grid = np.array([list(line.strip()) for line in lines])

# ------------------------------
# Part 1
# ------------------------------
flatten = lambda l: [item for sl in l for item in sl]
not_none = lambda x: x is not None


def within_bounds(grid, coords):
    return 0 <= coords[0] < grid.shape[0] and 0 <= coords[1] < grid.shape[1]


# Get a contiguous region from starting point
# @lru_cache(maxsize = 128)
def get_region(grid, coords, plant, visited):
    if not within_bounds(grid, coords):
        return [None]
    if grid[*coords] != plant:
        return [None]
    if tuple(coords) in visited:
        return [None]

    visited.add(tuple(coords))
    if len(coords) == 2:
        directions = np.array([(0, 1), (0, -1), (1, 0), (-1, 0)])
    else:
        directions = np.array([1, -1])
    return [tuple(coords)] + flatten(
        [get_region(grid, coords + dir, plant, visited) for dir in directions]
    )


def get_circumference(region):
    directions = np.array([(0, 1), (0, -1), (1, 0), (-1, 0)])
    return sum(
        [4 - len([1 for d in directions if tuple(p + d) in region]) for p in region]
    )


# Get all regions
regions = []
for i, j in np.ndindex(grid.shape):
    if (i, j) in flatten(regions):
        continue
    region = [
        x for x in get_region(grid, (i, j), grid[*(i, j)], set()) if x is not None
    ]
    regions.append(region)

sum([len(region) * get_circumference(region) for region in regions])

# ------------------------------
# Part 2
# ------------------------------


def region_grid(region):
    min_x, min_y = np.min(region, axis=0)
    max_x, max_y = np.max(region, axis=0)
    region_grid = np.full((max_x - min_x + 1, max_y - min_y + 1), 0)
    for x, y in region:
        region_grid[x - min_x, y - min_y] = 1
    return region_grid


def get_edges(region):
    grid = np.array(region_grid(region))
    pad = lambda g: np.pad(g, 1, mode="constant")[:, 1:-1]
    row_segments = lambda g: [
        len([key for key, _ in groupby(g[i - 1] + g[i] * -1) if key != 0])
        for i in range(1, len(g))
    ]

    return sum(row_segments(pad(grid)) + row_segments(pad(grid.T)))


sum([len(region) * get_edges(region) for region in regions])
