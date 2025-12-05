"""Advent of Code - Day 4 Part 2"""

from aoc_solutions.utils import get_input, submit_answer
import queue

DAY = 4

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
LIMIT = 3

def check_char(row: int, col: int, lines: list[str]) -> tuple[bool, list[tuple[int, int]]]:
    count = 0
    to_recheck = []

    for d_row, d_col in DIRECTIONS:
        n_row, n_col = row + d_row, col + d_col
        # Check bounds
        if 0 <= n_row < len(lines) and 0 <= n_col < len(lines[n_row]):
            if lines[n_row][n_col] == '@':
                to_recheck.append((n_row, n_col))
                count += 1
    if count > LIMIT:
        return False, None
    return True, to_recheck

def part_2(data: str) -> int:
    count = 0
    recheck_queue = queue.Queue()
    lines = [list(line) for line in data.splitlines()]
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '@':
                is_removable, to_recheck = check_char(row, col, lines)
                if is_removable:
                    count += 1
                    lines[row][col] = '.'
                    for item in to_recheck:
                        recheck_queue.put(item)

    while not recheck_queue.empty():
        row, col = recheck_queue.get()
        if lines[row][col] != '@':
            continue
        is_removable, to_recheck = check_char(row, col, lines)
        if is_removable:
            count += 1
            lines[row][col] = '.'
            for item in to_recheck:
                recheck_queue.put(item)

    return count



if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
