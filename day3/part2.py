# 526341 - too low
from icecream import ic
from dataclasses import dataclass

# lines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()


@dataclass
class Symbol:
    x: int
    y: int
    value: str


@dataclass
class Part:
    xrange: list[int]
    symbol: Symbol | None
    value: int
    y: int

    def _y_offsets(self):
        return [self.y - 1, self.y, self.y + 1]

    def _x_offsets(self):
        return [self.xrange[0] - 1, self.xrange[-1] + 1, *self.xrange]

    def check_match(self, symbol: Symbol):
        if self.symbol:
            return self

        if symbol.y not in self._y_offsets():
            return self

        if symbol.x in self._x_offsets():
            self.symbol = symbol

        return self


symbols = []
parts = []
for y, line in enumerate(lines):
    xrange = []
    value = ""
    for x, char in enumerate(line):
        if char.isdigit():
            xrange.append(x)
            value += char

            if x == len(line) - 1:
                part = Part(xrange=xrange, value=int(value), y=y, symbol=None)
                parts.append(part)
        else:
            if value:
                part = Part(xrange=xrange, value=int(value), y=y, symbol=None)
                parts.append(part)
                xrange = []
                value = ""
            if char != ".":
                symbol = Symbol(x=x, y=y, value=char)
                symbols.append(symbol)


gear_ratios = []
for symbol in symbols:
    # ic(symbol)
    matching_parts = []
    for part in parts:
        part = part.check_match(symbol)

        if part.symbol and part.symbol == symbol and part.symbol.value == "*":
            matching_parts.append(part)

    if len(matching_parts) == 2:
        gear_ratios.append(matching_parts[0].value * matching_parts[1].value)

ic(gear_ratios)
ic(sum(gear_ratios))
