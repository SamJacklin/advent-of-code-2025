"""Advent of Code - Day 11 Part 2"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 11


def count_paths(node, graph, memo, dac_visited=False, fft_visited=False):
    if node == 'out':
        if dac_visited and fft_visited:
            return 1
        else:
            return 0

    if node == 'dac':
        dac_visited = True
    if node == 'fft':
        fft_visited = True

    if (node, dac_visited, fft_visited) in memo:
        return memo[(node, dac_visited, fft_visited)]

    total = 0
    for neighbour in graph.get(node, []):
        total += count_paths(neighbour, graph, memo, dac_visited, fft_visited)

    memo[(node, dac_visited, fft_visited)] = total
    return total


def part_2(data: str) -> int:
    graph = {}
    for line in data.splitlines():
        parts = line.split(': ')
        graph[parts[0]] = parts[1].split(' ')

    start = 'svr'
    route_memory = {}
    total_paths = count_paths(start, graph, route_memory)

    return total_paths


if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_2(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_2(real))
    submit_answer(day=DAY, part=2, answer=part_2(real))
