from collections import Counter
from pathlib import Path

# Parsing
def parse_data(data: str):
    left_list = []
    right_list = []
    for line in data.split("\n"):
        left, right = map(int, line.split("   "))
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list


# Part 1
def get_total_distance(left_list: list[int], right_list: list[int]) -> int:
    return sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list)))


# Part 2
def get_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    counter = Counter(right_list)
    return sum(left * counter[left] for left in left_list)


def main():
    # Parsing
    data = Path("input").read_text(encoding="utf-8")
    left_list, right_list = parse_data(data)

    # Part 1
    print(f"Part 1:{get_total_distance(left_list, right_list)}")
    # Part 2
    print(f"Part 2:{get_similarity_score(left_list, right_list)}")


if __name__ == "__main__":
    main()
