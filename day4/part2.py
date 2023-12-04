from icecream import ic
from dataclasses import dataclass

# lines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()


@dataclass
class Card:
    id: int
    value: int


cards = []
for line in lines:
    card_id = int(line.split(":")[0].split(" ")[-1])
    winning = line.split(":")[1].split(" | ")[0].strip().split(" ")
    winning = set([int(w) for w in winning if w.strip()])
    numbers = line.split(":")[1].split(" | ")[1].strip().split(" ")
    numbers = set(([int(n) for n in numbers if n.strip()]))

    my_wins = winning & numbers
    cards.append(Card(id=card_id, value=len(my_wins)))


idx = 0
while idx < len(cards):
    card = cards[idx]
    idx += 1

    if card:
        cards += cards[card.id : card.id + card.value]

ic(idx)
