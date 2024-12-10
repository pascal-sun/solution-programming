from pathlib import Path

LOWEST_POSITION = 0
HIGHEST_POSITION = 9


def parse_data(data: str) -> dict[complex, int]:
    map_ = {}
    for y, row in enumerate(data.splitlines()):
        for x, cell in enumerate(row):
            map_[complex(x, y)] = int(cell) if cell.isdigit() else float("inf")
    return map_


def get_lowest_positions(data: dict[complex, int]) -> list[complex]:
    starts = []
    for position, cell in data.items():
        if cell == LOWEST_POSITION:
            starts.append(position)
    return starts


def find_trailheads(data: dict[complex, int], position: complex) -> tuple[set[complex], int]:
    if data[position] == HIGHEST_POSITION:
        return {position}, 1
    highest_positions = set()
    distinct_trails_number = 0
    for direction in [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]:
        if position + direction not in data or data[position + direction] != data[position] + 1:
            continue
        highest_position, distinct_trail_number = find_trailheads(data, position + direction)
        highest_positions.update(highest_position)
        distinct_trails_number += distinct_trail_number
    return highest_positions, distinct_trails_number


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    part_1 = 0
    part_2 = 0
    for lowest_position in get_lowest_positions(data):
        highest_positions, distinct_trails_number = find_trailheads(data, lowest_position)
        part_1 += len(set(highest_positions))
        part_2 += distinct_trails_number
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
