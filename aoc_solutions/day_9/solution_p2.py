"""Advent of Code - Day 9 Part 2"""

from aoc_solutions.utils import get_input, submit_answer

from collections import defaultdict

DAY = 9

def build_area_segments(coords: list[tuple[int, int]]) -> dict[int, list[tuple[int, int]]]:
    n = len(coords)
    vertical_edges = []
    horizontal_segments_by_y = defaultdict(list)

    # Build vertical edges and horizontal boundary segments
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]

        if x1 == x2:
            y_low, y_high = sorted((y1, y2))
            vertical_edges.append((x1, y_low, y_high))
        elif y1 == y2:
            x_low, x_high = sorted((x1, x2))
            horizontal_segments_by_y[y1].append((x_low, x_high))

    crossings_by_y = defaultdict(list)
    for x, y_low, y_high in vertical_edges:
        for y in range(y_low, y_high):
            crossings_by_y[y].append(x)

    allowed_segments = {}

    all_rows = set(crossings_by_y.keys()) | set(horizontal_segments_by_y.keys())
    for y in all_rows:
        segments = []

        xs = crossings_by_y.get(y)
        if xs:
            xs.sort()
            for i in range(0, len(xs), 2):
                x_start = xs[i]
                x_end = xs[i + 1]
                segments.append((x_start, x_end))

        segments.extend(horizontal_segments_by_y.get(y, []))

        if not segments:
            continue

        segments.sort()
        merged = [segments[0]]
        for s, e in segments[1:]:
            last_s, last_e = merged[-1]
            if s <= last_e + 1:  # overlap or touch
                merged[-1] = (last_s, max(last_e, e))
            else:
                merged.append((s, e))

        allowed_segments[y] = merged

    return allowed_segments

def horizontal_segment_inside(y: int, minx: int, maxx: int, allowed_segments) -> bool:
    segs = allowed_segments.get(y)
    if not segs:
        return False
    for s, e in segs:
        if s <= minx and maxx <= e:
            return True
    return False


def vertical_segment_inside(x: int, miny: int, maxy: int, allowed_segments) -> bool:
    for y in range(miny, maxy + 1):
        segs = allowed_segments.get(y)
        if not segs:
            return False
        ok_here = False
        for s, e in segs:
            if s <= x <= e:
                ok_here = True
                break
        if not ok_here:
            return False
    return True


def part_2(data: str) -> int:
    coords = []
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    for line in data.splitlines():
        x, y = map(int, line.split(','))
        coords.append((x, y))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    perimeter = set()
    for i, coord in enumerate(coords):
        x, y = coord
        if i == len(coords) - 1:
            x2, y2 = coords[0]
        else:
            x2, y2 = coords[i + 1]
        if x == x2:
            # Vertical line
            for j in range(min(y, y2), max(y, y2) + 1):
                perimeter.add((x, j))
        elif y == y2:
            # Horizontal line
            for j in range(min(x, x2), max(x, x2) + 1):
                perimeter.add((j, y))
    
    area_segments = build_area_segments(coords)

    max_area = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if x1 == x2 and y1 == y2:
                continue
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                minx, maxx = sorted((x1, x2))
                miny, maxy = sorted((y1, y2))

                # Check that all four sides are inside the red/green area
                if not horizontal_segment_inside(miny, minx, maxx, area_segments):
                    continue
                if not horizontal_segment_inside(maxy, minx, maxx, area_segments):
                    continue
                if not vertical_segment_inside(minx, miny, maxy, area_segments):
                    continue
                if not vertical_segment_inside(maxx, miny, maxy, area_segments):
                    continue

                max_area = area

    return max_area


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
