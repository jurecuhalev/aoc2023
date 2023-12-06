from icecream import ic
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    distance: int

    def count_wins(self):
        count = 0
        for time in range(1, self.time):
            count += int((self.time - time) * time > self.distance)

        return count


# race = Race(time=71530, distance=940200)
race = Race(time=38947970, distance=241154910741091)

ic(race.count_wins())
