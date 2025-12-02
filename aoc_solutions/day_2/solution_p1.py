"""Advent of Code - Day 2 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 2

def check_for_repeating_digits(lower: int, upper: int) -> int:
    repetition_sum = 0
    for number in range(lower, upper + 1):
        num_str = str(number)
        if len(num_str) % 2 != 0:
            continue  # Must have even number of digits to have a pair
        left_half = num_str[:len(num_str)//2]
        right_half = num_str[len(num_str)//2:]
        if left_half == right_half:
            repetition_sum += number

    return repetition_sum

def part_1(data: str) -> int:
    total_sum = 0
    for id_range in data.split(','):
        lower, upper = map(int, id_range.split('-'))
        total_sum += check_for_repeating_digits(lower, upper)
    return total_sum


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
