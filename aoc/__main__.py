import importlib
from pathlib import Path

import click

from aoc import utils


@click.command()
@click.option(
    "-d",
    "--day",
    type=click.IntRange(1, 25),
    default=1,
    help="The desired day of code to run.",
)
@click.option(
    "-q",
    "--question",
    type=click.IntRange(0, 2),
    default=0,
    help="The question to run (0 for both).",
)
@click.option(
    "-g",
    "--generate",
    type=click.IntRange(1, 25),
    default=None,
    help="Generate a new py file for a particular day.",
)
def aoc(day: int, question: int, generate: int | None) -> None:
    if generate:
        return utils.create_from_template(generate)

    file = f"day_{day}"
    path = f"aoc/{file}.py"

    if not Path(path).exists():
        if click.prompt(f"Path {path!r} does not exist, create it?"):
            return utils.create_from_template(day)

    for func in utils.extract_functions(
        importlib.import_module(f"aoc.{file}").__dict__, question
    ):
        if result := func():
            print(f"{utils.pretty_name(func)}: {result}")


if __name__ == "__main__":
    aoc()
