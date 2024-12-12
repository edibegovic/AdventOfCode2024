import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

stones = list(map(int, lines[0].split()))

# ------------------------------
# Part 1
# ------------------------------
flatten = lambda l: [item for sl in l for item in sl]


def blink(stone):
    if stone == 0:
        return [1]
    if len(stone_str := str(stone)) % 2 == 0:
        return list(
            map(
                int,
                [stone_str[: len(stone_str) // 2], stone_str[len(stone_str) // 2 :]],
            )
        )
    else:
        return [2024 * stone]


for _ in range(25):
    stones = flatten(map(blink, stones))

len(stones)

# ------------------------------
# Part 2
# ------------------------------
from functools import lru_cache


@lru_cache(maxsize=None)
def blink_rec(stone, depth):
    if depth == 1:
        return len(blink(stone))
    else:
        return sum([blink_rec(s, depth - 1) for s in blink(stone)])


sum([blink_rec(s, 75) for s in stones])
