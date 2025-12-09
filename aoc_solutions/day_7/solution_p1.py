"""Advent of Code - Day 7 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 7


def part_1(data: str) -> int:
    lines = data.splitlines()
    positions_to_check = set()
    for i, char in enumerate(lines[0]):
        if char == 'S':
            positions_to_check.add(i)

    split_count = 0
    
    for i, line in enumerate(lines):
        positions_to_add = set()
        for j in range(len(positions_to_check), 0, -1):
            pos = sorted(positions_to_check)[j - 1]
            if line[pos] == '^':
                positions_to_add.add(pos - 1)
                positions_to_add.add(pos + 1)
                positions_to_check.remove(pos)
                split_count += 1
        positions_to_check.update(positions_to_add)
    return split_count


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
