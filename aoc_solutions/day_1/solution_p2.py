from aoc_solutions.utils import get_input, submit_answer

DAY = 1
DIAL_STARTING_POSITION = 50

def calculate_rotation_crosses_zero(position: int, direction: str, distance: int) -> int:
    if direction == "L":
        cross_zero = abs((position - distance) // 100)
        final_position = (position - distance) % 100
        if position == 0:
            cross_zero -= 1

        if final_position == 0:
            cross_zero += 1

    elif direction == "R":
        cross_zero = (position + distance) // 100
        final_position = (position + distance) % 100
    else:
        raise ValueError("Invalid direction")
    return final_position, cross_zero

def part_2(data: str) -> int:
    dial_position = DIAL_STARTING_POSITION
    zero_counts = 0
    for line in data.splitlines():
        direction = line[0]
        distance = int(line[1:].strip())
        dial_position, crosses = calculate_rotation_crosses_zero(dial_position, direction, distance)
        zero_counts += crosses
    return zero_counts

print(part_2(get_input(day=DAY, example=True)))
print(part_2(get_input(day=DAY, example=False)))

submit_answer(day=DAY, part=2, answer=part_2(get_input(day=DAY, example=False)))

