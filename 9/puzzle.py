with open("sample.txt") as f:
    lines = f.readlines()

line = list(map(int, (lines[0].strip())))

# ------------------------------
# Part 1
# ------------------------------
flatten = lambda l: [item for sl in l for item in sl]

files = line[::2]
space = line[1::2] + [0]

diskmap = flatten(
    [flatten([f[1] * [f[0]], s * [None]]) for f, s in (zip(enumerate(files), space))]
)

n = len(diskmap)

for _ in enumerate(diskmap):
    next_free = next(filter(lambda x: x[1] is None, enumerate(diskmap)))
    last_val = next(filter(lambda x: x[1] != None, enumerate(diskmap[::-1])))

    if next_free[0] + last_val[0] == n:
        break

    diskmap[next_free[0]] = last_val[1]
    diskmap[n - last_val[0] - 1] = None

sum([i * x for i, x in enumerate(diskmap) if x is not None])

# ------------------------------
# Part 2
# ------------------------------
from itertools import groupby

diskmap = flatten(
    [flatten([f[1] * [f[0]], s * [None]]) for f, s in (zip(enumerate(files), space))]
)

groups = [
    (k, [x[0] for x in list(group)])
    for k, group in groupby(enumerate(diskmap), lambda x: x[1])
]

fraak

for fragment, positions in fragments[::-1]:

