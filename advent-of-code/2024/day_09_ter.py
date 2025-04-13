from __future__ import annotations

from collections import deque
from pathlib import Path


def parse_data(data: str) -> list[tuple[int, int | str]]:
    files = deque()
    spaces = deque()
    for i, digit in enumerate(data):
        if i % 2 == 0:
            files.append((int(digit), i // 2))  # (size, index)
        else:
            spaces.append(int(digit))  # size
    return files, spaces


def get_file(files):
    return files.popleft()


def get_space(spaces):
    return spaces.popleft()


def get_file_by_space(files, spaces, space):
    for i in range(len(files) - 1, -1, -1):
        size, index = files[i]
        if size <= space:
            del files[i]
            spaces.insert(i, size)
            return size, index
    return None, None


def part_2(files, spaces):
    result = []
    print("-------------------")
    print(files)
    print(spaces)
    print(result)
    old_data = True
    while True:
        if old_data:
            size, index = files.popleft()
            result.extend([index for _ in range(size)])
            print("-------------------OLD_DATA")
            print(files)
            print(spaces)
            print(result)
            old_data = False  # have some space
        else:
            space = spaces.popleft()
            moved_size, moved_index = get_file_by_space(files, spaces, space)
            if moved_size is None and moved_index is None:
                result.extend(["." for _ in range(space)])
                old_data = True
                print("-------------------NEW_DATA (.)")
                print(files)
                print(spaces)
                print(result)
                continue
            result.extend([moved_index for _ in range(moved_size)])
            space -= moved_size
            if space:
                spaces.appendleft(space)
                old_data = False  # Still have space
                print("-------------------NEW_DATA")
                print(files)
                print(spaces)
                print(result)
            else:
                old_data = True
                print("-------------------NEW_DATA")
                print(files)
                print(spaces)
                print(result)


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    files, spaces = parse_data(data)
    print(files)
    print(spaces)
    get_file_by_space(files, spaces, 1)
    print(files)
    print(spaces)
    print()
    part_2(files, spaces)


if __name__ == "__main__":
    main()
