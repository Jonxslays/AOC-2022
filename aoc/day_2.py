from enum import Enum
from pathlib import Path
from typing import Any

# from aoc.utils import unimplemented
from aoc.utils import read_input_data


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    LOST = 0
    DRAW = 3
    WON = 6


ELF_MAPPING = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
}


USER_MAPPING = {
    "X": Choice.ROCK,
    "Y": Choice.PAPER,
    "Z": Choice.SCISSORS,
}


OUTCOME_MAPPING = {
    "X": Outcome.LOST,
    "Y": Outcome.DRAW,
    "Z": Outcome.WON,
}


def read_data() -> Any:
    day = __file__.split(".")[0][-1]
    path = Path(f"data/day_{day}.txt")
    data = read_input_data(path).strip().split("\n")
    return [tuple(item.split()) for item in data]


def get_outcome(elf: Choice, us: Choice) -> Outcome:
    if elf is Choice.PAPER:
        if us is Choice.PAPER:
            return Outcome.DRAW

        if us is Choice.ROCK:
            return Outcome.LOST

        return Outcome.WON

    if elf is Choice.ROCK:
        if us is Choice.PAPER:
            return Outcome.WON

        if us is Choice.ROCK:
            return Outcome.DRAW

        return Outcome.LOST

    if us is Choice.PAPER:
        return Outcome.LOST

    if us is Choice.ROCK:
        return Outcome.WON

    return Outcome.DRAW


def find_win(other: Choice) -> Choice:
    if other is Choice.SCISSORS:
        return Choice.ROCK

    if other is Choice.ROCK:
        return Choice.PAPER

    return Choice.SCISSORS


def find_lose(other: Choice) -> Choice:
    if other is Choice.SCISSORS:
        return Choice.PAPER

    if other is Choice.ROCK:
        return Choice.SCISSORS

    return Choice.ROCK


def convert_outcome(elf: Choice, outcome: Outcome) -> Choice:
    if outcome is Outcome.WON:
        return find_win(elf)

    if outcome is Outcome.LOST:
        return find_lose(elf)

    return elf


# @unimplemented
def question_1() -> Any:
    data = read_data()
    total = 0

    for data_point in data:
        elf = ELF_MAPPING[data_point[0]]
        us = USER_MAPPING[data_point[1]]
        outcome = get_outcome(elf, us)
        total += outcome.value + us.value

    return total

# @unimplemented
def question_2() -> Any:
    data = read_data()
    total = 0

    for data_point in data:
        elf = ELF_MAPPING[data_point[0]]
        outcome = OUTCOME_MAPPING[data_point[1]]
        us = convert_outcome(elf, outcome)
        total += outcome.value + us.value

    return total
