"""Advent of Code - Day 9 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 9


def part_1(data: str) -> int:
    coords = []
    for line in data.splitlines():
        x, y = map(int, line.split(','))
        coords.append((x, y))
    max_area = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if x1 == x2 and y1 == y2:
                continue
            # Calculate the area
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_area = max(max_area, area)
    return max_area

if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
