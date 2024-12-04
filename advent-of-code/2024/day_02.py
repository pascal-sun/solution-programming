from pathlib import Path


# Parsing
def parse_data(data: str) -> list[list[int]]:
    return [list(map(int, line.split())) for line in data.splitlines()]


# Helper
def is_sorted(levels: list[int]) -> bool:
    return bool(levels == sorted(levels) or levels == sorted(levels, reverse=True))


def is_between_one_and_three(levels: list[int]) -> bool:
    diff_levels = [abs(previous_level - next_level) for previous_level, next_level in zip(levels[:-1], levels[1:])]
    return all(1 <= x <= 3 for x in diff_levels)


# Part 1
def part_1(reports: list[list[int]]) -> int:
    return sum(1 for levels in reports if is_between_one_and_three(levels) and is_sorted(levels))


# Part 2
def part_2(reports: list[list[int]]) -> int:
    results = 0
    for levels in reports:
        if is_sorted(levels) and is_between_one_and_three(levels):
            results += 1
        else:
            for i in range(len(levels)):
                tmp = levels[:]
                tmp.pop(i)
                if is_sorted(tmp) and is_between_one_and_three(tmp):
                    results += 1
                    break
    return results


def main() -> None:
    # Parsing
    data = Path("input").read_text(encoding="utf-8")
    reports = parse_data(data)

    # Part 1
    print(f"Part 1: {part_1(reports)}")

    # Part 2
    print(f"Part 2: {part_2(reports)}")


if __name__ == "__main__":
    main()
