from icecream import ic
from dataclasses import dataclass

# lines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()

points = 0
for line in lines:
    card_id = line.split(":")[0].split(" ")[1]
    winning = line.split(":")[1].split(" | ")[0].strip().split(" ")
    winning = set([int(w) for w in winning if w.strip()])
    numbers = line.split(":")[1].split(" | ")[1].strip().split(" ")
    numbers = set(([int(n) for n in numbers if n.strip()]))

    my_wins = winning & numbers
    if my_wins:
        ic(my_wins, 2 ** (len(my_wins) - 1))
        points += 2 ** (len(my_wins) - 1)

ic(points)
