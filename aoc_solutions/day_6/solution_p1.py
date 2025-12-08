"""Advent of Code - Day 6 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 6


def part_1(data: str) -> int:
    lines = data.splitlines()
    col_signs = lines.pop(-1).split()
    columns = []
    for line in lines:
        values = line.split()
        for i, val in enumerate(values):
            if i >= len(columns):
                columns.append([])
            columns[i].append(val)
    for i, col in enumerate(columns):
        if col_signs[i] == '+':
            columns[i] = sum(map(int, col))
        elif col_signs[i] == '*':
            prod = 1
            for val in map(int, col):
                prod *= val
            columns[i] = prod
    total = sum(columns)
            
    return total


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
