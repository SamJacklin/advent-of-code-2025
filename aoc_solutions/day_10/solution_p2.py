"""Advent of Code - Day 10 Part 2"""

from aoc_solutions.utils import get_input, submit_answer
from functools import lru_cache

DAY = 10

def parity_mask(vec: tuple[int, ...]) -> int:
    pm = 0
    for i, v in enumerate(vec):
        if v & 1:
            pm |= (1 << i)
    return pm


def part_2(data: str) -> int:
    total = 0

    for line in data.splitlines():
        if not line.strip():
            continue

        parts = line.split(' ')

        buttons_raw = parts[1:-1]
        buttons = []
        for button in buttons_raw:
            inner = button.strip()[1:-1]
            buttons.append([int(x) for x in inner.split(',') if x])

        joltage = parts[-1]
        target_joltage = tuple(int(x) for x in joltage[1:-1].split(","))
        target_joltage_length = len(target_joltage)
        num_buttons = len(buttons)

        subsets_by_parity = {}
        for mask in range(1 << num_buttons):
            effect = [0] * target_joltage_length
            press_count = 0
            for j in range(num_buttons):
                if (mask >> j) & 1:
                    press_count += 1
                    for idx in buttons[j]:
                        effect[idx] += 1
            effect = tuple(effect)
            pm = parity_mask(effect)
            subsets_by_parity.setdefault(pm, []).append((effect, press_count))

        @lru_cache(maxsize=None)
        def solve(state: tuple[int, ...]) -> int:
            if all(v == 0 for v in state):
                return 0

            pm = parity_mask(state)
            best = 10**18

            for effect, presses in subsets_by_parity.get(pm, []):
                if any(effect[i] > state[i] for i in range(target_joltage_length)):
                    continue

                next_state = tuple((state[i] - effect[i]) // 2 for i in range(target_joltage_length))
                best = min(best, presses + 2 * solve(next_state))

            return best

        total += solve(target_joltage)

    return total


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
