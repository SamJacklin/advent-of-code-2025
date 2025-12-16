"""Advent of Code - Day 10 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 10


def part_1(data: str) -> int:
    total = 0
    for line in data.splitlines():
        parts = line.split(' ')
        indicator = []
        indicator_results = []
        for char in parts[0][1:-1]:
            indicator.append(0)
            if char == '.':
                indicator_results.append(0)
            else:
                indicator_results.append(1)

        buttons_raw = parts[1:-1]
        buttons = []
        for button in buttons_raw:
            buttons.append(button.strip()[1:-1].split(','))
        joltage = parts[-1]
        
        depth = 0
        running = True
        states = [indicator]
        while running:
            depth += 1
            new_states = []
            for state in states:
                for button in buttons:
                    new_indicator = state.copy()
                    
                    for i in button:
                        new_indicator[int(i)] ^= 1  # Toggle the bit

                    if new_indicator == indicator_results:
                        total += depth
                        running = False
                        break
                    new_states.append(new_indicator)
                if not running:
                    break
            states = new_states

    return total

if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
