from __future__ import annotations

from typing import Any


def main() -> None:
    with open("./input.txt", encoding="utf-8") as f:
        lines: list[Any] = [s.strip().split(" ") for s in f.readlines()]
        lines = [a for a, in lines]
        print(solve(lines))


def solve(arr: list[Any]) -> int:
    z = len(arr[0])
    zeros = [0] * z
    ones = [0] * z
    for line in arr:
        for i, ch in enumerate(line):
            if ch == "0":
                zeros[i] += 1
            else:
                ones[i] += 1

    oxy, co2 = "", ""
    for i in range(z):
        if zeros[i] > ones[i]:
            oxy += "0"
            co2 += "1"
        else:
            oxy += "1"
            co2 += "0"

    oxygen = int(oxy, base=2)
    c02 = int(co2, base=2)

    return oxygen * c02


if __name__ == "__main__":
    main()
