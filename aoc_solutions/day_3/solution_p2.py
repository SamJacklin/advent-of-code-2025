"""Advent of Code - Day 3 Part 2"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 3


def part_2(data: str) -> int:
    total = 0
    DIGITS_REQUIRED = 12
    for line in data.splitlines():
        min_index = -1
        value = ''
        for i in range(DIGITS_REQUIRED - 1, -1, -1):
            line_window = line[min_index + 1:len(line)-i]
            max_val = max(line_window)
            min_index = line_window.index(max_val) + min_index + 1
            value += str(max_val)
        total += int(value)

    return total


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
