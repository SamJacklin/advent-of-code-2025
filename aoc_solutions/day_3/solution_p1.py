"""Advent of Code - Day 3 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 3


def part_1(data: str) -> int:
    total = 0
    for line in data.splitlines():
        line_bar_one = line[:len(line)-1]
        max_val = max(line_bar_one)
        max_num_index = line.index(max_val)
        line_from_max = line[max_num_index + 1:]
        max_val_2 = max(line_from_max)
        num = int(max_val + max_val_2)
        total += num

    return total


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
