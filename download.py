from __future__ import annotations

import argparse
import time
from datetime import date
from pathlib import Path
from typing import cast
from urllib.error import URLError
from urllib.request import Request, urlopen


def get_input(year: int, day: int) -> str:
    with open(".env", encoding="utf-8") as f:
        contents = f.read()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    req = Request(url, headers={"Cookie": contents.strip()})
    return cast(str, urlopen(req).read().decode())


def main() -> None:
    today = date.today()
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, default=today.year)
    parser.add_argument("--day", type=int, default=today.day + 1)
    args = parser.parse_args()

    for _ in range(5):
        try:
            s = get_input(args.year, args.day)
        except URLError as e:
            print(f"Zzz: not ready yet: {e}")
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit("Timed out after 5 attempts")

    path = Path(f"aoc/year{args.year}/day{args.day:02d}")
    path.mkdir(parents=True, exist_ok=True)
    (path / "input.txt").write_text(s, encoding="utf-8")

    for i in range(1, 3):
        part = Path(f"aoc/year{args.year}/day01/part1.py").read_text(encoding="utf-8")
        (path / f"part{i}.py").write_text(part, encoding="utf-8")

    lines = s.splitlines()
    if len(lines) > 10:
        for line in lines[:10]:
            print(line)
        print("...")
    else:
        print(lines[0][:80])
        print("...")


if __name__ == "__main__":
    main()
