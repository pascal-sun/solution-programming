from collections import defaultdict
from pathlib import Path


def parse_data(data: str) -> dict[int, int]:
    stones = defaultdict(int)  # key: number on the stone, value: how many
    for digit in data.split():
        stones[int(digit)] += 1
    return stones


def get_number_of_stones(stones: dict[int, int], blink: int) -> int:
    for _ in range(blink):
        stones_tmp = stones.copy()
        for stone, count in stones.items():
            if stone == 0:
                stones_tmp[1] += count
                stones_tmp[0] -= count
            elif len(str(stone)) % 2 == 0:
                left = int(str(stone)[:len(str(stone)) // 2])
                right = int(str(stone)[len(str(stone)) // 2:])
                stones_tmp[left] += count
                stones_tmp[right] += count
                stones_tmp[stone] -= count
            else:
                stones_tmp[stone * 2024] += count
                stones_tmp[stone] -= count
        stones = stones_tmp
    count = 0
    for number in stones.values():
        count += number
    return count, len(stones.keys())


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    data = parse_data(data)
    print(get_number_of_stones(data, 73))


if __name__ == "__main__":
    main()
