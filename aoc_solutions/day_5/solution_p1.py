"""Advent of Code - Day 5 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 5


def part_1(data: str) -> int:
    sections = data.split("\n\n")
    ranges, idxs = sections[0], sections[1]
    ranges_list = []
    for id_range in ranges.splitlines():
        start, end = map(int, id_range.split("-"))
        ranges_list.append((start, end))
    
    count = 0
    for idx in map(int, idxs.splitlines()):
        for start, end in ranges_list:
            if start <= idx <= end:
                count += 1
                break
    return count

if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
