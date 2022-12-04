from pathlib import Path
from typing import Any

# from aoc.utils import unimplemented
from aoc.utils import read_input_data


def read_data() -> Any:
    day = __file__.split(".")[0][-1]
    path = Path(f"data/day_{day}.txt")
    data = read_input_data(path).strip().split("\n")
    return list(map(lambda l: l.split(","), data))


def get_int_range(data: str) -> range:
    return range(int(data.split("-")[0]), int(data.split("-")[1]) + 1)


def get_int_ranges(data: list[list[str]]) -> list[list[range]]:
    result: list[list[range]] = []

    for item in data:
        left = get_int_range(item[0])
        right = get_int_range(item[1])
        result.append([left, right])

    return result


# @unimplemented
def question_1() -> Any:
    data = get_int_ranges(read_data())
    total = 0

    for pair in data:
        intersection = set(pair[0]).intersection(pair[1])
        if any(len(intersection) == len(p) for p in pair):
            total += 1

    return total


# @unimplemented
def question_2() -> Any:
    data = get_int_ranges(read_data())
    total = 0

    for pair in data:
        intersection = set(pair[0]).intersection(pair[1])
        if intersection:
            total += 1

    return total
