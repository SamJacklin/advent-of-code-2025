"""Advent of Code - Day 6 Part 2"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 6


def part_2(data: str) -> int:
    lines = data.splitlines()
    col_signs = lines.pop(-1).split()
    columns = []
    for line in lines:
        for i, char in enumerate(line):
            if i >= len(columns):
                columns.append([])
            columns[i].append(char)
    separators = set()
    for i, col in enumerate(columns):
        if all(c == ' ' for c in col):
            separators.add(i)
    separators.add(len(columns))
    total = 0
    for i, separator in enumerate(sorted(separators)):
        if i == 0:
            start = 0
        else:
            start = sorted(separators)[i-1] + 1
        end = separator
        col_sign = col_signs[i]
        col_chars = []
        col_total = 0
        for col in columns[start:end]:
            val = int(''.join(col).strip())
            if col_sign == '+':
                col_total += val
            elif col_sign == '*':
                if col_total == 0:
                    col_total = val
                else:
                    col_total *= val
        total += col_total
    return total


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
