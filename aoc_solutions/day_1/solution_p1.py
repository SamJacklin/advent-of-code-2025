from aoc_solutions.utils import get_input, submit_answer

DAY = 1
DIAL_STARTING_POSITION = 50

def calculate_single_rotation(position: int, direction: str, distance: int) -> int:
    if direction == "L":
        position = (position - distance) % 100
    elif direction == "R":
        position = (position + distance) % 100
    else:
        raise ValueError("Invalid direction")
    return position

def part_1(data: str) -> int:
    dial_position = DIAL_STARTING_POSITION
    zero_counts = 0
    for line in data.splitlines():
        direction = line[0]
        distance = int(line[1:].strip())
        dial_position = calculate_single_rotation(dial_position, direction, distance)
        if dial_position == 0:
            zero_counts += 1
    return zero_counts

print(part_1(get_input(day=DAY, example=True)))
print(part_1(get_input(day=DAY, example=False)))

submit_answer(day=DAY, part=1, answer=part_1(get_input(day=DAY, example=False)))

