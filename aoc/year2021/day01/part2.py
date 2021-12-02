from __future__ import annotations

from typing import Any


def main() -> None:
    with open("./input.txt", encoding="utf-8") as f:
        lines: list[Any] = [s.split(" ") for s in f.readlines()]
        lines = [int(a) for a, in lines]
        print(solve(lines))


def solve(arr: list[Any]) -> int:
    count = 0
    prev = 100000000
    for i in range(len(arr) - 2):
        curr = arr[i] + arr[i + 1] + arr[i + 2]
        if curr > prev:
            count += 1
        prev = curr
    return count


if __name__ == "__main__":
    main()
