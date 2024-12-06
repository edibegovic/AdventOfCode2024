import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

grid = np.array([list(line.strip()) for line in lines])


# ------------------------------
# Part 1
# ------------------------------
def within_bounds(x, y):
    return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]


directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

visited = set()
turns = 0
pos = np.argwhere(grid == "^")[0]


while True:
    visited.add(tuple(pos))
    next = [*pos] + directions[turns % 4]
    if not within_bounds(*next):
        break
    if grid[*next] == "#":
        turns += 1
        continue
    pos += directions[turns % 4]

len(visited)

# ------------------------------
# Part 2
# ------------------------------
# it's the weekend copy paste bruteforce letssgooooooo

solutions = 0


def within_bounds(x, y):
    return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]


directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == "^":
            continue
        mod_grid = grid.copy()
        mod_grid[i, j] = "#"

        steps = 0
        turns = 0
        starting_pos = np.argwhere(grid == "^")[0]
        pos = starting_pos

        while True:
            steps += 1
            if steps > len(grid) * len(grid[0]):
                solutions += 1
                break
            next = [*pos] + directions[turns % 4]
            if not within_bounds(*next):
                break
            if mod_grid[*next] == "#":
                turns += 1
                continue
            pos += directions[turns % 4]

        print(i, j, solutions)
