import pytest
from icecream import ic
from dataclasses import dataclass

# lines = open("test.txt").read().splitlines()
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

next_node = "AAA"
idx = 0
c = 0
while True:
    ic(next_node)
    if next_node == "ZZZ":
        break

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
