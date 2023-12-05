# 29401440 - too high
from icecream import ic
from dataclasses import dataclass

# lines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()

STEP = 100


@dataclass
class Map:
    destination: int
    source: int
    length: int

    def get_source_range(self):
        return range(self.source, self.source + self.length)

    def get_source_boundries(self):
        return self.source, self.source + self.length

    def convert_seed(self, seed_to_convert):
        range_b, range_t = self.get_source_boundries()
        if range_b <= seed_to_convert < range_t:
            return seed_to_convert - self.source + self.destination, True

        return seed_to_convert, False


@dataclass
class MapList:
    name: str
    maps: list[Map]

    def get_new_seed(self, seed_to_convert: int):
        converted_seed = seed_to_convert
        for m in self.maps:
            converted_seed, changed = m.convert_seed(seed_to_convert)
            if changed:
                return converted_seed

        return converted_seed


@dataclass
class SeedRange:
    start: int
    length: int

    def get_seeds(self, full=False, prev_min=0):
        if full:
            return range(
                prev_min - 2 * round(self.length / 1000),
                prev_min + 2 * round(self.length / 1000),
            )

        return range(self.start, self.start + self.length, round(self.length / 10))


seeds: list[SeedRange] = []
conversions = []
current_name = ""
current_maplist: MapList | None = None
for idx, line in enumerate(lines):
    if idx == 0:
        raw_s = line.split(": ")[1].split(" ")
        raw_s = [int(s) for s in raw_s if s.strip()]

        t = []
        while raw_s:
            if len(t) < 2:
                t.append(raw_s.pop(0))
            else:
                seeds.append(SeedRange(start=t[0], length=t[1]))
                t = []
        seeds.append(SeedRange(start=t[0], length=t[1]))
        continue

    if "map" in line:
        name = line.split(" ")[0]
        if current_name != name:
            if current_name:
                conversions.append(current_maplist)

            current_name = name
            current_maplist = MapList(name=name, maps=[])

    elif line:
        dst, src, l = [int(e) for e in line.split(" ")]
        current_maplist.maps.append(Map(destination=dst, source=src, length=l))

    if idx == len(lines) - 1:
        conversions.append(current_maplist)

min_location = float("inf")
min_seed_range = None
min_source_seed = None
for seed_range in seeds[:]:
    for source_seed in seed_range.get_seeds():
        seed = source_seed
        for conv in conversions:
            seed = conv.get_new_seed(seed)
        if seed < min_location:
            ic("replacing", min_location, seed)
            min_location = seed
            min_seed_range = seed_range
            min_source_seed = source_seed

ic(min_location, min_seed_range, min_source_seed)
c = 0
for source_seed in min_seed_range.get_seeds(full=True, prev_min=min_source_seed):
    if source_seed == min_source_seed:
        ic("mid-point")

    seed = source_seed
    for conv in conversions:
        seed = conv.get_new_seed(seed)
    if seed < min_location:
        ic("replacing", min_location, seed)
        min_location = seed
        min_source_seed = source_seed

    c += 1
    if c % 100000 == 0:
        ic(c, round(c / min_seed_range.length * 100, 2))


ic(min_location, min_source_seed)
# 26778403
