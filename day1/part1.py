from icecream import ic

# lines = open("test1.txt").read().splitlines()
lines = open("input.txt").read().splitlines()

numbers = []
for line in lines:
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)

    number = int(digits[0] + digits[-1])
    numbers.append(number)

ic(sum(numbers))