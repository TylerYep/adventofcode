from __future__ import annotations

import argparse
import os
import time
from datetime import date
from pathlib import Path
from typing import cast
from urllib.error import URLError
from urllib.request import Request, urlopen


def get_input_file(year: int, day: int) -> str:
    with open(".env", encoding="utf-8") as f:
        contents = f.read()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    req = Request(url, headers={"Cookie": contents.strip()})
    return cast(str, urlopen(req).read().decode())


def get_input_file_with_retry(year: int, day: int) -> str:
    for _ in range(3):
        try:
            return get_input_file(year, day)
        except URLError as e:
            print(f"Zzz: not ready yet: {e}")
            time.sleep(1)
    raise SystemExit("Timed out after 3 attempts")


def init_new_day_folder(year: int, day: int) -> tuple[Path, str]:
    path = Path(f"aoc/year{year}/day{day:02d}")
    if path.is_dir():
        return path, ""

    input_txt = get_input_file_with_retry(year, day)
    path.mkdir(parents=True, exist_ok=True)
    (path / "input.txt").write_text(input_txt, encoding="utf-8")
    (path / "__init__.py").touch()

    for i in range(1, 3):
        part = Path(f"aoc/year{year}/day01/part1.py").read_text(encoding="utf-8")
        (path / f"part{i}.py").write_text(part, encoding="utf-8")

    return path, input_txt


def preview_input(input_txt: str) -> None:
    lines = input_txt.splitlines()
    if len(lines) > 10:
        for line in lines[:10]:
            print(line)
        print("...")
    else:
        print(lines[0][:80])
        print("...")


def main() -> None:
    today = date.today()
    if today.month != 12 or today.day > 25:
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, default=today.year)
    parser.add_argument("--day", type=int, default=today.day + 1)
    args = parser.parse_args()

    path, input_txt = init_new_day_folder(args.year, args.day)
    if not input_txt:
        return

    preview_input(input_txt)
    os.chdir(os.getcwd() / path)


if __name__ == "__main__":
    main()
