"""Advent of Code - Day 8 Part 1"""

from math import prod
from aoc_solutions.utils import get_input, submit_answer

DAY = 8


def part_1(data: str) -> int:
    coordinates = []
    for line in data.splitlines():
        x, y, z = map(int, line.split(','))
        coordinates.append((x, y, z))

    coordinate_pairs = []
    for i, (x1, y1, z1) in enumerate(coordinates):
        for j, (x2, y2, z2) in enumerate(coordinates):
            if i < j:
                coordinate_pairs.append(((i,j), (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2))

    max_connections = 1000
    circuits: list[set[int]] = []
    for i in range(max_connections):
        min_distance = min(coordinate_pairs, key=lambda x: x[1])

        coordinate_pairs.remove(min_distance)
        found = False
        for circuit in circuits:
            if min_distance[0][0] in circuit or min_distance[0][1] in circuit:
                if not found:
                    circuit.update((min_distance[0][0], min_distance[0][1]))
                    found = True
                else:
                    circuit.update((min_distance[0][0], min_distance[0][1]))
                    # Merge circuits
                    for other_circuit in circuits:
                        if other_circuit is not circuit and (min_distance[0][0] in other_circuit or min_distance[0][1] in other_circuit):
                            circuit.update(other_circuit)
                            circuits.remove(other_circuit)
                    break
        if not found:
            circuits.append({min_distance[0][0], min_distance[0][1]})
    

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)[:3]  # get the three largest circuits
    total = prod(len(circuit) for circuit in circuits)
    return total


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
