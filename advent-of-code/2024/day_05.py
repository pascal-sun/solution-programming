from __future__ import annotations

from collections import defaultdict
from pathlib import Path

type Rules = dict[int, set[int]]
type Update = list[int]
type Updates = list[Update]


def parse_data(data: str) -> tuple[Rules, Updates]:
    rules_data, updates_data = data.split("\n\n")
    # Rules
    rules = defaultdict(set)
    for rule in rules_data.splitlines():
        x, y = map(int, rule.split("|"))
        rules[x].add(y)
    # Updates
    updates = [list(map(int, update.split(","))) for update in updates_data.splitlines()]
    return rules, updates


def is_correctly_ordered(rules: Rules, update: Update) -> tuple[bool, int | None]:
    already_seen = set()
    for page in update:
        for rule in rules[page]:
            if rule in already_seen:
                return False, page
        already_seen.add(page)
    return True, None


def part_1(rules: Rules, updates: Updates) -> int:
    result = 0
    for update in updates:
        if is_correctly_ordered(rules, update)[0]:
            result += update[len(update) // 2]
    return result


def part_2(rules: Rules, updates: Updates) -> int:
    result = 0
    for update in updates:
        is_correct = True
        tmp = update[:]
        while not is_correctly_ordered(rules, tmp)[0]:
            is_correct = False
            page_index = tmp.index(is_correctly_ordered(rules, tmp)[1])
            # Switch page with previous one
            tmp[page_index], tmp[page_index - 1] = tmp[page_index - 1], tmp[page_index]
        if not is_correct:
            result += tmp[len(tmp) // 2]
    return result


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    rules, updates = parse_data(data)
    print(f"Part 1: {part_1(rules, updates)}")
    print(f"Part 2: {part_2(rules, updates)}")


if __name__ == "__main__":
    main()
