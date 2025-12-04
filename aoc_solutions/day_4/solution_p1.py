"""Advent of Code - Day 4 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 4

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
LIMIT = 3

def check_char(row: int, col: int, lines: list[str]) -> bool:
    count = 0

    for d_row, d_col in DIRECTIONS:
        n_row, n_col = row + d_row, col + d_col
        # Check bounds
        if 0 <= n_row < len(lines) and 0 <= n_col < len(lines[n_row]):
            if lines[n_row][n_col] == '@':
                count += 1
    if count > LIMIT:
        return False
    return True

def part_1(data: str) -> int:
    count = 0
    lines = data.splitlines()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '@':
                if check_char(row, col, lines):
                    count += 1
    return count

if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
