import pytest
from icecream import ic
from dataclasses import dataclass

# lines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()

strengths = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
strengths.reverse()


@dataclass
class CardHand:
    cards: str
    bid: int

    @property
    def type(self):
        cards = self.cards
        if "J" in cards:
            if cards == "JJJJJ":
                cards = "AAAAA"
            else:
                letters = {}
                for char in set(cards) - set("J"):
                    letters[char] = cards.count(char)

                top_letter = sorted(letters.items(), key=lambda i: i[1], reverse=True)
                cards = cards.replace("J", top_letter.pop(0)[0])

        card_set = set(cards)
        # Five of a kind
        if len(card_set) == 1:
            return 7

        # Four of a kind or Full house
        if len(card_set) == 2:
            # Four of a kind - AA8AA
            if cards.count(cards[0]) in [1, 4]:
                return 6

            # Full house - 23332
            return 5

        # Three of a kind or Two pair
        if len(card_set) == 3:
            letters = {}
            for char in card_set:
                letters[char] = cards.count(char)

            # Three of a kind - TTT98
            if sorted(letters.values(), reverse=True) == [3, 1, 1]:
                return 4

            # Two pair - 23432, KTJJT
            return 3

        # One pair - A23A4
        if len(card_set) == 4:
            return 2

        # High card - 23456
        if len(card_set) == 5:
            return 1

    def __eq__(self, other):
        if isinstance(other, CardHand) and self.cards == other.cards:
            return True

    def __lt__(self, other):
        if self.type == other.type:
            for first, second in zip(self.cards, other.cards):
                if first == second:
                    continue

                return strengths.index(first) < strengths.index(second)

        return self.type < other.type


# 32T3K, KTJJT, KK677, T55J5, QQQJA

if __name__ == "__main__":
    games = []
    for line in lines:
        games.append(CardHand(cards=line.split(" ")[0], bid=int(line.split(" ")[1])))

    bids = []
    for idx, hand in enumerate(sorted(games), start=1):
        bids.append(idx * hand.bid)
    # ic(bids)
    ic(sum(bids))


@pytest.mark.parametrize(
    "hand,expected_type",
    (
        ["AAAA", 7],
        ["AA8AA", 6],
        ["23332", 5],
        ["TTT98", 4],
        ["23432", 3],
        ["A23A4", 2],
        ["23456", 1],
        ["32T3K", 2],
        ["KK677", 3],
        ["KTJJT", 3],
    ),
)
def test_hand_type(hand, expected_type):
    hand = CardHand(hand, 5)
    assert hand.type == expected_type


@pytest.mark.parametrize(
    "a, b, result",
    (
        ["33332", "2AAAA", True],
        ["77888", "77788", True],
        ["77788", "77888", False],
        ["KK677", "KTJJT", False],
        ["KTJJT", "KK677", True],
    ),
)
def test_compare_cards(a, b, result):
    card_a = CardHand(a, 1)
    card_b = CardHand(b, 1)

    assert result == (card_a > card_b)


def test_joker():
    card = CardHand("QJJQ2", 1)

    assert card.type == 6
