from aocd import get_data, submit
from aoc_solutions.config import settings

def get_input(day: int, example: bool = False) -> str:
    if example:
        with open(f"aoc_solutions/day_{day}/example_input.txt") as f:
            data = f.read()
        return data
    
    data = get_data(day=day, year=settings.year, session=settings.aoc_session)
    return data

def submit_answer(day: int, part: int, answer: int) -> None:
    part_letter = "a" if part == 1 else "b"
    print(submit(answer, part=part_letter, day=day, year=settings.year, session=settings.aoc_session))
    