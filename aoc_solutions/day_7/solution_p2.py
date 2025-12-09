"""Advent of Code - Day 7 Part 2"""

from aoc_solutions.utils import get_input, submit_answer

from collections import defaultdict
from pydantic import BaseModel

DAY = 7

def part_2(data: str) -> int:
    lines = data.splitlines()
    positions_to_check = []
    for i, char in enumerate(lines[0]):
        if char == 'S':
            positions_to_check.append((i, 1)) # position, parent_count

    for i, line in enumerate(lines):
        if i == 0:
            continue
        positions_to_add = defaultdict(int)
        for j in range(len(positions_to_check), 0, -1):
            pos, parent_count = positions_to_check[j - 1]
            if line[pos] == '^':
                positions_to_add[pos - 1] += parent_count
                positions_to_add[pos + 1] += parent_count
                positions_to_check.remove((pos, parent_count))
        for pos, parent_count in positions_to_add.items():
            positions_to_check.append((pos, parent_count))
    total = 0
    for pos, parent_count in positions_to_check:
        total += parent_count
    return total


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
