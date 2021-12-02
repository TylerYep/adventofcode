from __future__ import annotations

from typing import Any


def main() -> None:
    with open("./input.txt", encoding="utf-8") as f:
        lines: list[Any] = [s.split(" ") for s in f.readlines()]
        lines = [(a, int(b)) for a, b in lines]
        print(solve(lines))


def solve(arr: list[Any]) -> int:
    x, y = 0, 0
    aim = 0
    for command, d in arr:
        if command == "forward":
            x += d
            y += aim * d
        elif command == "down":
            aim += d
        elif command == "up":
            aim -= d
    return x * y


if __name__ == "__main__":
    main()
