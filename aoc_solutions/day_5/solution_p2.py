"""Advent of Code - Day 5 Part 2"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 5


def part_2(data: str) -> int:
    sections = data.split("\n\n")
    ranges, idxs = sections[0], sections[1]
    ranges_list = []
    total_valid_ids = 0
    for id_range in ranges.splitlines():
        start, end = map(int, id_range.split("-"))
        ranges_list.append((start, end))
    sorted_ranges = sorted(ranges_list, key=lambda x: x[0])

    # Remove engulfed ranges
    for i in range(len(sorted_ranges) - 1, 0, -1):
        if sorted_ranges[i-1][0] <= sorted_ranges[i][0] and sorted_ranges[i-1][1] >= sorted_ranges[i][1]:
            print("Removing engulfed range:", sorted_ranges[i])
            sorted_ranges.pop(i)
            continue
    
        if i < len(sorted_ranges)-1:
            if sorted_ranges[i+1][0] <= sorted_ranges[i][0] and sorted_ranges[i+1][1] >= sorted_ranges[i][1]:
                print("Removing engulfed range:", sorted_ranges[i])
                sorted_ranges.pop(i)
                continue

    # Remove crossing ranges
    for i in range(len(sorted_ranges) - 1, 1, -1):
        if sorted_ranges[i-1][0] < sorted_ranges[i][0] <= sorted_ranges[i-1][1]:
            sorted_ranges[i] = (sorted_ranges[i-1][1] + 1, sorted_ranges[i][1])
    
    # Check if ids overlap after adjustment
    for i in range(len(sorted_ranges) - 1):
        if sorted_ranges[i][1] >= sorted_ranges[i+1][0]:
            print("Overlap detected:", sorted_ranges[i], sorted_ranges[i+1])

    # Simple count
    for id_range in sorted_ranges:
        start, end = id_range
        total_valid_ids += end - start + 1
        
    return total_valid_ids
    
    


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
