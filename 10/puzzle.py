import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

grid = np.array([list(map(int, line.strip())) for line in lines])

# ------------------------------
# Part 1
# ------------------------------
flatten = lambda l: [item for sl in l for item in sl]

trailheads = np.argwhere(grid == 0)


def within_bounds(x, y):
    return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]


def get_tops(grid, pos):
    if grid[*pos] == 9:
        return [pos]

    neighbors = [
        [pos[0] + 1, pos[1]],
        [pos[0] - 1, pos[1]],
        [pos[0], pos[1] + 1],
        [pos[0], pos[1] - 1],
    ]

    valid_neighbors = [
        get_tops(grid, n_coor)
        for n_coor in neighbors
        if within_bounds(*n_coor) and grid[*n_coor] == grid[*pos] + 1
    ]
    return flatten(valid_neighbors)


# Result
sum([len(np.unique(get_tops(grid, pos), axis=0)) for pos in trailheads])

# ------------------------------
# Part 2
# ------------------------------


def get_tops(grid, pos):
    if grid[*pos] == 9:
        return 1

    neighbors = [
        [pos[0] + 1, pos[1]],
        [pos[0] - 1, pos[1]],
        [pos[0], pos[1] + 1],
        [pos[0], pos[1] - 1],
    ]

    valid_neighbors = [
        get_tops(grid, n_coor)
        for n_coor in neighbors
        if within_bounds(*n_coor) and grid[*n_coor] == grid[*pos] + 1
    ]
    return sum(valid_neighbors)


# Result
sum([get_tops(grid, pos) for pos in trailheads])
