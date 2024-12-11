#Todays challenge was ultimately too difficult for me so the solution is copied from
#hamatti.org/adventofcode/2024/solutions/day-11
from functools import cache
import sys

sys.set_int_max_str_digits(10000)

line = "2 77706 5847 9258441 0 741 883933 12".split(" ")
intlist = []
for i in line:
  intlist.append(int(i))




def map_fn(line):
    return [int(n) for n in line.split()]


@cache
def blink(stone, iteration=0, max_iteration=25):
    if iteration == max_iteration:
        return 1

    if stone == 0:
        return blink(1, iteration + 1, max_iteration)

    stone_str = str(stone)
    digits = len(stone_str)
    if digits % 2 == 0:
        mid = digits // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])

        return blink(left, iteration + 1, max_iteration) + blink(
            right, iteration + 1, max_iteration
        )

    return blink(stone * 2024, iteration + 1, max_iteration)


def part_1():
    stones = intlist
    stone_count = 0
    for stone in stones:
        stone_count += blink(stone)

    print(f"Part 1: {stone_count}")


def part_2():
    stones = intlist
    stone_count = 0
    for stone in stones:
        stone_count += blink(stone, max_iteration=75)

    print(f"Part 2: {stone_count}")


part_1()
part_2()