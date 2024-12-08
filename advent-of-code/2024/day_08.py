from collections import defaultdict
from pathlib import Path


def parse_data(data: str) -> dict[complex, str]:
    map_ = {}
    for y, row in enumerate(data.splitlines()):
        for x, cell in enumerate(row):
            map_[complex(x, y)] = cell
    return map_


def get_antennas(data: dict[complex, str]) -> dict[str, list[complex]]:
    antennas = defaultdict(list)
    for position, value in data.items():
        if value != ".":
            antennas[value].append(position)
    return antennas


def get_antinode(data: dict[complex, str], first_antenna: complex, second_antenna: complex) -> complex | None:
    if first_antenna == second_antenna:
        return None
    antinode = second_antenna - (first_antenna - second_antenna)
    if antinode not in data:
        return None
    return antinode


def get_antinodes(data: dict[complex, str], first_antenna: complex, second_antenna: complex) -> list[complex]:
    third_antinode = get_antinode(data, first_antenna, second_antenna)
    first_antenna, second_antenna = second_antenna, third_antinode
    antinodes = []
    while second_antenna is not None:
        antinodes.append(second_antenna)
        third_antinode = get_antinode(data, first_antenna, second_antenna)
        first_antenna, second_antenna = second_antenna, third_antinode
    return antinodes


def part_1(data: dict[complex, str]) -> int:
    antennas = get_antennas(data)
    antinodes = set()
    for values in antennas.values():
        for first_antenna in values:
            for second_antenna in values:
                antinode = get_antinode(data, first_antenna, second_antenna)
                if antinode:
                    antinodes.add(antinode)
    return len(antinodes)


def part_2(data: dict[complex, str]) -> int:
    antennas = get_antennas(data)
    antinodes = set()
    for values in antennas.values():
        for first_antenna in values:
            antinodes.add(first_antenna)
            for second_antenna in values:
                antinodes.update(get_antinodes(data, first_antenna, second_antenna))
    return len(antinodes)


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
