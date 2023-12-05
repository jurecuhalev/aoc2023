# 1852510996 - too high
from icecream import ic
from dataclasses import dataclass

# lines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()


@dataclass
class Map:
    destination: int
    source: int
    length: int

    def get_source_range(self):
        return range(self.source, self.source + self.length)

    def get_destination_range(self):
        return range(self.destination, self.destination + self.length)

    def convert_seed(self, seed_to_convert):
        # ic(
        #     seed_to_convert,
        #     self.get_source_range(),
        #     seed_to_convert - self.source + self.destination,
        #     seed_to_convert in self.get_source_range(),
        #     self.destination,
        #     self.source,
        #     self.length,
        # )
        if seed_to_convert in self.get_source_range():
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


seeds = []
conversions = []
current_name = ""
current_maplist: MapList | None = None
for idx, line in enumerate(lines):
    if idx == 0:
        seeds = line.split(": ")[1].split(" ")
        seeds = [int(s) for s in seeds if s.strip()]
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

locations = []
for source_seed in seeds[:1]:
    seed = source_seed
    for conv in conversions:
        ic(seed, conv.name)
        seed = conv.get_new_seed(seed)
    locations.append(seed)
    # print("-----")
ic(min(locations))
