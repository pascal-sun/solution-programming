from __future__ import annotations

from pathlib import Path


def parse_data(data: str) -> list[tuple[int, int | str]]:
    disk_map = []  # list of tuple, (size, index or .)
    for i, digit in enumerate(data):
        if i % 2 == 0:
            disk_map.append((int(digit), i // 2))
        else:
            disk_map.append((int(digit), "."))
    return disk_map


def disk_map_to_string(disk_map: list[tuple[int, int | str]]) -> str:
    result = ""
    for size, index in disk_map:
        result += size * str(index)
    return result


def part_2(disk_map: list[tuple[int, int | str]]) -> int:
    for space_cursor in range(len(disk_map)):  # Cursor for space
        space_size, space_index = disk_map[space_cursor]
        if space_index != ".":
            continue
        for file_cursor in range(len(disk_map) - 1, space_cursor - 2, -1):  # Cursor for file
            file_size, file_index = disk_map[file_cursor]
            if file_index == ".":
                continue
            if file_size > space_size:
                continue
            disk_map[file_cursor] = (file_size, ".")
            disk_map[space_cursor] = (file_size, file_index)
            if file_size < space_size:  # still have space
                disk_map.insert(space_cursor + 1, (space_size - file_size, "."))
            break
    checksum = 0
    disk_map = disk_map_to_string(disk_map)
    for space_cursor, data in enumerate(disk_map):
        if data == ".":
            continue
        checksum += space_cursor * int(data)
    return checksum


# C'est pas 85700128633
# C'est pas 85693733092
# C'est pas 85693733348
def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    disk_map = parse_data(data)
    print(f"Part 2: {part_2(disk_map)}")


if __name__ == "__main__":
    main()
