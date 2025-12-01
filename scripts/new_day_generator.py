#!/usr/bin/env python3
import os
import sys
from pathlib import Path

TEMPLATE_P1 = '''"""Advent of Code - Day {day} Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = {day}


def part_1(data: str) -> int:
    # TODO: implement
    return 0


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
'''

TEMPLATE_P2 = '''"""Advent of Code - Day {day} Part 2"""

from aoc_solutions.utils import get_input, submit_answer

DAY = {day}


def part_2(data: str) -> int:
    # TODO: implement
    return 0


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
'''


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/new_day.py <day-number>")
        sys.exit(1)

    day = int(sys.argv[1])
    base_dir = Path("aoc_solutions") / f"day_{day}"

    if base_dir.exists():
        print(f"Day {day} already exists at {base_dir}")
        sys.exit(1)

    print(f"Creating structure for Day {day}...")

    base_dir.mkdir(parents=True)
    (base_dir / "__init__.py").write_text('__all__ = ["solution_p1", "solution_p2"]\n')
    (base_dir / "example_input.txt").touch()
    (base_dir / "solution_p1.py").write_text(TEMPLATE_P1.format(day=day))
    (base_dir / "solution_p2.py").write_text(TEMPLATE_P2.format(day=day))

    print(f"Day {day} scaffolded successfully!")


if __name__ == "__main__":
    main()
