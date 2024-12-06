from __future__ import annotations

from copy import deepcopy
from pathlib import Path

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)


def parse_data(data: str) -> list[list[str]]:
    return [list(line) for line in data.splitlines()]


def get_start(data: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == "^":
                return y, x
    return -1, -1


def get_new_direction(data: list[list[str]], direction: tuple[int, int], y: int, x: int) -> tuple[int, int]:
    while data[y + direction[0]][x + direction[1]] == "#":
        if direction == UP:
            direction = RIGHT
        elif direction == RIGHT:
            direction = DOWN
        elif direction == DOWN:
            direction = LEFT
        elif direction == LEFT:
            direction = UP
    return direction


def is_leaving(data: list[list[str]], y: int, x: int) -> bool:
    return bool(y < 0 or x < 0 or y >= len(data) or x >= len(data[0]))


def part_1(data: list[list[str]]) -> tuple[int, set[tuple[int, int]]]:
    y, x = get_start(data)
    direction = UP
    already_seen = {(y, x)}
    while not is_leaving(data, y + direction[0], x + direction[1]):
        direction = get_new_direction(data, direction, y, x)
        y, x = y + direction[0], x + direction[1]
        already_seen.add((y, x))
    return len(already_seen), already_seen


def part_2(data: list[list[str]]) -> int:
    _, path = part_1(data)
    count = 0
    for j, i in path:
        tmp = deepcopy(data)
        tmp[j][i] = "#"
        y, x = get_start(tmp)
        direction = UP
        already_seen = {(y, x, direction)}
        while not is_leaving(tmp, y + direction[0], x + direction[1]):
            direction = get_new_direction(tmp, direction, y, x)
            y, x = y + direction[0], x + direction[1]
            if (y, x, direction) in already_seen:
                count += 1
                break
            already_seen.add((y, x, direction))
    return count


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    print(f"Part 1: {part_1(data)[0]}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
