from pathlib import Path


def parse_data(data: str) -> list[list[str]]:
    results = [list(line) for line in data.splitlines()]
    return results


def part_1(data: list[str]) -> bool:
    results = 0
    for y, data_row in enumerate(data):
        for x, data_cell in enumerate(data_row):
            if data_cell != "X":
                continue
            checks = [
                # Row
                [(y + 0, x + 1), (y + 0, x + 2), (y + 0, x + 3)],
                [(y + 0, x - 1), (y + 0, x - 2), (y + 0, x - 3)],
                # Column
                [(y + 1, x + 0), (y + 2, x + 0), (y + 3, x + 0)],
                [(y - 1, x + 0), (y - 2, x + 0), (y - 3, x + 0)],
                # Diag 1
                [(y + 1, x + 1), (y + 2, x + 2), (y + 3, x + 3)],
                [(y - 1, x - 1), (y - 2, x - 2), (y - 3, x - 3)],
                # Diag 2
                [(y - 1, x + 1), (y - 2, x + 2), (y - 3, x + 3)],
                [(y + 1, x - 1), (y + 2, x - 2), (y + 3, x - 3)]
            ]
            for check in checks:
                m_y, m_x = check[0]
                a_y, a_x = check[1]
                s_y, s_x = check[2]
                if m_y < 0 or m_x < 0:
                    continue
                if a_y < 0 or a_x < 0:
                    continue
                if s_y < 0 or s_x < 0:
                    continue
                try:
                    if data[m_y][m_x] == "M" and data[a_y][a_x] == "A" and data[s_y][s_x] == "S":
                        results += 1
                except:
                    pass
    return results


def part_2(data: list[str]) -> bool:
    results = 0
    for y, data_row in enumerate(data):
        for x, data_cell in enumerate(data_row):
            if data_cell != "A":
                continue
            if y - 1 < 0 or x - 1 < 0:
                continue
            try:
                a = data[y - 1][x - 1]
                b = data[y - 1][x + 1]
                d = data[y + 1][x - 1]
                c = data[y + 1][x + 1]
                if a == b == "M" and c == d == "S":
                    results += 1
                if a == d == "M" and b == c == "S":
                    results += 1
                if a == b == "S" and c == d == "M":
                    results += 1
                if a == d == "S" and b == c == "M":
                    results += 1
            except:
                pass
    return results


def main() -> None:
    # Parsing
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    print(data)

    # Part 1
    print(f"Part 1: {part_1(data)}")

    # Part 2
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
