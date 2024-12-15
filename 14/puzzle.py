import numpy as np
import re
from functools import reduce
from operator import mul
from scipy.stats import entropy

with open("input.txt") as f:
    lines = f.readlines()

robots = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]
w, h = 101, 103

# ------------------------------
# Part 1
# ------------------------------


def move(grid: tuple, robot: list, times=1):
    x, y, vx, vy = robot
    w, h = grid
    return ((x + vx * times) % w, (y + vy * times) % h)


moved_robots = [move((w, h), robot, 100) for robot in robots]

reduce(
    mul,
    [
        len([1 for x, y in moved_robots if x < w // 2 and y < h // 2]),
        len([1 for x, y in moved_robots if x > w // 2 and y < h // 2]),
        len([1 for x, y in moved_robots if x < w // 2 and y > h // 2]),
        len([1 for x, y in moved_robots if x > w // 2 and y > h // 2]),
    ],
)


# ------------------------------
# Part 2
# ------------------------------
res = []
for i in range(10000):
    moved_robots = [move((w, h), robot, i) for robot in robots]
    quadrants = [
        len([1 for x, y in moved_robots if x < w // 2 and y < h // 2]),
        len([1 for x, y in moved_robots if x > w // 2 and y < h // 2]),
        len([1 for x, y in moved_robots if x < w // 2 and y > h // 2]),
        len([1 for x, y in moved_robots if x > w // 2 and y > h // 2]),
    ]
    res.append((np.var(quadrants), i))


sorted(res, key=lambda x: x[0], reverse=True)[:10]  # 8050
