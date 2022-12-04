from pathlib import Path
from typing import Any

# from aoc.utils import unimplemented
from aoc.utils import read_input_data

GroupT = tuple[str, str, str]
GroupsT = list[tuple[GroupT, GroupT]]


def read_data() -> Any:
    day = __file__.split(".")[0][-1]
    path = Path(f"data/day_{day}.txt")
    data = read_input_data(path).strip().split("\n")
    return data


def split_line(line: str) -> tuple[str, str]:
    middle = len(line) // 2
    return (line[:middle], line[middle:])


def get_value(char: str) -> int:
    return ord(char) - 38 if char.isupper() else ord(char) - 96


# @unimplemented
def question_1() -> Any:
    data = read_data()
    total = 0

    for line in data:
        left, right = split_line(line)
        total += get_value(list(filter(lambda l: l in right, left))[0])

    return total


def group_by_x(x: int, groups: Any) -> Any:
    return list(zip(*([iter(groups)] * x)))


def split_group(group: tuple[str, str, str]) -> str:
    return list(filter(lambda s: s in group[1] and s in group[2], group[0]))[0]


def to_value(group: tuple[str, str, str]) -> int:
    return get_value(split_group(group))


# @unimplemented
def question_2() -> Any:
    data = read_data()
    groups = group_by_x(3, data)
    groups: GroupsT = group_by_x(2, groups)
    return sum(map(lambda g: to_value(g[0]) + to_value(g[1]), groups))
