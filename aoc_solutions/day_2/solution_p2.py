"""Advent of Code - Day 2 Part 2"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 2

def check_for_repeating_digits(lower: int, upper: int) -> int:
    repetition_sum = 0
    for number in range(lower, upper + 1):
        num_str = str(number)
        for i in range(1, len(num_str)):
            if len(num_str) % i != 0:
                continue # Must be divisible to have repeating segments
            # Split string into equal parts of length i
            parts = [num_str[j:j+i] for j in range(0, len(num_str), i)]

            # Check if all parts are the same
            if all(part == parts[0] for part in parts):
                repetition_sum += number
                break
    
    return repetition_sum

def part_2(data: str) -> int:
    total_sum = 0
    for id_range in data.split(','):
        lower, upper = map(int, id_range.split('-'))
        total_sum += check_for_repeating_digits(lower, upper)
    return total_sum



if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
