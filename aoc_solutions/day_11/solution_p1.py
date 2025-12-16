"""Advent of Code - Day 11 Part 1"""

from aoc_solutions.utils import get_input, submit_answer

DAY = 11

def count_paths(node, graph, memo):
    if node == 'out':
        return 1
    if node in memo:
        return memo[node]

    total = 0
    for neighbour in graph.get(node, []):
        total += count_paths(neighbour, graph, memo)

    memo[node] = total
    return total


def part_1(data: str) -> int:
    graph = {}
    for line in data.splitlines():
        parts = line.split(': ')
        graph[parts[0]] = parts[1].split(' ')

    start = 'you'
    route_memory = {}
    total_paths = count_paths(start, graph, route_memory)

    return total_paths



        



if __name__ == "__main__":
    example = get_input(day=DAY, example=True)
    print("Example:", part_1(example))

    real = get_input(day=DAY, example=False)
    print("Answer:", part_1(real))
    submit_answer(day=DAY, part=1, answer=part_1(real))
