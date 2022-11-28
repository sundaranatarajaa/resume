import json
import os

import typer
from rich.console import Console

from .builder import ResumeBuilder

cli_app = typer.Typer()


class FileNotFound(Exception):
    pass


def read_json(path: str):
    if not os.path.exists(path):
        raise FileNotFound("unknown path!")
    with open(path, "r") as details_file:
        details = json.loads(details_file.read())
    return details


def generate_resume(path: str):
    details = read_json(path)
    console = Console(record=True, color_system='truecolor', width=150)
    console.clear()
    resume = ResumeBuilder(console)
    resume.create_resume(details)


@cli_app.command()
def main():
    path="/Users/sundaranatarajaa/PycharmProjects/myresume/myresume/data/details.json"
    generate_resume(path)


if __name__ == "__main__":
    cli_app()
