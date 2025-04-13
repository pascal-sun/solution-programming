from pathlib import Path


def parse_data(data: str) -> dict[complex, str]:
    garden = {}
    for i, line in enumerate(data.splitlines()):
        for j, square in enumerate(line):
            garden[complex(i, j)] = square
    return garden


def part_1(garden: dict[complex]):
    data = {}
    for position, plant in garden.items():
        if plant not in data:
            data[plant] = {"area": 1, "perimeter": 0}
        else:
            data[plant]["area"] += 1
        for direction in [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]:
            if position + direction not in garden or garden[position + direction] != plant:
                data[plant]["perimeter"] += 1
    count = 0
    for values in data.values():
        count += values["area"] * values["perimeter"]
    print(data)
    return count


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    print(data)
    print(part_1(data))


if __name__ == "__main__":
    main()
