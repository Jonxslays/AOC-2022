import functools
import importlib
import sys
from pathlib import Path
from typing import Any, Callable

QuestionT = Callable[[], Any]
MaybeQuestionT = QuestionT | None


def read_input_data(path: Path) -> str:
    if not path.exists():
        print(f"No data file located at {str(path)!r}")
        sys.exit(1)

    with open(path, "r") as f:
        return f.read()


def pretty_name(func: QuestionT) -> str:
    return func.__name__.replace("_", " ").title()


def unimplemented(func: QuestionT) -> QuestionT:
    @functools.wraps(func)
    def inner() -> Any:
        print(f"{pretty_name(func)} is not implemented yet.")
        return None

    return inner


def map_errors(
    *data: tuple[MaybeQuestionT, str]
) -> tuple[list[QuestionT], list[str]]:
    questions: list[QuestionT] = []
    errors: list[str] = []

    for question, error in data:
        if not question:
            errors.append(error)
        else:
            questions.append(question)

    return questions, errors


def extract_functions_py(mod: dict[str, Any], q: int) -> list[QuestionT]:
    func1: MaybeQuestionT = mod.get("question_1")
    func2: MaybeQuestionT = mod.get("question_2")
    errors: list[str] = []

    if q == 0:
        questions, err = map_errors(
            (func1, "Question 1 function is missing."),
            (func2, "Question 2 function is missing."),
        )

        errors.extend(err)
    elif q == 1:
        questions, err = map_errors(
            (func1, "Question 1 function is missing."),
        )

        errors.extend(err)
    else:
        questions, err = map_errors(
            (func2, "Question 2 function is missing."),
        )

        errors.extend(err)

    if errors:
        print("\n".join(errors))
        sys.exit(1)

    return questions


def create_from_template(day: int) -> None:
    path = Path(f"aoc/day_{day}.py")
    path.touch()

    with open("aoc/templates/template.py", "rb") as f:
        path.write_bytes(f.read())

    print(f"Successfully initialized {path.as_posix()!r} with AOC template.")
    return None


def use_python(file: str, question: int) -> None:
    for func in extract_functions_py(
        importlib.import_module(f"aoc.{file}").__dict__, question
    ):
        if result := func():
            print(f"{pretty_name(func)}: {result}")
