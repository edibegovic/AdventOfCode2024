import numpy as np
from numpy.linalg import solve
import re

with open("input.txt") as f:
    lines = f.readlines()

machines = [(a, b, p) for a, b, p in zip(lines[0::4], lines[1::4], lines[2::4])]


def parse_machine(machine) -> tuple:
    numbers = re.findall(r"\d+", "".join(machine))
    M = np.array(list(map(int, numbers))).reshape(-1, 2)
    return M[:-1].T, M[-1]


# ------------------------------
# Part 1
# ------------------------------

solutions = [solve(*parse_machine(m)) for m in machines]

sum(
    [
        3 * a + b
        for a, b in solutions
        if np.isclose(a, round(a)) and np.isclose(b, round(b))
    ]
)

# ------------------------------
# Part 2
# ------------------------------
solutions = [
    solve(A, b + 10000000000000) for A, b in [parse_machine(m) for m in machines]
]
eps = 0.01

sum(
    [
        3 * round(a) + round(b)
        for a, b in solutions
        if abs(a - round(a)) < eps and abs(b - round(b)) < eps
    ]
)
