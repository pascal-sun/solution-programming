from __future__ import annotations

from copy import deepcopy
from pathlib import Path


def parse_data(data: str) -> list[list[str]]:
    return [list(line) for line in data.splitlines()]


def get_start(data: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == "^":
                return y, x
    return -1, -1


def get_new_direction(data: list[list[str]], direction: tuple[int, int], y: int, x: int) -> tuple[int, int]:
    try:
        if data[y + direction[0]][x + direction[1]] == "#":
            # change direction
            if direction == (-1, 0):
                direction = (0, 1)
            elif direction == (0, 1):
                direction = (1, 0)
            elif direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, -1):
                direction = (-1, 0)
    except IndexError:
        # Means he is leaving
        pass
    return direction


def is_leaving(data: list[list[str]], y: int, x: int) -> bool:
    return bool(y < 0 or x < 0 or y >= len(data) or x >= len(data[0]))


def part_1(data: list[list[str]]) -> int:
    y, x = get_start(data)
    direction = (-1, 0)  # Up
    already_seen = {(y, x)}
    while not is_leaving(data, y + direction[0], x + direction[1]):
        direction = get_new_direction(data, direction, y, x)
        y, x = y + direction[0], x + direction[1]
        already_seen.add((y, x))
    return len(already_seen)


def part_2(data: list[list[str]]) -> int:
    count = 0
    for j in range(len(data)):
        for i in range(len(data[0])):
            tmp = deepcopy(data)
            if tmp[j][i] == "#":
                continue
            tmp[j][i] = "#"

            y, x = get_start(tmp)
            direction = (-1, 0)  # Up
            already_seen = set()
            while not is_leaving(tmp, y + direction[0], x + direction[1]):
                if (y, x, direction) in already_seen:
                    count += 1
                    break
                already_seen.add((y, x, direction))
                direction = get_new_direction(tmp, direction, y, x)
                y, x = y + direction[0], x + direction[1]
    return count


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
