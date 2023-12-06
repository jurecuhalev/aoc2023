from icecream import ic
from dataclasses import dataclass
import math

# lines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()


@dataclass
class Race:
    time: int
    distance: int

    def count_wins(self):
        count = 0
        for time in range(1, self.time):
            count += int((self.time - time) * time > self.distance)

        return count


times = []
distances = []
for idx, line in enumerate(lines):
    if idx == 0:
        for t in line.split(" "):
            try:
                times.append(int(t))
            except ValueError:
                continue

    elif idx == 1:
        for d in line.split(" "):
            try:
                distances.append(int(d))
            except ValueError:
                continue

races: list[Race] = []
for idx in range(0, len(times)):
    races.append(Race(time=times[idx], distance=distances[idx]))

wins = []
for race in races:
    wins.append(race.count_wins())

ic(math.prod(wins))
