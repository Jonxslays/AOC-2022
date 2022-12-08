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
    help="0 for both questions, py only.",
)
@click.option(
    "-g",
    "--generate",
    type=click.IntRange(1, 25),
    default=None,
    help="Generate a new file for a the day.",
)
@click.option(
    "-l",
    "--language",
    type=click.Choice(("c", "py", "rs")),
    default="py",
    help="The language to be used - One of: c, py, rs.",
)
def aoc(day: int, question: int, generate: int | None, language: str) -> None:
    if generate:
        return utils.create_from_template(generate, language)

    file = f"day_{day}"
    path = f"aoc/{file}" + utils.get_suffix(language)

    if not Path(path).exists():
        if click.prompt(f"Path {path!r} does not exist, create it?"):
            return utils.create_from_template(day, language)

    if language == "py":
        return utils.use_python(file, question)

    if language == "c":
        return utils.use_c(file, path)

    if language == "rs":
        return utils.use_rust(file, path)


if __name__ == "__main__":
    aoc()
