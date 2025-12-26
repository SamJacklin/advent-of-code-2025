"""Advent of Code - Day 12 Part 1"""

from aoc_solutions.utils import get_input, submit_answer
from dataclasses import dataclass

DAY = 12

@dataclass
class ShapeInfo:
    area: int
    width: int
    height: int

def parse_shapes(shape_blocks: list[str]) -> list[ShapeInfo]:
    shapes: list[ShapeInfo] = []

    for block in shape_blocks:
        lines = block.splitlines()
        grid = lines[1:]

        area = sum(row.count("#") for row in grid)
        height = len(grid)
        width = len(grid[0]) if grid else 0

        shapes.append(ShapeInfo(area=area, width=width, height=height))

    return shapes

def region_passes_trivial_checks(
    region_line: str,
    shapes: list[ShapeInfo],
) -> bool:
    size_part, counts_part = region_line.split(":")
    region_width, region_height = map(int, size_part.split("x"))
    counts = list(map(int, counts_part.split()))

    region_area = region_width * region_height
    total_present_area = sum(
        count * shape.area
        for count, shape in zip(counts, shapes)
    )

    if total_present_area > region_area:
        return False

    for count, shape in zip(counts, shapes):
        if count == 0:
            continue

        w, h = shape.width, shape.height
        fits_in_region = (
            (w <= region_width and h <= region_height)
            or (h <= region_width and w <= region_height)
        )

        if not fits_in_region:
            return False

    return True

def part_1(data: str) -> int:
    blocks = data.strip().split("\n\n")
    regions_block = blocks.pop(-1)

    shapes = parse_shapes(blocks)

    # Count how many regions pass the trivial necessary checks
    count_feasible = 0
    for line in regions_block.splitlines():
        line = line.strip()
        if not line:
            continue

        if region_passes_trivial_checks(line, shapes):
            count_feasible += 1

    return count_feasible


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
