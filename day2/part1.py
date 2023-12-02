from icecream import ic
from dataclasses import dataclass

# lines = open("test1.txt").read().splitlines()
lines = open("input.txt").read().splitlines()


@dataclass
class Round:
    red: int
    green: int
    blue: int

    def is_possible(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14


possible_games = []
for line in lines:
    game, raw_plays = line.split(":")
    game_id = int(game.split(" ")[-1])

    results = []
    for raw_play in raw_plays.split(";"):
        play = Round(red=0, green=0, blue=0)
        for raw_count_color in raw_play.split(","):
            count, color = raw_count_color.strip().split(" ")
            match color.strip():
                case "red":
                    play.red = int(count)
                case "green":
                    play.green = int(count)
                case "blue":
                    play.blue = int(count)
                case _:
                    raise Exception

        results.append(play.is_possible())
    if all(results):
        possible_games.append(game_id)

ic(sum(possible_games))
