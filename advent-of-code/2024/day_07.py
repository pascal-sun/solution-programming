from pathlib import Path

type EQUATION = tuple[int, list[int]]
type EQUATIONS = list[EQUATION]


def parse_data(data: str) -> EQUATIONS:
    results = []
    for line in data.splitlines():
        test_value, numbers_data = line.split(": ")
        numbers = list(map(int, numbers_data.split()))
        results.append((int(test_value), numbers))
    return results


def get_calibration_result(data: EQUATIONS, operations: list) -> int:
    count = 0
    for test_value, numbers in data:
        results = set()
        for number in numbers:
            if len(results) == 0:
                results.add(number)
                continue
            new_results = set()
            for result in results:
                for operation in operations:
                    new_result = operation(result, number)
                    if new_result <= test_value:
                        new_results.add(new_result)
            results = new_results
        if test_value in results:
            count += test_value
    return count


def part_1(data: EQUATIONS) -> int:
    return get_calibration_result(data, [lambda x, y: x + y, lambda x, y: x * y])


def part_2(data: EQUATIONS) -> int:
    return get_calibration_result(data, [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(f"{x}{y}")])


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    # print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
