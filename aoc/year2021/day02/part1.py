from __future__ import annotations

from typing import Any


def main() -> None:
    with open("./input.txt", encoding="utf-8") as f:
        lines: list[Any] = [s.split(" ") for s in f.readlines()]
        lines = [(a, int(b)) for a, b in lines]
        print(solve(lines))


def solve(arr: list[Any]) -> int:
    x, y = 0, 0
    for command, d in arr:
        if command == "forward":
            x += d
        elif command == "backward":
            x -= d
        elif command == "down":
            y += d
        elif command == "up":
            y -= d
    return x * y


if __name__ == "__main__":
    main()
