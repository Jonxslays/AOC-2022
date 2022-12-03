from pathlib import Path
from typing import Any

from aoc.utils import unimplemented
from aoc.utils import read_input_data


def read_data() -> Any:
    day = __file__.split(".")[0][-1]
    path = Path(f"data/day_{day}.txt")
    _data = read_input_data(path)


@unimplemented
def question_1() -> Any:
    ...


@unimplemented
def question_2() -> Any:
    ...
