from pathlib import Path

import click

from aoc import utils


# Apparently the click deco typing is broken again :(
@click.command()  # pyright: ignore [reportUnknownMemberType]
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
    help="0 for both questions, py only.",
)
@click.option(
    "-g",
    "--generate",
    type=click.IntRange(1, 25),
    default=None,
    help="Generate a new file for a the day.",
)
def aoc(day: int, question: int, generate: int | None) -> None:
    file = f"day_{day}"
    path = f"aoc/{file}.py"

    if not Path(path).exists() or generate:
        if click.prompt(f"Path {path!r} does not exist, create it?"):
            return utils.create_from_template(generate if generate else day)

    return utils.use_python(file, question)


if __name__ == "__main__":
    aoc()
