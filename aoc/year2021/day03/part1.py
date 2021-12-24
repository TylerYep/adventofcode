from __future__ import annotations

from typing import Any


def main() -> None:
    with open("./input.txt", encoding="utf-8") as f:
        lines: list[Any] = [s.strip().split(" ") for s in f.readlines()]
        lines = [a for a, in lines]
        # lines = [
        #     "00100",
        #     "11110",
        #     "10110",
        #     "10111",
        #     "10101",
        #     "01111",
        #     "00111",
        #     "11100",
        #     "10000",
        #     "11001",
        #     "00010",
        #     "01010",
        # ]  # 198
        print(solve(lines))


def solve(arr: list[Any]) -> int:
    print(arr)
    z = len(arr[0])
    zeros = [0] * z
    ones = [0] * z
    for line in arr:
        for i, ch in enumerate(line):
            if ch == "0":
                zeros[i] += 1
            else:
                ones[i] += 1

    gam, eps = "", ""
    for i in range(z):
        if zeros[i] > ones[i]:
            gam += "0"
            eps += "1"
        else:
            gam += "1"
            eps += "0"

    gamma = int(gam, base=2)
    epsilon = int(eps, base=2)
    return gamma * epsilon


if __name__ == "__main__":
    main()
