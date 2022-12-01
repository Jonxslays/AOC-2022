from typing import Any

from aoc.utils import unimplemented


def read_data() -> Any:
    day = __file__.split(".")[0][-1]
    with open(f"data/day_{day}.txt", "r") as f:
        _data = f.read()


@unimplemented
def question_1() -> Any:
    ...


@unimplemented
def question_2() -> Any:
    ...
