# 22614725536743378114584561 - too high
import math

import pytest
from icecream import ic
from dataclasses import dataclass

# lines = open("test2.txt").read().splitlines()
lines = open("input.txt").read().splitlines()


@dataclass
class Node:
    left: str
    right: str


steps = []
nodes = {}

for idx, line in enumerate(lines):
    if idx == 0:
        steps = line

    if idx >= 2:
        key = line.split(" = ")[0]
        raw_l, raw_r = line.split(" = ")[1][1:-1].split(", ")
        nodes[key] = Node(raw_l, raw_r)


def count_steps(starting_node: str):
    next_node = starting_node
    idx = 0
    c = 0
    while True:
        # ic(next_node)
        if next_node.endswith("Z"):
            ic(next_node)
            return c

        node = nodes[next_node]
        next_step = steps[idx]
        if next_step == "L":
            next_node = node.left
        else:
            next_node = node.right

        c += 1
        idx += 1
        if idx >= len(steps):
            idx = 0


starting_nodes = [n for n in nodes.keys() if n.endswith("A")]
all_steps = []
for nn in starting_nodes:
    count = count_steps(nn)
    ic(nn, count)
    all_steps.append(count)

# ic(math.prod(all_steps))
ic(math.lcm(*all_steps))
