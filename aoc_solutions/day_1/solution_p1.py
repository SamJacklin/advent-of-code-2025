"""Advent of Code - Day 1 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 1
DIAL_STARTING_POSITION = 50

def calculate_single_rotation(position: int, direction: str, distance: int) -> int:
    if direction == "L":
        position = (position - distance) % 100
    elif direction == "R":
        position = (position + distance) % 100
    else:
        raise ValueError("Invalid direction")
    return position

def part_1(data: str) -> int:
    dial_position = DIAL_STARTING_POSITION
    zero_counts = 0
    for line in data.splitlines():
        direction = line[0]
        distance = int(line[1:].strip())
        dial_position = calculate_single_rotation(dial_position, direction, distance)
        if dial_position == 0:
            zero_counts += 1
    return zero_counts

if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
