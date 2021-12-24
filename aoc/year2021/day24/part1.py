from __future__ import annotations

from typing import Any


def main() -> None:
    with open("./input.txt", encoding="utf-8") as f:
        lines: list[Any] = [s.split(" ") for s in f.readlines()]
        lines = [int(a) for a, in lines]
        print(solve(lines))


def solve(arr: list[Any]) -> int:
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            count += 1
    return count


if __name__ == "__main__":
    main()
