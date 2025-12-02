import argparse
from importlib import import_module
from typing import Any, Callable

from aoc_solutions.utils import get_input
from aoc_solutions.efficiency_leaderboard import (
    measure_efficiency,
    print_leaderboard,
)


def resolve_part_func(day: int, part: int) -> Callable[[str], Any]:
    module_name = f"aoc_solutions.day_{day}.solution_p{part}"
    func_name = f"part_{part}"

    module = import_module(module_name)
    try:
        func = getattr(module, func_name)
    except AttributeError as e:
        raise SystemExit(f"Could not find {func_name} in {module_name}") from e
    return func


def run_once(
    day: int,
    part: int,
) -> int:
    """Run a single (day, part) with efficiency measuring."""
    func = resolve_part_func(day, part)
    data = get_input(day=day)

    with measure_efficiency(day=day, part=part):
        result = func(data)

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run AoC solution with efficiency measurements."
    )
    parser.add_argument("day", type=int, help="Day number (e.g., 1)")
    parser.add_argument("part", type=int, choices=[1, 2], help="Part number (1 or 2)")
    parser.add_argument(
        "--no-leaderboard",
        action="store_true",
        help="Do not print the leaderboard after running.",
    )

    args = parser.parse_args()

    run_once(
        day=args.day,
        part=args.part,
    )

    if not args.no_leaderboard:
        print_leaderboard(args.day)


if __name__ == "__main__":
    main()
