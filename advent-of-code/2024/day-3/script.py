import re
from pathlib import Path


# Part 1
def part_1(data: str) -> int:
    numbers = re.findall(r"mul\((\d+),(\d+)\)", data)
    return sum(int(x) * int(y) for x, y in numbers)


# Part 2
def part_2(data: str) -> int:
    data = re.sub(r"don't\(\).*?do\(\)", "", data, flags=re.DOTALL)
    data = re.sub(r"don't\(\).*?$", "", data)
    numbers = re.findall(r"mul\((\d+),(\d+)\)", data)
    return sum(int(x) * int(y) for x, y in numbers)


def main() -> None:
    # Parsing
    data = Path("input").read_text(encoding="utf-8")

    # Part 1
    print(f"Part 1: {part_1(data)}")

    # Part 2
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
