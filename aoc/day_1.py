from pathlib import Path
from typing import Any

# from aoc.utils import unimplemented
from aoc.utils import read_input_data


def read_data() -> Any:
    day = __file__.split(".")[0][-1]
    path = Path(f"data/day_{day}.txt")
    data = read_input_data(path)

    return tuple(
        [int(i) for i in individual.split("\n")]
        for individual in map(str.strip, data.split("\n\n"))
    )


# @unimplemented
def question_1() -> Any:
    return max(sum(i) for i in read_data())


# @unimplemented
def question_2() -> Any:
    return sum(sorted(sum(i) for i in read_data())[-3:])
