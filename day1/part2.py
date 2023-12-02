# 54607 - too high
from icecream import ic
import re

# lines = open("test2.txt").read().splitlines()
lines = open("input.txt").read().splitlines()


def find_all(pattern, text):
    return [m.start() for m in re.finditer(pattern, text)]


mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

numbers = []
for line in lines:
    matches = {}
    for word in mapping.keys():
        positions = find_all(word, line)
        for pos in positions:
            matches[pos] = mapping[word]

    for pos, char in enumerate(line):
        if char.isdigit():
            matches[pos] = char

    keys = sorted(matches.keys())
    numbers.append(int(matches[keys[0]] + matches[keys[-1]]))

ic(sum(numbers))
